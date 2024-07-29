from pathlib import Path
import sys
import os
from pathlib import Path
import colorama

#TASK 1

def total_salary(path):
    total = 0
    counter = 0
    average = 0
    
    try:
       with open(path, "r") as fh:
        for line in fh.readlines():
          if line.strip().split(',')[-1].isdigit():
             total = total + int(line.strip().split(',')[-1])
             counter = counter + 1

       average = int(total/counter)
    
       return total, average
       
    except FileNotFoundError:
       print(f"No such file or directory: {path}")
       return 0,0
    except ZeroDivisionError:
       print('You cant devide by 0')
       return 0,0
    

total, average = total_salary("/home/ran/Documents/STUDY/GoIT/list.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

total, average = total_salary("path/to/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}") # error


# TASK 2

example = [
    {"id": "60b90c1c13067a15887e1ae1", "name": "Tayson", "age": "3"},
    {"id": "60b90c2413067a15887e1ae2", "name": "Vika", "age": "1"},
    {"id": "60b90c2e13067a15887e1ae3", "name": "Barsik", "age": "2"},
    {"id": "60b90c3b13067a15887e1ae4", "name": "Simon", "age": "12"},
    {"id": "60b90c4613067a15887e1ae5", "name": "Tessi", "age": "5"},
]

def get_cats_info(path):
   dict_cats = []
   try:
      with open(path, "r") as fh:

        for line in fh.readlines():
             
             if not line.strip() == '':
               
               line_list = line.strip().split(',')
               dict_cats.append({"id": line_list[0], "name": line_list[1], "age": line_list[2]})

      return dict_cats
   
   except FileExistsError:
      print(f"No such file or directory: {path}")
   
cats_info = get_cats_info("/home/ran/Documents/STUDY/GoIT/cats.txt")
print(cats_info)

