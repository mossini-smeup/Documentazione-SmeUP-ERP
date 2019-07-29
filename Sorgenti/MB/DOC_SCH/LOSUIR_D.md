### UTILIZZO MESSAGGI

In queste schede vengono evidenziati le combinazioni possibili nell'utilizzo dei messaggi di conferma. Vengono esposte tutte le modalità grafiche possibili previste dell'attributo UirMGr - Modalità Grafica : 
* C :  Richiedi ed Esegui in Subsezione (Assunto)
* B :  Richiedi in Finestra, Esegui in Subsezione
* D :  Richiedi in Subsezione, Esegui in Nuova Finestra
* E :  Solo Richiesta in Subsezione

 ### NOTE OPERATIVE

 :  : R01 La struttura di richiamo

Tramite i tag G.SUB.UMC, G.SET.UMC e D.FUN.UMC è possibile lanciare una funzione, ponendo prima all'utente un richiesta di conferma esplicabile in una domanda specifica.

* Il tag G.SUB.UMC serve solo per identificare la subsezione, come una un subsezione che presenterà le sopracitate caratteristiche.
* Il tag G.SET.UMC serve per indicare quale sarà il messaggio che si andrà ad utilizzare (di default è la voce VO/M.MSGBA/BAS0101) e varie caratteristiche grafiche tramite le quali, il messaggio di conferma e la funzione stessa verranno posti all'utente.
* Il tag D.FUN.UMC serve per indicare quale funzione deve essere infine eseguita. Questo tag non si differenzia dal normale tag di funzione D.FUN.STD in nessun aspetto.

Esempio di richiamo (lancio scheda dell'applicazione B£)
 :  : PAR F(04) L(MON)
G.SEZ Pos(1)
G.SUB.UMC Tit="*NONE"
G.SET.UMC UirMGr="B"
D.FUN.UMC F(EXD;*SCO;) 1(TA;B£A;B£)


 :  : R01 I Messaggi

Quando si vuole specificare un messaggio specifico, questo può essere indicato tramite l'utilizzo delle voci. Qual'ora non si avesse familiarità con l'oggetto si rimanda alla scheda dell'oggetto in questione "VO" (il link è riportato a seguire).

Per quel che riguarda le voci da utilizzare come messaggi, specifici, si consiglia di utilizzare script avente nome corrispondente al modulo di riferimento (nell'esempio è stato utilizzato lo script del  modulo LOSUIR). Mentre per il codice si consiglia di utilizzare il prefisso UMC (nell'esempio abbiamo UMC001).

Si ricorda inoltre che indicando come parametro della voce M.filemessaggi è possibile tramite le voci fare inoltre riferimento ai "vecchi" file messaggi (es. VO/M.MSGBA/BAS0101 corrisponde al messaggio BAS0101 del file messaggi MSGBA). E' quindi possibile utilizzare anche tali messaggi come voci.

 :  : DEC T(OG) K(VO) I(Scheda della Classe Voce) L(1)

### NOTE SU ESEMPI

* Gli esempi sono suddivisi in due categorie : 
** Nella prima vedo il comportamento di default con il messaggio di conferma standard
** Nella seconda vedo il risultato dando indicazione di una voce specifica di conferma
* La funzione eseguita a seguito della conferma è sempre la stessa :  una matrice con l'elenco di tutte le applicazioni.





