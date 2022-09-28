# Caleigh Crossman 
# Discussion 5

import unittest

# Counts the number of a's in a sentence (e.g., a string)
# Not sure if this is supposed to be counting capital A's but I added it because my test cases 
# include counting capitals
def count_a(sentence):
	total = 0
	for i in range(len(sentence) - 1):
		if sentence[i] == 'a' or sentence[i] == 'A':
			total += 1
	return total


# Item class
# Describes an item to be sold. Each item has a name, a price, and a stock.
class Item:
	# Constructor.
	def __init__(self, name, price, stock):
		self.name = name
		self.price = price
		self.stock = stock

	# Print
	def __str__(self):
		return ("Item = {}, Price = {}, Stock = {}".format(self.name, self.price, self.stock))

# Warehouse class
# A warehouse stores items and manages them accordingly.
class Warehouse:

	# Constructor
	def __init__(self, items = []):
		self.items = items[:]

	# Prints all the items in the warehouse, one on each line.	
	def print_items(self):
		for item in self.items:
			print(item)
			print("\n")	

	# Adds an item to the warehouse	
	def add_item(self, item):
		self.items.append(item)

	# Returns the item in the warehouse with the most stock	
	# Not sure if we are supposed to be returning item.name or the item object 
	def get_max_stock(self):
		max_stock = self.items[0].stock
		temp = self.items[0].name
		for item in self.items:
			if item.stock > max_stock:
				max_stock = item.stock
				temp = item.name
		return temp

	# Returns the item in the warehouse with the highest price
	# Not sure if we are supposed to be returning item.name or the item object 
	def get_max_price(self):
		max_price = self.items[0].price
		temp = self.items[0].name
		for item in self.items:
			if item.price > max_price:
				max_price = item.price
				temp = item.name
		return temp	



# Tests
class TestAllMethods(unittest.TestCase):

	# SetUp -- we create a bunch of items for you to use in your tests.
	def setUp(self):
		self.item1 = Item("Beer", 6, 20)
		self.item2 = Item("Cider", 5, 25)
		self.item3 = Item("Water", 1, 100)
		self.item4 = Item("Fanta", 2, 60)
		self.item5 = Item("CocaCola", 3, 40)

	## Check to see whether count_a works
	def test_count_a(self):
		self.assertEqual(count_a("Yesterday I swam with my Dad"),3)
		self.assertEqual(count_a("Andrew ate apples after Aron's athletic adventure"),7)
		self.assertEqual(count_a("I like to surf"),0)


	## Check to see whether you can add an item to the warehouse
	def test_add_item(self):
		items_list = [self.item1, self.item2, self.item3, self.item4]
		warehouse = Warehouse(items_list)
		warehouse.add_item(self.item5)
		self.assertEqual(warehouse.items[4].name, "CocaCola")
		items2 = []
		warehouse2 = Warehouse(items2)
		warehouse2.add_item(self.item1)
		warehouse2.add_item(self.item2)
		self.assertEqual(warehouse2.items[0].name, "Beer")
		self.assertEqual(warehouse2.items[1].name, "Cider")

	## Check to see whether warehouse correctly returns the item with the most stock
	def test_warehouse_max_stocks(self):
		self.s1 = Item("Hammer", 5, 10)
		self.s2 = Item("Wood", 6, 30)
		self.s3 = Item("Boxes", 2, 2)
		self.s4 = Item("Nails", 7, 90)
		items_list = [self.s1, self.s2, self.s3, self.s4]
		warehouse = Warehouse(items_list)
		max_item = warehouse.get_max_stock()
		self.assertEqual(max_item, self.s4.name)

	# Check to see whether the warehouse correctly return the item with the highest price
	def test_warehouse_max_price(self):
		self.s1 = Item("Hammer", 5, 10)
		self.s2 = Item("Wood", 14, 30)
		self.s3 = Item("Boxes", 2, 2)
		self.s4 = Item("Nails", 7, 90)
		items_list = [self.s1, self.s2, self.s3, self.s4]
		warehouse = Warehouse(items_list)
		max_item = warehouse.get_max_price()
		self.assertEqual(max_item, self.s2.name)
		

def main():
	unittest.main()

if __name__ == "__main__":
	main()