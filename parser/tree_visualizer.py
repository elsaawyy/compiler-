from .ast_nodes import *

class TreeVisualizer:
    def __init__(self):
        self.lines = []
    
    def visualize(self, node):
        self.lines = []
        self._add_node(node)
        return "\n".join(self.lines)
    
    def _add_node(self, node, prefix="", is_last=True, is_root=True):
        """Recursively add nodes to the tree representation"""
        if is_root:
            connector = ""
        else:
            connector = "└── " if is_last else "├── "
        
        current_line = prefix + connector
        
        if node is None:
            self.lines.append(current_line + "None")
            return
        
        # Node representation
        if isinstance(node, Program):
            self.lines.append(current_line + "Program")
            new_prefix = prefix + ("    " if is_last else "│   ")
            for i, stmt in enumerate(node.statements):
                self._add_node(stmt, new_prefix, i == len(node.statements) - 1, False)
        
        elif isinstance(node, DeclarationStatement):
            self.lines.append(current_line + "DeclarationStatement")
            new_prefix = prefix + ("    " if is_last else "│   ")
            self._add_node(f"DECLARE", new_prefix, False, False)
            self._add_node(f"IDENTIFIER: {node.identifier}", new_prefix, True, False)
        
        elif isinstance(node, AssignmentStatement):
            self.lines.append(current_line + "AssignmentStatement")
            new_prefix = prefix + ("    " if is_last else "│   ")
            self._add_node(f"IDENTIFIER: {node.identifier}", new_prefix, False, False)
            self._add_node("ASSIGN", new_prefix, False, False)
            self._add_node(node.expression, new_prefix, True, False)
        
        elif isinstance(node, PrintStatement):
            self.lines.append(current_line + "PrintStatement")
            new_prefix = prefix + ("    " if is_last else "│   ")
            self._add_node("PRINT", new_prefix, False, False)
            self._add_node(node.expression, new_prefix, True, False)
        
        elif isinstance(node, IfStatement):
            self.lines.append(current_line + "IfStatement")
            new_prefix = prefix + ("    " if is_last else "│   ")
            self._add_node("IF", new_prefix, False, False)
            self._add_node("LPAREN", new_prefix, False, False)
            self._add_node(node.condition, new_prefix, False, False)
            self._add_node("RPAREN", new_prefix, False, False)
            self._add_node(node.then_branch, new_prefix, node.else_branch is None, False)
            if node.else_branch:
                self._add_node("ELSE", new_prefix, False, False)
                self._add_node(node.else_branch, new_prefix, True, False)
        
        elif isinstance(node, BinOpNode):
            self.lines.append(current_line + f"BinaryOperation({node.op})")
            new_prefix = prefix + ("    " if is_last else "│   ")
            self._add_node(node.left, new_prefix, False, False)
            self._add_node(node.right, new_prefix, True, False)
        
        elif isinstance(node, IdentifierNode):
            self.lines.append(current_line + f"Identifier({node.value})")
        
        elif isinstance(node, NumberNode):
            self.lines.append(current_line + f"Number({node.value})")
        
        elif isinstance(node, StringNode):
            self.lines.append(current_line + f"String({node.value})")
        
        else:
            self.lines.append(current_line + f"Unknown({type(node).__name__})")