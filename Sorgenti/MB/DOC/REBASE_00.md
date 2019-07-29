# Set'n play

## INTRODUZIONE
Il CRM ....
Digitare "applicazione RE" per accedere a la documentazione dinamica del CRM.
in partolare sotto la voce "sviluppo", "oggetti setup - RE - CRM" è possibile vedere una matrice che riclassifica tutti i moduli con relativi gestiti nel CRM.


## MODULI
I moduli del CRM sono : 

| 
| .COL Txt="Modulo" Lun="12" |
| ---|----|
| 
| .COL Txt="Descrizione" Lun="35" |
| 
| .COL Txt="Capitolo" Lun="12" |
| 
| .COL Txt="Descrizione" Lun="35" |
| 
| .COL Txt="Scheda" Lun="12" |
| 
| .COL Txt="Servizio" Lun="50" |
| 
| .COL Txt="Exit" Lun="10" |
| 
| .COL Txt="SCP_LAY" Lun="10" |
| REACCA|Account     |REACCA_01|Account    |REACCA_01|REACCA_01|REACCA_01U|CNNOM| |
| REREFE|Referenti   |REREFE_01|Referenti  |REREFE_01|REREFE_01|REREFE_01U|RN   | |
| REEVEN|Attività    |REEVEN_01|Attività   |REEVEN_01|REEVEN_01|REEVEN_01U|E3£C1| |
| RELEAD|Lead        |RELEAD_01|Lead       |RELEAD_01|RELEAD_01|RELEAD_01U|CM££3| |
| REOPPO|Opportunità |REOPPO_01|Opportunità|REOPPO_01|REOPPO_01|REOPPO_01U|CM£R3| |
|       |            |REOPPO_02|Prodotti   |REOPPO_02|REOPPO_02|REOPPO_02U|DR£CM| |
| REMARK|Marketing   |REMARK_01|Campagne   |REMARK_01|REMARK_01|REMARK_01U|CM£R1| |
|       |            |REMARK_02|Operazioni |REMARK_02|REMARK_02|REMARK_02U|CM£R2| |
| REVEND|Vendita     |REVEND_01|Ord/Off.   |REVEND_01|REVEND_01|REVEND_01U|     | |
| REMAMA|Socialmailer|REMAMA_01|Mail      |REMAMA_01|REMAMA_01|REMAMA_01U|     | |
| 


## OGGETTI COINVOLTI
Gli oggetti coinvolti nel CRM sono : 
* Account
* Referenti
* Campagne
* Operazioni di marketing
* Lead
* Opportunità
* Prodotti
* Attvità CRM
La gestione degli oggetti si basa sugli OAV.
Pertanto è necessario verificare ed eventualmente ricostruirle tutti gli oav degli oggetti coinvolti. Vedi "PROCEDURA DI INSTALLAZIONE"

_7_ACCOUNT
Per la gestione del CRM è necessario attivare gli Account.
Gli account sono enti di tipo "NOM".
Gli account garantiscono l'univocità di un ente nell'intero DB qualora sia presente contemporaneamente con diverse tipologie (Cliente, Fornitore...)
La sua attivazione induce una diversa modalità di gestione degli enti. E sempre necessario prima creare l'Account, perchè quando si crea un ente con un altra tipologia, per esempio un cliente, viene sempre chiesto prima da quale account derivarlo.
La gestione ente con account permette di codificare degli enti ancor prima che diventino clienti o fornitori e utilizzarli nel DB.

_7_REFERENTI
E' un nuovo oggetto di tipo "RN"(interfaccia £IRN). Gestisce la nuova anagrafica dei contatti REREFE0F.
E' strutturata principalmente con un identificativo, un nome, un cognome e un indirizzo mail.
Sostituisce la "£16" del BRESCO.
I dati di contatto tipo telefoni, etc.. sono gestiti in modo verticale nel C£ALIA0F con contesto "RN e definiti nella tabella "RER"

_7_CAMPAGNE
Sono commesse di tipo "£R1".

_7_OPERAZIONI DI MARKETING
Sono commesse di tipo "£R2"

_7_LEAD
Sono commesse di tipo "£R3"

_7_OPPORTUNITA'
Sono commesse di tipo "£R4"
Per questo oggetto insieme alla commessa si crea in automatico anche un documento di tipo "£CM"
Il numero documento è il codice commessa.
Gli articoli dell'opportunità (prodotti) sono le righe di questo documento.

_7_PRODOTTI
Sono articoli usati nelle opportunità

_7_ATTIVITA'
Le attività del CRM sono eventi di tipo "£C1".

# STRUTTURA DI NAVIGAZIONE
Ogni oggetto ha la seguente struttura di navigazione dal menù CRM
* Accesso
* Navigazione del molulo
* Ricerca libera
* Matrice dati

## RICERCA LIBERA £K41
In questo paragrafo mettiamo un accenno alla K41. Si rimanda comunque alla documentazione specifica di questa COPY (che al momento non c'è)
La K41 si appoggia al componente grafico SPL = Spotlight (dove si può mettere dentro un testo libero)
come si può vedere nella scheda di test della K41 (SCP_SCHESE/SMA_K41) dove ci sono alcuni esempi già compilati e la possibilità di fare i test

La K41 permette di cerare un oggetto secondo tutti i suoi OAV. le regole principali sono :  (per gli esempi ipotizziamo di essere nella ricerca di un account "CNNOM")
* la prima parola che metto la considera descrizione dell'oggetto (Es :  Gnutti)
* posso per ogni oggetto impostare che cosa voglio cercare dopo la parola "di", nel caso degli account ricerca la provincia (Es :  Gnutti di Brescia)
* posso usare la parola "e" oppure la parola "con" per aggiungere tutte le proprietà (Es :  Gnutti di brescia con settore automotive e commerciale Poiatti e inserimento maggiore di 01012016)
* posso avere alcune proprietà sui numeri/date scrivendo maggiore di, minore di

Nell'INPUT della funzione della K41 posso impostare alcuni campi : 
*StrTit()    =   Imposta la scritta che esce di fianco allo spotlight (es :  Opportunità attive di Corbetta)
*StrIni()    =   Imposta l'oggetto dello spotlight (es :  Opportunità)
*StrSuf     =   Aggiunge un suffisso "testuale" a quello che l'utente scrive (es :  con commerciale CORGIO) rimane invisibile all'utente
*StrWhe   =   Aggiunge un suffisso "SQL" a quello che l'utente scrive (funziona esattamente come l'StrSuf
*StrAll      =   Viene utilizzato per bypassare la richiesta tramite spotlight estraendo direttamente la matrice senza componente SPL
Di defualt la K41 è impostata per cercare solo gli oggetti con livello minore di 8

Oltre a questa impostazione bisogna tenere in considerazione che la K41 si basa sull'impostazione di alcuni ALIAS che posso usare per avere diverse parole che rispondono ad un campo.
Per vedere/caricare queste impostazioni vi invito ad andare nel TAB "Configurazione" nella scheda di esempio della K41 dove trovo i seguenti TAB
- Gestione descrizioni estese :  Scelto un oggetto "es :  CM£R4" posso impostare gli alias per ogni OAV (Es :  per il campo M$CDRE voglio che rispondano le parole Responsabile, Commerciale, Agente)
- Script standard configurazione oggetti :  Tutte le parole distribuite che rispondono agli oggetti "standard"
- Script utente configurazione oggetti :  Tutte le parole utente che rispondono agli oggetti
- Script utente configurazione campi :  In questo TAB posso impostare degli oggetti specifiche per impostare che per un oggetto, un campo del file che sarebbe libero è di default un oggetto

Oltre a questi alias esiste una normalizzazione delle descrizioni da lanciare (magari da mettere post inserimento agli oggetti più importanti e/o comunque da schedulare la sera). Questa normalizzazione permette di togliere spazi e caratteri speciali, per fare in modo che se cerco account "ROSSI" trovo anche eventuali account (scritti diversamente) RO-SS.I
Posso lanciare questa normalizzazione nel test dell K40 (T K40) lanciando la Funzione NOR - Metodo CLS - Tipo (CNNOM - ecc) (serve mettere una descrizione per farlo partire ma è ininfluente)

_7_Accesso
Digitare "CRM". Compariranno tutte le icone dei moduli del CRM, da dove è possibile accedere a tutte le funzioni navigazione del  modulo.

_7_Navigazine del modulo
La scheda di navigazione è divisa in due parti. A destra un menù e a sinistra la corrispondente
scheda dati. In particolare tra le funzioni c'è la riceca libera.

_7_Ricerca libera
La ricerca libera è una campo dove è possibile inserire una stringa di riceca per l'oggetto gestito dal modulo. Il risualtato della ricerca viene rappresentato dalla matrice dati del modulo.


_7_Matrice dati
La matrice rappresente i dati ottenuti dalla ricerca
Per ogni oggetto del CRM è stata definita una matrice di default : 

| 
| .COL Txt="Oggetto" Lun="12" |
| ---|----|
| 
| .COL Txt="Descrizione" Lun="50" |
| 
| .COL Txt="Scheda" Lun="10" |
| 
| .COL Txt="Servizio" Lun="10" |
| 
| .COL Txt="Exit" Lun="10" |
| 
| .COL Txt="ServizioOOld" Lun="10" |
| 
| .COL Txt="ExitOld" Lun="10" |
| CNNOM|Account                |REACCA_01|REACCA_01|REACCA_01U|REGESA_01|REGESA_01U| |
| RN   |Referenti              |REREFE_01|REREFE_01|REREFE_01U|REGESA_02|REGESA_02U| |
| CM£R1|Campagne               |REMARK_01|REMARK_01|REMARK_01U|         |          | |
| CM£R2|Operazioni di marketing|REMARK_02|REMARK_02|REMARK_02U|         |          | |
| CM£R3|Lead                   |RELEAD_01|RELEAD_01|RELEAD_01U|REMARK_03|REMARK_03U| |
| CM£R4|Opportunità            |REOPPO_01|REOPPO_01|REOPPO_01U|REMARK_04|REMARK_04U| |
| E3£C1|Attività               |REEVEN_01|REEVEN_01|REEVEN_01U|         |          | |
|      |Mail Marketing         |REMAMA_02|REMAMA_02|REMAMA_02U|         |          | |
| 

E' possibile personalizzare le colonne della matrice o filtrare i dati attraverso il programma utente con suffisso U del servizio standard (esempio REACCA_01U)
Per ogni riga ci sono delle azioni che permettono l'accesso alla gestione dei dati dell'oggetto.

# GESTIONE DATI
La gestione dei dati di un oggetto si basa sugli OAV.
Ogni dato è un OAV. Ogni OAV oltre a contenere il valore del dato, definisce anche le sue caratteristinche standard :  intestazione, tipo oggetto, lunghezza, tipo di visualizzazione...
La definizione dei campi da presentare in gestione si chiama struttura. Nella struttura oltre a indicare il campo si possono aggiugere e/o modficare alcune sue caratteristiche standard.
La struttura è uno script del file SCP_LAY.
Se per un oggetto non viene indicata la sua struttura vengono presentati tutti gli oav di tipo "I/" con le caratteristiche standard.
Per ogni oggetto del CRM è stata definita una sua struttura di default.
Per ogni oggetto del CRM è stata definita una matrice di default : 

| 
| .COL Txt="Oggetto" Lun="12" |
| ---|----|
| 
| .COL Txt="Descrizione" Lun="50" |
| 
| .COL Txt="SCP_LAY" Lun="10" |
| CNNOM|Account                |CNNOM |
| RN   |Referenti              |RN |
| CM£R1|Campagne               |CM£R1 |
| CM£R2|Operazioni di marketing|CM£R2 |
| CM£R3|Lead                   |CM£R3 |
| CM£R4|Opportunità            |CM£R4 |
| E3£C1|Attività               |E3£C1 |
| 

Costruita come XXYYY, dove XX è l'oggetto e YYY il parametro : 

Per ogni oggetto è possibile utlizzare un proprio SCP_LAY impostando la tabella B£Q, con i seguenti elementi fissi, la loro presenza ne innesta l'utilizzo.

| 
| .COL Txt="Oggetto" Lun="12" |
| ---|----|
| 
| .COL Txt="Descrizione" Lun="50" |
| 
| .COL Txt="Elemento B£Q" Lun="15" |
| CNNOM|Account                |£CNNOM |
| RN   |Referenti              |£RN |
| CM£R1|Campagne               |£CM£R1 |
| CM£R2|Operazioni di marketing|£CM£R2 |
| CM£R3|Lead                   |£CM£R3 |
| CM£R4|Opportunità            |£CM£R4 |
| E3£C1|Attività               |£E3£C1 |
| 

Per le attività sono stati definiti come defaulti oltre a tipo anche causale e categoria, nel
seguenti modo
* "£E3£C1"+XXX, dove XXX è la causale (N§CAEV), risalita
* "£E3£C1"+YYY, dove YYY è la categoria (N§CTEV), risalita
* "£E3£C1
Oltre all'SCP_LAY nella tabellea B£Q è possibile attivare un programma di exit sulla gestione dati,
una sottoscheda di info nella gestione (Con posizione orizzontale o verticare e dimensioni).
I proogrammi di exit sono relativi al programma standard di gestioen B£K89_XX dove XX è l'oggetto,
per una facile individuazione è meglio tenere lo stesso nome aggungendo un suffisso.
Esmepio exit B£K89_CNA per il programma Bstandard B£K89_CN che gestisce gli enti.
La sotoscheda di info è una scheda che risente di ogni invio nella gestione. E' utile aggiungerla quando in gestione si vogliono verificare istanze già presenti per quel dat. Per esempio in
immissione di un'opportunità si vule vedere se ci sono già opportnità aperte per quel account.


Come accenntato sopre la gestione di ogni oggetto passa da una nuova copy :  la £K89. Questa comunica con l'interfaccia grafica tramite il servizio LOA36_SE.
L'interfaccia è la gestione interagiscono tramite una struttura di schiere che contengono tutte le informazioni di un dato, sia di sruttura che di contenuto.
Ogni oggetto ha un suo particolare programma di gestione B£K89_XX dove XX è l'oggetto.
Ad ogni programma è poi associata una exit dove è possibile intervenire per modificare le caratteristiche di un campo, completare il contenuto di un campo in funzione del contenuto di un altro,  eseguire controlli specifici, agire prima e/o dopo l'aggiornamento ...
Per maggiori dettagli fare riferimento alla documentazione della £K89
- [£K89](Sorgenti/MB/DOC_OGG/P_TSTK89)

## PRECEDURA DI INSTALLAZIONE

## NUOVI FILES
_7_Referenti REREFE0F

## NUOVE TABELLE
_7_Tabella RE*.
_7_Tabella RE1.
_7_Tabella RE2.
_7_Tabella REA.
_7_Tabella REB.
_7_Tabella REC.
_7_Tabella REE.
_7_Tabella REF.
_7_Tabella REH.
_7_Tabella REI.
_7_Tabella REJ.
_7_Tabella REK.
_7_Tabella REL.
_7_Tabella REM.
_7_Tabella RER.

 :  : INI Importare la loro definizione dalla SMETAB
 :  : CMD UP FTB
 :  : FIN

## CREAZIONE SOTTOSETTORI E ELEMENTI TABELLE CRM

 :  : INI Eseguire il programma di controllo per la creazione/allineamento automatico tabelle
 :  : CMD C B£UTX61A 'RE'
 :  : FIN

## Controllare il contenuti delle seguenti tabella
 :  : DEC T(ST) K(RE*)
 :  : DEC T(ST) K(RE1)
 :  : DEC T(ST) K(RE2)
 :  : DEC T(ST) K(REA)
 :  : DEC T(ST) K(REB)
 :  : DEC T(ST) K(REC)
 :  : DEC T(ST) K(REE)
 :  : DEC T(ST) K(REFR1)
 :  : DEC T(ST) K(REFR2)
 :  : DEC T(ST) K(REFR3)
 :  : DEC T(ST) K(REFR4)
 :  : DEC T(ST) K(REH)
 :  : DEC T(ST) K(REI)
 :  : DEC T(ST) K(REJR1)
 :  : DEC T(ST) K(REJR2)
 :  : DEC T(ST) K(REJR3)
 :  : DEC T(ST) K(REJR4)
 :  : DEC T(ST) K(REK)
 :  : DEC T(ST) K(RELAU)
 :  : DEC T(ST) K(RELSN)
 :  : DEC T(ST) K(REM)
 :  : DEC T(ST) K(RER)
 :  : DEC T(ST) K(V£F)

## OAV BASE
**3.**rilanciare la costruzione degli OAV mediante
   la funzione COS metodo ALL della funzione TSTOAV.

  _9_Costruzione guidata modello attributi (slots) per i vari oggetti : 
 :  : INI **>**AR**Articolo
 :  : CMA  :  : FUN PG(REUT06) K1(AR)
 :  : FIN
 :  : INI **>**CN**Enti
 :  : CMA  :  : FUN PG(REUT06) K1(CN)
 :  : FIN
 :  : INI **>**CNNOM**Account
 :  : CMA  :  : FUN PG(REUT06) K1(CNNOM)
 :  : FIN
 :  : INI **>**RN**Referenti
 :  : CMA  :  : FUN PG(REUT06) K1(RN)
 :  : FIN
 :  : INI **>**CM**Commesse
 :  : CMA  :  : FUN PG(REUT06) K1(CM)
 :  : FIN
 :  : INI **>**CM£R1**Campagne
 :  : CMA  :  : FUN PG(REUT06) K1(CM£R1)
 :  : FIN
 :  : INI **>**CM£R2**Operazioni di marketing
 :  : CMA  :  : FUN PG(REUT06) K1(CM£R2)
 :  : FIN
 :  : INI **>**CM£R3**Lead
 :  : CMA  :  : FUN PG(REUT06) K1(CM£R3)
 :  : FIN
 :  : INI **>**CM£R4**Opportunità
 :  : CMA  :  : FUN PG(REUT06) K1(CM£R4)
 :  : FIN
 :  : INI **>**DO**Documenti (Testate)
 :  : CMA  :  : FUN PG(REUT06) K1(DO)
 :  : FIN
 :  : INI **>**DO£CM**Documenti CRM (Testate)
 :  : CMA  :  : FUN PG(REUT06) K1(DO£CM)
 :  : FIN
 :  : INI **>**DR**Documenti (Righe)
 :  : CMA  :  : FUN PG(REUT06) K1(DR)
 :  : FIN
 :  : INI **>**DR£CM**Documenti CRM (Righe)
 :  : CMA  :  : FUN PG(REUT06) K1(DR£CM)
 :  : FIN
 :  : INI **>**E3**Eventi
 :  : CMA  :  : FUN PG(REUT06) K1(E3)
 :  : FIN
 :  : INI **>**E3£C1**Eventi (Attvità CRM)
 :  : CMA  :  : FUN PG(REUT06) K1(E3£C1)
 :  : FIN

_7_Verifica-Inserimento autorizzazioni
Impostare le autorizzazioni per la gestione dei referenti
 :  : INI**Gestione autorizzazioni**
 :  : CMM CALL B£AUA0G PARM('RERN01')
 :  : FIN
Impostare le autorizzazioni per la gestione delle commesse
 :  : INI**Gestione autorizzazioni**
 :  : CMM CALL B£AUA0G PARM('BRCM01')
 :  : FIN
Impostare le autorizzazioni per la gestione degli eventi
 :  : INI**Gestione autorizzazioni**
 :  : CMM CALL B£AUA0G PARM('P5EV01')
 :  : FIN

_7_Creazione Account
Verificare la creazione del tipo ente Nominativo nelle tabelle BRE-BRZ (elemento NOM)
Impostare nella tabella BRE i tipi ente gestiti a nominativo
Impostare nella tabella B£2 il tipo ente nominativo
 :  : DEC T(ST) K(BRE)
 :  : DEC T(ST) K(BRZ)
 :  : DEC T(ST) K(BR2)
Impostare nel file SCP_SET lo script CN_£NO che contiene l'elenco dei campi del nominativo
Per la creazione degli account fare riferiemento al programma :  BRUT10A
 :  : INI Eseguire il programma di creazione automatica account
 :  : CMD C BRUT10A
 :  : FIN

_7_Creazione Referenti
Verficare il programma di conversione da BRESCO a REREFE :  REUT03A
 :  : INI Eseguire il programma di creazione automatica referenti
 :  : CMD C REUT03A
 :  : FIN

