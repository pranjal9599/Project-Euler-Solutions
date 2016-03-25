# Even Fibonacci numbers ( https://projecteuler.net/problem=2 )

# Generate the fibonacci series upto 4 million
fibonacci = [1,2]
sum = 0

for i in range(2,1000000):
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

    if(fibonacci[i] > 4000000):
        fibonacci.pop(i)
        break
        
for i in range(len(fibonacci)):
    if fibonacci[i] % 2 == 0:
        sum += fibonacci[i]

print(sum) # 4613732
