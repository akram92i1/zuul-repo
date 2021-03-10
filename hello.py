import unittest 
class TestHello(unittest.TestCase):
	def test_hello(self):
		self.assertEqual(hello(),'Hello MGL7760 From zuul')

def hello():
	return 'Hello MGL7760 From zuul'

if __name__ == '__main__':
	print(hello())
