# Exercise 1: Find Maximum Element

N = int(input('Enter the number odf elements:'))

elements = []
n = 0
while n < N:
    a = int(input())
    n+=1
    elements.append(a)

print(max(elements))
