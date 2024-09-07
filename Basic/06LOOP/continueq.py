# #print all those number in a list there are not multiple of 5.
# arr = [10,16,17,18,19,20,15]
# # for ele in arr:
# #     if ele % 5 == 0:
# #         continue
# #     print(ele)


# # for ele in arr:
# #     if ele % 5 != 0:
# #         print(ele)

# i = 0
# while i <= 5:
#     if i == 3:
#         i+=1
#         continue
#     print(i,i*i)
#     i+=1
    
list = [10,16,17,18,9,15,21,13]
for item in list:
    if item % 5 == 0:
        continue
    if item % 7 == 0:
        break
    print(item)
print("Bye")