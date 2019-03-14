print("Du stehst vor einem Gang. Was machst du?")

entscheidung1 = input("Wähle links [L] oder rechts [R]: ")

if entscheidung1 == "L":
    print("Du findest einen Schatz!")
    print("Wie willst du den Schatz ausgeben?")
    entscheidung2 = input("Sparen [S] oder Party [P]: ")
    if entscheidung2 == "S":
        print("Du häufst ein Vermögen an!")
    elif entscheidung2 == "P":
        print("Die Party gerät außer Kontrolle!! Du verarmst!")
    else:
        print("Du hast keine Option gewählt. Ende.")
    
elif entscheidung1 == "R":
    print("Du stirbst!")
else:
    print("TU ETWAS!")


