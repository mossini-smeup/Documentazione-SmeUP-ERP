# Scheda Fasatura tabelle
Formato scheda
![B£TABE_017](http://localhost:3000/immagini/MBDOC_SCH-ST_FT/BXTABE_017.png)
## Comparazione elementi di tabella (TABELx0F)
Date 2 librerie, la scheda permette di comparare : 
 * gli elementi di un settore di tabella (ricevuto nell'oggetto 1)
 * La definizione di un settore
 * la definizione dei campi di un settore

L'impostazione delle librerie da confrontare avviene tramite il richiamo di un apposito configuratore (attivato con l'apposito bottone "F18 Configurazione")
Qualora non si siano impostate le 2 librerie da confrontare, il confronto assume il **Modello** (libreria SMEMOD e file TABELM0F) come libreria 1 e l'**ambiente** (il file TABELx in lista librerie relativo al settore da confrontare in base all'archivio di appartenenza specificato nella definizione del settore) come libreria 2.

La copia di un elemento di tabella nel modello è possibile solo impostando l'apposita password nel configuratore.

### Struttura della scheda
![B£TABE_018](http://localhost:3000/immagini/MBDOC_SCH-ST_FT/BXTABE_018.png)A destra in alto vi è una matrice con con un elenco degli elementi di tabella per il settore analizzato, suddivisi a seconda dell'esito del confronto (diversi, presenti solo nella libreria 1, presenti solo nella libreria 2 ed uguali).
A sinistra viene visualizzata una matrice con il confronto dei record dei 2 elementi di tabella, con i campi che hanno valori differenti evidenziati in rosso.
Le azioni disponibili nell'albero il basso a sinistra, variabili a seconda delle caratteristiche dell'elemento selezionato, sono : 

- Copia dell'elemento dalla libreria 1 alla libreria 2
- Copia dell'elemento dalla libreria 2 alla libreria 1
- Copia diversi dalla libreria 1 alla libreria 2
- Copia diversi dalla libreria 2 alla libreria 1
- Copia mancanti dalla libreria 1 alla libreria 2
- Copia mancanti dalla libreria 2 alla libreria 1
- Copia tutti dalla libreria 1 alla libreria 2
- Copia tutti dalla libreria 2 alla libreria 1

In caso si verifichi un errore nella copia dei record viene visualizzato in messaggio.

## Comparazione definizione settore  (TABDS00F)
Date 2 librerie, la scheda permette la comparazione della definizione di un settore di tabella.
L'impostazione delle librerie da confrontare avviene tramite il richiamo di un apposito configuratore.
Qualora la scheda non riceva come oggetto 1 un settore vengono comparati tutti i settori.
Qualora non si siano impostate le 2 librerie da confrontare, viene emesso un apposito messaggio informativo.

### Struttura della scheda
![B£TABE_019](http://localhost:3000/immagini/MBDOC_SCH-ST_FT/BXTABE_019.png)A destra in alto vi è una matrice con con un elenco dei sottosettori suddivisi a seconda dell'esito del confronto (diversi, presenti solo nella libreria 1, presenti solo nella libreria 2 ed uguali).
A sinistra viene visualizzata una matrice con il confronto dei record dei 2 sottosettori, con i campi che hanno valori differenti evidenziati in rosso.
Le azioni disponibili nell'albero il basso a sinistra, variabili a seconda delle caratteristiche del sottosettore selezionato, sono : 

- Copia del record dalla libreria 1 alla libreria 2
- Copia del record dalla libreria 2 alla libreria 1
- Copia diversi dalla libreria 1 alla libreria 2
- Copia diversi dalla libreria 2 alla libreria 1
- Copia mancanti dalla libreria 1 alla libreria 2
- Copia mancanti dalla libreria 2 alla libreria 1
- Copia tutti dalla libreria 1 alla libreria 2
- Copia tutti dalla libreria 2 alla libreria 1

In caso si verifichi un errore nella copia dei record viene visualizzato in messaggio.

## Comparazione definizione campi (TABDC00F)
La scheda permette la comparazione della definizione di un settore di tabella date 2 librerie.
La scheda permette la comparazione della definizione dei campi di un settore di tabella (ricevuto nell'oggetto 1) date 2 librerie.
L'impostazione delle librerie da confrontare avviene tramite il richiamo di un apposito configuratore.
Qualora non si siano impostate le 2 librerie da confrontare, viene emesso un apposito messaggio informativo.

### Struttura della scheda
![B£TABE_020](http://localhost:3000/immagini/MBDOC_SCH-ST_FT/BXTABE_020.png)A destra in alto vi è una matrice con con un elenco dei campi del settore suddivisi a seconda dell'esito del confronto (diversi, presenti solo nella libreria 1, presenti solo nella libreria 2 ed uguali).
A sinistra viene visualizzata una matrice con il confronto dei record dei 2 campi, con valori differenti evidenziati in rosso.
Le azioni disponibili nell'albero il basso a sinistra, variabili a seconda delle caratteristiche del campo selezionato, sono : 

- Copia del record dalla libreria 1 alla libreria 2
- Copia del record dalla libreria 2 alla libreria 1
- Copia diversi dalla libreria 1 alla libreria 2
- Copia diversi dalla libreria 2 alla libreria 1
- Copia mancanti dalla libreria 1 alla libreria 2
- Copia mancanti dalla libreria 2 alla libreria 1
- Copia tutti dalla libreria 1 alla libreria 2
- Copia tutti dalla libreria 2 alla libreria 1

In caso si verifichi un errore nella copia dei record viene visualizzato in messaggio.
