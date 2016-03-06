from unittest import TestCase

from scripts.app import SummitionClass

# Step 1
class TestSummitionClass(TestCase):
  def setUp(self):
  	# this method is called once at the begining for every test_* method
    self.summition = SummitionClass()
    pdb.set_trace()

  def test_add_one(self):
  	self.assertEqual(self.summition.add_one(0), 1)

  def test_sum_two_numbers(self):
  	self.assertEqual(self.summition.sum_two_numbers(1, 2), 3)

  def test_sum_list(self):
  	self.assertEqual(self.summition.sum_list([1, 2, 3, 4, 5]), 15)

  def tearDown(self):
  	# this method is called once at the end for every test_* method
    pdb.set_trace()
