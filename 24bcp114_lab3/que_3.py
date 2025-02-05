def is_substring(string1, string2):
    
    for i in range(len(string1) - len(string2) + 1):  
        if string1[i:i + len(string2)] == string2:  
            return True  
    return False  


def is_substring_case_insensitive(string1, string2):
    
    string1 = string1.lower()  
    string2 = string2.lower()
    return is_substring(string1, string2)  



string1 = input("Enter the first string: ")
string2 = input("Enter the second string to search for: ")


if is_substring(string1, string2):
    print({string2}" is a substring of "{string1} (case-sensitive).")
else:
    print({string2}" is NOT a substring of "{string1} (case-sensitive).")


if is_substring_case_insensitive(string1, string2):
    print({string2} "is a substring of" {string1} (case-insensitive).")
else:
    print({string2}"is NOT a substring of "{string1} (case-insensitive).")


