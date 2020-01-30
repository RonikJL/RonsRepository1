n = int(input("Enter number: "))
count = 0
print(f"Prime numbers between 0 and {n} are:")
for number in range(0,n):
   if number > 1:
       for i in range(2,number):
           if (number % i) == 0:
               break
       else:
           print(number)
           count += 1
print(f"Number of primes are {count}")