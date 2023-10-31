from collections import deque

def transform_number(a, b):
    queue = deque([(a, [])])  
    while queue:
        current_num, transformations = queue.popleft()
        if current_num == b:
            return transformations  
        next_num_1 = current_num * 2
        next_num_2 = current_num * 10 + 1
        if next_num_1 <= b:
            queue.append((next_num_1, transformations + [next_num_1]))
        if next_num_2 <= b:
            queue.append((next_num_2, transformations + [next_num_2]))
    return None  
a, b = map(int, input().split())
transformations = transform_number(a, b)

if transformations is None:
    print("NO")
else:
    print("YES")
    print(len(transformations))
    print(a, end=" ")
    for transformation in transformations[:-1]: 
        print(transformation, end=" ")
    print(b)