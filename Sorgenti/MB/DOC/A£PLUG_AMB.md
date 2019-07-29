# Obiettivi
Indicare modalità std di lavoro per facilitare intercambiabilità  delle persone.
In questa sezione tratteremo la nomenclatura di : 

- _9_Librerie (std e personali)
- _9_Sorgenti e oggetti delle librerie personali


# Proposta ambiente e std operativi
## Librerie std
 Sono quelle fornite in fase di installazione
 :  : DEC T(OJ) P(*LIB) K(SMEDEV)
 :  : DEC T(OJ) P(*LIB) K(SMEUP_OBJ)
 :  : DEC T(OJ) P(*LIB) K(SMESTD)
 :  : DEC T(OJ) P(*LIB) K(SMESRC)
 :  : DEC T(OJ) P(*LIB) K(SMEMOD)
 :  : DEC T(OJ) P(*LIB) K(SMECON)

## Libreria personale
 In questa libreria (inizialmente fornita di file source vuoti) saranno  contenuti tutti gli
elementi (tranne i dati) che caratterizzeranno l'installazione specifica.

 Chiamarla SME_xxx dove xxx è il nome azienda
 Impostare la variabile "SIGAMB" mediante F15 - Personalizzazioni
 :  : DEC T(OJ) P(*LIB) K(SME_&SIGAMB)

In caso di installazioni con multisistemi informativi si può prevedere la libreria di
personalizzazioni di gruppo da creare con le stesse caratteristiche della lib. aziendale
con denominazione  SME_GRP (aggiungere un progressivo in caso numerico in caso di installazioni
con "multigruppi" es. SME_GRP001/002 ecc.)
 :  : DEC T(OJ) P(*LIB) K(SME_GRP)

## Libreria di "sistema"
 :  : DEC T(OJ) P(*LIB) K(SMESYS)
Dal rilascio V3R2 la libreria di sistema può essere gestita in due modi ("nomale" o "speciale") dal comando UP UT5.
**Si ricorda di inserire in questa libreria oltre ai file di sistema (tabelq0f) e ai programmi di
**gestione sistema (salvataggi e impostazioni di sistema) TUTTI GLI oggetti creati appositamente
**per l'applicazione come per esempio JOBQ,OUTQ e ovviamente le JOBD

## Libreria dati
 Chiamarla SMEDATxxx dove xxx è il nome azienda.
 Impostare la variabile "LICLDA" mediante F15 - Dati
  :  : DEC T(OJ) P(*LIB) K(SMEDAT&SIGAMB)
 Se non esiste ancora si può crearla duplicando la SMEUP_FIL, ottenendo così una libreria dati pre-configurata
 ..deve esistere
 :  : DEC T(OJ) P(*LIB) K(SMEUP_FIL)
In caso di installazioni "multisistemi informativi" creare la libreria SMEDATGRP per contenere i
file di gruppo (es. TABELG0F)

## File sorgenti forniti e, quindi, suggeriti nelle libreria SME_&SIGAMB
 :  : DEC T(OJ) P(*FILE) K(DOC_PER) LI(SME_&SIGAMB)
 :  : DEC T(OJ) P(*FILE) K(QILEGEN) LI(SME_&SIGAMB)
 :  : DEC T(OJ) P(*FILE) K(SCP_AZI) LI(SME_&SIGAMB)
 :  : DEC T(OJ) P(*FILE) K(SCP_BCD) LI(SME_&SIGAMB)
 :  : DEC T(OJ) P(*FILE) K(SCP_CFG) LI(SME_&SIGAMB)
 :  : DEC T(OJ) P(*FILE) K(SCP_CLO) LI(SME_&SIGAMB)
 :  : DEC T(OJ) P(*FILE) K(SCP_FLU) LI(SME_&SIGAMB)
 :  : DEC T(OJ) P(*FILE) K(SCP_G53) LI(SME_&SIGAMB)
 :  : DEC T(OJ) P(*FILE) K(SCP_MAP) LI(SME_&SIGAMB)
 :  : DEC T(OJ) P(*FILE) K(SCP_MNU) LI(SME_&SIGAMB)
 :  : DEC T(OJ) P(*FILE) K(SCP_NAV) LI(SME_&SIGAMB)
 :  : DEC T(OJ) P(*FILE) K(SCP_PDF) LI(SME_&SIGAMB)
 :  : DEC T(OJ) P(*FILE) K(SCP_QRY) LI(SME_&SIGAMB)
 :  : DEC T(OJ) P(*FILE) K(SCP_SCH) LI(SME_&SIGAMB)
 :  : DEC T(OJ) P(*FILE) K(SCP_SET) LI(SME_&SIGAMB)
 :  : DEC T(OJ) P(*FILE) K(SCP_SPL) LI(SME_&SIGAMB)
 :  : DEC T(OJ) P(*FILE) K(SCP_WFA) LI(SME_&SIGAMB)
 :  : DEC T(OJ) P(*FILE) K(SCP_XML) LI(SME_&SIGAMB)
 :  : DEC T(OJ) P(*FILE) K(SMEQSM)  LI(SME_&SIGAMB)
 :  : DEC T(OJ) P(*FILE) K(SMEUP)   LI(SME_&SIGAMB)
 :  : DEC T(OJ) P(*FILE) K(SRC)     LI(SME_&SIGAMB)
 :  : DEC T(OJ) P(*FILE) K(SRC_X1)  LI(SME_&SIGAMB)
 :  : DEC T(OJ) P(*FILE) K(SRCCON)  LI(SME_&SIGAMB)
 :  : DEC T(OJ) P(*FILE) K(SRCDB)   LI(SME_&SIGAMB)
 :  : DEC T(OJ) P(*FILE) K(SRCUTI)  LI(SME_&SIGAMB)
 :  : DEC T(OJ) P(*FILE) K(SRCWK)   LI(SME_&SIGAMB)


# Nomenclatura suggerita nei file sorgenti della libreria SME_&SIGAMB

## QILEGEN
In questo file ci vanno le /COPY personali ed le eventuali standard.
**SI SCONSIGLIA VIVAMENE DI MODIFICARE /COPY standard, siano esse tabelle (utilizzare il TTUSER o
**la gestione parametri) o routine standard

Approfittiamo per ricordare che le tabelle personali dovranno iniziare con la lettera 'X' quindi
le /copy relative saranno £TABXnnDS, mentre le routine personali saranno £Xnn (dove i pgm di
gestione X£XnnG) e le relative DS o schiere saranno £XnnDS o £XnnE (si consiglia di non utilizzare
il suffisso *E ma sempre e solo il *DS)

## SMEUP
In questo file devono essere messi i sorgenti STANDARD (per standard si intende sorgenti forniti
dall'applicazione e quindi presenti nei file della SMEDEV e/o della SMESRC)
**Le Exit dei programmi standard NON vanno messe in questo file

_1_Ricordando che la modifica di un sorgente standard NON DEVE ESSERE FATTO se non in casi estremi
_1_e concordata con lo sviluppo, in questo caso SI DEVE segnare all'interno dei sorgenti modificati : 
  In testa la data,l'autore della modifica e una descrizione sommaria della stessa
  Prima e dopo le specifiche modificate la sigla di INIZIO (I.MOD.XXX) e FINE (F.MOD.XXX)
  pesonalizzazione dove XXX è la sigla della azienda

**Questo è utile e necessario per installazioni di nuovi rilasci SME.up

## SRC
In questo file devono essere messi tutti i sorgenti creati per l'applicazione e non forniti da SMEUP
Si considerano anche le exit (unica eccezione di sorgente presenti nei file standard ma forniti solo
come esempio).


| 
| .COL Txt="." A="L" |
| ---|----|
| 
| .COL Txt="." A="L" |
| 
| .COL Txt="." LunAut="1" A="L" |
| - Pgm RPGLE|**XAPnnn**|AP = Sigla applicaz.riferimento |
| - Pgm CLLE|**XAPnnnC**|(es. V5) |
| - File DSPF|**XAPnnnV**| |
| - File PRTF|**XAPnnnP**| |
| - --|--|-- |
| - TST RPGLE|**TSTXyy**|Test "API" personali (QILEGEN) |
| - TST DSPF|**TSTXyy0V**|Dove Xyy deriva dalla /copy £Xyy |
| - --|--|-- |
| - Pgm RPGLE|**XUTnnn**|Utility **non** una tantum |
| - Pgm CLLE|**XUTnnnC**| |
| - File DSPF|**XUTnnnV**| |
| - File PRTF|**XUTnnnP**| |
| 


Caso particolare :  Exit previste da Sme.up

In caso di suffissi si segue l'indicazione specifica in help tabella (es. V5COL0_x dove x è il suffisso indicato in tabella)

Nel caso dei visualizzatori (gruppo £VS) si riprende il nome del programma richiamante (esempio per V5TDOC0F V5DO01Dnn e V5DO01DnnV per il relativo DSPF)

Nel caso siano programmi specificati in tabelle oppure in routine standard crearle con nome Xyyy_nn (dove yyy è la tabella, esempio M5E, oppure la routine , esempio G04 per la routine delle spese)

In tutti gli altri casi non specificati crearle con il prefisso del nome del programma che le lancia (come nel esempio dei visualizzatori)


## SRCDB
In questo file fanno inseriti i sorgenti relativo ai file creati, si SCONSIGLIA VIVAMENTE di modificare file standard.
I file personali inizieranno con la lettera X mentre i logici creati su file fisici standard avranno la 'X' finale al posto della 'L' per i logici e la lettera 'Y' al posto della lettera 'J' per i Join. Comen nel esempio sotto riportato



| 
| .COL Txt="." A="L" |
| ---|----|
| 
| .COL Txt="." A="L" |
| 
| .COL Txt="." LunAut="1" A="L" |
| - File fisici personali|**Xyyyyy0F**|yyyyy  = libero |
| - File logici personali|**Xyyyyy1L/2L/../nL**|yyyyy  = libero |
| - File logici su file fisici stanrd|**yyyyyy1X/2X/../nX**|yyyyyy = prefisso file std Sme.up |
| - File JOINi su file fisici stanrd|**yyyyyy1J/2J/../nJ**|yyyyyy = prefisso file std Sme.up |
| 


## (SRCUTI)
In questo file vanno messi i sorgenti relativi a programmi di utility creati appositamente. la nomenclatura come sotto riportata : 


| 
| .COL Txt="." A="L" |
| ---|----|
| 
| .COL Txt="." A="L" |
| 
| .COL Txt="." LunAut="1" A="L" |
| - Pgm RPGLE|**XXXnnn**|nnn    = progressivo |
| - Pgm CLLE|**XXXnnnCL**| |
| - File PRTF|**XXXnnnP**| |
| - File DSPF|**XXXnnnV**| |
| 


## File sorgente suggerito nelle libreria SMESYS
 :  : DEC T(OJ) P(*FILE) K(SRC_SYS) LI(SMESYS)

## Nomenclature suggerita nel file sorgente della SMESYS
   **(SRC)**

| 
| .COL Txt="." A="L" |
| ---|----|
| 
| .COL Txt="." A="L" |
| 
| .COL Txt="." LunAut="1" A="L" |
| - Pgm RPGLE|**XSYnnn**|nnn    = progressivo |
| - Pgm CLLE|**XSYnnnCL**| |
| - File PRTF|**XSYnnnP**| |
| - File DSPF|**XSYnnnV**| |
| 


## Membri sorgenti che dovrebbero esistere
 :  : DEC T(MB) P(DOC_PER) K(X1) LI(SME_&SIGAMB) I(_9_Documentazione specifica      >>)!!!!!

# Impostazione lista di librerie ambiente

## Lista libreria consigliata, un appunto speciale lo faremo successivamente per quando riguarda le, eventuali librerie di gruppo.

SMEDAT&SIGAMB
SMEDATGRP
SME_&SIGAMB
SME_GRP
SMEDEV
SMEUP_OBJ
SMESTD

Note : 
- La libreria SMESRC non è necessario che si trovi nella lista di librerie.
- La SMESTD non sarebbe necessaria per la libl degli utenti ma nell'ottica di ottimizzare gli ambienti si suggerisce di inserirla


## "MULTISISTEMI INFORMATIVI" (MSI) e relative librerie di gruppo.

In caso di MSI sorge il grosso problema di come impostare le librerie di gruppo e quali dati rendere comuni e dove metterli.

Le librerie necessarie all'operazione sono 2 : 

La SME_GRP che conterrà tutti i programmi, e i relativi sorgenti, comuni.
La SMEDATGRP che conterrà tutti i file comuni

Nella SME_GRP tendenzialmente ci vanno TUTTI i programmi e le exit fatte, le librerie specifiche servono solo per le eccezioni aziendali, si ricorda che queste devono essere il minor numero possibile e che normalmente è meglio cercare di inserire nel pgm standard con le eccezioni per azienda (utilizzando il campo ££B£2A).

Nella SMEDATGRP ci vanno i file. Il problema normalmente è quello di capire quali dati mettere in comune tra le varie aziende (e implicitamente tra ambienti reali e ambienti di TEST).
tra questi un file è fornito nella smeup_fil standard ed è TABELG0F.
In questo file andranno le tabelle comuni, per decidere quali tabelle rendere comuni serve considerare se gli elementi andranno bene per tutti. Nel dubbio si consiglia di condividerne il maggior numero possibile in quanto bisogna tener conto del motto : 
"separare è complicato, Unire di più"

Per gli altri archivi si consiglia di analizzarli tutti, questi indicati sono i più comuni : 

TABELG0F (già detto)
TABELA0F (menù smeup)
AUTOAP0F (le autorizzazioni)
B£SLOT0F (Definizione degli OAV)
BRCAMB (cambi valute)
DATI CONTABILI (citeremo a parte)

### Considerazione sull'ordine dei dati di gruppo

In realtà l'ordine "dati aziendali"/"dati di gruppo" è indifferente anche perchè si consiglia di NON tenere gli archivi doppi ma di spostarli.
L'ordine scelto si deve alla possibilità, sconsigliata, di avere delle eccezioni (esempio 10 aziende con la stessa anagrafica articoli e una NO).



## contabilità comune

In MSI si consiglia di mettere tutti i file, anche le tabelle con l'azienda come sottesettore, contabili nella libreria comune (bilanci consolidati unico utente contabile).




