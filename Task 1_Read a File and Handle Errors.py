
try:
    with open("Assignment-4/sample.txt",'rt') as Aw:
        l=Aw.readlines() # storing as list
        for i in range(len(l)):
            print(f"Line {i+1}: {l[i]}",end="")
except Exception as e:
    print(f"Error: The file 'sample.txt' was not found.")
