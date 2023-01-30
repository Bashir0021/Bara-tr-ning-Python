val1 = int(input("Write a number: "))
def fizz_buzz():
    if val1%3 == 0 and val1%5 == 0:
        return "FizzBuzz"
    if val1%3 == 0:
        return "Fizz"
    if val1%5 == 0:
        return "Buzz"
    return val1
print(fizz_buzz())

# for i in range(1, 101):
#     if i%3 == 0 and i%5 == 0:
#         print("FizzBuzz")
#     elif i%3 == 0:
#         print("Fizz")
#     elif i%5 == 0:
#         print("Buzz")
#     else:
#         print(i)


# for i in range(1, 101):
#     if i%3 == 0 and i%5 == 0:
#         print("FizzBuzz")
#     elif i%3 == 0:
#         print("Fizz")
#     elif i%5 == 0:
#         print("Buzz")
#     else:
#         print(i)


# ditt_val = int(input("skriv ett nummer: "))
# i = 1
# while i <= ditt_val:
#     if i%3 == 0 and i%5 == 0:
#         print("FizzBuzz", end=", ")    
#     elif i%3 == 0:
#         print("Fizz", end=", ")
#     elif i%5 == 0:
#         print("Buzz", end=", ")
#     else:
#         print(i, end=", ")
#     i += 1