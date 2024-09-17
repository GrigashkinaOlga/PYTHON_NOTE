def import_info():

    with open ('info.csv', 'r') as f:
       old_data = f.read() 
       new_data = old_data.replace('; ', ' ')
    with open ('info.csv', 'w') as f:
        f.write(new_data)  

    with open('info.csv', 'a') as file:
        file.write('\n')     
    
    pass

def import_info_2():

    with open ('info.csv', 'r') as f:
       old_data = f.read()
       new_data = old_data.replace(' ', '; ')
    with open ('info.csv', 'w') as f:
        f.write(new_data)

    pass
