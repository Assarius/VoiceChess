from collections import namedtuple
from itertools import count

from . import sunfish as sf

class Position(namedtuple('Position', 'board score wc bc ep kp')):
    def gen_moves(self):
        for i, p in enumerate(self.board):
            if not p.isupper(): continue
            for d in sf.directions[p]:
                for j in count(i+d, d):
                    q = self.board[j]
                    if q.isspace() or q.isupper(): break
                    if p == 'P' and d in (sf.N, sf.N+sf.N) and q != '.': break
                    if p == 'P' and d == sf.N+sf.N and (i < sf.A1+sf.N or self.board[i+sf.N] != '.'): break
                    if p == 'P' and d in (sf.N+sf.W, sf.N+sf.E) and q == '.' \
                            and j not in (self.ep, self.kp, self.kp-1, self.kp+1): break
                    yield (i, j)
                    if p in 'PNK' or q.islower(): break
                    if i == sf.A1 and self.board[j+sf.E] == 'K' and self.wc[0]: yield (j+sf.E, j+sf.W)
                    if i == sf.H1 and self.board[j+sf.W] == 'K' and self.wc[1]: yield (j+sf.W, j+sf.E)
    def rotate(self):
        return Position(self.board[::-1].swapcase(), -self.score, self.bc, self.wc,
                        119-self.ep if self.ep else 0, 119-self.kp if self.kp else 0)
    def nullmove(self):
        return Position(self.board[::-1].swapcase(), -self.score, self.bc, self.wc, 0, 0)
    def move(self, move):
        i, j = move
        p, q = self.board[i], self.board[j]
        put = lambda board, i, p: board[:i] + p + board[i+1:]
        board = self.board
        wc, bc, ep, kp = self.wc, self.bc, 0, 0
        score = self.score + self.value(move)
        board = put(board, j, board[i])
        board = put(board, i, '.')
        if i == sf.A1: wc = (False, wc[1])
        if i == sf.H1: wc = (wc[0], False)
        if j == sf.A8: bc = (bc[0], False)
        if j == sf.H8: bc = (False, bc[1])
        if p == 'K':
            wc = (False, False)
            if abs(j-i) == 2:
                kp = (i+j)//2
                board = put(board, sf.A1 if j < i else sf.H1, '.')
                board = put(board, kp, 'R')
        if p == 'P':
            if sf.A8 <= j <= sf.H8: board = put(board, j, 'Q')
            if j - i == 2*sf.N: ep = i + sf.N
            if j == self.ep: board = put(board, j+sf.S, '.')
        return Position(board, score, wc, bc, ep, kp).rotate()
    def value(self, move):
        i, j = move
        p, q = self.board[i], self.board[j]
        score = sf.pst[p][j] - sf.pst[p][i]
        if q.islower(): score += sf.pst[q.upper()][119-j]
        if abs(j-self.kp) < 2: score += sf.pst['K'][119-j]
        if p == 'K' and abs(i-j) == 2:
            score += sf.pst['R'][(i+j)//2]
            score -= sf.pst['R'][sf.A1 if j < i else sf.H1]
        if p == 'P':
            if sf.A8 <= j <= sf.H8: score += sf.pst['Q'][j] - sf.pst['P'][j]
            if j == self.ep: score += sf.pst['P'][119-(j+sf.S)]
        return score
Entry = namedtuple('Entry', 'lower upper')
class Searcher:
    def __init__(self):
        self.tp_score = {}
        self.tp_move = {}
        self.history = set()
    def bound(self, pos, gamma, depth, root=True):
        depth = max(depth, 0)
        if pos.score <= -sf.MATE_LOWER: return -sf.MATE_UPPER
        if not root and pos in self.history: return 0
        entry = self.tp_score.get((pos, depth, root), Entry(-sf.MATE_UPPER, sf.MATE_UPPER))
        if entry.lower >= gamma and (not root or self.tp_move.get(pos) is not None):
            return entry.lower
        if entry.upper < gamma: return entry.upper
        def moves():
            if depth > 0 and not root and any(c in pos.board for c in 'RBNQ'):
                yield None, -self.bound(pos.nullmove(), 1-gamma, depth-3, root=False)
            if depth == 0: yield None, pos.score
            killer = self.tp_move.get(pos)
            if killer and (depth > 0 or pos.value(killer) >= sf.QS_LIMIT):
                yield killer, -self.bound(pos.move(killer), 1-gamma, depth-1, root=False)
            for move in sorted(pos.gen_moves(), key=pos.value, reverse=True):
                if depth > 0 or pos.value(move) >= sf.QS_LIMIT:
                    yield move, -self.bound(pos.move(move), 1-gamma, depth-1, root=False)
        best = -sf.MATE_UPPER
        for move, score in moves():
            best = max(best, score)
            if best >= gamma:
                if len(self.tp_move) > sf.TABLE_SIZE: self.tp_move.clear()
                self.tp_move[pos] = move
                break
        if best < gamma and best < 0 and depth > 0:
            is_dead = lambda pos: any(pos.value(m) >= sf.MATE_LOWER for m in pos.gen_moves())
            if all(is_dead(pos.move(m)) for m in pos.gen_moves()):
                in_check = is_dead(pos.nullmove())
                best = -sf.MATE_UPPER if in_check else 0
        if len(self.tp_score) > sf.TABLE_SIZE: self.tp_score.clear()
        if best >= gamma: self.tp_score[pos, depth, root] = Entry(best, entry.upper)
        if best < gamma: self.tp_score[pos, depth, root] = Entry(entry.lower, best)
        return best
    def search(self, pos, history=()):
        self.history = set(history)
        self.tp_score.clear()
        for depth in range(1, 1000):
            lower, upper = -sf.MATE_UPPER, sf.MATE_UPPER
            while lower < upper - sf.EVAL_ROUGHNESS:
                gamma = (lower+upper+1)//2
                score = self.bound(pos, gamma, depth)
                if score >= gamma: lower = score
                if score < gamma: upper = score
            self.bound(pos, lower, depth)
            yield depth, self.tp_move.get(pos), self.tp_score.get((pos, depth, True)).lower
