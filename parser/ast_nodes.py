class ASTNode:
    """Base class for all AST nodes"""
    pass

class Program(ASTNode):
    def __init__(self, statements):
        self.statements = statements
    
    def __repr__(self):
        return f"Program({self.statements})"

class DeclarationStatement(ASTNode):
    def __init__(self, identifier):
        self.identifier = identifier
    
    def __repr__(self):
        return f"Declare({self.identifier})"

class AssignmentStatement(ASTNode):
    def __init__(self, identifier, expression):
        self.identifier = identifier
        self.expression = expression
    
    def __repr__(self):
        return f"Assign({self.identifier}, {self.expression})"

class PrintStatement(ASTNode):
    def __init__(self, expression):
        self.expression = expression
    
    def __repr__(self):
        return f"Print({self.expression})"

class InputStatement(ASTNode):
    def __init__(self, identifier):
        self.identifier = identifier
    
    def __repr__(self):
        return f"Input({self.identifier})"

class IfStatement(ASTNode):
    def __init__(self, condition, then_branch, else_branch=None):
        self.condition = condition
        self.then_branch = then_branch
        self.else_branch = else_branch
    
    def __repr__(self):
        return f"If({self.condition}, {self.then_branch}, {self.else_branch})"

class ReturnStatement(ASTNode):
    def __init__(self, expression):
        self.expression = expression
    
    def __repr__(self):
        return f"Return({self.expression})"

class BinOpNode(ASTNode):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right
    
    def __repr__(self):
        return f"BinOp({self.left}, {self.op}, {self.right})"

class IdentifierNode(ASTNode):
    def __init__(self, value):
        self.value = value
    
    def __repr__(self):
        return f"Identifier({self.value})"

class NumberNode(ASTNode):
    def __init__(self, value):
        self.value = value
    
    def __repr__(self):
        return f"Number({self.value})"

class StringNode(ASTNode):
    def __init__(self, value):
        self.value = value
    
    def __repr__(self):
        return f"String({self.value})"