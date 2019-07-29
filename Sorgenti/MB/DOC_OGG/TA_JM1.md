# JM1 - Personal. analisi mancanti
## OBIETTIVO
Contenere tutte le condizioni specifiche della impostazione iniziale dell'applicazione.
## UTILIZZO
Viene letta all'inizio dei programmi per condizionarne il comportamento.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM Codice
 :  : FLD T$DESC Descrizione
 :  : FLD T$J1DG __Direzione grafico__
Utilizzato dal programma di stampa dettaglio con collocazione grafica dei fabbisogni nel tempo.
Permette di scegliere il verso di rappresentazione del tempo : 
- 'S'  :  il tempo aumenta da destra verso sinistra;
- 'D'  :  il tempo aumenta da sinistra verso destra (valore assunto);
 :  : FLD T$J1GC __Giorni / carattere__
Utilizzato come sopra.
Permette di scegliere la scala di rappresentazione del tempo :  un numero da 1 a 9 specifica quanti giorni deve valere ogni carattere (valore assunto = 1).
 :  : FLD T$J1SR __Salto riga per livello 1__
Utilizzato dal programma di stampa dettaglio.
Se si immette un carattere qualsiasi, si ottiene in stampa una riga vuota di separazione ogni volta che inizia un assieme di livello 1.
 :  : FLD T$J1QD __Stampa quantità distinta__
Utilizzato come sopra.
Se si immette un carattere qualsiasi, si ottiene in stampa una colonna che contiene la quantità richiesta dalla distinta base per ogni fabbisogno.
 :  : FLD T$J1SO __Stato ordine massimo da stampare__
Utilizzato dai programmi di interrogazione e di stampa dettaglio.
Se sulla testata di un ordine di produzione il codice di stato è inferiore al valore immesso, o se il codice del centro di lavoro attuale è vuoto, viene presentato il codice di stato, altrimenti viene presentato il codice del centro di lavoro attuale.
 :  : FLD T$J1DA __Descrizione articolo completa__
Utilizzato dal programma di stampa dettaglio.
Se si immette un carattere qualsiasi, la descrizione di ogni articolo viene stampata per esteso su una riga aggiuntiva, altrimenti viene stampata sulla stessa riga, ma può anche essere troncata in funzione della lunghezza del codice articolo.
 :  : FLD T$J1CA __Lunghezza codice articolo__
Utilizzato dai programmi di interrogazione e di stampa dettaglio.
Permette di ottimizzare lo spazio occupato dal codice articolo, riducendolo al minimo per ogni installazione.
Se non impostato è assunto 15.
 :  : FLD T$J1AS __Attivazione scenari__
È un elemento fisso V2/MASCE :  definisce la modalità di applicazione scenari in questa applicazione.
 :  : FLD T$J1FA __Fonte fabbisogni primari (A)__
È un elemento della tabella M5F :  definisce la fonte futura che costituirà i fabbisogni primari dell'applicazione.
 :  : FLD T$J1FB __Fonte fabbisogni derivati (B)__
È un elemento della tabella M5F :  definisce la fonte futura che costituirà i fabbisogni derivati dell'applicazione.
 :  : FLD T$J1FX __Fonte fabbisogni pianificati di produzione (X)__
È un elemento della tabella M5F :  definisce la fonte futura che costituirà i fabbisogni pianificati di produzione. Dovrà avere come origine 'PN'.
 :  : FLD T$J1FY __Fonte fabbisogni pianificati di acquisto (Y)__
È un elemento della tabella M5F :  definisce la fonte futura che costituirà i fabbisogni pianificati di acquisto. Dovrà avere come origine 'PN'.
 :  : FLD T$J1FZ __Fonte fabbisogni pianificati di lavorazione esterna(Z)__
È un elemento della tabella M5F :  definisce la fonte futura che costituirà i fabbisogni pianificati di lavorazione esterna. Dovrà avere come origine 'PN'.
 :  : FLD T$J1MP __Magazzino principale__
È un elemento della tabella MAG :  definisce il magazzino su cui viene eseguita l'applicazione. Va obbligatoriamente impostato
Se non impostato viene assunto il magazzino aziendale in tabella B£2.
Va obbligatoriamente impostato se assente il magazzino aziendale.
 :  : FLD T$J1SS __Sotto scorta genera fabbisogni__
Se impostato, la scorta è un impegno alla data di pianificazione. (SV)
 :  : FLD T$J1TD __Tipo documento per V5__
È un elemento della tabella V5  :  definisce il tipo documento che individua gli ordini clienti estratti durante il caricamento automatico dei fabbisogni indipendenti.
 :  : FLD T$J1LM __Tipo distinta per livello minimo (llc)__
È un elemento della tabella BRL :  definisce il tipo distinta di cui si considererà il livello minimo durante l'elaborazione. Se assente verrà assunto 'ART'.
 :  : FLD T$J1XT __Suffisso programma esterno__
Se impostato, verranno eseguiti, se presenti, i programmi di uscita con questo suffisso, nei vari passi dell'elaborazione.
_9_Esempi : 
-    Verifica se il fabbisogno va gestito a commessa;
-    Verifica la compatibilità tra un fabbisogno ed una copertura;
-    Riordinamento specifico fonti di disponibilità.

