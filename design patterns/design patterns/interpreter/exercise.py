class ExpressionProcessor:
    def __init__(self):
        self.variables = {}

    def calculate(self, expression):
        # todo
        res = 0
        s = '+'
        val = 0
        for i in range(len(expression)):
            if isdigit(i) or isdigit(self.variables.get(i)):
                if not isdigit(i):
                    val = int(self.variables.get(i))
                else:
                    val = int(i)
                if s == '+':
                    res+=int(val)
                else:
                    res-=int(val)
            elif i == '+' or i == '-':
                s = i
            else:
                if not self.variables.get(i):
                    return 0
                
            