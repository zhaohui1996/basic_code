# 构造数据,需要导入random包
import random


def demo1():
    #构造10-15之间的数字10个,并打印出来
    src_data = [random.randint(10, 15) for _ in range(10)]
    print(src_data)
    # dest_data = list(set(src_data))
    # print(dest_data)
    # res_dict = dict.fromkeys(src_data)
    # res1 = list(res_dict.keys())
    # print(res1)
    # 创建一个空的列表,用于存放赛选之后的数字
    res = []
    [res.append(x) for x in src_data if x not in res]
    print(res)


if __name__ == '__main__':
    demo1()
