n = int(input("How many Fibonnaci numbers do you want to print? (must be greater than 1)\n"))

while n < 2:
    n = int(input("Please enter a number greater than 1.\n"))

fib = [0, 1]
print(fib[0],end=' ')
print(fib[1],end=' ')

while len(fib) < n:
    fib.append(fib[-2]+fib[-1])
    print(fib[-1],end=' ')
