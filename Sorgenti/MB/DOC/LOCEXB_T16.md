### Variabili base

Queste variabili vengono caricamente nel momento parte un dinamismo collegato alla matrice, nella sezione di destinazione del dinamismo (o su se stessa se non esiste una sezione di destinazione) vengono caricate le seguenti variabili di sezione : 
Row = N° Riga
RowId = N° ID della Riga
Column = Colonna
T1 = Tipo Oggetto
P1 = Parametro Oggetto
K1 = Codice Oggetto
KV = Codice Oggetto Editato (es. per il campo numero se la cella è vuota viene messo 0)
CellTx = Contenuto colonna non editato (es. date D8*YYMD in K1 ho gg/mm/aaaa in Celltx aaaammgg)
Codicedellacolonna = Contenuto della cella corrispondente alla nome della colonna in corrispondenza della riga selezionata.
*ALLSH = Stringa con l'elenco di tutte le variabili di cui sopra

Ogni volta che faccio tasto destro all'interno della cella, vengono invece caricate le stesse variabili di sezione, ad esclusione della variabile *ALLSH, con suffisso "POPUP.".
