# Passaggio interno forzatura e congelamento
Nel processo di schedulazione è possibile impostare forzatura e congelamento.
Queste informazioni non possono essere immediatamente registrate nell'archivio finale (S5IRIS) in quanto devono andare perse se si rinuncia al salvataggio della schedulazione.
Non pare opportuno salvare le informazioni originali, scrivere nell'archivio quelle della sessione, e all'uscita, per rinuncia, eseguire il ripristino :  se si verificasse una fine anomala del lavoro, gli archivi definitifi risulterebbero deteriorati.
Tuttavia di esse si deve tener conto nella rischedulazione all'interno della stessa sessione. Inoltre, si deve tener conto dell'eliminazione di una forzatura o di un congelamento.
Per questo motivo è stato realizzato un procedimento articolato di memorizzazione e ripristino.


# Campi di DSIRIS
## Campi generali (G)
XITFOR - Tipo risorsa forzata / congelata
XICFOR - Codice risorsa forzata / congelata
XINFOR - N.ro congelamento
## Campi di sessione (S)
XITFSE - Tipo risorsa forzata / congelata
XICFSE - Codice risorsa forzata / congelata
XINFSE - N.ro congelamento


# DSFORZ (di appoggio per memorizzazione)
## Campi generali
XFNFOR - N.ro occorrenza
## Campi per individuare l'impegno in DSIRIS (I)
XFTIOG - TIpo oggetto
XFPAOG - Parametro oggetto
XFCDOG - Codice oggetto
XFFASE - Codice fase
XFFSUD - Numero progressivo suddivisione
## Campi di appoggio (A)
XFTFSE - Tipo risorsa forzata / congelata
XFCFSE - Codice risorsa forzata / congelata
XFNFSE - N.ro congelamento


# Modalità esecutiva
Nel programma di caricamento DSIRIS a partire da S5IRIS
 :  : DEC T(OJ) P(*PGM) K(S5SMES_01I)
I campi dell'archivio vengono copiati in (G)
Alla prima costruzione della DS (quando questo programma non è richiamato per rischedulazione) oppure se l'impegno è iniziato, i campi (G) vengono copiati in (S). Il motivio per cui questa operazione viene eseguita anche in rischedulazione, se l'impegno è in corso, deriva dal fatto che su di esso può essere stato dichiarato un avanzamento dopo il primo richiamo, che fa divenatre l'impegno in corso, cosa che ha la precedenza su congelamenti e forzature.
In tutti i programmi vengono utilizzati i campi (S) :  il motivo che, ad ogni caricamento, vengono riportati i campi (G) è puramente documentativo. In questo modo si potrebbe rispondere alla domanda :  che modifiche sono state fatte in questa sessione?
In particolare, le forzature e i congelamenti (inseriti, variati o eliminati) vengono registrati nei campi (S) nel programma di interazione con il GANTT
 :  : DEC T(OJ) P(*PGM) K(S5SMES_D4)

Successivamente, sempre nella fase iniziale di caricamento, se presenti forzature (almeno un elemento in DSFORZ), viene eseguito il programma di aggiornamento forzature
 :  : DEC T(OJ) P(*PGM) K(S5SMES_01F)
Viene scandito DSFORZ e, per ogni elemento, viene letto il corrispondente elemento di DSIRIS e si copiano i campi da (A) a (S).
All'inizio, dopo il primo caricamento di DSIRIS, D0FORZ è vuota, quindi questa funzione viene eseguita solo dal secondo richiamo (di rischedulazione), successivamente alla reinizializzazione DS che andiamo ad illustrare.

Quando si chiede la rischedulazione, come primo passo viene eseguita la reinizializzazione delle DS
 :  : DEC T(OJ) P(*PGM) K(S5SMES_03)
In questo programma viene ricostruita DSFORZ a partire dai campi (S), in modo da essere disponibili per l'aggiornamento forzature. Dopo di ciò, sempre in questo programma, viene eliminato DSIRIS.

Ci si ricollega poi al normale caricamento iniziale : 
Costruzione di DSIRIS. Non essendo il richiamo iniziale, i campi (S) rimangono vuoti.
Aggiornamento forzature, in base a quanto memorizzato in DSFORZ.

Nel seguito riportiamo lo schema di quanto esposto

> -->  S5SMES_01I
|       Sempre :  riempie campi G
|         Se primo richiamo :  copia i campi da G a S
|         Altri richiami :  i campi S restano puliti
|           |
|           |
|     S5SMES_01F
|       Se DSFORZ non è vuota (può esserlo solo dal secondo
|       richiamo) copia i campi da A a S
|           |
|           |
|     S5SMES_D4
|       Aggiorna i campi S
|           |
|           |
|         Rischedulazione ? NO ---> S5SMES_25 (aggiorna S5IRIS dai
|           SI                                 campi S)
|           |
|           |
|     S5SMES_03
|      Ricostruisce DSFORZ dai campi S
|      Elimina DSIRIS
|           |
|           |
 -----------




Dato che questo processo implica una modifica alle DS della schedulazione, per altre informazioni che si intendono inserire e utilizzare nel corso della sessione, ma memorizzare soltanto se si conferma la schedulazione, è stata prevista un'altra modalità (più compatta, in quanto raggguppata in un unico programma).
Essa è stata implementata per la gestione del "Vincolo esterno al più presto", attivata nello script dei parametri (posizione 94)

# Gestione vincolo esterno al più presto (VPP)
 :  : DEC T(MB) P(BCDSRC) K(PAR_SCP) L(1)
E' stato realizzato a questo scopo il programma
 :  : DEC T(OJ) P(*PGM) K(S5SMES_65)
che ha le seguenti funzioni : 
INZ - Per inizializzare la DS di memorizzazione (lanciato da S5SMES_01I prima della lettura degli impegni, se è il primo richiamo, e da S5SMES_03)
MEM - Per memorizzare il VPP presente in S5IRSE (lanciato sempre da S5SMES_01I per ogni impegno letto)
RIF - Per rifasare il VPP (lanciato da S5SMES_03 prima di pulire DSIRIS)
RIT - Per ritornare se il VPP è bloccato (lanciato da S5SMES_D4 e da S5SMES_67)
Il richiamo dal S5SMES_D4 del S5SMES_65 in RIT, nella scrittura della riga di GANTT, ha lo scopo di decidere il disegno della cella (che è diverso a seconda che essa non abbia in VPP, lo abbia modificabile o non modificabile).

Esponiamo infine il colloquio, interessante per conoscere la modalità di aggiunta informazioni ad un dettaglio o a un impegno BCD, attraverso una finestra di emluazione.
Quando, sempre nel S5SMES_D4, si seleziona la voce di POPUP di gestione del VPP, esso richiama il S5SMES_67, che, a sua volta, richiama S5SMES_65 in RIT, per conoscere se il VPP è modificabile.
Questa informazione, insieme alle altre necessarie per la gestione del VPP, repertite dalla memoria attrraverso il puntatore ricevuto e parcheggiate nella DS
 :  : DEC T(MB) P(QILEGEN) K(£S5SM_D2) L(1)
sono memorizzate con la £G00.
Dopo di ciò, il S5SMES_67 (in un lavoro LOOCUP LO_E) fa eseguire (tramite RFunction) il programma S5SMES_68 (in un lavoro di emulazione, da cui la necessità del colloquio tramite £G00), che presenta il VPP e, se è il caso, permette di aggiornarlo.
A sua volta, questo programma scrive l'informazione del VPP (inserito, modificato o annullato) nella £G00.
Al ritorno, S5SMES_D4 rilegge la £G00 e aggiorna la DS dell'impegno con gli estremi del VPP.























