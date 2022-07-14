#Assignment:

#Write a program to generate the first 15 fibonacci numbers.

#1,1,2,3,5,8,13 ...

#A fibonacci number is the sum of the previous two fibonacci numbers.

fib = [1,1]
for i in range(13):
    fib.append(fib[-1] + fib[-2])
print(fib)
#%%
