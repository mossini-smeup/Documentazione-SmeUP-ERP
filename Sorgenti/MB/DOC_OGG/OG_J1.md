# Tipi di Oggetti J1

## 1) FIL_XLS
Oggetto di tipo file Excel. E' possibile da LoocUp aprire un file Excel e visualizzarlo in matrice. Cliccando sul tasto gestione file e' possibile aprire il file in Excel per
modificarlo etc...Una simulazione di questa gestione puo' essere la seguente : 

Premendo F4 dalla schermata principale di LOOCUP, compare la schermata
![OGJ101](http://localhost:3000/immagini/MBDOC_OGG-OG_J1/OGJ101.png)e compilarla con i dati Tipo=J1 e Parametro=FIL_XLS. Lasciando il terzo campo vuoto e premendo di nuovo F4 appare la classica schermata di ricerca del file di Windows. Selezionando il file e
premendo invio compare la schermata allegata, in cui sono evidenziati : 

- In Rosso la sezione con la lista dei fogli presenti nel file Excel; cliccando su una delle righe della matrice viene caricata la sezione
- In Giallo la sezione che riporta il contenuto del foglio selezionato.

Da notare in basso il tasto F06=Gestione File (in azzurro) utile per aprire il file in Excel.
![OGJ102](http://localhost:3000/immagini/MBDOC_OGG-OG_J1/OGJ102.png)Se il file Excel è protetto da password di apertura, appare la seguente finestra Messaggio : 
![OGJ103](http://localhost:3000/immagini/MBDOC_OGG-OG_J1/OGJ103.png)
## 2) FIL_EML
Oggetti di tipo file E-mail. E' possibile da LoocUp aprire un file E-mail, visualizzarne il contenuto e gestirlo. La simulazione di questa gestione e' analoga a quella
descritta precedentemente, cambia solo il tipo oggetto che diventa J1 FIL_EML.
![OGJ104](http://localhost:3000/immagini/MBDOC_OGG-OG_J1/OGJ104.png)La gestione del messaggio e' ancora in una fase molto iniziale, quindi non sara' oggetto di discussione in questa documentazione.

## 3) FIL_JPG
Oggetti di tipo immagine JPG. In modo del tutto analogo a quanto descritto precedentemente, è possibile da LOOCUP gestire dei file di immagine (con estensione JPG).

Appare la schermata
![OGJ105](http://localhost:3000/immagini/MBDOC_OGG-OG_J1/OGJ105.png)selezionando la tab Gestione Immagine e' possibile modificare l'immagine, aggiungendo un'etichetta, un rettangolo, tagliandone una porzione etc...
![OGJ106](http://localhost:3000/immagini/MBDOC_OGG-OG_J1/OGJ106.png)
## 4) STR_SQL
L' oggetto J1 di tipo Stringa SQL non e' altro che, come dice il nome stesso, una stringa SQL che quindi deve : 

rispettare le regole sintattiche dell'SQL
agire su file/tabelle esistenti e sui relativi campi

Partiamo dalla solita schermata di emulazione degli oggetti (F4 da LOOCUP) compilando i campi Tipo e Parametro con J1 e STR_SQL; Premendo nuovamente F4 si apre una finestra in cui
e' possibile inserire lo statement SQL nel formato SELECT ListaCampi, FROM File etc...










































### SVILUPPO
La lista è un codice che individua un insieme di oggetti omogenei.

Dettagli implementativi
 :  : DEC T(MB) P(DOC_OGG) K(OG_LI_D) L(1)
