# Introduzione
La ricerca di un oggetto può avvenire secondo varie modalità in funzione del contesto.
In questo documento tratteremo dell'individuazione di un oggetto non nel modulo Emulatore in quanto questo modulo utilizza meccanismi propri.

# Come eseguire una ricerca.
La ricerca di un oggetto avviene utilizzando l'apposito gestore. Il gestore si avvia o con il tasti funzione F4 oppure cliccando sul pulsante che riporta una lente.

**NOTA : ** il pulsante F4 non funziona quando il fuoco è posizionato su una subsezione che contiene un browser o un visualizzatore PDF. Questi visualizzatori pur essendo integrati in LoocUp vanno a ridefinire il comportamento dei pulsanti funzione.

## Il modulo di ricerca degli oggetti
Il modulo di ricerca degli oggetti oltre alle possibilità standard di cercare per codice o per descrizione introduce la possibilità di sfruttare filtri avanzati.

## Struttura del modulo.
Il modulo è composto da 3 finestre di dialogo.

## la finestra di selezione
E' la finestra con cui definisco tipo, parametro e metodo di ricerca.

![LOBASE_173](http://localhost:3000/immagini/MBDOC_OPE-LOCOGG/LOBASE_173.png)
## la finestra di filtro
E' la finestra con cui imposto i parametri del filtro di ricerca.
Le domande che vengono poaste dipendono dal tipo di filtro.

![LOBASE_174](http://localhost:3000/immagini/MBDOC_OPE-LOCOGG/LOBASE_174.png)
## la finestra di lista
E' la finestra che riporta la lista di oggetti filtrati in base al criterio impostato.

![LOBASE_175](http://localhost:3000/immagini/MBDOC_OPE-LOCOGG/LOBASE_175.png)
# Ricerche
Vediamo come eseguire le ricerche.

Esistono tre modi.

## Per codice
La ricerca per codice si avvia o premendo il tasto di tabulazione, oppure cliccando sull'icona dell'oggetto oppure inserendo il carattere "**!**" nel campo di ricerca.
Se al carattere "**!**" si fa seguire un valore avrò che la ricerca verrà eseguita partendo dal codice inserito. Il codice può anche essere parziale :  se inserisco "**!B**" la ricerca si posizionerà sull'oggetto con codice che inizia per B.

**NOTA** :  Se il codice dovesse essere sensibile al carattere spuntare il flag **Maiuscolo/Minuscolo**

## Per descrizione
La ricerca per descrizione si avvia o premendo il tasto di tabulazione, oppure cliccando sull'icona dell'oggetto oppure inserendo il carattere "**?**" nel campo di ricerca.
Se al carattere "**?**" si fa seguire un valore avrò che la ricerca verrà eseguita utilizzando il valore inserito. Il valore può anche essere parziale :  se inserisco "**?B**" la ricerca si posizionerà sull'oggetto con descrizione che inizia per B.

**NOTA** :  Il flag **Maiuscolo/Minuscolo** non viene considerato in questo tipo di ricerca.

## Ricerche avanzate
Le ricerche avanzate sfruttano il meccanismo delle Query.
Una query è composta da un insieme di domande (che costituiscono il filtro), uno o più schemi  e uno o più ordinamenti.

Vediamo i singoli elementi

### La query
Una query è un filtro avanzato definito per un tipo di oggetto.
E' composta da un insieme di domande che verranno utilizzate per filtrare gli oggetti.

Per utilizzare una query si può effettuare un ricerca standard, anche senza parametri di ricerca, e poi selezionare la query nella combo visibile nella figura seguente.

![LOBASE_176](http://localhost:3000/immagini/MBDOC_OPE-LOCOGG/LOBASE_176.png)
In alternativa si può inserire nel campo codice il carattere "**+**" seguito dal nome della query, ad esempio **+BASE** fa iniziare la ricerca con la query BASE.

Una volta scelta la query comparirà la finestra di filtro.

Premendo OK verranno memorizzate le scelte e verrà eseguito il filtro.
Comparirà una dinestra di dialogo contenente un elenco di zero o più valori.

### lo schema
E' una particolare visualizzazione dei dati ottenuti.

Nella figura seguente vediamo gli schemi definiti per la query BASE degli oggetti Articolo

![LOBASE_177](http://localhost:3000/immagini/MBDOC_OPE-LOCOGG/LOBASE_177.png)
### L'ordinamento
Consente di specificare come i dati vanno ordinati.

Nella figura seguente vediamo gli ordinamenti  definiti per la query BASE degli oggetti Articolo

![LOBASE_178](http://localhost:3000/immagini/MBDOC_OPE-LOCOGG/LOBASE_178.png)
### Esporta in tabella
I dati ottenuti si possono esportare in una matrice :  è sufficiente utilizzare il tasto **Esporta in tabella** per fare apparire una scheda contenente una matrice con i dati recuperati secondo lo schema selezionato.
A questo punto si può navigare nei dati (raggrupparli filtrarli ecc) o  esportarli in Excel o
