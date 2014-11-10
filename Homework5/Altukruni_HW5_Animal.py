#Abdulhalim Altukruni
#Python programming
#homework 5 program1


class Animal:
    def __init__(self, name):
        self.name = name

    def guess_who_am_i(self):
        x = 1
        for hint in (Dicthit[self.name]):
            print ("\nHint "+str(x)+". "+hint)
            answer = input ("Who am I?:")
            if answer == self.name:
                print ("\nYou got it! I am a " +self.name)
                break
            else:
                print ("\nnope, try again! ")
                x +=1
            if x > 3:
                print ("\nSorry, the answer is "+self.name)
            
print ("\n Weclome to guess the animal game")

print ("\n I will give you 3 hints, and you try to guess who am I")


Dicthit = {"tiger":["I am the biggest cat", "I come in black and white or orange and black", "I am a carnivore"],"elephant":["I have exceptional memory", "I am the largest land-living mammal in the world","I have a trunk"],
"bat":["I use echo-location", "I can fly", "I see well in dark"]}
t = Animal("tiger")
e = Animal("elephant")
b = Animal("bat")


t.guess_who_am_i()


e.guess_who_am_i()


b.guess_who_am_i()
