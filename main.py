tuoi = 24
ten = "Tien Nhat"
PI = 3.14
from fractions import Fraction
Fraction(3,4)
complex(2,1)
d = 2 + 4j
print(type(2 + 4j))
print(complex(2,1))
print(d.real)
print(d.imag)
print(type(tuoi))
print(type(ten))
print(type(PI))
print(type(Fraction(3,4)))
s = 'Free education'
player = "HowKteam"
print(type(s))
print(player)
print('\a')
print('Haizza, \neu mot ngay nao do')
a = r'\neu mot ngay \"'
print(a)
n = 'Hello'
n += "word"
m = 'nguyen'
m *= 0
print(m)
print(n)
print('my name is %s.' % ('Lucario'))
print('%d, that is %s problem' %(1, 'that'))
s = '%s, %s'
print(s %('one', 'two'))
class SomeThing:
     def __repr__(self):
        return 'Đây là __repr__'
     def __str__(self):
        return 'Đây là __str__'

sthing = SomeThing()
print(type(sthing))
sthing
print(sthing)
print("kter".upper())
print("how kteam".upper())
print('NGUYEN TIEN NHAT'.lower())
print('SAMSUNG electronic hcmc CE Complex'.swapcase())
print('kteam HOW About'.capitalize())
print("why Are YOU smile?".title())
print('fingerstyle'.center(24, '*'))
print('fingerstyle'.rjust(24, '*'))
print('fingerstyle'.ljust(24, '*'))
t = 'ố ồ'.encode();
print(t)
print(t.decode())
print(' '.join(['1', '2', '3']))
print('abc how abc kteam'.replace('abc','acb'))
print('%%%%Kter%%%'.strip('%'))
print('cababHowbaaaca'.strip('abc'))
print('\t\n\aKter\a\a\n\v'.strip())
print('\x07Kter\x07\x07')
print('%%%%Share%%%'.rstrip('%'))
print('cababKterbaaaca'.lstrip('abc'))
l = 'tttvttt'
print(l.removeprefix('t'))
print(l.removesuffix("t"))
print( 'How Kteam K9'.split())
print('How Kteam K9'.split(maxsplit=2))
print('How kteam EDUCATION'.rsplit(maxsplit=1))
print('a\nb\nc\nd\ne'.splitlines())
print('How kteam vs I hate python team vs Education'.partition('vs'))
print('How kteam vs I hate python team vs Education'.partition('VS'))
print('kkkkk'.count('k', 3))
print('how kteam free education'.startswith('kte', 4))
print('how kteam free education'.endswith('n', 0, 9))
list1 = [1, 'Nguyen Tien Nhat', [2, "ba", "bon"]]
print(list1)
a = [kteam for kteam in range(3)]
print(a)
another_lst = [[n, n * 1, n * 2] for n in range(1, 4)]
print(another_lst)
lst = list([1, 2, 3])
print(lst)
str = list("HOWKTEAM")
print(str)
list_1 = [1, 2]
list_1 += ['one', 'two']
print(list_1)
list_1 += "abc"
print(list_1)
l = list("KTER") * 2
print(l)
print('a' in [1, 2])
print("a" in ['a', 2, 3])
print('a' in [["a"], 2, 3])
print("*****************")
print([1, 2, 3] == [1, 2, 3])
print([4] > [3, 4])
print(['b', 'c', 'd'] < ['x', 'y', 'z'])
lt = [1, 2, 'a', 'b', [3, 4]]
print(lt[0])
print(lt[-1])
print(lt[1:3])
lst_2 = [1, 2, 'a', 'b', [3, 4]]
print(lst_2[1])
lst_2[1] = 4
print(lst_2)
lstt = [[1, 2, 3], [4, 5, 6]]
print(lstt)
print(lstt[0])
print(lstt[0][0])
print(lstt[0][:2])
Kteam = [1, 5, 1, 6, 2, 7]
print(Kteam.count(1))
print(Kteam.index(2))
another = lst_2.copy()
print(another)
print(another.clear())
print(lst_2)
Kteam.append(3)
print(Kteam)
Kteam.extend([4, 5])
print(Kteam)
Kteam.extend([7, 8, 9, 10])
print(Kteam)
Kteam.insert(2, 11)
print(Kteam)
Kteam.pop(3)
print(Kteam)
Kteam.reverse()
print(Kteam)
Kteam_true = Kteam.copy()
Kteam_true.sort(reverse= True)
print(Kteam_true)
Kteam.reverse()
a = ['This', 'is', 'How', 'Kteam']
b = a.copy()
a.sort
print(a)
b.sort(key = len)
print(b)
tup = (1, 2, 3, [4, 5])
print(tup)
print(type(tup))
tup1 = (9)
print(type(tup1))
print(len(tup))
f = 20
s = 'howkteam'
print(id(f))
print(id(s))
set_1 = {69, 96}
print(set_1)
set_2 = {1, 1, 1}
print(set_2)
a = {1, 2}
b = a.copy()
print(b)
c = {1, 2, 3, 4, 5}
d = {2, 4, 5, 6}
print(c.union(d))
print(c.intersection(d))
i = {1, 2, 3}
k = {2, 3, 4}
l = {3, 4, 5}
print(i^k^l)
#print(i.symmetric_difference(k, l))
print(i.symmetric_difference([2, 3, '6', '7']))
empty_dict = {}
print(type(empty_dict))
dic = {key: value for key, value in [('name', 'Kteam'), ('member', 69)]}
print(dic)
iter_ = [('name', 'Kteam'), ('member', 69)]
dic = dict(iter_)
print(dic)
f1 = [('ab'), ('cd')]
print(dict(f1))
iter_ = ('name', 'number', "class")
dic_none = dict.fromkeys(iter_)
print(dic_none)
print([x for x in range(3)])
itor = (x for x in range(3))
print(itor)
print(next(itor))
print(next(itor))
print(next(itor))
print('Kteam', 'Python', 'Course', sep='---')

#from time import sleep # nhập hàm sleep từ thư viện time

#print('start....')
#sleep(3) # dừng chương trình 3 giây
#print('end...')

#from time import sleep # nhập hàm sleep từ thư viện time

#print('start....', end='') # in ra nội dung và kết thúc bới một chuỗi  rỗng
#sleep(3) # dừng chương trình 3 giây
#print('end...')
#input("1234 = ")
print(ord('B'))
print("a" > "ABC")
print(not True)
a = 3
#if a-1 < 0:
#    print("a nho hon 1")

if a - 1 < 0: # False, tiếp tục
     print('a nhỏ hơn 1')
elif a - 2 < 0: # False, tiếp tục
     print('a nhỏ hơn 2')
elif a - 3 < 0: # False, tiếp tục
     print('a nhỏ hơn 3')
elif a - 4 < 0: # True, kết thúc
     print('a nhỏ hơn 4')
elif a - 5 < 0: # Khối BIG đã kết thúc, dù đây là True nhưng không ý nghĩa
     print('a nhỏ hơn 5')
print('t bằng 5' if t == 5 else 't khác 5')

if a - 1 > 0: print('a lớn hơn 1'); print('có thể a lớn hơn 2')
k = range(3)
print(type(k))
#Kteam(*lst)
#print(kteam(*('a', 'b', 'c'), 'd'))
Ktea = "How Kteam"
def Slogan():
    print("we are", Ktea)
Slogan()
