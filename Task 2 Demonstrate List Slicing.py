l=[]
for i in range(10):
    l.append(i+1)
print(f'Original List: {l}')

Elist=[]
for i in range(5):
    Eelement=l.pop(0)
    Elist.append(Eelement)
print("Extracted first five elements: ",Elist)

Elist=Elist[::-1]
print(f'Reversed Extracted elements: {Elist}')