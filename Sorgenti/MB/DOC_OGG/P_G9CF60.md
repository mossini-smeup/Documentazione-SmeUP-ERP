# Controllo Fatture di Acquisto
Con questa funzione si possono confrontare le fatture ricevute dai fornitori con le relative bolle di consegna ed i prezzi degli ordini.

La mappa video utilizzata per il controllo fatture è la seguente : 

![G9_01_01](http://localhost:3000/immagini/MBDOC_OGG-P_G9CF60/G9_01_01.png)
### Modalità di compilazione

|  R="0000000099" |
| 
| .COL Txt="**Campo**"  A="L" |
| ---|----|
| 
| .COL Txt="**Obb.**"  A="L" |
| 
| .COL Txt="**Descrizione**" LunAut="1" |
| - Causale contabile | Si | Definisce il tipo di trattamento da associare alla fattura che viene controllata |
| - Codice fornitore | Si |  A cui appartiene la fattura da controllare |
| - Assoggettamento fiscale | Si | Dall'anagrafico fornitore, può essere forzato manualmente, il campo sarà usato come selezione sulle bolle di entrata per selezionare solo le bolle con lo stesso assoggettamento IVA. |
| - Codice pagamento | Si | Derivato automaticamente dall'anagrafico fornitori |
| - Gestione Valuta |  | Se il fornitore può emettere fatture in valuta diversa (perché gli ordini sono in valuta diversa) si può compilare il campo e se questo è diverso da blank allora il sistema richiede obbligatorio i campi valuta e data cambio (il cambio viene ricavato in base alla tabella cambi). Si utilizzerà poi la valuta inserita per selezionare solo le bolle relative ad ordini della stessa valuta.  **Nota**, il cambio può essere forzato diverso da quello in tabella cambi. |
| 


### Metodi di elaborazione

|  R="0000000099" |
| 
| .COL Txt="**Azione**" A="L" |
| ---|----|
| 
| .COL  Txt="**Attività**" LunAut="1" |
| - Revisione fatture collegate | Seleziona solo bolle relative a fatture già inserite e contabilizzate. |
| - Revisione bolle in controllo | Seleziona solo bolle relative a fatture già inserite e con flag di blocco per controllo. |
| - Revisione bolle bloccate | Seleziona solo bolle relative a fatture già inserite e con flag di blocco. |
| - Non Contabilizzare | Permette di fare il controllo fatture, aggiornare il prezzo effettivo in Sme.up ma senza autorizzare l'invio in contabilità delle fatture controllate |
| - Gestione prezzi | Normalmente si visualizza e si può modificare l'importo totale di ogni riga di bolla, l'impostazione di questo metodo di elaborazione permette di attivare la gestione dei prezzi unitari (si potrà modificare il prezzo unitario, l'importo totale sarà ricalcolato). |
| 


Nella mappa video, oltre ai comandi funzione standard i seguenti comandi hanno funzioni particolari : 

- _3_F7 Revisione = per rivedere / modificare fatture già registrate ma non ancora contabilizzate (inviate in contabilità)
- _3_F5 Senza documento  e F8 Contabilità COGE = servono per contabilizzare direttamente da questa videata una fattura che non sia relativa  ad una bolla di ricevimento (queste funzioni sono in alternativa al data entry diretto nel Sistema di Contabilità Generale).


## Lista Bolle
Eseguita la selezione di ingresso il sistema presenta la lista delle bolle in attesa di controllo fatture. La lista è ordinata per numero bolla del fornitore e data bolla. : 

![G9_01_02](http://localhost:3000/immagini/MBDOC_OGG-P_G9CF60/G9_01_02.png)
La lista mostra, per il fornitore in input, tutte le bolle processate in Entrata Merci ed ancora in attesa di contabilizzazione :  sulla sinistra si vede il numero bolla data bolla della DDT del fornitore, al centro la quantità totale e l'importo totale per ogni bolla, a destra i numeri di riferimento interni che Sme.up associa ad ogni bolla processata.

Inserendo un carattere opportuno nel campo "S" si possono fare le azioni seguenti : 

- V = Visualizza; presenta la lista degli oggetti consegnati con la bolla, per ogni oggetto vengono presentati la quantità, l'importo e di i dati per la contabilizzazione (conto, centro di costo, commessa), anche da questo formato è possibile navigare ulteriormente nei dati gestionali :  T per vedere la testata ordine di acquisto, R per vedere la riga ordine, B per vedere la testata della bolla entrata merci, D per la riga di bolla.
- C = Contabilizza; per lanciare il processo di contabilizzazione
- G = Visualizza e Contabilizza; prima visualizza poi lancia la contabilizzazione
- A = Al controllo; inserisce un flag che sospende il proseguimento dell'attività su questa bolla, dopo che il problema è stato risolto si possono riprendere queste bolle compilando opportunamente le parzializzazioni in ingresso
- B = Blocco; inserisce un flag di blocco che sospende il proseguimento dell'attività su questa bolla, dopo che il problema è stato risolto si possono riprendere queste bolle compilando opportunamente le parzializzazioni in ingresso
- M = Messaggi; per aggiungere delle note alla bolla
- 5 = Dettaglio Bolla; presenta l'interrogazione della testata bolla entrata merci


## Contabilizzazione
Si usa il carattere "G", si possono selezionare contemporaneamente più bolle (quelle che sono indicate nella fattura del fornitore), con F6 si attiva l'azione.

Per le bolle selezionate il sistema presenta il formato seguente : 

![G9_01_03](http://localhost:3000/immagini/MBDOC_OGG-P_G9CF60/G9_01_03.png)
Gli importi della fattura vengono totalizzati per conto (anche centro di costo, voce di spesa, commessa dove applicabile), se manca il conto o se i dati sono incongruenti viene emessa segnalazione ed evidenziata la colonna di sinistra "E".
È possibile cambiare manualmente (o completare) le informazioni e confermare con F6, il sistema presenta il formato di seguente : 

![G9_01_04](http://localhost:3000/immagini/MBDOC_OGG-P_G9CF60/G9_01_04.png)
Deve essere inserito manualmente l'importo della fattura (rilevato dal documento cartaceo).
Per autorizzare la contabilizzazione il sistema controlla che l'importo fattura inserito manualmente corrisponda all'importo calcolato.

Gli altri dati da inserire sono : 

- Dati identificativi del documento (estremi) : 
-- Il numero documento e relativa data, sono il numero di protocollo IVA e la data di registrazione della fattura
-- Il numero riferimento e relativa data, sono numero e data fattura del fornitore
-- Il numero riferimento fornitore e la data effettiva dell'operazione sono informazioni opzionali rilevanti solo nel caso sia installata la Contabilità Generale e la Tesoreria ACG
- Dati legati al pagamento : 
-- Banca e codice pagamento sono derivati dalla mappa iniziale
-- Data scadenza e tipo pagamento se compilati vengono usati in alternativa al codice pagamento
-- Blocco del pagamento (per contabilizzare la fattura ma bloccare il pagamento in contabilità)

