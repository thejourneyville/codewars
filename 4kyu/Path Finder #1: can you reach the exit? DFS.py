def path_finder(maze):

    size = len(maze.split("\n"))
    string = "".join(maze.split("\n"))
    
    graph, outer, inner = {}, [], []
    for idx, ele in enumerate(string):
        if idx % size == 0 and idx != 0:
            outer.append(inner)
            inner = []
        if ele == "W":
            inner.append("W")
            continue
        inner.append(idx)
        graph[idx] = []
    outer.append(inner)
    
    for row in range(size):
        for col in range(size):
            
            if outer[row][col] != "W":
                current = outer[row][col]

                #UP
                if row > 0:
                    if outer[row - 1][col] != "W":
                        graph[current].append(outer[row - 1][col])
                #DOWN
                if row < size - 1:
                    if outer[row + 1][col] != "W":
                        graph[current].append(outer[row + 1][col])
                #LEFT
                if col > 0:
                    if outer[row][col - 1] != "W":
                        graph[current].append(outer[row][col - 1])
                #RIGHT
                if col < size - 1:
                    if outer[row][col + 1] != "W":
                        graph[current].append(outer[row][col + 1])
    
    
    # DFS
    stack = [outer[0][0]]
    visited = set()
    
    while len(stack) > 0:
        current = stack.pop()
        visited.add(current)
        if current == outer[size - 1][size - 1]:
            return True
        
        for neighbor in graph[current]:
            if neighbor not in visited:
                stack.append(neighbor)
    
    
    return False
