import re
import ast
import operator

# Definir las funciones
def suma(a, b):
    return a + b

def division(a, b):
    if b == 0:
        raise ZeroDivisionError("División por cero")
    return a / b

def multiplicar(a, b):
    return a * b

def resta(a, b):
    return a - b

# Diccionario de operadores
OPERATORS = {
    ast.Add: suma,
    ast.Sub: resta,
    ast.Mult: multiplicar,
    ast.Div: division
}

def calculate(expression):
    # Eliminar espacios en blanco
    expression = expression.replace(" ", "")
    
    # Validar que la expresión no esté vacía
    if not expression:
        raise ValueError("La expresión no puede estar vacía")
    
    # Validar que la expresión solo contenga números, operadores y paréntesis
    if not re.match(r'^[\d\.\+\-\*/\(\)]+$', expression):
        raise ValueError("La expresión contiene caracteres inválidos")
    
    try:
        # Parsear la expresión
        node = ast.parse(expression, mode='eval')
        return _eval(node.body)
    except ZeroDivisionError:
        raise ZeroDivisionError("División por cero")
    except SyntaxError:
        raise SyntaxError("Error de sintaxis en la expresión")
    except Exception as e:
        raise ValueError(f"Error al evaluar la expresión: {e}")

def _eval(node):
    if isinstance(node, ast.BinOp):
        left = _eval(node.left)
        right = _eval(node.right)
        return OPERATORS[type(node.op)](left, right)
    elif isinstance(node, ast.Num):
        return node.n
    elif isinstance(node, ast.Expression):
        return _eval(node.body)
    else:
        raise TypeError(node)