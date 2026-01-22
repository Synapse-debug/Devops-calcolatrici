# README

Questo codice contiene una semplice calcolatrice che esegue l'operazione di:

- somma tra due numeri

Include anche test unitari per verificare il corretto finzionamento della funzione somma

- verifica che l'interprete sia quello giusto
  - where python3 (Windows)

- Installare le dipendenze
  - pip install pytest

## Esecuzione normale

python3 calcolatrice.py

## Esecuzione dei test

pytest test_calcolatrice

## Installazione ambiente virtuale

py -m venv .venv
uv pip install --upgrade pip
uv pip install -r requirements.txt
uv pip sync requirements.txt
uv pip compile requirements.txt

docker build -t devops-calcolatrice:local .
docker run --rm -it devops-calcolatrice:local

# Devops-calcolatrice
