# Obiettivo
Eseguire le azioni di tipo MFP sui contenitori

# Funzioni
 * >INZ, Inizializzazione.
 * >CTR, Controlli.
 * >WRI, Scrittura.

## Premessa
La scrittura può eseguita solo dopo aver eseguito prima l'inizializzazione e il controllo e solo se il controllo ha dato esito positivo.
Si indica con _3_Ubicazionela tripletta :  Magazzino, Ubicazione, Fase.
L'_3_Ubicazione ANTEsarà :  Magazzino, Ubicazione Ante, Fase.
L'_3_Ubicazione POSTsarà :  Magazzino, Ubicazione Post, Fase.

_2_Inizializzazione
L'inizializzazione pulisce i campi di output e acquisisce l'elemento della tabella P5H relativo all'azione che si vuole eseguire. In particolare la P5H contiene il tipo di azione.

_2_Controllo
 I controlli sono specifici per ogni tipo azione. Verificano la validità dei dati di input. Se hanno avuto tutti esito positivo vengono passati ai dati di output e si può procedere alla scrittura.

_2_Scrittura
La scrittura è specifica per ogni tipo azione :  ogni tipo azione esegue delle proprie funzioni con i dati di output ricevuti dal controllo; pertanto prima di eseguirla è necesario eseguire le due funzioni precedenti di inzializzazione e controllo. In ogni caso la scrittura viene eseguita solo se sono stati ricevuti tutti i campi necessari per il tipo di azione.

## Flusso

|  Nam="Ciclo" R="90" |
| 
| .COL Cod="U01A" Txt="Ubicazione A" LunAut="1" A="C" |
| ---|----|
| 
| .COL Cod="F01" Txt="Fase"  LunAut="1" A="C" |
| 
| .COL Cod="U01P" Txt="Ubicazione P"  LunAut="1" A="C" |
| 
| .COL Cod="L01" Txt="Azione "  LunAut="1" A="C" |
| 
| .COL Cod="M01" Txt="Movimenti" LunAut="1" A="C" |
|  U1AN | 0010 | U1PS | _2_Riempimento | _1_Prelievo |
|  U1PS |          | U2AN | _2_Spostamento | |
|  U2AN | 0020 | U2PS | _2_Avanzamento | |
|  U2PS |          | U3AN | _2_Spostamento | |
|  U3AN | 0030 | U3PS | _2_Avanzamento| |
|  U3PS |          | U4AN | _2_Spostamento| |
|  U4AN | 0040 | U4PS | _2_Avanzamento | _1_Versamento |
| 


# Tipi azione
Sono stati definiti i seguenti tipi di azione : 
 * >01 = Creazione contenitore Pianificato :  crea un contenitore e scarica da uno pianificato.
 * >02 = Creazione contenitore NON Pianificato :  crea un contenitore senza scarico di uno pianificato.
 * >05 = Ritorno Contenitore Pianificato Disponibile :  determina il primo contenitore pianificato
 * >06 = Ritorno Contenitore da Alias :  dato un alias ristorna il contenitore associato
 * >09 = Consumo pianificato :  scarica una qtà/contenitore pianificata.
 * >11 = Avanzamento contenitore Da/A :  fase iniziale e finale sono dichiarate. Il contenitore di destinazione può essere esplicito o creato al momento.
 * >12 = Avanzamento contenitore Da/A (Fase successiva)
 * >13 = Avanzamento contenitore A/Da (Fase precedente assoluta)
 * >14 = Avanzamento contenitore A/Da (Fase precedente con giacenza nello stesso contenitore)
 * >15 = Avanzamento contenitore A/Da (Fasi precedenti con giacenza in qualunque contenitore)
 * >16 = Avanzamento contenitore A/Da (Fasi precedenti prima con giacenza nello stesso contenitore e poi con risalita in giacenza qualunque contenitore)
 * >21 = Trasferimento interno MFP (Spostamento) :  per spostare la giacenza all'interno dell'area MFP senza dichiarare attività. Il contenitore di destinazione può essere esplicito o creato al momento. Questa azione può essere usata anche per accorpamenti (da n contenitori a 1) o per smembramenti (da 1 a n contenitori).
 * >31 = Trasferimento esterno MFP (Uscita :  Perso)
 * >32 = Trasferimenti esterno MFP (Entrata :  Rilavorazione)
 * >41 = Rettifica quantità contenitore
 * >42 = Annullamento contenitore
 * >43 = Stampa contenitore


## Az.01. Creazione contenitore pianificato
Per l'ordine e la quantità richiesta crea un nuovo contenitore, _2_pianificato. Se non riceve la quantità usa quella standard del contenitore.
A seconda dei campi di input il codice contenitore può essere : 
 * dato da un numeratore interno (il contenitore di destinazione è vuoto ed è impostato il flag di creazione contenitore)
 * fornito dall'utente (il contenitore di destinazione è compilato con un codice che non è già presente in anagrafica contenitori)
 * dato da un numeratore interno e associato ad un alias fornito dall'utente  (il contenitore di destinazione è vuoto ed è impostato il flag di creazione contenitore, oppure è compilato con un codice utente che non è già presente in anagrafico, ed è presente l'alias) il nuovo contenitore viene associato all'alias ricevuto, il contesto dell'alias deve essere definito in tabella C£K.
### Input
 * Numero ordine (Obbligatorio)
 * Quantità
 * Contenitore destinazione (facoltativo, se compilato deve essere un codice nuovo)
 * Flag creazione contenitore (facoltativo)
 * Alias (facoltativo)
### Controlli
 * Il contenitore destinazione NON deve già esistere.
 * L'ordine deve esistere ed essere di tipo MFP
 * Non deve essere un'azione di scarto
### Scrittura (solo se presente l'ordine e il contenitore destinazione)
 * Crea il contenitore destinazione
 * Se presente crea l'alias del contenitore destinazione
 * Scarica un contenitore/qtà pianificato

## Az.02. Creazione contenitore non pianificato
Per l'ordine e la quantità richiesta crea un nuovo contenitore, _2_NON pianificato. Il resto del comportamento è come per il tipo azione 01con l'eccezione che non scarica i pianificati.

## Az.05. Ritorno Contenitore Pianificato Disponibile
Per l'ordine ritorna il prossimo contenitore pianificato.
### Input
 * Numero ordine (Obbligatorio)
### Controlli
 * L'ordine deve esistere ed essere di tipo MFP
### Scrittura (solo se presente l'ordine)
 * Ritorna nel contenitore di destinazione il contenitore pianificato

## Az.06. Ritorno Contenitore da alias
Dato l'alias ritorna il contenitore.
### Input
 * Numero ordine (Obbligatorio, solo se nella tabella P5M esistono più tipi MFP, altrimenti deriva il contesto Alias dall'unico tipo MFP in tabella P5M)
### Controlli
 * L'ordine, se passato, deve esistere ed essere di tipo MFP
### Scrittura (solo se presente l'ordine)
 * Ritorna nel contenitore di destinazione il contenitore

## Az.09. Consumo pianificato
Si verifica ad esempio in caso di riduzione della qtà dell'ordine, tutti i contenitori pianificati residui vengono consumati.

## Az.11. Avanzamento contenitore Da/A
Devono essere dati sia l'origine che la destinazione.
L'avanzamento determina : 
 * il movimento di carico nell'_3_Ubicazione di destinazione
 * il movimento di scarico dall'_3_Ubicazione origine
 * la dichiarazione di tutte le attività relative alla fasi comprese tra le due ubicazioni
 * l'aggiornamento della quantità riempita sul contenitore (_2_NOTA il comportamento è diverso quando siamo nella prima o nell'ultima fase del ciclo, vedi paragrafo "_1_Gestione prima e ultima fase del ciclo nel capitolo "Controlli e funzioni generali").
 * Se nell'avanzamento viene dichiarata la prima fasei :  aggiorna la quantità riempita sul contenitore destinazione, e se richiesto, aggiorna saldo contenitore.
### Input
 * Contenitore origine (Obbligatorio, se non presente si assume uguale al contenitore destinazione)
 * Magazzino origine (Obbligatorio se gestione multimagazzino)
 * Ubicazione origine (Obbligatoria)
 * Fase origine  (Obbligatoria se ubicazione multifase)
 * Contenitore destinazione (Obbligatorio, può essere :  un contenitore esistente -con o senza alias, un codice utente, un codice "*N" con o senza alias - in quest'ultimo caso il codice viene assegnato dal numeratore colli)
 * Magazzino destinazione (Obbligatorio se gestione multimagazzino)
 * Ubicazione destinazione (Obbligatoria)
 * Fase destinazione  (Obbligatoria se ubicazione multifase)
 * Quantità (Obbligatoria)
 * Se avanzamento su altro contenitore
 ** Saldo contenitore (Obbligatorio se si vuole proseguire l'avanzamento su altro contenitore)
### Controlli
 * Se manca il contenitore origine lo assume da destinazione, se manca il contenitore destinazione lo assume da origine (in questi casi si avanza lo stesso contenitore)
 * Deve essere presente nella tabella P5H la cauale avanzamento
 * Esegue_3_controlli riempimentosu destinazione
 * Esegue_3_controlli svuotamentosu origine
 * Esegue_3_controlli congruenza origine/destinazione
 * Controllo avanzamento (La fase+ubicazione destinazione deve essere successiva alla fase+ubicazione origine)
### Scrittura
 * Solo se presenti causale, contenitore, magazzino, ubicazione, fase origine; causale, contenitore, magazzino, ubicazione, fase destinazione; causale avanzamento; quantità.
 ** Movimento su origine (Se non è la prima _3_Ubicazione ANTE. In questo caso il movimento è generato dalla dichiarazione di attività della prima fase come prelievo componenti)
 ** Movimento su destinazione(Se non è l'ultima_3_Ubicazione POST. In questo caso il movimento è generato dalla dichiarazione di attività dell'ultima fase come versamento a magazzino)
 ** Dichiarazioni di tutte le attività relative alle fasi comprese tra le due ubicazioni (origine / destinazione)
 ** Se avanzamento su altro contenitore
 *** Aggiornamento contenitore destinazione :  Quantità riempimento e se richiesto saldo contenitore

## Az.12. Avanzamento contenitore Da/A (fase successiva)
Data un'origine determina la prima fase successiva.
(vedi :  _3_Az.21. Avanzamento contenitore Da/A)
### Differenze : 
 * Input
 ** Contenitore origine facoltativo, se non presente deriva da destinazione
 ** Magazzino, Ubicazione e Fase destinazione calcolati
 * Controlli
 ** Nel_3_controlli riempimentosu destinazione, determina dal ciclo del contenitore di destinazione l'_3_Ubicazione di destinazione :  è la fase + ubicazione successiva alla fase + ubicazione origine, se non trovata segnala l'anomalia.

## Az.13. Avanzamento contenitore A/Da fase precedente
Data una destinazione determina la fase immediatamente precedente indipendentemente dalla giacenza.
(vedi :  _3_Az.21. Avanzamento contenitore Da/A)
### Differenze : 
 * Input
 ** Contenitore origine obbligatorio
 ** Magazzino, Ubicazione e Fase origine calcolati
 * Controlli
 ** Nel_3_controlli svuotamentosu origine, determina dal ciclo del contenitore origine l'_Ubicazione origine e la fase + ubicazione precedente alla fase + ubicazione destinazione, se non trovata segnala l'anomalia..

## Az.14. Avanzamento contenitore A/Da fasi precedenti con giacenza sul contenitore origine
Data la quantità e i contenitori (destinazione/origine) in input, ricerca tutte le giacenze nelle ubicazioni precedenti fino ad esaurimento quantità, per ogni coppia di ubicazioni (origine / destinazione) trovata lancia i movimenti e gli avanzamenti (funzione 21).
_2_Nota, le giacenze vengono ricercate per il ciclo del contenitore di destinazione
### Input
 * Contenitore origine (facoltativo, se non presente assume uguale a contenitore destinazione)
 * Contenitore destinazione (Obbligatorio, può essere :  un contenitore esistente -con o senza alias, un codice utente, un codice "*N" con o senza alias - in quest'ultimo caso il codice viene assegnato dal numeratore colli)
 * Magazzino destinazione (Obbligatorio se gestione multimagazzino)
 * Ubicazione destinazione (Obbligatoria)
 * Fase destinazione  (Obbligatoria se ubicazione multifase)
 * Quantità (Obbligatoria)
 * Se avanzamento su altro contenitore
 ** Fine contenitore (Obbligatorio per poter iniziare l'avanzamento su altro cotenitore)
### Controlli
 * Deve essere presente nella tabella P5H la cauale avanzamento
 * Esegue_3_controlli riempimentosu destinazione
 * Esegue_3_controlli contenitoresu origine
 * I contenitori origine e destinazione devono essere sullo stesso ordine
### Scrittura
 * Solo se presenti causale, contenitore origine; causale, contenitore, magazzino, ubicazione, fase destinazione :  causale avanzamento; quantità.
 * Acquisisce tutte le_3_FASI(con ubicazione) del ciclo del contenitore origine.
 * Dalla fase+ubicazione destinazione(esclusa) arretrando per ogni_3_Ubicazioneorigine trovata con giacenza, esegue l'avanzamento : 
 ** Con quantità giacenza se minore della quantità dichiarata, altrimenti con con quantità dichiarata
 ** Esegue_3_Avanzamento contenitore Da/A
 ** Decrementa la quantità dichiarata con quantità usata nell'avanzamento
 ** Quando la quantità dichiarata finisce termina l'avanzamento
 * Se rimane residuo, esegue _3_Riempimento contenitorecon la quantità residua alla fase destinazione

## Az.15. Avanzamento contenitore A/Da fasi precedenti con giacenza su tutti i contenitori dell'ordine
Fino ad esaurimento della quantità richiesta, opera una serie di avanzamenti andando a ritroso dalle ubicazioni più vicine alla destinazione, sia per lo stesso contenitore che per altri.
Se rimane del residuo esegue un riempimento alla fase di destinazione del ciclo del contenitore destinazione.
_2_Nota, le giacenze vengono ricercate per tutti i cicli dei contenitori appartenenti allo stesso ordine del contenitore di destinazione

### Input
 * Contenitore destinazione (Obbligatorio, può essere :  un contenitore esistente -con o senza alias, un codice utente, un codice "*N" con o senza alias - in quest'ultimo caso il codice viene assegnato dal numeratore colli)
 * Magazzino destinazione (Obbligatorio se gestione multimagazzino)
 * Ubicazione destinazione (Obbligatoria)
 * Fase destinazione  (Obbligatoria se ubicazione multifase)
 * Quantità (Obbligatoria)
 * Se avanzamento su altro contenitore
 ** saldo contenitore (Obbligatorio per poter iniziare l'avanzamento su altro contenitore)
### Controlli
 * Deve essere presente nella tabella P5H la causale avanzamento
 * Esegue_3_controlli riempimentosu destinazione
 * Deve essere presente nella tabella P5H la causale origine
### Scrittura
 * Solo se presenti causale origine; causale, contenitore, magazzino, ubicazione, fase destinazione; causale avanzamento; quantità.
 * Acquisce tutte le_3_FASI(con ubicazione e giacenza) dei cicli di tutti i contenitori dell'ordine, precedenti alla fase+ubicazione di destinazione.
 * Dalla fase destinazione(escusa) arretrando per ogni_3_Ubicazione e relativo contenitore origine trovati, esegue l'avanzamento : 
 ** Con quantità giacenza se maggiore della quantità dichiarata, altrimenti con con quantità dichiarata
 ** Esegue_3_Avanzamento contenitore Da/A
 ** Decrementa la quantità dichiarata con quantità usata nell'avanzamento
 ** Quando la quantità dichiarata finisce termina l'avanzamento
 * Se rimane residuo, esegue _3_11. Riempimento contenitorecon la quantità residua alla fase destinazione

## Az.16. Avanzamento contenitore A/Da tutti i contenitori dell'ordine con giacenza su fasi precedenti
Esegue l'azione 15 e per il residuo risale alla 16

## Az.21. Trasferimento interno MFP contenitore
Il trasferimento interno determina un movimento di scarico dalla_3_Ubicazione origine e il corrispondente movimento di carico nella_3_Ubicazione destinazione anche di contenitori diversi.
Non è possibile scegliere una quantità superiore alla giacenza per fase del contentore origine.
### Input
 * Contenitore origine (facoltativo, se non presente assume contenitore destinazione)
 * Magazzino origine (Obbligatorio se gestione multimagazzino)
 * Ubicazione origine (Obbligatoria)
 * Fase origine (Facoltativa)
 * Contenitore destinazione (Obbligatorio, può essere :  un contenitore esistente -con o senza alias, un codice utente, un codice "*N" con o senza alias - in quest'ultimo caso il codice viene assegnato dal numeratore colli)
 * Magazzino destinazione (Obbligatorio se gestione multimagazzino)
 * Ubicazione destinazione (Obbligatoria)
 * Fase destinazione  (Obbligatoria se ubicazione multifase)
 * Quantità (Obbligatoria)
### Controlli
 * Se il contenitore origine è blank assume quello di destinazione
 * L'isieme dei campi origine deve essere diverso da destinazione
 * Esegue_3_controlli svuotamentosu origine
 ** Esegue_3_controlli riempimentosu destinazione
### Scrittura
 * Solo se presenti causale, contenitore, magazzino, ubicazione, fase origine; causale, contenitore, magazzino, ubicazione, fase destinazione; quantità.
 ** Movimento scarico origine
 ** Movimento carico destinazione

## Az.31. Trasferimento esterno MFP Contenitore :  Uscita (Perso)
Il trasferimento esterno di tipo uscita determina un movimento di scarico dalla_3_Ubicazione origine e il corrispondente movimento di carico in una giacenza esterna all'MFP dello stesso contenitore. Nel movimento di carico il contenitore, magazzino, ubicazione e fase destinazione sono quelli origine.
Per modificare o completare le chiavi di giacenza usare il programma di exit.
### Input
 * Contenitore origine (Obbligatorio)
 * Magazzino origine (Obbligatorio se gestione multimagazzino)
 * Ubicazione origine (Obbligatoria)
 * Fase origine  (Obbligatoria se ubicazione multifase)
 * Quantità (Obbligatoria)
### Controlli
 * Esegue_3_controlli svuotamentosu origine
 * Deve essere presente nella tabella P5H la causale destinazione
### Scrittura
 * Solo se presenti causale, contenitore, magazzino, ubicazione, fase origine; causale destinazione; quantità.
 * Movimento sacrico origine
 * Movimento carico destinazione (Se eseguiti controlli il contenitore, magazzino, ubicazione e fase sono quelli origine)
 * Decrementa quantità contenitore origine

## Az.32. Trasferimento esterno MFP contenitore :  Entrata (Rilavorazione)
Il trasferimento esterno di tipo Entrata determina un movimento di scarico da una giacenza esterna all'MFP e un corrispondente movimento di carico sulla_3_Ubicazione destinazione dello stesso contenitore.
Il contenitore può essere accodato ad un ordine esistente o ad un nuovo ordine.
### Input
 * Numero record GMQUAN origine (Obbligatorio)
 * Contenitore destinazione (Obbligatorio)
 * Magazzino destinazione (Obbligatorio se gestione multimagazzino)
 * Ubicazione destinazione (Obbligatoria)
 * Fase origine (Obbligatoria se ubicazione multifase)
 * Quantità (Obbligatoria)
 * Ordine(Facoltativo)
### Controlli
 * Deve essere presente nella tabella P5H la causale origine
 * La quantità in giacenza deve essere positiva
 * Il tipo e area giacenza nella causale origine devono corrispondere a quelli in giacenza
 * Esegue_3_controlli contenitoresu origine
 * Esegue_3_controlli riempimentosu destinazione
 * L'articolo del contenitore e della giacenza devono corrispondere
 * La quantità richiesta NON deve essere superiore a giacenza
### Scrittura
 * Solo se presenti causale origine; causale, contenitore, magazzino, ubicazione, fase destinazione; quantità.
 * Creazione nuovo ordine se non ricevuto
 * Aggiorna ordine su contenitore
 * Movimento origine
 * Movimento destinazione
 * Incrementa quantità contenitore destinazione

## Az.41. Rettifica quantità contenitore
La rettifica quantità del contenitore esegue un movimento sulla_3_Ubicazione destinazione per la quantità richiesta.
### Input
 * Contenitore destinazione (Obbligatorio)
 * Magazzino destinazione (Obbligatorio se gestione multimagazzino)
 * Ubicazione destinazione (Obbligatoria)
 * Fase destinazione (Obbligatoria se ubicazione multifase)
 * Quantità (Obbligatoria)
### Controlli
 * Esegue_3_controlli riempimentosu destinazione
 * Se la quantità richiesta è negativa NON deve essere in valore assoluto superiore alla quantità riempita nel contenitore
### Scrittura
 * Solo se presenti causale, contenitore, magazzino, ubicazione, fase destinazione; quantità.
 * Movimento destinazione.
 * Incrementa (valore algebrico) quantità contenitore destinazione.

## Az.42. Annullamento contenitore
Esegue l'annullamento logico del contenitore. L'azione è ammessa solo se il contenitore non è in giacenza.
### Input
 * Contenitore destinazione (Obbligatorio)
### Controlli
 * Esistenza contenitore
 * Il contenitore non deve essere in giacenza
### Scrittura
 * Solo se presente causale, contenitore destinazione;
 * Annullamento logico contenitore destinazione

## Az.43. Stampa contenitore
Esegue la stampa del contenitore.
### Input
 * Contenitore destinazione (Obbligatorio)
### Controlli
 * Esistenza contenitore
### Scrittura
 * Esegue la stampa

# Controlli e funzioni generali
## Controlli svuotamento
 * Esegue_3_Controlli contenitore sulla causale e contenitore origine
 * Esegue_3_Controlli ciclosul magazzino, ubicazione, fase origine

## Controlli riempimento
 * Esegue_3_Controlli contenitore sulla causale e contenitore destinazione
 * Esegue_3_Controlli ciclosul magazzino, ubicazione, fase destinazione

## Controlli congruenza origine/destinazione
 * Controlla che il contenitore origine e destinazione siano sullo stesso ordine
 * Controlla che la_3_Ubicazionedestinazione appartenga al ciclo del contenitore origine

## Controlli contenitore
 * Causale movimentazione obbligatoria
 * Contenitore obbligatorio, esistente e di tipo MFP
 * Se il controllo è sull'origine, il contenitore deve essere dichiarato saldato alla fase precedente, se esisite
 * Se il controllo è sulla destinazione il contenitore NON deve essere stato saldato alla fase corrente

## Controlli ciclo
 * Se monomagazzino assume default
 * Magazzino obbligatorio
 * Controllo esistenza magazzino
 * Controllo che il magazzino appartenga al ciclo del corrispondente contenitore
 * Ubicazione obbligatoria
 * Controllo esistenza ubicazione
 * Controllo ubicazione di tipo MFP
 * Controllo che l'ubicazione (Magazzino/Ubicazione) appartenga al ciclo del corrispondente contenitore
 * Se non è presente la fase e l' ubicazione è monofase deriva la fase dal ciclo
 * Fase obbligatoria
 * Controllo che l'_3_Ubicazione appartenega al ciclo del corrispondente contenitore

## Scrittura
La funzione di scrittura è divisa in 5 parti : 
 * Movimenti origine
 * Movimenti destinazione
 * Dichiarazioni attività (solo se si sta avanzando)
 * Azioni contenitore
 ** Creazione
 ** Riempimento
 ** Aggiornamento quantità
 ** Annullamento
 ** Stampa
 * Azioni ordine
 ** Rifasatura impegni
 ** Rifasatura quantità

La stampa del contenitore e le azioni sull'ordine sono sempre eseguite, mentre le altre dipendono dall'azione che si sta eseguendo

## Movimentazione prima e ultima fase del ciclo
Nella prima fase del ciclo non vengono fatti i movimenti di scarico sull'ubicazione ante (sono demandati alla G35 lanciata a standard dalla dichiarazione sulla prima fase).
Nell'ultima fase del ciclo non vengono fatti i movimenti di carico sull'ubicazione post (sono demandati alla G35 lanciata a standard dalla dichiarazione sull'ultima fase).

# APPENDICE
 * >Causali
 * >Quantità

## Causali
Le causali sono di 5 tipi : 
 * Causale avanzamento
 ** E' la causale usata nella dichiarazioni di attività. E' definita nella tabella "P5H".
 * Causale prelievo materiali.
 ** E' la causale usata dalla movimentazione per il prelievo dei materiali da magazzino. E' definta nella tabella "P5I". Il prelievo dei materilali è generato dalla dichiarazione attività della prima fase.
 * Causale origine MFP
 ** E' la causale di scarico usata dalla movimentazione nell'avanzamento MFP. E' definita nella tabella "P5H".
 * Causale destinazione MFP
 ** E' la causale di carico usata dalla movimentazione nell'avanzamento MFP. E' definita nella tabella "P5H".
 * Causale versamento finito
 ** E' la causale usata dalla movimentazione per il versamento a magazzino del finito. E' definita nei parametri logistici "£P2 - 1P2 - 2P2". Il versamento è generato dalla dichiarazione attività dell'ultima fase..

## Quantità
 * _3_Ordine
 ** Ordinata :  QT01 (Manuale)
 ** Prodotta :  QT02 (Da Versamento)
 ** Contenitori :  QT05 (Calcolata) = QTPA (Pianificata) + QTCO (Riempita)
 * _3_Contenitore
 ** Ordinata QTAO (Da creazione contentore)
 ** Riempita QTAC (Da Riempimento o Avazamento da altro contenitore)
 ** Pianificata QTPA (Calcolata) = QTAO - QTAC (se QTAO>QTAC e FLG4=' '  contenitore non finito, abbiamo introdotto il saldo alla fase???)
 * _3_Giacenza
 ** Riempita :  QTCO (Calcolata) = GCAN (Giacenza Ante) + GCPS (Giacenza Post)
Ogni volta che si modifica la quantità ordinata o si annulla l'ordine viene eseguita la rifasatura della quantità contenitori dell'ordine. Se la quantità ordinata è minore della quantità contenitore viene aggiornata con la quantità contenitori.
