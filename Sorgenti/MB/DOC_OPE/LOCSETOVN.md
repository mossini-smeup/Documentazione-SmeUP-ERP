# Introduzione
La gestione da parte del client dei setup nuovi e vecchi presenta alcune peculiarità che riportiamo : 


# Setup Nuovi
Innanzitutto in B£5 va disabilitato l'invio dei setup da parte del JATRE_18C.
Il client non effettua nessuna richiesta automatica di setup.
I setup possono arrivare con l'XML dei dati (se gestiti dal servizio).
Alla pressione del pulsante relativo al setup il client richiede al server i setup per quella sezione.
La chiave dei setup è costruita a partire dal context.

# Setup Vecchi
La gestione dei setup "vecchi" cambia a seconda che la subsezione presenti un contex o meno
## Setup vecchi senza context
Se la sezione non ha context gli eventuali setup utente arrivano con l'XML della scheda.
La chiave del setup è solo quella vecchia :  NomeScheda/NomeSezione.
## Setup vecchi con context
Se la sezione ha un context, allora il comportamento varia a seconda della release di Sme.UP.
### Setup vecchi con context e Sme.UP pre V3R1
In questa situazione i setup utente arrivano solo con l'XML della scheda.
La chiave del setup è solo quella vecchia :  NomeScheda/NomeSezione.
### Setup vecchi con context e Sme.UP >= V3R1
In questa situazione ci possono essere alcuni setup con chiave vecchia (NomeScheda/NomeSezione) e altri con chiave nuova (context).
La scrittura dei setup avviene con chiave nuova.
La lettura deve tenere conto sia di quelli con chiave vecchia che quelli con chiave nuova.
Gli eventuali setup con chiave vecchia arrivano con l'XML della scheda.
Poi il client effettua una chiamata per richiedere il setup di default (CFSER_02) e altre chiamate (JASER_02 e CFSER_02) per richiedere gli altri setup.
Il client poi effettua una fusione di tutti i setup ricevuti.
