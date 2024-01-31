class Solution:
    # # def is_int(self,str):
    # #     try:
    # #         int(str)
    # #         return True
    # #     except ValueError:
    # #         # The string does not represent a valid integer
    # #         return False

    # def evalRPN(self, tokens: List[str]) -> int:

    #     # def add(a,b):
    #     #     return a + b

    #     # def subtract(a,b):
    #     #     return a - b

    #     # def multiply(a,b):
    #     #     return a * b

    #     # def divide(a,b):
    #     #     return a / b

    #     # operations = {
    #     #     '+' : add,
    #     #     '-' : subtract,
    #     #     '*' : multiply,
    #     #     '/' : divide
    #     # }

    #     stack = []
    #     valid_operators = ['+', '-', '*','/']

    #     for token in tokens:
    #         # if self.is_int(token):
    #         if token not in valid_operators:
    #             stack.append(int(token)) # Convert to int immediately
    #         else:
    #             b, a = stack.pop(), stack.pop()
    #             # operation = operations[token]
    #             # stack.append(int(operation(a,b)))
    #             if token == '+':
    #                 stack.append(a + b)
    #             elif token == '-':
    #                 stack.append(a - b)
    #             elif token == '*':
    #                 stack.append(a * b)
    #             elif token == '/':
    #                 # Use int() for floor division result
    #                 stack.append(int(a / b))
    #     return stack.pop()

    # def evalRPN(self, tokens: List[str]) -> int:
    #     stack = []

    #     for token in tokens:
    #         if token in ['+', '-', '*', '/']:
    #             b, a = stack.pop(), stack.pop()
    #             if token == '+':
    #                 stack.append(a + b)
    #             elif token == '-':
    #                 stack.append(a - b)
    #             elif token == '*':
    #                 stack.append(a * b)
    #             elif token == '/':
    #                 # Use int() for floor division result
    #                 stack.append(int(a / b))
    #         else:
    #             stack.append(int(token))    
    #     return stack[-1]
    
    from operator import add, sub, mul,truediv

    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        operations = {
            '+' : add,
            '-' : sub,
            '*' : mul,
            '/' : lambda x,y : int(x/y)
        }
        # lambda x,y : int(x/y) instead of truediv

        for token in tokens:
            if token in operations:
                b,a = stack.pop(), stack.pop()
                stack.append(operations[token](a,b))
            else:
                stack.append(int(token))    
        
        return stack[0]
