# Documentazione Rilasci V2.R2

## Versione V2R2M070622-02F Stable (Rilasciata il 25-10-2007)

- Aggiunta la gestione degli errori del nuovo parser. In caso di XML errato, il sistema tenta di correggerlo. In caso di fallimento viene informato l'utente che può scegliere se visualizzare o meno il file.

## Versione V2R2M070622-02E Stable (Rilasciata il 19-10-2007)

- Corretto un errore di visualizzazione dell'XML nel nuovo Parser.

## Versione V2R2M070622-02D Stable (Rilasciata il 02-10-2007)

- Corretto errore nel caso di *ACTION senza emissione di alcun formato video

## Versione V2R2M070622-02C Stable (Rilasciata il 30-08-2007)

- Sostituito il parser XML. L'emulatore ora utilizza MSXML.
- Risolti due problemi relativi alla visualizzazione dell'XML normalizzato.

## Versione V2R2M070622-01A Stable (Rilasciata il 20-06-2007)

- Ottimizzata la gestione dei fuochi dei componenti dell'emulatore.
- Risolto un problema nel componente MaskEdit che non permetteva ai campi della griglia di inserire il valore "!" al click sull'icona correlata.

## Versione V2R2M070214-01F Stable (Rilasciata il 07-06-2007)

- Risolto un problema che si verificava a seguito del click sull'icona di una data quando il campo aveva un edtcode totalmente numerico.

## Versione V2R2M070214-01E Stable (Rilasciata il 22-05-2007)

- Risolto un problema di allineamento delle griglie.

## Versione V2R2M070214-01D Stable (Rilasciata il 09-05-2007)

- Corretto Errore che si verificava alla pressione del tasto F22
- Modificata implementazione Operazioni *ACTION. Ora è possibile richiamarle anche senza specificare un formato video

## Versione V2R2M070214-01B Stable (Rilasciata il 02-03-2007)

- Modificata la gestione del popup nella G18

## Versione V2R2M070214-01A Stable (Rilasciata il 21-02-2007)

- Modificata la gestione nelle opzioni della G18.
- Aggiunto il codice per l'interazione con la sezione EMU della scheda.
- Risolto un problema di posizionamento nella griglia e di ridimensionamento della stessa.

## Versione V2R2M061003-01I Stable (Rilasciata il 31-01-2007)

- Rimosso un problema di gestione dei fuochi in caso di scheda aperta da schermata di emulazione.

## Versione V2R2M061003-01H Stable (Rilasciata il 29-01-2007)

- Cambiato il comportamento in caso di apertura di una scheda da emulazione. Le finestre di emulazione rimangono aperte disabilitate.

## Versione V2R2M061003-01G Stable (Rilasciata il 22-12-2006)

- Correzione di alcuni problemi generati con le ultime due versioni sul posizionamento cursore.

## Versione V2R2M061003-01F Stable (Rilasciata il 11-12-2006)

- Modifica della gestione dei campi esterni ad un SFL se è visibile una griglia.

## Versione V2R2M061003-01E Stable (Rilasciata il 06-12-2006)

- Modificata la gestione del posizionamento nei SFL.

## Versione V2R2M061003-01D Stable (Rilasciata il 27-11-2006)

- Modificata la gestione del posizionamento cursore se presente una griglia ma esiste un errore in un campo esterno.

## Versione V2R2M061003-01C Stable (Rilasciata il 16-10-2006)

- Aumentata granularità log eccezioni per funzioni di inizializzazione

## Versione V2R2M061003-01B Stable (Rilasciata il 13-10-2006)

- Eliminato raise eccezione in distruzione commandbar. Oggi l'eccezione viene loggata ma ignorata

## Versione V2R2M061003-01A Stable (Rilasciata il 03-10-2006)

- Aggiunto il caricamento del setup da AS400 per l'emulatore.
- Realizzata la procedura di Gestione e Caricamento della Configurazione di un setup dell'emulatore.
- Aggiunta la voce Carica e Gestisci configurazione nel System Menu.
- Risolto un problema sull'XML restituito dai setup all'emulatore.
- Aggiunta una nuova voce di comunicazione (tag XML5250) per la ricezione e invio di dati in formato XML puro.
- Aggiunta la gestione del codice finestra nella voce di comunicazione XML5250.
- Aggiunto il richiamo per la ricerca Java nell'emulatore :  E' possibile definire a quali tipi di oggetti associare la ricerca classica o quella nuova "Java" tramite una voce nella configurazione (ObjectSearchs) in cui viene associato un tipo oggetto ad un tipo di ricerca.

## Versione V2R2M060410-01C Stable (Rilasciata il 31-05-2006)

- Rimossa dall'emulatore la gestione del tasto ESC per aprire un 5250 esterno. Sostituita con una normale gestione di pressione del tasto.
- Risolto un errore sulla gestione delle intestazioni del formato video.
## Versione V2R2M060410-01B Stable (Rilasciata il 07-05-2006)

- Aggiunte nuove informazioni per il tracking degli errori.
## Versione V2R2M060410-01A Stable (Rilasciata il 10-04-2006)

- Aggiunte alcune funzioni di utility interne.
## Versione V2R2M060117-01P Stable (Rilasciata il 04-04-2006)

- Risolto un problema che impediva il corretto funzionamento in Playback introddo nella versione 01I.

## Versione V2R2M060117-01O Stable (Rilasciata il 03-04-2006)

- Risolto un problema maggiore che si verificava al precaricamento delle icone da disco in assenza di DLL dedicata. Le icone in memoria venivano eliminate inavvertitamente al primo utilizzo.

## Versione V2R2M060117-01N Stable (Rilasciata il 28-03-2006)

- Sono state apportate delle modifiche all'emulatore in modo da potere invocare più ACTION consecutive senza bisogno di un input da parte dell'utente. E' NECESSARIO aggiungere il parametro NOTIFY(YES) alla funzione da chiamare.
- Riorganizzata una parte del codice dell'emulatore in modo da isolare un certo numero di funzioni di libreria.

## Versione V2R2M060117-01M Stable (Rilasciata il 21-03-2006)

- Corretto errore nella visualizzazione di attributi video (HI,RI) sulle costanti video.
- Aumentate le informazioni presenti nel file di traccia errori nel caso di Errore su Step7a.

## Versione V2R2M060117-01L Stable (Rilasciata il 20-03-2006)

- Aggiunto supporto reperimento icone via dll di risorse.

## Versione V2R2M060117-01I Stable (Rilasciata il 10-03-2006)

- Aggiunto Supporto Mulilingua nei messaggi "cablati" all'interno dell'emulatore.

## Versione V2R2M060117-01H Stable (Rilasciata il 07-03-2006)

- **Aggiunta la possibilità di definire un limite superiore alla dimensione del file traccia PerformanceSummary.log. Nel file di configurazione (smeuiclt.xml) può essere definita la dimensione massima del file (parametro PerfDataTraceSize in "/Application/Module@Name="UIEmulator" /Logging/PerfDataTraceSize"). La Dimensione massima è espressa in Megabyte (default = 1).

## Versione V2R2M060117-01G Stable (Rilasciata il 02-03-2006)

- **Corretto errore su ridimensionamento errato del subfile** (solo se G18) qualora fosse stata precedentemente ridimensionato il form.
- **Modificato il comportamento nello spostamento campi all'interno di un subfile.** Ora, se si preme il tasto di tabulazione sull'ultima colonna di un record del subfile il cursore viene automaticamente posizionato sul primo campo del record successivo (Precedentemente veniva posizionato sul primo campo dello stesso record), in modo analogo rispetto a quanto gestito dall'emulazione 5250.
Nel caso di pressione del tasto SHIFT-TAB sulla prima colonna di un record di subfile il cursore viene automaticamente posizionato sull'ultimo campo del record precedente.
Rispetto all'emulazione 5250 le differenze sono le seguenti : 
-- Se si è posizionati sull'ultimo campo dell'ultimo record del subfile la pressione del tasto TAB posiziona comunque sul primo campo dello stesso record e non sul primo campo di immissione del formato
-- Se si è posizionati sul primo campo di un formato che ha un subfile la pressione del tasto SHIFT-TAB posiziona sul record di subfile che aveva precedentemente il fuoco e non sull'ultima colonna dell'ultimo record del subfile
-- Se si preme TAB sull'ultima colonna di un record di subfile o SHIFT-TAB sulla prima colonna di un campo di subfile e il record successivo (nel caso di TAB) od il record precedente (nel caso di SHIFT-TAB) non hanno campi di input non viene selezionato alcun campo di immissione ed occorre posizionarsi sul record desiderato di subfile con i tasti SU e GIU

## Versione V2R2M060117-01F Stable (Rilasciata il 28-02-2006)

- **Corretta AV in esecuzione funzione Playback** (parametro /PLAYBACK=<nomefile> da command line) che veniva talvolta scatenata quando veniva raggiunta la fine del file di traccia.
- **Aumentata la granularità della traccia errori** per la ricerca dell'AV in Step7

