import random
from random import randint

verben = ["anbieten", "anfangen", "ankommen", "anrufen", "antworten", "arbeiten",
          "aufhören", "ausruhen", "auswählen", "beenden", "beginnen", "behandeln",
          "benutzen", "berühren", "beschreiben", "besuchen", "bevorzugen", "bewegen",
          "bleiben", "brauchen", "brennen", "rauchen", "telefonieren", "pupsen",
          "rauchen", "töten", "kitzeln", "dominieren"]

Nomen = [["ein Auto, das ", "ein Kind, das ", "ein Katzenbaby, das"],
         ["eine Bank, die", "eine Liebe, die ", "eine Mutter, die"],
         ["einen Vater, der", "einen Hund, der ", "einen Kuss, der"]]

Brot = str(random.choice(random.choice(Nomen)))


for i in range(80):
    sätze = ["Ich will "+str(Brot)+" "+str(random.choice(verben))+" kann!",
             "Ich will "+str(Brot)+" "+str(random.choice(["mich", "dich", "uns", "alles"]))+" "+str(random.choice(verben))+" kann!",]
    for s in sätze:
        print(random.choice(sätze))
