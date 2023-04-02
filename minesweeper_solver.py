# PROJECT BRIEFING: 
# Create a function that takes a grid of # and -, where each hash (#) represents a
# mine and each dash (-) represents a mine-free spot. Return a grid, where each dash
# is replaced by a digit, indicating the number of mines immediately adjacent to the 
# spot i.e. (horizontally, vertically, and diagonally).

# Provide minesweeper grid where each hash (#) represents a mine and 
# each dash (-) represents a mine-free spot.
minesweeper = [ ["-", "-", "-", "#", "#"],
                ["-", "#", "-", "-", "-"],
                ["-", "-", "#", "-", "-"],
                ["-", "#", "#", "-", "-"],
                ["-", "-", "-", "-", "-"]]

# Calculate the number of rows and number of columns.
row_number = len(minesweeper)
for rows in range(row_number):
    column_number = len(minesweeper[rows])

# Function to determine the number of mines immediately adjacent to a 
# given grid location or providing a hash (#) to indicate the presence 
# of a mine. Account for going out of bounds of the grid.
def mine_count(row, column):
    total = 0
    if minesweeper[row][column] == "#":
        total = "#"
    if minesweeper[row][column] != "#":
        if row > 0 and column > 0:
            if minesweeper[row-1][column-1] == "#":
                total += 1
        if row > 0:    
            if minesweeper[row-1][column] == "#":
                total += 1
        if row > 0 and (column < (column_number-1)):
            if minesweeper[row-1][column+1] == "#":
                total += 1
        if column > 0:
            if minesweeper[row][column-1] == "#":
                    total += 1
        if column < (column_number-1):
            if minesweeper[row][column+1] == "#":
                total += 1
        if column > 0 and (row < (row_number-1)):
            if minesweeper[row+1][column-1] == "#":
                total += 1
        if row < (row_number-1):
            if minesweeper[row+1][column] == "#":
                total += 1
        if (column < (column_number-1)) and (row < (row_number-1)):
            if minesweeper[row+1][column+1] == "#":
                total += 1
    return total

# Iterate the function to return a list of output values for all grid locations. 
solution_list = []
for row in range(len(minesweeper)):
    for element in range(len(minesweeper[row])):
        solution_list += str(mine_count(row,element))

# Convert to nested list. 
i=0
solution_nest=[]
while i<len(solution_list):
    solution_nest.append(solution_list[i:i+row_number])
    i+=row_number

# Print nested list line by line to return a grid where a digit indicates the number
# of mines immediately adjacent to a given grid location and a hash (#) indicates the 
# presence of a mine. 
for element in solution_nest: 
    print(element)
