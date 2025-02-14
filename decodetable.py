# We start by fetching the table from the url using pandas, which gives us a pandas DataFrame.

# Then we create a 2D array to map the characters into. We take the largest number from the x-coordinate
# column of the table as width of our array, and the largest number from the y-coordinate column as
# the height of the array.  We set the default value of every element of this array to be a single
# space character.

# Next we iterate over the table.  The x-coordinate value represents the arrays column index, the
# y-coordinate value represent the arrays row index, and the Character is inserted as the array
# column/row element.  We take care to cast the coordinate values from String to Integer.

# Before printing the message, we must reverse the order of the rows.  The original table defines
# the bottom to be y=0, but it is more convenient for us to print from top to bottom.

# Finally we iterate over our 2D array.  We start at the top row and print each character one
# column at a time, making sure that Python does not automatically include a newline after every
# character.  Once we have completed all the columns on a line, we insert a newline, and move on
# to the next row.

import pandas as pd

# Get the table from the url
url = r'http://thetable.html'
tables = pd.read_html(url)
table = tables[0]
table = table.drop([0])

# Create a 2d array full of spaces
num_cols = int(table[0].max()) + 1
num_rows = int(table[2].max()) + 1
array = [[" " for _ in range(num_cols)] for _ in range(num_rows)]

# Map the table entries into the array
for i in range(1, len(table)):
    array [int(table[2][i])] [int(table[0][i])] = table[1][i]

# The table defines bottom left as (0,0). To make printing convenient
# we want to start at the top left, so we reverse the order of the rows
array.reverse()

# print the array one row at a time
for y in range(0, num_rows):
    for x in range(0, num_cols):
        print(array[y][x], end="")
    print('\n')
