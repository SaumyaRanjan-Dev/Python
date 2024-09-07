### Find the smallest divisor of a number where that divisor is grater than 1.
# num = int(input("Enter the number: "))
# for ele in range(2, num + 1):
#     if num % ele == 0:
#         print(ele)
#         break
    
num = int(input("Emter n:"))
x=2
while x<=num:
    if num%x==0:
        print(x)
        break