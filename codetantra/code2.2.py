# def fibonacci(n):
# 	if n<=1:
# 		return n

# 	else:


#		return fibonacci(n-1)+fibonacci(n-2)

#n = int(input())
# for i in range(1, n + 1):
# 	print(fibonacci(i), end=" ")


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

n = int(input())

for i in range(n):
    print(fib(i), end=" ")