z1 = "/"
z2 = "\\"
w1 = "Donau"

def donau():
    for i in range(2857): #gesamtlänge der Donau
        print(z1*20)
        print(z2*20)
        print(z1*20)
        print(z2*20)
        print(z1*5+" ".join(w1)+z1*5)
        print(z2*20)
        print(z1*20)
        print(z2*20)
        print(z1*20)
