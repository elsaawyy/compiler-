from .ast_nodes import *

class TreeVisualizer:
    def __init__(self):
        self.lines = []
    
    def visualize(self, node):
        self.lines = []
        self._add_node(node)
        return "\n".join(self.lines)
    
    def _add_node(self, node, prefix="", is_last=True):
        if node is None:
            return
        
        connector = "└── " if is_last else "├── "
        current_line = prefix + connector
        
        if isinstance(node, Program):
            self.lines.append(current_line + "Program")
            new_prefix = prefix + ("    " if is_last else "│   ")
            for i, stmt in enumerate(node.statements):
                self._add_node(stmt, new_prefix, i == len(node.statements) - 1)
        
        elif isinstance(node, DeclarationStatement):
            self.lines.append(current_line + "Declaration")
            new_prefix = prefix + ("    " if is_last else "│   ")
            self._add_node(node.identifier, new_prefix, True)
        
        elif isinstance(node, AssignmentStatement):
            self.lines.append(current_line + "Assignment")
            new_prefix = prefix + ("    " if is_last else "│   ")
            self._add_node(node.identifier, new_prefix, False)
            self._add_node(node.expression, new_prefix, True)
        
        elif isinstance(node, PrintStatement):
            self.lines.append(current_line + "Print")
            self._add_node(node.expression, prefix + "    ", True)
        
        elif isinstance(node, InputStatement):
            self.lines.append(current_line + "Input")
            self._add_node(node.identifier, prefix + "    ", True)
        
        elif isinstance(node, IfStatement):
            self.lines.append(current_line + "IfStatement")
            new_prefix = prefix + ("    " if is_last else "│   ")
            self._add_node(node.condition, new_prefix, False)
            self._add_node(node.then_branch, new_prefix, node.else_branch is None)
            if node.else_branch:
                self._add_node(node.else_branch, new_prefix, True)
        
        elif isinstance(node, ReturnStatement):
            self.lines.append(current_line + "Return")
            self._add_node(node.expression, prefix + "    ", True)
        
        elif isinstance(node, BinOpNode):
            self.lines.append(current_line + f"BinaryOp({node.op})")
            new_prefix = prefix + ("    " if is_last else "│   ")
            self._add_node(node.left, new_prefix, False)
            self._add_node(node.right, new_prefix, True)
        
        elif isinstance(node, IdentifierNode):
            self.lines.append(current_line + f"Identifier({node.value})")
        
        elif isinstance(node, NumberNode):
            self.lines.append(current_line + f"Number({node.value})")
        
        elif isinstance(node, StringNode):
            self.lines.append(current_line + f"String({node.value})")
        
        else:
            self.lines.append(current_line + f"Unknown({type(node).__name__}: {node})")