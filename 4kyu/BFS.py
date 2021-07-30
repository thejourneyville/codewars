# def path_finder(maze):
#     rows = maze.count("\n") + 1
#     cols = rows
#     min_distance = (rows - 1) * 2
#
#
#     if any([maze[0] == "W", maze[-1] == "W"]):
#         return False
#
#     maze = "".join(maze.split())
#     grid, inner, cell = [], [], 0
#     for idx in range(len(maze)):
#
#         if idx % cols == 0 and idx != 0:
#             grid.append(inner)
#             inner = []
#
#         if maze[idx] == ".":
#             inner.append(cell)
#             cell += 1
#         else:
#             inner.append("W")
#             cell += 1
#
#     grid.append(inner)
#     for i in grid:
#         print(i)
#
#
#     # BFS
#     start_point = grid[0][0]
#     end_point = grid[-1][-1]
#     visited = {end_point: None}
#     queue = [end_point]
#
#     while queue:
#         current_cell = queue.pop(0)
#
#         if current_cell == start_point:
#             shortest_path = []
#
#             while current_cell:
#                 shortest_path.append(current_cell)
#                 current_cell = visited[current_cell]
#
#             return shortest_path
#
#         else:
#             neighbors = []
#
#             for row in range(rows):
#                 for col in range(cols):
#
#                     if grid[row][col] != "W" and grid[row][col] == current_cell:
#
#                         if col < cols - 1:
#                             if grid[row][col + 1] != "W" and grid[row][col + 1]:
#                                 neighbors.append(grid[row][col + 1])
#
#                         if row < rows - 1:
#                             if grid[row + 1][col] != "W" and grid[row + 1][col]:
#                                 neighbors.append(grid[row + 1][col])
#
#                         if col > 0:
#                             if grid[row][col - 1] != "W" and grid[row][col - 1]:
#                                 neighbors.append(grid[row][col - 1])
#
#                         if row > 0:
#                             if grid[row - 1][col] != "W" and grid[row - 1][col]:
#                                 neighbors.append(grid[row - 1][col])
#                         for point in neighbors:
#                             if point not in visited:
#                                 print(visited)
#                                 visited[point] = current_cell
#                                 queue.append(point)



    # print(graph)
    # visited_list = []
    # queue = []
    #
    # def bfs(visited, tree, node):
    #
    #     queue.append(node)
    #     visited.append(node)
    #
    #     while queue:
    #         n = queue.pop(0)
    #         print(n, end="->")
    #         for neighbor in tree[n]:
    #             if neighbor not in visited:
    #                 visited.append(neighbor)
    #                 if n == grid[-1][-1]:
    #                     shortest_path = []
    #                     while n:
    #                         shortest_path.append(n)
    #                         if tree[n]:
    #                             n = tree[n]
    #                     return shortest_path
    #
    #                 queue.append(neighbor)
    #
    # bfs(visited_list, graph, 0)




# a = "\n".join([
#     ".W.",
#     ".W.",
#     "..."
# ])
#
# b = "\n".join([
#     ".W.",
#     ".W.",
#     "W.."
# ])
#
# c = "\n".join([
#     "......",
#     "......",
#     "......",
#     "......",
#     "......",
#     "......"
# ])
#
# d = "\n".join([
#     "......",
#     "......",
#     "......",
#     "......",
#     ".....W",
#     "....W."
# ])
# for test in [a, b, c, d]:
#     print(path_finder(test))
#     print()



# tree = {
#     6: [3, 1, 9],
#     3: [4, 7],
#     1: [9],
#     4: [],
#     7: [2, 5],
#     8: [1],
#     9: [],
#     2: [],
#     5: [8]
# }
#
# visited_list = []
# queue = []
#
#
# def bfs(visited, graph, node):
#
#     queue.append(node)
#     visited.append(node)
#
#     while queue:
#         n = queue.pop(0)
#         print(n, end="->")
#         for neighbor in graph[n]:
#             if neighbor not in visited:
#                 visited.append(neighbor)
#                 queue.append(neighbor)
#
#
# bfs(visited_list, tree, 6)


def grid(maze):
    ''' Maze Properties'''
    num_rows = len(maze)
    num_cols = len(maze[0])
    end_pt = (num_cols - 1,num_rows - 1)
    start_pt = (0, 0)

    '''BFS'''
    visited = {end_pt: None}
    queue = [end_pt]
    while queue:
        current = queue.pop(0)
        if current == start_pt:
            shortest_path = []
            while current:
                shortest_path.append(current)
                current = visited[current]
            return shortest_path
        adj_points = []
        '''FIND ADJACENT POINTS'''
        current_col, current_row = current
        #UP
        if current_row > 0:
            if maze[current_row - 1][current_col] == " ":
                adj_points.append((current_col, current_row - 1))
        #RIGHT
        if current_col < (len(maze[0])-1):
            if maze[current_row][current_col + 1] == " ":
                adj_points.append((current_col + 1, current_row))
        #DOWN
        if current_row < (len(maze) - 1):
            if maze[current_row + 1][current_col] == " ":
                adj_points.append((current_col, current_row + 1))
        #LEFT
        if current_col > 0:
            if maze[current_row][current_col - 1] == " ":
                adj_points.append((current_col - 1, current_row))

        '''LOOP THROUGH ADJACENT PTS'''
        for point in adj_points:
            if point not in visited:
                visited[point] = current
                queue.append(point)

maze = [[' ', '#', ' ', '#', ' '],
        [' ', '#', ' ', ' ', ' '],
        [' ', '#', ' ', '#', ' '],
        [' ', '#', ' ', '#', ' '],
        [' ', '#', ' ', '#', ' '],
        [' ', ' ', ' ', '#', ' '],
        [' ', ' ', '#', '#', ' '],
        [' ', ' ', '#', ' ', ' '],
        ['#', ' ', '#', ' ', '#'],
        [' ', ' ', '#', ' ', ' ']]

print(grid(maze))