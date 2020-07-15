def no_dups(s):
    # Your code here
    dupe = {}
    stringer= ""

    for (i, word) in enumerate (s.split()):
        word = word.lower()
        if word not in dupe:
            if i == 0:
                stringer += word
            else:
                stringer += " " + word
        dupe[word] = word
    return stringer


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))