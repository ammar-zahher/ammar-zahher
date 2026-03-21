command = input("What do you want to do? ")

match command:
    case "start":
        print("Starting system...")
    case "stop":
        print("Stopping system...")
    case _:
        print("Command not recognized")
