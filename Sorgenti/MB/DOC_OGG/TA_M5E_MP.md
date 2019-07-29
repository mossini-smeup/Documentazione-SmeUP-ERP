## Voce MPS
>Se l'origine è MP (voce MPS)  : 
Parametro 1 : 
>Pos.1/6 :   Codice piano (obbligatorio)
>Pos.7 :     - '1' se considerare il piano con codice più alto con radice uguale
.                     al codice impostato;
.               - ' ' se considerare solo il piano impostato.
>Pos.8     È significativa se l'applicazione è multimagazzino; definisce il
.               magazzino a cui appartiene la vista : 
.               - ' '  il codice magazzino viene assunto dal magazzino definito
.                      nella tabella piano.
.               - '1'  il codice magazzino è la chiave 1 della vista.
.               - '2'  il codice magazzino è la chiave 2 della vista.
>Pos.9     Se impostata, l'articolo è la chiave 2, se lasciata in bianco è la
.               chiave 1.
.               **NB** :  è compito del compilatore delle fonti, assicurarsi la
.               congruenza tra quanto definito nelle posizioni 8 e 9 e le chiavi
.               impostate nella vista :  questa impostazione non viene eseguita nel
.               programma per motivi di prestazioni.
Parametro 2 : 
>Pos.1/3 :   Codice vista (obbligatoria).
>Pos.4 '1/5'  :  numero di MPPIAN da considerare, (obbligatorio)

