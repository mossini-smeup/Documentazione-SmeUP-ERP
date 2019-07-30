# Gestione G30 in LOOC.up
Questa scheda mostra l'utilizzo del servizio B£SUP_02 per la gestione di G30 in ambiente LOOC.up.
Tale servizio : 

- Carica una G30 tra quelle fornite dai programmi AS di gestione G30 (xx_G30).
- Istanzia i valori della G30 con quelli di una memorizzazione specificata come parametro nel servizio (in questa scheda :  nome del programma di cui sta presentando la G30, come V5AT10G, + suffisso XXX).
- Gestisce il controllo e l'aggiornamento dei valori della G30 e il salvataggio della memorizzazione.
- Istanzia, per i campi della G30 valorizzati, delle variabili del tipo G30nnn, dove nnn è il numero riga.

Il B£SUP_02 presenta inoltre una funzione per mostrare le G30 disponibili in un programma xx_G30, qui utilizzata per la selezione e il caricamento dinamico della G30. Sono, infine, mostrati degli esempi di dinamicità indotta dalle modifiche dei valori in G30.

## Temi aperti

- Non sono correttamente gestiti :  tipi dinamici della G30, ricerca sui valori particolari.
- Per ora i controlli sui valori della G30 sono bloccanti solo sul campo che si sta editando :  bisogna gestire il controllo e l'aggiornamento multirecord.

