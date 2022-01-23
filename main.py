# -*- coding: utf-8 -*-
import random

f = open('restaurant.txt', 'r')

list = f.readlines() #リストとして読み込む

random.shuffle(list)
print(list[0])

f.close()