class Token:
    def __init__(self, value=0):
        self.value = value


class Memento(list):
    
    def __init__(self, token):
        self.append(token)


class TokenMachine:
    def __init__(self):
        self.tokens = []
        self.count = 0

    def add_token_value(self, value):
        self.add_token(Token(value))
        m = Memento(Token(value))
        self.count+=1
        return m
        

    def add_token(self, token):
        # todo
        self.tokens.append(token)

    def revert(self, memento):
        # todo
        if self.count>0:
            self.count-=1
            m = memento[self.count]
            self.add_token(m)
        return None