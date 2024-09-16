def calculate() :
    result = 0
    calculation = input()
    #calculation = "(10 + 5) / 2";
    match checkForError(calculation):
        case 1:
            raise Exception("ERROR: Incorrect parenthesis.")
        case 2:
            raise Exception("ERROR: No letters in calculation")
    calculation = removeWhiteSpaces(calculation)
    print(calculation)
    print("Errorless rn")
    print(recursive(calculation), ": result")

def checkForError(strVal) :
    stack = []
    allowedStrings = "+-*/.() "
    # 0 - errorless, 1 - parenthesis, 2 - letters
    for letter in strVal:
        match letter:
            case "(":
                stack.append(0)
            case ")":
                if not stack[len(stack) - 1] == 0:
                    return 1
                stack.pop()
        if not letter.isdigit() and letter not in allowedStrings:
            return 2

    if(len(stack) > 0):
        return 1

    return 0

def removeWhiteSpaces(string) :
    return string.replace(" ", "")

def addParenthesis(string):
    operators = "+-*/"
    for i in range(len(string)):
        if string[i] in operators:
            subindex = i - 1
            while subindex > 0:
                if string[subindex] in operators:

                elif string[subindex] == "(":
                    break
                subindex-=1

    return string

def recursive(strval) :
    substr = ""
    while len(strval) > 0:
        if strval[0] == "(":
            #val = str(recursive(strval[1:]))
            strval = str(recursive(strval[1:]))
        elif strval[0] == ")":
            strval = strval[1:]
            break
        else:
            substr += strval[0]
            strval = strval[1:]
    #for i in range(len(strval)):
    #    if strval[i] == "(":
    #        strval = strval[:i] + str(recursive(strval[i+1:])) + strval[i + 1:]
    #    if strval[i] == ")":
    #        strval = strval[:i] + strval[i+1:]
    #        break
    #    substr += strval[i]
    #    if i == 0:
    #        strval = strval[1:]
    #        continue
    strval = strval[:len(strval)]
    n1, op, n2 = extractFromStr(substr)
    print(strval, "is strval")
    return str(calculateOperation(n1 ,op, n2)) + strval;

def extractFromStr(string):
    n1, op, n2 = "", "", ""
    n1Done = False;
    operatorSelection = "+-*/"
    for letter in string:

        if not n1Done:
            if letter.isdigit() or letter == ".":
                n1 += letter
            elif letter in operatorSelection:
                op = letter
                n1Done = True
            continue

        n2 += letter

    print(n1, op, n2)

    n1 = float(n1)
    n2 = float(n2)

    return n1, op, n2

def calculateOperation(a, op, b) :
    answer = 0
    match op:
        case "+":
            answer = a + b
        case "-":
            answer = a - b
        case "*":
            answer = a * b
        case "/":
            if b == 0 :
                raise Exception("ERROR: cannot divide by 0")
            answer = a / b
    print(a, b, op, answer, "CMON")
    print("-----")
    return answer

calculate()
