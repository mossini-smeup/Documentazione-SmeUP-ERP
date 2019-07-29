# Obiettivo

Il modulo di ricerca è un componente di LOOC.up la cui finalità primaria è la selezione di un oggetto applicativo.

# Utilizzi

Lo strumento di ricerca viene utilizzato in ogni contesto in cui è necessaria la ricerca e la selezione di un oggetto applicativo. Attraverso la visualizzazione di una interfaccia grafica, l'utente viene guidato nella procedura di visualizzazione di una lista filtrata di oggetti applicativi affinchè possa effettuare la selezione di uno o più di questo oggetti. Per la sua natura il modulo di ricerca può essere invocato in qualsiasi momento ed essere integrato in altri moduli applicativi di LoocUp. La funzionalità di ricerca è controllata da un apposito scriptche consente di variare dinamicamente le condizioni di definizione sia della lista oggetti (fonte, query di selezione) sia della loro visualizzazione (schema, ordinamento).

Le funzionalità di base del modulo di ricerca sono le seguenti : 


- Consentire la selezione di qualsiasi oggetto applicativo.
- Consentire la visualizzazione di liste di oggetti di qualsiasi tipo al fine di consentire la selezione di uno o più oggetti.
- Consentire la personalizzazione sui contenuti :  l'utente può definire la Query che definisce la lista di oggetti su cui effettuare la selezione
- Consentire la personalizzazione sulla visualizzazione :  è possibile definire il tipo di informazioni visualizzate (Schema) e le modalità di ordinamento della lista.
- Fornire un comodo punto di accesso per l'analisi e la modifica dello script di ricerca associatoalla lista oggetti.


# Come accedere alla modalità di ricerca degli oggetti

La ricerca di un oggetto può avvenire in due contesti differenti : 

## Selezione di un oggetto di tipologia nota.

In questo specifico contesto l'utente ha la necessità di selezionare un codice oggetto scelto tra una lista di oggetti di tipo predefinito. Tipicamente questo tipo di ricerca è associata ad uncampo di immissione tipizzato :  ad esempio, un campo di immissione in cui è richiesto l'inserimento di un codice cliente o di un codice articolo. In questi contesti la ricerca si limita a proporre all'utente una lista di oggetti filtrata (in funzione del contesto e delle specifiche di ricerca) in modo da consentire la selezione di un oggetto. La ricerca di questo tipoè attivabile su tutti i campi di immissione tipizzati (identificati dalla presenza di una icona che identifica la tipologia di oggetto) in due modi diversi :  cliccando con il tasto sinistrodel mouse sulla icona oppure premendo il tasto F4 quando il campo di immissione possiede il fuoco.

In questo caso specifico la finestra di ricerca assume l'aspetto riportato nella seguente figura : 

![ese1](http://localhost:3000/immagini/LOCQRY_01/ese1.png)

La finestra di ricerca è suddivisa in tre zone funzionali distinte : 

### Pannello di definizione delle condizioni di ricerca.

![ese2](http://localhost:3000/immagini/LOCQRY_01/ese2.png)
Questo pannello, posto nella parte alta della finestra di ricerca, consente di modificare le opzioni di filtro/visualizzazione della lista di oggetti da selezionare. I suoi principali campi sono : 


- Query :  consente la selezione delle Query di ricerca disponibili per la tipologia di oggetti da selezionare. La query definisce la lista degli oggetti visualizzati attraverso la definizione di fonte dei dati e filtro di selezione. La lista di query disponibili è definita all'interno dello script di definizione della ricerca.
- Schema :  consente la selezione degli schemi di visualizzazione disponibili. Lo schema di visualizzazione definisce il tipo e la natura dei dati visualizzati per ognuno degli oggetti che si intende selezionare. E' infatti possibile personalizzare la visualizzazione e fare in modo che nella lista oggetti compaiano una serie di informazioni aggiuntive relative all'oggetto da selezionare. Attraverso la seleziona dello schema è possibile modificare e categorizzare le informazioni da visualizzare (ad esempio, uno schema potrebbe privilegiare le informazioni commerciali, un altro le informazioni contabile ecc ecc). Anche gli schemi sono definiti nello script di ricerca.
- Ordinamento :  consente la selezione dei criteri di ordianamento disponibili. Potenzialmente ogni categoria di informazione associata ad una categoria di oggetti può diventare chiave di ordinamento.
- Bottone di condizioni :  attiva la visualizzazione di un questionario di tipo G30 che consente la specificazione delle condizioni di query. Ad esempio, se la query presenta dei campi di filtro, permette l'immissione dei valori che definiscono le condizioni di filtro da applicare alla lista di oggetti da visualizzare. Quando la lista di oggetti visualizzata è filtrata, questo bottone viene visualizzato con lo sfondo giallo (per segnalare la condizione di filtro attivo).
- Ricerca per codice :  consente di puntare ad un codice specifico all'interno della lista oggetti. Ad esempio, se immetto in questo campo il valore "CL" e premo il tasto invio, mi verrà mostrato come primo elemento della lista oggetti il primo oggetto il cui codice inizia per "CL". Se non esiste viene mostrato il primo oggetto della lista oggetti senza filtro. La selezione di una ricerca per codice attiva per default la visualizzazione ordinata per codice articolo.
- Ricerca per descrizione : consente di puntare ad una descrizione specifica all'interno della lista oggetti. Ad esempio, se immetto in questo campo il valore "Cliente" e premo il tasto invio, mi verrà mostrato come primo elemento della lista oggetti il primo oggetto la cui descrizione inizia per "Cliente". Se non esiste viene mostrato il primo oggetto della lista oggetti senza filtro. La selezione di una ricerca per descrizione attiva per default la visualizzazione ordinata per descrizione articolo (se possibile) .


### Pannello di visualizzazione della lista oggetti

Questo pannello, posto nella parte centrale della finestra di selezione oggetto, consente la visualizzazione della lista di oggetti selezionabili. Il pannello è diviso in due parti :  la parte a sinistra, fissa, mostra le colonne codice e descrizione. Queste colonne sono identificate all'interno dello script di ricerca e potenzialmente ogni campo parametro associato ad un oggetto può essere dichiarato codice o descrizione. In caso di selezione di un oggetto, verrà sempre tornata al richiedente la coppia codice-descrizione dell'oggetto selezionato.
La parte destra del pannello mostra invece tutte le informazioni aggiuntive associate agli oggetti da selezionare. La nature di queste informazioni aggiuntive è definita dallo schema di visualizzazione e dipende strettamente da questo parametro. Le colonne di tipo tipizzato sono identificate dalla presenza di un icona nell'header di colonna e dalla presenza di uno sfondo giallo. Sfondo che invece è bianco per le colonne di tipo testo.

Al fine di velocizzare le operazioni di comunicazione, la visualizzazione della lista degli oggetti può avvenire per pagine. Cioè la lista degli oggetti può essere caricata a gruppi di n oggetti alla volta, con n dipendente dalla query associata al tipo di oggetti che si vuole selezionare. Lo scorrimento tra le pagine successive può avvenire in più modi : 


- Attraverso l'uso dei tasti cursore :  quando la lista viene scorsa fino all'ultimo elemento visibile l'ulteriore pressione del tasto PG_DOWN o freccia giù provoca il caricamento automatico della pagina successiva (ammesso che esista).
- Attraverso l'apposito bottone della bottoniera (vedi descrizione nel paragrafo successivo).
- Attraverso una ricerca per codice o per descrizione. Se viene richiesta una ricerca per codice o descrizione che punta ad un elemento non ancora visualizzato, viene automaticamente caricata la pagina che ha come primo elemento l'oggetto che soddisfa le condizioni di ricerca. In questo caso non vengono però valorizzare le pagine precedenti a quella visualizzata.


### Bottoniera di controllo

![ese3](http://localhost:3000/immagini/LOCQRY_01/ese3.png)

Nella parte bassa della finestra di ricerca c'è la bottoniera di controllo che mostra una serie di bottoni che consentono l'attivazione di una serie di operazioni.
A seguito la descrizione dei singoli bottoni : 


- Successivi :  pulsante che attiva il caricamento della pagina sucessiva di oggetti. E' attivo solo se la lista oggetti mostrata è paginata, in caso contrario il bottone è disattivato.
- Aggiorna :  ricarica la lista di oggetti e riporta lo stato alle condizioni iniziali. La medesima funzione può anche essere richiesta con la pressione del tasto F5.
- Esporta in tabella :  mostra la lista di oggetti caricata fino a quel momento con il modulo tabella di LoocUp in modo da consentire una migliore navigazione nei dati e operazioni di raggruppamento ed analisi. In caso di lista di ricerca paginata, i dati esportati verso il modulo tabella sono solo quelli caricati fino a quel momento.
- Vedi XML :  funzione di debug (non presente nella versione definitiva del modulo) che mostra l'ultimo XML letto dal modulo di ricerca.
- Lista chiamate :  funzione di debug (non presente nella versione definitiva del modulo) che mostra la lista di richieste effettuate dal modulo di ricerca all'AS400
- Edita script :  consente un accesso veloce all'editing dello script di ricerca associato alla categoria di oggetti corrente.
- Documetazione :  consente la visualizzazione della documentazione relativa al servizio
- Annulla :  annulla l'operazione di selezione senza selezionare nulla.
- OK :  chiudi tutto e torna l'oggetto selezionato.


## Selezione di un oggetto qualsiasi

In questo specifico contesto l'utente ha la necessità di selezionare un oggetto qualsiasi. Deve quindi selezionare sia la tipologia dell'oggetto sia il suo codice. Questo tipo di ricerca è assimilabile alla funzione UP FUN presente su AS400 ed è richiamabile in qualsiasi punto dell'interfaccia grafica di LoocUp (tranne ovviamente all'interno dei campi di immissione tipizzati perchè in questo caso partirebbe la ricerca per oggetto specifico descritta al punto precedente).
La funzionalità di ricerca di un oggetto quasiasi svolge all'interno di LoocUp una importante funzione di "centro di controllo" :  da qualsiasi punto di LoocUp l'utente può premere il tasto F4 e selezionare un oggetto alternativo da analizzare (attraverso la scheda associata) o da sottoporre a funzione specifica (attraverso l'uso del tasto destro del mouse e del menù di popup contestuale).

La pressione del tasto F4 porta alla visualizzazione di una finestra di selezione oggetto del tipo : 

![ese4](http://localhost:3000/immagini/LOCQRY_01/ese4.png)

Questa finestra consente di definire la selezione di un oggetto specifico attraverso la selezione dei tre parametri distintivi di un oggetto applicativo, il tipo, il parametro e il codice. I tre campi di immissione sono a loro volta dei campi di tipo tipizzato e sono strettamente legati :  la selezione del campo tipo influenza la tipologia del campo parametro. Quindi se si sceglie un determinato tipo, il campo parametro accetterà solo parametri associabili al tipo selezionato. Il campo codice ovviamente dipende sia dal campo tipo che dal campo parametro. Tutti e tre i campi sono dotati di funzione di ricerca, attivabile cliccando con il tasto sinistro del mouse sulle icone oppure premendo il tasto F4 quando uno dei campi possiede il fuoco. Il campo di spunta "Minuscoli/maiuscoli" attiva la modalità case sensitive :  se il campo di spunta è attivato il sistema tiene conto anche della minuscole e delle maiuscole nella definizione di codici (in questo caso, il codice "a01" e il codice "A01" sono diversi).

Una volta compilati i tre campi tipo, parametro e codice e selezionato l'oggetto è possibile uscire dalla finestra di selezione in due modi distinti.


- Clickando sul bottone OK o dando Invio da tastiera :  per default viene visualizzata la scheda dell'oggetto selezionato, cioè dell'oggetto identificato dalla terna di valori tipo, parametro e codice immessi. Con questa funzionalità è possibile passare velocemente da un oggetto applicativo ad un altro semplicemente premendo F4 in qualsiasi punto di LoocUp e selezionando l'oggetto che si vuole analizzare. In questa modalità il pannello di selezione oggetti diventa un cruscotto di navigazione tra oggetti applicativi.
- Richiedendo una azione dal menù di popup contestuale :  l'utente clicca con il tasto destro del mouse su uno qualsiasi dei tre campi di immissione e sceglie dal menù di popup che viene visualizzato una delle funzioni applicative disponibili per il contesto attivo. In questo caso non solo viene selezionato un oggetto ma viene anche selezionata la funzione da applicare sull'oggetto scelto. In questo caso il pannello di selezione di un oggetto diventa un centro di controllo per il richiamo di funzioni su oggetti.

