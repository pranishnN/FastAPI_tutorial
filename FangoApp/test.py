l = [15, 85, 35, 89, 125, 5, 69, 2, 36, 57, 1]

print()
def find_max(lst):
    cur_val = 0
    max_v = 0
    for i in range(len(lst)):
        cv = lst[i]
        
        if cv > max_v:
            # cur_val = lst[i-1]
            cur_val = max_v
            max_v = cv

        # while pi >= 0 and lst[pi] > cv:
        #     lst[pi+1] = lst[pi]
        #     lst[pi] = cv
        #     pi -= 1



    return max_v, cur_val

# print(find_max(l))

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}

def mrge_dict(d1:dict, d2:dict):

    for x in (d2.items()):
        # print(x)
        if x[0] in d1.keys():
            d1[x[0]] = d1[x[0]] + x[1]
        else:
            d1[x[0]] = x[1]

    return d1

# print(mrge_dict(dict1, dict2))

# s = [3, 5, 2, -4, 8, 11] 
s = [3, 5, 6, 2, -4, 8, 11,1]

sum = 7

def rtn_sum_vals(lst, val):
    nl = []
    a,b = 0,0

    for i in range(len(lst)):
        a = lst[i]
        for j in lst:
            if (a + j) == val:
                b = j
                print(a,b)
                # nl.append((a,b))

        # if (lst[i] + lst[i+1]) % val == 0:
        #     a = lst[i]
        #     b = lst[i+1]
    # return nl
    return a,b

# print(rtn_sum_vals(s, sum))

nums = [1, 2, 3, 2, 1, 3, 2, 4, 5, 4]

def count_num(lst):
    d = {}
    for i in lst:
        if i in d.keys():
            d[i] = d[i] + 1
        else:
            d[i] = 1

    return d

# print(count_num(nums))

import copy
dt = {"a":2,"b":3,"t":4}

dft = copy.deepcopy(dt)

dt["f"] = 5

print(dft)
