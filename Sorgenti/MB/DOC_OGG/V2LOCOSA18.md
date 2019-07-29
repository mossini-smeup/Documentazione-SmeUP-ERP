## Obiettivo
Costruire un sottoinsieme partendo da un insieme di partenza. Dare la possibilità all'utente, tramite Drag&Drop, di scegliere singolarmente gli elementi da includere nel sottoinsieme.

## La scheda LOA18

La scheda si suddivide in 2 parti :  quella a sinistra contiene l'insieme di partenza (costruito tramite i parametri passati alla scheda), mentre la parte di destra contiene il sottoinsieme di arrivo (cartella di un carrello) da popolare tramite Drag&Drop.
Le due sezioni possono essere esposte alternativamente tramite i componenti, matrice, albero, image list.

Per ogni approfondimento riguardo alla scheda e ai suoi componenti, rifarsi allo script, alla documentazione del B£SER_25, a quella del carrello B£CARR e a quella del Drag&Drop.

## Esempi LOA18
Per poter usare il LOA18 occorre specificare nei parametri di lancio il tipo di **visualizzazione** e i **parametri** : 
D.FUN.STD F(EXD;*SCO;) 2(MB;SCP_SCH;LOA18) 4(;;A01) P(TPaOgg([A]) NomLis([B]) NomCar([C]) Id([n]))

Le visualizzazioni sono quelle specificate precedentemente.

I parametri sono : 
-**TPaOgg** :  tipo parametro dell'oggetto di cui si vuole visualizzare la lista :  per esempio CNCLI, TAB£NAR, TAV§P, etc.
-**NomLis** :  è il nome della lista associata all'oggetto. Se non viene passata si assume la lista di tutti gli elementi.
-**NomLisD** :  nome lista di arrivo. La lista deve essere una lista dell'oggetto indicato in TPaOgg di tipo C/ (Carrello Utente) G/ (Carrelli Generale).
-**Carrello** :  nome carrello. Viene assunto l'utente (il tipo è fisso TAB£U). Quest'ultimo in coppia al parametro NomCar sono alternativi al parametro NomLisD
- **NomCar** :  è il nome della cartella di un carrello
-**CmpO** :  Componente per lista origine. Se vuoto viene assunta matrice, se "T" viene utilizzato l'albero, se "I" l'image list.
-**CmpD** :  Componente per lista di destinazione. Se vuoto viene assunta matrice, se "T" viene utilizzato l'albero, se "I" l'image list.
-**TitO** :  Titolo per sezione origine. Opzionale, se non viene passato assume, se passata una lista, la decodifica della lista, vivecersa "Scelta Lista"
-**TitD** :  Titolo per sezione destinazione. Opzionale se non viene passato assume la descrizione della lista/carrello d'origine.
-**SchO** :  Se la lista origine viene mostrata in matrice può essere passato lo schema con cui presentare questa lista.
-**NSetO** :  Di default nella sezione della lista origine viene presentata la possibilità di modificare l'istanza di riferimento e/o lo schema. Tramite questo parametro, valorizzato ad 1 è possibile nascondere questa sezione.
-**Id** :  è un numero identificativo in caso di chiamata multipla nella stessa scheda.







