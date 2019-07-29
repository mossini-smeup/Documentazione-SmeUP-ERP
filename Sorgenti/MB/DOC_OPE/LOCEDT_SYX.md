# Sintassi del linguaggio della documentazione - Introduzione
Il presente documento ha lo scopo di descrivere le specifiche e i costrutti, e dove possibile fornirne degli esempi, disponibili per la composizione della documentazione attiva visualizzabile tramite i componenti della scheda o del browser di Loocup.
Questo a complemento del wizard presente nell'editor e richiamabile premendo _B_CTRL+W sulle specifiche.
Il documento è suddiviso nella varie categoria di elementi supportati dalla sintassi dell'editor.

# Elementi di testo
Sono a disposizione elementi per definire titoli, righe o paragrafi con formato definito.
## I titoli
Esistono tre livelli gerarchici di titolo di importanza decrescente : 
 - ..**T01**
 - ..**T02**
 - ..**T03**

## Le righe
Esistono tre tipi di riga : 
 - ..**R01**
 - ..**R02**
 - ..**R03**

### Esempi
 :  : R01 Riga tipo R01
Sintassi : 
 :  : R01 Riga tipo R01
 :  : R02 Riga tipo R02
Sintassi : 
 :  : R02 Riga tipo R02
 :  : R03 Riga tipo R03
Sintassi : 
 :  : R03 Riga tipo R03

## I paragrafi
 :  : R01 Specifica PAR che deve essere chiusa dalla specifica PAR.END
Esistono quattro diversi tipi di paragrafo : 
 - Piano senza valorizzazione della variabile F
 - In evidenza (grassetto) :  F(01)
 - Formato fisso (font monospaced con colore blu) :  F(02)
 - Nota tecnica (italic con font piccolo) :  F(03)
 - Formattazione forzata :  F(04)

### Esempi
Piano
Esempio di PAR
Sintassi : 
** : ** : PAR T(Piano)
Esempio di PAR
** : ** : PAR.END
In evidenza : 
Esempio di PAR
Sintassi : 
** : ** : PAR F(01) T(In evidenza)
Esempio di PAR
** : ** : PAR.END
Formato fisso : 
Esempio di PAR
Sintassi : 
** : ** : PAR F(02) T(Formato fisso)
-
Esempio di PAR
** : ** : PAR.END
Nota tecnica : 
Esempio di PAR
Sintassi : 
** : ** : PAR F(03) T(Nota tecnica)
Esempio di PAR
** : ** : PAR.END

# Le liste
 :  : R01 Specifica PAR che deve essere chiusa dalla specifica PAR.END
Il linguaggio permette di comporre delle liste, anche annidate. Esse possono avere come indicatori punti, numeri o lettere.
 * I singoli item delle lista devono essere una riga nuova che comincia con un trattino e uno spazio ("_2_- ")
 * Le liste supportano gli stessi formati dei paragrafi :  F(01), F(02), F(03) e F(04) che rappresentano gli stessi effetti di stile.
 * Nel caso di liste ordinate (numerate o letterali) è supportata la variabile C che permette di indicare : 
 ** se continuare la numerazione o "letterazione" prendendola dall'elenco precedente _2_*CONT
 ** se iniziare l'elenco da una specifica lettera o numero
 * Vengono gestiti anche tre differenti tipi di lista tramite la variabile L

## Puntate
### Esempi
Tipo puntato : 
 * Riga 3.p
 * Riga 3.p
 ** Nested 1
 * Riga 3.p
Sintassi : 
** : ** : PAR T(Tipo puntato) L(PUN)
 * Riga 3.p
 * Riga 3.p
 ** Nested 1
 * Riga 3.p
** : ** : PAR.END

## Numerate
### Esempi
Tipo numerato : 
 - Riga 1.n
 - Riga 2.n
 - Riga 3.n
 -- Riga 3.1.n
 --- Riga 3.1.1.n
 --- Riga 3.1.2.n
 -- Riga 3.2.n
 - Riga 4.n

Sintassi : 
** : ** : PAR L(NUM) T(Tipo numerato)
- Riga 1.n
- Riga 2.n
- Riga 3.n
-- Riga 3.1.n
--- Riga 3.1.1.n
--- Riga 3.1.2.n
-- Riga 3.2.n
- Riga 4.n
** : ** : PAR.END


## Alfabetiche
L(LET)
### Esempi
 :  : PAR L(LET) T(Tipo alfabetico)
- Riga 2.l
-- Riga 2.l
--- Riga 2.l
- Riga 2.l
- Riga 2.l
- Riga 2.l

 :  : PAR T(Sintassi) F(04)
** : ** : PAR L(LET) T(Tipo alfabetico)
- Riga 2.l
-- Riga 2.l
--- Riga 2.l
- Riga 2.l
- Riga 2.l
- Riga 2.l
** : ** : PAR.END

**P.S.** :  all'interno delle liste vengono mal gestite le immagini, quindi tag IMG all'interno di liste possono dare origine a comportamenti non lineari nel posizionamento delle immagini, soprattutto nella generazione del PDF.


# Le tabelle
 :  : R01 Specifica TAB che deve essere chiusa dalla specifica TAB.END
La sintassi è simile alle liste : 
 * _2_Nota, c'è un tag aggiuntivo rispetto alle liste che permette di qualificare le colonne (es. la dimensione) e la loro intestazione ed è il tag ..TAB.COL che deve essere specificato per ogni colonna. _2_Attenzione, per una corretta gestione nella stampa Latex l'ultima colonna deve avere _1_Allineamento = "L".
 * Ogni riga di contenuto contiene i valori delle celle separati da pipe (**|**)
 * Nella specifica TAB viene gestito il parametro _1_R, che determina la percentuale di riduzione della larghezza della tabella rispetto alla larghezza pagina (default 60%)
 * Nella specifica TAB.COL viene gestito il parametro _1_Lun, che determina la percentuale di larghezza della colonna rispetto alla larghezza pagina (se manca o se = 0 il parametro Lun viene saltato e si utilizzano Allineamento e LunAut. _2_Nota Bene la somma dei parametri Lun della varie colonne non può essere superiore al parametro R della tabella.

## Con colonne omogenee
### Esempi

|  Nam="Esempio tabella 1" |
| 
| .COL Txt="Test" LunAut="1" |
| ---|----|
| 
| .COL Txt="tabella" Lun="0" LunAut="1" |
| 
| .COL Txt="HTML" LunAut="1" A="L" |
| riga|dati|esempio |
| 

 :  : PAR T(Sintassi) F(04)
** : ** : TAB T(Esempio tabella 1)
** : ** : TAB.COL Txt="Test"  LunAut="1"
** : ** : TAB.COL Txt="tabella" Lun="0"  LunAut="1"
** : ** : TAB.COL Txt="HTML" LunAut="1"  A="L"
- riga|dati|esempio
** : ** : TAB.END


## Con colonne disomogenee
 **E' attivo solo nell'esportazione in PDF ma non vale nella visualizzazione HTML**
### Esempi

|  Nam="Esempio tabella 2" R="0000000065" |
| 
| .COL Txt="Test" |
| ---|----|
| 
| .COL Txt="tabella" |
| 
| .COL Txt="HTML"  LunAut="1" A="L" |
| riga|dati|esempio |
| 

 :  : PAR T(Sintassi) F(04)
** : ** : TAB T(Esempio tabella 2" R="0000000065")
** : ** : TAB.COL Txt="Test"
** : ** : TAB.COL Txt="tabella"
** : ** : TAB.COL Txt="HTML" LunAut="1" A="L"
- riga|dati|esempio
** : ** : TAB.END


# Le immagini
E' possibile includere nel documento immagini utilizzando la specifica IMG

## Inclusioni esplicite
 :  : R01 Specifica IMG
La specifica IMG gestisce quattro parametri : 
 - Il parametro P permette di indicare il percorso
 - Il parametro H permette di indicare l'altezza con cui verrà rappresentata l'immagine
 - Il parametro W permette di indicare la larghezza con cui verrà rappresentata l'immagine
 - Il parametro R permette di indicare la percentuale di scalatura, che mantiene le proporzioni della stessa, con cui verrà rappresentata l'immagine. **E' attivo solo nell'esportazione in PDF, ma non vale nella visualizzazione HTML

### Esempi
 :  : IMG P(\\Smea.it\dfs_root\aziende\smea\LOOCUP_IMG\AR\02.jpg) H(0000000180) W(0000000200)
 :  : IMG P([IMG : CN;COL;01]) H(0000000180) W(0000000200)
 :  : IMG P([IMG : CN;COL;01]) R(30)
 :  : IMG P([IMG : J1;FUN;F(EXA;B£SER_43B;TST.IMG) 1(J1;GRA;EXA) 2(TA;V§R;) P(Typ(PIE))])
 :  : IMG P([IMG : J1;FUN;F(SPC;B£SER_43B;TST.IMG) 1(J1;GRA;SPC) 2(TA;V§R;) P(Typ(FRE))])
 :  : IMG P([IMG : J1;FUN;F(EXB;B£SER_43B;TST.IMG) 1(J1;GRA;EXB) 2(TA;V§R;)])



 :  : DEC T(J1) P(PATHFILE) K(\\Smea.it\dfs_root\aziende\smea\LOOCUP_IMG\AR\01.jpg)

Sintassi : 
..IMG P([AZI.IMG]\CN\COL\default.jpg) H(0000000180) W(0000000200)
oppure
..IMG P([AZI.IMG]\CN\COL\default.jpg) R(90)

# Le funzioni
 :  : R01 Specifica DEC
La specifica DEC permette di rappresentare delle chiamate funzione.

La specifica DEC supporta i seguenti parametri : 
 * **T** :  tipo oggetto
 * **P** :  parametro oggetto
 * **K** :  codice oggetto
 * **D** :  descizione dell' oggetto
 * **I** :  intestazione del link
 * **X** :  eventuale funzione da richiamare sul click anzichè il default
 * **O** :  configurazione dell' output del link :  essa può assumere uno o più di dei seguenti valori : 
 ** **T** riporta il tipo del documento linkato nel link
 ** **P** riporta il parametro del documento linkato nel link
 ** **K** riporta il codice del documento linkato nel link
 ** **I** riporta il campo I nel link
 ** **D** riporta il campo D nel link
 ** **G** riporta l'immagine dell'oggetto T-P-K nel link
 ** **R** non permette l'inclusione del file puntato nella generazione del PDF

La funzione di default è la chiamata della scheda dell'oggetto T-P-K.
In alcuni casi però il comportamento si discosta da tale standard : 
 * Nei tipi oggetto **MB-DOC**, infatti viene richiamato il file di documentazione.
 * Nei tipi oggetto **J1-PATHFILE** viene richiamato il file PC.

>N.B. :  nel caso di tipo di ogggetto _1_MB-DOC,  bisogna considerare le seguenti caratteristiche : 
 - viene riportata **sempre e solo** la descrizione del membro. **Il parametro O, in questo caso, viene trascurato.
 - se non viene specificato il parametro _1_I viene incluso il membro in oggetto, diversamente viene formato il link al membro.

## Chiamate di funzioni
### Esempi
 :  : DEC T(AR) P() K(A01) I(Funzione su articolo)
 :  : PAR F(04) T(Sintassi)
 :  : DEC T(AR) P() K(A01) I(Funzione su articolo)

 :  : DEC T(AR) P() K(A01) D(G) I(Prova override funzione di default) X({M(EMU;ESE;AZI) 1(TA;MEABR;0101) P() G() SP() SG() NOTIFY()}) O(I)
 :  : DEC I(Esempio Funzione) X(F(TRE;*MNU;)) O(I)

 :  : PAR F(04) T(Sintassi)
 :  : DEC T(AR) P() K(A01) D(G) I(Prova override funzione di default) X({M(EMU;ESE;AZI) 1(TA;MEABR;0101) P() G() SP() SG() NOTIFY()}) O(I)

## Chiamate a link esterni
[https://mail.softia.com](https://mail.softia.com)
[https://mail.softia.com](https://mail.softia.com)
[http://www.smeup.com](http://www.smeup.com)
[http://www.smeup.com](http://www.smeup.com)
 :  : DEC T(J1) P(PATHFILE) K([AZI.HOM.01]\Documenti\PDF_SUBHTM.pdf) I(Link a file PDF) O(GI)

Sintassi : 
[http://www.smeup.com/images/home_centro_sx.jpg](http://www.smeup.com/images/home_centro_sx.jpg)

## Chiamate a documentazione
Sintassi : 
 :  : DEC T(MB) P(DOC) K(LOCHTM_PTF) D(Informazioni su Rilasci) I(Prova link a documentazione non incluso) O(GIR) L(1)

# I popup
 :  : R01 Specifica INT che deve essere chiusa con FIN
E' possibile costruire delle finestre di popup contenenti testo. La prima riga viene considerata come titolo del popup ed il resto viene utilizzato come contenuto dello stesso. Nelle sezioni della scheda il popup viene rappresentato in piano, mentre nel componente _3_Browser appare in finestra separata.

## Rappresentazione popup
### Esempi
Titolo del popup
Contenuto del popup stesso

Sintassi : 
 :  : INT Titolo del popup
Contenuto del popup stesso
 :  : FIN

# Salto pagina
Esiste la possibilità di forzare il salto pagina in qualunque punto del testo. Questa specifica avrà efficacia nei documenti PDF : 
.. :  : **NPG**
Sintassi : 
 :  : NPG Nuova pagina

# Formattazione testo inline
Per **formattazione inline** si intende la possibilità di cambiare il formato del testo all'interno di frasi, elementi complessi come liste, tabelle, ecc...

|  Nam="Esempi di tutti i font trattati" |
| 
| .COL Cod="1" Txt="Effetto" |
| ---|----|
| 
| .COL Cod="2" Txt="Specifica" |
| _1_  Rosso   Grande    | 1 |
| _2_  Blu     Grande    | 2 |
| _3_  Verde scuro    Grande    | 3 |
| _4_  Rosa  Grande    | 4 |
| _5_  Verde chiaro Reverse    | 5 |
| _7_  Rosso              | 7 |
| >  Blu                | 8 |
| _9_  Verde scuro      | 9 |
| _B_  Rosa   | B |
| _R_  Verde chiaro| R |
| ** Sottolineato      **| u |
| ** Alta intensità    **| h |
| _  Italic             _| i |
| _r_  Rosso sottolineato| r |
| 

All'interno di un testo si può cambiare il formato del testo ponendo prima del testo oggetto del cambio una delle specifiche sopra indicate racchiuse fra _ e chiudendo la porzione di testo interessata dal cambio con la specifica n racchiusa fra _.
Quindi _queste parole saranno in italic_
Questo, a capo e **bold**

# Documenti collegati : 
- [Costruzione output PDF](Sorgenti/MB/DOC/LOCFRM)

# Specifica aggiuntiva - Le inclusioni
 :  : R01 Specifica I.INC.MBR
Permette di includere in un documento di testo un altro documento di testo. La specifica gestisce due parametri : 
 - Il parametro Fil che stabilisce in quale file è contenuto il membro di testo da includere
 - Il parametro Mem che è il nome membro da includere

### Esempio di compilazione
..I.INC.MBR Fil(DOC_OGG) Mem(P_V5STA01)

### Caratteri speciali
verifica di riga che caratteri speciali [{
[
{
"key" : "auxiliary1",
"label" : "Saldo Punti",
"value" : "%PUNTI%",
"textAlignment" : "PKTextAlignmentLeft"
},
{
}
]
