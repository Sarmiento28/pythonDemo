
#sample text-based game with simple conditional statement
character_health = 100
buzz_health = 120
crak_health = 110
item = ""
import random

name = input("Enter your name: ")
print("Hello " + name)

while character_health > 0:

    if character_health != 100 and item == "Fish":
        n = input("You have taken some damage to heal select [1 to heal/ 0 to ignore]")
        if n == "1":
            character_health += 10
            print("Your character's health is back to " + str(character_health))
        else :
             print("Your character's health is back to " + str(character_health))

    elif  character_health != 100 and item == "Athena Shield":
                n = input("You have chance to heal!! using your:" + item + "! \n" + "[press 1 to heal]")
                if n == "1":
                    character_health += 100
                    print("Character health + 100! \n" + "Your Character Health is now: " + str(character_health))


  

    v = int(input("Choose 1 if you want to cross the river\nChoose 2 if you want to jump on the ravine\nChoose 3 if you want to fight monster in the dungeon \nInput: "))
   
    #Start of Journey
    if v == 1: 
        choice = input("If you want to go fishing select [1 for yes/ 0 for no]")
        if choice == "1":
            #Fishing minigame
            print("You have chosen Fishing! ")
            chance = random.randint(0,9)
            if chance > 6:
                item = "Fish"
                print("You have catch a Fish!")
            else:
                print("There is no fish to catch")

        elif choice == "0":
            print("You have crossed the river")


    elif v == 2:
        #damages the player
        print("You have jumped into the ravine")
        print("Your character has taken 10pt of damage")
        character_health = character_health - 10

    elif v == 3:
    
        #damages the player
        print("You have enter the dungeon")
        #monster attack
        chance = random.randint(0,9)
        if chance > 5:
            
            print ("A Crak Appeared !!!")
            choice = input("Fight the The Crack! \n \t [1 to fight using your Basic attack and 0 for to fight using your Skills]")
            if choice == "1":
                print ("You dealt normal damage using your basic attack! Crak taken -20hp")
                print ("Your Character taken some damage from the Crak! -20")
                character_health -= 20
                crak_health -= 20
                print ("crak Health: " + str (crak_health))
            elif choice == "0":
                print ("You dealt critical damages using your Special Skill attack! Crak taken -60hp")
                print ("Your Character taken some damage from the Crak! -20")
                character_health -= 20
                crak_health -= 60
                print ("crak Health: " + str (crak_health))

            if crak_health <= 0:
                print("you have sucessfully deafeated the Crak! and gain new item! ")
                item = "Haas claw"
                print("You have found " + item + "!\n")
               
        else:
            print ("An buzz appeared!")
            choice =  input("Fight the Buzz! \n \t [1 to Fight using your Axe, or 0 to Fight using your Sword]")
            if choice == "1":
                print ("you faught using your axe! Buzz taken -50hp")
                print ("your character taken some damage from the attack of the Buzz! -30hp")
                character_health -= 30
                buzz_health -= 50
                print ("Buzz Health: " + str (buzz_health))
            elif choice == "0":
                item = "Smooth Love Potion"
                print ("you fought using your axe! Buzz taken -20hp")
                print ("your character taken some damages from the attack of the Buzz! -30hp")
                character_health -= 30
                buzz_health -= 20
                print("Buzz Health:" + str(buzz_health))

                
            if buzz_health <= 0:
                print("you have sucessfully deafeated the Buzz! and gain new item! ")
                item = "Athena Shield"
                print ("You have found " + item + "! \n")
                print ("Your character is leveling up!")

           

                

           
        

    else:
        print("Invalid input")

    print("Your character's Health: " + str(character_health))

print("Your Character is dead!")
