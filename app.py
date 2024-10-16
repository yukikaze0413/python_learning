statis=0
while True:
 command = input("Enter a command: ")
 if command == "help":
    print('''
start - to start the car
stop - to stop the car
quit - to quit the program
            ''')
 elif command == "start" :
     if statis==0:
      statis=1
      print("The car has started")
     else:
         print("The car is already started")
 elif command == "stop" :
     if statis==1:
      statis=0
      print("The car has stopped")
     else:
         print("The car is already stopped")
 elif command == "quit":
    print("The program has been quit")
    break
 else:
    print("Invalid command")
