# Step 2
class SummitionClass(object):
	def sum_two_numbers(self, a, b):
		return a+b

	def sum_list(self, *args):
		return reduce(self.sum_two_numbers, args[0])

	def add_one(self, num):
		return num+1

# Step 3 - This is the final step where functional code is ready for production
def main():
	s = SummitionClass()
	print s.sum_two_numbers(1, 999)
	print s.sum_list([1, 999, 890, 345, 234])
	print s.add_one(999)

main()
