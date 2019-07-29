## Obiettivo
Generalizzare la costruzione di testi.

## Autorizzazioni
A livello di USRLVL le funzioni disponibili hanno autorizzazione annegate nel source del servizio : 
SFIN____________________Aut Usr
* Gestione del testo_________01
* Gestione della struttura_____01
* Testo in matrice
* Testo grafico
* Testo non formattato
* Imposta variabili___________01
* Documentazione specifica__01
* Set'n Play_______________ 02

e vengono gestite da SmeUp : 
 -  Classe :  USRLVL
 -  Utente :  [utente/gruppo]
 -  Funzione :  LOA19_SE

Per quanto riguarda la gestione delle autorizzazioni per singolo paragrafo invece, la classe è la "LO.EXD"
gestita come segue : 
 - Classe :  LO.EXD
 - Utente :  [utente/gruppo]
 - Funzione :  [codice lettera]


## Testo
Il testo può essere recuperato da diverse forme : 
* Parametro interno
* Nota oggetto
* Nota specifica
* Documentazione oggetto
* Documentazione specifica
* Descrizione in lingua
Il testo può essere definito in varie lingue ed è possibile visualizzare solo il testo nella lingua desiderata andando a settare la specifica variabile

## Struttura Script
L'installatore deve definire la propria struttura di recupero dei testi nello script che deve risiedere nel sorgente**SCP_SET**.
Il nome dello script deve essere composto da una parte fissa (LOA19_) e una parte variabile che indica il gruppo sotto cui riunire una serie di testi.
All'interno dello script devono essere specificati almeno una sezione, una sottosezione e un paragrafo per visualizzare un testo.
(Lo script è composto da due parti, la prima carattere e la seconda numerica, permettendo così la generazione di script meno corposi e semplici da mantenere.
La parte carattere non deve eccedere gli 8 caratteri, mentre la parte numerica deve essere lunga 2.)

 ### Tag dello script
 Elenco delle tag e del loro significato

 
| Tag|Significato |
| ---|----|
| SEZ|Inizio di una sezione |
| SUB|Inizio di una sottosezione |
| A19.SET|Setup del testo |
| A19.PAR|Metoto di ricerca del paragrafo |
| A19.MNU|Funzione di menù |
| A19.VAR|Impostazione variabile |
| A19.PAF|Funzione richiesta parametri per simulazione |
|  


Ora vediamo in dettaglio gli attributi di ogni tag

**SEZ**Sezione

| Attributo|Significato|Descrizione |
| ---|----|----|
| Cod|Codice|Ragguppa per omogeneità i modelli di testo |
| Txt|Descrizione|Significato del gruppo |
| 


**SUB**Sotto sezione

| Attributo|Significato|Descrizione |
| ---|----|----|
| Cod|Codice|Identifica in maniera univoca il modello di testo |
| Txt|Descrizione|Significato del modello |
| 


**A19.SET**Setup del testo
Permette di impostare il modello del tetso.


| Attributo|Significato|Descrizione |
| ---|----|----|
| Con|Contesto|Identifica il contesto da cui recuperare le variabili |
| Met|Metodo|Metodo con cui risolvere la lingua del testo |
| T1|Tipo oggetto|Tipo oggetto utilizzato per risolvere la lingua del testo |
| K1|Oggetto|Oggetto utilizzato per risolvere la lingua del testo |
| Var|Variabile|Variabile che contiene la lingua del testo |
| 


**A19.MNU**Funzione del menu
Permette di aggiungere al menu delle proprie funzioni attivabili solo sul modello in esame.


| Attributo|Significato|Descrizione |
| ---|----|----|
| Des|Descrizione|Descrizione della funzione presentata nel menu |
| Fun|Funzione|Funzione da eseguire |
| Aut|Autorizzazione|Livello di autorizzazione alla funzione, se non abilitato la funzione non sarà visibile |
| Ico|Icona|l'icona che rappresenterà sul menu la funzione |
| 


**A19.VAR**Variabili
Permette di aggiungere delle variabili per poter simulare il testo


| Attributo|Significato|Descrizione |
| ---|----|----|
| Cod|Nome|Nome della variabile |
| Als|Alias|Nome della variabile da cuio deriva il contenuto |
| Des|Descrizione|Descrizione della variabile |
| Ogg|Oggetto|Oggetto della variabile, permette l'utilizzo dei suoi attributi |
| Val|Valore|Contenuto della variabile |
| 


**A19.PAR**Paragrafo
Permette di definire il paragrafo.


| Attributo|Significato|Descrizione |
| ---|----|----|
| Gra|Grafica|Rappresentazione del paragrafo |
| Lin|Lingua|Abilita il paragrafo solo se il modello del testo è della stessa lingua |
| Aut|Autorizzazione|Abilita il paragrafo solo se autorizzati |
| Des|Descrizione|Nota del paragrafo ad uso dell'implementatore |
| Cnd|Condizione|Abilita il paragrafo solo se la condizione è vera |
| |Paragrafo Interno| |
| IPa|Paragrafo|Testo del paragrafo |
| |Descrizioni estese|Se assente risale al paragrafo interno |
| ET1|Tipo Oggetto|Tipo oggetto |
| EK1|Oggetto|Oggetto |
| |Nota oggetto|Se assente risale al paragrafo interno |
| NT1|Tipo Oggetto|Tipo oggetto |
| NO1|Oggetto|Oggetto |
| |Documentazione oggetto|Se assente risale al paragrafo interno |
| DT1|Tipo Oggetto|Tipo oggetto |
| DK1|Oggetto|Oggetto |
| |Documentazione|Se assente risale al paragrafo interno |
| DLI|Libreria|Libreria |
| DFI|File|File sorgente |
| DME|Membro|Membro |
| DTG|Tag|Tag iniziale da cui estrarre il testo |
| DAT|Attributo|Attributo identificativo del tag. |
| |Nota|Se assente risale al paragrafo interno |
| NCO|Contenitore|Contenitore dela nota |
| NCA|Capitolo|Capitolo da leggere |
| NK1|Oggetto 1|Oggetto 1 |
| NK2|Oggetto 2|Oggetto 2 |
| NK3|Oggetto 3|Oggetto 3 |
| Con|Contesto|Contesto |
| TxtTit|Intestazione|Permette di personalizzare l'intestazione del testo in matrice. |
| OvrPar|Override Parametri|Permette di specificare un valore (T1[SE] P1[GRU.A19] K1[...]) per ottenere l'override del layout dei paragrafi della lettera. |
| 


**A19.PAF**Funzione richiesta Parametri
Permette di mostrare una sezione di richiesta parametri nella forma : 
       2(CN;CLI;-(O;;CNCLI;Cliente)) 3(CN;AZI;-(O;;AZ;Azienda)) 4(TA;C5X;-(O;;TAC5X;Tipo Sollecito))

dove : 
     (-)=richiesta
     (O)=obbligatorio
     (CNCLI), (CNAZI)...=oggetto tipo

 : T02 Modalità di richiamo

Per visualizzare nei servizi il risultato delle lettere occorre lanciare la seguente stringa
D.FUN.STD F(FRM;LOA19_SE;RIT.TXT) 1(SE;SUB.A19;xx.yy.zz) 2(;;) P() INPUT()

Dove FRM indica la visualizzazione del testo in formato grafico. Altre possibilità possono essere EXB (matrice) o TXT(formato di testo)

Nell'oggetto 1 occorre specificare il codice della lettera in oggetto formato da 3 parti xx.yy.zz dove : 

 xx sono gli ultimi due caratteri dello script LOA19_xx in cui ho specificato il modello delle lettere.
 yy sono le lettere che identificano il codice della sezione (SEZ) dello script che ci interessa.
 zz sono le lettere del codice della sottosezione (SUB) dello script che ci interessa.

## Creazione del Testo

Dalla scheda del Costruttore A19 è possibile modificare lo script, dopo averlo creato nell'SCP_SET, attraverso pochi passaggi.

Selezionando il gruppo nella parte alta a sinistra dello schermo e scegliendo "Gestione della Struttura" si visualizza lo schema dello script in cui è possibile gestire i tag già presenti, oppure aggiungerne di nuovi utilizzando il drag&drop.
Selezionando un tag nelle "Istruzioni ammesse" e trascinandolo nella struttura selezionata si aggiungono nuovi tag allo script, e nella parte destra si possono modificare i vari attributi per modellare il testo.

Selezionando una riga dalla "Struttura del testo" e cliccando due volte su "Elimina" la si cancella.

Lo script è possibile modificarlo anche visualizzando l'Editor dello script.
