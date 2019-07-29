# Introduzione dei concetti di Azienda e Scenario

## Database multiaziendale
Al fine di ottimizzare la codifica ed evitare la ridondanza delle informazioni (con tutto ciò che ne può conseguire), è stata introdotta l'opportunità di gestire l'anagrafica in un unico
database comune.

La rilevanza di ogni informazione viene gestita a vari livelli e, in particolare, è possibile decidere che il tipo contatto abbia : 

- una rilevanza comune per tutte le aziende, per le quali pertanto sarà necessario codificare i contatti una volta sola (un esempio idoneo a tale configurazione è dato dall'anagrafica banche);
- una rilevanza specifica per ogni singola azienda (il codice può/deve essere attivato per una, tutte o soltanto alcune aziende).

Un altro livello di configurazione è presente nella seconda tipologia di gestione del tipo contatto :  è infatti possibile definire quali informazioni del contatto abbiano una valenza comune e
quali, viceversa, una specifica per ogni azienda.

Le informazioni vengono assunte di default con una valenza comune e codificate, pertanto, una sola volta :  la variazione della ragione sociale di una azienda verrà automaticamente
modificata in tutti i gestionali delle società in cui essa abbia il medesimo codice.
Questo però non vincola le varie società a gestire altri dati dell'impresa in oggetto in modo differente :  è possibile, ad esempio, stabilire codici pagamento differenti, che varranno solo
per l'azienda specifica in cui l'aggiornamento avviene.

Tale struttura è applicabile in modo libero a qualsiasi campo/estensione anagrafica.

## Database multiscenario
La conformazione illustrata può essere applicata anche a un livello di dettaglio più basso, denominato "scenario" :  ad esempio alla divisione, la filiale, la linea di vendita o l'insieme delle stesse.

# Introduzione del concetto di Nominativo
Un effetto simile a quello dato dall'ottimizzazione della codifica di informazioni comuni di un codice multiaziendale si può ottenere anche a un livello più alto, che prende in
considerazione non il semplice codice, ma la persona fisica/giuridica in tutte le vesti assunte nell'ambito aziendale
(es. uno stesso soggetto potrebbe essere, per l'azienda, sia cliente che fornitore).

A questo proposito è possibile attivare la gestione di un tipo contatto "nominativo" che identifichi univocamente la persona fisica/giuridica e a cui facciano
riferimento tutte le cariche da essa rivestite.

In questo modo, definendo anche le informazioni da codificare nel nominativo, ogni modifica fatta avrà una valenza per tutti i codici collegati (stabilendo, ad esempio, la gestione della
ragione sociale, indirizzo, telefoni e mail a livello di nominativo).

La modifica di uno di questi dati varrà per tutti i codici collegati (siano questi clienti o fornitori).

Tale relazione farà inoltre da perno per l'interrogazione incrociata delle varie situazioni del soggetto inteso come persona fisica/giuridica (ad esempio, il partitario contabile
ottenuto dalla fusione della situazione del codice cliente collegato e del codice fornitore collegato).

L'attivazione è per tipo contatto e, pertanto, è possibile decidere di attivarla per i clienti/fornitori e non per le banche.

# Introduzione del concetto di Data Effective
E' stata introdotta la possibilità di gestire la storicizzazione delle modifiche anagrafiche.

Tale gestione è attivabile a livello di tipo contatto e di singolo campo/estensione.

In pratica, per ogni tipo contatto si indicano le informazioni che si intendono storicizzare (es. ragione sociale, partita IVA ecc.).

L'anagrafica sarà perciò accessibile in funzione della configurazione storica; ad esempio, nella stampa fatture, l'anagrafica verrà agganciata in funzione della configurazione rilevante alla data fattura.

Questo viene ottenuto inserendo nell'interfaccia anagrafica la data da prendere in considerazione.

# Flessibilità e configurabilità del Data Entry
E' stata introdotta una nuova gestione del data entry anagrafico, attivabile in modo opzionale se non è stata utilizzata una delle funzioni sopra elencate, che comportano
invece automaticamente il passaggio alla nuova gestione.

Le nuove funzionalità si possono riassumere nel seguente modo : 

- _2_gestione a lista/subfile dei dati (con la possibilità di codificare/visualizzare in un'unica sessione dati multiazienda/scenario, ordinandoli per campo o per scenario);
- _2_codifica univoca per le informazioni comuni ai soggetti multiazienda/scenario;
- _2_unificazione della gestione dei campi anagrafici e delle estensioni in un unico data entry;
- _2_definizione di prospettive di interrogazione dei campi (es. dati commerciali, dati finanziari, ecc...), configurabili tramite semplice script con elenco dei campi/estensioni;
- _2_autorizzazioni a livello di tipo contatto/scenario/prospettiva/campo;
- _2_file di work delle gestione delle modifiche (che permette di riprendere le modifiche in caso di caduta della sessione, senza perdere la congruenza dei dati), configurabili tramite semplice script con elenco dei campi/estensioni.


## Passaggio alle nuove funzionalità
Tutte le nuove funzioni sono scalabili e attivabili separatamente, perciò ognuno potrà decidere di mantenere l'anagrafica oppure di attivare l'una o l'altra funzione.

Per ognuna delle nuove funzioni saranno comunque disponibili anche dei programmi di utilità, che agevoleranno il passaggio alle nuove funzioni con stampe di controllo e azioni di aggiornamento/scrittura.

# Perfezionamento ed estensione del tracciato

## File Anagrafico
_2_Campi aggiunti : 

- Scenario/Azienda
- Data inizio/Fine Validità
- 5 Date Libere
- Estensione dei flag da 20 a 40
- Ora inserimento/aggiornamento
- Utente inserimento
- Tipo/Codice Ente Nominativo
- IDOJ
- IBAN
- Swift


_2_Campi modificati : 

- Mail (da 20 a 132)
- Categoria contabile (da 6 a 15)
- Fido (da 6/0 a 21/6)



## File Estensioni Anagrafiche
_2_Campi aggiunti : 

- Scenario/Azienda
- Data inizio/Fine Validità
- 5 Date Libere
- 5 Codici Liberi
- 5 Numeri Liberi
- Estensione dei flag da 5 a 40
- Un campo libero esteso
- Ora inserimento/aggiornamento
- Utente inserimento


## Schermate di esempio : 
![BR_V002_01](http://localhost:3000/immagini/BRENTI_001/BR_V002_01.png)
![BR_V002_02](http://localhost:3000/immagini/BRENTI_001/BR_V002_02.png)i per campo)

![BR_V002_03](http://localhost:3000/immagini/BRENTI_001/BR_V002_03.png)i  per scenario)

![BR_V002_04](http://localhost:3000/immagini/BRENTI_001/BR_V002_04.png)