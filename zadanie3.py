

file_name_1 = '1.txt'
file_name_2 = '2.txt'
file_name_3 = '3.txt'

def catalog_reader(file_name_1, file_name_2, file_name_3):
    list_f = [file_name_1, file_name_2, file_name_3]
    big_dict = {}
    file_dict = {}
    
    for i in list_f:
        with open(i) as file:
            text = file.readlines()
            file_dict ={i:[len(text),text]}
            big_dict.update(file_dict)

    sorted_tuple = sorted(big_dict.items(), key=lambda x: x[1])
    
    with open('1_2_3.txt', "w") as file_end:
        for key, value in dict(sorted_tuple).items():
            file_end.write(f"{key}\n")
            file_end.write(f"{value[0]}\n{''.join(value[1])}\n")
                
    

    
      
catalog_reader(file_name_1, file_name_2, file_name_3)

