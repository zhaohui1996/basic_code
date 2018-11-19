# 构造数据,需要导入random包
import random

#产生-10到10之间的数字,并赛选出大于等于0的数字,保存为一个列表
def demo1():
    data = [random.randint(-10, 10) for _ in range(10)]
    print(data)
    res = [x for x in data if x >= 0]
    print(res)

#产生一个字典,并赛选字典值大于等于90的的键值对
def demo2():
    data = {"N{}".format(name): random.randint(80, 100) for name in range(1, 11)}
    print(data)
    res = {k: v for k, v in data.items() if v >= 90}
    print(res)

#产生10个数字,赛选出能被3整除的数字
def demo3():
    data = {random.randint(-10, 10) for _ in range(10)}
    print(data)
    res = {x for x in data if not x % 3}
    print(res)


if __name__ == '__main__':
    demo1()
    demo2()
    demo3()
