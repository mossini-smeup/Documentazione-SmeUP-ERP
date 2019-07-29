 :  : PRO Cod(A01) Txt(Esercizi) STAT(00) RESP(SCIMAM)

 :  : ATT Cod(001) Txt(Il mio Desktop in Sme.UP)  STAT(10) RESP(LANSIL)
//--***************************************************************
//--  IL MIO DESKTOP IN SMEUP                              *
//--***************************************************************
01. In SpotLight digitare "Desktop"
Chiamiamo "SpotLight" il campo in alto a destra in Looc.UP
Possiamo aprire il desktop e lavorare sui file lì contenuti
Si otterrà quanto presente nella funzione (A) associata a questo esercizio
 :  : DEC T(J1) P(FUN) D(A.Il mio Desktop) K(F(EXD;*SCO;) 1(J1;PATHDIR;"(("USER.HOME"))"\Desktop))

02. Proprietà della matrice.
Scopo di questo passo è presentare le proprietà fondamentali della matrice.
In questa matrice posso vedere l'elenco dei file e delle cartelle che sono sul mio desktop

02.A. Spostare una colonna
Spostare la colonna "Descrizione" in seconda posizione (di fianco alla colonna "nome") dalla posizione originaria in cui si trova (7/8 posizione)
Per spostare una colonna posso utilizzare il Drag&Drop sull'intestazione della colonna che voglio spostare. Mentre sposto la colonna si creano delle frecce verdi per indicarmi dove sto andando a mettere la colonna che ho "sollevato"

mettere la colonna che ho "sollevato"
02.B. Eliminare una colonna<
Eliminare la colonna "Path" e/o la colonna "Attributi"
Quando in una matrice voglio eliminare una colonna devo allontanare con il Drag&Drop l'intestazione della colonna stessa.
Allontanandomi dalla sua posizione originaria compare una "X" nera, che sta ad indicare che sto per eliminare la colonna.

02.C. Riordinare per una colonna
Riordinare per "Data ultima modifica" o per "dimensione"
Per riordinare una matrice per una colonna posso cliccare sull'intestazione della colonna in oggetto.
Un click produce l'ordine ascendente, un altro click inverte l'ordine in discendente

03.  Colonne aggiuntive
Per colonna aggiuntive si intendono delle colonne che posso aggiungere come "informazioni aggiuntive" di una colonna che esiste già nella matrice : 
Ad esempio : 
Astrattamente data una persona potrei aggiungere una colonna con il colore dei suoi capelli, che macchina sta guidando o la sua data di assunzione
Data una data, una colonna aggiuntiva potrebbe essere il giorno della settimana, il mese o il segno dell'oroscopo cinese di quella data.
Se in una matrice ho una provincia, una colonna aggiuntiva può essere la sua regione o il capoluogo della provincia stessa.

03.A. Aggiungere una colonna
Alla colonna "Data ultima modifica"  aggiungere il "giorno della settimana" di quella data.
Facendo "tasto destro" sull'intestazione "Data ultima modifica"
Colonne aggiuntive -> Informazioni Calcolate -> "Giorno della settimana"

03.B. Aggiungere la descrizione
Aggiungere la descrizione della colonna appena aggiunta.
Una delle "colonne aggiuntive" principali e la descrizione di un oggetto.
Facendo "tasto destro" sull'intestazione "Giorno della settimana"
Colonne aggiuntive -> Descrizione -> Descrizione

05. Operazioni sulla matrice

05.A. Abilitare il "Conta"
Abilitare il "conta" della colonna appena aggiunta
colonna e facendo "tasto destro" posso scegliere le diverse operzioni).
colonna stessa : 
- Quando ho valori numerici (i campi colorati di verde) posso calcolare la somma, la media, il minimo, il massimo e contare gli elementi.
- Quando ho colonne oggettizate (i campi colorati di gialli) posso avere solo il valore conta.

05.B. Raggruppare per una colonna
i l'intestazione di una colonna per raggruppare".

05.C. Filtrare un valore
Filtrare la colonna "Giorno della settimana" scegliendo solo il giorno della settimana che ha più file.
Sulla intestazione di ogni colonna c'è un "imbutino" nero che appare quando con il mouse mi muovo sull'intestazione stessa.
Cliccando su questo simbolo si apre l'elenco dei valori presenti e posso scegliere uno o più valori che mi interessa analizzare.
Nel nostro caso il giorno con il maggior numero di file.
Astrattamente solo le persone che hanno i capelli castani.

06. La scheda della data
Anche la data è un oggetto, e ha tutta una serie di sue proprietà.
Scegliendo una data qualsiasi di quelle nella colonna "Data ultima modifica" posso fare "tasto destro" -> "Scheda"
Analizzare quindi la scheda della data proposta.
In particolare
- La pagina di internet collegata
- Le proprietà evidenziate a destra e le immagini associate ad alcune proprietà (ho l'immagine del segno zodiacale che è un'immagine di una proprietà della data che sto analizzando).
Posso vedere la scheda esemplificativa di una data nella funzione (B) delle funzioni associate a questo esercizio

 :  : DEC T(J1) P(FUN) D(La scheda della data OGGI) K(F(EXD;*SCO;) 1(D8;*DMYY;&OGI))



 :  : ATT Cod(002) Txt(Ricerca)  STAT(10) RESP(MOROLE)

01.La Ricerca in Sme.UP
//-- ********************** CAPITOLO 1 **********************

In Sme.UP è possibile effettuara una ricerca su diversi moduli e anche a livello "globale" (che approfondiremo più avanti). Per semplificare l'identificazione delle funzionalità fondamentali abbiamo pensato di creare
una scheda "CERCA"  (che troviamo scrivendo 'cerca' nello spotlight in alto)  con un menu a sinistra dove sono elencati alcuni contesti di Sme.UP .

02.Menu ad albero
//-- ********************** CAPITOLO 2 **********************

Nella scheda "cerca" troviamo il menu (albero) sulla sinistra con diversi contesti (ad esempio :  AR->articoli, CM->commesse ecc.-> che a loro volta hanno diverse caratteristiche come codice e descrizione ad esempio )
Cliccando quindi su CN :  Commesse avremmo il campo di ricerca contestuale della commessa.
Cliccando invece su "codice" (che sta sotto la commessa) potremmo cercare la commessa mettendo il codice (sempre e solo nel contesto commessa).

03.Tutti i contesti
//-- ********************** CAPITOLO 3 **********************

L'ultima voce del menu a sinistra (ALL :  Tutti i contesti) riguarda tutti i contesti di Sme.UP, quindi lo spotlight in questo caso diventa globale.






