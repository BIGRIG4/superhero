def rev_string(str):
    reversed = ""

    for i in range(len(str)):
        reversed = str[i-1] + reversed

    return reversed

print(rev_string("nick beck warren"))
