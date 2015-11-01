# -*- encoding: utf-8 -*-
__author__ = 'lai'

import unittest

# 先定义一个被测试的方法
def addOne(a):
    """ 输入数自增1后返回 """

    return a + 1

# 编写测试用例
class TestAddOne(unittest.TestCase):

    knownResult = (
        (1, 2),
        (2, 3),
        (3, 4),
        (4, 5),
        (5, 6)
    )

    def testKnownResults(self):
        """ addOne输出结果应该与测试用例一致 """
        for a, b in self.knownResult:
            # 计算结果
            c = addOne(a)

            # 断言
            self.assertEqual(b, c)

if __name__ == '__main__':
    unittest.main()