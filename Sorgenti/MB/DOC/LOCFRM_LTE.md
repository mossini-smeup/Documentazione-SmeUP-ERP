# La produzione dei pdf
Il processo produzione del file PDF è suddiviso in due fasi : 

- conversione del file membro di documentazione attiva in formato LaTeX;
- generazione del file PDF grazie all'utilizzo del motore MikTeX ( non incluso nella versione standard di Loocup).


Analizziamo in dettaglio cosa succede quando richiedo la stampa di un documento : 
 - Su AS400 viene letto il membro indicato e risolte le eventuali inclusioni
 - Su AS400 viene convertito nel formato Tex
 - Viene restituito a Loocup e dato in pasto al componente FRO
 - Vengono creati dei file temporanei nella cartella LOOCUP_OUT\LTX presente nella cartella di installazione di Loocup,
 - Viene richiamato MikTex 2 volte chiedendo per prima cosa la generazione dell'indice e poi la generazione del documento PDF
 - Vengono cancellati i file temporanei (a meno che non venga specificato il contrario)

La conversione da formato Tex in Pdf avviene in due fasi :  nella prima viene generato l'indice, nella seconda il documento comprensivo di contenuto e indice.

NOTE : 
Se non specifico il nome del file PDF, viene creato un file il cui nome è il timestamp. Il file viene generato nella cartella  LOOCUP_OUT\LTX.
Nella stessa cartella troveranno posto i file Tex utilizzati per la generazione del PDF.

L'utilizzo del componente **LaTeX/PDF** prevede l'installazione dei seguenti programmi : 

- MikTeX (versione 2.8), è il generatore dei pdf, obbligatorio
- TEXnicCenter, è un editor di Tex, opzionale
- WinEdt (versione 5.6), è un editor di Tex, opzionale in alternativa a TEXnicCenter.


# MikTeX (versione 2.8)
MikTeX è una distribuzione di TeX/LaTeX opensource per Microsoft Windows. Il software permette la compilazione dei file TeX per la generazione di PDF e/o DVI.
L'installazione del software è **obbligatoria** per un corretto utilizzo del componente e per la generazione dei file PDF.
Per l'installazione è necessaria una connessione internet.

 :  : R01 Nota :  i linguaggi
Per una corretta generazione dei file PDF è **necessario** avere la lingua "italiano" tra le opzioni di lingua del programma. La mancata impostazione potrebbe comportare errori di vario genere (ad esempio errori nella sillabazione per i ritorni a capo delle parole...).

In un'installazione standard la lingua "italiano" è già correttamente installata.
Nel caso non lo fosse, è possibile impostarla tra le varie opzioni nel seguente modo : 

- dalla barra delle applicazioni di Windows premere
  "start" -> tutti i programmi -> MikTeX 2.7 -> settings
- selezionare la scheda "Languages"
- spuntare la voce "italian"
- premere "OK" e confermare l'operazione


![LOCFRM_038](http://localhost:3000/immagini/LOCFRM_LTE/LOCFRM_038.png)
 :  : R01 Nota :  i pacchetti aggiuntivi
Durante le prime generazioni dei file PDF sarà richiesta l'installazione di package (pacchetti) aggiuntivi. Per un corretto funzionamento del programma è necessario confermare l'installazione.
A seguito della conferma i pacchetti verranno scaricati ed installati automaticamente.

E' possibile installare i package manualmente nel seguente modo : 

- dalla barra delle applicazioni di Windows premere
  "start" -> tutti i programmi -> MikTeX -> Maintenance -> MiKTeK settings
- selezionare la scheda "packages"
- spuntare il pacchetto desiderato
- premere "OK" e confermare l'installazione


![LOCFRM_039](http://localhost:3000/immagini/LOCFRM_LTE/LOCFRM_039.png)
E' possibile ricercare il package desiderato aprendo lo "start package manager", in cui sono elencati tutti i pacchetti disponibili dal repository (archivio).

 :  : R01 Installazione MikTeX
E' possibile installare MikTeX seguendo il percorso : 
http://miktex.org/download

# la gestione degli errori
La soluzione di un errore è molto semplificata se viene installato un editor di Tex.

Gli errori più comuni sono : 
 - Tabella con un numero di colonne inferiore al numero di celle :  è sufficiente ad esempio aggiungere un | dopo l'ultimo valore inserito.
 - Presenza di un carattere non gestito. La soluzione di questo errore potrebbe essere piuttosto complessa quando si stampano book corposi. E' necessario stampari i documenti uno per volta, fino ad identificare quello che produce l'errore. Una volta identificato il documento, nella scheda  "set and play", del documento, è possibile visualizzare il sorgente LaTeX generato selezionando la scheda "Formattazione LaTeX". Va copiato questo testo nell'editor di Tex e provare a compilarlo.
 - Immagini senza riferimento :  se nel riferimento di un'immagine trovo in ? significa che l'ID del riferimento è diverso dall'ID dell'immagine. Verificare le corrispondenze
 - Se trovo ?? nel riferimento di una figura potrebbe essere dovuto al fatto che il motore di conversione non è riuscito a creare l'indice.

NOTA : 
Il riferimento ad un'immagine inserisce la dicitura "vedi fig. xxx". Questa frase è cablata nella conversione.

# I messaggi di compilazione
Compilando un documento può capitare che pur non essendo presenti errori venga segnalato che ci sono dei Bad Box :  questo significa che le aree di stampa sono più grandi del documento. Questo messaggio non costituisce però un problema.

Nota :  C'è un file di Log???

# WinEdt (versione 5.6)
WinEdt è un editor shareware per la scrittura di file TeX (esistono anche editor free. Ad esempio LEd, TeXnicCenter, TeXMaker).
L'installazione del software è **opzionale**, ma utile soprattutto nel caso di errori nella generazione dei file PDF. E' infatti possibile correggere gli errori presenti nel sorgente LaTeX generato a seguito della conversione.

 :  : R01 Nota :  correzione degli errori
Selezionando la scheda "set and play" del documento desiderato, è possibile visualizzare il sorgente LaTeX generato selezionando la scheda "Formattazione LaTeX".

![LOCFRM_022](http://localhost:3000/immagini/LOCFRM_LTE/LOCFRM_022.png)
Copiare il sorgente visualizzato nella scheda in un nuovo file creato in WinEdt. A questo punto lanciare la compilazione del documento da WinEdt premendo il tasto F9. Il programma si interromperà al primo errore, visualizzando il numero di riga e la causa dell'errore.

![COMPWINEDT](http://localhost:3000/immagini/LOCFRM_LTE/COMPWINEDT.png)
 :  : R01 Installazione WinEdt
E' possibile installare WinEdt seguendo il percorso : 
http://www.winedt.com/download.html e selezionando l'ultima versione disponibile

# OpenOffice Impress
OpenOffice Impress è un programma gratuito per la creazione di presentazioni informatiche multimediali.  Il programma fa parte della suite OpenOffice.org sviluppata dalla Sun Microsystems e permette, in aggiunta alle funzionalità standard offerte anche da Microsoft Power Point, la creazione di file PDF dalle presentazioni.

 :  : R01 Installazione OpenOffice Impress
E' possibile installare OpenOffice Impress e tutta la suite OpenOffice seguendo il percorso : 
http://download.openoffice.org/index.html

# TexMaker
TexMaker è un software che permette di capire meglio, in caso di errori nella compilazione del sorgente Tex, dove risiede il problema.
TexMaker è catalogato in Sme.UP come oggetto V2 SSORI 09 e quindi si rimanda alla sua scheda per maggiori informazioni
 :  : DEC T(V2) P(SSORI) K(09) D(Scheda TexMaker) O(D)

# Glossario

- **package** (pacchetto), ovvero file di stile (.sty) scritti in LaTeX, scaricabili ed installabili da appositi repository. I file contenengono una serie di istruzioni che permettono di eseguire operazioni personalizzate, che potrebbero essere utili nella compilazione del documento.
- **repository** (archivio), ovvero archivi utilizzabili da MikTeX per il download dei package mancanti.

