# Gestione Inventari

## Gestione Inventari

In generale l'Inventario di Magazzino è una procedura sistematica mediante la quale viene accertata l'esistenza di beni, in un determinato luogo e ad una data definita, in corrispondenza della quale non dovrebbero avvenire movimenti. Obiettivo fondamentale dell'Inventario di magazzino è quello di confermare o rettificare la Quantità Contabile dei beni perchè corrisponda a quella Fisica. Qualora così non fosse, bisognerà apportare le rettifiche necessarie.
La condizione ottimale per l'effettuazione di un Inventario sarebbe a fine anno e a negozio chiuso, con applicazione delle Rettifiche Inventariali al 31/12, così da chiudere l'esercizio appena trascorso.

 * Se l'Inventario viene eseguito al mattino a negozio chiuso, la **Data dell'inventario** dovrà essere quella del **giorno precedente**, visto che gli ultimi movimenti contabili risalgono a quella data
 * Se al mattino il negozio è aperto e vengono registrate delle vendite e il negozio viene chiuso la sera per effettuare l'Inventario, allora la **Data** sarà quella del **Giorno Stesso**
 * E' altamente sconsigliato effettuare un Inventario a Negozio aperto, si rischierebbe di vendere Merce non ancora conteggiata. Se proprio fosse necessario effettuarlo in questa condizione, è fondamentale assicurarsi di vendere merce già contata, altrimenti ricordarsi di conservare il cartellino dell'articolo per poterlo aggiungere all'Inventario.

## Descrizione

La procedura permette la gestione degli Inventari di Magazzini e di Punti Vendita.
Il Menu dedicato agli Inventari **Principale>Inventari** è così suddiviso : 

 * Gestione Inventario
 * Inventari per Zona
 ** Scarico Dati da Terminalino
 ** Registrazione Manuale Dati Inventario
 ** Visualizzazione Zone con Articoli Inesistenti
 ** Selezione Conta Attiva
 ** Analisi Confronto Conte
 ** Analisi Inventari di Zona
 ** Analisi Avanzamento Inventario
 ** Conferma Dati Inventario
 ** Gestione Articoli Inesistenti
 * Eventi Inventariali
 ** Gestione Modelli Eventi Inventariali
 ** Gestione Eventi Inventariali
 * Analisi Differenze Inventariali
 * Creazione Movimenti di Rettifica Inventariale
 * Stampa Differenze Inventariali Applicate
 * Riapertura Inventari
 * Analisi Valorizzazione Magazzino
 * Stampa Scheda Fiscale di Magazzino
 * Analisi Valorizzazione Magazzino per Fascia di Prezzo
 * Stampa Scheda Fiscale di Magazzino per Fascia di Prezzo

## Gestione Inventario

La funzione permette di Creare e Gestire gli Inventari. Dal Menu>Principale>Inventari>Gestione Inventario si aprirà una videata nella quale occorre inizialmente selezionare il Negozio da elaborare (se Elaborazione di Sede), mentre, se elaborazione di Negozio, viene automaticamente impostato il Codice definito nella configurazione.
All'attivazione della funzione viene presentato l'elenco degli Inventari di stato **Introdotto_n_ o**Da Inviare** esistenti per il Magazzino selezionato.
E' da tenere presente che un inventario di stato **Introdotto** è considerato da Negoziando come un inventario non ancora completato e quindi alcune funzionalità (Trasmissione Datietc) non potranno essere effettuate per l'Inventario in questione.

Sono a disposizione i seguenti tasti funzionali : 

 * F6 per Inserimento
 * Invio per Modifica
 * F4 Annullamento
 * F5 Visualizza
 * F8 Tutti/Da Inviare. Questo tasto permette di visualizzare tutti gli Inventari esistenti per il Negozio, indipendentemente dallo Stato. Premere di nuovo F8 per tornare alla visualizzazione normale.
 * F9 Cambia Stato. Questo tasto permette di modificare lo Stato dell'Inventario. Con la pressione del Tasto l'Inventario passerà da **Stato Introdotto**a **Da Inviare** e viceversa
 * F11 Documento. Questo tasto funzionale permette di inserire gli articoli nell'Inventario a partire da un Documento esistente. Viene richiesto di indicare i riferimenti del Documento di Vendita da utilizzare, quindi
 ** Magazzino di Emissione
 ** Tipo
 ** Periodo
 ** N° Documento
Verrà richiesta conferma prima di scaricare la Qta di Articoli presenti nel Documento
 * F12 F12 Terminalino. Questo tasto funzionale permette di inserire gli articoli nell'Inventario scaricando un Terminalino o utilizzando uno scarico precedentemente effettuato
Se lo scarico del terminalino era già stato effettuato in precedenza indicarne i riferimenti, quindi Periodo e Numero, altrimenti lasciare in bianco per lo Scarico Immediato e in questo caso verrà richiesto di collegare il terminalino
Al termine dell'Elaborazione viene presentato l'elenco degli articoli compresi nello scarico stesso.
Sono a disposizione i tasti funzionali F6 Inserimento, Invio Modifica ed F4 Annullamento per le gestione delle righe dello scarico.
Con il tasto F9 sarà possibile visualizzare il Totale delle Quantità dello Scarico suddivise per Unità di Misura, mentre col tasto F8 è possibile confermare l'Elaborazione delle righe dello Scarico.

Ora che abbiamo descritto i tasti funzionali, torniamo alla Gestione dell'Inventario
Premere F6 Inserisci per aggiungere un nuovo Inventario. Verranno richiesti innanzitutto i Dati di Testata : 

 * Data Inventario. E' consigliabile effettuare l'Inventario a Negozio Chiuso o al Mattino (prima dell'Apertura) o alla Sera (dopo la chiusura).
 ** Nel caso l'Inventario venga effettuato al Mattino indicare come Data Inventario la Data del giorno Precedente alla sua effettuazione.
 ** Nel caso venga effettuato alla Sera indicare come Data Inventario la Data del giorno della sua effettuazione.
 ** Nel caso (fortemente sconsigliato) di Inventario a Negozio Aperto indicare la Data del giorno Precedente alla sua effettuazione e assicurarsi di inserire nell'Inventario anche tutti gli articoli eventuali venduti (ma non ancora contati)
 * Responsabile Inventario
 * Quantità Prevista. Col tasto F8 la Quantità Prevista verrà automaticamente calcolata dal programma sulla base della Giacenza Contabile alla Data specificata come Data dell'Inventario.
 * Numero Zone
 * Tipologia Inventario. Può essere : 
 ** Globale
 ** Rotazione (solo Articoli Rilevati). In questo caso le funzioni di Analisi Differenze Inventariali e Creazione Movimenti di Rettifica Inventariale terranno in considerazione solo gli
Articoli Rilevati.
 ** Parziale (solo Articoli Presenti nell'Evento Inventariale legato all'Inventario). In questo caso le funzioni di Analisi Differenze Inventariali e Creazione Movimenti di Rettifica Inventariale terranno in considerazione solo gli Articoli Presenti
nell'evento inventariale abbinato all'inventario.
Per la gestione degli inventari parziali si rimanda alla sezione specifica descritta in seguito nel presente manuale.
 * Codice Workflow (solo se attiva gestione).E' possibile intervenire sullo stato del workflow in base alle transizioni effettuabili.

Premere Invio per passare alla gestione delle Righe.
Vengono inizialmente elencati gli articoli presenti con le relative quantità, se si entra in modalità di Modifica
Sono a disposizione i seguenti tasti funzionali : 

 * F6 Inserisci
 * Invio Modifica
 * F4 Elimina
 * F5 Visualizza
 * F8 Ordinamento
 * F9 Ricerca Articolo

Premendo F6 Inserisci o Invio Modifica si entra nella gestione delle Righe Articolo dell'Inventario.
Indicare l'Articolo da Inserire/Modificare e la relativa quantità e premere Invio per conferma dell'inserimento/variazione.

N.B. Se viene utilizzata la funzione di Inserimento è a disposizione il tasto funzionale F11 che permette di passare dalla modalità **Automatica** a quella **Manuale**
Nella modalità Automatica, dopo aver indicato il Codice a Barre (o il Codice Articolo) e premuto Invio, il programma effettua direttamente l'Inserimento con Quantità=1.
Nella modalità Manuale, invece, dopo l'Indicazione del Codice a Barre (o Articolo) il programma si posiziona sulla richiesta della Quantità in modo da poterla indicare manualmente.
Nella funzione di Modifica la modalità utilizzata è quella Manuale.

Con il tasto F9 è possibile effettuare la ricerca di un Articolo all'interno dell'Inventario. E' da tenere presente che per effettuare la ricerca di un articolo occorre impostare l'Ordinamento per Articolo premendo il tasto F8 (l'Ordinamento impostato viene visualizzato accanto al Titolo della Finestra)
Terminato l'Inserimento degli Articoli premere Esc Indietro e il programma ci riporterà alla videata con l'Elenco degli Inventari esistenti.
Ricordarsi di premere F9 Cambia Stato se l'Inventario è terminato.

## Inventari per Zona

L'Elaborazione degli Inventari per Zona permette una migliore gestione dell'Inventario in quanto è possibile appunto suddividere il Magazzino per Zone ed effettuare delle conte più specifiche degli Articoli e quindi più controllate.
Per la gestione degli Inventari per Zona sono a disposizione le seguenti funzioni : 

 * Inventari per Zona
 * Scarico Dati da Terminalino
 * Registrazione Manuale Dati Inventario
 * Visualizzazione Zone con Articoli Inesistenti
 * Selezione Conta Attiva
 * Analisi Confronto Conte
 * Analisi Inventari di Zona
 * Analisi Avanzamento Inventario
 * Conferma Dati Inventario
 * Gestione Articoli Inesistenti

## Inventari per Zona - Scarico Dati da Terminalino

Questa funzione permette di inserire gli articoli nelle varie Zone utilizzando un terminalino. Una volta selezionata questa funzione dal _Menu>Principale>Inventari>Inventari per Zona>Scarico Dati da Terminalino si aprirà la videata con l'Elenco degli Inventari Aperti, quindi è opportuno aver prima creato la Riga dell'Inventario dal _Menu>Principale>Inventari>Gestione Inventari 

N.B. E' possibile con la stessa elaborazione scaricare più di una zona. In questo caso, le informazioni ricevute dal terminalino dovranno essere suddivise tra informazioni di Testata (che conterranno il
numero della Zona) e informazioni di Riga (Articolo/Quantità).

La funzione prevede, come tutte le funzioni relative agli Inventari di Zona, la selezione iniziale dell'Inventario sul quale effettuare l'Elaborazione.
Dopo la selezione dell'Inventario viene richiesto di collegare il terminalino
Se nell'Elaborazione del file ricevuto dal terminalino non è stato possibile effettuare una distinzione delle zone, tutti gli articoli vengono considerati appartenenti alla stessa zona e vengono richieste le
informazioni mancanti : 

 * Nr. Terminalino
 * Zona
 * Squadra

Al termine dell'Elaborazione il programma visualizza l'Elenco degli scarichi effettuati (suddivisi per zona).
Sono a disposizione i tasti funzionali F7 Stampa Complessiva e F8 Stampa Articoli Errati

## Inventari di Zona - Registrazione Manuale Dati Inventario

Dal Menu>Principale>Inventari>Inventari per Zona>Registrazione Manuale Dati Inventario è possibile gestire le righe degli Inventari di Zona. La funzione richiede inizialmente la selezione dell'Inventario
Dopo la selezione iniziale viene presentato l'Elenco delle Zone (e relative conte) presenti nell'Inventario.
Premendo F6 Inserisci o Invio Modifica si entra nella gestione della Zona.
Vengono richieste le informazioni di Testata della zona. : 

 * Nr. Terminalino
 * Zona
 * Squadra
 * Progressivo Conta. Viene controllato il numero indicato. Nel caso di inserimento deve essere indicato un valore inesistente immediatamente successivo all'ultimo valore imputato.
 * Note
 * Tipo Conta. E' possibile definire se : 
 ** Dettagliata. Non occorre indicare la Quantità Totale e premendo Invio si passerà alla gestione degli Articoli della zona.
 ** Totalizzata. In questo caso occorrerà solo indicare la Quantità Totale, non è prevista la gestione degli Articoli.

Dopo aver premuto Invio alla richiesta di informazioni di testata della Zona (se zona di tipo Dettagliata e se in Modalità Modifica) si passa alla gestione delle Righe della Zona.
Vengono elencati gli articoli presenti nella zona.

N.B. Gli articoli che hanno ******** nel campo Descrizione (e che non hanno Articolo/Colore/Taglia) sono articoli **errati**, cioè codici a barre letti con il terminalino ma che non esistono negli archivi anagrafici di Negoziando.

## Inventari di Zona - Visualizzazione Zone con Articoli Inesistenti

Questa funzione serve per visualizzare i codici a barre errati presenti in tutte le zone dell'inventario. Dal _Menu>Principale>Inventari>Inventari per Zona>Visualizzazione Zone con Articoli Inesistenti selezionare l'Inventario che si intende interrogare.
Una volta selezionato e dato conferma, si aprirà la videata col dettaglio di tutti gli Articoli inesistenti

## Inventari di Zona - Selezione Conta Attiva

La funzione permette di selezionare tra le varie Conte che possono esistere in una zona quale conta è da considerare come Attiva, ovvero quella che Negoziando dovrà prendere in considerazione per l'Elaborazione dell'Inventario.  Dal _Menu>Principale>Inventari>Inventari per Zona>Selezione Conta Attiva
La funzione richiede inizialmente la selezione dell'Inventario
La videata che apparirà riporta l'elenco delle Zone indicando con una spunta Verde la presenza di una Conta Attiva. La mancanza di questa Impostazione verrà segnalata da un triangolino giallo
Premendo F8 è possibile visualizzare tutte le zone per le quali non è stata definita nessuna Conta Attiva
Il Tasto Invio Seleziona Zona permette, se presenti più Conte della stessa Zona, di modificare la Conta Attiva selezionandone un'altra. Premere F6 per Confermare
N.B. Non è possibile impostare come Attiva una conta di tipo Totalizzata

## Inventari di Zona - Analisi Confronto Conte

Questa funzione permette di confrontare il contenuto (Articoli/Quantità) fra due conte della stessa Zona.  Dal _Menu>Principale>Inventari>Inventari per Zona>Analisi Confronto Conte_
La funzione richiede inizialmente la selezione dell'Inventario.
Indicare il Numero della Zona e premere Invio. Vengono elencate tutte le Conte esistenti per la zona selezionata
Con il tasto F7 Da Elaborare SI/NO selezionare le due Conte da confrontare (accanto ad esse apparirà la Spunta Verde) e premere F6 Conferma (non possono essere selezionate le Conte di Tipo Totalizzate)
Verrà Visualizzato l'Elenco di tutti gli Articoli presenti e le Quantità delle Conte saranno riportate nelle due Colonne finali. Col Tasto F5 sarà possibile Visualizzare Tutti gli Articoli oppure Solo quelli con Differenze. Col Tasto F7 è possibile Stampare l'Elenco

## Inventari di Zona - Analisi Inventari di Zona

Questa funzione permette di effettuare analisi sugli Inventari di Zona. Dal _Menu>Principale>Inventari>Inventari per Zona>Analisi Inventari di Zona_
La funzione richiede inizialmente la selezione dell'Inventario. All'Attivazione vengono richiesti i parametri di selezione : 

 * Da Zona a Zona
 * Da Terminalino a Terminalino
 * Da Squadra a Squadra
 * Da Rilevazione a Rilevazione
 * Solo Conte Attive SI/NO
 * Solo Conte Rilevate SI/NO
 * Valorizza Zone SI/NO
 * Ordinamento
 ** Numero Rilevazione
 ** Zona/Progressivo Conta
 * Tipo Valorizzazione Primaria/Secondaria
 ** Costo Standard
 ** Costo Medio
 ** Costo Medio Ponderato
 ** Listino d'Acquisto
 ** Listino di Vendita. Se viene selezionato, apparirà anche la Richiesta del Codice Listino

Dopo la selezione dei parametri viene presentata a video l'Analisi richiesta.
Sono evidenziate le Zone, le Conte, il Numero di Righe e Quantità OK, il Numero di Righe e Quantità Errate, etc...
Col Tasto F7 è possibile stampare il Report.

## Analisi Avanzamento Inventario

Questa funzione permette di analizzare lo stato di avanzamento dell'Inventario.  Dal _Menu>Principale>Inventari>Inventari per Zona>Analisi Avanzamento Inventario_
La funzione richiede inizialmente la selezione dell'Inventario
Con questa funzione vengono confrontati i valori definiti nella testata dell'Inventario (Gestione Inventario - Quantità Prevista/Numero Zone) con i dati presenti negli Inventari di Zona al
momento dell'Attivazione della funzione.


## Conferma Dati Inventario

Questa funzione chiude sostanzialmente l'Elaborazione dell'Inventario per Zone. Dal _Menu>Principale>Inventari>Inventari per Zona>Conferma Dati Inventario_, la funzione richiede la Selezione
dell'Inventario.
A questo punto apparirà una richiesta di Conferma di Elaborazione contenente il dettaglio del Magazzino e la Data dell'Inventario. Premendo OK l'Elaborazione trasferirà i dati (Articoli/Quantità) dagli Inventari di Zona agli Inventari Normali.
Viene inoltre eseguito un controllo sull'esistenza di righe articolo nell'inventario normale (se si è utilizzata la gestione Inventari di Zona, l'Inventario normale non dovrà contenere nessuna riga)
chiedendo conferma se proseguire.
N.B. Prima di attivare questa funzione è opportuno effettuare una verifica sulla definizione delle conte Attive per ciascuna zona. In caso di mancata indicazione delle Zone Attive, l'Elaborazione non sarà possibile

## Gestione Articoli Inesistenti

La funzione in oggetto permette di visualizzare l'Elenco degli Articoli Inesistenti. Dal _Menu>Principale>Inventari>Inventari per Zona>Gestione Articoli Inesistenti_

## Gestione Eventi Inventariali - Inventari Parziali

Gli inventari parziali sono degli inventari a rotazione con la particolarità che gli articoli oggetto di inventario sono definiti dalla Sede.
Sono inventariabili solo gli articoli inseriti nell'Evento Inventariale associato all'Inventario.
Degli Articoli non inventariati verrà azzerata la giacenza.
Le funzioni sono presenti nel Menu di Negoziando sotto la voce _Principale>Inventari>Eventi Inventariali>Gestione Modelli Eventi Inventariali_ e _Principale>Inventari>Eventi Inventariali>Gestione Eventi Inventariali

Lato sede sono attive entrambe le funzioni, mentre lato Punto Vendita è attiva solo la voce _Gestione Eventi Inventariali_

La funzione in oggetto permette alla Sede di Creare un Evento Inventariale, quindi di programmare la verifica delle Quantità di un determinato Gruppo di Articoli decisi dalla Sede stessa. Dal _Menu>Principale>Inventari>Eventi Inventariali>Gestione Eventi Inventariali_




