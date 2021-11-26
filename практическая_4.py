# -*- coding: utf-8 -*-
"""Практическая 4

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-0ZG7a8YX1agMx2g5uaPlZAn5t2Ba1TN

![image.png](data:image/png;base64,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)
"""

class Izdanie:
  def __init__(self,name,data_release,autor,izdanie = 'Crystall'):
    self.name = name
    self.release = data_release
    self.autor = autor
    self.izdanie = izdanie
  def presentation(self):
    print('А вот и продукция нашего издания {}'.format(self.izdanie))

class Magazine(Izdanie):
  def details(self,topic,star):
    self.topic = topic
    self.star = star
    print('Тема выпуска: {} Лицо журнала: {}'.format(self.topic,self.star))
  def reading(self,evaluation):
    self.evaluation = evaluation
    if self.evaluation >=4:
      print('Читатель советует журнал {} к прочтению.'.format(self.name,self.evaluation))
    elif self.evaluation == 3:
      print('Журнал {} имеет свои недочёты.'.format(self.name,self.evaluation))
    else:
      print('Журнал {} читателю не понравился.'.format(self.name,self.evaluation))
  def __str__(self):
    print('Название журнала: {} \nГод выпуска журнала: {} \nГлавный редактор: {} \nНазвание издания: {}'.format(self.name, self.release, self.autor, self.izdanie))


class Book(Izdanie):
  def review(self, heroes, topic):
    self.heroes = heroes
    self.topic = topic
    print('Герои книги {} : {} \nТема книги: {}'.format(self.name,self.heroes,self.topic))
  def reading(self,like):
    self.like = like
    if self.like ==  "Да":
        print('Книга {} понравилась читателю'.format(self.name))
    elif self.like == "да":
       print('Книга {} понравилась читателю'.format(self.name))
    elif self.like == "Нет":
       print('Книга {} мне не понравилась'.format(self.name))
    elif self.like == "нет":
       print('Книга {} не понравилась читателю'.format(self.name))
    else:
        print('Читатель не может сказать ничего конкретного по поводу книги {}'.format(self.name))  
  def __str__(self):
    print('Название книги: {} \nГод написания книги: {} \nАвтор книги: {} \nНазвание издания: {}'.format(self.name, self.release, self.autor, self.izdanie))


class Textbook(Book):
    def details(self,Object):
      self.Object = Object
      print('Перед нами учебник по предмету {}'.format(self.Object))  
    def __str__(self):
      print('Название учебника: {} \nГод написания учебника: {} \nАвтор учебника: {} \nНазвание издания: {}'.format(self.name, self.release, self.autor, self.izdanie))
  
    
b = Magazine('Vogue Russia', '2021', 'Ксения Соловьёва')
b.presentation()
b.__str__()
b.details('Мода', 'Ирина Шейк')
b.reading(int(input('Оцените журнал от 1 до 5: '))) 


m = Textbook('Enjoy English','2020','Биболетова')
m.presentation()
m.__str__()  
m.details(input('Укажите по какому предмету учебник: '))
m.reading(input('"Вам понравилась книга? (Да/Нет) - ')) 

d = Book('Старуха Изергиль', '1894', 'М.Горький')
d.presentation()
d.__str__()
d.review('Данко, Старуха Изергиль', 'самопожертвование и эгоизм')
d.reading(input("Вам понравилась книга? (Да/Нет) - "))