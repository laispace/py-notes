# -*- encoding: utf-8 -*-
__author__ = 'lai'

# 迭代器就是一个定义了 __iter__() 和 __iter__() 方法的类。

class Counter():
    def __init__(self, number):
        self.n = 0
        self.number = number


    def __iter__(self):
        return self

    def __next__(self):
        if self.n > self.number:
            # 抛出 StopIteration 异常， 这是给调用者表示迭代用完了的信号。 和大多数异常不同， 这不是错误
            raise StopIteration

        self.n += 1
        return self.n


# 示例
counter1 = Counter(10)
print('counter1')
print(next(counter1), end=' ')
print(next(counter1), end=' ')
print(next(counter1), end=' ')
print(next(counter1), end=' ')
print(next(counter1), end='\n')
print('')

counter2 = Counter(20)
print('counter2')
for c in counter2:
    print(c, end=' ')
print('')