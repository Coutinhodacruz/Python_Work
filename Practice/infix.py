class InfixEvaluator:
    @staticmethod
    def is_operator(c):
        return c == '+' or c == '-' or c == '*' or c == '/'

    @staticmethod
    def precedence(operator):
        if operator == '+' or operator == '-':
            return 1
        elif operator == '*' or operator == '/':
            return 2
        else:
            return 0

    @staticmethod
    def apply_operator(operator, operand1, operand2):
        if operator == '+':
            return operand1 + operand2
        elif operator == '-':
            return operand1 - operand2
        elif operator == '*':
            return operand1 * operand2
        elif operator == '/':
            if operand2 == 0:
                raise ZeroDivisionError('Division by zero')
            return operand1 // operand2
        else:
            raise ValueError('Invalid operator')

    @staticmethod
    def evaluate(expression):
        operands = []
        operators = []

        i = 0
        while i < len(expression):
            c = expression[i]

            if c.isdigit():
                operand = 0
                while i < len(expression) and expression[i].isdigit():
                    operand = operand * 10 + int(expression[i])
                    i += 1
                operands.append(operand)
                i -= 1
            elif InfixEvaluator.is_operator(c):
                while operators and InfixEvaluator.precedence(operators[-1]) >= InfixEvaluator.precedence(c):
                    operand2 = operands.pop()
                    operand1 = operands.pop()
                    operator = operators.pop()
                    result = InfixEvaluator.apply_operator(operator, operand1, operand2)
                    operands.append(result)
                operators.append(c)
            elif c == '(':
                operators.append(c)
            elif c == ')':
                while operators[-1] != '(':
                    operand2 = operands.pop()
                    operand1 = operands.pop()
                    operator = operators.pop()
                    result = InfixEvaluator.apply_operator(operator, operand1, operand2)
                    operands.append(result)
                operators.pop()

            i += 1

        while operators:
            operand2 = operands.pop()
            operand1 = operands.pop()
            operator = operators.pop()
            result = InfixEvaluator.apply_operator(operator, operand1, operand2)
            operands.append(result)

        if len(operands) != 1 or operators:
            raise ValueError('Invalid expression')

        return operands[0]


expression = "2 + 3 * 4 - 5"
result = InfixEvaluator.evaluate(expression)
print(f"{expression} = {result}")
