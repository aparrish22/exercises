

from typing import LiteralString


def sum(a,b):
    return print(f"{a} + {b} = {a + b}")

def sum_user_input():
    flag = True
    while (True):
        try:
            a = int(input("Enter a for a + b: \n"))
            b = int(input("Enter b for a + b: \n"))
            return print(f"The sum of {a} + {b} = {a + b}")
        except ValueError:
            print("Invalid input. Please try again with an integer.")
            flag = False

def multiply(a,b):
    return print(f"{a} * {b} = {a * b}")

def mult_user_input():
    flag = True
    while (True):
        try:
            a = int(input("Enter a for a * b: \n"))
            b = int(input("Enter b for a * b: \n"))
            return print(f"The multiplication of {a} * {b} = {a * b}")
        except ValueError:
            print("Invalid input. Please try again with an integer.")
            flag = False
            
def print_curr_prev(length):
    curr = 0
    prev = 0
    for n in range(length + 1):
        if curr == prev:
            sum = curr + prev
            curr += 1
            
        else:
            print(f"Current Number {curr}  Previous Number {prev}  Sum {sum}")
            sum = curr + prev
            curr += 1
            prev += 1
        
def even_str(str):
    count = 0
    for char in str:
        if count % 2 == 0:   
            print(f"{char}")
            count += 1
        else:
            count += 1

# using splice!
def remove_chars(str, n):
    print(str[n:])
    
def first_and_last(list):
    try:
        return list[0] == list[-1]
    except IndexError:
        print("Index out of bounds.")
        
def multiples_five_list(list):
    for n in list:
        if n % 5 == 0:
            print(f"{n}")
 
def print_pattern(n):
    for num in range(1, n + 1):
        for i in range(num):
            print(num, end=" ")
        print()
        
def check_palin(str):
    rev_str = str[::-1]
    if str == rev_str:
        print("Yes. given string is palindrome number")
    else:
        print("No. given string is not palindrome number")
    return
        
def odd_even_list(l1, l2):
    new_list = []
    for n in l1:
        if n % 2 != 0:
            new_list.append(n)
    for n in l2:
        if n % 2 == 0:
            new_list.append(n)
    return new_list
        
def odd_even_listc(l1, l2):
    new_list = []
    new_list.append([ n for n in l1 if n % 2 != 0])
    new_list.append([ n for n in l2 if n % 2 == 0])
    return new_list
    

if __name__=="__main__":
    # 10, done
    # Given a two list of numbers, write a program to create a new list
    # such that the new list should contain odd numbers from the first list
    # and even numbers from the second list
    list_1 = [10, 20, 25, 30, 35]
    list_2 = [40, 45, 60, 75, 90]
    print(odd_even_list(list_1, list_2))
    print(odd_even_listc(list_1, list_2))
    
    # 9, done
    str = input("Enter str to see if it's a palindrome: ")
    check_palin(str)
    
    # 8, done
    n = int(input("Enter n numbers: "))
    print_pattern(n)
    
    # 7, done
    str_x = "Austin plays FFXIV. Very cool, Austin is. Aus tin is da best. Heh. Austin . Hey Austin"
    ss = "Austin"
    print(str_x.count(ss))
    
    # 6, done
    my_list = [10,5,60,65,35,24,78,15,9,8]
    multiples_five_list(my_list)

    # 5, done
    list = [4,10,8,5,4]
    result = first_and_last(list)
    print(result)
    
    # 4 done
    remove_chars("Warlock",3)
    
    
    # 3, done
    str = input("Enter a string: ")
    even_str(str)
    
    # 2, done
    try:
        result = int(input("Enter length to sum current and previous number: "))
    except ValueError:
        print("Must be Integer")
        exit()
    print_curr_prev(result)
    
    # 1, done
    sum(6,9)
    sum_user_input()
    multiply(6,9)
    mult_user_input()
    
    
    exit()
