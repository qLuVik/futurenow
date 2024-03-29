# -*- coding: utf-8 -*-
"""Практическая 1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nPFnUS60WjZiXgyPmC41AdzZZBqeG0qM
"""

#1
class First:
  color = "red"
  def out(self):
    print(self.color + "!")

obj1 = First()    
obj2 = First()
print(obj1.color)
print(obj2.color)
obj1.out()
obj2.out()

class Second:
  color = "red"
  form = "circle"
  volume = "2D"
  def changecolor(self,newcolor):
    self.color = newcolor
  def changeform(self,newform):
    self.form = newform
  def changevolume(self,newvolume):
    self.volume = newvolume  

obj1 = Second()
obj2 = Second()
obj3 = Second()

print(obj1.color, obj1.form, obj1.volume)
print(obj2.color, obj2.form, obj2.volume)
print(obj3.color, obj3.form, obj3.volume)

obj1.changecolor("green")
obj2.changecolor("blue")
obj2.changeform("oval")
obj3.changecolor("yellow")
obj3.changeform("triangle")
obj3.changevolume("3D")

print(obj1.color,obj1.form, obj1.volume)
print(obj2.color,obj2.form, obj2.volume)
print(obj3.color,obj3.form, obj3.volume)

class Grass:
  def __init__(self,color):
    self.color = color
class Cow:
  def __init__(self,name):
    self.name = name
  def eat(self, col):
    self.col = col
    print("Корова по кличке {} ест траву цвета {}".format(self.name,self.col))  
obj1 = Cow("Сусанна")    
obj2 = Grass("зелёный")
obj1.eat(obj2.color)

#3
class YesInit:
  def __init__(self,one,two):
    self.fname = one
    self.sname = two
obj1 = YesInit("Peter","Ok")

print(obj1.fname,obj1.sname)
class NoInit:
  def names(self,one,two):
    self.fname = one
    self.sname = two
objl = NoInit()    
objl.names("Peter","Ok")
print(objl.fname,objl.sname)

#4
class Fruits:
  def __init__(self,w,n=0):
    self.what = w
    self.numbers = n
f1 = Fruits("apple",150)    
f2 = Fruits("pineapple")
print(f1.what,f1.numbers)
print(f2.what,f2.numbers)
#class Fruits:
#  def __init__(self,n=0,w): #ERROR
#    self.what = w
#    self.numbers = n
#f1 = Fruits(150,"apple")    
#f2 = Fruits("pineapple")
#print(f1.what,f1.numbers)
#print(f2.what,f2.numbers)

#6
class Building: #класс
  def __init__(self,w,c,n=0): #конструктор класса
    self.what = w
    self.color = c
    self.numbers = n
    self.mwhere(n)
 #выводим в отдельную функцию, чтобы
  def mwhere(self,n): #метод определения наличия на скаладе || создается атрибут where объектов
    if n <=0:
      self.where = "отсутствуют"
    elif 0 < n < 100:
      self.where = "малый склад"
    else:
      self.where = "основной склад"

  def plus(self,p): #метод добавления кол-ва предметов на склад
    self.numbers = self.numbers + p
    self.mwhere(self.numbers)
  def minus(self,m):          #метод убавления кол-ва предметов со склада
    self.numbers = self.numbers - m
    self.mwhere(self.numbers)

#объекты
m1 = Building("доски", "белые", 50)
m2 = Building("доски", "коричневые", 300)
m3 = Building("кирпичи", "белые")

print(m1.what,m1.color,m1.where)
print(m2.what,m2.color,m2.where)
print(m3.what,m3.color,m3.where)

m1.plus(500)
print(m1.numbers, m1.where)

class Books:
  def __init__(self,n,a,p):
    self.name = n
    self.autor = a
    self.pages = p
t1 = Books("Кому на Руси жить хорошо", "Николай Некрасов", 391)
t2 = Books("Преступление и наказание", "Федор Достоевский", 570)    
print("Название книги: {} \nАвтор книги: {} \nКол-во страниц: {}".format(t1.name,t1.autor,t1.pages))
print("Название книги: {} \nАвтор книги: {} \nКол-во страниц: {}".format(t2.name,t2.autor,t2.pages))

class Things:
  def __init__(self,n,t,c=""):
    self.namething = n
    self.total = t
    self.color = c
th1 = Things("table",5)
th2 = Things("computer",7)
print(th1.namething,th1.total)
print(th2.namething,th2.total)    
th1.color = "green"
print(th1.color)
print(th2.color)

class Table:
  def __init__(self, l,w,h):# инициализация конструктора для класа табле в котором три параметра
    self.long = l   
    self.width = w
    self.height = h
  def outing(self):
    print(self.long,self.width,self.height)
class Kitchen(Table):
  def howplaces(self,n):
    if n < 2:
      print("Это не кухонный стол")
    else:
      self.places = n  
  def outplaces(self):
    print(self.places)
class DeskTable(Table):
  def square(self):
    return self.width * self.long
  def color(self,c):
    self.color = c 
    return print("Этот стол {}".format(self.color))

t_room1 = Kitchen(2,1,0.5)
t_room1.outing()
t_room1.howplaces(5)
t_room1.outplaces()

t_2 = Table(1,3,0.7)
t_2.outing()

t_3 = DeskTable(3,6,0.6)
t_3.outing()
t_3.square()
t_3.color("красный")
#t_2.howplaces(8)

class Figure:
  def __init__(self):
    self.color = "Белый"

  def changecolor(self,color):
    self.color = color  
    return self.color

class Oval(Figure):
  def __init__(self,s,color):
    Figure.__init__(self)
    self.square = s

class Square(Figure):
  def __init__(self,s,color):
    Figure.__init__(self)
    self.square = s

f1 = Oval(13,"")
f1.changecolor("Красный")
print("{} овал имеет площадь равную {}".format(f1.color,f1.square))
f2 = Square(16, "")
print("{} квадрат имеет площадь равную {}".format(f2.color,f2.square))