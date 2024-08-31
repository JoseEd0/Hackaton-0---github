import re
import operator

# Definir las funciones
def suma(a, b):
    return a + b

def division(a, b):
    return a / b

def multiplicar(a, b):
    return a * b

def resta(a, b):
    return a - b

# Diccionario de operadores
OPERATORS = {
    '+': suma,
    '-': resta,
    '*': multiplicar,
    '/': division
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
        # Reemplazar operadores con las funciones definidas
        for op, func in OPERATORS.items():
            expression = expression.replace(op, f' {func.__name__} ')
        
        # Evaluar la expresión en un entorno seguro
        result = eval(expression, {"__builtins__": None}, OPERATORS)
    except ZeroDivisionError:
        raise ZeroDivisionError("División por cero")
    except SyntaxError:
        raise SyntaxError("Error de sintaxis en la expresión")
    except Exception as e:
        raise ValueError(f"Error al evaluar la expresión: {e}")
    
    return result