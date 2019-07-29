# Assunti
 - Un agente non può avere provvigioni con diverse periodicità, nè con diverse valute
 - Sulle fatture in valuta non vengono calcolati i contributi
 - Vengono gestite solo le periodicità mensili e trimestrali
 - Nel controllo bolle fatture viene dato per scontanto che ad ogni documento generato dalle provvigioni corrisponda una sola fattura e sia stata compilata correttamente l'anagrafica del percipiente
 - Il tipo provvigione associato alle note d'accredito deve avere il flag 8 valorizzato e un tipo documento diverso dalle fatture perchè i record delle note d'accredito costituiscono un documento a parte.

# Generazione Piano provvigioni/Documento attesa fattura
In base a quanto ottenuto dall'elaborazione delle liquidazioni è possibile generare un piano d'analisi delle provvigioni (memorizzato sul D5COSO) e un nuovo documento d'attesa della futura fattura dell'agente, che potranno poi essere utilizzati come strumenti di controllo in fase di contabilizzazione della stessa.

Il piano delle provvigioni può essere utilizzato come strumento d'analisi e monitoraggio del calcolo dei contributi degli agenti e viene scritto sul D5COSO, in base all'elemento della tabella D5O£P £PC (= Piano provvigioni), la cui costruzione non può essere libera, ma ripresa dallo standard. Il piano verrà scritto inizialmente con chiave Azienda / Tipo Documento / Numero Documento (se gestita la generazione dei documenti, altrimenti nelle ultime due chiavi verrà memorizzato **) con riferimento al periodo di liquidazione. Al momento della contabilizzazione del documento (se gestito), le ultime due chiavi verranno sostituite con il registro IVA della fattura e il numero protocollo della fattura (con l'anno), nella forma AAAA PPPPPPPPPP.
I dati memorizzati sul piano riguardano : 
 * le provvigioni liquidate (calcolate in base alla  liquidazione e agli anticipi già corrisposti);
 * l'imponibile e l'importo delle ritenute (calcolati in base all'anagrafica del percipiente e in considerazione di eventuali anticipi corrisposti);
 * l'enasarco (calcolato in base alla tabella V6T);
 * il FIRR (in base alla tabella V6U);
 * l'ISC (i cui calcoli si basano invece sulla tabella V6V).

Su ogni record verranno memorizzati i flag per specificare se il record è già stato contabilizzato, se riguarda una fattura d'anticipo e a quale tipo di periodicità fa riferimento.
Vengono storicizzati anche gli imponibili su cui calcolare Enasarco, FIRR e ISC perchè possono non coincidere con l'imponibile su cui calcolare le provvigioni (la tabella V5P del tipo provvigione permette di pilotare il comportamento).
È stata realizzata una stampa riepilogativa annuale della situazione agente, comprensiva di provvigioni e contributi.

Tutte queste considerazioni sono completamente a carico della /COPY £V5R, che si occupa di cancellare e riscrivere il piano ad ogni esecuzione.

Il piano delle provvigioni viene cancellato e ricreato ad ogni elaborazione e, anche se ogni documento d'attesa viene generato solo con l'elaborazione definitiva, il risultato finale è monitorizzabile anche in modalità provvisoria tramite la stampa di controllo.

Per attribuire una descrizione sensata alle righe del documento, è possibile utilizzare gli elementi della tabella *CNVP :  nella riga verrà forzata la descrizione dell'elemento della tabella, ottenuta costruendo il codice dell'elemento nel seguente modo : 
 * Il 1° carattere può assumere 3 valori : 
 ** "L" indica che la riga è relativa a una normale liquidazione delle provvigioni
 ** "A" indica che la riga è relativa a una liquidazione dovuta al corrispettivo di un anticipo
 ** "C" indica invece che la riga è relativa alla detrazione di anticipi già corrisposti in una normale liquidazione
 ** "K" indica invece che la riga è relativa alla detrazione di anticipi già corrisposti sotto forma di minimo garantito in una normale liquidazione
 * Il 2° carattere indica la periodicità della liquidazione
 * Il 3° e il 4° carattere indicano invece il mese di liquidazione

Anche per questa funzione la data dell'ultima elaborazione definitiva viene memorizzata in un elemento della tabella B£4, il cui codice è dato dall'unione della radice "*GC" + il codice di ogni periodicità.
Come per la liquidazione, è presente un pgm di riallineamento, che però si limita a rifasare solo il file V5PROV0F (nel caso siano stati generati dei documenti, questi dovranno essere cancellati a mano).

# Definizione e significato del tema del piano delle provvigioni
Il piano delle provvigioni si basa sull'elemento £PC della tabella D5O£P e deve essere compilato nel seguente modo : 
>Descrizione Livello  :   Piano Provvigioni
Codice 1             :   AZ
Parametro codice 1   : 
Codice 2             :   **
Parametro codice 2   : 
Codice 3             :   **
Parametro codice 3   : 
Suf.Pgm.Spec.D5CO_xx :   07
S/S indici (Se STD)  : 
Data/Periodo         :   P
Tipo periodo         :   P
Punti sep./decimali  :   22
Programma aggiust.   : 


I campi così gestibili sono definiti dal programma D5CO_07.
 * Fattura
 ** Provvigioni (l'importo della fattura corrisposta all'agente)
 ** Imponibile Ritenute (l'imponibile delle ritenute della fattura)
 ** Ritenute (l'importo delle ritenute)
 ** Anticipi (l'importo degli anticipi precedentemente corrisposti all'agente)

 * Enasarco
 ** Dovuto azienda (l'importo che l'azienda dovrà versare)
 ** Dovuto agente (l'importo che l'agente dovrà versare)
 ** Anticipo azienda (l'importo dell'eventuale anticipo che l'azienda deve versare nel caso non superi il minimale)
 ** Imponibile (l'importo imponibile per l'Enasarco)
 ** Contabilizzato (l'Enasarco è stato contabilizzato)

 * F.I.R.R.
 ** Accantonamento  (l'importo accantonato per il FIRR)
 ** Imponibile - (l'imponibile per FIRR)
 ** Contabilizzato (il FIRR è stato contabilizzato)

 * I.S.C.
 ** Accantonamento (l'importo accantonato per l'ISC)
 ** Imponibile (l'imponibile per ISC)
 ** Contabilizzato (l' ISC è stato contabilizzato)

 * Contabilizzazione (indica se il documento di riferimento è stato contabilizzato o meno)

 * Anticipo (indica se il documento di riferimento è una fattura d'anticipo)

 * Tipo periodo (indica se la fattura è stata corrisposta e il tipo di periodicità di riferimento)

# Stampa pro-forma documento d'attesa / Contributi
I documenti generati dalle provvigioni sono  stampabili tramite un apposito pgm di stampa che permette di integrare le righe del documento con i dati relativi ai contributi memorizzati sul piano.

E' inoltre prevista un'apposita stampa per l'analisi dei contributi.

# Contabilizzazione Documento attesa fattura
Al momento della contabilizzazione del documento d'attesa fattura verranno ripresi i dati dei contributi memorizzati sul piano, con la possibilità di apportare modifiche che verranno a loro volta riportate sul piano.

## Pgm esempio allineamento piano provvigioni
Sono stati implementati due sorgenti di esempio di pgm funizzati da utilizzare per allineare il piano provvigioni in caso di modiche di valore al relativo documento collegato (V5PR07A) e l'immisione del piano da una registrazione contabile slegata dalla gestione provvigioni (V5PR08A).

# Oggetti
## Pgm del flusso
V5PR03G/V  :  Guida
V5PR03C    :  Scansione in attesa di fatturazione/creazione Documenti
V5V5R0     :  Scrittura piano provvigioni
D5CO_07    :  Programma di gestione del tema £PC del D5COSO
V5PR13A    :  Guida allinamento file dopo esecuzione definitiva
V5PR13ACL  :  Selezione dei record da allineare
V5PR13B    :  Esecuzione allineamento del file
V5PR06A/V  :  Guida stampa documento pro-forma
V5PR06ACL  :  Selezione documenti da stampare
V5PR06S    :  Esecuzione stampa documento pro-forma
V5PR15A    :  Guida stampa contributi
V5PR15B    :  Esecuzione stampa contributi
G9CF60/V   :  Allineamento contributi in contabilizzazione (vecchio modo)
G9FA05_SM  :  Ripresa contributi in contabilizzazione (nuovo modo)
C5CF60C    :  Ripresa contributi in contabilizzazione (nuovo modo)
C5CF60K    :  Allineamento contributi in contabilizzazione (nuovo modo)

## Richiamo pgm Generazione piano provvigioni/Documento attesa
 :  : INI
 :  : CMD CALL V5PR03G
 :  : FIN
## Richiamo pgm Riallineamento collegamento fatturazione
 :  : INI
 :  : CMD CALL V5PR13A
 :  : FIN
## Richiamo pgm Stampa Pro-forma
 :  : INI
 :  : CMD CALL V5PR06A
 :  : FIN
## Richiamo pgm Stampa Contributi
 :  : INI
 :  : CMD CALL V5PR15A
 :  : FIN

## Visualizzazione sorgenti pgm di esempio
### Esempio allineamento da documento
 :  : INI
 :  : CMD CALL B£VED0 PARM('V5PR07A' '' '' '' '0')
 :  : FIN
### Esempio immissione da registrazione
 :  : INI
 :  : CMD CALL B£VED0 PARM('V5PR08A' '' '' '' '0')
 :  : FIN

## Tabelle
 :  : DEC T(ST) P() K(V58)
 :  : DEC T(ST) P() K(V5P)
 :  : DEC T(ST) P() K(AGE)
 :  : DEC T(ST) P() K(V6T)
 :  : DEC T(ST) P() K(V6U)
 :  : DEC T(ST) P() K(V6V)
 :  : DEC T(ST) P() K(V6Z)
 :  : DEC T(TA) P(B£4) K(*GCM)
 :  : DEC T(TA) P(B£4) K(*GCT)
 :  : DEC T(TA) P(D5O£P) K(£PC)
 :  : DEC T(TA) P(D5S) K(TAAGE)

## Stampe riepilogative
Sono disponibili 2 stampe della situazione contributiva degli agenti, entrambe lanciabili dallo stesso programma V5PR15A scegliendo la tipologia di output : 
 * la prima è la riepilogativa di tutti gli agenti e mostra agente per agente quanto è stato liquidato nel periodo e quanto è stato versato agli enti Enasarco, FIRR e ISC;
 * la seconda è il dettaglio del singolo agente e mostra fattura per fattura le provvigioni maturate e i versamenti contributivi, presentando, alla fine, un riepilogo trimestrale di questi dati.

## Programma di stampa
 :  : INI
 :  : CMD CALL V5PR15A
 :  : FIN
