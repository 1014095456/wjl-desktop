# -*- coding: utf-8 -*-
"""
Created on Mon May  4 15:18:23 2020

@author: wujinlv
"""
"""
import tensorflow as tf
#import keras
with tf.device('/cpu:0'):
    a = tf.constant([1.0,2.0,3.0],shape=[3],name='a')
    b = tf.constant([1.0,2.0,3.0],shape=[3],name='b')
with tf.device('/gpu:1'):
    c = a+b
#注意：allow_soft_placement=True表明：计算设备可自行选择，如果没有这个参数，会报错。
#因为不是所有的操作都可以被放在GPU上，如果强行将无法放在GPU上的操作指定到GPU上，将会报错。
sess = tf.Session(config=tf.ConfigProto(allow_soft_placement=True,log_device_placement=True))
#sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
sess.run(tf.global_variables_initializer())
print(sess.run(c))
"""

#数据类型
'''
d=float(input('输入华氏度'))
e=(d-32)/1.8
print('%.1f华氏度=%.1f摄氏度'%(d,e))#百分号忘记
print(f'{d:.1f}华氏度={e:.1f}摄氏度')#f忘记
'''

##分支
'''
x1=float(input('x='))
if x1>1:
    y1=3*x1
else:
    y1=7*x1
print('f(%.1f)=%.2f'(x1,y1))
'''

#循环结构
'''
sum1=0
for x2 in range(1,101,2):
    if x2%2==0:
        sum1 +=x2
print(x2)
row1=int(input('输入行数'))
for i in range(row1):
    for _ in range(i+1):
        print('*',end=' ')#end=''作为print()B参数，使print关闭“在输出中自动包含换行”的默认行为
    print()
'''

##函数，Python可以在函数下定义函数
'''
def add(*args):# 在参数名前面的*表示args是一个可变参数
    total = 0
    for i in args:
        total+=i
    return total
'''

#模块管理函数
'''
model1.py
def foo():
    print('hello world')
model2.py
def foo():
    print('goodbye world')
import  model1 as m1
import model2 as m2
m1.foo()
m2.foo()
'''

#使用__main__ 
'''
导入的模块除了定义函数之外还中有可以执行代码，那么Python解释器在导入这个模块时
就会执行这些代码,最好是将这些执行代码放入如下所示的条件中，这样的话除非直接运行
该模块，if条件下的这些代码是不会执行的，因为只有直接执行的模块的名字才是"__main__"
model3.py
def foo():
    pass
def bar():
    pass
if __name__=='__main__':
    print('call foo()')
    foo()
import model3
导入时，不会执行模块中if条件成立时的代码 因为模块的名字是module3而不是__main__
'''

#变量作用域，global关键字用来在函数或其他局部作用域中使用全局变量
#nonlocal声明的变量不是局部变量,也不是全局变量,而是外部嵌套函数内的变量
'''
def foo():
    global a#使用global关键字来指示foo函数中的变量a来自于全局作用域
    a=200
    print(a)
def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter
if __name__=='__main__':
    a=100
    foo()
    print(a)#200
'''

#字符串
'''
s1='hello world'#单个或多个字符用单引号或者双引号包围起来就是字符串
s2="""hello,
world"""# 以三个双引号或单引号开头的字符串可以折行
#字符串中使用\（反斜杠）来表示转义，\n换行 \t制表符 表示'用\'
s3 = '\'hello, world!\''
#Python为字符串类型提供了非常丰富的运算符，+实现字符串的拼接，*重复一个字符串
#的内容，in和not in来判断一个字符串是否包含另外一个字符串（成员运算），
#[]和[:]运算符从字符串取出某个字符或某些字符（切片运算）
s4='hello '*3
s5=s4[3:7]
print(s1,'\n',s2,s3,s4,s5,end='')
a,b=2,3
print('%d*%d=%d'%(a,b,a*b))
print(f'{a}*{b}={a*b}')#格式化字符串
'''

#列表
'''
list1=[1,2,3,4,5,6,7,8]
print(list1)
print(len(list1))
print(list1[5])
print(list1[-1])
for i in range(len(list1)):
    print(list1[i])
for i in list1:
    print(i)
for i,j in enumerate(list1):#enumerate同时获得元素索引和值
    print(i,j)
list1.append(9)
list1.insert(1,200)
list1.pop(1)
list1.extend([10,11,12])#合并列表
list1.remove(4)
list1.pop(0)#指定位置删除
list2=sorted(list1)#函数返回列表排序后的拷贝不会修改传入的列表
print(list2)
list1.sort(reverse=True)#直接在列表对象上进行排序
f=[x for x in range(1,10)]#列表的生成式语法
print(f)
'''

##元组,无法修改,创建时间和占用的空间上面都优于列表，多线程优势
'''
t=('骆驼',39,True,'四川')
print(t)
print(t[3])
person=list(t)#元组转列表
print(person)
person[1]=49
print(person)
fruits=['apple','banana']
fruits1=tuple(fruits)#转元组
print(fruits1)
'''

##集合
'''
set0={1,2,3,4,4,2,1}
print(set0)
set1=set(range(1,10))##创建集合
set2=set((1,2,3,4,5,2))
print(set1,set2)
set1.add(6)#集合添加删除
set2.update([10,39])
set2.discard(5)
set2.remove(4)
print(set1.pop(),set2)
print(set1 & set2)
print (set1 | set2)
print(set1 - set2)
print(set1 ^ set2)#对称差运算
'''

#字典
'''
scores={'one':93,'two':49,'three':84}
print(scores)
iteams=dict(one =1,two = 2,three=3,four=4)
iteams1=dict(zip(['a','b','c'],'123'))
print(iteams,iteams1)
print(scores[one])
'''
#跑马灯
'''
import os
import time
def main():
    content='北京欢迎您......'
    while True:
        os.system('cls')
        print(content)
        time.sleep(0.2)
        content=content[1:]+content[0]
if __name__ =='__main__':
    main()
'''  
#产生随机验证码
'''
import random
def generate_code(code_len=4):
    all_chars='0123456789abcdefghijklmn'
    maxpos=len(all_chars)-1
    code=''
    for i in range(code_len):
        index=random.randint(0,maxpos)
        code+=all_chars[index]#字符串增加
    return code
if __name__ =='__main__':
    print(generate_code())
 '''

##类
'''
class student(object):#定义类
    def __init__(self,name,age):#希望属性是私有的，属性命名时用两个下划线作为开头
        self.name=name
        self.age=age
    def study(self,course_name):
        print('%s正在努力学习%s.'%(self.name,course_name))
    def watch_movie(self):
        if self.age<18:
            print('%s在看熊出没'%(self.name))
        else:
            print('%s在看岛国电影'%(self.name))
def main():#创建使用类
    stu1=student('徐艳',20)
    stu1.study('小黄文')
    stu1.watch_movie()
if __name__=='__main__':
    main() 
'''
#访问可见性问题
'''
class Test:
    def __init__(self,foo):
        self.__foo=foo
    def __bar(self):
        print(self.__foo)
        print('__bar')
def main():
    test=Test('hello')
    print(test._Test__foo)#给私有的属性和方法换了一个名字来妨碍对它们的访问
    #print(test.__foo)#希望属性是私有的，属性命名时用两个下划线作为开头
    #test.__bar
if __name__=='__main__':
    main()
'''            
#继承、多态、封装

#面对对象进阶
'''           
class Person(object):
    def __init__(self,name,age):
        self._name=name#单下划线_开头：这是私有属性，外部依然可以访问更改
        self._age=age
    @property
    def name(self):# 获取私有属性值  p1.name 会执行这个函数
        return self._name
    @property 
    def age(self):
        return self._age
    @age.setter
    def age(self,age):#设置私有属性值  p1.age = 666
        self._age=age
def main():
    person=Person('王大',12)
    person.age=22
    print(person.age)
    print(person.name)
    #person.name='李元芳'

if __name__=='__main__':
    main()
'''

##Python允许给对象绑定新的属性或方法
##__slot__,限定自定义类型的对象只能绑定某些属性,只对当前类的对象生效，对子类并不起任何作用           
'''
class Person(object):
    __slots__=('_name','_age','_gender')
    def __init__(self,name,age):
        self._name=name
        self._age=age
    @property
    def name(self):
        return self._name
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,age):
        self._age=age
    def play(self):
        if self._age<16:
            print('%s在玩飞行棋'%self._name)
        else:
            print('%s在玩斗地主'%self._name)
def main():
    person=Person('徐艳',20)
    person.play()
    person._gender='男'#对象动态添加属性、方法
    #person._is_gay=True
if __name__=='__main__':
    main()
 '''   

#对象方法、类方法（静态方法）
'''
from math import sqrt
class Triangle(object):
    def __init__(self,a,b,c):
         self.a=a
         self.b=b
         self.c=c
    @staticmethod#静态方法,类和对象都可使用,但该方法不可调用类其他方法
    def is_valid(a,b,c):
        return a+b>c and b+c>a and a+c>b
    @classmethod#通过这个参数我们可以获取和类相关的信息并且可以创建出类的对象
    def start(cls):#cls作为第一个参数用来表示类本身
        a1,b1,c1=4,5,6#持有cls参数，可以来调用类的属性，类的方法，实例化对象等
        return cls(a1,b1,c1)
        
    def area(self):
        return sqrt(self.a)
def main():
    a,b,c=3,4,5
    if Triangle.is_valid(a,b,c):
        t=Triangle(a,b,c)
        t1=Triangle.start()
        print(t.area())
        print(t1.area())
    else:
        print('不是三角形')
if __name__=='__main__':
    main()
 '''

##继承
'''
class Person(object):
    def __init__(self,name,age):
        self._name=name
        self._age=age
    @property
    def name(self):
        return self._name
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,age):
        self._age=age
    def play(self):
        print('%s在玩耍'%self._name)
    def watchav(self):
        if self._age>18:
            print('%s在看岛国片'%self._name)
        else:
            print('%s在看喜洋洋'%self._name)
class Student(Person):
    def __init__(self,name,age,grade):
        super().__init__(name,age)#继承时，子类与父类同名，自动覆盖，采用super调用父类方法属性
        self._grade=grade
    def study(self,course):
        print('%s在学习%s'%(self._name,course))
def main():
    stu=Student('徐艳',20,'大二')
    stu.watchav()
    stu.study('英语')
if __name__=='__main__':
    main()
'''        

##多态
#子类继承父类方法后，对父类已有方法重写，使父类同一个行为在子类中拥有不同版本，即为多态
      
##抽象类          
#abc模块的ABCMeta元类和abstractmethod包装器来达到抽象类的效果
#@abstractmethod装饰器实现抽象方法    子类实现了基类的抽象方法才能实例化。   
'''    
from abc import ABCMeta ,abstractmethod
class Pet(object,metaclass=ABCMeta):
    def __init__(self,name):
        self._name=name
    @abstractmethod
    def make_voice(self):
        '发出声音'
        pass
class Dog(Pet):
    def make_voice(self):
        print('%s:汪汪'%self._name)
class Cat(Pet):
    def make_voice(self):
        print('%s:喵喵'%self._name)
def main():
    pets=[Dog('旺财'),Cat('凯迪')]
    for pet in pets:
        pet.make_voice()
if __name__=='__main__':
    main()
'''        
##案例:奥特曼打怪兽
'''
from abc import ABCMeta,abstractmethod    
from random import randint,randrange
class Fighter(object,metaclass=ABCMeta):
    __slots__=('_name','_hp')
    def __init__(self,name,hp):
        self._name=name
        self._hp=hp
    @property
    def name(self):
        return self._name
    @property
    def hp(self):
        return self._hp
    @hp.setter
    def hp(self,hp):
        self._hp=hp if hp>=0 else 0#用法
    @property
    def alive(self):
        return self._hp>0
    @abstractmethod
    def attack(self,hp):
        '攻击'
        pass
class Ultraman(Fighter):
    __slots__=('_name','_hp','_mp')
    def __init__(self,name,hp,mp):
        super().__init__(name,hp)
        self._mp=mp
    def attack(self,other):
        other._hp-=randint(15,25)
    def huge_attack(self,other):
        if self._mp>=50:
            self._mp-=50
            injury = other.hp*3//4#整数除法
            injury =injury if injury>=50 else 50
            other.hp-=injury
            return True
        else:
            self.attack(other)
            return False
    def resume(self):
        incr_point=randint(30,40)
        self._mp+=incr_point
        return incr_point
    def __str__(self):
        return '%s奥特曼'%self._name+\
            '  生命值：%d'%self._hp+'  魔法值：%d'%self._mp
class Monster(Fighter):
    __solt__=('_name','_hp')
    def attack(self,other):
        other.hp-=randint(15,25)
    def __str__(self):#__str__方法叫做这个对象的描写，print(对象)时，打印出属性
        return '%s怪兽'%self._name+'生命值：%d'%self._hp+'\n'
def is_any_alive(monsters):
    for monster in monsters:
        if monster.alive>0:
            return True
    return False
def select_alive_one(monsters):
    monster_len=len(monsters)
    while True:
        index=randrange(monster_len)#随机整数randrange
        monster=monsters[index]
        if monster.alive>0:
            return monster
def display(ultraman,monsters):
    print(ultraman)
    for mons in monsters:
        print(mons,end='')
def main():
    u=Ultraman('迪迦',300,100)
    m1=Monster('鬼灰',400)
    m2=Monster('卢克',300)
    m3=Monster('魔女',250)
    ms=[m1,m2,m3]
    fight_round=1
    while u.alive and is_any_alive(ms):
        print('\n回合%d'%fight_round)
        m=select_alive_one(ms)
        skill=randint(0,10)
        if skill<=6:
            print('%s使用普通攻击打了%s'%(u.name,m.name))
            u.attack(m)
            print('%s的魔法值回复了%d点'%(u.name,u.resume()))
        else:
            if u.huge_attack(m):
                print('%s使用必杀技打了%s'%(u.name,m.name))
            else:
                u.attack(m)
                print('%s的魔法值回复了%d点'%(u.name,u.resume()))
        if m.alive>0:
            print('%s回击了%s'%(m.name,u.name))
            m.attack(u)
        display(u,ms)
        fight_round+=1
    print('\n战斗结束')
    if u.alive>0:
        print('%s胜利'%u.name)
    else:
        print('怪兽胜利')
if __name__=='__main__':
    main()
'''
#关于random
'''
import random
print(random.randint(1,10))
print(random.random())
print(random.uniform(1.2,3.4))
print(random.randrange(2,20,2))
a=[2,3,4,5,2]
print(random.choice(a))
print(random.shuffle(a))            
'''

#__new__与__init__
#_init__是当实例对象创建完成后被调用的，然后设置对象属性的一些初始值      
#__new__是在实例创建之前被调用的，因为它的任务就是创建实例然后返回该实例，是个静态方法   
#__new__在__init__之前被调用，__new__的返回值（实例）
#将传递给__init__方法的第一个参数，然后__init__给这个实例设置一些参数        
class A(object):
    def __init__(self):#参数self，就是这个__new__返回的实例
        print(self)
        print('这是init方法')
    def __new__(cls):#至少要有一个参数cls，代表要实例化的类
        print(id(cls))
        print('这是new方法')
        ret = object.__new__(cls)   
        print(ret)
        return ret#必须要有返回值
    def __del__(self):
        print('回收启动')
print(id(A))
a=A()
a1=a
a2=a
del(a2)
del(a1)
del(a)#del 把内存的所有应用删除，立刻调用__del__方法
#__del__对象回收机制   
    
    
    
    
    
    
    
    
    
    
