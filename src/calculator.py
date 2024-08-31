import re

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
        # Evaluar la expresión
        result = eval(expression)
        # Redondear el resultado para evitar problemas de precisión de punto flotante
        result = round(result, 10)
    except ZeroDivisionError:
        raise ZeroDivisionError("División por cero")
    except SyntaxError:
        raise SyntaxError("Error de sintaxis en la expresión")
    except Exception as e:
        raise ValueError(f"Error al evaluar la expresión: {e}")
    
    return result