import unittest


# def test_case_one():
#     assert 5 * 10 == 50, f"Should Be 50"

# def test_case_two():
#     assert 5 * 50 == 250, f"Should Be 250"

# if __name__ == "__main__":
#     test_case_one()
#     test_case_two()

#     print("All Tests Passed")


class MyTestCase(unittest.TestCase):

    # def test_one(self):
    #     self.assertTrue(100 > 97, "Should Be True test_one")
    # def test_two(self):
    #     self.assertEqual(40 + 60, 100, "Should Be 100")
    def test_three(self):    
        try:
            self.assertGreater(100, 101, AssertionError)
        except AssertionError:
              print("Should Be True From test_three")
    # def test_four(self):
    #     self.assertNotIsInstance(test2, MyTestCase, "This Is An Instance")
test2 = []
# test = MyTestCase()
if __name__ == "__main__":
    # test.test_one()
    unittest.main()