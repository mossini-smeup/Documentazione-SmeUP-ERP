# Gestione Richieste di acquisto in V5
## INTRODUZIONE
La richiesta di Acquisto in Trade_up diventa uno strumento strettamente integrato con la gestione ordini fornitori, in quanto la Rda diventa la riga origine dell'ordine fornitore.
I vantaggi li possiamo riassumere in questi punti : 
   1. Collegamento/Scollegamento delle quantità nella modalità nativa di V5. Se cancello una riga fornitore la quantità ordinata della Rda si aggiorna, non posso cancellare una rda se esistono ordini acquisto estratti.
   2. Possibilità di utilizzare tutti gli strumenti di implementazione V5 come visualizzatori, exit, programmi funizzati...
   3. Uniformità Aziendale delle form di inserimento dati ed interrogazione.
   4. Gestione Workflow per Testata di Rda (valido il processo per un insieme di righe di rda).

## ASSUNTI
Il database di Trade_up nella gestione rda viene rispettato.
Si consiglia comunque di attenersi all'impostazione tabellare di esempio contenuta nel modello per l'avviamento iniziale dell'applicazione.
In particolare si sconsiglia di intestare la rda ad uno specifico fornitore, in quanto ciò limita la gestione del work-flow di applicazione e di estrazione della rda in ordine fornitore.
L'ente cui abbiamo intestato la testata delle Richieste di acquisto è l'azienda.
E' possibile impostare "n" tipi riga tanti quanti tipi oggetto vogliamo gestire, si noti che il fornitore è scritto nel campo R§CODS.

## GENERAZIONE ORDINE ACQUISTO
La generazione dell'ordine di acquisto viene fatta attraverso un classico flusso di estrazione "V5"
Si noti che l'estrazione può essere filtrata per  : 
  * buyer
  * fornitore
  * stato approvazione rda
  * oggetto
Dato che la conferma può originare  "n" testate di ordine fornitore, il flusso contiene un passo in cui inserire un programma XV5XX funizzato, che riceve nei parametri FUNT1/P1/K1 la testata V5 al fine di lanciare, ad esempio, il collegamento dell'ordine alla rda, la generazione dell'ordine Work-flow, la stampa dell'ordine a fornitore, etc...
Il programma XV5RDA_ESE è un esempio applicativo.

## IMPOSTAZIONE  TABELLARE
   :  : DEC T(TA) P(V5D) K(RA)
   :  : DEC T(TA) P(V5ARA) K(001)
   :  : DEC T(TA) P(V5BRA) K(001)
   :  : DEC T(TA) P(B£Y) K(T35)
   :  : DEC T(TA) P(B£Y) K(R35)
   :  : DEC T(TA) P(B£Q) K(TRA)
   :  : DEC T(TA) P(B£Q) K(RRA)
   :  : DEC T(TA) P(V5GCP) K(CP800)
   :  : DEC T(TA) P(B£JCP) K(G0010)
   :  : DEC T(TA) P(B£JCP) K(G0020)

