from math import sqrt


class Node:
	"""
	:argument type - use 1 for points from user
					 use 2 for Hanan points
					 use 3 for points generated by heuristics
	"""
	def __init__(self, x, y, type):
		self.x = x
		self.y = y
		self.type = type;

	def __repr__(self):
		return "(" + str(self.x) + ", " + str(self.y) + ")"

	def hello(self):
		print("x: " + str(self.x) + ", y: " + str(self.y))

	def __hash__(self):
		return hash((self.x, self.y))

	def __eq__(self, other):
		if isinstance(other, Node):
			return other.x == self.x and other.y == self.y
		else:
			return False

class Edge:
	def __init__(self, n1, n2):
		self.n1 = n1
		self.n2 = n2
		x_diff = n1.x - n2.x
		y_diff = n1.y - n2.y
		self.weight = sqrt(x_diff**2 + y_diff**2) #distance beetwen n1 and n2

	def hello(self):
		print("Edge with weight: " + str(self.weight))
		self.n1.hello()
		self.n2.hello()