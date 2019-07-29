# C£L - Listini e condizioni
 :  : DEC T(ST) K(C£L)
## OBIETTIVO
Permette di gestire gruppi di dati a cui possono essere associati valori liberi. Rientrano in questo caso la gestione dei listini o delle valute.
## SOTTOSETTORI
Permettono di separare i listini da altre tipologie di valori. Sono previsti per sviluppi dell'utente. SME_UP utilizza sempre il sottosettore bianco.
## CONTENUTO DEI CAMPI
 :  : FLD T$LISS **Sottosettore sezioni ammesse**
Indica un sottosettore di C£V utilizzato per la verifica delle sezioni valide.
 :  : FLD T$VDEL **Validità data / lotto Da/A**
Indica se, per la ricerca del valore valido in funzione di quantità e data, si deve utilizzare il limite
 :  : FLD T$C£LA **Categoria listini**
Permette di caratterizzare il listino. A livello di tipologia documento (V5D) o tipologia ente (BRE) si può definire una categoria che sarà utilizzata come condizione di validità del listino. Ai clienti, ad esempio, potrò assegnare solo listini di vendita ecc.
 :  : FLD T$C£LB **Data inizio/fine di validità**
Utilizzata dalle funzioni di controllo validità dei listini e di ricerca dei listini validi ad una data.
 :  : FLD T$C£LD **Livello protezione**
È un elemento della tabella B£W, sottosettore LI. Su di esso si impostano le autorizzazioni delle righe appartenenti a questo listino.
 :  : FLD T$C£LE **Natura**
Caratterizza i listini di questo tipo.
E'un campo necessario per le interrogazioni di Loocup
