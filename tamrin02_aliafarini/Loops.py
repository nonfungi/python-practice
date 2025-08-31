#Loops
#1
even = []
for i in range (100):
    if i%2 == 0:
        even.append(i)
print (even)


#2

entered_number = []
while i != 0:
    i = int(input("Enter a number (0 to stop): "))
    entered_number.append(i)

print("You entered:", entered_number)

3#

my_list = list(range(11))
n = int(input("enter a number in (0 to 10): "))
if n in my_list:
    for i in my_list:
        print (i*n)