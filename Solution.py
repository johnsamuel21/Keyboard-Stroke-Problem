a,b = list(map(int,input().split()))
row,column = 0,0
count = 0
lst = []
for i in range(a):
    lst.append(list(input()))
word = list(input())
word.append("*")
for i in range(len(word)):
    for j in range(len(lst)):
        if word[i] in lst[j]:
            count+=abs(row-j)
            row = j
            pos = lst[j].index(word[i])
            count+= abs(pos-column)
            column = pos
            count+=1
            break
print(count)
