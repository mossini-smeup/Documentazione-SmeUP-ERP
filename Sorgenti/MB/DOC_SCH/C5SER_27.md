### Obiettivo
Fornire un'analisi dell'evoluzione nel tempo dei saldi dei diversi rapporti bancari attivi per l'azienda.
### Parametri di lancio
All'interno dei parametri di lancio dell'interrogazione è possibile impostare : 
* Data inizio :  è la data a partire dalla quale saranno analizzati i saldi. Nel caso in cui non venga impostata viene preso come default 'oggi'.
* Periodicità :  è la cadenza temporale con cui si vogliono visualizzare i saldi. Ad esempio, impostando una periodicità mensile verranno espostii saldi a fine mese di ogni rapporto bancario. Nel caso in cui il campo venga lasciato vuoto viene impostata come default una periodicità giornaliera.
* Pertinenza e Condizione :  questi due campi servono per includere o meno registrazioni gestionali e simulate. Lasciando entrambe i campi vuoti verranno incluse le registrazioni fiscali attive e sospese.
* Movimenti Stimati :  permette di includere l'analisi del saldo di movimenti non ancora registrati sulla banca in analisi ma per i quali è lecito ritenere che l'incasso/uscita avverrà sulla banca stessa. Un esempio potrebbe essere una fattura di acquisto con pagamento RiBa per la quale sia già stata inserita la banca d'appoggio.
### Dettaglio informazioni
Per ogni rapporto bancario vengono riportati : 

- Fido :  è il valore ripreso dalle condizioni generali del rapporto bancario alla data impostata sull'intestazione della colonna
- Saldo C/Sbf :  è il saldo per data operazione del rapporto collegato al rapporto in analisi. Ad esempio se stiamo analizzando il rapporto 003.001 e all'interno della tabella C5J è indicato come rapporto collegato il 003.002 in questa cella vedremo il saldo di questo rapporto. Generalmente  all'interno della tabella C5J il campo è compilato sui rapporti di tipo CCO per visualizzare il saldo del relativo conto SBF.
- Saldo Periodo :  è il saldo periodico del rapporto bancario per data operazione. Ad esempio se abbiamo impostato una periodicità mensile e stiamo analizzando la colonna 31/03/20XX in questa cella vedremo il saldo contabile dei movimenti con data operazione tra il 01/03/20XX e il 31/03/20XX.
- Saldo Progressivo :  è il saldo progressivo del rapporto bancario per data operazione. Ad esempio se abbiamo impostato una periodicità mensile e stiamo analizzando la colonna 31/03/20XX in questa cella vedremo il saldo contabile dei movimenti con data operazione fino al 31/03/20XX.
- Stimati Periodo :  è il saldo dei movimenti stimati per il periodo.Ad esempio se abbiamo impostato una periodicità mensile e stiamo analizzando la colonna 31/03/20XX in questa cella vedremo il saldo dei movimenti stimati con data operazione tra il 01/03/20XX e il 31/03/20XX.
- Stimati Progressivo :  è il saldo progressivo dei movimenti stimati. Ad esempio se abbiamo impostato una periodicità mensile e stiamo analizzando la colonna 31/03/20XX in questa cella vedremo il saldo dei movimenti stimati con data operazione fino al 31/03/20XX.
- Disponibilità :  è la somma del fido e dei valori progressivi (1 + 2 + 4 + 6)

