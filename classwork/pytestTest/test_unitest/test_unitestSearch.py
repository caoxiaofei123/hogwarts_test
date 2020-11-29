import unittest

class search:
    def seach_fun(self):
        print("search")
        return True

class TestSearct(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.search = search()
        print("class set up")

    @classmethod
    def tearDownClass(cls) -> None:
        print("class tearDean")


    def test_search1(self):
        print("search1")
        assert True == self.search.seach_fun()

    def test_search2(self):
        print("search2")
        assert True == self.search.seach_fun()

    def test_search3(self):
        print("search3")
        assert True == self.search.seach_fun()