'''
    Author : Cyberkid
    Language : Python3
    email : thehappymentorkid@gmail.com
'''


tcs = int(input())
for i in range(tcs):
	n, k = map(int, input().split())
	arr = list(map(int, input().split()))
	arr2 = list()
	for j in range(k, n, 1):
		arr2.append(arr[j])
	for j in range(0, k, 1):
		arr2.append(arr[j])
	print(*arr2)


'''

k th
reverse[arr,arr+k]
reverse[arr+k,arr.end()]
reverse[arr,arr.end()]

#----INPUT----

2
8 2
2 -4 3 -1 8 -5 0 6
8 3
-2 -4 -8 -6 -3 -1 -5 -7

#----OUTPUT----

3 -1 8 -5 0 6 2 -4
-6 -3 -1 -5 -7 -2 -4 -8
[1m2m34m4]=l [ map,l.split("m")]
'''

#SHORTER CODE
# for i in range(int(input())):
# 	n, k = map(int, input().split())
# 	arr = list(map(int, input().split()))
# 	arr = arr[k:] + arr[:k]
# 	print(*arr)