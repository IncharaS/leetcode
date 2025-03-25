class Solution(object):
    def evalRPN(self, tokens):
        \\\
        :type tokens: List[str]
        :rtype: int
        \\\
        operators = set(['+', '-', '/', '*'])

        number_stack = []
        operator_stack = []
        for i in tokens:
            if i in operators:
                operator_stack.append(i)
            else:
                number_stack.append(i)
            while len(number_stack) > 1 and len(operator_stack) > 0:
                    number1 = int(number_stack.pop())
                    number2 = int(number_stack.pop())
                    op = operator_stack.pop()
                    if op == '+':
                        result = number2 + number1
                    elif op == '-':
                        result = number2 - number1
                    elif op == '*':
                        result = number2 * number1
                    elif op == '/':
                        result = int(float(number2) / number1)
                        print(number1, number2,result, '1 and 2')

                    number_stack.append(result)
                    # print(number_stack)
                    # print(operator_stack)
        return int(number_stack[0])