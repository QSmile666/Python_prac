'''
    企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
    利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
    20万到40万之间时，高于20万元的部分，可提成5%；
    40万到60万之间时高于40万元的部分，可提成3%；
    60万到100万之间时，高于60万元的部分，可提成1.5%;
    高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
'''

# bonus = 0
# # 这时输入是个字符串
# # I = input()
#
# # 输入的字符串转换为整数
# I = int(input("请输入利润(元)："))
# # print("请输入利润(万元)：", I)
# if I <= 100000:
#     bonus = I * 0.1
# elif I > 100000 and I <= 200000:
#     bonus = 100000 * 0.1 + (I - 100000) * 0.075
# elif I > 200000 and I <= 400000:
#     bonus = 100000 * 0.1 + 100000 * 0.075 + (I - 200000) * 0.05
# elif I > 400000 and I <= 600000:
#     bonus = 100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + (I - 400000) * 0.03
# elif I > 600000 and I <= 1000000:
#     bonus = 100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + 200000 * 0.03 + (I - 600000) * 0.015
# elif I > 1000000:
#     bonus = 100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + 200000 * 0.03 + 400000 * 0.015 + (I - 600000) * 0.01
#
# print("应发放奖金总数(元): ", bonus)

'''
python中input()和raw_input的区别

1>python3里面已经把raw_input()给去掉了

事实上是这样的：在 Python 3 内，将 raw_input() 重命名为 input()，这样一来，无须导入也能从标准输入获得数据了。如果您需要保留版本 2.x 的 input() 功能，可以使用 eval(input())，效果基本相同。
2>Python 版本 2.x 中，raw_input() 会从标准输入（sys.stdin）读取一个输入并返回一个字符串，且尾部的换行符从末尾移除
————————————————
版权声明：本文为CSDN博主「携手凡生」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/salove_y/article/details/78823838
'''

'''
报错信息：
Traceback (most recent call last):
  File "D:/pycharm/runoob_prac/python100/test2.py", line 13, in <module>
    if I <= 10:
TypeError: '<=' not supported between instances of 'str' and 'int'
'''

# 优化版
I = int(input("请输入利润(元)："))
abonus = 0
arr = [1000000, 600000, 400000, 200000, 100000, 0]
rate = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1, ]

for index in range(0, 6):
    if I > arr[index]:
        abs =  (I - arr[index]) * rate[index]
        print(abs)
        abonus = abonus + abs
        I = arr[index]


print("应发放奖金总数(元): ", abonus)