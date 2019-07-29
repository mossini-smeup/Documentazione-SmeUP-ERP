# Gestione fatture scartate

## Definizione
Le fatture con esito di scarto, non vengono considerate come fatture in stato definitivo. Questo perchè ci si aspetta che rispetto alla problematica che ha provocato lo scarto, vengano fatte delle azioni correttive.

Quando quindi dopo un aggiornamento degli esiti le fatture passano ad una stato di scarto è necessario operare come segue : 
* verificare tramite la funzione di dettaglio degli esiti, quale sia il motivo dello scarto
* applicare le azioni correttive correlate alla suddetta motivazione
* eseguire una nuova estrazione della fattura indicando nel lancio l'opzione "riestrai fatture che sono state scartate".


