# print("hello world")
#
# a="hello world"
# print(a)
#
# l=[1,2,3,4,5,6,7]
# l[3]=80
# print(l)
#
# b=(1,2,3,4,4,5,5,6)
# print(b)
#
# c={1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9}
# print(c)
#
# a=34
# b='63'
# c=43.96
# print(a+int(b)+float(c))
#
# a=True
# b=59
# print(a+b)
#
# a=False
# b=59
# print(a+b)
#
# a={'name':'老八','sex':'男','age':'18'}
# print(a['name'])
#
#
# a=[12,13,15,19,19,25,28,81,81,25,64]
# print(tuple(a))
# print(set(a))
#
# y='12123698741'
# print(list(y))
# print(tuple(y))
# print(set(y))
#
#
# q='asdfg'
# w={'a','5','p'}
# e=['a','5','p']
# r=('a','5','p')
# t={'fxxk':'111','nice':'4396','apple':'18'}
# print('d' in q)
# print('5' in w)
# print('p' in e)
# print('a' in r)
# print('fxxk' in t)
#
#
# money = 100000000000000000000000
# if(money < 100):
#     print('早点睡觉小老弟')
# elif(money < 1000):
#     print('抽烟喝酒烫头')
# elif(money < 10000):
#     print('酒吧包厢一条龙')
# elif(money < 100000):
#     print('游艇party使劲摇')
# elif(money < 1000000000000000000):
#     print('把美国买了')
# else:
#     print('太空人')
#
#
# for a in range(10):
#     print('跟着爷爷我摇就完事儿了')
#
# for a in [1,2,3,4,5]:
#     print(a)
#     print('跟着爷爷我摇就完事儿了')


# print(list(range(1,100000000,25)))
# print(list(range(10000,10,-10)))

# i = 1
# while i<10:
#     print(i)
#     i += 1
#
#
# while True:
#     print('起飞')

# for i in range(1,11):
#     if(i == 5):
#         continue
#     print(i)
#
#
# for i in range(1,11):
#     if(i == 5):
#         pass
#     else:
#         print(i)
#
# for i in range(0,101,10):
#     if(i in [50,70,90]):
#         continue
#     print(i)

#
# def div(a,b):
#     if b <= a:
#         print(b / a)
#     else:
#         print(a / b)
# div(50,200)


# def select_data(sql):
#     res='查询结果'
#     return res
#
# result = select_data('')
# print(result)


# def x(a=10,b=50,c=35):
#     return a+b*a-c
# print(x(5,6,20))
# print(x(c=10))
# print(x(8,10,c=20))
# print(x(a=7,b=5,c=9))


# def x(*args,**kwargs):
#     print(args)
#     print(kwargs)
# x(1,3,5,7,9,a=10,b=25,c=30,d=45,sex='男')



# f=open('z.txt','w')
# f.write('10086')
# f.close()
#
# f=open('z.txt','r')
# r=f.read()
# print(r)
# f.close()

# a=5
# def fff():
#     global a
#     a = 10
# fff()
# print(a)



# a='1819213548891491561321351251324'
# print(a[3:])
# print(a[1:-1])
# print(a[-2:])
# print(a[1:-2])
# print(a[:2])

# a=' sfghhgdjgfjhgfhgfh '
# a=a.strip()
# print(a.strip())
# print(a.lstrip())
# print(a.rstrip())
#
# b='11，22，33，44，55，66'
# b=b.replace('，',',')
# print(b)
# print(b.split(','))

# for a in range(1,51):
#     for b in range(1,a+1):
#         print("%sX%s=%s"%(a,b,a*b),end='   \t')
#     print()

# l = [1,2,3,4,5,6,7,8]
# # for i in l :
# #     print(i)
#
# l[0]=20 # 根据下标修改列表元素的值
# l.append(9) # 往列表末尾添加数据
# l.insert(2,30) # 根据下标往列表中插入数据
# l.extend((1,2,3,4,5)) # 往列表末尾添加多个数据
# l.pop()#删除列表末尾最后一个元素
# l.pop(0) # 根据下标删除数据
# l.remove(2) # 根据内容删除列表中的数据，有重复只会删除第一个
# print(l.index(6)) # 查询某个元素的下标，多个值，只查询第一个
# l.sort() # 默认升序，会修改原列表中的数据
# l.sort(reverse=True) # 降序
#
# print(l)

# 元祖
# t = (1,) # 一个元素的元祖
# print(t)
## 遍历，拼接，截取 和字符串列表一样
# 不支持修改，所以不支持其他操作


# 空集合
# s = set()
## 遍历
## 不支持下标索引，所以不支持其他操作


# 字典
# d = {"name":"小明","age":"20","sex":"男"}
#
# print(d["name"]) # 访问字典值
# d["name"] = "小红" # 修改value
# d["sex"] = "女" # 因为sex在原字典中不存在，所以是新增
# d.pop("sex") # 删除字典中的数据
#
# d2 = {"sex":"女"}
# d.update(d2) # 合并两个字典
# print(dict(d,addr="上海闵行",phone="1856954125")) # 创建一个新字典，并把数据放进去
#
#
# print(d)

# l = [10,1,35,61,89,36,55]
# # 依次比较相邻的两个数据，如果前边的数据比后边的大， 则交换两个数据的位置，直到把最大的数据都放到最后第一次排序结束，
# # 第二次排序重复第一次排序的动作，把第二大的放到倒数第二的位置，依次类推，直到所有的数据都排好序为止
#
#
# for i in range(len(l)-1,0,-1): # i代表最后一个未排好序的数据下标
#     for j in range(0,i): # j 代表每次循环时，当前位置的下标
#         if(l[j] > l[j+1]): # 比较当前位置和下一个位置的数据大小，如果当前位置大于下个位置，则交换两个数据的位置
#             l[j],l[j+1] = l[j+1],l[j]  # 交换两个数据的位置
#
# print(l)





# class str_demo():
#     s=[0,15,189,98,65,34]
#     print(s)
#     def replace(self):
#         print('sadsadsad')
#     def split(self):
#         print('kjhlhghj')
#
# sd = str_demo()
# sd.s = 'hello'
# sd.replace()
# sd.split()
# import random
# def random_str(str, length):
#     res = random.choices(str, k=length)
#     return "".join(res)
#
# def random_name():
#     xing_list = ["赵","钱","孙","李","周","武","郑","王","欧阳","诸葛","轩辕","上官","司徒"]
#     zi_list = "花赤橙黄绿青蓝紫冬梅建国华世凯"
#     xing = random.choice(xing_list)
#     zi_length = random.randint(1,2)
#     zi = random_str(zi_list,zi_length)
#     return xing + zi
#
# print(random_name())

try:
    r=open('a.txt','r')
except Exception as e:
    print(e)
    # print(e.args)
    # print(str(e))
    # print(repr(e))
    print('程序执行遇到问题')
    print('重新打开文件')
else:
    print('无内鬼')
finally:
    print('对不起，我是个警察')
print('文件已打开')









