VALUE, PLUS, MINUS, MULTI, DIV, EOF = 'VALUE', 'PLUS', 'MINUS', 'MULTI', 'DIV', 'EOF'

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value
    def __str__(self):
        return f"self.type={self.type}, self.value={self.value}"

class Lexer:
    def __init__(self, form):
        self.form = form
        self.pos = 0
        self.curr_char = self.form[self.pos]
        self.curr_token = None
    
    def error(self):
        raise Exception('Parsing invalid character!')

    def skip_space(self):
        while self.curr_char is not None and self.curr_char.isspace():
            self.advance()
    
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
            if self.curr_char == '*':
                self.advance()
                return Token(MULTI, '*')
            if self.curr_char == '/':
                self.advance()
                return Token(DIV, '/')
            self.error()
        return Token(EOF, None)

    def integer(self):
        curr_int = ""
        while self.curr_char is not None and self.curr_char.isdigit():
            curr_int += self.curr_char
            self.advance()
        return int(curr_int)
    
    def advance(self):
        self.pos += 1
        if self.pos < len(self.form):
            self.curr_char = self.form[self.pos]
        else:
            self.curr_char = None

class Interpreter:
    def __init__(self, lexer):
        self.lexer = lexer
        self.curr_token = self.lexer.get_next_token()
    
    def error(self):
        raise Exception('Interpreter error!')

    def eat(self, type):
        if self.curr_token.type == type:
            self.curr_token = self.lexer.get_next_token()
        else:
            self.error()
    
    def term(self):
        result = self.factor()
        while self.curr_token.type in (MULTI, DIV):
            if self.curr_token.type == MULTI:
                self.eat(MULTI)
                next_token = self.curr_token
                self.eat(VALUE)
                result *= next_token.value
            elif self.curr_token.type == DIV:
                self.eat(DIV)
                next_token = self.curr_token
                self.eat(VALUE)
                result /= next_token.value
            else:
                self.error()
        return result
    
    def factor(self):
        token = self.curr_token
        self.eat(VALUE)
        return token.value
    
    def expr(self):
        result = self.term()
        while self.curr_token.type in (PLUS, MINUS):
            if self.curr_token.type == PLUS:
                self.eat(PLUS)
                result += self.term()
            elif self.curr_token.type == MINUS:
                self.eat(MINUS)
                result -= self.term()
            else:
                self.error()
        return result

def main():
    while 1:
        try:
            form = input('calc>')
        except EOFError:
            break
        if form == None:
            continue
        lexer = Lexer(form)
        interpreter = Interpreter(lexer)
        res = interpreter.expr()
        print(f'Final result is {res}')

if __name__ == '__main__':
    main()