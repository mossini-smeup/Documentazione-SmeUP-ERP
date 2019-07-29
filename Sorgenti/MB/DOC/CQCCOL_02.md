## Obiettivo
 * Gestire Cicli di Collaudo con chiave variabile configurabile da utente.
 * Possibilità di gestire al contempo controlli per articolo, configurazione prodotto, articolo fornitore, macchina articolo fase, a seconda della tipologia lotto.

## Tabelle Interessate
_2_CQ1
Definisce la versione dei Cicli di Collaudo da utilizzare (se non specificato, si assume 'SM' :  Cicli di Collaudo versione con tipo variabile; al contrario, se si intende usare la versione con articolo, mettere 'CQ').
 :  : DEC T(TA) P(CQ1) K(*)
_2_CRJ
Definisce i tipi ciclo esistenti, descrivendone le caratteristiche principali.
 :  : DEC T(TA) P(CRJ) K(ART)
_2_B£G
Definisce il significato della parte variabile
 :  : DEC T(TA) P(B£G) K( )
_2_NSC
Definisce il contenitore note associato; in caso non sia assegnato viene assunto il tipo di default CDC.
 :  : DEC T(TA) P(NSC) K(CDC)
_2_CRNCQ
Definisce la struttura e i numeratori del numero identificativo di record degli archivi cicli e rilievi
 :  : DEC T(TA) P(CRNCQ) K(CCOL)
 :  : DEC T(TA) P(CRNCQ) K(CCO1)
 :  : DEC T(TA) P(CRNCQ) K(CCO2)
_2_C£I
Definisce la struttura dei dati della parte variabile del file
 :  : DEC T(TA) P(C£I) K(*)
_2_CR1
Attiva o meno la verifica che i rilievi obbligatori siano dichiarati
 :  : DEC T(TA) P(CR1) K(*)

## Dati Campionamento/articolo
Abilita o meno la gestione dei dati Piani Campionamento.
_2_ Tipo Parametro OAV Risalita 
La risalita avviene in questo modo : 

 - Dato il tipo ciclo def. in tab CQL, si valorizzano le chiavi con i valori del lotto. Si cerca il ciclo di quel tipo con quelle chiavi. Il modo con cui si valorizzano le chiavi è definito (cablato) nel pgm B£ICQC0. Se, ad esempio, la prima chiave della griglia è AR, il pgm B£ICQC0 sostituisce al primo codice il valore dell'articolo del lotto (T$ARTI); se la chiave è CN-FOR verrà sostituito l'ente di addebito (T$COEA)
 - Se non viene trovato un ciclo con queste chiavi, si sostituisce il valore generico (**) alle chiavi e si cerca questo stesso tipo ciclo con le nuove chiavi
 - Se il ciclo non viene ancora trovato, si prova a sostituire alle chiavi i valori dei rispettivi OAV (impostati in tab CRJ) e si cerca il tipo ciclo di risalita (T$CRJK) con le nuove chiavi
 - Se il ciclo non viene ancora trovato, si sostituisce il valore generico (**) alle chiavi
 - Se non viene trovato, si ricomincia da capo, provando le risalite tramite gli OAV definiti nel tipo ciclo di risalita.
In pratica si percorre una catena di elementi della CRJ, continuando a sostituire alle chiavi i valori dell'oav e cercando il ciclo del tipo def in T$CRJK .
Attenzione a non creare un loop infinito!

_2_ Suffisso Programma aggiustamento 
Se si desidera utilizzare un programma particolare di calcolo valori è possibile specificare un carattere che costituisce il suffisso del programma da richiamare.
Se presente un valore diverso da ' ' , viene lanciato il programma di aggiustamento CQCM50_x, dove 'x' è il carattere qui specificato.
Per maggiori informazioni sulla modalità di utilizzo del programma, leggere le note riportate nel sorgente del programma prototipo (CQCM50_X).

## Archivi Interessati
 :  : DEC T(OJ) P(*FILE) K(CQRICI0F)
 :  : DEC T(OJ) P(*FILE) K(CQCON20F)

_2_ Gli archivi di appoggio della gestione sono differenti da quelli della gestione precedente.
In caso si desideri utilizzare la nuova gestione, è necessario scrivere dei programmi di conversione (vedi programmi di conversione prototipo CQRICI_V21, per archivio cicli CQCON2_V21, per rilievi e misure).

## Approvazione/Rilascio Cicli di Collaudo
Le funzioni Approvazione/Rilascio delle fasi del Ciclo sono gestita dal Modulo Documentazione (CQ DOCU) sul tipo documento CCOL.
_7_Tipo Documento CQ0 
 :  : DEC T(TA) P(CQ0) K(CCOL)
_7_Numeratore Documento 
 :  : DEC T(TA) P(CRNDO) K(CCOL)

## Logica funzionamento
_7_Tipo Lotto CQL 
Da Tipo Lotto  CQL
 :  : DEC T(TA) P(CQL) K(OL)

_7_Tipo Ciclo di Collaudo CRJ
Se specificato assunto altrimenti nei parametri £Q1 definisco tutti i tipi ciclo compatibili con qs tipo lotto
 :  : INI **Gestione Parametri
 :  : CMD CALL C£CR01G '£Q1'
 :  : FIN

 :  : DEC T(TA) P(C£E) K(£Q1)
 :  : DEC T(TA) P(B£NLO) K(A10)

 :  : INI **Benestare di Collaudo
 :  : CMD CALL CQBC10G
 :  : FIN

### Verifica Presenza CICLO DI COLLAUDO
Legge tab. CRJ confronta con tipi ciclo previsti (parametri lotto)
Se tipo ciclo previsto nei parametri LOT interfaccia cicli per verifica presenza.

B£ICQC0 Formatta chiavi ciclo di collaudo.
Il tipo ciclo viene gestito sul campo T§PLAN file CQLOTT0F. Se non valorizzato da tabella CQL (campo T$CQLC).
Dal tipo lotto tab. CQL viene ricavato il tipo ciclo (CRJ) e la griglia oggetti B£G dal campo T$CQL6. Se T$CQL6 non valorizzato griglia di controllo da CRJ.
A seconda del valore delle chiavi previste dalla griglia di controllo, vengono assegnati i valori ricavati dal file CQLOTT0F.
In caso di creazione nuove griglie bisogna modificare di conseguenza anche il presente pgm di cablatura.

B£ICQC_SM Interfaccia cicli di collaudo.
Il programma si occupa di costruire il ciclo con le regole impostate
Se in TAB CRJ è previsto un pgm di aggiustamento, viene lanciato in uscita da ogni dettaglio del ciclo, che permette di cambiare i valori ottenuti.
L'obiettivo di questa exit è quello di costruire fasi con valori variabili descritti da regole esterne, ad esempio parametri (vedi pgm esempio CQCM50_X).

 :  : INI **£IFCQC /COPY  Cicli di Collaudo
 :  : CMD CALL TSTCQC
 :  : FIN

### Esempio 01      >>** **Verificare conformità lotto XXXXXXXXXX con ogg : **
Tipo Lotto      AG
Articolo        A
Configurazione  **
Possiede  . Ciclo di Collaudo (tipo YD1) con terza chiave cliente **
           . Associato alla tabella CQL sono previsti tipo e parametro
           . primario e secondario che descrivono il significato delle
           . chiavi varibili del lotto qualità (Articolo,campo libero1)
           . e il tipo ciclo di collaudo assunto.
           . Il programma d'intefaccia cicli di collaudo si occupa di
           . associare al lotto i controlli da effettuarsi.

## Verifiche oggetti
 :  : DEC T(OJ) P(*FILE) K(CQRICI0F)
 :  : DEC T(OJ) P(*FILE) K(CQCON20F)

 :  : DEC T(OJ) P(*PGM) K(B£ICQC0) Formatta chiavi Ciclo di Collaudo.
 :  : DEC T(OJ) P(*PGM) K(B£ICQC_SM) Interfaccia Ciclo di Collaudo.
 :  : DEC T(OJ) P(*PGM) K(B£ICQC_CQ) Interfaccia Ciclo di Collaudo.
 :  : DEC T(OJ) P(*PGM) K(CQCM50G) Gestione Ciclo di Collaudo.

 :  : DEC T(TA) P(CRJ) K(ART)
 :  : DEC T(TA) P(B£G) K(*)
 :  : DEC T(TA) P(CQL) K(AG)

## Esecuzione
 :  : INI **Gestione Cicli di Collaudo**
 :  : CMD CALL CQCM50G
 :  : FIN

 :  : INI **Stampa Cicli di Collaudo**
 :  : CMD CALL CQCM51A
 :  : FIN

## Verifiche nell'applicazione
 :  : INI **Benestare di Collaudo**
 :  : CMD CALL CQBC10G
 :  : FIN

 :  : INI **Stampa Rilievi e Misure**
 :  : CMD CALL CQRM51A
 :  : FIN
