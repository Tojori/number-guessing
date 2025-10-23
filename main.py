import random

def main():
    Versuche = 0

    print("Herzlich Wilkommen! \nIn diesem Spiel geht es darum eine Zahl zwischen 0 und 100 zu erraten. \nDoch achtung dir stehen nur eine Begrenzte Anzahl an Antworten zur verfügung. Nach jeder antwort sagt dir der Computer ob du höher oder tiefer als die gesuchte zahl bist. Wenn du es schaffst innerhalb deiner Versuche die Zahl zu erraten Gewinnst du andernfals Verlierst du. \nDamit Währe alles erklärt Suche jetzt deine Schwierigkeit aus und viel Spaz beim spielen.\n")
    while Versuche == 0:
        Schwierigkeit = input("Tippe 1, 2 oder 3 um deine Schwierigkeit zu wählen. \n1. Einfach (10 Versuche)\n2. Mittel (5 Versuche)\n3. Schwer (3 Versuche)\nSchwierigkeit: ")

        if Schwierigkeit == "1":
            Versuche = 10
        
        elif Schwierigkeit == "2":
            Versuche = 5

        elif Schwierigkeit == "3":
            Versuche = 3
    print("\n")
    ges_zahl = random.randint(0, 100)
    while Versuche > 0:
        Antwort = input(f"Du hast noch {Versuche} übrig Welche Zahl wird gesucht? ")
        try:
            Zahl_Antwort = int(Antwort)

            if Zahl_Antwort == ges_zahl:
                break
            
            elif Zahl_Antwort > ges_zahl:
                print("Die Gesuchte Zahl ist kleiner.\n")
            
            elif Zahl_Antwort < ges_zahl:
                print("Die Gesuchte Zahl ist größer.\n")
            
            Versuche -= 1

        except:
            pass
    
    if Versuche <= 0:
        print("Schade die Zahl wurde nicht gefunden villeicht kapt es ja nächstes mal.")
    
    else:
        print("Herzlichen Glückwunsch du hast die Zahl gefunden.")






if __name__ == "__main__":
    main()
