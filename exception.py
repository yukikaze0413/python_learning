try :
    time = int(input("Enter the time in hours: "))
    route = float(input("Enter the route: "))
    speed =route / time
    printf("The speed is %.2f km/h", speed)
except ValueError:
    print("Invalid input. Please enter a valid number.")
except ZeroDivisionError:
    print("Time cannot be zero.")
