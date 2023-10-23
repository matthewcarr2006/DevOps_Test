# 3)	Write a function that takes 3 numbers as arguments, and returns the highest number.


class Numbers:
    def __init__(self, nums=0):
        self.nums = []

    def add_nums(self, num):
        self.nums.append(num)

    def highest_num(self):
        highest = max(self.nums)
        return print(f"{highest} is the highest number in the data set.")


my_numbers = Numbers(0) 
my_numbers.add_nums(100)
my_numbers.add_nums(101)
my_numbers.add_nums(999)
my_numbers.add_nums(1000)
#print(my_numbers.highest_num())