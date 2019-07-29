# IMPORT LISTE DI CONTA DA EXCEL

## File import

Deve essere caricato in una cartella IFP dell'AS400.

Deve essere in formato CSV con separatore colonne ';'

Deve essere composto delle seguenti colonne : 
01 = Codice inventario;
02 = Area Giacenza;
03 = Tipo Giacenza;
04 = Magazzino;
05 = Articolo;
06 = Codice 1;
07 = Codice 2;
08 = Codice 3;
09 = Codice 4;
10 = Collo;
11 = Quantità effettiva;

Le prima riga puà essere di intestazione

## Controlli import

Se la prima riga è di intestazione impostare a "1" il campo di
richiesta parametri "Prima riga intestazione" in modo che non
sia considerata come riga di inventario.

Gestisce solo le righe che hanno codice inventario di lancio
corrispondente al codice inventario dei file.

Prima di eseguire l'import contolla che : 
- tutti i campi devono essere presenti ed esistenti
  (I codici in funzione del tipo giacenza)
- la quantità effettiva deve essere obbligatoria

Se è presente anche un solo errore non viene eseguito l'import

## Import
ATTENZIONE : 
Se si imposta a "1" il campo "Pulizia contato" viene azzerato tutto
il contato presente nell'inventario

Se la riga del file non è già presente nell'inventario la inserisce
in stato "30".

Se la riga del file è già presente nell'inventario aggiorna la
quantità effettiva e la porta in stato "30"

