## Programma BRDI02G
Tramite questo programma è possibile importare le distinte base da un file in formato CSV (cioè
un file di testo che utilizza come separatore di colonne il carattere ';', i file sono facilmente
generabili da file Excel tramite il comando 'Salva con nome', 'Tipo file' uguale a 'CSV (delimitato
dal separatore di elenco *.csv)).
I file devono essere salvati in una cartella condivisa dell'AS400 (contenuta quindi nella cartella
di sistema QDLS).
Il programma BRDI02 può essere preso come template per importare dati in qualsiasi formato in
quanto si limita a riempire il file di lavoro B£WKDB0F (file di lavoro esteso derivato dal
file standard B£WKXT0F) riempiendo i seguenti campi : 
>BTCD01 Assieme
BTCD02 Descrizione assieme
BTCD03 Componente
BTCD04 Descrizione componente
BTQT01 Coefficiente di impiego
BTNR01 Numero progressivo
BTKEY1 = BTCD01+BTCD03+BTNR01


## Scelte a video
Il programma guida richiede a video i seguenti parametri : 
 * Cartella nella quale è contenuto il file
 * Nome del file da importare
 * Tipo distinta in cui copiare i dati
 * Formato del file CSV (per adesso sono supportati 2 formati, vedi dopo per maggiori informazioni)
 * Azione da eseguire (visualizzazione guidata, stampa (IN SVILUPPO) o esecuzione)

### Opzioni 
 * _2_Sostituzione distinte esistenti, se viene scelta questa opzione prima di elaborare un assieme viene cancellata tutta la sua distinta eventualmente presente
 * _2_Aggiornamento legami esistenti, se viene scelta questa opzione, nel caso in cui nel sistema il legame sia già esistente, esso viene sovrascritto
 * _2_Riprende anche articoli mancanti, se viene scelta questa opzione vengono scritti i legami anche se coinvolgono articoli che non esistono nel sistema

Se viene scelta la modalità di visualizzazione sarà possibile decidere la scrittura dei singoli legami (opzione WL) o di tutti i legami di un assieme (opzione WA), oltre a veder visualizzati eventuali errori quali la presenza a sistema dello stesso legame di distinta o la non esistenza di un articolo.

La visualizzazione resta limitata ad un massimo di 9800 righe.

## ESEMPIO
Come esempio si consideri una distinta cosi strutturata : 
>A01
 - A02 qta 5
 -- A04 qta 1
 - A03 qta 2


I formati supportati sono i seguenti : 
1= Cod. Assieme; Descrizione assieme; Cod. Componente; Descrizione componente; Coefficiente di impiego
Esempio
>A01;Articolo A01;A02;Articolo A02;5
A01;Articolo A01;A03;Articolo A03;2
A02;Articolo A02;A04;Articolo A04;1

2= Livello; Cod. Articolo; Descrizione articolo; Coefficiente di impiego
Esempio
>0;A01;Articolo A01
1;A02;Articolo A02;5
2;A04;Articolo A04;1
1;A03;Articolo A03;2

