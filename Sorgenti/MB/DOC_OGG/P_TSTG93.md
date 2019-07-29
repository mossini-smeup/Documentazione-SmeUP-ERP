# INTRODUZIONE
Tra gli oggetti trattati dalle matrice, c'è la cella grafica (tipo J4, parametro BAR) che permette di visualizzare varie forme (triangoli, cerchi, barre, linee verticali, ecc..).
La sintassi, per la definizione, è semplice ma molto specifica e per questo è stata creata una /COPY (di seguito trattata in dettaglio) che ne semplifica la composizione.

# SINTASSI
## I SEPARATORI
 T(In definitiva si tratta di una stringa con diversi separatori : )
- \\ separa una informazione nella definizione di un elemento/barra da una altra informazione relativa allo stesso elemento/barra.
- \\AND\\ separa la definizione di una barra da quella di una altra barra all'interno della stessa cella J4BAR.

I separatori si limitano a delimitare dei marcatori in questo modo : 
 :  : PAR
[Marcatore 1]\\[Marcatore 2]\\AND\\[Marcatore 3]\\[Marcatore 4].

 T(L'esempio sopra riportato indica la presenza di due barre all'interno della stessa cella : )
- [Marcatore 1]\\[Marcatore 2]
- [Marcatore 3]\\[Marcatore 4]

 entrambe con due marcatori ognuna.

## I MARCATORI
I marcatori definiscono i diversi aspetti del singolo elemento/barra che fa parte della cella.
Vengono indicati tramite una copia di attributi : 

[Nome];[Valore]


Ad eccezione del marcatore BCOLOR, che ha significato globale per tutta la cella e che quindi dovrebbe essere specificato una volta sola, tutti i marcatori possono essere ripetuti una volta per ogni elemento che compone la cella.
 T(I marcatori possibili sono i seguenti : )
- BCOLOR :  Indica il colore di sfondo dell'intera cella. Accetta come valori solo un colore con sintassi RGB (es :  R200G011B123).
- SHAPE :  Indica la forma da utilizzare nell'elemento. I valori accettati sono i seguenti : 
  -- CIRCLE :  L'elemento da disegnare sarà un cerchio.
  -- TRIL :  L'elemento da disegnare sarà un triangolo isoscele con la punta rivolta verso sinistra.
  -- TRIR :  L'elemento da disegnare sarà un triangolo isoscele con la punta rivolta verso destra.
  -- BAR o assenza del marcatore :  L'elemento da disegnare sarà una barra rettangolare.
- HEIGHT :  Indica le altezze delle componenti dell'elemento. I valori ammessi sono numeri interi (0-100) separati da ;.
- Coppia Colore;Percentuale :  Indicano i dati veri e propri. Il colore è definito in RGB e la percentuale è un intero.


 T(N.B :  la percentuale è espressa con coordinata relativa e viene intesa diversamente in funzione della shape definita, come segue : )
- Barra :  è la percentuale di lughezza occupata dalla singola barra nella cella, posizionata a partire dalla precedente.
- Cerchio :  indica il punto del centro del cerchio come coordinata relativa alla precedente.
- Triangoli :  come per la barra. Il vertice è posizionato a metà dell'altezza dell'elemento.

Il colore può avere valore speciale *NONE. In questo caso nello spazio occupato dall'elemento non sarà visualizzata alcuna forma.

Come marcatore è anche possibile utilizzare un "separatore". Ogni separatore è un marcatore particolare con le sue regole speciali indicato tramite la sintassi tipo;percentuale;colore(opzionale);spessore(in pixel opzionale);altezza(in percertuale opzionale).
 T(Esistono i seguenti separatori : )
- SEP :  Disegna un separatore verticale (linea) nella posizione relativa definita da percentuale. Se definito lo spessore la linea avrà larghezza come da definizione. Se definita l'altezza, la linea sarà alta in percentuale rispetto alla altezza della cella. In caso contrario sarà alta come la cella.
- DIV :  Come SEP, ma ignora altezza e spessore.
- ARW :  Disegna una freccia, centrata nel punto definito da percentuale e la punta rivolta verso l'alto.
- GRID :  Disegna una griglia (tipo righello), dividendo la cella in tanti "tick" quanti indicati dal campo percentuale. Con "tick" s'intendo appunto i marcatori dei righelli.


## ESEMPI
"R100G200B002;50,4\\SEP;80,00;R255G000B000;2\\R255G150B000;98,00"
"SHAPE;CIRCLE\\*R000G200B000;33,3\\R255G255B051;66,5\\R220G00B00;100,0"

# LA /COPY
Per semplificare la composizione della stringa XML che esegue tali funzioni, è stata realizzata la routine £G93, che riceve in input le informazioni elementari, esegue le elaborazioni opportune (determinazione della scala, ec..) e torna la stringa £G93 che va semplicemente trimmata, ed n si tocchino verticalmente.
aggiunta alla stringa £JaxCP, nella colonna opportuna.

Vi sono tre tipi di oggetti grafici
- di cella elementari
- di cella composti
- di colonna
Il primo tipo si risolve in una singola chiamata, il secondo in più chiamate per comporre una cella, il terzo in più chiamate per comporre tutte le celle di una colonna.
Per quest'ultimo è quindi necessario che la routine conservi memoria tra un richiamo e l'altro.
A tale scopo sono state realizzate più repliche :  ad ogni richiamo si deve comunicare l'identificativo della replica.
Si consiglia di tenere la versione base per gli oggetti di cella (sia elementari sia composti) ed una replica per ogni colonna.
Sono state implementate 10 repliche, quindi è possibile presentare, in una matrice, fino ad un massimo di 10 colonne.
Per superarlo sarà sufficiente aggiungere ulteriori repliche a B£G93G.


# MODALITA' DI RICHIAMO
Tutti i campi di input sono puliti in uscita e tutti quelli di output sono puliti in ingresso.


## OGGETTI DI CELLA ELEMENTARI
Quando si deve disegnare in una cella un singolo oggetto, è sufficiente un unico richiamo alla routine £G93.
Celle diverse della stessa colonna possono contenere forme diverse :  non vi è "memoria" tra due richiami successivi per valorizzare la stessa cella.
I campi di input sono i seguenti : 
### £G93FU Funzione
Impostare 'WRI'
### £G93I01 Numero campo
Si consiglia di lasciare vuoto questo campo.
### £G93I02 Forma da disegnare
Riferirsi alla COPY £G93DS per l'elenco dei valori possibili.
NB :  queste informazioni sono presenti nel sorgente della /copy, non nella sua documentazione.
 :  : DEC T(MB) P(QILEGEN) K(£G93DS) L(1)
Non va scelta la forma linea (riservata per i casi successivi).
La forma vuota serve quando si vuol riempire solo lo sfondo. Ad esempio, se in una colonna si imposta un colore di sfondo (nel modo che sarà esposto nel seguito) e, solo in alcuni casi, si vuol disegnare un triangolo, quando non lo si disegna si vuole comunque riempire lo sfondo per continuità verticale :  in questo caso si imposta la forma vuota.
### Colore
Il colore di riempimento della forma viene determinato con questa risalita
. Valore RGB in £G93I20.
E' possibile inserire il codice *NONE che ha il significato di "trasparente", vale a dire che assume il colore dello sfondo. Può essere utile, tra l'altro, in caso di cella composta (strudel o scritture in ADD), per saltare alcune fette.
. Se assente :  Numero colore di £ATR in £G93I03
. Se assente :  Numero colore 16 (grigio)
Questo campo non è significativo per la forma semaforo.
Talvolta può interessare che
### Colore sfondo 
Il colore dello sfondo viene determinato con questa risalita
. Valore RGB in £G93I21
. Se assente :  Numero colore di £ATR in £G93I05
. Se assente :  si lascia bianco.
Non è significativo il colore *NONE.
### £G93I04 Luce semaforo
Par la forma semaforo, si impostano in qusto campo le luci da accendere.
Riferirsi alla COPY £G93DS per l'elenco dei valori possibili.
NB :  queste informazioni sono presenti nel sorgente della /copy, non nella sua documentazione.
NB :  queste informazioni sono presenti nel sorgente della /copy, non nella sua documentazione.
 :  : DEC T(MB) P(QILEGEN) K(£G93DS) L(1)

## OGGETTO CELLA LIVELLO
Un particolare oggetto elementare è il livello :  viene disegnata una linea il base a numeri ricevuti : 
- livello di partenza in £G93I10
- livello di arrivo in £G93I13
- livello massimo in £G93I26.
La cella viene divisa in un numero di celle pari al livello massimo.
Se si imposta solo il livello di parteza si riempie la cella corrispondente.
Se si imposta solo il livello di arrivo si riempiono le celle dalla prima a quella corrispondente al livello di arrivo.
Se si impostano entrambe le celle, si riempiono le celle da quella corrispondente al livello di partenza a quello corrispondente al livello di arrivo.
Dato che questo oggetto in realtà è uno strudel automatico (lo strudel, un tipo oggetto di cella composto, verrà descritto nel seguito), sono attive le sue formattazioni :  % di spazio a sinistra e a destra (£G93I06 e £G96I07) e altezza della colonna (£G96I08), che vanno passate nella funzione WRI.
Per quanto riguarda il colore delle singole celle, se viene passato il codice (come RGB in £G93I20 o come £ATR in  £G93I02) tutte le celle vengono riempite con questo colore :  se invece il si lascia vuoti, esse vengono riempite con una gradazione crescente di colori, in modo che la ennesima cella venga riempita sempre con lo stesso colore.
E' possibile inoltre impostare che vengano alternati due colori (il primo per le posizoni dispari e il secondo per quelle pari).
Devono essere impostai sia il colore 1 (£G93I03, £ATR oppure £G93I20, RGB) sia il colore 2 (£G93I27, £ATR oppure £G93I28, RGB).

## OGGETTI DI CELLA COMPOSTI
Questa forma permettere di disegnare una serie di linee nella stessa cella.
L'utilizzo implementato è lo "strudel" vale a dire una torta rettangolare, in cui il colore delle singole fette è proporzionale ai valori passati.
Si devono quindi eseguire più richiami, ma tutti all'interno della costruzione della stessa cella.
Quindi anche in questo caso non va conservata memoria in richiami successivi per la stessa cella in righe diverse.
Essa potrebbe contenere forme eterogenee :  in una riga un semaforo, in qella successiva uno strudel.

### _2_RICHIAMO IN INIZIALIZZAZIONE
All'inizio di ogni cella, va comunicato che si vuole comporre una nuova stringa
### £G93FU Funzione
Impostare 'INZ'
### £G93I01 Numero campo
Si consiglia di lasciare vuoto questo campo.
### £G93I02 Forma da disegnare
Va scelta la forma '05' (linea)
### % Spazio
Si può impostare la percentuale di spazio da lasciare a sinistra (£G93I06) e a destra (£G93I07) rispetto al bordi della cella (valore da 1 a 99) :  se la somma supera 100 vengono entrambi azzerati.
### £G93I08 Strudel ad altezza variabile
E' significativo solo in disegno dello strudel :  impostare un valore positivo (ad esempio 1) per comunicare che lo strudel sarà ad altezza variabile.
### £G93I09 Tipo di linea
Si imposta il valore '6' (strudel)

### _2_RICHIAMO IN IMPOSTAZIONE SCALA
Viene lanciata per ogni numero in cui suddivider la linea.
Ad esempio, se si passano i numeri 23, 40 10 e 3 (ciascuno con un colore diverso) verranno disegnate le seguenti linee : 
(al netto degi spazi agli estremi)
23 / (23+40+10+3)= 30 %
(23+40) / (23+40+10+3)= 86 %
(23+40+10) / 23+40+10+3)= 96 %
(23+40+10+3) / (23+40+10+3)= 100 %
### £G93FU Funzione
Impostare 'SCA'
### £G93I08 Altezza strudel
E' significativo in caso dello strudel, quando è stato passato un valore, in questo stesso campo, nella funzione INZ, per comunicare che lo strudel è ad altezza variabile.
Si può impostare un numero da 1 a 99, che riduce percentualmente l'altezza della linea, per la fetta che si sta pssando.
E' possibile azzerare l'altezza di una fetta impostando il colore *NONE, che rende questa fetta trasmarente :  mentre non va impostata l'altezza a zero, in quanto il client in questo caso la porterebbe a 100.
### £G93I10 Numero da riportare
### Colore
E' il colore con cui verrà riempita la linea fino al numero precedente.
Per le risalite riferirsi a quanto esposto per la cella elementare

### _2_RICHIAMO IN SCRITTURA
Quando sono stati passati tutti i numeri si deve chiedere alla routine di ritornare la stringa £G93SR che verrà trimmata nella £JaxCP.
### £G93FU Funzione
Impostare 'WRI'
### Colore sfondo
Per le risalite riferirsi a quanto esposto per la cella elementare
### £G93I08 Altezza linea
Si può impostare un nmuero da 1 a 99, che riduce percentualmente l'altezza della linea.
NB :  TUTTO lo strudel viene ridotto.
Se attivata la presentazione dello strudel ad altezza variabile, questo campo viene trascurato.



## OGGETTI DI COLONNA
In questo caso, in ogni colonna si disegna un grafico diverso, quindi deve essere riservato un numero di campo (£G93I01) diverso per ciascuna di esse, che va impostato prima di tutti i richiami di questo tipo. Cià ha l'effetto di richiamare una versione specifica del programma, che quindi possiede le proprie aree di memoria riservate (valori minimo e massimo, scale, ecc...).

### _2_RICHIAMO IN INIZIALIZZAZIONE
Va eseguito all'inizio della costruzione della matrice, per ogni colonna grafica
### £G93FU Funzione
Impostare 'INZ'
### £G93I02 Forma da disegnare
Va scelta la forma '05' (linea)
### £G93I09 Tipo di linea
Si imposta un valore da '' a '5'
Riferirsi alla COPY £G93DS per l'elenco dei valori possibili.
NB :  queste informazioni sono presenti nel sorgente della /copy, non nella sua documentazione.
 :  : DEC T(MB) P(QILEGEN) K(£G93DS) L(1)
Le linee disegnate sono le seguenti : 

**Numero**
La scala va dal numero più basso (se maggiore di zero si assume zero) al numero più alto (se minore di zero si assume zero).
Se si forza (in questo richiamo di inizializzazione) la risoluzione massima, nel campo £G93I23, la scala va dal valore minimo a quello massimo.
Viene disegnata una linea a partire dall'origine, a sinistra per i numeri negativi e a destra per quelli positivi.
Nel caso di forzatura della risoluzione massima, se tutti i vallri sono positivi si parte dal valore minimo, se sono negativi si parte dal valore massimo.

**Intervallo di numeri**
La scala va dal'estremo inferiore più basso (se maggiore di zero si assume zero) all'estreno superiore più alto (se minore di zero si assume zero).
Se si forza (in questo richiamo di inizalizzazione) la risoluzione massima, nel campo £G93I23, la scala va dall'estremo inferiore a quello superiore.
Viene disegnata una linea per ogni intervallo, dall'estremo inferiore a  quello superiore.

**Data o istante**
L'istante è definito da una coppia di numeri :  data e istante (oggetto I1 di tipo 1).
La scala va dalla data (o istante) più bassa a quella più alta.
Viene disegnata una linea a partire dalla data (o istante) più bassa, fino al valore da rappresentare.

**Intervallo di date o istanti**
La scala va dal'estremo inferiore più basso all'estremo superiore più alto.
Viene disegnata una linea per ogni intervallo, dall'estremo inferiore a  quello superiore.

Nel caso di valori tutti uguali di numeri date o istanti, viene disegnata una linea al 50 % dello spazio utile.

### Valori della linea. Metodo £G93ME 'SCA'
E' possibile impostare in inizializzazione gli estremi della scala, se sono noti oppure se li si vuole prefissare indipendentemente dai valori effettivi (in questo caso eventuali valori esterni verranno troncati agli estremi e ne verrà data segnalazione tra i parametri di ritorno.
Nel caso di numeri o intervalli di numeri si devonmo riempire i valori £G93I10 e £G93I3.
Nel caso di date  o intervalli di date si devonmo riempire i valori £G93I11 e £G93I4
Nel caso di istanti o intervalli di istanti si devonmo riempire i valori £G93I11, £G93I12, £G93I4, £G93I15.
Non è indispensabile fornire i valori in ordine crescente
### % Spazio
Riferirsi a quanto esposto per la cella composta
### £G93I16 Applicazione % di spazio agli estremi
Permette di correggere l'agggiunta degli spazi agli estremi, nel caso di numeri sempre dello stesso segno.
Riferirsi alla COPY £G93DS per l'elenco dei valori possibili.
NB :  queste informazioni sono presenti nel sorgente della /copy, non nella sua documentazione.
 :  : DEC T(MB) P(QILEGEN) K(£G93DS) L(1)
### £G93I17 Aggiunta asse Y
E' possibile decidere se disegnare l'asse Y, che assume la seguente posizione
- se numero o intervallo di numeri è l'origine; in presenza della forzatura della massima risoluzione, se tutti i valori
sono positivi è l'estremo inferiore, se tutti negativi è l'estremo superiore, se misti resla l'origine.
- se data, istante, o intervallo di date o istanti è l'estremo inferiore. In questo caso è significativo se è stata
impostata una % di spazio a sinistra.
Con questo parametro si può decidere se disegnare l'asse Y.
Riferirsi alla COPY £G93DS per l'elenco dei valori possibili.
NB :  queste informazioni sono presenti nel sorgente della /copy, non nella sua documentazione.
 :  : DEC T(MB) P(QILEGEN) K(£G93DS) L(1)
### Caratteristiche asse Y
Si può impostare la largehzza in pixel dell'asse Y (£G93I18) default 1, ed il suo colore (£G18I19) default grigio
(colore 19 di £ATR).
### £G93I22 Sfondo alternato
Se non è stato impostato esplicitamente uno sfondo (in scrittura), impostando questo parametro lo sfondo viene riempito a righe alternate (con il valore £ATR 19), in modo da ottenere un effetto di lettura facilitata.
### £G93I25 Tipo griglia
Impostando il valore '01', nel caso di date, istanti, intervalli di date e di istanti, viene disegnata una linea verticale ad ogni cambio di giorno.
Impostando il valore '02', nel caso di una cella che rappresenta un giorno (estremi di scala 0 - 24), viene riportata una griglia che riporta le ore, ad altezza variabile per migliorare la lettura.
Attenzione :  la routine **NON** controlla il fatto che la cella rappresenti effettivamente un giorno.

### _2_RICHIAMO IN IMPOSTAZIONE SCALA
Qualora non siano stati passati in inizializzazione, è possibile passare tutti i valori da riportare, ciascuno con un richiamo alla routine.
### £G93FU Funzione
Impostare 'SCA'
### Valori
In funzione del tipo di linea, si pasaa il valore (o i valori, in caso di intervalli o istanti) nei campi specifici.
Nel caso di numeri si deve riempire il valore £G93I10.
Nel caso di intervalli di numeri si devonmo riempire i valori £G93I10 e £G93I3.
Nel caso di date si deve riempire il valore £G93I11.
Nel caso di intervalli di date si devonmo riempire i valori £G93I11 e £G93I4
Nel caso di istanti si devonmo riempire i valori £G93I11 e £G93I12.
Nel caso di intervalli di istanti devonmo riempire i valori £G93I11, £G93I12 (istante iniziale)
e £G93I4, £G93I15 (istante finale).
Nel caso di intervalli non è indispensabile fornire i valori in ordine crescente.
Questi valori, nella definizione della scala, vengono confrontati con quelli eventalmente forniti in inizializzazione.

### _2_RICHIAMO IN SCRITTURA
Ad ogni scrittura di riga si debe richiamare la funzione, passando il valore da presentare, e ricevendo la stringa £G93SR che verrà trimmata nella £JaxCP.
### £G93FU Funzione
Impostare 'WRI'
### Colore sfondo
Per le risalite riferirsi a quanto esposto per la cella elementare
### Valori
Riferirsi a quanto esposto nel richiamo in impostazione scala
### £G93I08 Altezza linea
Riferirsi a quanto esposto nel richiamo in scrittura cella composta

### _2_RICHIAMO IN SCRITTURA IN ADD
E' possibile disegnare più oggetti dello stesso tipo nella stessa cella.
In tal caso, si utilizza il metodo 'ADD' per i richiami successivi al primo, che non pulisce la stringa di output £G93RI ma la ritorna aggiornata con il valore.
Alcune impostazioni (l'altezza e lo sfondo) sono sentite nel primo richiamo (con metodo vuoto), mentre altre (il colore) sono valide per tutti i richiami.
Va tenuto presente che i valori passati devono essere progressivi ed assoluti. Ciò distingue questa modalità di richiamo dallo strudel. Se i valori successivi sono inferiori ai precedenti vengono trascurati.
Ad esempio, se si eseguono questi richiami (con tipo linea numero e valore massimo 10)
WRI -  -  2 - colore rosso
WRI - ADD - 4 - colore giallo
WRI - ADD - 6  - colore blu
si ha l'effetto di una linea riempita per il primo 20 %  in rosso, dal 20 % al 40 % in giallo, dal 40 % al 60 % in blu, e la parte rimanente vuota.
Lo stesso effetto si ha con gli inervalli :  l'eventuale sovrapposizione, anche parziale, viene trascurata.


### _2_VALORI DI RITORNO
Dopo ogni richiamo in scrittura di oggetti di colonna, vengono ritornati i seguenti valori : 
£G93O01 :  Valore della scala, in numeri, giorni o istanti
£G93O02 :  Flag se il valore è un estremo. Riferirsi alla COPY £G93DS per l'elenco dei valori ritornati.
NB :  queste informazioni sono presenti nel sorgente della /copy, non nella sua documentazione.
 :  : DEC T(MB) P(QILEGEN) K(£G93DS) L(1)
£G93O03 - £G93O04 :  Valore minimo e massimo dell'intera colonna (se numero o intervallo di numeri)
£G93O05 - £G93O06 :  Data minima e massima dell'intera colonna (se data, istante, o intervallo di date o istanti)
£G93O07 - £G93O08 :  Istante minimo e massimo dell'intera colonna (se istante o intervallo di istannti)
£G93O09 - Flag se riga con sfondo. Viene tornato se è stato impostato lo sfondo alternato. Può essere utile per riempire, in questo caso, altre celle grafiche con lo stesso sfondo, dando un effetto di continuità.
£G93O10 - Torna '1' se valore inferiore al minimo. Può accadere quando la scala è stata forzata.
£G93O11 - Torna '1' se valore superiore al massimo. Può accadere quando la scala è stata forzata.


# SOVRAPPOSIZIONE
E' possibile sovrapporre due celle grafiche passando all'XML l'unione dei due campi nel seguente modo : 
%TRIM(XXG93SR1)+'\\AND\\'+%TRIM(XXG93SR1)
Dove XXG93SR1 e XXG93SR2 sono, rispettivamente, i risultati dei due £G93 che si vogliono fondere.
NB :  il secondo risultato copre il primo nelle parti in cui è riempito.
Bisogna distinguere tra le parti vuote del secondo, che non si sovrappongono al primo, e le parti riempite con il colore "trasperente" che si sovrappongono.



# GRIGLIE "PERSONALI" DI N ELEMENTI
Attualmente è possibile costruire una griglia a giorni o a ore (se cella di un giorno).
Il seguente è un "trucco" per ottenere una griglia a N suddivisioni qualsiasi.
Il modo è di costruire una cella vuota con una griglia di N giorni, e concatenare il risultato alla cella grafica.
Il modo di ottenere le N suddivisioni è di impostare come estremi due date che differiscono di N giorni. Ad esempio, se si vuol ottenere una griglia di 4 suddivisioni, si impostano le due date estreme con, ad esempio 20150101 e 20150105 (che differiscono di 4 giorni).
Il seguente è il codice con cui si ottiene questo risultato.

>C                   CLEAR                   £G93DI
C                   EVAL      £G93FU='INZ'
C                   EVAL      £G93ME='SCA'
C                   EVAL      £G93I01=''
C**  Forma linea - Linea
C                   EVAL      £G93I02='05'
C**  Tipo linea - Intervallo di date
C                   EVAL      £G93I09='4'
C** Inizio e fine intervallo :  la griglia costruita sarà di 3 elementi
C                   EVAL      £G93I11=20150101
C                   EVAL      £G93I14=20150104
C** Tipo griglia - Fissa in giorni
C                   EVAL      £G93I25='01'
C** Colore asse Y (in questo esempio è nero)
C                   EVAL      £G93I19=18
C** spazi (devono essere gli stessi del richiamo della cella)
C                   EVAL      £G93I06=2
C                   EVAL      £G93I07=2
C                   EXSR      £G93
C**
C                   EVAL      £G93FU='WRI'
C                   EVAL      £G93ME=''
C                   EXSR      £G93
C** il campo XG93SR (definito *LIKE di £G93SR) va concatenato a quest'ultimo
C                   EVAL      XG93SR=£G93SR


e concatenara ogni £G93SR con quello ottenuto con il precedente richiamo.


# NOTE GENERALI

## LARGHEZZA COLONNA
La larghezza delle colonne di una matrice viene determinata altomaticamente dal Client.
L'unica eccezione è la cella grafica, in cui il valore impostato nella griglia assume il significato di "Numero di unità grafiche". Per avere una risoluzione più alta questo valore va aumentato.
Per gli oggetti elementari, tuttavia, questa larghezza è opportuno sia fissa.
Riferirsi alla COPY £G93DS per i valori consiglati per i singoli oggetti grafici.
NB :  queste informazioni sono presenti nel sorgente della /copy, non nella sua documentazione.
 :  : DEC T(MB) P(QILEGEN) K(£G93DS) L(1)
E' in sviluppo l'impostazione della larghezza della colonna direttamente da questa routine.

# CONSIDERAZIONI ESTETICHE
In caso di diagrammi di GANTT
impostare % di spazi ai bordi, in modo da dare un senso di continuità diagonale.
In caso di disegno di altre linee è invece preferibile ridurre l'altezza, in modo che le linee non si tocchino verticalmente.
In diagrammi di numeri è preferibile che, se positivi, non tocchino il bordo di destra, se negativi il bordo di sinistra, se a farfalla entrambi.
L'applicazione della % di spazio agli estremi 'appoggiata' riflette questa considerazione.

# MODALITA' DI TEST
Questa /COPY non può essere simulata con un normale programma di test, in quanto il suo output deve essere grafico.
La visualizzazione della stringa risultante (£G93SR) non è sufficientemente significativa.
Per questo motivo è stata realizzata una scheda di test, richiamabile dalla scheda della /COPY.
In essa sono presesnti due script, la cui esecuzione lancia richiami multipli alla routine e, nella  matrice del risulato, presenta le celle grafiche ottenute.
Gli script, contenuti in SCP_SET di SMEDEV sono : 
. SMA_G93_01, che contiene gli esempi base e verrà aggiornato dallo sviluppo.
. SMA_G93_02, in cui si possono inserire le proprie prove.
La sintassi di questi script è la seguente : 
TAG ;;SIM.G93
Gli attributi sonno i parametri di input della routine.
Ogni riga contienme un richiamo con funzione, metodo, e attributi opportuni.
L'attributo "Significato" (Txt) fa da intestazione di ogni numvo esempio, e da separazione tra due esempi diversi.
Viene scritta una riga per ogni funzione 'WRI' a meno che si stato esplicitamente impedito, impostando l'attributo "Escluso da stampa" (Esc) a '1'. In questo modo si simula la scrittura in ADD, valorizzando questo attributo su tutte le esecuzioni in WRI, tranne l'ultima.

Nella riga della matrice, oltre alla cella grafica, sono riportati i campi di output, compresa la stringa £G93SR, che è il campo passato effettivamente alla £JaxCP.
