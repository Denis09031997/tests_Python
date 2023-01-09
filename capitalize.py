def capitalize(text):
    if text == '':
        return ''
    elif text == 2:
        return 2 ** 2
    first_char = text[0].upper()
    rest_substring = text[1:]
    return f'{first_char}{rest_substring}'
