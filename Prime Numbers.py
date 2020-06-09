def prime(num):
    for i in range(2, num):
        if num % i == 0:
            print("Not prime")
            break
    else:
        print("Prime")


    for i in range(2, num):
        for n in range(2, i):
            if(i%n) == 0:
                break
        else:
            print(i, end=" ")

inputvar = 9
inputvarstring = str(inputvar)
if(type(inputvar)!=int):
    print("Error: Input is not an integer. Please input an integer")
else:
    print("Input: " + inputvarstring + "\n" + "Output: ")
    prime(inputvar)