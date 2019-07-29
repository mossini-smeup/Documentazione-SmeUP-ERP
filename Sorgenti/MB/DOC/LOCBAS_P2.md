# Sviluppi modulo base (J1-GRA-BAS) dopo V2R2 (dal 17 gennaio 2006)

Il modulo comprende : 
- Il modulo di comunicazione con As/400
- Il modulo grafico di base che gestisce
  . utenti
  . le finestre, il loro richiamo e la comunicazione tra i vari moduli Java e non.
- Gli oggetti grafici di base come
  . la finestra di selezione di un oggetto
  . il preview di funzione
  . il carrello
  . il setup
- La finestra di consolle che rappresenta la finestra di ingresso nell'applicazione

## Versione 002 (25 gennaio 2006)

- (DF) Modificato comportamento oggetti di tipo A8 nel UIObjectField. Ora non viene più
effettuato un controllo formale se il codice immesso inizia per &.
- (DF) Nuova gestione del menù iniziale.
- (DF) Separazione tra XML di setup e modulo di avvio.
- (DF) Creato nuovo modulo di console
- (DF) Possibilità di avviare Loocup con albero menù o con modulo alternativo.
- (DF) Creazione variabili di setup iniziale. Definita una lista iniziale di variabili di defaule e
modificato il meccanismo di creazione delle funzioni aperte (parentesi quadre) perchè
possa accettare anche variabili come riferimento.

## Versione 003 (1 febbraio 2006)

