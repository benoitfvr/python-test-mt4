def evaluate_rpn(expression):
    pass

def main():
    while True:
        print("Entrez un calcul (ou tapez 'exit' pour quitter) : ")
        expression = input().strip()
        if expression.lower() == 'exit':
            break
        try:
            result = evaluate_rpn(expression)
            print(f"Résultat : {result}")
        except Exception as e:
            print(f"Erreur: {e}. Assurez-vous que l'expression est correcte.")

if __name__ == "__main__":
    main()
