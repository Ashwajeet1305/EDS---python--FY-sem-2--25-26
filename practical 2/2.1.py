elements=input().split(" ")
key = input()

if key in elements:
	print(elements.index(key))
else:
	print("Not found")