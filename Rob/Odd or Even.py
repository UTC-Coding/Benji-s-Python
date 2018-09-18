odd = [1,3,5,7,9]
even = [2,4,6,8,10]

answer = input("Please enter your number! \n")
answer = int(answer)

if answer in odd:
    print("That is quite odd!")
elif answer in even:
    print("That's even")
else:
    print("You are broken!")