import re
import speech_recognition as sr

r = sr.Recognizer()
r.dynamic_energy_threshold = False

def check_input(text):
    ## Sprawdzanie wprowadzonego polecenia wg kryteriów
    if text is not None and len(text) == 4:
        if re.match("(^[a-hA-H)])([1-8])([a-hA-H])([1-8])", text):
            return 0
        else:
            return 1
    else:
        return 2

def get_pos(BOARD, player_name):
    with sr.Microphone() as source:
        try:
            BOARD.display_text(f'{player_name} podaj ruch')
            audio = r.listen(source, timeout=5)
            text = r.recognize_google(audio, language='pl-PL')
            move = ""
            for char in str(text):
                if char != " ":
                    move += char
            check_val = check_input(move)
            if check_val == 0:
                print(f"Wszystko ok. {move}")
                return move.lower()
            elif check_val == 1:
                print(f"Nie ma takiego pola {text}")
            else:
                print(f"Zła długośc ruchu {text}")
        except:
            pass

if __name__ == "__main__":
    print(get_pos())
