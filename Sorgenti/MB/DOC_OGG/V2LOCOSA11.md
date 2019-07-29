# Obiettivo

L'obiettivo dei flussi è la possibilità di eseguire alcune funzioni (A o F) parametrizzando il flusso tramite uno script specifico. Per l'esecuzione dei flussi sono previste una serie di funzionalità tra cui : 
* Generare una matrice di valori e successivamente produrre un documento PDF o Excel derivato da quella matrice
* Eseguire uno o più funzioni che siano incluse in un'iterazione. Ad esempio determino una serie di oggetti derivati da una query SQL e per ogni oggetto trovato eseguo le funzioni definite.
* Eseguire alcune funzioni che dipendano da alcuni parametri impostati in precedenza :  ad esempio chiamo un configuratore che imposta una data e un articolo e successivamente posso usare tali informazioni nei passi del flusso
* Eseguire alcuni passi in base a delle condizioni IF

# Gestione flussi
## Note operative
I flussi gestiti dal costruttore **LOA11** vengono parametrizzati tramite gli script del file **SCP_SET** che hanno come prefisso del nome LOA11_*.
Solo alcuni tag possono essere applicati a membri utilizzati per i flussi, perchè il contenuto dei membri del file SCP_SET è variegato. Nello specifico si posso utilizzare : 
* **SEZ** :  definisce un gruppo di flussi
* **SUB** :  definisce un flusso all'interno del gruppo
* **FLU** :  definisce un'azione eseguita dal flusso
* **DO** :  definisce un ciclo DO di azioni FLU
* **IF** :  definisce una condizione sull'esecuzioni di azioni FLU

La scansione dell'SCP_SET tramilte il LOA11 permette l'utilizzo delle variabilli della G91 con tutte le varie funzionalità (es. posso indicare gli OAV di un variabile).
Dalla scheda **LOA11** è possibile analizzare i flussi implementati in questo modo.


## Documentazione dei tag
### SUB
Definisce l'inizio di un flusso. Un flusso corrisponde alla tripla COD SCRIPT-SEZIONE-SOTTOSEZIONE. Ad esempio se abbiamo uno scrip LOA11_TT al cui interno abbiamo una sezione (attributo SEZ) A01 e due sottosezioni (identificate dall'attributo SUB) B01 e B02 è possibile identificare i due seguenti flussi : 
* TT.A01.B01
* TT.A01.B02

Questa nomenclatura permette di avere un riferimento preciso al flusso richiamabile nella scheda LOA11 ed esternamente in una nostra scheda. E' possibile inoltre referenziare un flusso B all'interno di un flusso A tramite i flussi dinamici. Si veda di seguito al paragrafo **Flussi dinamici  per una descrizione dettagliata sul loro utilizzo.
Il tag SUB permette di caricare delle configurazioni e delle variabili utilizzabili all'interno del flusso. Si veda al pragrafo **Configurazione flussi e inizializzazione variabili**

### FLU.SET
E' il tag che permette di impostare  alcuni parametri di esecuzione del flusso. Nell'elenco dei flussi dovrebbe essere il primo tag di ogni flusso in quanto va a definire il setup che verrà applicato allo stesso. Il componente FLU assume di default alcuni parametri.
Tra i parametri previsti dal flusso è possibile impostare che il flusso sia **statico** o **dinamico**. Un flusso statico carica inizialmente tutti i passi e sostituisce tutte le variabili al caricamento del flusso. Il flusso dinamico richiede il passo successivo dopo l'esecuzione di ogni passo
### DO - ENDDO
Permettono di definire un zona di flusso ripetitiva per un certo oggetto (un ciclo su una lista di oggetti). La zona ripetiva inizia con DO finisce con un'istruzione ENDDO. Tutte le istruzioni incluse verrrano ripetute per tutti gli oggetti che verrano ritornati dal programma o dalla lista indicata in questo tag. All'interno delle istruzioni potrò poi utilizzare il codice &CO.Cod per indicare dove sostiure il codice del singolo oggetto ottenuto dal loop.
Nel caso sia defnito un **programma esterno** di caricamento gli attributi sono : 
* Pgm :  programma che si occupa di ritornare gli oggetti per i quali le istruzioni incluse nel loop dovranno essere eseguite. Come programma di esempio vedere il programma **LOA11_01**.
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


E' inoltre possibile utlizzare i parametri passati alla chiamata del LOA11_SE riferendosi ad esse con variabili &OG. per gli oggetti, &PA. per il Parametro e &IN. per l'Input.

### FLU.OVS
Permette di scrivere nella SME.LDA (£G00) l'override del setup di un particolare componente, che verrà poi recuperato nella prima esecuzione del componente dal B£GPE3.
* Tip :  indico il setup (es. SET.MAT, FRM.SET, FRM.REP)
* Nam :  indico opzionalmente il nome di un modello che posso utilizzare per l'override (normalmente A01). I modelli sono contenuti nello script SCP_SCH.J3_SET_STD o SCP_SCH.J3_SET_USR
* Ovr :  posso indicare opzionalmente i valori dei singoli attributi di setup che voglio utilizzare
### FLU.FUN
Permette di eseguire delle funzioni di tipo F o  A
* Fun :  metto in modo esplicito la funzione (A o F) da lanciare
* Des :  indica la descrizione del passo di flusso (che posso vedere nella documentazione del flusso)
### FLU.MNU
Permette di eseguire delle funzioni di tipo F che devono obbligatoriamente chiamare una scheda.
* Fun :  metto in modo esplicito la funzione da lanciare
* Des :  indica la descrizione del passo di flusso
* Aut :  Livello di autorizzazione alla funzione
### FLU.AZA
Permette di lanciare funzioni di tipo A(EMU specifiche svolte dal pgm LOA11_AZ (per le funzioni disponibili vedere il parametro Modo).
### FLU.AZF
Permette di lanciare  delle funzioni di tipo F(FBK specifiche svolte dal pgm LOA11_AZ (per le funzioni disponibili vedere il parametro Modo)
### IF/ELSE/ENDIF
Tramite questi tag è possibile condizionare l'esecuzione dei passi di flusso. La sintassi è quella prevista dalla /COPY G91.
### FLU.VAR
Tramite questo tag è possibile istanziare delle variabili nel flusso.
Le modalità possibili sono due : 
* **mod : VAR.PAR**- Per istanziare delle variabili nello script. Nell'attributo del tag **Par_n_ vanno inserire delle variabili del tipo X1(AX) X2(A1) ... richiamabili nello script tramite &CO.X1 &CO.X2. Esempio >FLU.VAR Mod="VAR.PAR" Par="X1(AX) X2(A1)"
* **mod : VAR.PGM**- Per istanziare delle variabili richiamando un programma di exit (tramite il parametro **Par**). Nel programma richiamato tramite la /copy G91 vengono create le variabili da utilizzare poi successivamente.  I nomi delle variabili devono essere sempre nella forma &CO.XXXX. Esempio >FLU.VAR Mod="VAR.PGM" Par="Pgm(LOA11_X1) Fun(SCE) Met(AGE)" dove il programma LOA11_X1 verrà richiamato con 3 parametri (funzione(SCE)/metodo(AGE)/contesto(passato implicitamente LOA11)).

## Configurazione flussi e inizializzazione variabili
Tramite l'attributo **CCfg** presente nel tag **SUB** è possibile caricare all'avvio del flusso un setup. Un esempio è CCfg="LOA11/A" che carica la sezione A dello script G30 chiamato LOA11 presente nel file SCP_CFG.
Attenzione : 
* la configurazione viene caricato con l'attributo *ENV  e non *JOB. Riferirsi alla documentazione del G30 per maggiori dettagli
* la configurazione G30 non viene mostrata all'utente ma viene letta dal file B£MEDE0F dove deve essere stata memorizzata in precedenza. Per modificare la configurazione è necessario richiamare il componente G30 esternamente al flusso con il nome della configurazione. Esempio di chiamata di modifica allla configurazione LOA11/A è A(CFCF01X;GES;02) 1(CF;S-LOA11/A;*ENV)

## Flussi dinamici
I flussi dinamici permettono di eseguire un flusso che durante l'esecuzione dei suoi passi può cambiare le condizioni di esecuzione.
Il flusso dopo essere stato eseguito richiama la funzione impostata nell'attributo del flusso **StepFun**questa deve essere in grado di restituire i passi sucessivi del flusso da eseguire. Se non vengono ritornati passi il flusso termina.
TODO 02/09/10 - Verificare funzionamento e completare documentazione.


## Costruzione di un flusso a partire da funzioni ricevute nell'INPUT

Chiamata :  >F(FLU;LOA11_SE;FLU.COS)

### Parametri passati nell'INPUT

| Tag | Descrizione |
| ---|----|
| NAM() | Nome del flusso |
| DES() | Descrizione del flusso |
| FUNnn() | Fino a 5 funzioni da eseguire come passi del flusso |
| 



# TODO 02/09/10
* Documentare gestione dello script (rinviare a L_EDT_SET)
* Verificare autorizzazioni e utilizzo
* Chiamata diretta del flusso documentare
* Dettaglio delle funzioni richiamate e maggiori esempi
* Utilizzo dei Report e applicazione dei setup J3
* Analisi di pareto
* Analisi tabellare
* Cruscotto di controllo migliorarlo e documentarne gli utilizzi
* Set'n Play  e log su server
