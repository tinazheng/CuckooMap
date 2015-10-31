# Python 3

class CuckooMap:

	maxKnockout = 2000

	def __init__(self, n):
		self.max_size = n
		self.bucket_size = 2*n
		self.curr_size = 0
		self.buckets = [None]*2*n
		self.hash_functions = [self.hash_one, self.has_two]

	def hash_one(self, key):
		return hash(key) % self.bucket_size

	def hash_two(self, key):
		return (hash(key) - id(key) - 7) % self.bucket_size

	def doesNotExceedKnockoutLimit(self, hash_node):
		i = 0
		curr_node = hash_node
		curr_index = self.hash_functions[hash_node.getFunction()](hash_node.getKey())
		while i < self.maxKnockout:
			next_index = self.hash_functions[1-curr_node.getFunction()](curr_node.getKey())
			next_node = self.buckets[next_index]
			if not next_node:
				return True
			i += 1
			curr_node = next_node
		return False

	def _set_helper(self, hash_node):
		other_hash_func = self.hash_functions[1 - hash_node.getFunction()]
		if self.buckets[other_hash_func(hash_node.getKey())]:
			other_node = self.buckets[other_hash_func(hash_node.getKey())]
			self.buckets[other_has_func(hash_node.getKey())] = hash_node
			_set_helper(other_node)

	def set(self, key, val):
		node1 = self.buckets[self.hash_one(key)]
		node2 = self.buckets[self.hash_two(key)]
		if self.curr_size >= self.max_size:
			if node1 and node1.getKey() == key:
				node1.setVal(val)
			elif node2 and node2.getKey() == key:
				node2.setVal(val)
			else:
				return False
		else:
			if node1:
				if node1.getKey() == key:
					node1.setVal(val)
				elif not node2:
					self.buckets[self.hash_two(key)] = Node(key, val, 1)
					self.curr_size += 1
				elif node2.getKey() == key:
					node2.setVal(val)
				elif self.doesNotExceedKnockoutLimit(node1):
					self._set_helper(node1)
					self.curr_size += 1
				else:
					return False
			else:
				self.buckets[self.hash_one(key)] = Node(key, val, 0)
				self.curr_size += 1
		return True

	def get(self, key):
		node_one = self.buckets[self.hash_one(key)]
		node_two = self.buckets[self.hash_two(key)]
		if node_one and node_one.getKey() == key:
			return self.buckets[self.hash_one(key)].getVal()
		elif node_two and node_two.getKey() == key:
			return self.buckets[self.hash_two(key)].getVal()
		else:
			return None
	
	def delete(self, key):
		node_one = self.buckets[self.hash_one(key)]
		node_two = self.buckets[self.hash_two(key)]
		if node_one and node_one.getKey() == key:
			self.buckets[self.hash_one(key)] = None
			self.curr_size -= 1
			return node_one
		elif node_two and node_two.getKey() == key:
			self.buckets[self.hash_two(key)] = None
			self.curr_size -= 1
			return node_two
		else:
			return None

	def load(self):
		return self.curr_size / self.max_size

	def __repr__(self):
		return str(self.buckets)

	class Node:
		def __init__(self, key, val, function_id):
			self.key = key
			self.val = val
			self.function = function_id

		def getKey(self):
			return self.key

		def getVal(self):
			return self.val

		def setVal(self, val):
			self.val = val

		def getFunction(self):
			return self.function

		def __repr__(self):
			return "(" + self.key + ": " + str(self.val) + ")"


