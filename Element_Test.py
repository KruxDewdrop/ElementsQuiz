import numpy as np
print("Hello, this is a test to determine your magical element.")
print("Think of it like a fun game. Answering this question is quite difficult though.")
print("Personality, heritage, metaphysical influences, etc. There are a number of different variables that could point to wildly differing elemental affinities.")
print("Worse yet, outside the standard four(five) elements, there are also the eastern ones as well as incarnations to think about.")
print("Then there are the rare and outlying elements which are even more unusual...")
print("Through this quiz, I will ask you to respond with one of the listed options. However, do not let that stop you from freely answering however you like.")
##Determine Element, Circuit Quality, Quantity, Origin, and field of Magecraft
Waterv = 0
Firev = 0
Earthv = 0
Airv = 0
Woodv = 0
Metalv = 0
Voidv = 0
Blankv = 0
print("So to get started, I will ask you a few questions.")
print("What is your western sign? Since birth can play a part in determining your element, I have included it. An example would be leo or scorpio.")
Wsign = input("Enter your western zodiac sign: ").lower() 
if Wsign == "taurus" or Wsign == "virgo" or Wsign== "capricorn":
        Earthv += 1
elif Wsign == "aries" or Wsign == "leo" or Wsign == "sagittarius":
        Firev += 1
elif Wsign == "gemini" or Wsign == "libra" or Wsign == "aquarius":
        Airv += 1
elif Wsign == "cancer" or Wsign == "scorpio" or Wsign == "pisces":
        Waterv += 1
else:
        Blankv += 1
print("First question down, good job!")
print("Next one, what animal is your chinese zodiac? If you don't know, just google your birthday and you should get an element and an animal.")
Esign = input("Enter the animal you got: ").lower()
if Esign == "rabbit" or Esign == "tiger":
    Woodv += 1
elif Esign == "snake" or Esign == "horse":
    Firev += 1
elif Esign == "ox" or Esign == "dragon" or Esign == "goat" or Esign == "dog":
    Earthv +=1
elif Esign == "monkey" or Esign == "rooster":
    Metalv += 1
elif Esign == "pig" or Esign == "rat":
    Waterv += 1
else:
    Blankv += 1
print("Ok, now that you put the animal, now it's time for the element.")
Ell = input("now put the element you got that corresponds to your chinese zodiac: ").lower()
if Ell == "metal":
    Metalv += 2
    Airv += 1
elif Ell == "fire":
    Firev += 1
elif Ell == "wood":
    Woodv += 2
elif Ell == "earth":
    Earthv +=2
elif Ell == "water":
    Waterv += 2
else:
    Blankv += 1
print("MBTI time")
mbti = input("Tell me, what myers briggs personality are you?: ").lower()
if mbti == "istp" or mbti == "entj" or mbti == "estp" or mbti == "entp":
    Firev += 1
elif mbti == "enfp" or mbti == "esfp" or mbti == "intp" or mbti == "isfp":
    Airv += 2
    Metalv += 1
elif mbti == "infj" or mbti == "esfj" or mbti == "infp" or mbti == "enfj":
    Waterv += 2
    Woodv += 1
elif mbti == "estj" or mbti == "istj" or mbti == "intj" or mbti == "isfj":
    Earthv +=1
else:
    Blankv += 1
print ("Now, what would you rather have?")
WeSk = input("Large amounts of wealth, allowing you to freely buy what you need or want, or would you rather be extremely skilled in the areas of your choice? Wealth to gain skills or skills to gain wealth? Or perhaps you would rather live freely and see how the dice fall? Answer thus, Wealth, Skill, or Neither: ").lower()
if WeSk == "wealth":
    Woodv += 3
elif WeSk == "skill":
    Metalv += 3
elif WeSk == "neither":
    Voidv += 3
else:
    Blankv += 1
print("Pick a skill: Mana Burst, Reinforcement, Alteration, or Projection?")
skillt = input("").lower
if skillt == "mana burst":
    Firev += 1
    Metalv += 1
elif skillt == "reinforcement":
    Earthv += 1
    Woodv += 1
elif skillt == "alteration":
    Waterv += 2
elif skillt == "projection":
    Airv+= 1
else:
    Blankv += 1
print("What sensation feels the best on your skin? Windy, Hot, Damp, Dry, or Cold?")
sen = input("").lower()
if sen == "windy":
    Woodv += 2
    Airv += 1
elif sen == "hot":
    Firev += 1
    Voidv += 1
elif sen == "damp":
    Earthv += 2
    Waterv += 1
elif sen == "dry":
    Metalv += 2
    Earthv += 1
elif sen == "cold":
    Waterv += 2
    Voidv += 3
else:
    Blankv += 1
print("Do you you have any of these animals as pets? Bird, Dog, Cat, Lizard, Or a Rabbit? Or are you more a plant person? If you have more than one, choose your favorite, or if you have none, just type none.")
pet = input("").lower()
if pet == "bird":
    Airv += 1
elif pet == "dog":
    Earthv += 1
    Metalv += 1
elif pet == "cat":
    Earthv += 1
elif pet == "lizard":
    Firev += 2
    Earthv += 1
    Waterv += 1
elif pet == "rabbit":
    Woodv += 2
    Earthv += 1
    Voidv += 1
elif pet == "plant":
    Woodv += 3
    Waterv += 1
    Earthv += 1
elif pet == "none":
    Voidv += 1
else:
    Blankv += 1
print("What blood type are you? Please include the +/- after. An example: A+")
bl = input("").lower()
if bl == "o+":
    Firev += 1
    Metalv += 1
elif bl == "o-":
    Firev += 1
    Metalv += 1
    Voidv += 4
elif bl == "a+" or bl == "a-":
    Woodv += 1
    Earthv += 1
elif bl == "b+" or bl == "b-":
    Woodv += 1
    Waterv += 1
elif bl == "ab+":
    Waterv += 2
    Earthv += 2
elif bl == "ab-":
    Voidv += 4
else:
    Blankv += 1
print("This next question requires a little bit of history. Is your family closely related to any of these elements? Water, Wind, Fire, Earth, Wood, Metal, Mathmatics or none?")
fam = input("").lower()
if fam == "water":
    Waterv += 2
elif fam == "wind":
    Airv += 2
elif fam == "fire":
    Firev += 2
elif fam == "earth":
    Earthv += 2
elif fam == "wood":
    Wood += 2
elif fam == "metal":
    Metalv += 2
elif fam =="mathmatics":
    Voidv += 2
elif fam == "none":
    Waterv += 1
    Airv += 1
    Firev += 1
    Earthv += 1
    Woodv += 1
    Metalv += 1
else:
    Blankv += 1
print("Finally, does your family contain any royalty or does it mostly made up of 'common' folk? Just royalty or common will suffice as an answer")
roy = input("").lower()
if roy == "royalty":
    Airv += 2
    Firev += 2
elif roy == "common":
    Earthv += 2
    Woodv += 1
    Waterv += 2
    Metalv += 1
else:
    Blankv += 1
print("That's the main questions out of the way. Now, after taking this quiz, if you were to see the numbers, you would see that some elements come in close second.")
print("What determines if you are able to use more than one element is essentially up to luck. Sorry, but thems the dice.")
print("Not a single person taking this quiz is some sort of culmination of magus family's trying to get the perfect heir.")
print("No, you are the common people wanting to know more about yourselves for your own ends.")
print("Now let's see, are you a prodigy?")
print("Hmmmm.....")
from numpy import random
prod = np.random.randint(0, 100)
if roy == "royalty":
    prod -= ((Airv*.5) + (Firev*.5))
    if prod <= 0:
        prod = .01
    else:
        print("whoops")
elif roy == "common":
    print("Sorry, your blood won't help you here. Still, there's hope...")
print("")
if prod <= 20 and prod > 10:
    print("Well, you're not a prodigy, but you can use two elements, at the very least!")
elif prod <= 10 and prod >5:
    print("Wowza, seems you can use three elements!")
elif prod <= 5 and prod >=1:
    print("Ding ding! You can use a whopping four elements! Nice! Try not to blow up too much stuff with that arsenal!")
elif prod < 1:
    print("... You... You're an actual prodigy! I can't believe it! You'd be quite the catch in the moonlit world, you know.")
elif prod > 20:
    print("Welp, looks like you're a normal magus at best.")
else:
    print("I don't know how to say it, but you seem to have no talent whatsoever. You can't use even a single element, unfortunately. Did I do somehting wrong? Or are you just that bad?")

print("Your Water affinty is " + str(Waterv) )
print("Your Fire affinty is " + str(Firev) )
print("Your Wind affinty is " + str(Airv) )
print("Your Earth affinty is " + str(Earthv))
print("Your Metal affinty is " + str(Metalv) )
print("Your Wood affinty is " + str(Woodv) )
print("Your Void affinty is " + str(Voidv) )
print("??? " + str(Blankv) )
print("Here, I'll help do some tiebreaking. That is of course, if you need it")
tb = input("Yes or No?: ").lower()
if tb == "yes":

    breaker = list()
    tie = input("Enter in the number of elements that were tied and I will tell you which ones you're aligned to and in what order: ").lower()
    print("Enter the elements in question")
    for i in range(int(tie)):
        n = input("Element: ")
        breaker.append((n))
        random.shuffle(breaker)
        print(breaker)
else:
    print("Alright then, your loss.")

incar = np.random.randint(0, 500)
if (Blankv >= 9):
    print("Oh, what's this? It seem's you're a bit of an odd one, aren't you?")
    incar -= (Blankv*20)
else:
    print("Just in case, I want to check something...")
    incar -= (Blankv* 10)
if incar <= 1:
    print("...")
    print("...It can't be...")
    print("You're an incarnation! Forget about element, we need to figure out your origin!")
else:
    print("I guess it was nothing.")
elements = [Waterv, Firev, Earthv, Airv, Metalv, ]
print("I hope you enjoyed this. I'll admit it was short, lacking in elements, and otherswise fallible, but I like to think it can help some.")