well=30
current_pos=0
move_up=3
move_down=2
day=1

print("Snail in a well")
print("-"*40)


while True:
    current_pos+=move_up
    print("Day ",day ," , Position : ",current_pos,"m")
    if current_pos >= well:
        break
    current_pos-=move_down
    day+=1
print("\nIt's tood {} days to escape the well".format(day))
