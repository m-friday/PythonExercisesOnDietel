# for row in range(10):
#     for column in range(10):
#         print('<' if row % 2 == 1 else '>', end='')
#     print()

# a = b = 7
# print('a =', a, '\nb =', b)

# for row in range(3):
#     for column in range(3):
#         print('0', end='')
#     print()

# print("Welcome to our medical diagnosis program.")
# problem = input("What is your problem? ")
#
# while problem:
#     input("Have you had this problem before (yes or no)? ")
#     if input == "yes":
#         print("Well, you have it again.")
#         break
#     elif input() == "no":
#         print("Well, you have it now.")
#         break
#     else:
#         print("Sorry, I didn't understand your response. Please answer 'yes' or 'no'.")

# print("HOUR \t\t\t Number of Bacteria")
# for hour in range (0, 16, 5):
#      number_of_bacteria = 200 * 2 ** hour
#      print(f"{hour: <5}{number_of_bacteria: >30}")


# infections = []
# for i in range(1, 8):
#     num_infections = int(input(f"Enter the number of reported infections for day {i}: "))
#     infections.append(num_infections)
# total_infections = sum(infections)
# average_infections = total_infections / len(infections)
# smallest_infections = min(infections)
# largest_infections = max(infections)
# print(f"Total infections for the week: {total_infections}")
# print(f"Average infections per day: {average_infections}")
# print(f"Smallest number of infections in a day: {smallest_infections}")
# print(f"Largest number of infections in a day: {largest_infections}")

# seconds = int(input("Enter the number of seconds: "))
# hours = seconds // 3600
# seconds %= 3600
# minutes = seconds // 60
# seconds %= 60
# print(f"{hours} hours, {minutes} minutes, {seconds} seconds")


# base_wage = 10.0
# percent_increase = 0.03
# for years in range(1, 11):
#     wage = base_wage * (1 + percent_increase) ** years
#     print(f"Hourly wage for year {years}: ${wage:.2f}")


# total_rabbits = 0
# total_does = 0
# does = int(input("Enter the number of does in the rabbit colony (-1 to end): "))
# while does != -1:
#     rabbits_born = int(input("Enter the number of rabbits born this month: "))
#     total_rabbits += rabbits_born
#     total_does += does
#     does = int(input("Enter the number of does in the rabbit colony (-1 to end): "))
# if total_does > 0:
#     average_rabbits_per_doe = total_rabbits / total_does
#     print(f"The average number of rabbits born per doe is {average_rabbits_per_doe:.2f}.")
# else:
#     print("No data was entered.")


# side1 = float(input("Enter the length of the first side of the triangle: "))
# side2 = float(input("Enter the length of the second side of the triangle: "))
# side3 = float(input("Enter the length of the third side of the triangle: "))
# if side1 == side2 and side2 == side3:
#     print("The triangle is equilateral.")
# else:
#     print("The triangle is not equilateral.")
