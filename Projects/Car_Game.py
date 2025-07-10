
started = False

while True:
    user_choice = input("Enter your choice: ").lower()

    if user_choice == "start":
        if started:
            print("Car is already started and running!")
        else:
            started = True
            print("Car started and is now running.")

    elif user_choice == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car stopped.")

    elif user_choice == "help":
        print("""
Help:
    start - to start the car
    stop  - to stop the car
    quit  - to exit
    help  - to show this help message
""")

    elif user_choice == "quit":
        print("Exiting game. Goodbye!")
        break

    else:
        print("Invalid command! Type 'help' to see available commands.")
