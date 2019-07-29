# I video di SME.up

I video di SME.up sono tesi a facilitare il passaggio di conoscenze.
Il video è un oggetto (MB   DOC_VID) cui è associato un documento che ne descrive sinteticamente le caratteristiche quali : 

- Descrizione
- A chi si rivolge
- Contenuto
- Requisiti
- Documentazione collegata
- Durata


# Convenzioni
Per quanto riguarda la denominazione da attribuire al video abbiamo la seguente codifica : 
mmmmmm_ann dove : 
* - mmmmmm Modulo
* - a      Gruppo, rappresenta il tipo di video :  C = Commerciale, P = Operativo, T = Tecnico, ..
* - nn     Progressivo
Es. A£LABS modulo C gruppo e 01 il progressivo, otteniamo la denominazione A£LABS_C01.

## Regole generiche

 * Procedura di registrazione del video : 
 ** Stendere l'agenda del video dettagliando il contenuto delle singole voci (ovvero predisporre una scenografia del video)
 ** Sottoporre la scenografia del video al responsabile della documentazione per una prima approvazione
 ** Generare il video uilizzando Camtasia e seguendo lo standard riportato all'interno del presente documento (in modo da creare il progetto in modo congruo e metterlo nelle cartelle corrette)
 ** Sottoporre nuovamente il video completo al responsabile per l'ultima approvazione
 ** Una volta che il video viene approvato seguire le istruzioni per caricare quest'ultimo nella cartella corretta per la condivisione e pubblicarlo su youtube.
 * Carattere per scritte :  Arial
 * Ricordarsi che per tutte le applicazioni il formato del nome è :  Applicazione.UP (il nome dell'applicazione deve quindi essere scritto con il primo carattere maiuscolo e le lettere seguenti minuscole mentre UP deve sempre essere scritto maiuscolo)
 * La durata di un singolo video non deve superare i 10/15 minuti, se  necessario anzichè fare lunghi video farne diversi ma brevi
 * Salvataggio dei file :  i file devono essere salvati seguendo il seguente percorso :  [SME.OGG]_7_\MBDOC_VID all'interno della cartella MBDOC_VID è necessario individuare o creare la cartella relativa al nome del video in questione. Per accedere alla cartella è anche possibile entrare nel modulo A£FORM da Looc.UP, selezionare all'interno del menù la voce 'Video'. Così facendo si accede alla scheda per la navigazione/gestione dei video di Sme.UP. Da qui è necessario cercare il membro legato al video che sto creando, se non esiste crearlo seguendo le relative istruzioni.

 :  : REM
Parte commentata
 * Modifica stato video :  all'interno della matrice dei corsi nel A£FORM gli elementi che identificano i filmati da realizzare sono di tipo VIDXX dove XX è un numero che identifica lo stato del video. Quindi nel caso in cui il video non sia ancora stato assegnato avrà tipologia VID00, se è stato assegnato ma non è ancora in realizzazione sarà VID10, se è in fase di realizzazione sarà VID20, se è completo sarà VID80 mentre se è annullato sarà VID90. Di conseguenza chi verrà incaricato di realizzare un video dovrà preoccuparsi di modificare la tipologia del membro all'interno del file DOC_EDU.
 :  : REM.END

## Strumento per la produzione del video
Per la produzione dei video è stato indentificato uno software commerciale di nome Camtasia.
Altre informazioni sul prodotto è possibile reperirle come oggetto V2 SSORI 12
 :  : DEC T(V2) P(SSORI) K(12) D(Camtasia) O(D)
Di seguito viene invece riportato il modus-operandi per la produzione del file video

## Definizione dello std della struttura
 * Introduzione. L'introduzione del filmato deve essere costituita dalla copertina della presentazione power point che ovviamente avrà come sfondo quello attualmente in utilizzo per le presentazione Sme.UP. Al centro della copertina deve essere posizionato il titolo del video + un eventuale sottotitolo.
 * Agenda. Subito dopo la copertina dovrà essere mostrato il contenuto del video. Dovrà quindi essere visualizzata e spiegata una slide che riporti gli obiettivi del video, ovvero i contenuti che dovranno essere appresi dallo spettatore (agenda dell'intervento).
 * Struttura del video. La scenografia del video deve rispecchiare esattamente l'agenda della presentazione. Attraverso l'utilizzo di markers è possibile fare in modo che i titoli del TOC rispecchino i punti riportati in agenda.
 * Il video deve essere editato per quanto riguarda le parti di power point con uno sfondo standard.
 * Conclusione. Al termine del video dovrà essere riportata nuovamente l'agenda dell'intervento che riassume i punti toccati nel video e le nozioni apprese e una pagina di ringraziamento : 
![A£FORM_002](http://localhost:3000/immagini/A£FORM_01/AXFORM_002.png)
## Definizione dello std delle riprese
 * Le riprese devono essere effettuate impostando la luce sul mouse e la comparsa del 'centro' al click del mouse. Per impostare queste opzioni è necessario entrare nel pannello Camtasia recorder, scegliere Effects e quindi Cursor e Highlight Cursor&Clicks.

## Definizione dello std di editing
 * Transitions :  il passaggio tra diversi filmati può essere effettuato tramite l'utilizzo di flip della durata di 1 sec.
 * All'interno dell'Audio Enhancements selezionare Event out volume levels -> Setting :  low volume variations per livellare le variazioni nel volume dell'audio : 
![A£FORM_003](http://localhost:3000/immagini/A£FORM_01/AXFORM_003.png)
## Definizione dello std di produzione
 * Il filmato dovrà essere prodotto in formato WMV 800X640 e dovrà contenere il TOC. Per ottenere questo formato compilare come segue il wizard di produzione : 
![A£FORM_004](http://localhost:3000/immagini/A£FORM_01/AXFORM_004.png)![A£FORM_005](http://localhost:3000/immagini/A£FORM_01/AXFORM_005.png)![A£FORM_006](http://localhost:3000/immagini/A£FORM_01/AXFORM_006.png)![A£FORM_007](http://localhost:3000/immagini/A£FORM_01/AXFORM_007.png)![A£FORM_008](http://localhost:3000/immagini/A£FORM_01/AXFORM_008.png)![A£FORM_009](http://localhost:3000/immagini/A£FORM_01/AXFORM_009.png)![A£FORM_010](http://localhost:3000/immagini/A£FORM_01/AXFORM_010.png)
## Definizione dello std delle cartelle di Looc.UP
 * All'interno di Looc.UP i file devono essere organizzati nel seguente modo : 
 ** una cartella 'File di lavoro' in cui è necessario inserire le riprese, eventuali registrazioni audio, i power point, il progetto camtasia e la cartella prodotta dalla produzione del video (di default viene  nominata con il nome assegnato + _media).
 ** Il file wmv compilato che verrà poi caricato su internet : 
![A£FORM_011](http://localhost:3000/immagini/A£FORM_01/AXFORM_011.png)
## Compilazione della Descrizione del corso
Una volta inserite le cartelle con i file relativi al video realizzato è necessario compilare la scheda descrittiva del corso che si trova nel tab 'Documentazione'. Qui è necessario compilare la descrizione del corso i prerequisiti, la sceneggiatura e l'autore del video.

## Divieti e consigli
 * È assolutamente vietato andare fuori agenda
 * Evitare di soffermarsi a lungo su schermate 'statiche'. Anche nel caso in cui una stessa schermata richieda una spiegazione piuttosto lunga utilizzare zoom e callouts per rendere il video meno statico possibile.
 * Utilizzare frequentemente esempi all'interno del video.
