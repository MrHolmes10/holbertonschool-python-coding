#!/usr/bin/python3
"'this is a class'"

class Square:
   ""a class is that""
   
   def __init__(self,size=0):
       if  not isinstance(size,int):
           raise TypeErroe("size must be an integer")
       if size < 0:
           raise ValueError("size must be >= 0")
       self.__size = size
  
   def area(self):
      """DEFAS"""
      return self.__size ** 2
