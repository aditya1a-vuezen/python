#  Write a function that is given such a list and checks to see if someone has won. Return True if there is a winner and False otherwise.

list1_input = [[0,2,1],
               [0,0,1],
               [1,2,1]]

def check_winner(list1=list1_input):
    for i in range(3):
        if list1[i][0] == list1[i][1] == list1[i][2] != 0 :
            return True

    for j in range(3):
        if list1[0][j] == list1[1][j] == list1[2][j] != 0:

            return True


    if list1[0][0] == list1[1][1] == list1[2][2] != 0:
        return True
    if list1[0][2] == list1[1][1] == list1[2][1] != 0:
        return True

    return False
print(check_winner(list1_input))
