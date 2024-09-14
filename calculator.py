def calculate() :
    result = 0
    # calculation = input()
    calculation = "(((10    +              3) -           9) /    2)    -         (0.5)";
    match checkForError(calculation):
        case 1:
            raise Exception("ERROR: Incorrect parenthesis.")
        case 2:
            raise Exception("ERROR: No letters in calculation")
    calculation = removeWhiteSpaces(calculation)
    print(calculation)
    print("Errorless rn")
    print(recursive(calculation))

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

def recursive(strval) :
    substr = ""
    for i in range(len(strval)):
        if strval[i] == "(":
            recursive(strVal[i+1:])
        if strval[i] == ")":
            break
        substr += strval[i]

    n1, op, n2 = extractFromStr(substr)
    return calculateOperation(n1 ,op, n2);

def extractFromStr(string):
    n1, op, n2;
    n1Done = False;
    operatorSelection = "+-*/"
    for letter in string:

        if not n1Done:
            if letter.isdigit() or letter == ".":
                n1 += letter
            elif operatorSelection.includes(letter):
                op = letter
                n1Done = True
            continue

        n2 += letter

    n1 = float(n1)
    n2 = float(n2)

    return n1, op, n3

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
            asnwer = a / b
    return answer

calculate()
