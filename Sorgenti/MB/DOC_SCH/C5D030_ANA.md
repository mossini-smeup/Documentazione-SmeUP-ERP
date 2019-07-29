## Obiettivo
Obiettivo di questa scheda è analizzare l'anagrafica dei rapporti bancari definiti per l'azienda e accedere alla configurazione delle condizioni dei diversi rapporti e alle analisi dei movimenti associati ai diversi rapporti.

![C5D030_050](http://localhost:3000/immagini/MBDOC_SCH-C5D030_ANA/C5D030_050.png)
## Dettaglio informazioni
Per ogni rapporto bancario è possibile visualizzare : 
 * Tipo rapporto :  è definito all'interno della tabella C5J
 * Valuta :  è definito all'interno dell'anagrafica del conto contabile (tabella C5B)
 * Codice banca :  è il codice ABI CAB della banca a cui è associato il rapporto
 * Codice C/C :  è il numero di conto corrente
 * Iban :  è l'iban derivante dalla combinazione del codice banca e del numero di conto corrente ed è definito all'interno dell'estensione £21 dell'anagrafica aziendale
 * Swift :  è definito all'interno dell'estensione £21 dell'anagrafica aziendale
 * Conto contabile :  è il conto di contabilizzazione dei movimenti del rapporto bancario
 * Data consolidamento :  è la data dell'ultimo consolidamento effettuato sul rapporto bancario
 * CUP/CIG :  per ogni rapporto bancario definisce se accetta o meno i codici CUP e CIG
 * Banca azienda :  è la banca a cui è associato il rapporto
 * Circuito :  riporta il circuito definito sulla banca a cui è associato il rapporto (tabella C5F)
 * Intermediario Extrabancario :  definisce se il rapporto bancario rappresenta un intermediario extrabancario (es. società di factor) o meno
 * Note :  espone le note riportate sul rapporto bancario
 * Segnalazioni :  nel caso in cui siano presenti errori nella configurazione del rapporto bancario, il rapporto viene  evidenziato in rosso e in questa colonna viene indicato l'errore rilevato

## Opzioni
Per ogni rapporto bancario sono disponibili le opzioni : 
 * Scheda dati anagrafici completi :  permette di visualizzare all'interno di un'unica videata il dettaglio dei dati anagrafici del rapporto bancario
 * Gestione coordinate complete :  mi permette di manutenere IBAN e SWIFT associati al rapporto
 * Gestione condizioni affidamento :  permette di impostare i tassi di interesse e le condizioni di tenuta conto del rapporto
 * Gestione condizioni per operazione :  permette di impostare spese e altre condizioni per le diverse operazioni bancarie eseguite sul rapporto
 * Gestione archivio saldi :  permette di analizzare l'archivio saldi del rapporto bancario

All'interno delle funzioni di Fly è poi possibile accedere alle interrogazioni di tesoreria in cui sono visualizzabili : 
 * Estratto conto per Data Operazione :  riporta il dettaglio dei movimenti ordinati per data operazione bancaria
 * Estratto conto per Data Valuta :  riporta il dettaglio dei movimenti ordinati per data valuta
 * Movimenti di Remote del rapporto selezionato :  riporta il dettaglio dei movimenti provenienti da remote banking e caricati a sistema
 * Analisi del castelletto del rapporto (per rapporti SBF) :  riporta il dettaglio delle scadenze presenti nel castelletto del rapporto con le relative scadenze e valute




