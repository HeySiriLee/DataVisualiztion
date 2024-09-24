# Conditional statement
# if condition1 (bool) :
#     if condition1 is true, then result
# elif condition2 :
#     if condition2 is true, then result
# else :
#     when none of the above conditions are true, result

# Declare the resident registration number
rrn = '900000-1000000'

if len(rrn) == 14 and rrn[6] == "-" :
    if int(rrn[:2]) <= 24 :
        if rrn[7] == "3":
            print("Men")
        elif rrn[7] == "4":
            print("Women")
        else : 
            print("Who r u?")
    else:
        if rrn[7] == "1":
            print("Men")
        elif rrn[7] == "2":
            print("Women")
        else : 
            print("Who r u?")
else: 
    print("That's wrong number")

# Iteration statement
sum1 = 0
for i in range(1, 10, 2) :
    sum1 += i
print(sum1)

# Practice
# Sum of odd & even
oddSum = 0
evenSum = 0

for j in range(101):
    if j % 2 == 0:  
        evenSum += j
    else: 
        oddSum += j

print("Sum of odd numbers:", oddSum)
print("Sum of even numbers:", evenSum)

# make the multiplication table
for k in range(10):
    print(k, ' Times table')
    print('               ')
    for l in range(1, 10):
        print(k, ' * ', l, ' = ', k*l)
    print('---------------')