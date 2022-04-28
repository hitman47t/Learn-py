from time import time


def timedec(func):

    def wrap(*args):
        start_time = time()
        res = func(*args)
        end_time = time()
        res_time = end_time - start_time
        print("func_name = ", func)
        print("\tres_time", res_time)
        print("\tres = ", res)
        return res

    return wrap

def power(*args, st=None):
    return [v**st for v in args]

@timedec
def num(num_list,mode):
    def isPrime(numb):
        if [x for x in range(2, numb) if numb % x == 0] == []:
            return True
        else:
            return False
    if mode == "even":
        res = [x for x in num_list if x % 2 == 0]
    elif mode == "odd":
        res = [x for x in num_list if x % 2 != 0]
    elif mode == "prime":
        res = [x for x in num_list if isPrime(x) == True]
    else:
        res = None
    return res

print(power(5,2,3, st=4))
nums = [1,2,3,4,5,15,19,20,99]
print(num(nums,"even"))
print(num(nums,"odd"))
print(num(nums,"prime"))
print(num(nums,"prime2"))
