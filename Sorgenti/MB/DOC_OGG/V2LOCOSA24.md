## Obiettivo
Gestire attraverso un'unico componente la gestione di una variabile di input e output.
Per ottenere il risultato è stata creato il componente A24 con il proprio servizio LOA24_SE e sviluppate schede per modello denominate LOA24_"Modello"

## Modalità di richiamo
Bisogna richiamare la scheda del modello desiderato impostando come sottoscheda il tipo di rappresentazione desiderata e i parametri desiderati.

## Modelli
### Modello A
Matrice ad un solo valore
Tipo di rappresentazione del modelllo
 :  : PAR L(TAB)
A01|Solo variabile
A02|Con intestazione della variabile in veritcale
A03|Con intestazione della variabile in orizzontale
A04|Con intestazione della variabile in orizzontale e comando di esecuzione funzione

### Modello B
Matrice con il tipo oggetto che precede il valore
Tipo di rappresentazione del modelllo
 :  : PAR L(TAB)
B01|Solo variabile
B02|Con intestazione della variabile in veritcale
B03|Con intestazione della variabile in orizzontale

### Modello C
Matrice con limiti del oggetto richiesto
Tipo di rappresentazione del modelllo
 :  : PAR L(TAB)
C01|Solo variabile, limiti in orizzontale intestati con Iniziale e Finale

### Modello D
Simile al modello B con la differenza che recepisce il parametro MOg che attiva la possibilità di modificare anche il tipo oggetto.
Tipo di rappresentazione del modelllo
 :  : PAR L(TAB)
D01|Solo variabile orizzontale
D02|Solo variabile verticale

### Modello E
Non viene utilizzata una matrice, ma un bottone per eseguire la ricerca dell'ogetto richiesto
Tipo di rappresentazione del modelllo
 :  : PAR L(TAB)
E01|Solo variabile



## Parametri
 :  : PAR L(TAB)
Parametro|Modello|Significato
Nam|Tutti|Nome della variabile Non deve eccedere i 9 "nove" caratteri.
Txt|Tutti|Intestazione
Ogg|Tutti|Oggetto
Len|Tutti|Lunghezza
Val|Tutti|Valore iniziale
Not|Tutti|Dinamismo, se separato dal carattere virgola comanda più dinamismi contemporaneamente
NoD|Tutti|Dinamismo, se separato dal carattere virgola comanda più dinamismi contemporaneamente in maniera Differita
FSz|Tutti|Dimensione del Font
Sea|Tutti|funzione A() per eseguire la ricerca utente
VEr|Tutti|Visualizza Barra dei messaggi di errore
Fun|Tutti|Funzione da eseguire, per passare le variabili racchiuse fra parentesi qudarate bisogna utilizzare il formato **(*(**Variabile**)*)**
Ctr|Tutti|Nome controllo esterno, riceve tutti i parametri
MCt|Tutti|Medodo di controllo
Con|Tutti|Contesto di persistenza - definisce una chiave per la quale viene memorizzato sia come MDE che come G00 l'ultimo valore imputato per quella chiave
Mod|Tutti|Tipo di Rappresentazione del modello
Des|Tutti|Impostando Yes si attiva la visualizzazione della descrizione
Cha|Tutti|Impostando Yes si attiva il dinamismo "Change"
MOg|D|Attiva la modifica del tipo oggetto in matrice 1=Visualizza, 2=Modificabile
Lwc|Tutti|Impostando Yes consente l'immissione di lettere minuscole
Int|D E|Impostando No non verrà emessa l'intestazione dell'oggetto
DimI|E|Dimesione in % dell'intestazione
DimB|E|Dimesione in % del bottone
DimK|E|Dimesione in % dell'oggetto
DimD|E|Dimesione in % della descrizione
StE|A escluso il 04|La stringa è intesa come comando, Verrà eseguito il servizio B£SER_26 con funzione STR.FUN e parametro Str() contenente la stringa digitata. Se il parametro è StE(Yes) esegue l'eventuale comando oppure apre la scheda del J1STR di quanto contenuto in Str(). Se il parametro è StE(OCmd)  esegue l'eventuale comando oppure non fa altro.
Exi|Tutti|Impostando Yes, anche all'usita del campo esegue una convalida dello stesso (Si comporta come se si fosse dato un invio)
|Tutti|Altri parametri possono essere utilizzati per passare valori al programma di controllo.


## Variabili
Le variabili restituite assumono il nome dichiarato e sviluppate a secondo del modello ricevuto : 
 :  : PAR L(TAB)
Nome|Significato|Mod A|Mod B|Mod C|Mod D|Mod E
S...|Intestazione|A|B|||E
T...|Tipo Oggetto||||D
P...|Parametro Oggetto||||D
O...|Tipo e parametro oggetto|A|B|C||E
...|Oggetto|A|B||D|E
...I|Oggetto Iniziale|||C
...F|Oggetto Finale|||C
D...|Descrizione|A|B||D|E
F...|Funzione|A|B|C|D


## Controllo esterno
Il controllo esterno è un servizio utente realizzato con ingresso funuzzato.
La funzione è CTR, il metodo è l'attributo MCt, riceve nell'oggetto 1 il valore della variabile ed in £FUND2 l'immagine dei parametri.
In caso di errore deve essere acceso l'indicatore £FUN35 e ritornato il messaggio di errore nella £FUND2 o attraverso i campi specifici £FUNFI e £FUNMS.



