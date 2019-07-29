Attraverso questa funzione è possibile decidere su quale rapporto bancario destinare gli importi di ogni singola rata/fattura/scadenza etc. presente nella proposta.

![C5D010_048](http://localhost:3000/immagini/MBDOC_OGG-P_C5RR12P1/C5D010_048.png)
Per ogni rapporto bancario si visualizza la relativa disponibilità, l'importo deciso da assegnare e poi quello effettivamente assegnato attraverso l'associazione con le singole rate.
Premessa è che vi è la possibilità di selezionare la data rispetto alla quale effettuare queste operazioni.
In basso invece "Totali" rappresenta la somma delle disponibilità dei rapporti, "Importo Proposto" l'ammontare della proposta, "Residuo" è quanto rimane ancora da assegnare, "Disponibilità Finale" è invece il valore del totale dei rapporti successivamente all'assegnazione completa.
Inserendo nella colonna editabile si può decidere quale importo della proposta assegnare a ciascun rapporto (è subordinato alla ricerca delle rate presenti e alle condizioni inserite nell'F17)
*F09 si distribuisce automaticamente per intero il totale non ancora assegnato
*F11 equivale all'F06 di conferma ed effettua l'esecuzione in Batch (in automatico, in relazione alle impostazioni e condizioni inserite, andrà ad associare le singole rate ai rapporti)
*F17 si imposta le modalità di visualizzazione della tabella

![C5D010_050](http://localhost:3000/immagini/MBDOC_OGG-P_C5RR12P1/C5D010_050.png)
Fondamentale la compilazione della terza riga (Attrib. Rapp. Banc. Rate), in cui si imposta il criterio con cui l'importo digitato manualmente va a collegarsi con le singole rate :  ad esempio con 1 l'associazione sarà fatta solo in caso di corrispondenza tra il codice ABI delle possibili rate abbinabili e il rapporto scelto, 4 lo stesso concetto ma con il circuito bancario, mentre con 2 non ha nessun vincolo per abbinare.
F14 si può andare invece ad assegnare manualmente ogni singola rata al rispettivo rapporto bancario, oppure visualizzare quelle assegnate in precedenza in automatico.
