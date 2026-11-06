# Support a +/- b

# Define all token
VALUE, PLUS, MINUS, EOF = 'VALUE', 'PLUS', 'MINUS', 'EOF'

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value
    
    def __str__(self):
        return f"self.type={self.type}, self.value={self.value}"

class Interpreter:
    def __init__(self, form):
        self.form = form
        self.pos = 0
        self.curr_token = Token(EOF, 'EOF')

    def error(self):
        raise Exception('Error parsing input')

    def eat(self, type):
        if self.curr_token.type == type:
            self.curr_token = self.get_next_token()
        else:
            self.error()

    def get_next_token(self):
        while self.pos < len(self.form) and self.form[self.pos].isspace():
            self.pos += 1
        if self.pos >= len(self.form):
            return Token(EOF, None)
        curr_char = self.form[self.pos]
        if curr_char.isdigit():
            self.pos += 1
            return Token(VALUE, int(curr_char))
        elif curr_char == '+':
            self.pos += 1
            return Token(PLUS, '+')
        elif curr_char == '-':
            self.pos += 1
            return Token(MINUS, '-')
        else:
            self.error()

    def expr(self):
        self.curr_token = self.get_next_token()
        left = self.curr_token
        self.eat(VALUE)

        op = self.curr_token
        if op.type == PLUS:
            self.eat(PLUS)
        elif op.type == MINUS:
            self.eat(MINUS)
        else:
            self.error()
        

        right = self.curr_token
        self.eat(VALUE)

        if op.type == PLUS:
            return left.value + right.value
        elif op.type == MINUS:
            return left.value - right.value

def main():
    while 1:
        try:
            form = input('calc>')
        except EOFError:
            break
        if form == None:
            continue
        interpreter = Interpreter(form)
        res = interpreter.expr()
        print(f'result = {res}')


if __name__ == '__main__':
    main()