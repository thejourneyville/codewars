def path_finder(maze):

    def formatter(string):
        raw = "".join(string.split("\n"))
        outer, inner = [], []
        for idx, ele in enumerate(raw):
            if idx % rows == 0 and idx != 0:
                outer.append(inner)
                inner = []
            inner.append(ele)
        outer.append(inner)
        return outer

    rows = maze.count("\n") + 1
    cols = rows
    graph = formatter(maze)
    start = (0, 0)
    end = (rows - 1, cols - 1)
    visited = {end: None}
    queue = [end]

    if any([graph[0][0] == "W", graph[rows - 1][cols - 1] == "W"]):
        return False

    while queue:

        current = queue.pop(0)

        if current == start:
            return True

        current_row, current_col = current[0], current[-1]

        neighbors = []
        if current_row > 0:
            if graph[current_row - 1][current_col] == ".":
                neighbors.append((current_row - 1, current_col))
        if current_row < rows - 1:
            if graph[current_row + 1][current_col] == ".":
                neighbors.append((current_row + 1, current_col))
        if current_col > 0:
            if graph[current_row][current_col - 1] == ".":
                neighbors.append((current_row, current_col - 1))
        if current_col < cols - 1:
            if graph[current_row][current_col + 1] == ".":
                neighbors.append((current_row, current_col + 1))

        for neighbor in neighbors:
            if neighbor not in visited:
                visited[neighbor] = current
                queue.append(neighbor)

    return False
