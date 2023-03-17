
def print_operation_table(operation, a=6, b=6):
    for i in range(1,b+1):
        for j in range(1,a+1):
            print(operation(i,j), end=" ")
        print()

print_operation_table(lambda x, y: x * y)