#Write your code below this line 👇
print("Welcome to the rollercoaster program")
height = int(input("Please input your height"))
age = int(input("Please input your age"))
bill = 0

if height >= 120:
  if age < 12:
    bill += 5
else:
  print("Sorry, you have to grow taller to ride this.")