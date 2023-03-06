# python3
# 221RDB128 Bernhards Arnitis
import sys
import threading



def compute_height(n, parents):
    max_height = 0
    nodes = [[] for _ in range(n)]
    root = None
    for i in range(n):
        parent = parents[i]
        if parent == -1:
            root = i
        else:
            nodes[parent].append(i)
    st = [(root, 1)]
    while st:
        node, height = st.pop(0)
        if height > max_height:
            max_height = height
        max_height = max(max_height, height)
        for child in nodes[node]:
            st.append((child, height+1))
    return max_height


def main():
    # implement input form keyboard and from files
    text = input()
     
    if text == "I":
        n = int(input())
        parents = list(map(int, input().split()))
        print(compute_height(n, parents))
    else:
        print("Invalid")
        
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
