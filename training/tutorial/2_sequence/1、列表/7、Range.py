#range函数可以生成一个自然数的序列。 
r = range(5)
print(r)
print(list(r))
#将会生成一个从0-4的序列，[0,1,2,3,4]。
#与slice类似，一共有三个参数，用，区分。分别为起点终点步长。
r = range(3,20,2)
print(r)
print(list(r))

#通过采用for循环，可以遍历整个range序列。
#通常用于配合for循环使用，与while循环不同，for循环不会造成死循环。
#与while循环类似，包括else，break，continue都可在for循环使用。
