#  Write a function that is given such a list and randomly chooses a spot in which to place a 2. The spot chosen must currently be a 0 and a spot must be chosen.
import random
list_input = [[0,2,1],[0,0,1],[1,2,1]]

def place_two(list1):

    zero_locations = []
    for i in range (3):
        for j in range(3):
            if list1[i][j] == 0:
                zero_locations.append((i,j))

    print(zero_locations)
    selected_location = random.choice(zero_locations)
    print(selected_location)

    list1[selected_location[0]][selected_location[1]]=2
    return list1

list_output = place_two(list_input)

print(list_output)
