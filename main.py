from operazioni import somma, sottrazione, moltiplicazione, divisione

def main():
    print("--- Calcolatrice Python con uv ---")
    print("Operazioni disponibili:")
    print("1. Somma (+)")
    print("2. Sottrazione (-)")
    print("3. Moltiplicazione (*)")
    print("4. Divisione (/)")
    print("5. Esci")

    while True:
        scelta = input("\nScegli un'operazione (1-5): ")

        if scelta == '5':
            print("Chiusura calcolatrice. Ciao!")
            break

        if scelta in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Inserisci il primo numero: "))
                num2 = float(input("Inserisci il secondo numero: "))
            except ValueError:
                print("Errore: Inserisci solo numeri validi.")
                continue

            risultato = None

            if scelta == '1':
                risultato = somma(num1, num2)
                operatore = "+"
            elif scelta == '2':
                risultato = sottrazione(num1, num2)
                operatore = "-"
            elif scelta == '3':

                risultato = moltiplicazione(num1, num2)
                operatore = "*"
            elif scelta == '4':
                risultato = divisione(num1, num2)
                operatore = "/"

            if risultato is not None:
                print(f"Risultato: {num1} {operatore} {num2} = {risultato}")
            else:
                print("Errore: Operazione non riuscita (controlla i tipi o la divisione per zero).")
        else:
            print("Scelta non valida.")

if __name__ == "__main__":
    main()
#test