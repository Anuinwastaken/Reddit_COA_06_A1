#Original Code by amiroo4
#Edited by Anuin

grid: list = []
with open("data.txt", "r") as file:
    line = file.readline()
    while line:
        grid.append([i for i in line.strip()])
        line = file.readline()

guard: list = [0, 0]
for x, row in enumerate(grid):
    if "^" in row:
        guard = (x, row.index("^"))

def print_grid(grid: list) -> None:
    for row in grid:
        print("".join(row))
    print()

running = True

try:
    while running:
        match grid[guard[0]][guard[1]]:
            case "^":
                if grid[guard[0]-1][guard[1]] != "#":
                    grid[guard[0]][guard[1]] = "X"
                    guard = (guard[0]-1, guard[1])
                    grid[guard[0]][guard[1]] = "^"
                else:
                    grid[guard[0]][guard[1]] = ">"
            case ">":
                if grid[guard[0]][guard[1]+1] != "#":
                    grid[guard[0]][guard[1]] = "X"
                    guard = (guard[0], guard[1]+1)
                    grid[guard[0]][guard[1]] = ">"
                else:
                    grid[guard[0]][guard[1]] = "v"
            case "v":
                if grid[guard[0]+1][guard[1]] != "#":
                    grid[guard[0]][guard[1]] = "X"
                    guard = (guard[0]+1, guard[1])
                    grid[guard[0]][guard[1]] = "v"
                else:
                    grid[guard[0]][guard[1]] = "<"
            case "<":
                if grid[guard[0]][guard[1]-1] != "#":
                    grid[guard[0]][guard[1]] = "X"
                    guard = (guard[0], guard[1]-1)
                    grid[guard[0]][guard[1]] = "<"
                else:
                    grid[guard[0]][guard[1]] = "^"
            case _:
                break

        if guard[0] < 0 or guard[0] > len(grid) or guard[1] < 0 or guard[1] > len(grid):
            grid[guard[0]][guard[1]] = "X"
            running = False
except KeyboardInterrupt:
    print(guard)

grid[guard[0]][guard[1]] = '\033[42m' + "G" + "\033[0m"
print_grid(grid)

def count_waypoints(puzzle: list) -> int:
    count: int = 0
    for row in puzzle:
        count += row.count('X')
    return count
print(count_waypoints(grid))