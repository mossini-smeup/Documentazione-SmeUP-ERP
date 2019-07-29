## Obiettivo
Generalizzare la costruzione di totali, mediante comandi sql, e l'analisi del loro dettaglio.

## Comando SQL
Il comando SQL viene costruito attraverso gli schemi.

## Attività dell'installatore
L'installatore deve definire la propria struttura di recupero dei testi nello script che deve risiedere nel sorgente**SCP_SET**.
Lo script è composto da due parti, la prima carattere e la seconda numerica, permettendo così la generazione di script meno corposi e semplici da mantenere.
La parte carattere non deve eccedere gli 8 caratteri, mentre la parte numerica deve essere lunga 2.

 ### Tag dello script
 Elenco delle tag e del loro significato
 
| Tag|Significato |
| ---|----|
| SEZ|Inizio di una sezione |
| SUB|Inizio di una sottosezione |
| A30.SET|Setup |
| A30.MNU|Funzione di menù |
| A30.POP|Funzione di pop.up |
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


**A30.SET**Setup del testo
Permette di impostare la modalità di sintesi

| Attributo|Significato|Descrizione |
| ---|----|----|
| Des|Descrizione|Descrizione della sintesi |
| TSc|Oggetto|Script dello schema presente in SCP_NAV |
| NSc|Schema|Nome dello schema presente per l'oggetto |
| Whr|Where|Condizione di filtro, puo essere ricevuta anche nell'imput con l'attributo WHR |
| LOg|Lista Oggetto|L'oggetto identificativo del filtro per lista |
| LNm|Lista Nome|Nome della lista, puo essere ricevuta nell'impoy con l'attributo LI(<og>;<Nome>) |
| 


 **A30.MNU**Funzione del menu
 Permette di aggiungere al menu delle proprie funzioni attivabili solo sulla sintesi in esame.
 
|  Attributo|Significato|Descrizione |
| ---|----|----|
|  Des|Descrizione|Descrizione della funzione presentata nel menu |
|  Fun|Funzione|Funzione da eseguire |
|  Aut|Autorizzazione|Livello di autorizzazione alla funzione, se non abilitato la funzione non  sarà visibile |
|  Ico|Icona|l'icona che rappresenterà sul menu la funzione |
|  


 **A30.POP**Funzione del Pop.UP
 Permette di aggiungere al Pop_up delle proprie funzioni attivabili solo sulla sintesi in esame.
 
|  Attributo|Significato|Descrizione |
| ---|----|----|
|  T1|Tipo|Tipo oggetto su cui attivare il pop.up |
|  P1|Parametro|Parametro oggetto su cui attivare il pop.up |
|  K1|Oggetto|Oggetto su cui attivare il pop.up |
|  Des|Descrizione|Descrizione della funzione presentata nel pop.up |
|  Fun|Funzione|Funzione da eseguire |
|  Aut|Autorizzazione|Livello di autorizzazione alla funzione, se non abilitato la funzione non  sarà visibile |
|  Ico|Icona|l'icona che rappresenterà sul menu la funzione |
|  


 ### Variabili interne
 Elenco delle variabili utilizzabili negli script del menu e del pop.up.

| Variabile|Significato|Descrizione |
| ---|----|----|
| G25|Script Schema|Nome dello script "TSc" |
| N25|Nome Schema|Nome dello schema "NSc" |
| Doc|Documentazione|Nome della documentazione specifica |
| Ogg|Oggetto|Nome dell'oggetto SE |
| Gru|Gruppo|Nome del gruppo SE |
| IN|Input|Input della funzione |
| PA|Parametro|Parametro della funzione |
| 

