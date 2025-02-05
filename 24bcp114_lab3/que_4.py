def remove_substring(one_string, remove_string):
   
    index = one_string.find(remove_string)  

    if index != -1:  
        final_string = one_string[:index] + one_string[index + len(remove_string):]
        return final_string
    else:
        return one_string  



one_string = input("Enter the main string: ")
remove_string = input("Enter the string to remove: ")

result_string = remove_substring(one_string, remove_string)
print("Resultant string:", result_string)


