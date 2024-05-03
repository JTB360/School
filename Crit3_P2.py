while True: 
    try: 
        current_time = int(input("Please enter the current local time: ")) 
        alarm_time = int(input("Enter hours until alarm goes off: "))
        break 
# ValueError is used if user enters a non number
    except ValueError: 
        print("Invalid input.") 
new_time = (current_time + alarm_time) % 24

if len(str(new_time)) < 2:
    print ('The alarm will go off at ' + '0' + str(new_time)+ ':00')
elif len(str(new_time)) == 2:
    print ('The alarm will go off at ' + str(new_time)+ ':00')
