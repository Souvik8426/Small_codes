#basically this is multplication with out using * symbol just adding a number n m times
m = int(input("Enter First number: "))
n = int(input("Enter Second number: "))
result = 0
for i in range(1,m+1):
    result = result + n
print(result)
