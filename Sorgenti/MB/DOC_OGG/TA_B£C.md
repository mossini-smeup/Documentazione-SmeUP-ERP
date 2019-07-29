# B£C - Costruzione/controllo campo
 :  : DEC T(ST) K(B£C)
## OBIETTIVI
-    Costruire in modo parametrico un codice articolo;
-    Definire la struttura della configurazione di un prodotto;
-    Formattare e/o controllare una stringa.
La tabella descrive i singoli passi di una sequenza di funzioni, applicabili ad una stringa, utilizzando un modello definito nella tabella B£F.
## SOTTOSETTORI
Utilizzati per scomporre logicamente vari gruppi di passi
## INTRODUZIONE
**Definizioni**
-    Matrice (9 righe di 99 caratteri);
-    Matrice di base : 
viene alimentata dalle matrici dei passi che vengono elaborati.
-    Matrice del passo : 
area temporanea di lavoro utilizzata per alimentare la matrice di base.
-    Coordinate : 
identificazione di riga e colonna di una matrice
**Utilizzo**
-    Costruzione/controllo di un codice articolo
-    Costruzione/controllo della configurazione
**Metodo**
Partendo da una matrice bianca (base), si esegue una sequenza di passi ognuno dei quali costruisce una matrice (del passo), che viene parzialmente trasferita nella matrice base fino ad ottenere il risultato.
Nella matrice base, la prima riga rappresenta il campo (codice, configurazione ecc.) eventualmente da controllare, le altre righe possono essere la descrizione, il disegno o ogni altra funzione derivabile dalle scelte effettuate.
## DETTAGLIO DEI METODI
### *OGG =    Oggetto
.     Significato
Questo metodo permette di effettuare determinate operazioni su oggetti di tipo *CNTT come il controllo dell'appartenenza o la ricerca di elementi.
.     Struttura del parametro
a    Car 1 -2  Tipo Oggetto da *CNTT  (Obblig.)
b    Car 3 -12 Parametro funzione dell'oggetto.
c    Car 13-30 Elemento funzione di passo ab (Non Obblig.)
Se presente e valido si posseggono già tutte le informazioni che servono per costruire la risposta, senza bisogno di fare la domanda (stesso caso della domanda implicita).
.    _9_Esempio
TACLS
AR
.    Struttura della matrice di lavoro
1.......10........20........30......
Codice
Descrizione oggetto
Dati dell'elemento di tabella (presente se tipo oggetto=TA)
### *GRUPPO=  Gruppo passi
.     Significato
Questo metodo permette di gestire in un unico formato le azioni collegate e contraddistinte dal metodo *GRUPPO; le risposte alle domande vengono richieste in un'unica videata all'inizio della conversazione con il costruttore.
I controlli gestiti sono su oggetti di tipo *CNTT.
Se oggetto di tipo NR, per gestire un numero con decimali devo specificare nel parametro        il numero di decimali significativi.
.     Struttura del parametro
a    Car 1 -2  Tipo Oggetto (Obblig.)
b    Car 3 -12 Parametro funzione dell'oggetto.
.    _9_Esempio
TACLS
AR
.    Struttura della matrice di lavoro
1.......10........20........30......
Codice
Descrizione oggetto
Dati dell'elemento di tabella (presente se tipo oggetto=TA)
### *DOI =    Domanda implicita
.     Significato
Questo metodo permette di effettuare una domanda implicita, cioè di leggere la risposta dalla matrice base senza effettuare la domanda a video.
.     Struttura del parametro
a    Car 1 -2  Tipo Oggetto da *CNTT (Obblig.)
b    Car 3 -12 Parametro funzione dell'oggetto.
c    Car 13-30  : /x/yy/zz/, dove : 
x=   Riga
yy=  Colonna
zz=  Lunghezza
rappresentano le coordinate e la lunghezza per reperire la risposta dalla matrice base.
.    _9_Esempio
TACLS         /1/01/02/
.    Struttura della matrice del passo
1.......10........20........30......
Codice
Descrizione oggetto
Dati dell'elemento di tabella (presente se tipo oggetto=TA)
### *CAR =    Carattere
.     Significato
Permette la costruzione di particolari stringhe e costanti.
Le possibilità e i relativi significati sono descritte nel campo parametro.
.     Struttura del parametro
CO..............
Questo metodo permette di assumere la costante digitata dopo la sigla CO
CL
Questo metodo permette, in fase di costruzione, di aprire una finestra in cui è possibile digitare una stringa libera lunga 99 caratteri.
NR
Questo metodo permette di aprire un finestra in cui digitare un stringa numerica lunga 20(14,6).
.    _9_Esempio
COViti grandi
NR
.    Struttura della matrice del passo
1.......10........20........30......
Valore risultante
### *CONSTR :   Controllo di stringa
.     Significato
Questo metodo verifica la correttezza di una stringa. La tipologia della stringa va inserita nel campo parametro.
.     Struttura del parametro
A Carattere Alfabetico Obbligatorio.
a Carattere Alfabetico Non Obbligatorio
- Carattere Obbligatorio Blanks.
N Carattere Numerico Obbligatorio.
n Carattere Numerico non obbligatorio.
* Carattere qualsiasi.
.    _9_Esempio
AAA-NNN   ->   3 lettere, un bianco e 3 numeri
.    Struttura della matrice del passo
1.......10........20........30......
Valore risultante
Se la stringa non è corretta appare una finestra nella quale vengono evidenziati i caratteri non corretti.
### *TAB :      Elemento di tabella
.     Significato
Permette di Parzializzare sugli elementi di una tabella
.     Struttura del parametro
Settore e sottosettore/limite 1 /Limite 2/.
.     _9_Esempio
CLS  /A/A99999/ -> Tutti gli elementi di CLS (sottosettore blanks) che iniziano con A
.    Struttura della matrice del passo
1.......10........20........30......
Codice       Descrizione oggetto
Dati dell'elemento di tabella.
### *PRGOG :    Progressivo di un oggetto
.     Significato
Permette di ottenere il prossimo progressivo da assegnare un un codice data la sua parte iniziale.
.     Struttura del parametro
-    Tipo/Parametro oggetto
-    Tipo lettura S=Stringa o C=Coordinate
-    Significato stringa o Coordinate relative alla posizione iniziale della radice nella matrice lavoro xyy
Coordinate  : 
x=   Riga
yy=  colonna
-    Lunghezza della stringa o della radice (Sempre 2 numeri)
-    Lunghezza del progressivo (Sempre 2 numeri)
-    Tipo di incremento A=Alfan. / N=Numerico
.     _9_Esempio
1.   AR/S/VIT/03/06/N
Prossimo progressivo fra i codici articolo che iniziano con VIT. Il risultato dovrà avere la struttura VITnnnnnn
.    Struttura della matrice del passo
1.......10........20........30......
Codice
.     _9_Esempio
2.   AR/C/101/04/03/N
Prossimo progressivo fra i codici articolo che iniziano con la radice che si trova in riga 1 colonna 1 della matrice base ed è lunga 4 . Il risultato dovrà avere la struttura Radicennn, dove nnn è il progressivo.
.    Struttura della matrice del passo
1.......10........20........30......
RadiceProgressivo.
### *DOMPAR :   Domande di gruppo derivate da parametro
.    Significato
Presenta le domande che sono catalogate in un parametro.
Ciò permette di rendere le domande dipendenti da un modello che l'utente sceglie implicitamente o esplicitamente in un
passo precedente.
Ad _9_esempio : 
-    Chiedo il modello di sedia
-    Dai parametri del modello (codificato come articolo e coincidente con il gruppo distinta) derivo le domande rilevanti e le presento.
Le domande che si possono inserire nel passo devono essere con metodo *TAB, *OGG, *RISPAR.
.    Specificità
Se la categoria dei parametri indicata ha associato una tabella di condizionamento "C£N", la presentazione delle domande avviene per sezioni successive condizionate dalle risposte alle domande precedenti. Si procede nel modo seguente : 
1)   Associare una condizione "SE" alla domanda interessata
2)   Definire il metodo di condizionamento.
Ad _9_esempio : 
Domanda A0050 richiesta se la risposta alla domanda A0010 è un valore : 
-    VA   incluso in una lista
-    ES   escluso da una lista
-    EQ   uguale a
-    RG   compreso in range di valori
Sruttura del parametro
-    Categoria parametri
-    Codice parametro all'interno della categoria
-    Codice oggetto (Eventualmente variabile nella forma sopra descritta &RCoLu)
.     _9_Esempio
XXXYYY$10115
Leggere il parametro "YYY" per l'oggetto derivato dalla riga 1 a partire da colonna 02 per 15 posizioni all'interno della categoria parametri "XXX".
.    Struttura della matrice del passo
1.......10........20........30......
Nessuna
### *RISPAR :   Risposte controllate mediante un parametro
.    Significato
Condiziona i valori possibili di una risposta, compresa in un gruppo del metodo "*DOMPAR", ai soli valori presenti, per uno specifico parametro di un oggetto.
.    Sruttura del parametro
-    Categoria parametri
-    Codice parametro all'interno della categoria
-    Codice oggetto (Eventualmente variabile nella forma sopra descritta &RCoLu)
.     _9_Esempio
XXXYYY$10115
Leggere il parametro "YYY" per l'oggetto derivato dalla riga 1 a partire da colonna 02 per 15 posizioni all'interno della categoria parametri "XXX" ed utilizzare i valori associati come unici valori ammessi per la domanda.
.    Struttura della matrice del passo
1.......10........20........30......
Come per *TAB se il parametro ha associato una tabella, diversamente come *OGG.
### *PRGCRN :   Progressivo da tabella CRN
.    Significato
Costruisce un progressivo di un oggetto a partire dalla tabella CRN.
Se viene specificato il Tipo/Parametro di verifica il numeratore (Presente in CRN) viene decrementato fino al primo progressivo valido per quel Tipo/Parametro Oggetto.
Successivamente viene aggiornato il numeratore in tabella CRN.
.    Sruttura del parametro
-    S.S. tabella CRN
-    Codice numeratore
-    Tipo oggetto per verifica (TAB *CNTT)
-    Parametro per Verifica
.   _9_Esempio
XXYYYYYYZZKKKKKKKKKK
Ricava il progressivo dal S.S. XX della tabella CRN elemento YYYYYY e esegue le verifiche (£DEC) sul tipo oggetto ZZ parametro KKKKKKKKKK.
.    Struttura della matrice del passo
1.......10........20........30......
Progressivo come da tabella CRN.
### *DOMGRU :   Domanda di Gruppo
.    Significato
Permette di associare ad una domanda (Passo B£C) un insieme di domande.
.    Sruttura del parametro
-    S.S. tabella B£C
-    Limite Iniziale Domande
-    Limite Finale Domande
.   _9_Esempio
XXYYYYYKKKKK
Vengono effettuate le domande (TAB B£C) presenti nel sottosettore XX comprese tra YYYYY e KKKKK.
.    Struttura della matrice del passo
1.......10........20........30......
Nessuna
### *VERUNI :   Verifica univocità parametri
.    Significato
Permette di verificare l'univocità dei parametri legati ad un oggetto. Se l'univocità non è soddisfatta verranno presentati tutti gli oggetti trovati ed un successivo messaggio. Impostando il parametro della tabella il messaggio sarà di tipo informativo (non accetta duplicazioni, il flusso verrà abbandonato) o con conferma (accetta duplicazioni, il flusso potrà proseguire in funzione della risposta).
.    Struttura del parametro
-    Tipo V2SI/NO.
.    Struttura della matrice del passo
1.......10........20........30......
Nessuna
## CONTENUTO DEI CAMPI
 :  : FLD T$B£CM **Programma/Metodo**
Se il campo inizia con il carattere '*' è un metodo già fornito, altrimenti è un programma.
Programma : 
In questo campo va inserito il programma da chiamare (tutti i programmi applicabili devono avere la stessa struttura di chiamata).
_9_Esempio
-    Programma che controlla i caratteri numerici/alfanumerici maiuscoli/minuscoli
-    Programma che controlla elementi di tabella
-    Programma che gestisce le varianti della risposta ad una domanda di configurazione.
Metodo : 
In questo caso va digitato il tipo di metodo utilizzato dall'elemento di tabella. I metodi sono identificati dal loro inizio con *. I metodi attualmente sviluppati sono descritti di seguito.
 :  : FLD T$B£CP **Parametro**
In questo campo va inserito il tipo di parametro da gestire.
Le possibilità e la tipologia cambiano a seconda del METODO utilizzato come descritto di seguito.
Il parametro può contenere il riferimento a posizioni della matrice risultante. Ciò si ottiene indicando nelle posizioni desiderate : 
- &RCoLu
- &    Indica l'inizio di una variabile.
- R    Riga della matrice del risultato.
- Co   Colonna della matrice del risultato.
- Lu   Lunghezza caratteri da sostituire.
 :  : FLD T$OR,1 **Azione 1**
Sequenza di azioni con cui trasferire parti della matrice del passo alla matrice base.
-    Per ogni azione avremo la struttura : 
xyyllzww
xyy  Coordinate origine
x=   Riga
yy=  Colonna
ll   Lunghezza della stringa da trasferire
zww  Coordinate destinazione
z=   Riga
ww=  Colonna
_9_Esempio
-    Portare la variante colore di un materiale nelle prime 5 posizioni della configurazione
-    Portare la parola "Cilindro" nella descrizione dell'articolo se viene scelta la classe "CIL"
-    Fissare il pianificatore in funzione della famiglia di prodotti.
 :  : FLD T$B£CS **Passo successivo**
1)   Derivazione fissa
-    Subsettore della tabella stessa
-    Elemento all'interno del subsettore
2)   Derivazione calcolata
Coordinate e lunghezza che identificano il prossimo passo da eseguire (dello stesso subsettore) derivato dalla matrice base del momento.
xyyzz Coordinate e lunghezza : 
x=   Riga
yy=  colonna
zz=  lunghezza
_7_N.B. La derivazione calcolata ha precedenza sulla fissa.
