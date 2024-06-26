def calculate(expression):
    stack = []
    operators = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y}

    operands = expression.split()
    for operand in operands:
        if operand in operators:
            operand2 = stack.pop()
            operand1 = stack.pop()
            operation = operators[operand]
            result = operation(operand1, operand2)
            stack.append(result)
        else:
            stack.append(int(operand))

    return stack.pop()

def main():
    while True:
        print("Entrez un calcul (ou tapez 'exit' pour quitter) : ")
        expression = input().strip()
        if expression.lower() == 'exit':
            break
        try:
            result = calculate(expression)
            print(f"Résultat : {result}")
        except Exception as e:
            print(f"Erreur: {e}. Assurez-vous que l'expression est correcte.")

if __name__ == "__main__":
    main()
