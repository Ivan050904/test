
int_list = [17,28,24,31,3,5,7]


def apply_all_func(int_list,*functions):
    results = {}
    for func in functions:
        func_name = func.__name__
        results[func_name] = func(int_list)
    return results


def summ(lst):
    return sum(lst)

def lenn(lst):
    return len(lst)

def sortedd(lst):
    return sorted(lst)

def maxim(lst):
    return max(lst)

def minn(lst):
    return min(lst)

print(apply_all_func(int_list,summ,lenn,sortedd,maxim,minn))
    
 