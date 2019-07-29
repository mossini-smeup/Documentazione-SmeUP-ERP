# Utilizzo delle Program Call in login
Web.UP con provider e Looc.UP fanno tutte le chiamate previste (forse anche qualcuna di troppo).
Nel seguente capitolo il dettaglio.

# Program call loocup e provider

# Looc.UP se al collegamento non specifico l'ingresso utente

## Descrizione generale
Viene inizializzato l'ambiente.
Successivamente viene chiesto il numero di ambienti disponibili. Perché? Non lo so.
Poi viene chiesta la lista degli ingressi utente.
In caso l'utente abbia più di 20 ingressi utente attivi, vengono presentati solo i primi 20. E a
questo punto è possibile caricare altri elementi nella lista (andando sia avanti che indietro).
Una volta scelto l'ingresso utente viene verificata l'effettiva validità. Se è valido vengono fatte
tutte le chiamate necessarie per avviare la sessione su quell'ingresso utente.

## Dettaglio : 
* Inserimento credenziali
* INZJAC
* SMEVER JAC
  **Risposta con "V3R1"
* DATAMB NUM
  **Risposta con numero ambienti
* LISAMB LET
  **Risposta con lista ambienti (primi 20 se presenti di più)
* Emissione lista ambienti
* Scelta ambiente
* DATAMB VER
* DATSES CON MAS
  **CALL JAJAS0SB che effettua SBMJOB LO_E
* DATSES CHG
  **Passa per B£QQ50V (CHGLIBL)
* Il client spedisce su DTAQ il COM-COL-CHG e ora tutta la comunicazione si sposta su DTAQ

# Looc.UP se al collegamento specifico l'ingresso utente
## Descrizione generale
Viene inizializzato l'ambiente.
Viene verificata la validità dell'ingresso utente. Se è valido vengono fatte tutte le chiamate necessarie per avviare la sessione su quell'ingresso utente.

## Dettaglio
Inserimento credenziali e ingresso utente
* INZJAC
* SMEVER JAC
  **Risposta con "V3R1"
* DATAMB VER
* DATSES CON MAS
  **CALL JAJAS0SB che effettua SBMJOB LO_E
* DATSES CHG
  **Passa per B£QQ50V (CHGLIBL)
* Il client spedisce su DTAQ il COM-COL-CHG e ora tutta la comunicazione si sposta su DTAQ


# Looc.UP se al collegamento specifico un ambiente (NON un ingresso utente)

## Descrizione generale

Viene inizializzato l'ambiente.
Successivamente viene chiesto il numero di ambienti disponibili. Perché? Non lo so.
Poi viene chiesta la lista degli ingressi utente. In caso l'utente abbia più di 20 ingressi utente attivi, viene ripetuta la richiesta (col posizionamento adeguato) fino a quando non vengono comunicati tutti. Il client cerca il primo ingresso utente corrispondente all'ambiente indicato e ne verifica la validità. Se è valido vengono fatte tutte le chiamate necessarie per avviare la sessione su quell'ingresso utente.

## Dettaglio

*Inserimento credenziali
* INZJAC
* SMEVER JAC
  **Risposta con "V3R1"
* DATAMB NUM
  **Risposta con numero ambienti
* LISAMB LET
* Risposta con lista ambienti
* Eventuale ripetizione di LISAMB LET
* Ricerca dell'ingresso utente corrispondente all'ambiente.
* DATAMB VER
* DATSES CON MAS
  **CALL JAJAS0SB che effettua SBMJOB LO_E
* DATSES CHG
  **Passa per B£QQ50V (CHGLIBL)
* Il client spedisce su DTAQ il COM-COL-CHG e ora tutta la comunicazione si sposta su DTAQ

# Web.UP con provider se al collegamento specifico l'ingresso utente

## Descrizione generale
*Viene inizializzato l'ambiente.
*Viene verificata la validità dell'ingresso utente. Se è valido vengono fatte tutte le chiamate necessarie per avviare la sessione su quell'ingresso utente.

## Dettaglio
* Inserimento credenziali e ingresso utente
* INZJAC
* SMEVER JAC
  **Risposta con "V3R1"
* DATAMB VER
* DATSES CON MAS
  **CALL JAJAS0SB che effettua SBMJOB LO_E
* DATSES CHG
  **Passa per B£QQ50V (CHGLIBL)
* Il client spedisce su DTAQ il COM-COL-CHG e ora tutta la comunicazione si sposta su DTAQ

# Web.UP con provider se al collegamento specifico un ambiente (NON un ingresso utente)

## Descrizione generale
Viene inizializzato l'ambiente.
Successivamente viene chiesto il numero di ambienti disponibili. Perché? Non lo so.
Poi viene chiesta la lista degli ingressi utente. In caso l'utente abbia più di 20 ingressi utente attivi, viene ripetuta la richiesta (col posizionamento adeguato) fino a quando non vengono comunicati tutti. Il client cerca il primo ingresso utente corrispondente all'ambiente indicato e ne verifica la validità. Se è valido vengono fatte tutte le chiamate necessarie per avviare la sessione su quell'ingresso utente.

## Dettaglio
* Inserimento credenziali
* INZJAC
* SMEVER JAC
 **Risposta con "V3R1"
* DATAMB NUM
  **Risposta con numero ambienti
* LISAMB LET
  **Risposta con lista ambienti
* Eventuale ripetizione di LISAMB LET
* Ricerca dell'ingresso utente corrispondente all'ambiente.
* DATAMB VER
* DATSES CON MAS
  **CALL JAJAS0SB che effettua SBMJOB LO_E
* DATSES CHG
  **Passa per B£QQ50V (CHGLIBL)
* Il client spedisce su DTAQ il COM-COL-CHG e ora tutta la comunicazione si sposta su DTAQ




Web.UP fun-provider non fa le chiamate giuste.
Mancano alcune chiamate fondamentali e altre sono nell'ordine errato.
Nel seguente documento il dettaglio e come andrebbero modificate le chiamate.

# Program call funprovider

## Nota
Vengono analizzate le program call attuali e vine indicato come andrebbe modificata la sequenza.
Queste proposte di modifica sono fatte presupponendo la non modifica della parte AS.
### Se considerassimo anche la possibilità di modificare la parte AS, potremmo ripensare il login in modo molto più efficiente. C'è però da capire come garantire la retrocompatibilità.

## Web.UP fun-provider se al collegamento specifico l'ingresso utente
### Descrizione generale
NON Viene inizializzato l'ambiente.
NON Viene verificata la validità dell'ingresso utente.
Viene avviato l'ambiente.
NON viene richeisto il cambio ambiente del QZRCSRVS
Viene richiesta la LISAMB LET. Forse perché il fun-provider non capisce che ha già ricevuto un ingresso utente e non un ambiente?

### Dettaglio
Inserimento credenziali e ingresso utente
* INZJAC - NON FATTA e SERVE
* SMEVER JAC - non fatta ma direi che non serve
* DATAMB VER - NON FATTA e SERVE
* LISAMB LET - FATTA MA INUTILE?
* DATSES CON MAS - fatta
* DATSES CHG - NON FATTA. Sarebbe meglio farla? Se il QZRCSRVS poi "muore", non serve.
* Il client spedisce su DTAQ il COM-COL-CHG e ora tutta la comunicazione si sposta su DTAQ - fatta

## Web.UP con fun-provider se al collegamento specifico un ambiente (NON un ingresso utente)

### Descrizione generale
NON Viene inizializzato l'ambiente.
NON Viene verificata la validità dell'ingresso utente.
A questo punto viene avviata la sessione. Poi viene chiesta la lista degli ingressi utente (solo la prima pagina). Il client cerca il primo ingresso utente corrispondente all'ambiente indicato e NON ne verifica la validità. NON viene richiesto il cambio ambiente del QZRCSRVS

### Dettaglio com'è
Inserimento credenziali
* INZJAC - NON FATTA e SERVE
* SMEVER JAC - non fatta ma direi che non serve
* DATSES CON MAS - VA FATTA DOPO LA LISAMB LET e DATAMB VER (che non è nemmeno fatta)
* LISAMB LET - fatta solo sulla prima pagina
* Ricerca dell'ingresso utente corrispondente all'ambiente.
* DATSES CHG - NON FATTA. Sarebbe meglio farla? Se il QZRCSRVS poi "muore", non serve.
* Il client spedisce su DTAQ il COM-COL-CHG e ora tutta la comunicazione si sposta su DTAQ

### Dettaglio come dovrebbe essere
* INZJAC
* LISAMB LET n volte
* DATAMB VER
* DATSES CON MAS
* DATSES CHG (Se il QZRCSRVS poi "muore", non serve.)
* Il client spedisce su DTAQ il COM-COL-CHG e ora tutta la comunicazione si sposta su DTAQ - fatta

