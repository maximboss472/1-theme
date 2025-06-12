# 1 задание

# def binary_search(data, elem):
#
#     low = 0
#     high = len(data) - 1
# 
#     while low <= high:
#
#         middle = (low + high)//2
#
#         if data[middle] == elem:
#             return middle
#         elif data[middle] > elem:
#             high = middle - 1
#         else:
#             low = middle + 1
#
#     return -1

# 2 задание

# a = [7, 5, -8, 0, 10, 1]
# N = len(a)
#
# for i in range(0, N-1):
#     for j in range(0, N-1-i):
#         if a[j] > a[j+1]:
#             a[j], a[j+1] = a[j+1], a[j]
#
# print(a)