''' multiples of three or five '''
''' Find the sum of all the multiples of 3 or 5 below 1000 '''


def sum_multiples(max_num):
    sum = 0
    for n in range(max_num):
        if (is_multiple(n)):
            sum += n
        else:
            continue
    return sum
            

def is_multiple(num):
    ''' check if number is multiple of 3 or 5 '''
    if num % 3 == 0 or num % 5 == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    max_num = 1000
    print(sum_multiples(max_num))
