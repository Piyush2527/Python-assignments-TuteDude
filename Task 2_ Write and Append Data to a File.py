filename="output.txt"

with open(f"Assignment-4/{filename}","wt") as T2:
    T2.write(input("Enter text to write to the file: "))
    print(f"Data successfully written to {filename}.")
print()
with open(f"Assignment-4/{filename}","at") as T2:
    T2.write("\n"+input("Enter additional text to append: "))
    print("Data successfully appended.")
print()
with open(f"Assignment-4/{filename}","rt") as T2:
    l=T2.readlines()
    print(f'Final content of {filename}:')
    for i in range(len(l)):
        print(l[i],end="")