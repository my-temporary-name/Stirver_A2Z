# Given a data type, help Geek in finding the size of it in byte.

def dtype_size(str):
    if str=="character":
        return 1
    elif str=="integer":
        return 4
    elif str=="float":
        return 4
    elif str=="double":
        return 8
    elif str=="long":
        return 8
    else:
        return -1
    
# Driver code
if __name__ == '__main__':
    print(dtype_size("character"))
    print(dtype_size("integer"))
    print(dtype_size("float"))
    print(dtype_size("double"))
    print(dtype_size("long"))