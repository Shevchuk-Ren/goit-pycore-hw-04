
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



