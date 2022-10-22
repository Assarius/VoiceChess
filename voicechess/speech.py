import re
import speech_recognition as sr
# import game

r = sr.Recognizer()
r.dynamic_energy_threshold = False

def checkChar(txt):
    ## Sprawdzanie wprowadzonego polecenia wg kryteriów
    if txt is not None and len(txt) == 4:
        if re.match("(^[a-hA-H)])([1-8])([a-hA-H])([1-8])", txt):
            return 0
        else:
            return 1
    else:
        return 2

def get_pos():
    with sr.Microphone() as source:
        try:
            print("Podaj ruch jaki chcesz wykonać")
            audio = r.listen(source, timeout=5)
            text = r.recognize_google(audio, language='pl-PL')
            move = ""
            for char in str(text):
                if char != " ":
                    move += char
            check_val = checkChar(move)
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
