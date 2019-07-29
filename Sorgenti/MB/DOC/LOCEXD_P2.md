# Informazioni su Rilasci Componente Scheda
## In fase di sviluppo

- Ampliamento capacità della matrice, su totalizzazioni e analisi dei dati.

## Versione V2R2M070622-01Z Stable 25/10/2007

- Sostituito il parser precedentemente utilizzato con il parser XML MSXML 3.0.
- Corretto un errore sulla matrice di aggiornamento. In determinate condizioni si generava in presenza di un errore un loop.
- Corretto un problema nell'albero. Veniva erroneamente inserito uno spazio nel codice di ogni nodo dell'albero impedendo il corretto funzionamento di espansione dinamica e dinamismi.
- Corretto un problema di conversioni di carattere negli attributi dell'XML nel nuovo parser.
- Aggiunta una funzionalità di controllo e correzione di errori (al momento solo sulla spaziatura e validità degli attributi) nel parser XML al caricamento.
- Modifica degli algoritmi del modulo di esportazione in Excel. Questa operazione ha consintito un notevole aumento di performance.
- Modificata la finestra di segnalazione di errore in caso di XML errato. Ora l'utente è in grado di aprire il file XML con il programma predefinito del Sistema Operativo.
- Modificata la chiamata al sistema operativo per l'apertura di un file xml. Viene ora effettuata la stessa operazione che esegue un utente con il doppioclick.
- Aggiunto un meccanismo di caching nell'albero per le icone provenienti dal sistema operativo. E' stata anche cambiata la modalità di caricamento in modo da fornire l'icona generica di sistema in caso di file non trovato.
- Aggiornato il System Info di Smetray, in modo da riconosce come sistema operativo anche Windows Vista.
- Aggiunto il supporto ad Excel 2007.
- Risolto un problema che si verificava al ricaricamento di una sezione se presente la Toolbar estesa della stessa.
- Risolto un problema che si verificava al ricaricamento di una scheda se presenti nel setup dimensioni e posizioni della stessa.
- Aggiunta la possibilità di specificare nel setup di scheda, negli attributi di posizione e dimensione, delle percentuali di schermo(prima era possibile solo indicare la dimensione in pixel).
- Aggiunta la gestione grafica dei setup da servizio nelle sezioni della scheda. L'utente percepisce i setup in maniera trasparente.
- Risolto un problema che si verificava alla selezione, tramite bottone con menu, dei setup utente.
- Risolto un problema nel risolutore di formule. In caso di presenza in operandi segnalati come stringhe dei caratteri "(" e ")", il risolutore falliva la condizione.
- Risolto un problema che si verificava al "merging" di due XML di tipo dati. Veniva creato un XML errato o mancante di un tag di chiusura.
- Risolto un problema relativo alla selezione multipla di celle nella matrice in presenza della colonna di servizio "Id".
- Risolto un problema nella matrice relativo al calcolo del numero dei decimali in colonne con oggetto indiretto.
- Risolto un problema di sincronia di comunicazione che talvolta mostrava la scheda di partenza completamente grigia.
- Aggiunta la funzionalità di passaggio a matrice totalizzata per le matrici raggruppate.

## Versione V2R2M070622-01R Stable 10/10/2007

- Risolto un problema sulla procedura di aggiornamento di una matrice introdotto nell'ultima versione rilasciata.
- Eseguiti numerosi fixing.

## Versione V2R2M070622-01Q Stable 05/10/2007

- Nuovo modulo di esportazione in excel che tiene conto dei filtri, stili e colori della matrice. E' possibile abilitare varie caratteristiche dal pannello di esportazione che appare a richiesta.
- Modificata la matrice di aggiornamento con aggiornamento istantaneo in modo da gestire risposte a Line multiple da AS.

## Versione V2R2M070622-01M Stable 12/09/2007

- Risolto un problema di instabilità nelle sezioni di tipo HTM, dovuto al nuovo rilascio di IE7.
- Alcuni fixing sulla matrice.

## Versione V2R2M070622-01I Stable 31/08/2007

- Risolto un problema sull'individuazione dell'oggetto draggato nelle matrici. A volte non venivano riconosciute correttamente colonna e riga.


## Versione V2R2M070622-01H Stable 30/08/2007

- Risolto un problema sugli stili condizionali per la comparazione delle stringhe. Veniva forzata la stringa di condizione in maiuscolo ma non il contenuto dei campi.
- Modificata la struttura della gestione delle variabili nell'evento drop.

## Versione V2R2M070622-01D Stable 18/07/2007

- Numerosi fixing sulla stabilità.
- Divisione in pagine per i grafici a linea veloce.
- Aggiunta la gestione nella matrice dell'oggetto J4PIE. Riferirsi alla documentazione per maggiori informazioni.
- Aggiunto l'Hint sui valori di una serie in modo da mostrare il valore quando il mouse vi si ferma sopra.
- La combinazione CTRL+F10 in una matrice ora visualizza le colonne nascoste della medesima.
- Aggiunta la colonna di tipo G nella matrice. Si tratta di una colonna nascosta di tipo attributo. I valori nelle sue celle vengono cioè utilizzati per modificare un attributo della rispettiva cella nella colonna successiva. E' possibile attualmente specificare 2 indicatori separati da ; . Il primo è un numero tra 1 e 9 e modifica l'aspetto grafico (colore, font) della colonna successiva. Il secondo è una stringa che, se presente e se attivo il DetailHint della  matrice, setta il messaggio da visualizzare per la cella adiacente. Esempio :  1;Sono una cella in Grassetto

## Versione V2R2M070622-01B Stable 28/06/2007

- Aggiunta la gestione di nuove celle grafiche per la matrice. In particolare la gestione dell'oggetto J4PIE che crea un grafico a torta o semplicemente un ellisse nella cella. Vedere la documentazione.
- Risolto un problema nell'utilizzo dell'attributo SelRow nella matrice se specificato un raggruppamento di default.
- Aggiunta la possibilità di associare il valore *LAST all'attributo SelRow della matrice, per selezionare l'ultima riga.
- Risolto un problema che si verificava alla pressione dei tasti toolbar della matrice di aggiornamento.
- Ora quando viene richiesto un report viene impostato come titolo del report il titolo della sezione.

## Versione V2R2M070622-01A Stable 20/06/2007

- Risolto un problema che generava un errore Access Violation all'espansione di una scheda intera.
- Risolto un problema che rimuoveva i pulsanti si setup di sezione una volta rimosso l'ultimo setup utente.
- Risolto un problema che impediva il corretto caricamento del setup corrente dopo la pressione del tasto "Annulla" del gestore dei setup.
- Risolto un problema che non mostrava il pulsante del setup utente una volta aggiunto come primo ad una sezione.
- Risolto un problema che faceva scattare involontariamente un dinamismo nella matrice (se presente) anche in assenza di attributo SelFirst se presenti dei raggruppamenti multipli.
- In caso di presenza di celle grafiche la matrice viene ora swappata su disco.
- Risolto un problema sulla generazione di una cella grafica della matrice. Non veniva calcolata correttamente l'altezza in alcuni casi.
- Risolto un problema che si verificava al click di un nodo di un albero caricato tramite paginazione.
- Aggiunto il Parsing per al gestione interna della variabile CallerFlds contenente i campi ritornati da una scheda all'altra.
- Aggiunta la gestione delle ricerche "specializzate" anche su Input Panel senza servizio di aggiornamento collegato.
- Aggiunta la possibilità di definire nella matrice un tooltip del record personalizzato.
- Aggiunta la gestione automatica dei campi memo nella matrice sia in input sia in output.
- Risolto un problema che si verificava in taluni casi in presenza di descrizione tipizzata.
- Aggiunto un minimo di dimensione (3 pixel) alla larghezza delle barre nelle celle grafiche della matrice.
- Aggiunta una voce al menù di sezione per la visualizzazione del Setup di aggiornamento in caso di matrice di aggiornamento (o input panel).
- Aggiunto il pulsante di stampa della sezione HTM.
- I campi memo hanno la possibilità di definire un numero di colonne (caratteri) dopo il quale viene eseguito un AutoWrapping del testo.
- Risolto un problema che si verificava a volte dopo l'espansione dinamica di un albero, cliccando sui nodi rimasti "grigi".
- Irrobustita la gestione delle variabili di Smetray in modo da segnalare la sintassi sbagliata da parte dell'utente in fase di formalizzazione di una variabile.
- Aggiunta la possibilità di richiamare la scheda standard di Debug con la pressione della combinazione di tasti "Ctrl+F9"
- Risolto un problema che impediva di mantenere il colore dei titoli delle colonne di asse e serie in una matrice.
- Ottimizzata la gestione dei fuochi degli oggetti che compongono Smetray.
- Aggiunto un blending di colore per le celle che hanno condizione Dpy="R" in modo da evidenziare la condizione.

## Versione V2R2M070214-02Q Stable 30/05/2007

- Attivate ricerche "specializzate" anche con ritorno di valori multipli all'interno degli input panel (anche se non abbinati a matrici) omogeneizzandolo a quanto era già possibile fare nelle matrici di aggiornamento. La funzione di ricerca deve essere specificata in un nodo <Search> all'interno del nodo Campo al quale si riferisce.
Gli attributi da impostare nel nodo <Search> sono : 
-- Char="<carattere>" :  Identifica il carattere al quale è legata l'esecuzione della funzione di ricerca
-- Type="Direct|Indirect"  : 
--- Direct=Ricerca "Standard" fornita da altri componenti (Java od Emulatore);
--- Indirect=Ricerca "via Scheda" (accessibile dalle sole schede)
-- Funzione="<funzione>" :  Funzione da richiamare per eseguire la ricerca. Occorre specificare se desiderato nel parametro *CALLERFLDS le mappature (separate da ;) tra i nomi dei campi di destinazione e i nomi dei campi ritornati dalla ricerca stessa
- Inserito Parser Xml nella composizione dei messaggi di risposta ricerche per evitare problemi su caratteri speciali
- E' stato creato un nuovo attributo nel setup delle matrici che consente la customizzazione dei messaggi di Hint.
Nell'attributo DetailHintText è possibile definire un proprio testo da visualizzare utilizzando i nomi dei campi del record corrente
(Es :  DetailHint="Yes" DetailHinText="Il Codice articolo è :  [A§ARTI]"
- Corretto un errore che preveniva la visualizzazione corretta dei campi memo nel caso di campo di solo output in matrice di aggiornamento

## Versione V2R2M070214-02L Stable 22/05/2007

- Modificata la gestione dei campi data in input panel e in matrice.
- Risolto un problema che si generava sul change di un nodo dell'albero.
- Risolti alcuni problemi di caricamento delle serie nei grafici.
- Risolto un problema relativo al caricamento dei PDF.
- Modificata la gestione dei setup nella chiamata al componente REP (Report), ora viene passato il setup corretto con le modifiche apportate a video.
- Aggiunte altre funzionalità alla cella grafica della matrice per l'oggetto J4BAR (vedi documentazione specifica).

## Versione V2R2M070214-01L Stable 14/05/2007

- Aggiunti check-box e campi memo nella matrice.
- Risolti alcuni problemi sul drag and drop da albero. Non venivano compilate correttamente delle variabili.
- Aggiunto l'attributo OnlyFocus nella definizione dei dinamismi. Tramite questo attributo è possibile dare il fuoco ad una sezione senza ricaricarla (se già caricata).
- E' ora possibile definire dei dinamismi sulla stessa sezione di partenza.
- Cambiata la modalità di filtrering della matrice in modo da integrare anche filtri esterni tramite emulazione. I filtri divisi in categorie saranno comunque visualizzati nella barra informativa della matrice. La definizione di servizi di filtering particolari è possibile tramite particolari indicativi nell'XML di UIPopup.
- Aggiunte nuove funzionalità alla paginazione in matrice (così come il carica completamente) ed integrata nella barra dei filtri.
- Aggiunti nuovi attributi di layout nel setup generale di Smetray.
- Aggiunta la possibilità di visualizzare le sottoschede tramite un menu sommario a scomparsa.
- Fissati innumerevoli problemi minori ed instabilità.
- Modificata la gestione dei popup menu da AS400 in modo da gestire il caricamento dinamico su richiesta.
- Risolti due problemi relativi al grafico e alle serie calcolate.
- Aggiunta la visualizzazione della riga ID nella matrice tramite setup.
- Aggiunte molte funzionalità (vedere la documentazione specifica) alla cella grafica della matrice su oggetto J4BAR.
- Aggiunto un attributo per nascondere l'header delle colonne della matrice.


## Versione V2R2M070214-01H Stable 19/03/2007

- Modificata la gestione dei decimali nella matrice. Se nulli non vengono considerati per il calcolo della lunghezza del campo e non mostrati.
- Risolto un problema relativo alla stampa delle sezioni Grafico introdotto con l'ultimo rilascio.
- Modificata la gestione della sezione HTM per evitare che la stessa appaia in posizione errata. Al caricamento la sezione HTM mantiene sempre il fuoco.

## Versione V2R2M070214-01D Stable 02/03/2007

- Risoluzione di parecchii Memory Leak di Smetray.
- Risolti i problemi di disallocazione dei contenuti dei documenti XML. I problemi spinosi dati dalla struttura e gestione dell'XML sono stati risolti.
- Risolto un problema legato all'XML delle liste dei setup generato a seguito dell'ottimizzazione.
- Modificata la gestione dei campi dinamici della matrice per risolvere alcuni problemi, quali la formattazione dei numeri, la dimensione dei caratteri nascosti, il ridimensionamento delle colonne in automatico.
- L'oggetto J4BAR ora gestisce correttamente la dimensione 100 e l'altezza.
- Modificata la gestione dell'oggetto NR nella matrice in modo da formattare correttamente i decimali anche se la matrice è vuota e l'oggetto è indiretto.
- Aggiunto l'attributo RowHeight  per potere specificare l'altezza di partenza delle righe di una matrice.
- Aggiunta la possibilità di definire un host remoto (servente java.. tipicamente Loocup.jar) con cui dialogare da riga di comando.
- Corretto un problema relativo ai Tab-alberi che non trasportavano le variabili presenti nel foglio principale allo scattare dei dinamismi.
- Corretto un problema relativo ai Tab-alberi che facevano sparire i pulsanti definiti in UIPopup.
- Modificata la gestione del dettaglio record in una matrice in modo da puntare al record corretto sempre.
- Risolto un problema che faceva scattare l'apertura del dettaglio record alla pressione anche della combinazione Alt-24
- Aggiunto l'attributo ForceOneLine per forzare il numero di linee ad uno nelle celle della matrice.
- Risolto un problema nella gestione dei Setup utente introdotto con l'ultimo rilascio.
- Modificata la gestione degli assi e delle serie nel grafico. Ora il grafico non mostra più come possibili serie le colonne impostate dall'utente se queste non sono compatibili (colonne numeriche).

## Versione V2R2M070214-01A Stable 21/02/2007

- Modificata la gestione dell'XML della sezione HTM per la l'utilizzo dei link interni nella documentazione.
- Modificata la sezione EMU aggiungendo alcuni attributi per l'autoriapertura e l'inserimento in sezione.
- Modificata la gestione degli eventi RETURN in modo da essere compatibili con la sezione EMU.
- Risolto un problema di fuochi nella sezione EMU.
- Risolto il problema di gestione multievento nei pulsanti e nelle voci di menu da UIPopup.
- Modificato il caricamento della sezione EMU in modo da ultimare la costruzione dei pulsanti UIPopup prima.
- Aggiunta la gestione dell'attributo load sui dinamismi relativi a bottoni e popup definiti tramite UIPopup.
- Risolto un problema che si verificava a volte durante il caricamento di sottoschede con etichetta non visibile.
- Modificata la gestione dei nodi TA-MEA nell'albero. Ora l'apertura di una scheda legata a voce di menu è condizionata da una variabile (TAMEAGRAPHICMODE) definita nello script SCP_CLO, in cui è possibile specificare la modalità di apertura della scheda (NFI, etc. etc.).

## Versione V2R2M061003-05G Stable 31/01/2007

- Risolto un problema sulla matrice di aggiornamento. Scattava sempre l'evento change anche se non presente l'attributo SelFirst al caricamento.
- Risolto un problema sulla sezione HTML che portava ad un AV in caso di caricamento di PDF da percorso di rete (invece che URL).
- Risolto un problema sull'autofitting delle colonne nella matrice. Non veniva calcolata la lunghezza dei totali se presenti. Ora la colonna è ridimensionata tenendo conto della lunghezza effettiva del totale.
- Risolto un problema sulla mancata presa di fuoco dei controlli nell'input panel.
- Modificata la gestione dei filtri nell'esportazione in excel per esportare correttamente tutti i filtri (anche i blanks) previsti in loocup.
- Modificata l'esportazione in excel in modo da mostrare i valori corretti in caso di presenza di formule nelle colonne e nei totali.
- Risolto un problema sulla sezione OCX.
- Affinata la parte di caricamento delle finestre nella sezione EMU. La sezione EMU è in grado ora di caricare internamente una finestra di emulazione.
- Aggiunta una nuova parte di comunicazione alla sezione EMU. E' ora possibile scambiare variabili e agganciare eventi alla sezione.
- Aggiunto un attributo alla matrice per potere visualizzare la colonna ID come indice di record. Modificata di conseguenza anche la gestione della colonna in questione.
- Risolto un problema che faceva partire il valore della variabile row in una matrice da 0 anziché da 1.
- Aggiunto un attributo al grafico in modo da potere visualizzare nei marks i valori nelle ordinate al posto dei nomi dei campi.
- Risolto un problema nella sceda relativo alla visibilità della sezione KEYBOTTOM.
- Aggiunta la lettura dei setup di componente anche nell'XML dei dati in modo da essere specificabili da servizio.
- Risolto un problema per cui non venivano memorizzate nel setup utente tutte le impostazioni delle colonne raggruppate in particolare l'ordinamento.
- Risolto un problema che si verificava all'esportazione in Excel di una matrice. Non venivano visualizzati i raggruppamenti nella versione 2003.
- Modificato il formato di salvataggio dei fogli Excel 2003. Ora vengono salvati nello standard XLS.
- Risolvere un errore di tipo AV sulla massimizzazione delle sezioni sottoscheda. Ora vengono riaperte in un'altra scheda nello stesso stack.
- Modificato il comportamento sulla massimizzazione delle sezioni. In ogni caso la pressione del tasto F12 non chiude la finestra ma torna a sezione non massimizzata.
- Risolto un errore che si verificava all'esportazione di una matrice con colonna Id visibile in excel.
- Modificata la gestione dell'XML nella sezione HTM in modo che se si è effettuato del browsing la stampa della sezione stampa il contenuto corretto.
- Aggiunto l'attributo OnlyFocus alla specifica G.DIN in modo da indicare un dinamismo che non faccia ricaricare i contenuti della sezione di destinazione.
- Modificata la gestione della tastiera nella sezione HTM. Ora tutti i caratteri funzionano correttamente ed è possibile rinominare file all'interno della sezione.

## Versione V2R2M061003-04I Stable 18/12/2006

- Ottimizzazione del caricamento della matrice.
- Modificati i costruttori degli oggetti grafici in modo da non mostrare nulla durante la creazione della parte video. Questo ha incrementato di non poco le performance di Smetray.
- Eliminato la parte di rimozione dei nodi xml UIPOPUP relativi alla paginazione. Sostituita con controlli in fase di creazione della bottoniera.
- Implementato un sistema (abilitabile da riga di comando o setup di scheda) di logging di performance nella scheda.

## Versione V2R2M061003-04H Stable 15/12/2006

- Modificata la visibilità di ogni componente in costruzione per rimuovere l'effetto di flickering e aumentare le performance durante la costruzione a video.
- Ottimizzati alcuni algoritmi della parte di costruzione della scheda.
- Ottimizzato il caricamento in matrice dei dati.
- Implementato un sistema di logging di performance nella scheda. E' possibile abilitare da riga di comando o da setup di scheda la nuova funzionalità tramite l'attributo "ExtDebug".
- Modificata la gestione dei caricamenti delle barre dei setup di Smetray.
- Risolto un problema sulla matrice di aggiornamento. Non veniva effettuato il controllo di formattazione di numeri e date in caso di comparazione dei dati con il default.
- Modificata la sezione EMU. Ora le funzioni da lanciare vengono risolte appena prima dell'esecuzione.
- Aggiunta nella sezione di tipo EMU la possibilità di lanciare più funzioni di emulazione in sequenza. Il sistema aspetta la risposta da ogni funzione prima di lanciare la successiva.
- Aggiunto l'attributo HEIGHT nella sintassi delle celle grafiche in modo da potere specificare  in altezza una percentuale della cella da colorare.
- Risolto un problema sulla matrice di aggiornamento che si verificava durante il movimento con i tasti.
- Risolto un errore sulla matrice di aggiornamento. Veniva emesso un messaggio di operazione pendente anche nel caso di inserimento automatico su matrice vuota.
- Risolto un errore sulla matrice di aggiornamento. In caso di messaggio di errore su cancellazione e annullamento non veniva selezionato nella combobox l'indice giusto.
- Risolto un problema sulla matrice di aggiornamento. Non venivano annullate le modifiche pendenti alla cancellazione dell'operazione in alcuni casi.

## Versione V2R2M061003-04G Stable 11/12/2006

- Modificata una parte di gestione della paginazione in modo da contemplare altri bottoni e comandi. Raffinata anche la parte di merging dell'XML.
- Risolto un problema sulla matrice di aggiornamento relativo ai messaggi.
- Aggiunti altri tipi di separatori nella definizione della cella di tipo grafico. In particolare freccia (ARW) e griglia (GRID).
- Modificata la gestione dei colori della cella di tipo grafico. Ora è possibile definire colore e spessore anche per i separatori.
- Risolto un problema che generava un xml non valido in alcuni casi durante la paginazione dell'albero.
- Rifinito la generazione dell'immagine della cella grafica.
- Aggiunti gli attributi di colore cablati,  *DPYELLOW,*DPRED,*DPGREEN,*DPBLU,*DPSELECTION per usare le sfumature di colore identiche ai campi della matrice anche nell'XML di definizione delle celle grafiche.

## Versione V2R2M061003-04F Stable 05/12/2006

- Aggiunti nuovi tipi di separatori nella definizione della cella di tipo grafico. In particolare freccia (ARW) e una griglia (GRID).
- Modificata la gestione dei colori della cella di tipo grafico. Ora è possibile definire colore e spessore anche per i separatori.
- Risolto un problema che generava un xml non valido o cmq sbagliato in alcuni casi durante la paginazione. In particolare nell'albero.
- Fissato un errore durante la generazione dell'immagine della cella grafica.
- Aggiunti gli attributi di colore cablati (ad esempio, *DPYELLOW) per dare anche nell'XML di definizione delle celle graficheall'utente la possibilità di utilizzare le sfumature di colore identiche a quelle usate come default nei campi della matrice.

## Versione V2R2M061003-03G Stable 01/12/2006

- Risolti alcuni problemi di cambio riga che si verificavano al posizionamento tra colonne bloccate.
- Aggiunto un attributo di setup per impostare il ritorno ad inizio record dopo la pressione del tasto invio nella matrice di aggiornamento.
- Aggiunto un attributo nel setup di matrice che permette di evidenziare il record corrente.
- Implementata la gestione delle colonne con grafo (di tipo oggetto J4 BAR) nella matrice. La documentazione specifica è presente nella documentazione di Looc.up.
- Risolto un problema sulla esportazione di Excel di una matrice con le intestazioni su più linee. Veniva generato un carattere illeggibile a fine riga.
- Risolto un problema sulle formule nelle matrici. Veniva generato un access violation nel caso in cui ci fosse un operando negativo e una sottrazione con 0.
- Risolto un possibile problema nella gestione delle funzioni di emulazione con ritorno nelle ricerche da matrice di aggiornamento.

## Versione V2R2M061003-03F Stable 28/11/2006

- Paginazione nella matrice :  Definita la funzione che accoda i dati e anche la funzione associata al bottone di paginazione, che  può cambiare in base a quanto definito dal servizio di volta in volta.
- Risolto un problema segnalata sulle matrici di aggiornamento. Andava in errore se si modificava un numero in cui era presente il separatore delle migliaia.
- Modificato la gestione del blocco delle colonne da setup di aggiornamento per permettere cmq la navigazione con il mouse (popup compreso) ma lasciando lo spostamento con la tastiera bloccato.
- Risolto un problema sulla matrice di aggiornamento. Non veniva gestito correttamente l'evento INIT in alcuni casi specifici.
- Risolto un problema sul cambio dei Bottoni da uipopup al caricamento di una scheda.
- Modificata parte la gestione degli UIPOPUP in modo da dare meno problemi sul cambio dei fuochi tra sezioni. Spostata la logica sul cambio tabsheet e adattato il resto del codice.- Risolto un problema sulla conversione dei decimali nella matrice di aggiornamento. Per numeri molto piccoli (quinto decimale) veniva passato ad AS400 il numero in notazione scientifica, e quindi interpretato erroneamente dal servizio di aggiornamento.
- Sezione EMU :  Cambiata la comunicazione. Ora predisposta per il futuro interscambio di informazioni, variabili o semplici chiamate con ritorno tra emulatore e scheda.
- Risolto un problema nella matrice di aggiornamento. Se la matrice è vuota il primo inserimento veniva effettuato due volte.
- Risolto un problema nella matrice di aggiornamento con setup multipli. Dopo avere cancellato un record cambiando setup veniva comunque mantenuto il record cancellato.
- Risolto un problema nella matrice di aggiornamento che impediva il reinserimento di un record se dopo cancellazione non erano rimasti altri record.


## Versione V2R2M061003-03E Stable 20/11/2006

- Risolto un problema sulla matrice di aggiornamento che impediva il corretto editing di un campo in particolari condizioni.
- Aggiunta una sezione di tipo EMU in cui è possibile specificare una o più chiamate all'emulatore. La sezione provederà ad aprire le schermate di emulazione al caricamento.
- Risolto un problema che generava un Access Violation se veniva salvato il primo setup su una sezione di tipo DYN.
- Risolto un problema relativo al click nella matrice di aggiornamento se presente un dinamismo associato allo stesso evento.
- E' ora possibile ridefinire nell'XML di setup della matrice di aggiornamento la funzione ricerca associata ad un campo. E' possibile anche specificare un carattere chiave a cui associare quella particolare ricerca.
- Risolto un problema sui nomi dei medesimi setup salvati tramite i tasti Salva e Salva come Default.


## Versione V2R2M061003-03D Stable 09/11/2006

- Realizzato la comunicazione per il precontrollo di esistenza degli oggetti in una matrice di aggiornamento. E' possibile specificare all'interno dell'XML di setup di aggiornamento se per un campo è abilitato il controllo preventivo del valore da parte di Smetray.
- Risolto un problema di chiamata ciclica tra due funzioni, che si verificava se per errore in una scheda veniva definito un bottone da UIpopup con funzione standard (ad esempio pressione del tasto F12) e tasto funzionale associato standard (ad esempio lo stesso F12). Ovviamente questa definizione non era contemplata.
- Risolto un problema  che si verificava all'aggiornamento della sezione :  non venivano distrutti i pulsanti UIPOPUP e quindi duplicati per sbaglio.
- Implementato il dettaglio del record di matrice. Ora premendo CTRL-D viene aperta una finestra contenente il record selezionato.
- Aggiunto l'attributo "AlwaysUpdate" nel Xml di setup della matrice di aggiornamento in modo da consentire l'aggiornamento automatico anche se non sono stati cambiati i valori di default di inserimento.

## Versione V2R2M061003-02C Stable 27/10/2006

- Implementata la nuova gestione dei popup e bottoni generati da nodo UIPopup. Vengono visualizzati anche i popup e i bottoni delle sottoschede e viene aggiornata la barra a seconda della sezione che ha il fuoco.
- Modificato radicalmente il codice che impostava le stringhe del popup in modo da fare il preventivamente il merging. In questo modo ogni sezione ha una stringa di popup che contiene quelle delle sezioni precedenti in cui è inclusa.
- Risolto un problema relativo alla nuova gestione dei UIPopup. Veniva per sbaglio replicato in alcuni casi il primo popup se presente.
- Implementato un sistema di Tooltip a livello di record selezionato per la matrice.
- Aggiunto l'attributo DetailHint nel setup di matrice per attivare il nuovo Tooltip di record.

## Versione V2R2M061003-02B Stable 23/10/2006

- Risolto un problema di internazionalizzazione relativo ai numeri (separatore decimale).
- Risolto un problema di internazionalizzazione segnalato relativo all'encoding della data (Separatori e posizioni).
- Aggiunta la gestione degli oggetti variabili nel INPUT panel.
- Modificato l'utilizzo dell'attributo UpdSvc della matrice. Era trattato come bloccante delle funzionalità di aggiornamento se nullo o non specificato. Ora invece l'attributo bloccante è ReadOnly.
- Aggiunta la funzionalità di apertura della scheda al click dell'icona in input panel o, se il campo è vuoto, della ricerca.
- Risolto un problema di scrolling nei campi della matrice di aggiornamento con colonne non editabili.
- Risolto un errore che si generava in caso di barra dei setup non esistente durante la cancellazione della operazione di salvataggio di un setup utente.
- Aggiunto un nuovo invio delle segnalazioni. Ora, se presente, viene usato Outlook per inviare la mail. In caso contrario viene utilizzato il metodo già conosciuto.
- Risolto un problema che si verificava quando veniva estratto il nome utente di windows dal sistema. In alcuni casi la stringa veniva terminata impedendone la concatenazione.
- Modificata la gestione della barra dei setup in modo da apparire anche se la matrice è in modalità deferred update ma priva di setup multipli.
- Creata ed unificata la gestione dei bottoni di Smetray per quel che riguarda funzioni di base e associazione dei tasti funzione. Ora è possibile sia tramite nodo UIPOPUP nell'XML, sia tramite bottoniera ridefinire i bottoni in modo da replicare o sostituire le funzioni di base associate ai tasti funzione standard.
- Aggiunta la gestione dell'oggetto J1PATHFILEC e J1PATHDIRC controllati dal client Loocup per quel che riguarda l'esistenza dell'oggetto.
- Realizzato la gestione delle formule nella matrice, per subtotali e totali. La documentazione specifica è disponibile con SMEDEV.
- Implementata la gestione dell'ordine delle colonne nel modulo di esportazione in Excel, ovviamente solo se l'esportazione viene da matrice.

## Versione V2R2M061003-01B Stable 05/10/2006

- Corretta chiamata al gestore del setup del componente scheda :  veniva mostrato il messaggio "Errore questionario non definito"
- Corretto errore di timeout in richiamo gestore setup (servizio JA_00_01). Nota tecnica :  portato timeout del GetSynchronousXml a 60 secondi
- Corretto Access Violation nell'emissione del Popup relativo all'intestazione di colonna di una matrice.

## Versione V2R2M061003-01A Stable 03/10/2006

- sostituita la chiamata non standard al servizio JA_SET con quella standard JA_00_01
- il messaggio "Setup utente salvato"  veniva mostrato anche se, nell'operazione salva con nome, si decideva di annullare.
- Modificati i pulsanti della barra dei setup di matrice in modo da avere il salvataggio corrente e quello di default con funzionalità diverse.
- Modificato il comportamento del popup di oggetto nel caso in cui venisse richiesto su una riga di raggruppamento della matrice.
- Risolti due problemi sulla matrice che si verificavano se presenti caratteri non dell'alfabeto Latin-1.
- Risolto il problema della finestra fantasma che faceva continuamente perdere il fuoco alle finestre di Smetray.
- Risolto un problema del popup di oggetto che impediva la chiamata corretta delle funzioni di aggiunta a preferiti, apertura della funzione associata etc. etc. Venivano indicizzate in maniera sbagliata le voci di menù.
- Risolto un problema relativo alle ricerche nella matrice di aggiornamento per la data.
- Rinforzata la gestione dei fuochi.
- Risolto un problema di fuochi in smetray sulle chiamate SCO.

# Informazioni su Rilasci Componente Scheda (precedente a V2R2M061003-01A)
## Versione V2R2M060410-04F Beta 27/09/2006

- sostituita la chiamata non standard al servizio JA_SET con quella standard JA_00_01
- il messaggio "Setup utente salvato"  veniva mostrato anche se, nell'operazione salva con nome, si decideva di annullare.

## Versione V2R2M060410-03I Stable 08/09/2006

- Risolto il problema della finestra fantasma che faceva continuamente perdere il fuoco alle finestre di Smetray.
- Risolto un problema di fuochi in smetray sulle chiamate SCO.

## Versione V2R2M060410-04B Beta 31/07/2006

- Aggiunto il caricamento ed il salvataggio del setup di Smetray da AS400.
- Aggiunte due voci nel sistem menu delle finestre di scheda, per il caricamento e gestione dei setup di Smetray.
- Risolto un problema nella nuova gestione dell'expression solver in modo da rendere più stabile la sintassi ed eventuali errori su di essa.
- Aggiunta la gestione dei nodi UserSetup multipli nell'xml di componente.
- Modificato la gestione dei tasti funzionali nella matrice di aggiornamento in modo da consentire al servizio di aggiornamento di risettarli ad ogni comunicazione.
- Risolto un problema che generava la duplicazione della barra dei tasti funzionali nell'input panel se accompagnato da servizio di aggiornamento.
- Risolto un problema riguardante l'expression solver e alcuni caratteri particolari (parentesi tonde).
- Realizzata la gestione dei setup utente multipli, mediante pulsante con popup per la selezione.
- Abilitata la possibilità di gestire matrici con più fonti di dati. E' necessario che gli xml che compongono i dati facciano riferimento agli stessi set di colonne.
- Risolto un problema sul pannello di stampa della matrice in modo da allineare i subtotali se nella matrice sono allineati.
- Risolto un problema sulla matrice che si manifestava al caricamento se sono impostati determinati filtri (NOT).
- Risolto un problema di autorizzazioni :  era necessario che l'utente connesso al PC avesse i privilegi di amministratore della macchina a causa di un file scritto nella root del sistema erroneamente.
- Modificato l'aggiornamento della matrice in modo da gestire come nuovo inserimento un record vuoto completo dei soli valori iniziali.
- Risolto un problema di conversione dei valori iniziali della matrice di aggiornamento.
- Risolti alcuni problemi inerenti alle matrici di aggiornamento e al workflow.
- Ripristinato l'inserimento di un record vuoto in caso di matrice di aggiornamento priva di record.
- Risolto un problema legato al pulsante dei setup multipli utente con dropdown.
- Risolto un problema sull'input panel e i campi di output legati ad una matrice ma presenti in un file video.
- Aggiunta la possibilità di identificazione di un record nell'input panel legato a matrice anche in assenza di campo Id nascosto presente nel file video. Questo risolve un problema sugli attributi di eccezione in caso di errore.
- Risolto un problema sulla assegnazione del titolo nella stampa di matrice. Non veniva più mantenuta in alcuni casi l'impostazione utente.
- Modificato il System Info di Smetray in modo da non dovere allocare una istanza di openoffice per stabilirne la versione. Questo dava in alcuni casi dei problemi.
- Risolto un problema di sincronia tra i bottoni dei setup utente multipli e le voci di menù.
- Risolto un problema sulla esportazione in excel di matrici in cui sono specificati nel setup le colonne e il loro ordine.
- Aggiunti due attributi nel setup di matrice per bloccare le colonne a destra o a sinistra.

## Versione V2R2M060410-03H Stable 20/07/2006

- Risolto un problema di autorizzazioni :  era necessario che l'utente connesso al PC avesse i privilegi di amministratore della macchina a causa di un file scritto nella root del sistema erroneamente.

## Versione V2R2M060410-03G Stable 10/07/2006

- Risolto un problema nella nuova gestione dell'expression solver in modo da rendere più stabile la sintassi ed eventuali errori su di essa.

## Versione V2R2M060410-04A Beta 07/07/2006

- Risolto un problema che impediva la corretta apertura di editor, browser e passaggio ad altri componenti nel caso in cui, all'interno della documentazione si apriva un link "interno".
- Corretto un difetto nella sezione HTM che non mostrava l'XML dell'ultima pagina aperta in un browser.
- Risolto un problema sulla navigazione nei campi bloccati della matrice di aggiornamento.
- Risolto un problema sulle autorizzazioni dei menù di sezione. Alcune voci non erano gestite correttamente ed erroneamente autorizzate.
- Risolto un problema che generava un errore di tipo Access Violation sulla matrice a causa della presenza di caratteri non in lingua italiana.
- Risolto un problema sulla Matrice che causava lo scattare dell'evento "ChangeRow" alla apertura della matrice anche senza la presenza dell'attributo SelFirst nel setup.
- Risolto un problema di caratteri non validi nei nomi di campi dell'Input Panel.
- Risolto un problema nella stampa della matrice. Venivano riportati erroneamente anche i valori numerici a 0 che non sono visibili nella matrice stessa.
- Realizzata la parte di interazione con la nuova gestione dei Setup in modo da applicare correttamente un setup dopo che è stato scelto nel pannello di gestione.
- Ristrutturato completamente l'expression solver, in quanto la sintassi era rimasta limitata. E' ora possibile specificare gli operandi usando gli apici. Questo consente di confrontare frasi contenenti spazi ed altri caratteri altrimenti non validi. E' anche possibile usare *BLANK nei confronti per indicare un operando nullo. La nuova sintassi affianca quella vecchia MA non può essere usata contemporaneamente.
- Risolto un problema sulla matrice in caso di caricamento di setup multipli. Non veniva scelto il setup corretto sotto alcune condizioni.
- Aggiunta la gestione dei pulsanti di salvataggio con nome e apertura nella bottoniera dei setup.
- Aggiunte le funzioni per il richiamo delle nuove modalità di apertura, salvataggio e gestione dei setup.
- Abilitato il bottone generale F17 in modo da gestire il setup della sezione che ha il fuoco. Rimosso quello nella bottoniera dei setup.

## Versione V2R2M060410-03F Stable 07/07/2006

- Risolto un problema che impediva la corretta apertura di editor, browser e passaggio ad altri componenti nel caso in cui, all'interno della documentazione si apriva un link "interno".
- Corretto un difetto nella sezione HTM che non mostrava l'XML dell'ultima pagina aperta in un browser.
- Risolto un problema sulla navigazione nei campi bloccati della matrice di aggiornamento.
- Risolto un problema sulle autorizzazioni dei menù di sezione. Alcune voci non erano gestite correttamente ed erroneamente autorizzate.
- Risolto un problema che generava un errore di tipo Access Violation sulla matrice a causa della presenza di caratteri non in lingua italiana.
- Risolto un problema sulla Matrice che causava lo scattare dell'evento "ChangeRow" alla apertura della matrice anche senza la presenza dell'attributo SelFirst nel setup.
- Risolto un problema di caratteri non validi nei nomi di campi dell'Input Panel.
- Risolto un problema nella stampa della matrice. Venivano riportati erroneamente anche i valori numerici a 0 che non sono visibili nella matrice stessa.
- Realizzata la parte di interazione con la nuova gestione dei Setup in modo da applicare correttamente un setup dopo che è stato scelto nel pannello di gestione.
- Ristrutturato completamente l'expression solver, in quanto la sintassi era rimasta limitata. E' ora possibile specificare gli operandi usando gli apici. Questo consente di confrontare frasi contenenti spazi ed altri caratteri altrimenti non validi. E' anche possibile usare *BLANK nei confronti per indicare un operando nullo. La nuova sintassi affianca quella vecchia MA non può essere usata contemporaneamente.
- Risolto un problema sulla matrice in caso di caricamento di setup multipli. Non veniva scelto il setup corretto sotto alcune condizioni.
- Aggiunta la gestione dei pulsanti di salvataggio con nome e apertura nella bottoniera dei setup.
- Aggiunte le funzioni per il richiamo delle nuove modalità di apertura, salvataggio e gestione dei setup.
- Abilitato il bottone generale F17 in modo da gestire il setup della sezione che ha il fuoco. Rimosso quello nella bottoniera dei setup.

## Versione V2R2M060410-03E Beta 28/06/2006

- Collegato input panel alla matrice con possibilità di visualizzare record per record usando i tasti PGUP e PGDOWN.
- Ultimata la prima versione completa con aggiornamento del componente InputPanel.
- Aggiunta la gestione degli errori nell'input panel. Ora in caso di aggiornamento con segnalazione di errori vengono illuminati i campi errati.
- Aggiunta la gestione del tasti INS e SHIFT+CANC per abilitare l'inserimento e la cancellazione di record nell'input panel.
- Concluso l'input panel con l'aggiunta dei tasti di cancellazione ed inserimento alla toolbar  (next, previous e invio).
- Modificata la gestione dei fuochi per legare finestre di dialog java a form delphi.
- Implementato un gestore delle tabelle a livello di scheda.
- Aggiunta la possibilità di specificare nel setup di matrice, input panel, grafico, una tabella matriciale da condividere in più sezioni.
- Risolto un problema sulla matrice di aggiornamento sull'inserimento multiplo. Venivano raddoppiate le operazioni con conseguenti problemi.
- Modificata la gestione del refresh di scheda in modo da gestire il parametro G(SFI) di una chiamata, come refresh della stessa scheda ma tramire dati di una altra funzione.

## Versione V2R2M060410-02F Beta 28/06/2006

- Risolto un problema sulla matrice di aggiornamento sull'inserimento multiplo. Venivano raddoppiate le operazioni con conseguenti problemi.
- Risolto un problema di scorrimento record sul pannello di input.

## Versione V2R2M060410-03D Beta 14/06/2006

- Aggiunta la gestione di un Setup di scheda nel nodo layout in cui per ora è possibile specificare dimensione, posizione e altri comportamenti
- Aggiunta la possibilità di creazione di un video per l'input panel che rifletta i campi di una matrice.
- Risolto un problema sull'input panel in presenza di XML multiplo.
- Risolto un problema di "traslazione" dei codici di autorizzazione in Smetray.
- Risolto un problema sulla matrice di aggiornamento durante la ricezione dei campi di INIT. Non veniva correttamente svuotato il buffer dei valori.
- Ultimata la gestione dei tasti funzione dell'aggiornatore. La matrice in aggiornamento ora è in grado i visualizzare i bottoni.
- Modificata la sezione HTM in modo da potere aprire i link UILINK all'interno della stessa invece che chiamare il browser java esterno.
- Aggiunta la possibilità di specificare tramite specifica D.FUN.STD fonti dati multiple per tutti i componenti.
- Modificato lievemente la sezione EXE in modo da forzare l'utilizzo di un programma specifico.

## Versione V2R2M060410-02E Stable 14/06/2006

- Risolto un problema di "traslazione" dei codici di autorizzazione in Smetray.
- Modificato lievemente la sezione EXE in modo da forzare l'utilizzo di un programma specifico.
- Risolto un problema sulla matrice di aggiornamento durante la ricezione dei campi di INIT. Non veniva correttamente svuotato il buffer dei valori.

## Versione V2R2M060410-02D Stable 07/06/2006

- Fissate molte segnalazioni sulla matrice di aggiornamento.

## Versione V2R2M060410-03C Beta 31/05/2006

- Risolto un problema sulla nuova gestione del riconoscimento delle versioni di Excel.
- Aggiunte le autorizzazionisu alcune voci di menù di smetray che prima erano cablate.
- Risolto un problema di sostituzione dei caratteri nelle intestazioni di un foglio excel se nella matrice ha intestazioni a righe multiple.
- Modificata la DLL dei fuochi per irrobustire la nuova gestione e riconoscimento delle finestre figlie.
- Modificata la dll dei fuochi in modo da non togliere il fuoco ad altre applicazioni esterne a loocup.
- Risolto un problema sui menù, in caso di script da AS non corretto.
- Modificata la gestione dei caratteri speciali dell'XML nella comunicazione con il servizio di aggiornamento della matrice.
- Risolto un problema su Excel per quanto riguarda i salvataggi dei fogli.
- Risolto un problema sui raggruppamenti in Excel che non permetteva una visualizzazione corretta in taluni casi.
- Modificata la scheda per la gestione dei fuochi e interazione coi dialog java.
- Risolti due problemi correlati delle sezioni DYN in presenza di setup multipli e setup utente. Nel primo caso si aveva un AV nel secondo non veniva caricato correttamente il setup salvato.
- Risolto un piccolo errore nell'esportazione in excel che generava una non completa compilazione del foglio.
- Aggiunti i livelli di autorizzazione corretti e le traduzioni alle voci cablate del menù della scheda.
- Modificato il modulo di esportazione in Excel in modo da richiamare la visualizzazione del file generato con esattamente la versione di excel per cui è stato generato il file.

## Versione V2R2M060410-02C Stable 31/05/2006

- Risolto un problema sulla nuova gestione del riconoscimento delle versioni di Excel.
- Aggiunte le autorizzazionisu alcune voci di menù di smetray che prima erano cablate.
- Risolto un problema di sostituzione dei caratteri nelle intestazioni di un foglio excel se nella matrice ha intestazioni a righe multiple.
- Modificata la DLL dei fuochi per irrobustire la nuova gestione e riconoscimento delle finestre figlie.
- Modificata la dll dei fuochi in modo da non togliere il fuoco ad altre applicazioni esterne a loocup.
- Risolto un problema sui menù, in caso di script da AS non corretto.
- Modificata la gestione dei caratteri speciali dell'XML nella comunicazione con il servizio di aggiornamento della matrice.
- Risolto un problema su Excel per quanto riguarda i salvataggi dei fogli.
- Risolto un problema sui raggruppamenti in Excel che non permetteva una visualizzazione corretta in taluni casi.
- Modificata la scheda per la gestione dei fuochi e interazione coi dialog java.
- Risolti due problemi correlati delle sezioni DYN in presenza di setup multipli e setup utente. Nel primo caso si aveva un AV nel secondo non veniva caricato correttamente il setup salvato.
- Risolto un piccolo errore nell'esportazione in excel che generava una non completa compilazione del foglio.
- Aggiunti i livelli di autorizzazione corretti e le traduzioni alle voci cablate del menù della scheda.
- Modificato il modulo di esportazione in Excel in modo da richiamare la visualizzazione del file generato con esattamente la versione di excel per cui è stato generato il file.

## Versione V2R2M060410-03B Beta 17/05/2006

- Risolto un problema relativo al caricamento di un menù sezione di default in assenza di uno script SCP_CLO/DEFAULT che lo contiene.
- Risolto un problema con l'esportazione in Excel. Ora il nome del foglio viene preso dal nome del tab da cui è esportato ma limitato a 31 caratteri con sostituzione dei caratteri proibiti da Excel.
- Risolto un problema che generava un errore di tipo "List Index Out of Bound" alla costruzione della sottosezione.
- Aggiunta per le label la gestione delle date che vengono ora convertite in formato ShortDate di Windows. Questo viene fatto solo se non è presente l'attributo Testo della label e l'attributo Codice contiene la data in formato Smeup come indicata negli attributi Tipo e Parametro.

## Versione V2R2M060410-02B Stable 17/05/2006

- Risolto un problema relativo al caricamento di un menù sezione di default in assenza di uno script SCP_CLO/DEFAULT che lo contiene.
- Risolto un problema con l'esportazione in Excel. Ora il nome del foglio viene preso dal nome del tab da cui è esportato ma limitato a 31 caratteri con sostituzione dei caratteri proibiti da Excel.
- Risolto un problema che generava un errore di tipo "List Index Out of Bound" alla costruzione della sottosezione.
- Aggiunta per le label la gestione delle date che vengono ora convertite in formato ShortDate di Windows. Questo viene fatto solo se non è presente l'attributo Testo della label e l'attributo Codice contiene la data in formato Smeup come indicata negli attributi Tipo e Parametro.

## Versione V2R2M060410-03A Beta 05/05/2006

- Risolto un problema sulla preview di stampa della matrice.
- Risolto un problema relativo alla presenza di caratteri " e ; all'interno di celle di aggiornamento.
- Aggiunto l'attributo LabelAngle nel setup di grafico in modo da specificare l'orientamento delle etichette dell'asse orizzontale del grafico.
- Aggiunta la gestione dei tasti funzionali nel componente InputPanel.
- Aggiunta la gestione del fuoco all'interno del componente Inputpanel tramite tasto TAB.
- Aggiunta la variabile *ALLSH in ogni sezione che contiene le informazioni di tutte le variabili della sezione stessa.
- Risolto un problema sull'utilizzo del TitleLock sui dinamismi.
- Risolto un problema relativo alla presenza di caratteri particolari (<>=) nelle celle aggiornabili di una matrice.
- Aggiunto il passaggio della variabile Tx nel componente bottoniera.
- Gestiti gli attributi video nel componente Input Panel.
- Gestite le maschere numeriche (e non) nei campi di input del componente INP.
- Gestiti gli indicatori nel componente INP.
- Modificato il servizio di reperimento delle informazioni del client di delphi. Ora restiuisce un xml di tipo griglia contenente le informazioni. Inoltre è stato snellito enormemente il processo di riconoscimento delle version di office in modo da non causare più rallentamenti al caricamento di Smetray.
- Risolto un problema di esportazione in excel delle matrici di aggiornamento.

## Versione V2R2M060410-02A Stable 05/05/2006

- Risolto un problema sulla preview di stampa della matrice.
- Risolto un problema relativo alla presenza di caratteri " e ; all'interno di celle di aggiornamento.
- Aggiunto l'attributo LabelAngle nel setup di grafico in modo da specificare l'orientamento delle etichette dell'asse orizzontale del grafico.
- Aggiunta la gestione dei tasti funzionali nel componente InputPanel.
- Aggiunta la gestione del fuoco all'interno del componente Inputpanel tramite tasto TAB.
- Aggiunta la variabile *ALLSH in ogni sezione che contiene le informazioni di tutte le variabili della sezione stessa.
- Risolto un problema sull'utilizzo del TitleLock sui dinamismi.
- Risolto un problema relativo alla presenza di caratteri particolari (<>=) nelle celle aggiornabili di una matrice.
- Aggiunto il passaggio della variabile Tx nel componente bottoniera.
- Gestiti gli attributi video nel componente Input Panel.
- Gestite le maschere numeriche (e non) nei campi di input del componente INP.
- Gestiti gli indicatori nel componente INP.
- Modificato il servizio di reperimento delle informazioni del client di delphi. Ora restiuisce un xml di tipo griglia contenente le informazioni. Inoltre è stato snellito enormemente il processo di riconoscimento delle version di office in modo da non causare più rallentamenti al caricamento di Smetray.
- Risolto un problema di esportazione in excel delle matrici di aggiornamento.

## Versione V2R2M060410-02C Beta 27/04/2006

- Il passaggio delle informazioni (XML di Setup) della matrice di aggiornamento è stata generalizzato in modo da essere usato in ogni componente ed integrato con la compilazione di valori iniziali del componente INP.
- Risolto un problema che impediva l'attivazione degli eventi legati da script di scheda alle voci di popup.
- Input Panel :  la creazione avviene molto più velocemente e senza i flickering a video.
- Risolto un problema sull'albero ad espansione dinamica che invertiva l'ordinamento ad ogni espansione successiva se non vi era presente alcun ordinamento.
- Risolto alcuni problemi relativi alla nuova gestione dei menù dei tab di smetray.
- Modificata l'assegnazione dei nomi dei file temporanei nell'esportazione di Excel in modo da essere ordinati per data.
- Aggiunto il nome della sezione come nome di foglio nell'esportazione in excel.
- Modificato il sistema di sottototalizzazione nell'esportazione in Excel.
- Modificata la matrice di aggiornamento per consentire il copia ed incolla da excel anche senza deferred update.
- Fissato un problema che generava un access violation sul caricamento di un tabsheet di un tabalbero sotto certe condizioni.
- Ristrutturata la gestione del menù di sezione e della sua lettura da AS400. E' stato deciso di attribuire il servizio JA_00_12 a Delphi.

## Versione V2R2M060410-01C Stable 27/04/2006

- Il passaggio delle informazioni (XML di Setup) della matrice di aggiornamento è stata generalizzato in modo da essere usato in ogni componente ed integrato con la compilazione di valori iniziali del componente INP.
- Risolto un problema che impediva l'attivazione degli eventi legati da script di scheda alle voci di popup.
- Input Panel :  la creazione avviene molto più velocemente e senza i flickering a video.
- Risolto un problema sull'albero ad espansione dinamica che invertiva l'ordinamento ad ogni espansione successiva se non vi era presente alcun ordinamento.
- Risolto alcuni problemi relativi alla nuova gestione dei menù dei tab di smetray.
- Modificata l'assegnazione dei nomi dei file temporanei nell'esportazione di Excel in modo da essere ordinati per data.
- Modificato il sistema di sottototalizzazione nell'esportazione in Excel.
- Ristrutturata la gestione del menù di sezione e della sua lettura da AS400. E' stato deciso di attribuire il servizio JA_00_12 a Delphi.

## Versione V2R2M060410-01B Stable 20/04/2006

- Fissato un problema che generava un access violation sul caricamento di un tabsheet di un tabalbero sotto certe condizioni.
- Modificata la matrice di aggiornamento per consentire il copia ed incolla da excel anche senza deferred update.
- Aggiunto il nome della sezione come nome di foglio nell'esportazione in excel.

## Versione V2R2M060410-02B Beta 12/04/2006

- Risolto un problema di aggiornamento che si verifica con il cambio ambiente da scheda.
- Aggiunto l'attributo ShowGrid (Yes/No Default : No) per la visualizzazione delle righe di griglia della matrice.
- Risolto un problema di loop infinite nelle matrici le cui colonne indirette contengono più parentesi quadre.
- Corretto un problema sulla visualizzazione delle icone associate a file di immagini.
- Risolto un problema introdotto con l'ultimo rilascio che impediva la sostituzione delle variabili nei testi dei bottoni.
- Aggiunto la risoluzione delle variabili negli altri attributi del bottone.

## Versione V2R2M060410-02A Beta 10/04/2006

- Aggiunto l'attributo EnableRefresh per disabilitare il menù aggiorna nella specifica G.SUB di sottosezione.
- Aggiunta la possibilità di modificare il comportamento del pulsante di chiusura delle finestre della scheda tramite la definizione di una voce J1-KEY-*CLOSE nella specifica I.POP.
- Aggiunto l'attributo Enabled nella specifica G.DIN in modo da potere disabilitare o abilitare il dinamismo tramite variabili.
- La scheda utilizza le icone definite nel filesystem quando si riferisce ad un oggetto che ne fa parte.
- Risolto un problema sulla risoluzione delle variabili nella funzione da eseguire di un bottone. Veniva erroneamente effettuata la sostituzione prima dell'esecuzione dell'evento di pressione del tasto.
- Aaggiunto l'attributo Upd nell'XML di Line della risposta da AS400 per l'aggiornamento della matrice. Se Upd è uguale a No, l'update non viene eseguito.
- Modificato il comportamento del menu di popup nella matrice di aggiornamento per le voci taglia, incolla, duplica e cancella abilitandole in base al setup.
- Ho aiutato Luigi R. con alcuni problemi relativi all'emulazione. Ho una cosa da chiedere a Marco domani.
- Risolto un problema segnalato sulla matrice con raggruppamenti. Non veniva correttamente visualizzata in modalità collassata a causa di un problema sugli indici dei record per gli attributi selfirst e selitem.
- Aggiunta la gestione della barra comandi tramite pressione del tasto F21 (o apposito bottone) nella scheda.
- Risolto un problema che impediva al grafico di mantenere le impostazioni di sorting e raggruppamento in caso di date aggregate.
- Aggiunta la sezione di tipo EXE alla scheda. Questa sezione esegue semplicemente l'apertura del file specificato nell'xml dei dati da parte del sistema operativo.
- Modificata la finestra di errore ch si presenta quando i dati contengono un xml errato in modo da essere più leggibile.

## Versione V2R2M060410-01A Stable 10/04/2006

- Aggiunto l'attributo EnableRefresh per disabilitare il menù aggiorna nella specifica G.SUB di sottosezione.
- Aggiunta la possibilità di modificare il comportamento del pulsante di chiusura delle finestre della scheda tramite la definizione di una voce J1-KEY-*CLOSE nella specifica I.POP.
- Aggiunto l'attributo Enabled nella specifica G.DIN in modo da potere disabilitare o abilitare il dinamismo tramite variabili.
- La scheda utilizza le icone definite nel filesystem quando si riferisce ad un oggetto che ne fa parte.
- Risolto un problema sulla risoluzione delle variabili nella funzione da eseguire di un bottone. Veniva erroneamente effettuata la sostituzione prima dell'esecuzione dell'evento di pressione del tasto.
- Aaggiunto l'attributo Upd nell'XML di Line della risposta da AS400 per l'aggiornamento della matrice. Se Upd è uguale a No, l'update non viene eseguito.
- Modificato il comportamento del menu di popup nella matrice di aggiornamento per le voci taglia, incolla, duplica e cancella abilitandole in base al setup.
- Ho aiutato Luigi R. con alcuni problemi relativi all'emulazione. Ho una cosa da chiedere a Marco domani.
- Risolto un problema segnalato sulla matrice con raggruppamenti. Non veniva correttamente visualizzata in modalità collassata a causa di un problema sugli indici dei record per gli attributi selfirst e selitem.
- Aggiunta la gestione della barra comandi tramite pressione del tasto F21 (o apposito bottone) nella scheda.
- Risolto un problema che impediva al grafico di mantenere le impostazioni di sorting e raggruppamento in caso di date aggregate.
- Aggiunta la sezione di tipo EXE alla scheda. Questa sezione esegue semplicemente l'apertura del file specificato nell'xml dei dati da parte del sistema operativo.
- Modificata la finestra di errore ch si presenta quando i dati contengono un xml errato in modo da essere più leggibile.

## Versione V2R2M060117-03F Beta 03/04/2006

- Modificata la gestione dei messaggi di UNDO tra Java e Delphi in modo da potere avere come pagina iniziale solamente una scheda. Nel caso di prima scheda senza console la chiusura della stessa è possibile solo tramite F23 (pulsante esci).
- Aggiunta la possibilità di specificare nell setup di matrice di aggiornamento il nodo Config di configurazione contenente il parametro InitRow. Se presente il sistema richiederà ad ogni nuovo inserimento di record i valori di default al servizio.

## Versione V2R2M060117-03E Beta 31/03/2006

- Risolto un problema riguardante il mancato caricamento delle impostazioni di visibilità di colonna e di posizione di colonna dal setup utente di una matrice.
- La sezione IMG ora ha la possibilità di caricare immagini in formato TIFF non multipagina.
- Modificata la gestione delle icone degli oggetti J1 PATHFILE e J1 PATHDIR.
- Aggiunto un algoritmo di trasformazione dell'xml da griglia ad albero con griglia. Viene eseguito automaticamente se i dati di una sezione TRE vengono generato con la formattazione dell'Xml "Griglia".
- Aggiunto la possibilità di usare nodi action all'interno dell'xml di ogni componente e non solo nel componente VIR.
- Aggiunta al componente INP la tipizzazione, la trasparenza dell'icona oggetto che viene legata al campo di input corrispondente.
- Aggiunta l'oggettizzazione, le icone, i popupmenu e i colori al nuovo componente INPl. E' stata introdotta anche la gestione dell'EditCode come nell'emulatore.
- Aggiunto il caricamento della variabili di ambiente del sistema operativo alla partenza del modulo delphi. E' quindi possibile fare riferimento alle variabili all'interno di script di scheda usando la sintassi [*nomevariabile].
- La gestione delle Action è stata cambiata in modo da potere richiamare una funzione di refresh di una sezione che esegua una funzione scelta dal servizio invece di originale del componente.
- Risolto un problema nell'esportazione in Excel di una matrice. Ora non si verifica più il caso di mancata chiusura del processo excel una volta chiuso il foglio di calcolo. L'apertura del foglio di calcolo esportato ora viene eseguita dopo il salvataggio dello stesso.
- Risolto un problema sull'apertura di Excel durante la fase di riconoscimento della versione. Il processo rimaneva aperto ma inutilizzabile.
- Modificata la gestione dell'esportazione di una matrice in Excel versione precedente al 2003. In questo modo non si verifica più il problema di blocco di excel se un altro lavoro è già aperto.
- Aggiunta la sezione di tipo OCX in cui è possibile caricare dei controlli Active-X presenti sul client all'interno della scheda.
- Aggiunta la gestione del metodo "UNLOAD" nella sezione OCX. Se l'active-x è predisposto per avere una procedura di unload questa viene eseguita prima della chiusura della scheda che lo contiene.

## Versione V2R2M060117-03D Beta 20/03/2006

- Modificata la gestione della pressione del tasto F4 quando si è in una matrice di aggiornamento. Ora viene aperto direttamente il pannello di ricerca dell'oggetto.
- Modificata la matrice in modo da essere compatibile con i nuovi servizi relativi ai dati e all'aggiornamento.
- Aggiunta la nuova sezione di tipo INP (Input Panel) che consente di avere campi di inserimento e bottoni a cui sono collegati singolarmente gli eventi e i dinamismi (tramite script della scheda).
- Aggiunto l'attributo Source per la specifica G.DIN in modo da specificare il nome del sottocomponente per cui l'evento deve scattare.
- Modificata la scheda per utilizzare la nuova gestione delle icone e immagine da dll loocupicons.dll.
- Risolto un problema sulla stampa della matrice in presenza di setup multipli.
- Risolto un problema con il doppio click su albero. Veniva effettuata una chiamata all'emulatore non corretta.
- Risolto un problema sulla gestione delle icone nell'albero introdotto nei rilasci precedenti.
- Sistemato un problema con le date nella matrice. Ora se nei dati è presente il valore 99999999 (da parzializzazione) è trasformato in 31/12/9999 e correttamente accettato.
- Abilitata la possibilità di filtrare una matrice di aggiornamento. Modificato di conseguenza anche il taglia e incolla.

## Versione V2R2M060117-02I Stable 17/03/2006

- Corretto nella versione stabile di smetray un problema inerente all'esportazione in Excel.

## Versione V2R2M060117-02H Stable 15/03/2006

- Risolto un problema sulla stampa della matrice in presenza di setup multipli.
- Sistemato un problema con le date nella matrice. Ora se nei dati è presente il valore 99999999 (da parzializzazione) è trasformato in 31/12/9999 e correttamente accettato.

## Versione V2R2M060117-03C Beta 10/03/2006

- Tradotto in lingua inglese il pannello provvisorio delle immagini nella scheda.
- Risolto un problema che disabilitava la richiesta di salvataggio del foglio excel esportato da una matrice.
- Risolto un problema di "out of memory" che si verificava durante l'esportazione in Execel di matrici di aggiornamento molto grandi.
- Ottimizzate le prestazioni del componente Albero in presenza di icone.
- Risolto un errore di tipo "Access Violation" che si manifestava dopo il salvataggio di un setup utente in una sezione con un solo setup e senza nome. Premendo sul pulsante Default veniva generato l'errore e non applicato il setup.
- Aggiunto il supporto multilingua per le schede :  In caso che nell'xml di inizializzazione di smetray manchi la sezione delle lingue (AS400 non dispone del servizio per le lingue) viene letto un file XML di default.
- Risolto un problema sull'albero che si generava se il componente riceveva un XML sbagliato o non destinato al componente.
- Risolto un problema di sincronia tra dataset e xml di una matrice se di aggiornamento se viene cambiato il setup runtime.
- Modificata la gestione dei preferiti nella scheda per potere aggiungere alla lista le funzioni associate a TA-MEA.
- Risolto un problema sull'esportazione in excel che non prendeva in considerazione i formati delle colonne se veniva specificato nell'xml un oggetto variabile.
- Risolto un problema che generava un errore al click sul menù Aggiorna di un tabsheet di un TAB-ALBERO.

## Versione V2R2M060117-02G Stable 08/03/2006

- Risolto un problema sull'albero che si generava se il componente riceveva un XML sbagliato o non destinato al componente.
- Risolto un problema sull'esportazione in excel che non prendeva in considerazione i formati delle colonne se veniva specificato nell'xml un oggetto variabile.

## Versione V2R2M060117-03B Beta 27/02/2006

- Risolto un problema sulla scheda in caso di richiesta ACTION nell'xml di una sottosezione. Non veniva più analizzata l'azione corretta.
- Risolto un problema sulla ricerca in matrice di aggiornamento che alla pressione del tasto invio sottometteva il record all'AS.
- Risolto un problema sull'esportazione in Excel con versioni superiori a 2002. Il formato numerico non era correttamente formattato.

## Versione V2R2M060117-02F Stable 27/02/2006

- Risolto un problema sull'esportazione in Excel con versioni superiori a 2002. Il formato numerico non era correttamente formattato.

## Versione V2R2M060117-03A Beta 24/02/2006

- Risolto un problema sull'assegnazione del tasti che sostituiscono i tasti funzione base.
- Risolto un problema nell'esportazione di una matrice in Excel 2003 per il formato delle date.
- Corretta la generazione dello SpreadSheetML nell'esportazione della matrice in Excel senza password.
- Risolto un problema sui filtri della matrice quando la matrice è raggruppata. Ora mostra i valori corretti.
- Risolto il problema di inserimento di un record nella matrice di aggiornamento se questa è vuota. Ora se è di aggiornamento appare con una riga vuota fin dal caricamento.
- Risolto un problema che si verificava alla pressione del tasto del mouse su header di una matrice vuota.
- Risolto un problema che si verificava alla selezione dal menù di popup su header di una matrice vuota.
- Aggiunta la possibilità di selezionare un nodo di un albero dal testo tramite l'attributo SelName nel setup dell'albero.			
- Modificata la gestione dell'attributo SelItem dell'albero in modo da essere 1 based e non 0 based.		
- Risolto un problema sulla selezione dei nodi dell'albero se l'indice passato superava la lunghezza dell'albero.
- Aggiunta la gestione della stampa su pdf di semafori e cruscotti in maniera analoga a quanto fatto per il grafico. Viene generata l'immagine che è poi inclusa nel pdf.
- Sistemata l'icona delle finestre di smetray.
- Sistemato un errore che non disabilitava il menù "Visualizza come.." se non erano presenti componenti compatibili.

## Versione V2R2M060117-02E Stable 24/02/2006

- Risolto un problema sull'assegnazione del tasti che sostituiscono i tasti funzione base.
- Risolto un problema nell'esportazione di una matrice in Excel 2003 per il formato delle date.
- Corretta la generazione dello SpreadSheetML nell'esportazione della matrice in Excel senza password.
- Risolto un problema sui filtri della matrice quando la matrice è raggruppata. Ora mostra i valori corretti.
- Risolto il problema di inserimento di un record nella matrice di aggiornamento se questa è vuota. Ora se è di aggiornamento appare con una riga vuota fin dal caricamento.
- Risolto un problema che si verificava alla pressione del tasto del mouse su header di una matrice vuota.
- Risolto un problema che si verificava alla selezione dal menù di popup su header di una matrice vuota.
- Aggiunta la possibilità di selezionare un nodo di un albero dal testo tramite l'attributo SelName nel setup dell'albero.			
- Modificata la gestione dell'attributo SelItem dell'albero in modo da essere 1 based e non 0 based.		
- Risolto un problema sulla selezione dei nodi dell'albero se l'indice passato superava la lunghezza dell'albero.
- Aggiunta la gestione della stampa su pdf di semafori e cruscotti in maniera analoga a quanto fatto per il grafico. Viene generata l'immagine che è poi inclusa nel pdf.
- Sistemata l'icona delle finestre di smetray.
- Sistemato un errore che non disabilitava il menù "Visualizza come.." se non erano presenti componenti compatibili.

## Versione V2R2M060117-02D Beta 17/02/2006

- Risolto un problema nella matrice che impediva il corretto autofit delle colonne. Non veniva presa in considerazione la lunghezza del primo record.
- Risolto un problema nella matrice che non consentiva l'autofit delle colonne marcate 'H' (nascoste) ma forzate visibili tramite l'attributo di setup DefaultColumns.
- Cambiata la procedura di autofit delle singole colonne della matrice per avere maggiore precisione.
- Sistemato un problema che impediva il caricamento dell'XML di una sezione se il suo titolo veniva aggiornato dinamicamente e conteneva il carattere &.
- Sistemata la risoluzione delle variabili di sezione per funzionare correttamente in presenza del carattere &.
- Modificato il pannello di visualizzazione delle variabili in modo da visualizzare correttamente le variabili il cui valore contiene &.
- Sistemato un problema che impediva alla funzionalità di "ricerca" (F4) di ottenere correttamente il parametro (?XX non prendeva in considerazione XX).
- Risolto un problema che faceva bloccare la sezione matrice di una scheda al caricamento di una matrice con relazioni che facevano riferimento ad una matrice correlata non fornita nell'xml.
- Risolto un problema che bloccava il caricamento della matrice se nella tabella correlata erano presenti due relazioni duplicate.
- Modificato il codice della matrice per consentire la funzionalità di raggruppamento runtime anche con la matrice in aggiornamento.
- Risolto un problema che generava un "Access Violation" al click su alcune parti della matrice di aggiornamento.
- Risolto un problema sulla risoluzione dei link di tipo UILINK (proprietari di loocup) nella documentazione tramite componente HTML.
- Aggiunta la possibilità di gestire i dinamismi da Popup semplicemente aggiungendo la riga (o le righe) G.DIN sotto la specifica I.POP di definizione, analogamente a quanto avviene nelle sottosezioni G.SUB. sezioni. E' possibile usare tutte le opzioni del G.DIN tranne l'attributo When che è preimpostato a Click.
- Risolto un problema sui bottoni utente inseribili con la specifica I.POP. Se il bottone sostituiva un bottone standard, lo shortcut permetteva cmq di lanciare la funzione standard, causando in taluni casi la chiusura obbligatoria di loocup.
- Risolto un problema che si verificava se nella funzione associata ad una scheda erano presente parentesi tonde in numero non corretto (sintassi errata) causando un loop.
- Risolto un problema che non permetteva di ricavare i parametri corretti dall'attributo P di una funzione se all'interno erano presente delle parentesi tonde annidate.
- Modificato il modulo di esportazione in excel per non generare più documenti che salvati hanno una password ignota. Il foglio non viene più esportato in SpreadsheetML ma direttamente nel formato XLS.

## Versione V2R2M060117-01B Stable 13/02/2006

- Aggiornato il sistema di invio automatico delle segnalazioni :  Ora è possibili specificare i destinatari della segnalazione, salvare la segnalazione senza inviarla e forzare l'invio della segnalazione anche non in caso di errore (tramite l'apposita voce di menu').

## Versione V2R2M060117-02C Beta 08/02/2006

- Risolto un problema che impediva di all'evento UPDATE di scattare in caso di cancellazione del record.
- Modificata la getione dell'invio automatico delle segnalazioni di errore in modo che la finestrella di invio sparisca se l'invio fallisce.
- Limitata la grandezza del file di log di smetray ad 1 MB. (Prima non era gestito alcun limite).
- Aggiunta una funzionalità di error logging nella scheda in modo da tracciare l'ultimo errore avvenuto.
- Aggiornato il sistema di invio automatico delle segnalazioni :  Ora è possibili specificare i destinatari della segnalazione, salvare la segnalazione senza inviarla e forzare l'invio della segnalazione anche non in caso di errore (tramite l'apposita voce di menu').- Aiutato Gabriele A. con un problema sull'emulatore.
- Modificata la gestione del menu' di popup della sottosezione in modo che sia possibile cambiarne la forma e i contenuti. E' possibile aggiungere un nodo MenuTab nell'XML di setup iniziale che contenga dei nodi oggetto con parametro "MNUTAB", in modo da descrivere il menu' di popup.
- Risolti due errori introdotti nel precedente rilascio che causavano la non visualizzazione del componente grafico e la generazione di un messaggio di errore.
- Risolto un problema sulla funzionalità di invio segnalazioni automatiche :  il nome del file di log non era creato correttamente.
- Risolto un altro problema sul componente grafico che causava un errore di tipo "Access Violation" (non bloccante) alla pressione del tasto annulla sulla selezione di assi e serie.

## Versione V2R2M060117-02B Beta 26/01/2006

- Risolto un problema sulla matrice durante l'esportazione in Excel :  Ora dopo l'esportazione, la matrice viene riportata alle impostazioni precedenti di espansione/collassamento se raggruppata.
- Aggiunto un controllo che filtra il tipo di setup nelle sezioni e visualizza nella barra e nel menu' solo quelli del tipo corretto o compatibile.
- Standardizzata la barra dei setup per tutti i componenti.
- Aggiunta la gestione dell'attributo "i" nell'xml del componente albero in modo da potere specificare una icona personalizzata per quel nodo.
- Sistemati alcuni problemi di indice in caso di setup multipli con sezioni di tipo DYN.
- Aggiunto il reset della barra dei setup in caso di cambio di tipo di sezione all'interno della sezione DYN.
- Corretta la selezione del primo setup disponibile in caso di sezioni DYN.
- Corretti due problemi nella sezione di tipo VIR che impedivano il funzionamento delle ACTION lette dall'XML.
- Modificate le routine di creazione dei Menu' di finestra in modo da potere inserire a qualsiasi livello un nuovo menu' anche dopo la creazione del menù principale.
- Aggiunta la gestione dei menù J1,MNUAPP in modo da essere omogenei con i menù Java.
- Ora se la scheda è una sottoscheda i menu' MNUAPP, vengono aggiunti al popup della sottosezione.
- Aggiunta una funzione di base allo scattare del doppio click dell'albero.
- Aggiunta la gestione dei livelli di annidamento delle schede fino al livello 8. Viene emesso un messaggio in caso la profondità della scheda sia troppo elevata.
- Sulla massimizzazione di una sezione scheda giunta al livello massimo di annidamento ora viene aperta una nuova scheda.

## Versione V2R2M060117-02A Beta 19/01/2006

- Aggiunto la possibilità di creare uno screenshot della scheda intera tramite l'utilizzo dell'apposita voce di menu'.
- Aggiunta la funzionalità di drag and drop su tutti i componenti della scheda.
- Aggiunta la gestione degli eventi drag e drop tramite G.DIN analogamente a quanto avviene per altri eventi.
- Risolto un memory leak sulla chiusura della scheda.
- Il titolo della matrice nella stampa di matrice ora viene impostato automaticamente.
- Rimossa la assegnazione delle variabili standard allo scattare dell'evento ondrop.
- Aggiunte le variabili TO. sulla sezione destinazione dell'evento OnDrop :  vengono impostate le variabili di tipo, parametro, codice, descrizione dell'oggetto mittente.
- Risolti due problemi nel risolutore di formule di Smetray. Cambiata la funzione per stabilire se trattare la stringa come numerica oppure no.
- Aggiunto un messaggio di avvertimento nella matrice in caso di esportazione in Excel con versione > 2003. Viene avvisato l'utente di rimuovere la password al salvataggio.
- Risolto un errore che portava alla duplicazione dei bottoni personalizzati definiti tramite la specifica I.POP in alcune schede.
- Risolto un problema nella matrice in aggiornamento che generava il doppio invio di messaggi ad AS in caso di errore.
- Risolto un problema nella matrice di aggiornamento all'atto dell'inserimento di numeri negativi.
- Risolto un problema nella funzione di utility IsNumeric che avveniva durante la conversione dei numeri negativi.
- Nel componente matrice in aggiornamento ora sono gestiti correttamente i messaggi sui nodi "line" dell'xml inviato da AS, evidenziati i campi e impostati i valori.
- Risolto un problema nella matrice in aggiornamento che considerava l'esistenza di moifiche pendenti anche dopo averle annullate con la pressione del tasto Esc.
- Aggiunte variabili di riga e colonna nel componente matrice quando viene selezionata una cella.
- Aggiunta la funzionalità di invio automatico delle segnalazioni di errore. Al verificarsi di un errore viene generata una schermata che chiede all'utente un commento e prepara i log da inviare ai destinatari predefiniti.

## Versione V2R2M060117-01A Stable 18/01/2006

- Aggiunto la possibilità di creare uno screenshot della scheda intera tramite l'utilizzo dell'apposita voce di menu'.
- Aggiunta la funzionalità di drag and drop su tutti i componenti della scheda.
- Aggiunta la gestione degli eventi drag e drop tramite G.DIN analogamente a quanto avviene per altri eventi.
- Risolto un memory leak sulla chiusura della scheda.
- Il titolo della matrice nella stampa di matrice ora viene impostato automaticamente.
- Rimossa la assegnazione delle variabili standard allo scattare dell'evento ondrop.
- Aggiunte le variabili TO. sulla sezione destinazione dell'evento OnDrop :  vengono impostate le variabili di tipo, parametro, codice, descrizione dell'oggetto mittente.
- Risolti due problemi nel risolutore di formule di Smetray. Cambiata la funzione per stabilire se trattare la stringa come numerica oppure no.
- Aggiunto un messaggio di avvertimento nella matrice in caso di esportazione in Excel con versione > 2003. Viene avvisato l'utente di rimuovere la password al salvataggio.
- Risolto un errore che portava alla duplicazione dei bottoni personalizzati definiti tramite la specifica I.POP in alcune schede.
- Risolto un problema nella matrice in aggiornamento che generava il doppio invio di messaggi ad AS in caso di errore.
- Risolto un problema nella matrice di aggiornamento all'atto dell'inserimento di numeri negativi.
- Risolto un problema nella funzione di utility IsNumeric che avveniva durante la conversione dei numeri negativi.
- Nel componente matrice in aggiornamento ora sono gestiti correttamente i messaggi sui nodi "line" dell'xml inviato da AS, evidenziati i campi e impostati i valori.
- Risolto un problema nella matrice in aggiornamento che considerava l'esistenza di moifiche pendenti anche dopo averle annullate con la pressione del tasto Esc.
- Aggiunte variabili di riga e colonna nel componente matrice quando viene selezionata una cella.
- Aggiunta la funzionalità di invio automatico delle segnalazioni di errore. Al verificarsi di un errore viene generata una schermata che chiede all'utente un commento e prepara i log da inviare ai destinatari predefiniti.

