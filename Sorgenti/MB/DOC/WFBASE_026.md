# Presentazione

Le transizioni extra rete offrono allo sviluppatore la possibilità di personalizzare in maniera totale la rete del processo, creando e gestendo impegni (slegati dalla rete!) in maniera totalmente manuale.
In pratica viene offerta la possibilità di utilizzare le strutture dati del workflow (in particolare gli impegni) senza passare per il motore di workflow.

# Creazione

Il modello per un impegno extra-rete è una transizione extra-rete, dichiarabile nello script del processo utilizzando la keyword Exr="1".
Questo si riflette nella valorizzazione dei flag delle attività derivate, che avranno F4FL02="E".
Le transizioni extra rete non possono avere una transizione master nello script (a carico di chi le scrive eventualmente attaccarne una per legarle nella rappresentazione grafica).

## Utilizzo

La creazione degli impegni (sul modello della corrispondente transizione) e la loro attivazione è manuale.
Poi : 
 * E' possibile specificare nella transizione extra-rete i gruppi utenti esecutori / di assegnazione :  questi vengono controllati.
 * E' possibile specificare nella transizione extra-rete le azioni esterne da presentare nella scheda dell'impegno extra-rete e le conseguenze esterne da eseguire alle varie dichiarazioni :  queste vengono gestite.
 * La gestione dell'attivazione delle azioni esterne è tuttavia manuale :  vengono testate le condizioni, ma non vengono inibite le azioni in relazione all'eventuale stato di non pronto dell'impegno. E' cura dell'implementatore della rete vincolare con delle condizioni sullo stato, se desiderato.

