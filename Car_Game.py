command = ""
started =False
print ("Enter 'help' for manuals")
while True:
    command = input("> Enter command: ").lower()
    if(command == "start"):
        if started:
            print("Car already started!!")
        else:
            started = True
            print ("Car started")
    elif(command == "stop"):
        if not started:
            print("Car already stopped!!")
        else:
            print("Car stopped")
            started = False
    elif(command == "help"):
        print("""
start to start the car
stop to stop the car
quit to exit
            """)
    elif(command == "quit"):
        break
    