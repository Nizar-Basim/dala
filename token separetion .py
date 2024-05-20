def token(a):
    keywords = [
        'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break',
        'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally',
        'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal',
        'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'
    ]
    
    operators = [
        '+', '-', '*', '/', '//', '%', '=', '==', '!=', '<', '<=', '>', '>=', '&&', 
        '||', '^', '&', '|', '~', '<<', '>>', '+=', '-=', '*=', '/=', '%=', '//=', 
        '**=', '&=', '|=', '^=', '>>=', '<<=', 'and', 'or', 'not', 'is', 'is not'
    ]
    
    special_characters = "!@#$^&()}{[]|:;''<>,.?\"'`~\\"
    
    for i in a:
        if i in keywords:
            print("keyword", i)
        elif i.isdigit():
            print("integer", i)
        elif i in operators:
            print("operator", i)
        elif i in special_characters:
            print("special character", i)
        elif i[0].isalpha() or i[0] == "_":
            print("valid identifier:", i)
        else:
            print("unknown token:", i)


with open("example.txt", "r") as file:
    content = file.read()
    tokens = content.split()
    token(tokens)
