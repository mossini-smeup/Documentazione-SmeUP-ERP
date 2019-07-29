# Installazione - IN SVILUPPO
Per quanto riguarda l'installazione del modulo delle Richieste di Acquisto si consiglia di prelevare dal modello (libreria Smeupfil) i seguenti elementi di tabella : 
## Necessari per l'impianto V5
 :  : DEC T(TA) P(V5D) K(RA) R(1)
 :  : DEC T(TA) P(V5ARA) K(001) R(1)
 :  : DEC T(TA) P(V5BRA) K(001) R(1)
 :  : DEC T(TA) P(V5GCP) K(CP800) R(1)
 :  : DEC T(TA) P(V5GCP) K(CP880) R(1)
Si presti particolare attenzione alle tabelle B£WRA (stati gestiti dal workflow) e ai flussi sugli oggetti DROP (lancio della fasatura "light" dei documenti origine invece del collegamento).

## Necessari per l'impianto workflow
 :  : DEC T(TA) P(WFA) K(£DORA01) R(1)
 :  : DEC T(TA) P(WFA) K(£DORA02A) R(1)

Inoltre deve essere presente lo script di workflow, contenuto nel file SCP_WFA della smedev, £DORA01 e £DORA02A.
Fare riferimento, nella scheda di TAWFA £DORA01 e £DORA02A, alle sezioni di Istruzione e Documentazione tecnica.

In tabella B£2 deve essere attivata la nuova gestione azioni (valore 02)

AUTORIZZAZIONI PER PARTIRE :  immettere le autorizzazioni sulla classe WF£DORA02 e WFORTE.


