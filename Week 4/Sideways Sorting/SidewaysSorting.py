## Author: Daniella Seum, dseum2023@my.fit.edu
## Course: CSE 2050, Fall 2024
## Project: Sideways Sorting, week 4, problem B

def sideways_sorting():
    while True:
        try:
            line = input()
            if not line.strip():
                continue
            r, c = map(int, line.strip().split())
            if r == 0 and c == 0:
                break
            matrix = []
            for _ in range(r):
                while True:
                    row = input()
                    if row.strip():
                        break
                if len(row) < c:
                    row += ' ' * (c - len(row))
                matrix.append(list(row))
            columns = []
            for col_idx in range(c):
                col = [matrix[row_idx][col_idx] for row_idx in range(r)]
                sort_key = ''.join(col).lower()
                columns.append((col_idx, col, sort_key))
            columns.sort(key=lambda x: x[2])
            sorted_columns = [col for idx, col, key in columns]
            result = []
            for row_idx in range(r):
                row = ''.join(sorted_columns[col_idx][row_idx] for col_idx in range(c))
                result.append(row)
            for row in result:
                print(row)
            print()
        except EOFError:
            break


sideways_sorting()
