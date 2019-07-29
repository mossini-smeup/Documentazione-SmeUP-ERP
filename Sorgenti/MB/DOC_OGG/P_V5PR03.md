# Obiettivi
In base a quanto ottenuto dall'elaborazione delle liquidazioni è possibile generare un piano d'analisi delle provvigioni e un nuovo documento d'attesa della futura fattura dell'agente, che potranno poi essere utilizzati come strumenti di controllo in fase di contabilizzazione della stessa.

Il piano delle provvigioni può essere utilizzato come strumento d'analisi e monitoraggio del calcolo dei contributi degli agenti.

I dati memorizzati sul piano riguardano : 
 * le provvigioni liquidate (calcolate in base alla liquidazione e agli anticipi già corrisposti);
 * l'imponibile e l'importo delle ritenute (calcolati in base all'anagrafica del percipiente e in considerazione di eventuali anticipi corrisposti);
 * l'enasarco (calcolato in base alla tabella V6T);
 * il FIRR (in base alla tabella V6U);
 * l'ISC (i cui calcoli si basano invece sulla tabella V6V).

Su ogni record verranno memorizzati i flag per specificare se il record è già stato contabilizzato, se riguarda una fattura d'anticipo e a quale tipo di periodicità fa riferimento.

Vengono storicizzati anche gli imponibili su cui calcolare Enasarco, FIRR e ISC perchè possono non coincidere con l'imponibile su cui calcolare le provvigioni (la tabella V5P del tipo provvigione permette di pilotare il comportamento).

È possibile richiedere una stampa riepilogativa annuale della situazione agente, comprensiva di provvigioni e contributi.

Il piano delle provvigioni viene cancellato e ricreato ad ogni elaborazione e, anche se ogni documento d'attesa viene generato solo con l'elaborazione definitiva, il risultato finale è monitorizzabile anche in modalità provvisoria tramite la stampa di controllo.

# Formato di lancio
![V5PR03_01](http://localhost:3000/immagini/MBDOC_OGG-P_V5PR03/V5PR03_01.png)