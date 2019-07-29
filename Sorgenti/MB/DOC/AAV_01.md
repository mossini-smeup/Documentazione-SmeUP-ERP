# Produzione a commessa

## Definizione e caratteristiche
Una commessa può essere definita come un insieme di attività da portare a termine in una sequenza logico-temporale, con l'obiettivo di rispondere alle specifiche del cliente in termini di qualità, costo e tempi di consegna.

Caratteristiche : 
 * la produzione inizia su specifica richiesta del cliente
 * i prodotti sono studiati in funzione delle esigenze del cliente quindi si tratta di beni più o meno  differenziati tra loro, al limite unici
 * le caratteristiche della produzione dipendono direttamente dal grado di omogeneità dei prodotti, la struttura produttiva deve essere flessibile per adattarsi alle esigenze dei clienti;
 * la data di consegna viene stabilita in sede di ordine di vendita quindi condizionata dal cliente
 * il prezzo viene fissato prima dell'inizio dei lavori, attraverso la formulazione di un preventivo iniziale, prendendo in considerazione i costi che si ipotizzano possano essere sostenuti ed il margine di profitto

### Modalità operative
Dal punto di vista dell'impatto sui processi aziendali e sulle modalità operative possiamo elencare : 
 * **E.T.O. (Engineer to order - Progetta sulla base dell'ordine)**, il progetto intero o di una parte del prodotto viene eseguito solo dopo aver ricevuto l'ordine da parte del cliente
 * **M.T.O. (Make to order - Produci sull'ordine)**, la produzione viene attivata dopo il ricevimento dell'ordine cliente mentre le attività di progettazione/ingegnerizzazione possono essere anticipate
 * **A.T.O. (Assembly to order - Assembla sulla base dell'ordine)**, le parti componenti sono già state fabbricate mentre il motaggio finale viene eseguito solo dopo l'acquisizione dell'ordine. Questa tipologia prevede due modalità gestionali distinte : 
 ** la produzione su previsione di sottogruppi standard
 ** la successiva personalizzazione del prodotto finito in fase di assemblaggio finale in base a quanto richiesto dall'ordine.

## Confronto tra produzione per stock e produzione su commessa
![AAV_01_01](http://localhost:3000/immagini/AAV_01/AAV_01_01.png)
## Processi coinvolti
 * Gestione anagrafico commessa
 * Gestione offerte di vendita
 * Configurazione del prodotto
 * Formulazione del preventivo
 * Gestione ordine di vendita
 * Definizione del piano di fatturazione (es. a Stato Avanzamento Lavori)
 * Pianificazione generale di commessa
 * Gestione del progetto
 * Gestione dei retrofit
 * Pianificazione materiali
 * Documenti (ciclo passivo - ciclo interno) per commessa
 * Logistica interna per commessa
 * Consuntivi (avanzamento e movimenti)
 * Avviamento e installazione
 * Post vendita
 * Documentazione

### Anagrafico commesse
Gestione dei dati anagrafici della commessa
 * riferimenti (cliente, offerta, ordine, ..)
 * date significative (acquisizione, avvio / fine progetto, avvio / fine produzione, avvio / fine montaggio, collaudo, garanzia, ...)
**Esempi**
- [Anagrafico commessa](Sorgenti/MB/DOC/AAV_01_00)

**Note applicative**
Tabella Tipo Commessa = BSA
Per la commessa si può attivare la costruzione automatica del codice.
Quantità/Importi = tab. C£H_CM (sono possibili fino a 10 quantità)
Date implicite = tab. C£J_CM (sono possibili fino a 10 date)
Parametri impliciti si possono attivare fino a 5 campi alfanumerici + 5 campi numerici

### Offerte
Gestione delle offerte
 * Cliente
 * Destinazione
 * Revisione
 * Funzionalità ed opzioni
 * Prezzo di offerta
 * Scadenze e modalità di pagamento

In questa fase potrebbe essere già necessario aprire la commessa per imputare ad essa attività quali : 
 * Studio di fattibilità (ufficio tecnico)
 * Progettazione di massima (ufficio tecnico)
 * Prototipazione (reparti interni o terzisti)
 * Spese di consulenti esterni all'azienda

**Esempi**
- [Commessa su documenti di vendita](Sorgenti/MB/DOC/AAV_01_04)

**Note applicative**
............

### Configurazione del prodotto
A seconda dei casi il prodotto offerto può risultare dalla composizione di ogetti semilavorati o semifiti di produzione standard (in questo caso questi oggetti sono codificato come articoli ed hanno tutti gli attributi e le caratterisitche di un articolo) oppure l'oggetto offerto non esiste e deve essere progettato, in questi casi l'offerta si riferisce ad una tipologia di prodotto o di macchina / impianto e ad una serie di opzioni/funzioni associate.

**Esempi**
- [Distinta di commessa](Sorgenti/MB/DOC/AAV_01_02)

**Note applicative**
............

### Preventivi
Se la
Stima dei costi degli elementi prioritari del costo (ore per tipologia, materiali significativi, ...)

**Esempi**
............

**Note applicative**
............

### Ordini vendita
Vedi gestione offerte

**Esempi**
............

**Note applicative**
............

### Piano di fatturazione (SAL)
 * Modalità di pagamento / rate estemporanee
* .Avanzamento lavori per data/evento

**Esempi**
- [Piani di pagamento variabili](Sorgenti/MB/DOC/AAV_01_07)

**Note applicative**
............

### Pianificazione generale
 * Gantt di commessa
 * Flussi di cassa
 * Controllo avanzamento

**Esempi**
............

**Note applicative**
............
### Progettazione
 * Pianificazione attività del progetto
 ** vincoli prerequisiti
 ** risorsa assegnata
 * Avanzamento
 ** dichiarazione ore eseguite
 ** dichiarazione completamento / stima avanzamento attività
 * Distinta di commessa
 * Revisioni
 ** gestione cambi di progetto
 ** analisi impatto su produzioni in corso
 ** feedback da montaggio / post vendita

**Esempi**
- [Gestione progetti](Sorgenti/MB/DOC/AAV_01_01)
- [Dichiarazioni attività progettazione](Sorgenti/MB/DOC/AAV_01_06)

**Note applicative**
............

### Gestione retrofit
Analisi delle macchine preassemblate non assegnate disponibili
Analisi delle differenze
Emissione distinte di modifica

**Esempi**
............

**Note applicative**
............

### Pianificazione materiali
MRP per commessa

**Esempi**
............

**Note applicative**
............

### Produzione / montaggio
 * Pianificazione attività
 * Analisi mancanti
 * Avanzamento produzione

**Esempi**
- [Avanzamento produzione](Sorgenti/MB/DOC/AAV_01_14)
- [Confronto distinta tecnica e commessa](Sorgenti/MB/DOC/AAV_01_03)
- [Produzione a commessa](Sorgenti/MB/DOC/AAV_01_05)

**Note applicative**
............

### Acquisti
Righe ordine per commessa

**Esempi**
............

**Note applicative**
............

### Giacenze e movimenti
 * Giacenze per commessa
 * Prelievi per commessa (kit)

**Esempi**
............

**Note applicative**
............

### Consuntivi
 * Acquisti
 * Materiali
 * Attività
 * Valutazione avanzamento
 ** dichiarazioni di produzione
 ** stima % completamento attività

**Esempi**
- [Costi di commessa](Sorgenti/MB/DOC/AAV_01_11)

**Note applicative**
............

### Avviamento
 * Collaudo in house
 * Smontaggio e imballo
 * Spedizione
 * Montaggio c/o cliente
 * Collaudo c/o cliente
 * Benestare di collaudo

**Esempi**
............

**Note applicative**
............

### Post vendita
 * Distinta commessa aggiornata
 * Assistenza
 * Ricambi
 * Garanzie
 ** sull'impianto
 ** sui particolari sostituiti
 * Destinazione finale (vendita da un cliente ad un altro)
 * Commessa madre - commesse figlie

**Esempi**
............

**Note applicative**
............

### Documentazione di commessa
 * Progetto
 * Disegni
 * Tavole di montaggio
 * Manuali di utilizzo
 * Certificazioni

**Esempi**
............

**Note applicative**
............
