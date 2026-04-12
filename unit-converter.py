def converter(number, unit):  #function that converts values based on unit type
    
        if unit == "Celsius": #temperature
            result = f"{number} {unit} equals {round((number * 9/5) + 32, 2)} Fahrenheits!" 
            #Using the formula, we convert the value and round it to two decimal places using (round)
            return(result) #Return our result
        elif unit == "Fahrenheit": #temperature
            result = f"{number} {unit} equals {round((number - 32) * 5/9, 2)} Celsius!"
            return(result)
        elif unit == "Kilometers": #distance
            result = f"{number} {unit} equals {round(number * 0.621, 2)} Miles!"
            return(result)
        elif unit == "Miles": #distance
            result = f"{number} {unit} equals {round(number * 1.609, 2)} Kilometers!"
            return(result)
        elif unit == "Kilograms": #weight
            result = f"{number} {unit} equals {round(number * 2.2, 2)} Pounds!"
            return(result)
        elif unit == "Pounds": #weight
            result = f"{number} {unit} equals {round(number * 0.45, 2)} Kilograms!" 
            return(result)
while True: #set the program loop using "while"
    print("Choose the unit:") #making menu with different choices of converting pairs 
    print("1. Celsius ==> Fahrenheit")
    print("2. Fahrenheit ==> Celsius")
    print("3. Kilometers ==> Miles")
    print("4. Miles ==> Kilometers")
    print("5. Kilograms ==> Pounds")
    print("6. Pounds ==> Kilograms")
    print("0. Exit")                

    try: 
        choice = int(input("Enter your choice (0-6): ")) #choosing needed converting pair
        if choice == 1:
            unit = "Celsius"
        elif choice == 2:
            unit = "Fahrenheit"
        elif choice == 3:
            unit = "Kilometers"
        elif choice == 4:
            unit = "Miles"
        elif choice == 5:
            unit = "Kilograms"
        elif choice == 6:
            unit = "Pounds"
        elif choice == 0: #this allows to exit 
            exit()
        elif choice not in [0, 1, 2, 3, 4, 5, 6]: #by "not in" checking if the choice in our frame
            print("Please enter a number from 0 to 6!")
            continue
    except ValueError:  #if user will enter wrong symbols programm won't stop, but ask again for right symbol
            print("Something went wrong! Please try again!")


    while True: #loop to ensure valid number input
            try:
                    number = float(input("Enter number: "))
                    break
            except ValueError:  #if user will enter wrong symbols programm won't stop, but ask again for right symbol
                    print("Something went wrong! Please try again!") 
          
    print(converter(number, unit)) #print our results
     