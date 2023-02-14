row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]

map = [row1, row2, row3]
print(f"{row1}\n{row2},\n{row3}")
position = input("Where do you want to put the treasure?\n:")

j = int(position[0])
i = int(position[1])

map[i-1][j-1] = "X"

print(f"{row1}\n{row2},\n{row3}")
