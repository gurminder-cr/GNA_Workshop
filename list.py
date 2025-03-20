a=[12,14,18,90]
b=[45,14,18,99]

# output-- [(14,14),(18,18)]
li=[]
for i in a:
    for j in b:
        if i==j:
            li.append((i,j))
            
print(li)
# list comprehension -- 
l=[(i,j) for i in a for j in b if i==j]
print(l)
            

