def  right():
    turn_left()
    turn_left()
    turn_left()
    
def  jump():
    turn_left()
    move()
    right()
    move()
    right()
    move()
    turn_left()
    
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
        
    
