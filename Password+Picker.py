import random
import string
# The following imports above allow strings and random things to generate

# The following list contains fifteen adjectives
adjectives = ['silly','crazy','purple','stanky','frantic','green','futuristic','spooky','snowy','blue','yellow','sticky','runny','pink','red']
# The following list contains fifteen nouns
nouns = ['Francis','School','Prison','FortniteBattlePass','Yeast','Bread','Sam','Superhero','Battlefield','Soldier','Villian','Asylum','Course','Music','Ball']
# The follwoing list contains fifteen numbers
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# The following list contains fifteen special characters
special_characters = ['@','$',':','?','&','#','*','%','!','/','+','-','_','`','~']
number_of_passwords = None

print("Welcome to the Password Picker Python Program!")
number_of_passwords = int(input("Please enter the amount of passwords you would like:\n"))
# The int above lets you be able to choose how many passwords you would like


# This makes it to where the random import will print out random things for a password
while True:

#This range helps for if you want 3 different passwords shown
    for num in range(number_of_passwords):
        adjective = random.choice(adjectives)
        noun = random.choice(nouns)
        number = random.randrange(0, 15)
        special_character = random.choice(special_characters)

#This helps show what the new passowrd is
        password = adjective + noun + str(number) + special_character
        print("Your new password is: %s " % password)

# This help determine if someone wants a new password generated or not
    response = input("\nWould you like another password? Type y or n: \n").lower()
    if response == 'n':
        break
    number_of_passwords = int(input("Please enter the amount of passwords you would like:\n"))
    
   
