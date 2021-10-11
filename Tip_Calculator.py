# from Calculator_Functions import *
# I wanted to create a Functions file that I could import from
# only right that I thank you for eating at my establishmentl. More people should eat hummus, it is good for us.
print("Thank you for eating at Jessy's Hummus House. Here is your Tip calculator. Just follow the instructions to pay for your service")
# Want to add safety measures incase anyone uses all capitals, for example.
# Have to ask for feed back on how our services were.
Yes_No =input('Was the meal to your liking? Yes/No: \n')
if Yes_No == 'Yes':
    print('Glad to hear that. Here at Jessy"s Hummus House we take pride in provide the best service in this side of the virtual world')
elif Yes_No =='No':
    print('Sorry to hear that. We will make sure to work on it emmediately')
else:
    print('Sorry, I could not hear you')
# Here I tried to use the first function I was trying to create. It worked, however it would also print out "NONE" and did not have the time to figure it out
bill = float(input("What was the total bill?:\n $"))
# Before I tried my imported function, I tried a while loop just incase someone did not typed intergers
# # # while bill == False:
# # #     print(bill)
# print(get_bill())
# bill= get_bill()
# Here I included another If loop just for more practice
tip = int(input("What percentage tip would you like to give? 10, 12 or 15: \n"))
if tip ==0:
    print('You must be doing worse than we are, God Bless you')
elif tip <14:
    print("We are grateful with any tip you may want to contribute")
elif tip >= 15:
    print("Thank you for your kindness")
    if tip>= 100:
        print("You are welcomed back any time")
# It was getting late so I pretty much ended it here.
people = int(input("How many people to split the bill?\n "))
# wanted to make sure everyone knew how much the tip by itself would total.
print(f'the total amount for the tip will be ${bill * (tip/100)}')
split =  (bill *(1 + tip / 100)) / people

print(f"Each person should pay: ${(round(split, 2))}")
print('Thank you, have a wonderful day!')
