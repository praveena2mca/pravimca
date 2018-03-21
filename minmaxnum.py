l1= []
n=int(input('How many numbers: '))
for i in range(n):
    num= int(input('Enter number '))
    l1.append(num)
print("Maximum element in the list is :", max(l1), "\nMinimum element in the list is :", min(l1))
