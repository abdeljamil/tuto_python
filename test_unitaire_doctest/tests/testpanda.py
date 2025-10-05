
import unittest

from test_unitaire.src.panda import Panda

# class TestPanda(unittest.TestCase):
#     def test_panda_is_instance_of_panda(self):
#         # p = Panda("kiiko",15)
#         p = Panda(15.64,15)
#         self.assertIsInstance(p,Panda)

#     def test_panda_age_is_positive(self):
#         p = Panda("kiiko",15)
#         self.assertGreater(p.age,0)





class TestPanda(unittest.TestCase):

    def setUp(self):
        self.p = Panda("kiiko",15)

    def test_panda_is_instance_of_panda(self):

        self.assertIsInstance(self.p,Panda)

    def test_panda_age_is_positive(self):

        self.assertGreater(self.p.age,0)




if __name__ == '__main__':
    unittest.main()