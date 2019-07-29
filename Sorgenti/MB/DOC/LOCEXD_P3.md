# Informazioni su Rilasci Componente Scheda
## In fase di sviluppo

- Ampliamento capacità della matrice, su totalizzazioni e analisi dei dati.
- Maggiore interazione tra componenti.
- Usabilita'.

## Versione V2R3M071026-03L Stable 24/07/2008

- Rilasciata completa la caratteristica di aggiunta colonne dinamiche in matrice.
- Numerosi fixing.
- Risolto un problema sulla gestione dei setup di componente, indicati nei dati.

## Versione V2R3M071026-03E Stable 14/05/2008

- Risolti due problemi sulla generazione dell'XML per la richiesta di attributi delle colonne aggiuntive.

## Versione V2R3M071026-03B Stable 07/05/2008

- Migliorato il componente G18 per gestile le opzioni e gli oggetti della riga.
- Corretti alcuni problemi di esportazione in excel con versioni di office precedenti al 2003.
- Corretto un problema alla base della comunicazione di Smetray che portava al blocco del sistema in caso di sessioni di lavoro molto lunghe (superiori alle 24 ore).
- Modificata la funzione di riconoscimento delle sezioni invalide (in corso di sostituzione per dinamismo) in modo da eliminare piccoli problemi che si potevano verificare a volte.
- Tramite il campo Formula dell'XML di matrice è ora possibile specificare di caricare all'avvio una colonna attributo di altra colonna, specificando ATT([NomeColonna].[NomeAttributo]).

## Versione V2R3M071026-02Z Stable 18/04/2008

- Aggiunta la gestione dei colori di Smetray da setup generale.
- Aggiunta la possibilità di non fare apparire la barra dei messaggi nelle sezioni di aggiornamento tramite l'attributo ShowMsgBar.
- Aggiunta la gestione del riposizionamento sul record in caso di matrice con dinamismo parziale.
- Aggiunta la gestione dei campi chiave per identificare univocamente un record nella matrice (lettera K nell'attributo Dpy della colonna).
- Aggiunta una barra di progressione nell'esportazione in Excel e un avviso in caso di operazione particolarmente lunga.
- Risolti alcuni problemi relativi all'esportazione in excel con excel 2000 ed excel 2003.
- Aggiunta l'emissione di un messaggio di avviso al caricamento di una matrice particolarmente grande.
- Sviluppato il componente G18 (in fase di test) in grado di visualizzare una G18 in scheda.
- Risolti alcuni problemi sulla matrice di aggiornamento, in particolare all'emissione del comando *EXIT.

## Versione V2R3M071026-02I Stable 04/03/2008

- Risolto un problema di instabilità che causava, sotto certe condizioni, la chiusura immediata dell'applicazione sull'uscita da una scheda.
- Risolto un memory leak sulla distruzione di una scheda.
- Aggiunto un limite sul numero di schede aperte contemporaneamente. E' stato aggiunto anche un settaggio per impostare tale numero nel setup del componente scheda.
- Aggiunta la possibilità di specificare se non aprire schede diverse al caricamento di oggetti dello stesso tipo. Gli oggetti di stesso tipo verranno aperti nella stessa scheda. Anche in questo caso è stato aggiunto un settaggio nel setup del componente scheda per decidere il comportamento di default.

## Versione V2R3M071026-02C Stable 21/02/2008

- Aggiunta la possibilità di specificare una azione da intraprendere nei dinamismi. Specificando Action="LOAD" il comportamento del dinamismo è quello normale. Specificando Action="RELOAD" la sezione di destinazione non viene ricaricata ma vengono ricaricati solo i dati in essa contenuti ove possibile.
- Modificata la gestione dei bottoni da UIPOPUP in modo da minimizzare le costruzioni e distruzioni dei medesimi.
- Risolto un problema relativo alla sezione HTML.
- Aggiunta alla lista delle azioni (per la sezione virtuale), anche la possibilità di chiudere completamente l'applicazione (specificando EXIT come tipo di azione) o scatenare un refresh della sezione (specificando DINAMIC).
- Risolto un problema relativo alla comunicazione con il servizio di aggiornamento della matrice in caso di presenza di nomicampi che iniziano con numeri.


## Versione V2R3M071026-01Z Stable 09/02/2008

- Modifiche all'esportazione in excel per fare in modo di non lasciare processi EXCEL.EXE appesi in memoria.
- Aggiunta la possibilità di generare un foglio excel che contenga anche i riferimenti agli aoggetti nelle colonne a partire da una matrice.
- Aggiunto il supporto per le immagini PNG.
- Corretto un errore nel risolutore di formula della matrice, che sbagliava i calcoli in presenza di formule numeriche molto lunghe.
- Aggiunta la funzionalità di Refresh Parziale per Immagini, Bottoni, Label e HTML, in modo che siano più rapidi i caricamenti succesivi al primo. (E' possibile impostare la funzionalità a partire dal setup del componente Smetray).
- Modificata lievemente la comunicazione di Smetray in modo da essere più sicura(in fase di partenza) e performante.
- La funzionalità di aggiunta colonna di una matrice a aprtire da un attributo oggetto è in avanzamento (ho aggiunto la memorizzazione della colonna) ma non essendo ancora conclusa non è accessibile dal menù della matrice.
- Corretto un errore nel popup di oggetto, che impediva il lancio della funzione implicita delle TAMEA.
- Risolto un problema relativo allo stack delle finestre che impediva al gestore dei fuochi di funzionare correttamente.

## Versione V2R3M071026-01S Stable 26/01/2008

- Risolto un problema sulla matrice di aggiornamento differita. In caso di update multiplo di un record veniva persa l'ultima modifica.

## Versione V2R3M071026-01S Stable 21/01/2008

- Effettuate alcune correzioni relative al caricamento delle singole sezioni in modo da dare più stabilità al sistema.
- Gestione migliorata dei check oggetto nella matrice di aggiornamento. L'attributo ChkObj definito nel setup del servizio di aggiornamento ora può contenere non solo Yes/No ma anche il nome di campo che contenga la decodifica in caso di riscontro positivo dell'esistenza dell'oggetto.
- Risolto un problema relativo all'Input Panel. In caso di aggiornamenti pendenti non veniva informato l'utente sulla possibile perdita di dati all'uscita della scheda.
- Risolto un problema sulla matrice di aggiornamento differita. In caso di update di un record appena inserito venivano perse le modifiche.

## Versione V2R3M071026-01P Stable 21/12/2007

- Aggiunte funzioni di "trasformazione" tra grafico e matrice e viceversa. Vengono conservate tutte le impostazioni utente.
- Aggiunta la possibilità di definire nelle matrici colori alternati per le righe tramite l'attributo AltRowCol. Il valore di questo attributo può essere booleano (Yes/No) oppure uno o due colori separati dal carattere "|".
- Modificata la funzione di scrittura dei log di sistema in modo da limitare ad un massimo di 10MB la dimensione di ogni file di log. I file vengono salvati con estensione .BAK e riscritti nuovamente.

## Versione V2R3M071026-01O Stable 14/12/2007

- Risolto un problema sulla visualizzazione delle matrici. In alcuni casi non venivano caricate a causa dello swap su disco.
- Aggiunta la possibilità di riferirsi a tre variabili di default negli script di scheda :  *CARDID, *SUBCARDID e *SELFID che restituiscono rispettivamente gli identificativi della Scheda, Sottoscheda e Sottosezione correnti.
- Modificato il Drag 'n Drop in modo da gestire il Drop (dove abilitato) anche su "spazi vuoti" della sezione e non solo su oggetti. Sono state anche irrobustite determinate procedure in modo da correggere ed evitare errori.
- Aggiunta al grafico la possibilità di elaborare le serie numeriche runtime e di posizionare i pannelli riassuntivi in fase di setup (Attributo PanelPos). E' stata anche aggiunta la possibilità di mostrare nei mark delle serie i valori in percentuale (PercYValue).

## Versione V2R3M071026-01M Stable 10/12/2007

- Risolto un problema sul drag di un oggetto su una sezione che si sta ricaricando a seguito di un dinamismo.
- Risolto un problema con l'esportazione in Excel. Se non erano presenti dei totali non veniva mostrata l'etichetta del nodo di raggruppamento.
- Fissati alcuni errori AV strutturali.

## Versione V2R3M071026-01I Stable 06/12/2007

- Risolto un problema con l'esportazione della matrice in excel. In presenza di raggruppamenti e formule personalizzate i totali e subtotali non erano calcolati correttamente.
- Modificata l'applicazione dell'attributo SelectRow="*LAST" nella matrice in modo da posizionarsi sull'ultima riga anche in caso di riordinamento dei record.
- Ultimata la gestione degli shortcut di carrello nella matrice ed input panel. E' possibile utilizzare le combinazioni ALT+C, ALT+O, ALT+W per copiare un oggetto nel carrello e la combinazione ALT+V per incollare l'ultimo oggetto dal carrello.

## Versione V2R3M071026-01G Stable 30/11/2007

- Risolto un problema sui subtotali generati nell'esportazione in Excel in presenza di raggruppamenti annidati.
- Modificata la gestione del popup dei componenti in modo da essere più efficienti.
- Aggiunta la possibilità di sorting dei nodi XML nelle liste di nodi.
- Ulteriori miglioramenti sulla stabilità del sistema.

## Versione V2R3M071026-01F Stable 29/11/2007

- Modificata una parte di comunicazione per avere una applicazione più stabile.
- Irrobustita tutta la gestione dei fogli e delle nuove modifiche grafiche.
- Risolti alcuni problemi all'eliminazione delle finestre.

## Versione V2R3M071026-01F Stable 27/11/2007

- Modificata la gestione dei setup di componente nei dati in modo da controllare la tipologia di setup.

## Versione V2R3M071026-01E Stable 26/11/2007

- Messa in evidenza della sezione che ha il fuoco tramite un riquadro blu. Per aumentare la comprensione della scheda, sono state aggiunte delle descrizioni sulle sezioni indicanti gli eventi agganciati a quella sezione e che insistono su quella sezione. Infine è stato messo in evidenza il periodo di caricamento ed elaborazione di una sezione.
- Modificati i log di sistema. Sono stati normalizzati i tracciati e centralizzata la posizione in cui vengono salvati (la cartella application data dell'utente windows).
- Aggiunta la possibilità di specificare se un dinamismo di una sezione è sincrono (usando l'attributo Sync="Yes"). Il dinamismo disabilita il componente che ha fatto scattare l'evento fino al caricamento completo della sezione che riceve il dinamismo.
- Eseguite numerose correzioni sulla gestione dei fogli (sezioni) e della loro distruzione.
- Modificati i popup di servizio della matrice di aggiornamento in modo da mostrare tra le voci anche l'inserimento del record e da disabilitare determinate voci in caso di selezione multipla se la matrice di aggiornamento non è in modalità deferred.
- Ora è possibile richiamare le funzioni (di default o ridefinite nella scheda) associate ai tasti F1-F24 nell'XML, semplicemente specificandole nell'attributo Exec. (Es :  Exec="*F03")
- Aggiunta la possibilità di definire dei "dinamismi" nelle  pagine HTML del browser incluso nella scheda, analogamente ai link UILINK. Riferirsi alla sezione esempi per ulteriori informazioni.
- Risolti alcuni problemi relativi alla sezione HTM in particolare all'handler della tastiera.


## Versione V2R3M071026-01B Stable 08/11/2007

- Aggiunta la funzionalità di passaggio alla matrice di un singolo raggruppamento per matrici raggruppate.
- Migliorate le performance di esportazione in Excel per matrici prive di stili.
- Risolto un problema sull'esportazione di Excel, che impediva in taluni casi l'esportazione stessa.
- Aggiunta la variabile K1.ALL negli alberi, variabile che contiene tutti i codici di livello dell'albero concatenati.
- Risolti alcuni errori di sincronia tra setup utente, menu di setup e bottoni di setup.
- Fissati alcuni errori di tipo Access Violation introdotti nella precedente versione.
- Aggiunta la possibilità di apertura modale interprocesso di una finestra, specificando G(DLG) a fine della funzione chiamata.
- Risolto un problema sul click nell'albero. Scattavano gli eventi anche se veniva clickata un area vuota dell'albero.

## Versione V2R3M071026-01A Stable 26/10/2007

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
