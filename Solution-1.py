def StringManipulation(str):
    ans1=''
    ans2=''
    ans3=''
    for letter in str:
        if letter.isalpha():
            if letter.casefold() == 'z':
                if letter == 'Z':
                    ans1 += 'A'
                elif letter == 'z':
                    ans1 += 'a'
            else:
                ans1 += chr(ord(letter)+1)
        else:
            ans1 += letter

    print('Output 1:')
    print(ans1)

    for letter in ans1:
        if letter.casefold() == 'a' or letter.casefold() == 'e' or letter.casefold() == 'i' or letter.casefold() == 'o' or letter.casefold() == 'u':
            continue
        else:
            ans2 += letter
    ans2 = ans2[::-1]
    
    print('Output 2:')
    print(ans2)

    for i in range(0, len(str), 2):
        ans3 += str[i]

    print('Output 3:')
    print(ans3)

str = input('Enter String: ')
StringManipulation(str)