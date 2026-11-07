VALUE, PLUS, MINUS, EOF = 'VALUE', 'PLUS', 'MINUS', 'EOF'

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value
    def __str__(self):
        return f'self.type = {self.type}, self.value = {self.value}'

class Interpreter:
    def __init__(self, form):
        self.form = form
        self.pos = 0
        self.curr_char = form[self.pos]
        self.curr_token = None
    
    def error(self):
        raise Exception('Input parsing error')

    def eat(self, type):
        if self.curr_token.type == type:
            self.curr_token = self.get_next_token()
        else:
            self.error()

    def advance(self):
        self.pos += 1
        if self.pos < len(self.form):
            self.curr_char = self.form[self.pos]
        else:
            self.curr_char = None

    def skip_space(self):
        while self.curr_char is not None and self.curr_char.isspace():
            self.advance()

    def integer(self):
        curr_int = ""
        while self.curr_char is not None and self.curr_char.isdigit():
            curr_int += self.curr_char
            self.advance()
        return int(curr_int)

    def get_next_token(self):
        while self.curr_char is not None:
            if self.curr_char.isspace():
                self.skip_space()
                continue
            if self.curr_char.isdigit():
                return Token(VALUE, self.integer())
            if self.curr_char == '+':
                self.advance()
                return Token(PLUS, '+')
            if self.curr_char == '-':
                self.advance()
                return Token(MINUS, '-')
        return Token(EOF, None)

    def expr(self):
        self.curr_token = self.get_next_token()
        # print(f'self.curr_token={self.curr_token}')
        beg_token = self.curr_token
        self.eat(VALUE)
        result = beg_token.value
        
        
        while self.curr_token is not None and self.curr_token.type in (PLUS, MINUS):
            # print(f'Inside self.curr_token={self.curr_token}')
            if self.curr_token.type == PLUS:
                self.eat(PLUS)
                next_token = self.curr_token
                self.eat(VALUE)
                result += next_token.value
            elif self.curr_token.type == MINUS:
                self.eat(MINUS)
                next_token = self.curr_token
                self.eat(VALUE)
                result -= next_token.value
            else:
                self.error()
        return result


def main():
    while 1:
        try:
            form = input('calc>')
        except EOFError:
            break
        if form is None:
            continue
        interpreter = Interpreter(form)
        res = interpreter.expr()
        print(f'final result is {res}')

if __name__ == '__main__':
    main()