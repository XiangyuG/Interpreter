# Support a+b

# Define all token
VALUE, PLUS, EOF = 'VALUE', 'PLUS', 'EOF'

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
        self.curr_token = None
    
    def error(self):
        raise Exception('Error parsing input')

    def get_next_token(self):
        if self.pos >= len(self.form):
            return Token(EOF, None)
        
        curr_char = self.form[self.pos]
        if curr_char.isdigit():
            self.pos += 1
            return Token(VALUE, int(curr_char))
        elif curr_char == '+':
            self.pos += 1
            return Token(PLUS, '+')
        else:
            self.error()

    def eat(self, type):
        if self.curr_token.type == type:
            self.curr_token = self.get_next_token()
        else:
            self.error()

    def expr(self):
        self.curr_token = self.get_next_token()
        left = self.curr_token
        self.eat(VALUE)
        op = self.curr_token
        self.eat(PLUS)
        right = self.curr_token
        self.eat(VALUE)
        
        return left.value + right.value


def main():
    while 1:
        try:
            form = input('calc>')
            print(form)
        except EOFError:
            break
        if not form:
            continue
        interpreter = Interpreter(form)
        res = interpreter.expr()
        print(f"Final output is {res}")

if __name__ == '__main__':
    main()