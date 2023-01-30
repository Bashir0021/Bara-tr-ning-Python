# def mult_m_n():
#     m = int(input("Enter starting number: "))
#     n = int(input("Enter ending number: ")) 
#     s = 1
#     if m > n:
#         m,n = n,m
#     found = False
#     for i in range(m,n+1):
#         if i%2 != 0:
#             s = s * i
#             found = True
#     if found:
#         return s
#     else:
#         return "Not found"

# print("Product of odd numbers between",mult_m_n())

# def multiply_to_10():
#     result = []
#     s = ""
#     number = int(input("Write a number: "))
#     for i in range(1,11):
#         result.append(str(i) + ' * ' + str(number) + ' = ' + str(number * i))
#     return result

# print(multiply_to_10())

