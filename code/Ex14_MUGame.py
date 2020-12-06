# Ex14: The MU Game

s = input('Enter your letters (M, U and I only): ')
rule = input('Enter a number for the rule between 1-4 (q = quit):')
s = s.upper()

while rule.lower() != 'q':
    # Rule 1 
    # If the current string's last character is I, then add U onto the end of the current string.
    if rule == '1':
        if s[-1] == 'I':
            s = s+'U'

    # Rule 2
    # If the first character of the current string is M, 
    # then the rest of the string should be repeated. 
    # E.g. If the string is MIUIUIM the output of rule 2 will be MIUIUIMIUIUIM since the first character is M, we repeat the IUIUIM part.
    elif rule == '2':
        if s[0] == 'M':
            s = s + s[1:]

    # Rule 3
    # If III is a substring of the current string, 
    # then replace the first occurrence of this substring with a U. 
    # E.g. If the string is MUIIIUIIIUIUIII it will become MUUUIIIUIUIII.
    elif rule == '3':
        index = s.find('III')
        if index == -1:
            print('Index found at -1')
            print('Index not found')
        else:
            s = s[:index] + 'U' + s[index+3:]

    # Rule 4
    # If UU is a substring of the current string, 
    # then delete the first occurrence of this substring.
    # E.g. If the string is MIIUMUIUUIMUU it will become MIIUMUIIMUU
    elif rule == '4':
        index = s.find('UU')
        if index == -1:
            print('Index found at -1')
            print('Index not found')
        else:
            s = s[:index] + '' + s[index+2:]

    print(s)
    rule = input('Enter a number for the rule between 1-4 (q = quit):')
