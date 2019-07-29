## Obiettivo
Costruire una navigazione a livelli attraverso uno script associando ad ogni livello la propria funzione da eseguire.
Il limite massimo di livelli ammessi è di 14.

## Attività dell'installatore
L'installatore deve definire la propria struttura di navigazione nello script che deve risiedere nel sorgente**SCP_SET**.
La struttura di navigazione è definità attraverso un legame a tre livelli così composto : 
**Livello 01**Nome dello script
**Livello 02**Nome della sezione
**Livello 03**Nome della sottosezione
Lo script è composto da due parti, la prima carattere e la seconda numerica, permettendo così la generazione di script meno corposi e semplici da mantenere.
La parte carattere non deve eccedere gli 8 caratteri, mentre la parte numerica deve essere lunga 2.

**Esempio : **
 :  : PAR L(TAB)
Script|Sezione|Sottosezione|Descrizione
**PROVA_01**|001|001|Struttura 01 Sezione 001 Sottosezione 001
**PROVA_01**|001|002|Struttura 01 Sezione 001 Sottosezione 002
**PROVA_01**|002|001|Struttura 01 Sezione 002 Sottosezione 001
PROVA_02|**001**|**001**|Struttura 02 Sezione 001 Sottosezione 001
PROVA_02|**001**|**002**|Struttura 02 Sezione 001 Sottosezione 002

Come si nota, all'interno dello script**PROVA_02**è permessa la stessa definizione di sezione e sottosezione utilizzata nello script**PROVA_01**

### Tag dello script
Elenco delle tag e del loro significato
 :  : PAR L(TAB)
Tag|Significato
SEZ|Inizio di una sezione
SUB|Inizio di una sottosezione
LIV|Definizione del livello di navigazione
LIV.AUT|Costruzione automatica dei livelli analizzando il comando SQL
INT|Inizio di una lista
INT.OGG|Oggetto della lista
FUN|Inizio di una azione
FUN.EXE|Azione da eseguire
GRA|Inizio di un grafico
G.SET.CHA|Setup del grafico
I.POP|Popup della sottosezione


Ora vediamo in dettaglio gli attributi di ogni tag
**SEZ**Sezione
 :  : PAR L(TAB)
Attributo|Significato|Descrizione
Cod|Codice|Viene presentato nell'albero di scelta
Txt|Descrizione|Viene presentato nell'albero di scelta


**SUB**Sotto sezione
 :  : PAR L(TAB)
Attributo|Significato|Descrizione
Cod|Codice|viene presentato nell'albero di scelta
Txt|Descrizione|viene presentato nell'albero di scelta


**LIV**Livello di navigazione
 :  : PAR L(TAB)
Attributo|Significato|Descrizione
Cod|Livello|Deve essere un progressivo numerico di 2 e iniziare da 01.
Txt|Descrizione|A solo uso documentativo negli altri casi.
Mod|Modalità|Assume i valori OGG(lista Oggetto), INT(Lista interna), LIS(Lista esterna), SQL, FUN(Funzione di tipo albero)
Par|Parametro|Comando SQL o funzione da eseguire
Ogg|Oggetto|Tipo e parametro dell'oggetto del livello. Si può definire, se in modalità SQL, il recupero attraverso il campo del file racchiuso fra parentesi quadre. Se modalità funzione (FUN) l'oggetto è assunto dalla funzione stessa.
Des|Descrizione dell'oggetto|Se impostata sovrascrive quella dell'oggetto.Si può definire, se in modalità SQL, il recupero attraverso il campo del file racchiuso fra parentesi quadre.
Ord|Ordinamento|Definire il valore**Des**per ottenere un'ordinamento discendente
Ele|Nr.elementi|Definire il numero di elementi massimi da emettere nel livello
Flt|Filtro interno|Definisce il filtro da usare (Attiva solo se si usa il modello OGG)
FlE|Filtro esterno|Definire una condizione di validazione (Attiva solo se si usa il modello OGG)
Lis|Nome della lista|Indica il nome della lista (Attiva solo se si usa il modello INT o LIS)
Fun|Nome funzione|Indica il nome della funzione da richiamare al click del mouse
ILi|Intestazione del Livello|Crea un livello solo descrittivo dei dati sottostanti
Ico|Icona|Se impostata definisce l'aspetto estetico dell'icona.Si può definire, se in modalità SQL, il recupero attraverso il campo del file racchiuso fra parentesi quadre.
Clo|Fine foglia|Forza la fine del livello, basta impostare un qualsiasi valore.
Usr|Exit Utente|Definire il nome del programma che dovrà creare il livello richiesto.
VEs|Vincolo esecuzione|Il livello viene eseguito solo se si verifica la condizione qui descritta
VEf|Vincolo esecuzione della funzione|La funzione associata al livello verrà eseguita solo se si verifica la condizione qui descritta
Var|Nome della variabile del libello
Gra|Nome del setup grafico
FGr|Forma grafica  (Se vuota assunta dall'azione)

La scrittura dell'SQL deve essere sempre spaziata, altrimenti la derivazione dell'ordinamento non produrrà l'effetto desiderato.
Scrivere sempre "campo = valore" e non "campo=valore"
La Where viene utilizzata per costruire l'ordinamento nella variabile A16CM, per questo motivo descrivere i campi nella sequenza desiderata.
E' possibile eseguire la seguente funzione per verificare il contenuto della memoria "F(EXD;*SCO;) 1([T1];[P1];[K1]) 2(MB;SCP_SCH;LOA16) 4(;;MEM) P(Scp([Scp]) Gru([Gru]) Str([Str]))"

Si può definire più esecuzioni allo stesso livello, bisogna però tener presente che : 
Le funzioni ad esso associate verranno determinate dall'oggetto definito sul livello stesso.

**LIV.AUT**Livello di navigazione automatico (Utilizzabile solo associata ad un comando SQL)
 :  : PAR L(TAB)
Attributo|Significato|Descrizione
Txt|Descrizione|A solo uso documentativo negli altri casi.
Par|Parametro|Comando SQL
Ogg|Oggetto|Tipo e parametro dell'oggetto del livello, si può definire il recupero attraverso il campo del file racchiuso fra parentesi quadre. Elencare per ogni livello separando con il carattere ";"
Fun|Nome funzione|Indica il nome della funzione da richiamare al click del mouse, Elencare per ogni livello separando con il carattere ";"
Ope|Operazione da eseguire
Var|Nome della variabile del libello. Elencare per ogni livello separando con il carattere ";"
Gra|Nome del setup grafico. Elencare per ogni livello separando con il carattere ";"
FGr|Forma grafica (Se vuota assunta dall'azione)



**I.POP**Pop.UP
Il pop.up deve essere inserito nella sottosezione in cui si vuole attivarlo. Questo avrà effetto su tutti i livelli in cui è presente l'oggetto del pop.up stesso.

**EXIT UTENTE**
L'exit utente riceverà i seguenti attributi : 
 :  : PAR L(TAB)
Attributo|Significato|Grandezza
Livelllo|Livello da generare|30
Riga|Riga dello script|30000 Variabile
Parametri|Parametri ricevuti per il livello|30000 Variabile

L'exit utente deve ritornare il livello esploso, può estendersi fino ad un massimo di 30000 caratteri, e deve ritornare l'indicatore 35 acceso in caso di livello vuoto.
Fare riferimento al programma di esempio denominato**LOA16_ES**come esempio di costruzione di un 2 livello.

**INT**Inizio della lista interna
 :  : PAR L(TAB)
Attributo|Significato|Descrizione
Cod|Codice|Nome della lista


**INT.OGG**Oggetto della lista interna
 :  : PAR L(TAB)
Attributo|Significato|Descrizione
Cod|Codice|viene presentato nell'albero di scelta
Ogg|Oggetto|Oggetto
Txt|Descrizione|Descrizione dell'oggetto


**FUN**Inizio della funzione
 :  : PAR L(TAB)
Attributo|Significato|Descrizione
Cod|Codice|Nome della funzione


**FUN.EXE**Funzione
 :  : PAR L(TAB)
Attributo|Significato|Descrizione
Fun|Funzione|Definire la funzione che deve essere eseguita.


## Variabili
Sono disponibili nello script
 :  : PAR L(TAB)
Varibile|Descrizione
Tnn|Oggetto del livello nn
Pnn|Parametro del livello nn
Lnn|Valore del livello nn
OG|Valore dell'oggetto in scrittura

La varibile può essere utilizzata per accedere ai suoi attributi.
Le varibili sono contenute nel contesto**LOA16_SE** seguita dalla struttura, aggiungendo variabili in questo contesto vengono rese disponibili nello script stesso.
la struttura è cosi strutturato : 
 :  : PAR L(TAB)
Descrizione|Valore
Separatore|_
Script|Nome dello script
Separatore|_
Struttura|Identificativo della struttura


Sono disponibili al client
 :  : PAR L(TAB)
Varibile|Descrizione|Quando di attiva
A16CM|Comando sql|Solo se in modalità SQL
A16NF|Nome file|Solo se in modalità SQL
A16WH|Where|Solo se in modalità SQL
A16LV|Mome campo del livello|Solo se in modalità SQL
A16PA|Variabili dei livelli|Sempre
A16FU|Funzione da eseguire|Sempre

Queste varibili si riferiscono all'attività che deve essere eseguita per sviluppare il livello sucessivo.

## Sezioni Utente
Ad ogni selezione del livello viene eseguita una chiamata alle sezioni utente denominate : 
 :  : PAR L(TAB)
LOA16_U01
LOA16_U02
LOA16_U03
LOA16_U04
LOA16_U05

vengono trasmesse le seguenti variabili : 
 :  : PAR L(TAB)
Varibile|Descrizione|Quando di attiva
A16CM|Comando sql|Solo se in modalità SQL
A16NF|Nome file|Solo se in modalità SQL
A16WH|Where|Solo se in modalità SQL
A16LV|Mome campo del livello|Solo se in modalità SQL
A16PA|Variabili dei livelli|Sempre
A16FU|Funzione da eseguire|Sempre


## Parametri di Impostazioni
 :  : PAR L(TAB)
Parametro|Valore|Descrizione|Quando di attiva
Scp|xx|Nome dello script|Viene utilizzato per esplodere la struttura, deve esistene nello SCP_SET e deve essere lungo al massimo 8 caratteri.
Azi|ORG|Organizzata|Viene visualizzata la struttura e ammessa la navigazione su di essa
Azi|ALB|Albero|Viene ricevuta la struttura su cui navigare, non è ammesso il cambio di struttura.
Azi|GRI|Griglia|Viene ricevuta la struttura su cui navigare, non è ammesso il cambio di struttura.
Azi|IML|Lista immagini|Viene ricevuta la struttura su cui navigare, non è ammesso il cambio di struttura.
Azi|IBL|Immagini badge list|Viene ricevuta la struttura su cui navigare, non è ammesso il cambio di struttura.
Azi|IST|Grafico|Viene ricevuta la struttura su cui navigare, non è ammesso il cambio di struttura.
Met|Vuoto|Tipo scheda|Divide la scheda in struttura e rende disponibile lo spazio su cui si esegyuiranno le funzioni associate al livello.
Met|USR|Tipo scheda|Tutta la scheda è riservata alla struttura
Gru|xx|Identificativo del gruppo|Concatenato allo script definisce il contenitore della struttura.|Da utilizzare quando non si vuole permettere la navigazione sulla struttura o limitarne i gruppi nella navigazione.
Fse|xx|Filtro della sezione|In esplosione della struttura,se in azione ORG, filtra la sola sezione passata.
AEs|1|Espansione iniziale della struttura|Se impostato la struttura viene aperta automaticamente.
Sch|xx.xx.xx|Identificativo della struttura in formato :  Gruppo.Sezione.Sottosezione.|Da utilizzare quando non si vuole permettere la navigazione sulla struttura in assenza verra mostrata l'intera struttura
VCo|No|Memorizzo variabili per contesto|Se impostato**No**memorizza le variabili per contesto LOA16_SE, in tutti gli altri casi per contesto LOA16_SE_<Scp>_<Sch>.
VCS|xx|Memorizzo variabili per contesto|Se impostat  memorizza le variabili per contesto ricevuto, permettendo la condivisione di variabili. Il contesto deve essere già stato preparato prima di essere utilizzato
NTx|Code|Tipo albero|Sono mostrati solo i codici
NTx|Text|Tipo albero|Sono mostrati solo le decodifiche
NTx|Both|Tipo albero|Sono mostrate sia i codici che le decodifiche, valore assunto per Default.
Exp|xx|Espansione dei livelli|Numero di livelli da aprire oltre quello richiesto
VLI|xx|Variabile del primo livello
DU1|No|Dinamicità su sezione LOA16_U01|Se impostato**No**non viene seguita la dinamicità al click, in tutti gli altri casi si (valore assunto per Default).
DU2|No|Dinamicità su sezione LOA16_U01|Se impostato**No**non viene seguita la dinamicità al click, in tutti gli altri casi si (valore assunto per Default).
DU3|No|Dinamicità su sezione LOA16_U01|Se impostato**No**non viene seguita la dinamicità al click, in tutti gli altri casi si (valore assunto per Default).
DU4|No|Dinamicità su sezione LOA16_U01|Se impostato**No**non viene seguita la dinamicità al click, in tutti gli altri casi si (valore assunto per Default).
DU5|No|Dinamicità su sezione LOA16_U01|Se impostato**No**non viene seguita la dinamicità al click, in tutti gli altri casi si (valore assunto per Default).

