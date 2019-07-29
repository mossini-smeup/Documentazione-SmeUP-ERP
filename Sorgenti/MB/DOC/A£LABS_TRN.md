 :  : PRO Cod(A02) Txt(Esercizi) STAT(00) RESP(VERFRA)

 :  : ATT Cod(001) Txt(Come generare dati prototipo) STAT(10) RESP(VERFRA)
//--***************************************************************
//--  CREAZIONE DI UN PROTOTIPO                       *
//--***************************************************************

01. Cosa sono i prototipi in Sme.UP?
//-- ********************** CAPITOLO 1 **********************

In Sme.Up esiste il concetto di dato prototipo, cioè creare dei dati fittizzi che possiamo utilizzare per popolare i nostri componenti di scheda.

Si rimanda alla documentazione ufficiale dei prototipi (Funzioni dell'esercizio).

 :  : DEC T(J1) P(FUN) D(A. Documentazione PROTOTIPO) K(F(EXD;*SCO;) 1(MB;DOC;A£LABS_PRO) 2(OJ;*FILE;DOC))

02. Dove creare i dati prototipo
//-- ********************** CAPITOLO 2 **********************

Per creare dei dati prototipo abbiamo bisogno di un membro SCP_SET.
Solitamente questi membri vengono creati seguendo la nomenclatura [NOME]_PRO.
Sovente si sceglie però di copiare i membri da altre librerie per inserirli nella propria libreria; vediamo come farlo : 
    1- Tramite la lente di ingrandimento dello spotlight cerchiamo il membro MB -> SCP_SET -> A£LABS_PRO (visibile anche in Funzioni dell'esercizio)
    2- Nel menu laterale di sinistra scegliere GESTIONE -> COPIA
    3- Nel campo "libreria" indicare la propria libreria personale (che solitamente è composta da "W_<nomeutente>", nel mio caso è W_VERFRA dove VERFRA è il mio nome utente)
    4- Nel campo "membro" inserire il nome che si vuole dare allo script che andrà a salvarsi nella nostra libreria (in questo caso inseriamo "PROVA_PRO")
    5- Il campo "tipo sorgente" indica al server AS la tipologia del membro che andremo a creare. Inseriamo quindi la dicitura "PRO" che indica un membro di tipo prototipo.
    6- Nel campo "testo" inseriamo una didascalia di massimo 50 caratteri per indicare cosa conterrà il sorgente, in questo caso inseriamo "Settaggio di prova"
    7- Confermiamo la copia del file

03. Come creare i dati prototipi
//-- ********************** CAPITOLO 3 **********************

Abbiamo due modi per generare dati prototipo, Randomici o Statici. Inizaimo a vedere i secondi : 

03.A.Prototipi statici

Di seguito vediamo uno script che genererà dati protoipo statici

(Si noti che per il codice sottostante necessita dei due punti iniziali ad ogni istruzione per funzionare)
 TBL Nam="BOX_001"
   COL Cod="A" Txt="Immagine Persona" Lun="10" IO="O" Ogg="J4IMG"
   COL Cod="B" Txt="Codice" Lun="6" IO="O" Ogg="CNCOL"
   COL Cod="C" Txt="Nome" Lun="30" IO="O" Ogg=""
   COL Cod="D" Txt="Matricola" Lun="5" IO="O" Ogg="NR"
   COL Cod="STYLE" Txt="Style" Lun="5" IO="H" Ogg="**"
     DAT Fld="CN;COL;SANCOS_$_PIPE_$_SANCOS_$_PIPE_$_Mauro Sanfilippo_$_PIPE_$_3500_$_PIPE_$_WEB01"
     DAT Fld="CN;COL;PARFRA_$_PIPE_$_PARFRA_$_PIPE_$_Franco Parodi_$_PIPE_$_4500_$_PIPE_$_WEB02"
     DAT Fld="CN;COL;FIOGIA_$_PIPE_$_FIOGIA_$_PIPE_$_Gianluca Fioletti_$_PIPE_$_1500_$_PIPE_$_WEB03"

in Tbl abbiamo il nome univoco che avrà la nostra sezione, e che utilizzeremo per andare a richiamre lo script dalla nostra scheda.
Tramite la dicitura "COL" andiamo ad indicare quante colonne ci aspettiamo, e qui specifichiamo un codice univoco e altri paramentri come i caratteri massimi della cella oppure l'oggetto di Sme.UP che essa conterrà.
In ultima battuta andiamo a valorizzare le nostre colonne inserendo dei dati cablati attraverso la dicitura DAT Fld="<campi da inserire nelle colonne>".
Ricordo che i campi vanno divisi dal carattere pipe "|", e per ogni colonna dobbiamo valorizzare la cella (anche se la colonna è vuota, gli verrà riservato uno spazio bianco delimitato da due pipe).

03.B. Prototipi randomici
I prototipi randomici servono per generare dei valori in modo casuale da inserire all'interno di una tabella.
Per fare questo basta inserire il campo Mod="RDN" e il numero di ripetizioni Rip="<numero di ripetizioni>".

(Si noti che per il codice sottostante necessita dei due punti iniziali ad ogni istruzione per funzionare)
 TBL Nam="BOX_002" Tit="Collaboratori casuali" Mod="RND" Rip="10"
   COL Cod="STR001" Txt="Collaboratore" Tip="" Lun="50" IO="B" Ogg="CNCOL" Dpy="" Aut="" Fill=""

Così compilato, questo esempio ci caricherà 10 collaboratori casuali (definiti nel parametro Ogg="CNCOL").

04.Come importare questi dati in una scheda
//-- ********************** CAPITOLO 4 **********************

Ora sposticiamoci in membro SCP_SCH, in cui vogliamo importare i dati che abbiamo appena editato in una matrice.
Per prima cosa andiamo a impostare due sezioni contenti entrambi una matrice : 

(Si noti che per il codice sottostante necessita dei due punti iniziali ad ogni istruzione per funzionare)
 G.SEZ Pos(A)
  G.SUB.MAT Tit="Dati Cablati"
  G.SET.MAT Load="I"
 G.SEZ Pos(B)
  G.SUB.MAT Tit="Dati Randomici"
  G.SET.MAT Load="I"

Ora dovremo utilizzare una FUN che carichi i nostri dati proprio dal membro dell'SCP_SET che abbiamo creato e riempia la nostra matrice attraverso l'utilizzo del servizio B£SER_46.

 F(EXB;B£SER_46;WRK.SCP) 1(MB;SCP_SET;<NOME_MEMBRO>) 2(;;<NOME_SEZIONE>)

Applichiamo questa FUN al nostro esempio, differenziando ovviamente il nome della sezione per le due matrici!
Ovviamente questo perchè vogliamo che vengano riempite in maniera differente, una con i dati cablati, mentre la seconda con i dati randomici : 


 G.SEZ Pos(A)
  G.SUB.MAT Tit="Dati Cablati"
  G.SET.MAT Load="I"
    D.FUN.STD F(EXB;B£SER_46;WRK.SCP) 1(MB;SCP_SET;PROVA_PRO) 2(;;BOX_001)
 G.SEZ Pos(B)
  G.SUB.MAT Tit="Dati Randomici"
  G.SET.MAT Load="I"
    D.FUN.STD F(EXB;B£SER_46;WRK.SCP) 1(MB;SCP_SET;PROVA_PRO) 2(;;BOX_002)


05. Vediamo un piccolo esercizio per prendere confidenza con qesto argomento
//-- ********************** CAPITOLO 5 **********************

1- Editare un membro SCP_SET con dei dati fittizzi che verranno uasti per valorizzare un box
2- Creare in un membro SCP_SCH una sezione BOX e tramite Fun passare i dati contenuti nel membro SCP_SET

06. Soluzione esercizio

Di seguito un esempio di script che possiamo scrivere all'interno di un SCP_SET : 

(Si noti che per il codice sottostante necessita dei due punti iniziali ad ogni istruzione per funzionare)
 TBL Nam="ESE_01" Tit="script  di prova"
  COL Cod="COL01" Txt="Colonna contenente immagini di collaboratori" Lun="50" IO="B" Ogg="J4IMG"
  COL Cod="COL02" Txt="Colonna contente un oggetto generico" Lun="100" IO="B" Ogg=""
  COL Cod="COL03" Txt="Colonna contente province" Lun="20" IO="B" Ogg="TAV§P"
    Dat Fld="CN;COL;SCIMAM_$_PIPE_$_Adro_$_PIPE_$_Brescia"
    Dat Fld="CN;COL;VERFRA_$_PIPE_$_Marcheno_$_PIPE_$_Brescia"
    Dat Fld="CN;COL;FEDROB_$_PIPE_$_Desenzano_$_PIPE_$_Brescia"
    Dat Fld="CN;COL;BERNIC_$_PIPE_$_Vimodrone_$_PIPE_$_Milano"

Ora editiamo il membro SCP_SCH per importare in un box i dati appena scritti : 

 G.SEZ Pos(1)
  G.SUB.BOX Tit="*NONE"
   D.FUN.STD F(EXB;B£SER_46;WRK.SCP) 1(MB;SCP_SET;PROVA_PRO) 2(;;ESE_01)



 :  : ATT Cod(002) Txt(I costruttori in SmeUP) STAT(10) RESP(VERFRA)

01.Cosa sono i costruttori in SmeUP?
//-- ********************** CAPITOLO 1 **********************

I costruttori in SmeUP sono un insieme di programmi che gestiscono tutti gli aspetti di un singolo ambito, come ad esempio la raccolta dati di campo.
Tutti i costruttori di SmeUP sono riconoscibili dalla nomenclatura LOA[XX], dove XX è un numero.


02.Arrivare sulla scheda di un costruttore
//-- ********************** CAPITOLO 2 **********************

Ogni costruttore ha una sua scheda di presentazione

02.A. Scheda del costruttore
Si provi a andare ad interrograre la scheda di un costruttore

02.B.Soluzione
Per arrivare alla scheda di un costruttore, dallo spotlight premiamo la lente di ingrandimento
e digitiamo T[V2] P[LOCOS] K[!]
Tramite il ! ci facciamo restituire tutta la lista dei costruttori. Selezioniamo quello che ci interessa e confermiamo.
da qui possiamo, ad esempio, accedere alla scheda di documentazione del costruttore.



 :  : ATT Cod(003) Txt(Sistema e Ambienti) STAT(10) RESP(VERFRA)

01.Cosa si intende per sistema in SmeUP
//-- ********************** CAPITOLO 1 **********************

Per sistema in SmeUP si intende su quale AS400 stiamo lavorando, al momento in laboratorio si utilizzano due sistemi, uno di sviluppo SRVLAB01.SMEUP.COM e uno di amministrazione SRVAMM.SMEUP.COM

02.Cosa si intende per ambiente in smeUP
//-- ********************** CAPITOLO 2 **********************

E' un ambiente di sviluppo isolato da tutti gli altri. Esistono ambienti di sviluppo e test, e ne esistono di produzione.

03.Verificare l'ambiente e il sistema di connessione a LoocUP
//-- ********************** CAPITOLO 3 **********************

In smeUp è possibile, una volta loggati conoscere i propri dati di connessione.

03.A.Esercizio
Si provi ad interrograre la scheda che restituisce questi dati di connessione

03.B.Soluzione
Una volta effettuata la connessione abbiamo due strade per vedere i nostri dati di connessione : 

03.B.1.Da UP!
pemere sul bottone UP --> Help --> About, premere su "Informazioni di sistema"
a questo punto ci verrà restituita una matrice cun tutta una serie di paramentri di connessione

03.B.2.Da Header di LoocUP
in alto a destra premere sul nome dell'ambiente in cui ci troviamo, ci apparirà una piccola finestra con alcune informazioni di connessione.









