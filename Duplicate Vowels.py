def strformat(string):
    for letter in string:
        if(letter =='a' or letter=='e' or letter=='i' or letter=='o' or letter=='u' or letter=='A' or letter=='E' or letter=='I' or letter=='O' or letter=='U'):
            return True
        else:
            return False

def duplicateVowels(string):
    s = len(string)
    result = ""
    for i in range(s):
        if(strformat(string[i])):
            result += string[i]
        result += string[i]
    return result

string="apple"
if (type(string)!=str):
    print("Error: Input is not a string. Please enter a string")
else:
    print("\nInput: ", string)
    result = duplicateVowels(string)
    print("Output:", result)        
    strformat(string)