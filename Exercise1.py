number = int(input("Enter number: "))
even_sum = 0
odd_sum = 0

for i in range(1, number + 1):
    if i % 2 == 1:
        odd_sum += i
    else:
        even_sum += i

print("The sum of odd numbers from 1 to {} is {}".format(number, odd_sum))
average = even_sum / len(range(2, number + 1, 2))
print("The average of even numbers from 1 to {} is {}".format(number, average))