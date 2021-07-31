# SHORTEST PATH USING BREADTH FIRST SEARCH

def formatter(maze):
    """
    maze = "\n".join([
                    ".W.",
                    ".W.",
                    "..."
    ])
    :param maze: takes the string format (above)
    :return: returns each element of the string as a cell in a nested list
    """

    rows = maze.count("\n") + 1
    cols = rows

    grid = "".join(maze.split())
    outer, inner = [], []
    for idx in range(len(grid)):

        if idx % cols == 0 and idx != 0:
            outer.append(inner)
            inner = []

        if grid[idx] == ".":
            inner.append(".")
        else:
            inner.append("W")

    outer.append(inner)
    return outer


def path_finder(grid):
    maze = formatter(grid)  # formats maze as a nested list

    rows = len(maze)
    cols = len(maze[0])
    start = (0, 0)
    end = (rows - 1, cols - 1)

    visited = {end: None}  # dict to keep track of {visited cells: its neighbors}
    queue = [end]  # list of cells to examine to determine its neighbors (if any)

    while queue:
        current = queue.pop(0)  # the first element is taken from the queue following FIFO

        if current == start:  # if the currently examine cell is the starting position
            path = []
            while current:
                path.append(current)  # append the current position to the path
                current = visited[current]  # the current position becomes its neighbor

            if path[-1] == end:  # if the last position of path equals the ending coordinate, the path has been solved
                return len(path) - 1  # returns the number of steps (not including the starting point)

        neighbors = []
        current_row, current_col = current[0], current[-1]

        #  eligible neighbors are searched for and appended to neighbors
        # UP
        if current_row > 0:  # the current row must be at least 1 to search for a row above it (0)
            if maze[current_row - 1][current_col] == ".":
                neighbors.append((current_row - 1, current_col))

        # DOWN
        if current_row < rows - 1:  # the current row must be at least 1 less than the last row
            # to search for a row above it (0)
            if maze[current_row + 1][current_col] == ".":
                neighbors.append((current_row + 1, current_col))

        # LEFT
        if current_col > 0:  # follows the same requires as rows but with columns
            if maze[current_row][current_col - 1] == ".":
                neighbors.append((current_row, current_col - 1))

        # RIGHT
        if current_col < cols - 1:
            if maze[current_row][current_col + 1] == ".":
                neighbors.append((current_row, current_col + 1))

        for neighbor in neighbors:  # looking at the neighbors list, if it's not a key in visited, it will be added
            # to the dictionary visited as a key and the current cell will be it's value indicating its origin
            if neighbor not in visited:
                visited[neighbor] = current
                queue.append(neighbor)  # the neighbor is appended to the queue to wait its turn to be examined

    return False  # if the current cell has no neighbors, the path cannot be completed and False is returned
