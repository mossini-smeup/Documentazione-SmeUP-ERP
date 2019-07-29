# B£S - Significato protezioni applicazione
 :  : DEC T(ST) K(B£S)
## OBIETTIVO
Descrivere i significati delle opzioni associate ad una classe di autorizzazione codificata nella tabella B£P.
## SOTTOSETTORI
Utilizzati per collezionare insiemi di funzioni omogenee. In generale ogni applicazione possiede un sottosettore delle funzioni tipiche. Il sottosettore GD contiene tutte le azioni di base quali immissione/variazione/ecc.
## CONTENUTO DEI CAMPI
 :  : FLD T$DESC **Descrizione**
È possibile rendere dinamica la descrizione inserendo il riferimento ad un oggetto, usando la sintassi tipica della documentazione attiva. Quindi, ad esempio :  T(CN) (P(CLI) K(000001) sostituisce la descrizione con il nome del cliente.
Il codice a sua volta può contenere delle variabili che saranno sostituite dal programma. In particolare abbiamo :  &FU = Codice della funzione. Quindi, ad esempio :  T(V2) (P(LOBAS) K(&FU.1) per la funzione MNU.BAR diventa T(V2) (P(LOBAS) K(MNU.BAR.1) e quindi la sua decodifica.
 :  : FLD VPT,1 **Valori ammessi 01/10**
Valore ammesso come risposta.
 :  : FLD VPT,2.VPT,1 Valori ammessi 01/10
 :  : FLD VPT,3.VPT,1 Valori ammessi 01/10
 :  : FLD VPT,4.VPT,1 Valori ammessi 01/10
 :  : FLD VPT,5.VPT,1 Valori ammessi 01/10
 :  : FLD VPT,6.VPT,1 Valori ammessi 01/10
 :  : FLD VPT,7.VPT,1 Valori ammessi 01/10
 :  : FLD VPT,8.VPT,1 Valori ammessi 01/10
 :  : FLD VPT,9.VPT,1 Valori ammessi 01/10
 :  : FLD VPT,10.VPT,1 Valori ammessi 01/10
 :  : FLD T$B£SA **Valore assunto**
Deve essere uno dei 10 valori ammessi. Utilizzato in particolare per creare le autorizzazioni assunte (Utente=** e funzione = **) automaticamente, qualora mancanti all'interno del programma di riorganizzazione delle autorizzazioni. Se manca il valore assunto, viene assunto il primo dei 10 valori ammessi.
