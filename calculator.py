def calculate() :
    result = 0
    calculation = input()
    match checkForError(calculation):
        case 1:
            raise Exception("ERROR: Incorrect parenthesis.")
        case 2:
            raise Exception("ERROR: No letters in calculation")
    print("Errorless rn")

def checkForError(strVal) :
    stack = []
    allowedStrings = "+-*/.() "
    # 0 - errorless, 1 - parenthesis, 2 - letters
    for letter in strVal:
        match letter:
            case "(":
                stack.append(0)
            case ")":
                if not stack[-1] == 0:
                    return 1
                stack.pop()
        if not letter.isdigit() and letter not in allowedStrings:
            return 2

    if(len(stack) > 0):
        return 1

    return 0

def calculateOperation() :
    answer = 0
    print("Insert num1.")
    num1 = float(input())
    print("Insert operator.")
    operator = input()
    print("Insert num2.")
    num2 = float(input())
    match operator:
        case "+":
            answer = num1 + num2
        case "-":
            answer = num1 - num2
        case "*":
            answer = num1 * num2
        case "/":
            if num2 == 0 :
                return "Please input correct value."
            asnwer = num1 / num2
        case _:
            return "Please enter correct value."
    return str(num1) + " " + operator + " " + str(num2) + " = " + str(answer)

calculate()
