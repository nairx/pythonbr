colour = input("Enter colour")
match colour:
    case "green":
        print("Go")
    case "red":
        print("Stop")
    case "yellow":
        print("slow down")
    case _:
        print("Invalid input")
    
    
# if colour == "green":
#     print("Go")
# elif colour == "red":
#     print("Stop")
# elif colour == "yellow":
#     print("Slow down")
# else:
#     print("Invalid input")