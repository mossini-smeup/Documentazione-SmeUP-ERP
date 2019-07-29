
# Generalità
L'istante di partenza della schedulazione, vale a dire l'istante più basso in cui si può caricare una risorsa, viene richiesto all'atto del lancio come data e ora.
E' conveniente impostare una data in formatro variabile, in modo da non doverla modificare ogni volta (ad esempio ieri, oppure oggi, in funzione dello stato di completamento delle dichiarazioni).
L'ora, se non impostata, vale 00 : 00 : 00 (ovvero l'istante iniziale della data). Ricordo che in SMEUP, gli istanti 24 : 00 : 00 del giorno N e 00 : 00 : 00 del giorno N+1, sono entrambi validi (e considerati uguali nel confronto tra istanti, se eseguiti con l'apposita procedura £P003).
Vi sono tuttavia alcuni accorgimenti che permettono di modificare in vari modi l'istante di partenza, per soddisfare alcune necessità specifiche.
Il programma che determina l'istante di partenza è
 :  : DEC T(OJ) P(*PGM) K(S5SMES_T1)
Ricordo che queste correzioni sono eseguite sia prima della schedulazione, sia prima della rischedulazione, con i dati aggiornati nel frattempo (ad esempio, come vedremo, dichiarazioni di attività, modifiche al calendario).

## Schedulazione Real Time
La schedulazione "Real Time" va predisposta impostando il campo opportuno (posizione 88 nello script dei parametri)
 :  : DEC T(MB) P(BCDSRC) K(PAR_SCP) L(1)
Se al lancio della schedulazione non viene impostato un istante di partenza, viene assunto l'istante di lancio.
Verosimilmente deve essere attivo un ritorno in tempo reale delle dichiarazioni dal campo, in modo che gli impegni risorse siano sempre aggiornati.
E' inoltre obbligatorio che anche la data sia quella odierna, impostata sia in modo esplicito sia implicito (&OGI00). Il sistema, tuttavia, non compie nessuna forzatura in questo senso.
L'insieme di queste impostazioni fa sì che ogni nuovo lancio di BCD abbia la funzione di WORK LIST in tempo reale; risponda quindi alla domanda :  qual'è l'impegno più urgente che posso eseguire adesso?
Questa è la prima correzione, indipendente dalle risorse, che viene eseguita, opzionalmente, all'istante di partenza.

## Partenza mossa
La partenza mossa  va predisposta impostando il campo opportuno (posizione 77 nello script dei parametri).
 :  : DEC T(MB) P(BCDSRC) K(PAR_SCP)  L(1)
come suffisso dell'exit
 :  : DEC T(MB) P(BCDSRC) K(S5SMX_16X)  L(1)
Essa permette, per ogni risorsa che si schedula di avanzare l'istante di partenza impostato (manualmento o Real Time) secondo modalità specifiche.
Sono disponibili le seguenti exit standard
 :  : DEC T(OJ) P(*PGM) K(S5SMX_161)
 :  : DEC T(OJ) P(*PGM) K(S5SMX_162)
 :  : DEC T(OJ) P(*PGM) K(S5SMX_163)
che eseguono il programma comune
 :  : DEC T(OJ) P(*PGM) K(S5SMES_70)
La logica che sottintende la partenza mossa, con le exit standard, è di operare con le dichiarazioni di attività non allineate alla stesso istante, e quindi di far partire la disponibilità di ogni risorsa dalla fine dell'ultima attività dichiarata.
Questo istante può essere
* la data dell'ultima attività su S5IRIS
* la più alta data di registrazione su P5ATTI
* il più alto istante di fine evento su P5ATTI

## Correzione con calendario
L'istante di partenza di ogni risorsa (con le eventuali correzioni per partenza mossa) viene infine portato al primo istante valido per il calendario della risorsa. Questa condizione è essenziale per la strategia di schedulazione. Infatti, se l'istante di inizio disponibilità di una risorsa fosse inferiore alla sua apertura, si correrebbe il rischio di non scegliere l'impegno più urgente.
NB :  dato che si utilizza questa correzione anche nell'avanzamento della disponibilità di una risorsa, dopo avervi piazzato un impegno, anche in questo caso viene eseguita la correzione  con il calendario. Se, ad esempio, dopo un impegno si vuol far riaprire la risorsa il giorni successivo, è sufficiente eseguire la exit opportuna di partenza disponibilità risorsa (S5SMX_19X) impostando le ore 24 : 00 : 00. Sarà cura della correzione standard del calendario (eseguita successivamente a questa exit) di avanzare al primo istante valido.

## Risorse a capacità infinita
Per queste risorse non vengono eseguite le correzioni di partenza mossa e di calendario, in quanto per loro l'istante di partenza non viene controllato nella strategia di sxchedulazione. Inoltre, nella loro datazione, sia l'istante di partenza sia quello di arrivo sono calcolati in modo da rispettare il loro calendario.

