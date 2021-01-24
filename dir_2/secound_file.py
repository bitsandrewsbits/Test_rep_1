for i in range(34, 0, -5):
        print(i ** 2)
print("Bye.")

#creating iterator

iterator1 = (x ** 2 for x in [4, 2, 5, 3])

print(next(iterator1))
