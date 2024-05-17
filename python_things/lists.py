# from time import perf_counter
# import matplotlib.pyplot as plt
# from typing import Any
from timeit import Timer


def f1(r:int)-> list[int]:
    l: list[int] = []
    for i in range(r):
        l.append(i)
    
    return l

def f2(r:int) -> list[int]:
    l: list[int] = []
    for i in range(r):
        l = l + [i]
    
    return l

def f3(r: int) -> list[int]:
    l = [_ for _ in range(r)]
    return l


r = 10
precision = 100

# t1 = Timer(f'f1({r})', "from __main__ import f1")
# t2 = Timer(f'f2({r})', "from __main__ import f2")
# t3 = Timer(f'f3({r})', "from __main__ import f3")

l = [_ for _ in range(1000000)]

t4 = Timer(f'len(l) == 0', "from __main__ import l")
t5 = Timer(f'l == []', "from __main__ import l")

# print(t1.timeit(number=precision), "ms")
# print(t2.timeit(number=precision), "ms")
# print(t3.timeit(number=precision), "ms")
print(t4.timeit(number=precision), "ms")
print(t5.timeit(number=precision), "ms")

# x = []
# y1 = []
# y2 = []
# y3 =[]

# while r < 1000:
#     x.append(r)
#     y1.append(timeit(f1, r))
#     y2.append(timeit(f2, r))
#     y3.append(timeit(f3, r))

# print(timeit(f1, 10000) * 1000)
# print(timeit(f2, 10000) * 1000)
# print(timeit(f3, 10000) * 1000)


#     r = r * 10
# # corresponding y axis values
 
# # plotting the points 
# plt.plot(x, y1)
# plt.plot(x, y2)
# plt.plot(x, y3)
 
# # naming the x axis
# plt.xlabel('x - axis')
# # naming the y axis
# plt.ylabel('y - axis')
 
# # giving a title to my graph
# plt.title('Comparing the performance of differnt way of filling a list')
# # function to show the plot
# plt.show()