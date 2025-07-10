import random
no_for_words={
     1:"stone",
     0:"paper",
     -1:"scisor"
}
while True:
    computer_no_choice=random.randint(-1,2)
    computer_choice=no_for_words[int(computer_no_choice)]
    user_choice=input("Enter your choice: ").lower()
    print(f"Computer's choice is : {computer_choice}")
    if(computer_choice==user_choice):
        print("It's a draw..!")
    elif(computer_choice=="stone" and user_choice=="paper"):
        print("You win...!")
    elif(computer_choice=="stone" and user_choice=="scisor"):
        print("You Lose...!")
    elif(computer_choice=="paper" and user_choice=="stone"):
        print("You Lose...!")
    
    elif(computer_choice=="paper" and user_choice=="scisor"):
        print("You Win...!")
    
    elif(computer_choice=="scisor" and user_choice=="stone"):
        print("You Win...!")
    
    elif(computer_choice=="scisor" and user_choice=="paper"):
        print("You Lose...!")
    elif(user_choice=="quit"):
        break
    else:
        print("Wrong input....\nSorry!")
    