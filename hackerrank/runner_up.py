n = int(input())
arr = map(int, input().split())
    
arrlist = []
for num in sorted(arr):
    arrlist.append(num)

max_num = arrlist[-1]
runner_up = arrlist[0]

for num in arrlist:
    if num != max_num: # check num, not runner_up
        runner_up = num
    elif runner_up == max_num:
        break
    
print(runner_up)