
#s = "Bashir", d = "*", n = 10 ==>s1 = "**Bashir**"
# def centerize(s,d,n):
#     n1 = n-len(s)
#     s1 = (n1-n1//2)*d+s+(n1//2)*d
#     return s1
# print(centerize("Bashir","*",10))

# def center_(s,d,n):
#     x = len(s)
#     n1 = n-x
#     s1 = (n1-n1//2)*d+s+(n1//2)*d
#     return s1
# print(center_("Ali","¤",11))



# "manam" "madam" ==> Palindrome ==> True else False

# def palindrome(s):
#     s = s.replace(" ","")
#     s = s.replace(".","")
#     if s==s[::-1]:
#         return True
#     else:
#         return False
# print(palindrome("madam"))

# isprime ===> 4=>False (1,2,4)   5--->(1,5)-->True
# def isprime(a):
#     for i in range(2,a):
#         if a%i == 0:
#             return False
#     return True
# print(isprime(5))

# 10,2 --> 4 
# 5,15 --> 6
# 8, 4 --> 6
# def find_even(m,n):
#     if m > n:
#         m,n = n,m
#     for i in range(m+1,n):
#         if i%2 == 0:
#             return i
        
# print(find_even(2,10))

# def sum_m_n():
#     m = int(input())
#     n = int(input())
#     if m > n:
#         m,n = n,m
#     s = 0
#     for i in range(m,n+1):
#         s += i
#     return s
# print(sum_m_n())

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

        










    

    