class BinaryTree:
    def __init__(self, value):
        self.value = value  
        self.left = None
        self.right = None

    def combine(self, operator, left_tree, right_tree):
        
        self.value = operator
        self.left = left_tree
        self.right = right_tree

    def pre_order(self):
        
        result = [self.value]
        if self.left:
            result.extend(self.left.pre_order())
        if self.right:
            result.extend(self.right.pre_order())
        return result

    def in_order(self):
        
        result = []
        if self.left:
            result.append("(")
            result.extend(self.left.in_order())
        result.append(self.value)
        if self.right:
            result.extend(self.right.in_order())
            result.append(")")
        return result

    def post_order(self):
        
        result = []
        if self.left:
            result.extend(self.left.post_order())
        if self.right:
            result.extend(self.right.post_order())
        result.append(self.value)
        return result


def build_expression_tree(postfix_expression):
    
    stack = []
    operators = {"+", "-", "*", "/"}  # Operadores válidos

    for token in postfix_expression.split():
        if token.isdigit() or token.isalpha():  
            stack.append(BinaryTree(token))
        elif token in operators:  
            if len(stack) < 2:
                raise ValueError("Expresión postfija inválida: falta operando.")
            right = stack.pop()
            left = stack.pop()
            new_tree = BinaryTree(None)
            new_tree.combine(token, left, right)
            stack.append(new_tree)
        else:
            raise ValueError(f"Token no válido: {token}")

    if len(stack) != 1:
        raise ValueError("Expresión postfija inválida: sobran operandos u operadores.")

    return stack.pop()


def evaluate_expressions(expressions):
   
    for idx, expr in enumerate(expressions):
        print(f"\nExpresión {idx + 1}: {expr}")
        try:
            tree = build_expression_tree(expr)
            print("Preorden: ", " ".join(tree.pre_order()))
            print("Inorden: ", "".join(tree.in_order()))
            print("Postorden:", " ".join(tree.post_order()))
        except ValueError as e:
            print(f"Error: {e}")



expressions = [
    "91 95 + 15 + 19 + 4 *",
    "B B * A C 4 * * -",
    "A 57",  
    "+ /"    
]

evaluate_expressions(expressions)
