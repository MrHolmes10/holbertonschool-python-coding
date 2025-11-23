#!/usr/bin/python3
"'this module a square class"'
class Square():
    """asdfghj"""
    def __init__(self,size=0):
       if not isinstance(size,int):
           raise TypeError("fuck")
       if size < 0:
           raise ValueError("fuck off")
       self.__size = size
