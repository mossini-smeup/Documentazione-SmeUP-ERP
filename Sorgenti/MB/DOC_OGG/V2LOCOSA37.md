
## Obiettivo
Il modulo A37 è un'interfaccia che permette di inviare o ricevere dati di campo, pertanto è un costruttore che permette di interfacciare dispositivi, ricevendo dati in ingresso, richiamando pertanto programmi di exit, o inviando dati a dispositivi, pertanto impartendo comandi, in quest'ultimo caso utilizzando il provider tramite l'API specifica K10.

Il costruttore A37 è costituto da 5 entità : 
* una scheda :  LOA37
* una servizio base :  LOA37_SE
* script SCP_SET specifici Sme.UP o utente :  LOA37_xx
* programmi specifici Sme.UP o utente che vengono richiamati dai dispositivi :  LOA37_xx
* programmi specifici Sme.UP o utente che richiamano i dispositivi tramite l'API K10

## Funzionamento
Lo Sme.UP Provider alla sua attivazione, tramite il servizio LOA37_SE, interpreta gli script di interfaccia ai dispositivi.

Negli script vengono definite le istanze della classe SESUB.A37 nel formato xx.yyy.zzz : 
* xx è il gruppo, corrisponde al nome dello script LOA37_xx
* yyy è la sezione definita all'interno dello script
* zzz è la subsezione definita all'interno dello script

### Avvio : 
* Chiede la lista delle reti presenti al LOA37_SE.
* Per ogni rete, chiede lista delle SEZ presenti (tabella degli attributi del SEZ).
* Per ogni SEZ istanzia la classe in base a  :  : A37.CLSSEZ
* Per ogni sezione chiede la configurazione (lista di A37.CNFSEZ). Passa la conf alla classe nel metodo init(Smeup smeup)
* Per ogni sezione chiede la lista delle SUB
* Per ogni SUB chiede la sua configurazione (A37.SUBVAR o A37.SUBOPC)
* Per ogni SUB chiede la struttura del suo messaggio verso AS400

### Messaggio dal mondo esterno : 
* la periferica registra un evento ed il plugin che gestisce la SEZ deve generare un evento che svegli il framework.
* crea il messaggio usando la definizione della SUB che lo descrive
* controlla le variabili dell'msg e se non sono congruenti alla configurazione manda exception
* chiama il metodo smeup.sendMessage()
* Il framework deve mandare un msg all'as400
** se tutto ok chiama F(INT;LOA37_SE;SND.MSG) 1(SE;SUB.A37;xyz.ttt.kkk) INPUT(MSG(VAR1(VAL1) VAR2(VAL2)))
* loA37 prepara le schiere per la exit e chiama la exit
** se la exit torna errore, o il LOA37_SE non trova la exit, o altri errori, LOA37_SE genera messaggio xml

All'interno dello script vengono pertanto indicate le chiamate provenienti dai dispositivi,
oppure dal server verso i dispositivi, definendo le relative variabili di input o di output.

Il provider passa questi oggetti : 
l'oggetto 1 contiene SE SUB.A37, è la subsezione A37 di riferimento;
l'oggetto 4 contiene I3 1, il timestamp attuale;
l'oggetto 5 contiene V3 LSE, il provider;
l'oggetto 6 contiene NR, un numero positivo che indica la qualità del pacchetto.


### Messaggio dall'as400
* pgm crea un messaggio e chiama la /COPY £K10 e passando la SUB.A37
* la £K10 controlla che le variabili inviate siano dichiarate (nessuna in più, va bene in meno)
* la £K10 crea la fun  F(INT;JA_00_51;SND.OUT) 1(SE;GRU.A37;IN) 2(SE;SEZ.A37;IN.C01)  3(SE;SUB.A37;IN.C01.L00) INPUT(MSGOUT(var1(val1) var2(val2)))
* La copy logga le operazione effettuate (appoggiarsi al PHTRAC)
* chiama la £G64
** attende la risposta -> se timeout, errore
* il JA_00_51 cerca la classe (già istanziata!) in mappa . Chiama invoke(Message msg).
* compone la risposta in xml per la £K10
** La risposta è un XML di matrice, speculare a quello inviato dal loa37, cioè contenente un <Messaggio> (ok, errore),  e il valore della variabili di risposta (nel caso sia prevista)
* La £K10 , leggendo questo xml, lo traduce in una risposta per il programma rpg chiamante, quindi : 
** messaggio con esito
** eventuali variabili di risposta restituite in schiera

## Definizione nello script SCP_SET
Nel dettaglio questi sono i tag previsti nello script ed i relativi attributi principali : 


| 
| .COL Cod="COL001" Txt="Tag" LunAut="1" |
| ---|----|
| 
| .COL Cod="COL002" Txt="Descrizione" LunAut="1" |
| A37.SUPPRV|l'attributo Active='1' indica l'attivazione, se non impostato lo script viene ignorato, invece nell'attributo DtaQ è possibile impostare un provider specifico per lo script, quando non è indicato la risalita del provider da utilizzare avviene tramite l'API K16 (è comunque necessario che sia impostato l'attributo Active='1') |
| SEZ       |nell'attributo Cod viene indicata la sezione |
| A37.CLSSEZ|l'attributo Class indica la classe lato provider, Pgm il programma di exit lato server e Batch il tipo di esecuzione (vedi Note Batch per ulteriori informazioni sull'esecuzione) |
| A37.CNFSEZ|l'attributo Name indica una variabile di sezione e Value il relativo valore |
| A37.CNFPGM|l'attributo Name indica una variabile per il programma di exit e Value il relativo valore |
| SUB       |nell'attributo Cod viene indicata la subsezione |
| A37.SUBOPC|l'attributo Name indica la variabile prevista in comunicazioni OPC (sia input che output) |
| A37.SUBVAR|l'attributo Name indica la variabile prevista per il dispositivo (sia input che output) |
| A37.MSGVAR|l'attributo Name indica la variabile ricevuta dal dispositivo, è possibile definire anche un oggetto in Ogg e un nome per la ridenominazione della variabile in Alias. |
| 

E' infine possibile tramite il tag A37.VAR definire delle variabili di contesto G91 (&CO.xxx..).

Negli script è pertanto possibile definire la ricezione di informazioni da dispositivi, che effettuano il richiamo di un programma di exit, oppure definire l'invio di informzioni a dispositivi, tramite l'API K10.

### DO - ENDDO
Permettono di definire una parte di script ripetitiva per un certo oggetto (un ciclo su una lista ddi oggetti). La zona ripetiva inizia con DO finisce con un'istruzione ENDDO. Tutte le istruzioni incluse verrano ripetute per tutti gli oggetti che verrano ritornati dal programma o dalla lista indicata in questo tag. All'interno delle istruzioni potrò poi utilizzare il codice &CO.Cod per indicare dove sostiure il codice del singolo oggetto ottenuto dal loop.
Nel caso sia defnito un **programma esterno** di caricamento gli attributi sono : 
* Pgm :  programma che si occupa di ritornare gli oggetti per i quali le istruzioni incluse nel loop dovranno essere eseguite. Come programma di esempio vedere il programma **LOA11_01**, è stato il primo programma ad utilizzare la gestione di un loop, non è specifico per l'uso esclusivo nell'A11, pertanto è un programma di esempio distribuito che può essere usato così com'è anche nell'A37.
* Mod :  passo funzione/metodo del programma stesso.
* Par :  posso passare un serie di parametri al programma specifico.

Nel caso in cui voglia ottenere degli oggetti da una **lista** : 
* Lis :  codice della lista.
* Par :  parametro della lista.

### Utilizzo del programma LOA11_01 per il caricamento di un elenco di oggetti
**Caricamento tramite SQL**
Esempio : 
.    :  : DO Pgm="LOA11_01" Mod="SQL" Par="Sql(SELECT DISTINCT D6AGE1 FROM V5STAT0F ORDER BY D6AGE1) Tip(OG) Par() Cod(CNCOL)" Des="Agenti"

La modalità Mod="SQL" prevede che il parametro contenga un attributo Sql() contenente l'istruzione di selezione da eseguire per reperire i codici e degli attributi Tip() Par() e Cod() per indicare che tipo di oggetto viene restituito dalla select

**Caricamento delle istanze di un oggetto**
Esempio : 
.    :  : DO Pgm="LOA11_01" Mod="OGG" Par="Tip(OG) Par() Cod(TAV5D)"  Des="Tutti i Tipi Documento"

La modalità Mod="OGG" prevede che il parametro contenga degli attributi Tip() Par() e Cod() per indicare di che tipo di oggetto restituire le istanze.

**Caricamento di una matrice**
Esempio : 
     :  : DO Pgm="LOA11_01" Mod="SER" Par="F(EXB;LOA10_SE;ELE) 1(LI;CNCLI;*)" CExb="3" PExb="CNCLI" Des="Tutti i clienti da servizio"

La modalità Mod="SER" prevede che il parametro contenga una funzione di albero o di matrice sulle cui righe ciclare.
I parametri CExb e PExb indicano rispettivamente l'indice numerico della colonna sui cui valori di cella impostare il DO ed il tipo di istanza di tali valori

### Variabili istanziate

| Variabile | Valore |
| ---|----|
| &CO.Cod| Codice dell'oggetto istanziato dal ciclo |
| &CO.Tip| Tipo dell'oggetto istanziato dal ciclo |
| &CO.Par| Parametro dell'oggetto istanziato dal ciclo |
| &CO.Dec| Descrizione dell'oggetto istanziato dal ciclo |
| &CO.Wik| Codice dell'oggetto istanziato dal ciclo con carattere £ sostituito da X per compatibilità Wiki |
| &CO.F01|Nome di file pdf composto come segue RES001_[Cod].PDF |
| &CO.F02|Nome di file pdf composto come segue RES002_[Cod].PDF |
| &CO.PDF| .PDF (estensione da usare in concatenazione con altre variabili) |
| &CO.XLS| .XLS (estensione da usare in concatenazione con altre variabili) |
| &CO.HTML| .HTML (estensione da usare in concatenazione con altre variabili) |
| &CO.ZIP| .ZIP (estensione da usare in concatenazione con altre variabili) |
| 



### Note Batch
Il parametro Batch indica il tipo di esecuzione e come da wizard può avere i seguenti valori : 

| 
| .COL Cod="COL001" Txt="Valore" A="C" LunAut="1" |
| ---|----|
| 
| .COL Cod="COL002" Txt="Descrizione" A="C" LunAut="1" |
| 
| .COL Cod="COL003" Txt="Nota" LunAut="1" |
| (vuoto)|Modalità retrocompatibile|viene effettuata una chiamamta sincrona con le variabili in schiere predefinite. |
| 1      |Asincrono (batch via Q01)|in questa modalità di esecuzione batch tramite l'API Q01 sono disponibili il parametro Amb dove indicare l'ambiente Sme.UP specifico, se necessario eseguire la exit in un ambiente diverso da quello del provider, ed i parametri JobQ e JobQL per indicare l'eventuale nome della coda lavori e libreria, nel caso sia necessario definirne una specifica. |
| 2      |Sincrono (chiamata diretta)|viene effettuata una chiamamta diretta, utile per effettuare debug. |
| 


Per l'invio di messaggi a dispositivi si rimanda alla documentazione specifica dell'API K10 : 
- [TST Dati di Campo](Sorgenti/MB/DOC_OGG/P_TSTK10)
