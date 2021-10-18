def make_matrix(m: int, n: int) -> str:



    x_start, x_end = 0, n - 1
    expand = True

    matrix, inner = "", []
    for row in range(n):
        for col in range(n):
            if col == x_start or col == x_end:
                inner.append(str(m)[0])
            elif col >= x_start and col <= x_end and row != n // 2:
                if expand:
                    inner.append(str(m)[1])
                else:
                    inner.append(str(m)[2])
            elif col < x_start or col > x_end:
                if col < n // 2:
                    inner.append(str(m)[3])
                elif col > n // 2:
                    inner.append(str(m)[4])

        if row < n - 1:
            matrix += " ".join(inner) + "\n"
        else:
            matrix += " ".join(inner)
        inner = []

        if expand:
            x_start += 1
            x_end -= 1
        else:
            x_start -= 1
            x_end += 1

        if x_start == x_end:
            expand = False

    return matrix


print(make_matrix(13579, 7))
