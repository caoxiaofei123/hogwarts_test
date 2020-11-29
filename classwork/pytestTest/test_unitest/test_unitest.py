import unittest
"""
1. 此处的类型没有要求，但是规范学法 驼峰原则
2. 类名后的传参是固定的
3. 测试用例按照test_XXX的规则
4. setup tearDown执行用例前后分别执行
5. setUpClass tearDownClass执行类前后分别执行
"""
class TestStringMethods(unittest.TestCase):

    # 执行用例前后分别执行
    def setUp(self) -> None:
        print("setup")

    def tearDown(self) -> None:
        print("tearDown")

    # 执行类前后分别执行
    @classmethod
    def setUpClass(cls) -> None:
        print("class setup")

    @classmethod
    def tearDownClass(cls) -> None:
        print("class tearDown")

    def test_upper(self):
        print("1111")
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        print("2222")
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        print("3333")
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    # 方法一：全量运行测试用例
    # unittest.main()

    # 方法二：执行套件,指定类中的用例方法
    # suit = unittest.TestSuite()
    # suit.addTest(TestStringMethods("test_upper"))
    # unittest.TextTestRunner().run(suit)

    # 方法三：加载测试类
    # suit1 = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
    # suit2 = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
    # suite = unittest.TestSuite([suit1,suit2])
    # unittest.TextTestRunner(verbosity=2).run(suite)

        # 方法四：执行指定文件下的测试类、方法
        test_dir = "./test_unitest"
        discover = unittest.defaultTestLoader.discover(test_dir,pattern="test_*.py")
        unittest.TextTestRunner().run(discover)
