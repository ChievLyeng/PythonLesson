# print("Exercise 1")
# text=input("Enter word : ")
# if len(text) <3:
#     print(text)
# if len(text) >= 3:
#     if text[-3:] == "ing":
#         print(text+"ly")
#     else:
#         print(text + "ing")
# print("---------------------------------")
# print("Exercise 2")
# BY=int(input("Enter your year of birth : "))
# zodiac=BY%12
# if zodiac == 0:
#     print("Your are Monkey!")
# if zodiac == 1:
#     print("Your are Rooster!")
# if zodiac == 2:
#     print("Your are Dog!")
# if zodiac == 3:
#     print("Your are Pig!")
# if zodiac == 4:
#     print("Your are Rat!")
# if zodiac == 5:
#     print("Your are Ox!")
# if zodiac == 6:
#     print("Your are Tiger!")
# if zodiac == 7:
#     print("Your are Rabbit!")
# if zodiac == 8:
#     print("Your are Dragon!")
# if zodiac == 9:
#     print("Your are Snake!")
# if zodiac == 10:
#     print("Your are Horse!")
# if zodiac == 11:
#     print("Your are Goat!")

print("---------------------------------")
print("Exercise 3")

print("Note: <<Month and Day format are in number>>")
mm=int(input("Enter month : "))
dd=int(input("Entre day   : "))

# if mm >12 and mm < 0:
#     print("There are only 12 months of a year.")
# if dd>31 and dd < 1:
#     print("There are only 28 to 31 days in a month.")

if (dd>=20 and dd<=31 and mm==3) or ( 3<mm<=6):
    print("It's spring season")
if (dd>=21 and dd<=30 and mm==6) or ( 6<=mm<=9):
    print("It's Summer season")
if (dd>=23 and dd<=30 and mm==9) or ( 9<=mm<=12):
    print("It's Autumn season")
if (dd>=22 and dd<=30 and mm==12) or ( 12<=mm<=3):
    print("It's Winter season")








# print("---------------------------------")
# print("Exercise 4")


