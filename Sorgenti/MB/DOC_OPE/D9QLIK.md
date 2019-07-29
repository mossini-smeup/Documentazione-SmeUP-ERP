# Lavorare con QlikView
In questo documento abbiamo riassunto le funzioni principali di QlikView per dare la possibilità anche all'utente poco esperto di navigare semplicemente attraverso i dati e poter interpretare quanto viene visualizzato.
Nella progettazione del modello standard, abbiamo diviso le informazioni presenti in fogli selezionabili attraverso label descrittive mantenendo la stessa struttura attiva su tutti i fogli.
In particolare, per meglio esprimere le selezioni e i dati, ogni foglio è suddiviso in tre sezioni principali : 

- le selezioni (lato sinistro)
- le totalizzazioni principali (in alto)
- grafici e tabelle (parte centrale)

Tutte le selezioni fatte su un foglio rimangono attive durante la navigazione, per questo motivo tutti i fogli del modello di QlikView mantengono la stessa formattazione.

![D9QLIK_06](http://localhost:3000/immagini/MBDOC_OPE-D9QLIK/D9QLIK_06.png)# Selezioni
Le selezioni ci consentono di interpretare i dati :  selezionando un qualsiasi valore di una list box, di una tabella o di un grafico, si attiva il filtro dati e tutti i grafici e le tabelle esistenti nel documento vengono di conseguenza valorizzate.

Supponendo di volere analizzare le vendite Italia - 2012 - da gennaio a marzo : 

- Nel dashboard selezionare il periodo in alto 2012.
- Selezionare il mese trascinando il periodo mensile desiderato su gennaio trascinando fino a marzo (il periodo evidenziato in verde è quello selezionato)
- Nella tabella appaiono immediatamente i dati degli anni selezionati. La selezione è valida su tutti i fogli.

Oltre agli anni si possono analizzare molte altre variabili, presenti nelle selezioni a sinistra del foglio.
Per selezionare una di queste variabili basta aprire la lista cliccando su un campo della multi box sulla sinistra e selezionare l'informazione che ci interessa. Se si vogliono selezionare più articoli contemporaneamente serve solo tenere premuto il tasto Ctrl mentre si clicca oppure se gli articoli che c'interessano sono in sequenza, tenere premuto il tasto sinistro del mouse e scorrere fino alla selezione desiderata (come funziona in Windows).
Per cancellare le selezioni è possibile agire in due modi :  attraverso il bottone Clear/Cancella presente nella barra degli strumenti, oppure cliccando nuovamente sulla selezione precedentemente effettuata.

## Casella Selezioni Correnti
Sul lato sinistro del foglio è presente una finestra all'interno della quale è possibile visualizzare tutte le selezioni attive.
![D9QLIK_07](http://localhost:3000/immagini/MBDOC_OPE-D9QLIK/D9QLIK_07.png)## Operazioni da effettuare col tasto destro e sinistro del mouse
![D9QLIK_08](http://localhost:3000/immagini/MBDOC_OPE-D9QLIK/D9QLIK_08.png)
- Select Possible/Seleziona Possibili - Prende in considerazione solo il valore selezionato.
-Select Excluded/Seleziona Esclusi - Seleziona tutti i valori evidenziati in verde escludendo quello dove si è cliccato che viene evidenziato in grigio.
- Select All/Seleziona Tutto - Evidenzia tutti i valori contenuti nella list box.
- Clear/Rimuovi - Ripulisce tutta la list box dalle eventuali selezioni effettuate in precedenza.
- Clear Other Fields/Cancella altri campi - Ripulisce tutta le altre list box dalle eventuali selezioni effettuate in precedenza; la selezione effettuata all'interno della list box resta valida ma tutte le altre selezioni nel foglio vengono annullate.
- Lock/Blocca - Blocca le celle evidenziate :  questo permette di evitare cancellature involontarie. Una volta attivato questo comando sulla selezione si può cliccare ripetutamente ma non si verificano cambiamenti.
- Unlock/Sblocca - Sblocca le celle e tutti i dati tornano a disposizione.
- Expand All Cells/Espandi Tutto - Ci consente di espandere tutte le celle, in modo da vedere tutte le possibili stratificazioni. In pratica dalle celle selezionate col segno "+" si ottengono celle con segno "-". Il segno "+" significa che esistono sottocelle, il segno "-" invece che non ci sono più sottocelle.
- Collapse All Cells/Riduci Tutto - Richiude le celle effettuando perciò dei raggruppamenti nei dati. Vengono nascoste informazioni di dettaglio prima riportate. In pratica dalle celle selezionate col segno "-" si ottengono celle con segno "+".
- Collapse Dimension Columns - Racchiude tutta la tabella solo sotto le voci della colonna.
- Print/Stampa
- Sent to Excel - Esporta la tabella in una tabella statica di un foglio Excel.
- Export - Permette di esportare la tabella in vari formati.


![D9QLIK_10](http://localhost:3000/immagini/MBDOC_OPE-D9QLIK/D9QLIK_10.png)## Cercare testi o numeri
Un'altra via per trovare i dati che ci interessano è la ricerca : 
1) scegliere la selezione cliccando sul pallino;
2) digitare la prima lettera della parola, immediatamente la list box del valore cercato si riempirà di dati inizianti con la lettera digitata. Si può anche scrivere direttamente tutta la parola, purché digitata in modo preciso.
In alternativa nelle list box si può anche schiacciare il bottone trova, indicato con una lente di ingrandimento.
3) Premere Invio per confermare le selezioni.



















### Uso del carattere "*" : 
- Come risultato di questa ricerca (A*) si ottengono tutti i dati che iniziano con "A".
- Come risultato di questa ricerca (*ia*) si ottengono tutti i dati nei quali è presente la combinazione di lettere "ia".
- Stesso procedimento avviene per la ricerca di numeri, con la piccola aggiunta di due simboli, e cioè del ">" o del "<".


## Torna indietro e vai avanti
![D9QLIK_11](http://localhost:3000/immagini/MBDOC_OPE-D9QLIK/D9QLIK_11.png)I bottoni per andare avanti o per tornare indietro si trovano sempre nella barra degli strumenti e sono indicati rispettivamente con due frecce, quella per tornare indietro rivolta verso sinistra, e quella per andare avanti rivolta verso destra. Ogni volta che questo bottone viene premuto ci consente di andare avanti o di tornare indietro per uno o più selezioni precedentemente effettuate.


## Bloccare e sbloccare selezioni
![D9QLIK_12](http://localhost:3000/immagini/MBDOC_OPE-D9QLIK/D9QLIK_12.png)Per bloccare le selezioni al fine di evitare cancellature involontarie si può usare il bottone rappresentato da un lucchetto chiuso ("blocca selezione"). Una volta attivato questo comando, la selezione è bloccata e non si può più cancellare.
Quando si sbloccare delle selezioni basta pigiare il bottone raffigurato da un lucchetto aperto ("sblocca selezione") e subito tutti i dati torneranno a disposizione.


# Creare un bookmark
![D9QLIK_13](http://localhost:3000/immagini/MBDOC_OPE-D9QLIK/D9QLIK_13.png)Creare dei bookmark (preferiti/segnalibri) significa salvare le selezioni effettuate all'interno del documento per un utilizzo successivo. I bookmark possono essere anche condivisi fra i diversi utenti.
Per creare un bookmark serve : 
- selezionare uno o più valori;
![D9QLIK_14](http://localhost:3000/immagini/MBDOC_OPE-D9QLIK/D9QLIK_14.png)- cliccare sull'icona, sopra la barra dei tab, raffigurante una stella ("crea bookmark");
- inserire il nome che si vuole dare al bookmark e premere Invio.

Le nostre selezioni verranno così salvate e potremmo farne uso successivamente.
Per riaprire un bookmark basta cliccare sulla freccia "-Select Bookmarks -" e apparirà un elenco a tendina dove è possibile scegliere il bookmark.
Per cancellare invece un bookmark è necessario premere il bottone a forma di stella ("cancella bookmark") e scegliere quale segnalibro cancellare.

# Grafici e Tabelle
Sui grafici si possono effettuare selezioni in modo da visualizzare in dettaglio solo alcuni dati; per fare ciò basta tenere premuto il tasto sinistro del mouse e scorrere finché tutti i dati che ci interessano saranno evidenziati in verde.
![D9QLIK_16](http://localhost:3000/immagini/MBDOC_OPE-D9QLIK/D9QLIK_16.png)I grafici e le tabelle possono anche esportati anche in Excel o direttamente stampati attraverso i bottoni presenti sull'intestazione della finestra.
![D9QLIK_15](http://localhost:3000/immagini/MBDOC_OPE-D9QLIK/D9QLIK_15.png)
