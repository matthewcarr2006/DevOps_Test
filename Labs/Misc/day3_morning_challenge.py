# Morning challenge - rewrite this code without using 'if' statements (or max or any inbuilt functions!!)

num = 50
num_1 = 20

#if num > num_1:
#    print(num)
#else:
#    print(num_1)

greatest = (num > num_1) * num + (num_1 >= num) * num_1
print(greatest)