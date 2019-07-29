# Documentazione
La scheda permette di gestire il Clipboard del sistema operativo.
La Clipboard è il deposito di quanto viene copiato/tagliato all'interno del sistema operativo.
Al momento è supportato solo il Copia
Le cose che è possibile copiare sono : 

- Stringhe
- File
- Liste di file
- Immagini


## Il Menù di sinistra
Una volta aperta la scheda (OGBASE_CLP), a sinistra è presente il menù.
Il menù è sensibile al contesto per cui viene richiamato : 

- Se la scheda è richiamata da "Gestire Incolla" su un Oggetto il menù farà riferimento a tale Oggetto
- Il menù è sensibile al tipo oggetto copiato : 
-- a seconda che si tratti di Stringa, File, Lista File, Immagine si presenterà con voci di menù alternative


## La parte di destra
A seconda del menù selezionato a destra sarà possibile : 

- Gestire il file in quanto oggetto J1 PATHFILE
- Gestire l'immagine (intesa come selezione di immagine o file PNG) come Immagine di Oggetto tramite la scheda standard di gestione immagine dell'oggetto
- Gestire il file (inteso come qalunque file non PNG) come documento per un Oggetto tramite la scheda standard di gestione dei files dell'oggetto
- La lista di file per ora non è supportata, quindi verrà mostrato solamente la stringa contenente la lista dei files.

