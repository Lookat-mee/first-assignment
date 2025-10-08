print("My name is P.k, short for Paul Kelly. I'm from Delta state, NIgeria reside in NIgeria and i'm a tech enthusiast")

# assignment 2 & 4
# name = input("please enter your name ")
# nationality = input("please enter your nationality ")
# profession = input("please enter your profesion ")
# print("hello " + name + " all " + nationality + " are welcome to learn python with jude" + " regarless of the fact that you're" + profession + "you are can learn and master python ")

# assignment (a simple calculator that performs only additional operations) 
# first_number = int(input("enter first number"))
# second_number = int(input("enter sedcond number"))
# result = first_number + second_number
# print (f" the summation to your numbers is  {result}")
# username=input("please enter your name")
# length = len(username)
# print(length, "\n", username)
# print("you're welcome")

# glass1 = "milk"
# glass2 = "juice"
# # new_glass1 = glass2
# # new_glass2 = glass1
# glass3 = glass1
# glass1= glass2
# glass2 = glass3
# print(glass1)
# print(glass2)

#band name generator
# print("Welcome to brand name Generator.")
# city_name = input("whats the name of your city" "\n")
# pets_name = input("whats your pet's name" "\n")
# name_of_band = print("your band's name could be " + city_name + " " + pets_name)


# subscripting data types
# print("12345678"[-7])
# print(type(len("442223")))
# print(type(False))
# print(type("home"))
# print(type(1234))
# print(type(12.45))

# type conversion and type casting
# print("number of fletters in your name: " + str(len(input("enter your name "))))
# print(3*3/3+3-3)

#tip calculator
print("welcome to the tip calculator")
bill = float(input("what was the total bill \n"))
tip = float(input("how much tip will you like to give? 10, 12 0r 15 \n"))
split= float(input("How many people to split the bill \n"))

#calculation engeine
tip_percentage = float(tip /100*bill)
preliminary_bill = float(tip_percentage+bill)
# print(type(bill))
# print(type(tip))
# print(type(split))
# print(type(tip_percentage))
split_bill = round(preliminary_bill / split, 2)
print(f"Each person should pay {split_bill}")