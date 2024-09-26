def remove(input_string):
    punctuation = '''!@#$%^&*():"<>?~_+|,.\/[]}{}'''
    result = ""

    for char in input_string:
        if char not in punctuation:
            result += char
    return result

user_input = input("Enter string: ")
updated_str = remove(user_input)
print("Without punctuation:  ", updated_str)
