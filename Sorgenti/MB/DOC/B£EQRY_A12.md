# Generalità

Le schede implementate nei surf, non sono nativamente utilizzabili per le ricerche. Su tali schede vanno implementati alcune funzionalità. Qual'ora viceversa non ci sia questa intenzione, la scheda va esplicitamente esclusa dalle ricerche, quando nel pgm della £G46, viene passato il campo £G46I_QR valorizzato (cioè il parametro che mi permette di capire che sono in modalità ricerca).

Va correttamente gestita la ricezione del parametro di INPUT "Qry" :  valorizzato a "Yes" indica che la scheda è stata richiamata in modalità ricerca. Tale parametro viene normalmente passato alla richiesta di configurazione per attivare il filtro E/*RIC, in sostituzione al filtro E/*JOB, ed al servizio di lista per attivare la colonna di selezione (questo è nativamente gestito dalle matrice risolte dal servizio generico LOA10, ma vanno alternativamente gestite manulmente nel richiamo dello schema £IQ2 o direttamente nel servizio se non sono previsti degli schemi).

Al di sopra della matrice di selezione va inoltre incluso il seguente membro di script :  B£EQRY_SEL. In questo modo vengono correttamente gestiti i dinamismi necessari per la selezione dell'elemento ricercato.

# Sostituzione della ricerca standard per codice/descrizione

Qual'ora si voglia inoltre, che oltre a vedersi, una particolare scheda di surf, va a sostituire la ricerca standard per codice e/o descrizione andranno fatte delle considerazioni aggiuntive.

Andrà gestita la recezione dei seguenti parametri : 
* Parametri P
** QryKey :  indica che sono stato richiamato con la ricerca per uno dei caratteri speciali previsti (!/?/ : ). Sulla base della presenza di esso andranno considerati tutti i parametri successivi
* Parametri INPUT
** Q1cPag :  conterrà il codice di posizionamento (per codice o descrizione a seconda della ricerca che viene sostituita). E' opportuno che qual'ora sia presente il parametro QryKey il campo di posizionamento venga sempre riempito con questa variabile, sia che sia valorizzata o meno.
** Q1cFst :  conterrà la stringa di ricerca in scansione (cioè la stringa che segue i caratteri speciali " : "). E' opportuno che qual'ora sia presente il parametro QryKey il campo di posizionamento venga sempre riempito con questa variabile, sia che sia valorizzata o meno.

Andrano inoltre date le seguenti indicazioni.
* Nel pgm specifico della G46 nella posizione relativa all'utilizzo della scheda, per il modulo, invece che uno spazio, dovrà alternativamente essere indicato uno dei seguenti caratteri : 
** K se sostituisce la ricerca per codice/scansione
** k se sostituisce la ricerca per codice ma non quella per scansione
** D se sostituisce la ricerca per descrizione
* Nel servizio B£EQRY_SE, nella routine RCHKSEA_SF andrà esplicitamente espressa la medesima volontà di utilizzare il surf in sostituzione della ricerche standard (è sufficiente dare un'occhio alla routine per intuirne il funzionamento).

