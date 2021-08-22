import random as random

def generateRandomNumber():
    random_number = 0
    while True:
        random_number = random.randint(100,999)
        random_number_str = str(random_number)
        if random_number_str[0] == random_number_str[1] or random_number_str[0] == random_number_str[2] or random_number_str[1] == random_number_str[2] :
            continue
        else:
            return random_number_str
def checkNumber(random_number_str,user_number):

    my_list = list()
    for index in range(3):
        my_list.append(random_number_str[index])
    for index in range(3):
        if(int(user_number)==int(random_number_str)):
            print("Match")
            return
        if(user_number[index] in my_list):
            print("Close")
            return
    print("Nope")
        
    
    
print("Welcome to the number,Guessing Game!")
print("The number has been generated, please follow the instruction")
print("Rule of the game:\n1: close:you guess at least 1 number correct but in the wrong postion\n2:Nope:you have not guess any number correct\n3.Match: You guess all 3 numbers correct")
computer_number = generateRandomNumber()
count = 0



while(True):

    # print(computer_number)
    user_input = input("Guess the number?")
    checkNumber(computer_number, user_input)
    if user_input == computer_number:
        break
    count +=1


print(f"You have won the game in {count} trie/s")
