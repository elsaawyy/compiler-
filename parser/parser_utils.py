class ParserError(Exception):
    def __init__(self, message, line=None, column=None):
        self.message = message
        self.line = line
        self.column = column
        super().__init__(f"Parser Error at line {line}, column {column}: {message}")

class TokenStream:
    def __init__(self, tokens):
        self.tokens = list(tokens)
        self.position = 0
        self.current_token = self.tokens[0] if self.tokens else None
    
    def peek(self):
        """Look at the current token without consuming it"""
        if self.position < len(self.tokens):
            return self.tokens[self.position]
        return ('EOF', '', -1, -1)
    
    def consume(self, expected_type=None):
        """Consume the current token and move to next"""
        if self.position >= len(self.tokens):
            raise ParserError("Unexpected end of input")
        
        current = self.tokens[self.position]
        
        if expected_type and current[0] != expected_type:
            raise ParserError(
                f"Expected {expected_type}, got {current[0]}",
                current[2], current[3]
            )
        
        self.position += 1
        self.current_token = self.tokens[self.position] if self.position < len(self.tokens) else None
        return current
    
    def match(self, token_type):
        """Check if current token matches given type"""
        token = self.peek()
        return token and token[0] == token_type
    
    def has_more(self):
        """Check if there are more tokens"""
        return self.position < len(self.tokens)