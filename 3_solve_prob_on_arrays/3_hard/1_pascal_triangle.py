# Pascal's triangle

from typing import List
def generate(n: int) -> List[List[int]]:
    if n==1:
        return [[1]]
    if n==2:
        return [[1], [1,1]]
    
    lst = [[1], [1,1]]

    for i in range(2,n):
        # take last element from list
        last_ele = lst[-1]
        lst2 = [1]

        for i in range(len(last_ele)-1):
            lst2.append(last_ele[i]+last_ele[i+1])
        
        lst2.append(1)
        lst.append(lst2)
    
    print(lst)


    return


generate(5)