import re
def spliter(text):
    if len(text) > 0:
        try:
            if len(text) > 0:
                pattern_multiply = "((?<=\d)(?=\()|(?<=\))(?=[\d\√\(])|(?<=[\d\)])(?=\√))|(?<=\%)(?=[\(\d])"
                #pattern_spacer = "(?=[\D])(?=[^\.])|(?<=[\+\-\*\\\%\√])|(?<=\()(?=\d)"
                pattern_spacer = "(?=\D)(?=[^\.])|(?<=[^\(\+\\\*\-][\+\*\b\-\\\%])|(?<=[\√\^\*])|(?<=\()(?=\d)"
                text = re.sub(pattern_multiply,"*",text) # adding * between )1, 1(, etc...
                text = re.sub(pattern_spacer," ",text) # adding " " space between all characters if they are not numbers
                text = text.split() # spliting text  to the list of splited characters
                for i in range(len(text)):
                    try:
                        #transforming all possible str(numbers) to float
                        text[i] = float(text[i])
                    except:
                        pass
                return text
        except:
            print("Error: something gone wrong ")


def percent(text,i):
    text[i-1] *= 0.01
    text.remove(text[i])
    return text

def multiply(text,i):
    text[i-1] = text[i-1] * text[i+1]
    text.remove(text[i])
    text.remove(text[i])
    return text

def devide(text,i):
    key = text[i-1] / text[i+1]
    text.remove(text[i+1])
    text[i-1] = key
    text.remove(text[i])
    return text

def plus(text,i):
    key = text[i-1] + text[i+1]
    text.remove(text[i+1])
    text[i-1] = key
    text.remove(text[i])
    return text

def minus(text,i):
    if i != 0:
        key = text[i-1] - text[i+1]
        text.remove(text[i+1])
        text[i-1] = key
        text.remove(text[i])
    elif i == 0 and type(text[i+1]) == float:
        text[i+1] = -(text[i+1])
        text.remove(text[i])
    return text

def square(text):
    result = []
    index = len(text)-1
    while text[index] != "^":
        index -=1
    i = index
    while text[i] == "^":
        key = text[i-1] ** text[i+1]
        text[i-1] = key
        text[i+1] = " "
        text[i] = " "
        i-=2
    text = [i for i in text if i != " "]
    return text


def root(text,i):
    text[i+1] = text[i+1] ** 0.5
    text.remove(text[i])
    return text

def calculator_in(text):
    while ("%" in text):
        for i in range(len(text)):
            if text[i] == "%":
                text = percent(text,i)
                break
    while ("^" in text) or ("√" in text):
        for i in range(len(text)):
            if text[i] == "^":
                text = square(text)
                break
        for i in range(len(text)):
            if text[i] == "√" and type(text[i+1]) == float:
                text = root(text,i)
                break
    while ("*" in text) or ("/" in text):
        for i in range(len(text)):
            if text[i] == "*":
                text = multiply(text,i)
                break
            elif text[i] == "/":
                text  = devide(text,i)
                break
    while ("+" in text) or ("-" in text):
        for i in range(len(text)):
            if text[i] == "+":
                text = plus(text,i)
                break
            elif text[i] == "-":
                text = minus(text,i)
                break
    #print(text)
    return text

def calculator(text):
    try :
        text1 = "".join([str(i) for i in spliter(text)])
        x = 0
        while text1.count("(") != 0:
            for i in range(len(text1)):
                if text1[i] == "(":
                    j = i
                if text1[i] == ")":
                    x = i
                    break
            text1 = text1.replace(text1[j:x+1],str(calculator_in(spliter(text1[j+1:x]))[0]))
        result = calculator_in(spliter(text1))
        print(result[0])
        return str(result[0])
    except:
        print("please input the valid number")
