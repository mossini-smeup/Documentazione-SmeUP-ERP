## Contenuto
Consigli di pianificazione.
E' rigenerato (totalmente o selettivamente) nel processo di pianificazione.
Per ogni articolo trattato contiene : 
- un record per ogni elemento ritornato dalla scansione disponibilità col gruppo fonti di pianificazione (fabbisogni e coperture in corso) :  scritto all'inizio della pianificazione ed eventualmente aggiornato, se è una copertura, con suggerimenti di variazione o annullamento.
- un record per ogni ordine pianificato (copertura pianificata), scritto nel processo di pianificazione.
- un record per ogni impegno pianificato (fabbisogno pianificato), scritto nel processo di pianificazione.
- un record per ogni suggerimento pianificato di eccedenza, scritto nel processo di pianificazione.

## Codice Oggetto (in TA/*CNTT)
 'M5'                               £FUNT1

## Chiave primaria
H§CDMG  -   H§NORI                  £FUNK1
che formano il codice dell'oggetto nel seguente modo : 
Posizione  1 -  3  :  Codice magazzino
Posizione  7 - 15  :  Riferimento origine

## Altri condizionamenti facoltativi in ricerca
N.A.

## Ulteriore chiave primaria
H§NORI.
Storicamente il riferimento origine era univoco per plant. Nella realizzazione dell'MRP multiplant è diventato univoco in assoluto, quindi ha assunto in pratica la valenza di IDOJ.

## Tabella guida
Alcuni campi di questo archivio sonmo tipizzati dalla tabella M51 Elemento ** e M5B (scenario) : 
 :  : DEC T(ST) K(M51)
 :  : DEC T(ST) K(M5B)
Alcuni comportamenti sono assunti dalla tabella M5A (politiche di pianificazione) : 
 :  : DEC T(ST) K(M5A)

## Autorizzazioni
E' presente la classe di autorizzazione 'M5CMRP' per consentire il rilascio selettivo degli ordini pianificati, la cui funzione + il codice della fonte del consiglio.

## Note strutturate (Tabella NSC)
N.A.

## Parametri (Tabella C£E)
N.A.

## Flussi (Tabella B£H)
N.A.

## Costruzione automatica campi (tabella B£C)
N.A.

## Presenza monitor - visualizzatore
N.A.

## Programmi di controllo
Dopo la scrittura di un consiglio (ordine pianificato e modifica esistente) viene lanciato un programma di aggiustamento con suffisso impostato in M5A, e con risalita a M51.
Dopo la scrittura di un record di fonte rilasciate, viene lanciato un programma di aggiustamento con suffisso definito in tabella M51.

## /COPY
Interfaccia consigli di pianificazione
 :  : DEC T(MB) P(QILEGEN) K(£IM5)
Interfaccia dati di pianificazione
 :  : DEC T(MB) P(QILEGEN) K(£M5A)
Interfaccia esecuzione suggerimenti
 :  : DEC T(MB) P(QILEGEN) K(£M5E)
Interfaccia navigazione pianificazione
 :  : DEC T(MB) P(QILEGEN) K(£M5N)
Esecuzione pianificazione
 :  : DEC T(MB) P(QILEGEN) K(£M5R)
Completamento consigli pianificazione
 :  : DEC T(MB) P(QILEGEN) K(£M5S)
Interfaccia scrittura impegni pianificati
 :  : DEC T(MB) P(QILEGEN) K(£M5W)

## Gruppi flag
N.A.

## Workflow e popup
N.A.

## Note particolari
N.A.

## CONTENUTO DEI CAMPI

 :  : FLD H§SCEN **Scenario**
E' una partizione dell'archivio, ciascuna di esse rappresenta una singola pianificazione, in modo tale che possono essere presenti (e confrontate) diverse pianificazioni.
L'attivazione di più scenari si imposta in M51. Nello scenario, in tabella M5B, sono presenti impostazioni aggiuntive o sostitutive rispetto a quelle di M51.
Se gli scenari non sono attivi, viene assunto come unico scenario '**', che quindi deve essere sempre presente.

 :  : FLD H§STAT **Stato**
Viene assunto dal livello impostato

 :  : FLD H§LIVE **Livello**
In scrittura del record si assume il livello '2'.
In annullamento logico dei suggerimenti (per escluderne alcuni da una applicazione di massa) viene portato a '9'.
Viene portato a '8'
- se il consiglio è applicato totalmente (per una quantità  non inferiore a quella del suggerimento oppure se saldato forzatamente)
- per eliminare gli impegni pianificati se trattati in un gruppo fonti a bilanciamento (riferirsi al campo di M5A per una spiegazione più ampia)

 :  : FLD H§NORI **N.Record origine**
E' un riferimento numerico univoco di ogni record di consigli, generato automaticamente all'atto della scrittura, senza basarsi su alcun numeratore.
NB :  **NON E'** il numero di record relativo nell'archivio.

 :  : FLD H§LIMI **Livello minimo**
Viene assunto dal valore presente nell'archivio dati tecnici articolo (BRARDT), usando , in risalita, il tipo distinta impostato in M5B, M51, oppure fissa 'ART'.

 :  : FLD H§CDMG **Codice magazzino**
Il contenuto dipende dal modo di pianificazione multimagazzino impostato in M51.
Sulle fonti rilasciate : 
- In caso di pianificazione completa o singola, viene ripreso il valore ritornato dalla scansione disponibilità (nella pianificazione singola il gruppo fonti può contenere un solo plant).
- In caso di pianificazione cumulata, viene forzato il primo plant del gruppo fonti. La scansione viene comunque eseguita con tutti i magazzini del gruppo fonti. Il magazzino reale della fonte, se diverso dal primo, viene memorizzato nel campo magazzino associato.
Sulle fonti pianificate viene assunto il valore in corso di pianificazione, ad eccezione degli impegni pianificati di trasferimento, nei quali vengono invertiti i campi di magazzino e di magazzino associato dell'ordine di trasferimento.

 :  : FLD H§ARTI **Codice articolo**
E' l'articolo intestatario del consiglio. Forma, insieme con lo scenario, il magazzino e l'oggetto di rottura (eventualmente vuoto) l'unità su cui si effettua la pianificazione.

 :  : FLD H§ESMO **Esponente di modifica**
Nelle fonti rilasciate viene assunto dal valore presente nell'archivio originale, ritornato dalla scansione disponibilità.
Negli ordini pianificati e nei suggerimenti di eccedenza, se l'MRP è a rottura di esponente di modifica e l'articolo è gestito a rottura, viene ripreso dall'oggetto di rottura che si sta pianificando.
Negli impegni pianificati, se l'assieme (dell'ordine pianificato) è gestito a rottura di esponente di modifica, viene calcolata la data di inizio validità dell'esponente dell'ordine pianificato, da cui si ricava l'esponente dell'articolo dell'impegno valido a questa data.
Se invece l'assieme non è gestito a rottura di esponente di modifica, l'esponente di modifica del componente viene calcolato in base al valore impostato in tabella M5A dell'assieme, nel campo "Esponente di modifica dei componenti".

 :  : FLD H§CROT **Codice di rottura**
Viene riempito per gli articoli gestiti a rottura
- Nelle fonti rilasciate e negli impegni pianificati viene assunto dal corrispondente oggetto di rottura (commessa, configurazione, ecc...) presente nello stesso record.
- Negli ordini pianificati e nei suggerimenti di eccedenza viene assunto dall'oggetto di rottura che si sta pianificando.

 :  : FLD H§OGRF **Oggetto riferimento**
Dipende da quanto impostato nella tabella scenario (M5B)
Può essere un OAV dell'articolo o un elemento di tabella di classificazione dell'articolo (Tipo articolo, ecc..). La prima modalità, più generale, comprende la seconda.

 :  : FLD H§TIEN **Tipo ente**
Riferirsi al campo codice ente, essendo trattato in coppia con quest'ultimo.

 :  : FLD H§COEN **Codice ente**
Nelle fonti rilasciate viene assunto dal valore presente nell'archivio originale, ritornato dalla scansione disponibilità.
Negli ordini pianificati viene determinato in base a quanto impostato in tabella M5A nel modo di assegnazione ente.
Negli impegni pianificati viene mantenuto il valore dell'ordine pianificato.

 :  : FLD H§COMM **Commessa**
Nelle fonti rilasciate viene assunto dal valore presente nell'archivio originale, ritornato dalla scansione disponibilità.
Negli ordini pianificati e nei suggerimenti di eccedenza, se l'MRP è a rottura di commessa e l'articolo è gestito a rottura, viene ripreso dall'oggetto di rottura che si sta pianificando.
Negli impegni pianificati viene mantenuto il valore dell'ordine pianificato.

 :  : FLD H§CONF **Configurazione**
Nelle fonti rilasciate viene assunto dal valore presente nell'archivio originale, ritornato dalla scansione disponibilità.
Negli ordini pianificati e nei suggerimenti di eccedenza, se l'MRP è a rottura di configurazione e l'articolo è gestito a rottura, viene ripreso dall'oggetto di rottura che si sta pianificando.
Negli impegni pianificati viene mantenuto il valore dell'ordine pianificato, eventualmente 'smagrito' nell'exit di scrittura del consiglio.

 :  : FLD H§FOPF **Fonte presente/futura**
Nelle fonti rilasciate viene assunto il valore ritornato dalla scansione della disponibilità.
Negli ordini pianificati e negli impegni pianificati viene assunto 'F'
Nei suggerimenti di eccedenza viene assunto 'E' se eccedenza presente e 'F' se eccedenza futura.

 :  : FLD H§OGFO **Origine fonte**
Nelle fonti rilasciate viene assunto il valore ritornato dalla scansione della disponibilità.
Negli ordini pianificati e negli impegni pianificati viene assunto il valore contenuto nella loro fonte (tabella M5F).
Nei suggerimenti di eccedenza viene assunto fisso 'QE'.

 :  : FLD H§ORFO **Ordinamento fonte**
Nelle fonti rilasciate viene assunto il valore ritornato dalla scansione della disponibilità.
Negl ordini pianificati e negli impegni pianificati viene assunto il valore contenuto nella loro fonte (tabella M5F).
Nei suggerimenti di eccedenza viene assunto fisso '9'.

 :  : FLD H§SGFO **Segno fonte**
Nelle fonti rilasciate, se nella disponibilità è valorizzata la quantità entrata : 
- se è positiva si assume '+'
- se è negativa (può essere soltanto una giacenza negativa che viene considerata un fabbisogno) si assume '-'.
se invece nella disponibilità è valorizzata la quantità uscita : 
- se è positiva si assume '-'
- se è negativa (può essere soltanto unrecupero che viene considerato una copertura) si assume '+'.
Negl ordini pianificati e negli impegni pianificati viene assunto il valore contenuto nella loro fonte (tabella M5F).
Nei suggerimenti di eccedenza viene assunto fisso '-'.

 :  : FLD H§COFO **Codice fonte**
Nelle fonti rilasciate viene assunto il valore ritornato dalla scansione della disponibilità.
Negli ordini pianificati e negli impegni pianificati viene assunto, rispttivamente, il valore della fonte di pianificazione e di impegno presente nella tabella della politica.
Nei suggerimenti di eccedenza viene assunto il codice di eccedenza presente o futura impostato nella tabella della politica.

 :  : FLD H§QTFO **Quantità fonte**
Nelle fonti rilasciate, si assume il valore ritornato dalla scansione della disponibilità, con le seguenti regole : 
- se è valorizzata la quantità entrata, se positiva si assume tal quale, se negativa si cambia di segno.
- se è valorizzata la quantità uscita, se positiva si assume tal quale, se negativa si cambia di segno.
Questo accorgimento, collegato con l'analoga impostazione del segno fonte, fa sì che la quantità della fonte sia sempre positiva, e venga considerata una copertura se il segno fonte è '+', e un fabbisogno se il segno della fonte è '-'.
Negli ordini pianificati è la quantità necessaria alla copertura dei fabbisogni all'interno del periodo di ragguppamento, prima di eseguire l'eventuale arrotondamento al lotto. Nel caso di pianificazione mista (ad esempio una % del fabbisogno di produzione, un'altra % (complemento a 100) di conto lavoro, oppure di assegnazione a più di un fornitore, questo campo è valorizzato solo per il primo ordine, con la quantità totale richiesta.
Negli impegni pianificati di produzione e conto lavoro, è la quantità ritornata dalla scansione della distinta base dell'assieme, lanciata con la quantità del suggerimento.
Negli impegni pianificati di trasferimento è pari alla quantità del suggerimento dell'ordine pianificato di trasferimento.
Nei suggerimenti di eccedenza è lasciata a zero.

 :  : FLD H§DTFO **Data fonte**
Nelle fonti rilasciate viene assunto il valore ritornato dalla scansione della disponibilità.
Negli ordini pianificati è la data a cui si verifica il primo fabbisogno che essi coprono.
Negi impegni pianificati è la data fine pianificata dell'assieme, arretrata dei tempi di approvvigionamento, eventualmente sostituiti da quello di rettifica del legame.
Nelle fonti di eccedenza è la data a cui essa si verifica (0 se è eccedenza presente).

 :  : FLD H§COD1 **Parametro 1 fonte**
Nelle fonti rilasciate contiene il paratetro della fonte (£M5DFP) ritornato dalla scansione della disponibilità, che riporta un'informazione dipendente dall'origine della fonte.
Negli ordini pianificati contiene (allineata a destra) la politica originale. Se non è attiva la sovrapposizione con i dati di pianificazione per riferimento, lo stesso valore viene riportato allineato a sinistra. In caso contrario, viene riportata la politica ritornata in base al riferimento (da impostazione in M51).
Negli impegni pianificati contiene il codice articolo dell'assieme.

 :  : FLD H§COD2 **Parametro 2 fonte**
Nelle fonti rilasciate di giacenza riporta l'eventuale risorsa  in cui è presente (campo necessario per la produzione a PDC).
Negli ordini pianficati, se sono frutto di suddivisione (ad esempio per differenziazione tra produzione e conto lavoro, oppure assegnazione a più di un fornitore), sugli ordini successivi è riportato il N.ro record origine del primo.
Negli impegni pianificati riporta il N.ro record origine dell'assieme a cui appartengono.
Nelle giacenze è la risorsa (CDL), se presente tra le chiavi di giacenza  (campo necessario per la PDC).

 :  : FLD H§COD3 **Parametro 3 fonte**
Nelle fonti rilasciate di giacenza riporta l'eventuale contenitore in cui è presente (campo necessario per la produzione a PDC).
Negli ordini pianificati riporta il N.ro record origine del primo fabbisogno che copre (solo sul primo ordine di un gruppo).
Negli impegni pianificati riporta il N.ro record origine del primo fabbisogno che il loro ordine pianificato copre.
Nei suggerimenti di quantità eccedente riporta il N.ro record origine della prima copertura che contiene quantità eccedente.
Nelle giacenze è il contenitore, se presente tra le chiavi di giacenza  (campo necessario per la PDC).

 :  : FLD H§COD4 **Parametro 4 fonte**
Campo attualmente non gestito dall'applicazione.

 :  : FLD H§COD5 **Parametro 5 fonte**
Campo attualmente non gestito dall'applicazione.

 :  : FLD H§COD6 **Parametro 6 fonte**
Campo attualmente non gestito dall'applicazione.

 :  : FLD H§COD7 **Parametro 7 fonte**
Campo attualmente non gestito dall'applicazione.

 :  : FLD H§COD8 **Parametro 8 fonte**
Campo attualmente non gestito dall'applicazione.

 :  : FLD H§COD9 **Parametro 9 fonte**
Campo attualmente non gestito dall'applicazione.

 :  : FLD H§CODA **Parametro A fonte**
Campo attualmente non gestito dall'applicazione.

 :  : FLD H§TISU **Tipo suggerimento**
Nelle fonti rilasciate è il suggerimento (opzionale) 'AE'.
Nelle fonti pianificate vale 'PN'.

 :  : FLD H§COSU **Codice suggerimento**
Nelle fonti rilasciate vale 'MO' se si suggerisce una variazione di data e/o una riduzione di quantità, vale 'EL' se ne si suggerisce l'eliminazione.
Nelle fonti pianificate definisce il tipo ordine ('PR', 'LV', 'AQ', 'TR'), vale invece 'EL' se è un suggerimento di eccedenza, 'TR' se è una fonte trascurata.

 :  : FLD H§QTSU **Quantità suggerimento**
Nelle fonti rilasciate è presente (opzionalmente) se il tipo e il codice del suggerimento sono, rispettivamente, 'AE' e 'MO', e rappresenta la nuova quantità (minore dell'originale) a cui si suggerisce di portare la fonte, tenendo conto della lottizzazione (lotto minimo e multiplo).
Negli ordini pianificati è la quantità da ordinare (partendo dalla data fonte e applicando la lottizzazione). In caso di pianificazione mista è la quantità di ogni singolo ordine.
Negli impegni pianificati è lasciata a zero.
Nei suggerimenti di eccedenza e di fonte trascurata rappresenta la quantità relativa a questi suggerimenti.

 :  : FLD H§DTSU **Data suggerimento**
Nelle fonti rilasciate è presente (opzionalmente) se il tipo e il codice del suggerimento sono, rispettivamente, 'AE' e 'MO', e rappresenta la data a cui  si suggerisce di portare la fonte.
Negli ordini pianificati è la data a cui si suggerisce di emettere il suggerimento, ed è calcolata arretrando dei tempi di approvvigionamento la data fonte.
Negli impegni pianificati è lasciata a zero.

 :  : FLD H§PRSU **Parametro suggerimento**
Nelle fonti rilasciate viene assunto il valore ritornato dalla scansione della disponibilità.
Negli ordini pianificati e negli impegni pianificati viene assunto il valore contenuto nella loro fonte (tabella M5F).
Se presente, rappresenta la modalità (programma e parametri di condizionamento) con cui si applica il suggerimento.

 :  : FLD H§DTFP **Data fine pianificata**
Negli ordini pianificati si ottiene avanzando la data fonte del tempo di approvvigionamento di rettifica dell'articolo.

 :  : FLD H§CDMA **Magazzino associato**
Nel caso di pianficazione cumulata, viene riportato, nelle fonti rilasciate, il plant effettivo se diverso dal primo (quello in cui si cumula la pianificazione).
Nel caso di pianificazione completa, per gli ordini rilasciati e gli impegni rilascati di trasferimento, si riporta il plant collegato (risperttivamente di partenza e d'arrivo).
Analogamente, per gli ordini pianificati di trasferimento e gli impegni pianificati di trasferimento si riporta il plant collegato (anche in questo caso risperttivamente di partenza e d'arrivo).

 :  : FLD H§TPRI **Tipo oggetto rilascio**
Per gli ordini pianificati è il tipo oggetto del rilascio (OR, DR).
Viene riempito, insieme all'oggetto (tipo/numero/numero riga) in due momenti diversi : 
- in fase di pianificazione, se l'assegnazione dell'ente ritorna anche il contratto a cui deve riferirsi il rilascio (può essere soltanto di tipo 'DR')
- in fase di rilascio, viene riempito l'oggetto effettivo (sia OR sia DR) che è stato generato dal suggerimento. Qualora si effettuino più rilasci parziali per lo stesso consiglio, prima di rieseguire l'MRP, il valore successivo copre il precedente. Inoltre, in questo caso, il contratto scritto nella fase di pianficazione, viene utilizzato se previsto nel parametro suggerimento (modo di rilascio definito in tabella M5V), e successivamente viene sovrascritto dal documento generato.

 :  : FLD H§TTRI **Tipo rilascio**
E' il tipo oggetto (riempitio se oggetto 'DR' o 'IM') di rilascio. Riferirsi alla documentazione del "Tipo oggetto rilascio" per un'esposizione completa se fonte pianificata.
Se fonte rilasciata è il tipo del documento.

 :  : FLD H§NURI **Numero rilascio**
E' l'oggetto di rilascio :  riferirsi alla documentazione del "Tipo oggetto rilascio" per un'esposizione completa se fonte pianificata.
Se fonte rilasciata è il codice dell'ordine/documento (in base all'origine fonte)

 :  : FLD H§RIRI **Riga rilascio**
E' la riga di rilascio (riempita se se oggetto 'DR') di rilascio. Riferirsi alla documentazione del "Tipo oggetto rilascio" per un'esposizione completase fonte pianificata.
Se fonte rilasciata è il numero di riga del documento.

 :  : FLD H§QTRI **Quantità rilasciata**
Per le fonti rilasciate di copertura è la quantità totale (non la residua), ritornata dalla scansione della disponibilità. Viene utilizzata per calcolare correttamente i suggerimenti di riduzione secondo il lotto.
Per le fonti pianificate di copertura viene riempita, all'atto del rilascio, con la quantità effettivamente rilasciata che, a meno di forzature manuali, coincide con la quantità del suggerimento.

 :  : FLD H§DT01 **Data libera 1**
Campo a disposizione utente

 :  : FLD H§DT02 **Data libera 2**
Campo a disposizione utente

 :  : FLD H§DT03 **Data libera 3**
Campo a disposizione utente

 :  : FLD H§DT04 **Data libera 4**
Campo a disposizione utente

 :  : FLD H§DT05 **Data libera 5**
Campo a disposizione utente

 :  : FLD H§QT01 **Quantità libera 1**
Campo a disposizione utente

 :  : FLD H§QT02 **Quantità libera 2**
Campo a disposizione utente

 :  : FLD H§QT03 **Quantità libera 3**
Campo a disposizione utente

 :  : FLD H§QT04 **Quantità libera 4**
Campo a disposizione utente

 :  : FLD H§QT05 **Quantità libera 5**
Campo a disposizione utente



