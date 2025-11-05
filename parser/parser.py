from .parser_utils import TokenStream, ParserError
from .ast_nodes import *

class Parser:
    def __init__(self, tokens):
        self.tokens = TokenStream(tokens)
    
    def parse(self):
        """Main parse method - starts parsing from Program"""
        statements = self.parse_statement_list()
        return Program(statements)
    
    def parse_statement_list(self):
        """StatementList → Statement StatementList | ε"""
        statements = []
        
        while self.tokens.has_more() and not self.tokens.match('EOF'):
            statement = self.parse_statement()
            if statement:
                statements.append(statement)
        
        return statements
    
    def parse_statement(self):
        """Statement → Declaration | Assignment | Print | Input | If | Return"""
        token_type = self.tokens.peek()[0] if self.tokens.peek() else None
        
        if token_type == 'DECLARE':
            return self.parse_declaration_statement()
        elif token_type == 'PRINT':
            return self.parse_print_statement()
        elif token_type == 'INPUT':
            return self.parse_input_statement()
        elif token_type == 'IF':
            return self.parse_if_statement()
        elif token_type == 'RETURN':
            return self.parse_return_statement()
        elif token_type == 'IDENTIFIER':
            return self.parse_assignment_statement()
        else:
            raise ParserError(
                f"Unexpected token {token_type} at start of statement",
                self.tokens.peek()[2], self.tokens.peek()[3]
            )
    
    def parse_declaration_statement(self):
        """DeclarationStatement → DECLARE IDENTIFIER"""
        self.tokens.consume('DECLARE')
        identifier_token = self.tokens.consume('IDENTIFIER')
        return DeclarationStatement(identifier_token[1])
    
    def parse_assignment_statement(self):
        """AssignmentStatement → IDENTIFIER ASSIGN Expression"""
        identifier_token = self.tokens.consume('IDENTIFIER')
        self.tokens.consume('ASSIGN')
        expression = self.parse_expression()
        return AssignmentStatement(identifier_token[1], expression)
    
    def parse_print_statement(self):
        """PrintStatement → PRINT Expression"""
        self.tokens.consume('PRINT')
        expression = self.parse_expression()
        return PrintStatement(expression)
    
    def parse_input_statement(self):
        """InputStatement → INPUT IDENTIFIER"""
        self.tokens.consume('INPUT')
        identifier_token = self.tokens.consume('IDENTIFIER')
        return InputStatement(identifier_token[1])
    
    def parse_if_statement(self):
        """IfStatement → IF LPAREN Condition RPAREN Statement (ELSE Statement)?"""
        self.tokens.consume('IF')
        self.tokens.consume('LPAREN')
        condition = self.parse_condition()
        self.tokens.consume('RPAREN')
        
        then_branch = self.parse_statement()
        else_branch = None
        
        if self.tokens.match('ELSE'):
            self.tokens.consume('ELSE')
            else_branch = self.parse_statement()
        
        return IfStatement(condition, then_branch, else_branch)
    
    def parse_return_statement(self):
        """ReturnStatement → RETURN Expression"""
        self.tokens.consume('RETURN')
        expression = self.parse_expression()
        return ReturnStatement(expression)
    
    def parse_condition(self):
        """Condition → Expression RelOp Expression"""
        left = self.parse_expression()
        rel_op = self.tokens.consume()[0]  # EQ, NE, GT, LT, GTE, LTE
        right = self.parse_expression()
        return BinOpNode(left, rel_op, right)
    
    def parse_expression(self):
        """Expression → Term Expression'"""
        left = self.parse_term()
        return self.parse_expression_prime(left)
    
    def parse_expression_prime(self, left):
        """Expression' → (PLUS | MINUS) Term Expression' | ε"""
        if self.tokens.match('PLUS') or self.tokens.match('MINUS'):
            op_token = self.tokens.consume()
            right = self.parse_term()
            new_left = BinOpNode(left, op_token[0], right)
            return self.parse_expression_prime(new_left)
        return left
    
    def parse_term(self):
        """Term → Factor Term'"""
        left = self.parse_factor()
        return self.parse_term_prime(left)
    
    def parse_term_prime(self, left):
        """Term' → (MULT | DIV) Factor Term' | ε"""
        if self.tokens.match('MULT') or self.tokens.match('DIV'):
            op_token = self.tokens.consume()
            right = self.parse_factor()
            new_left = BinOpNode(left, op_token[0], right)
            return self.parse_term_prime(new_left)
        return left
    
    def parse_factor(self):
        """Factor → IDENTIFIER | NUMBER | STRING | LPAREN Expression RPAREN"""
        token_type = self.tokens.peek()[0]
        
        if token_type == 'IDENTIFIER':
            token = self.tokens.consume('IDENTIFIER')
            return IdentifierNode(token[1])
        elif token_type == 'NUMBER':
            token = self.tokens.consume('NUMBER')
            return NumberNode(token[1])
        elif token_type == 'STRING':
            token = self.tokens.consume('STRING')
            return StringNode(token[1])
        elif token_type == 'LPAREN':
            self.tokens.consume('LPAREN')
            expression = self.parse_expression()
            self.tokens.consume('RPAREN')
            return expression
        else:
            raise ParserError(
                f"Expected identifier, number, string, or '(', got {token_type}",
                self.tokens.peek()[2], self.tokens.peek()[3]
            )