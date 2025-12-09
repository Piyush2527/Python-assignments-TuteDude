# # Factorial using recursion
# def fact_recu(num):
#     if num==1: #base/terminate condition
#         return 1
#     else: # main recursion condition
#         fact=num*fact_recu(num-1)
#         return fact
# n=int(input("Enter a number: "))
# print(f'Factorial of {n} is: {fact_recu(n)}')

# factorial using loop
def fact_loop(num):
    fact=1
    for i in range(num):
        fact=fact*(i+1)
    return fact

n=int(input("Enter a number: "))
print(f'Factorial of {n} is: {fact_loop(n)}')