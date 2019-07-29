_2_ C5UT63A _B_ Controllo quadrature Master C5
Programma per il controllo della consistenza dei database contabili.
L'esecuzione è interattiva e presente una maschera di richiesta parametri. E' però possibile prevedere un'esecuzione batch (anche schedulata), richiamando con una CALL il pgm C5UT63B, passando i medesimi parametri che si vedono nel richiamo interattivo del C5UT63B.

 :  : INI . Sorgente C5UT63A
 :  : CMD CALL B£VED0 PARM('C5UT63A' '' '' '' '0')
 :  : FIN
 :  : INI . Sorgente C5UT63B
 :  : CMD CALL B£VED0 PARM('C5UT63B' '' '' '' '0')
 :  : FIN

_2_ C5UT01A _B_ Cancellazione registrazioni per data
Programma per la cancellazione di massa delle registrazioni contabili. Il richieamo deve essere
eseguito passando i seguenti parametri : 
FUNZ (funzione)      = 'DEL' Cancellazione
METO (metodo)        = 'DAT' Per data
PAR1 (data Iniziale) = 'AAAAMMGG' data iniziale di cancellazione nel formato Anno-Mese-Giorno
PAR2 (data Fianle)   = 'AAAAMMGG' data Finale   di cancellazione nel formato Anno-Mese-Giorno
AZIE (Azienda)       = 'AZ' Codice azienda per cui effettuare la cancellazione
 :  : INI . Sorgente C5UT01A
 :  : CMD CALL B£VED0 PARM('C5UT01A' '' '' '' '0')
 :  : FIN
 :  : INI . Sorgente C5UT01B
 :  : CMD CALL B£VED0 PARM('C5UT01B' '' '' '' '0')
 :  : FIN
### C5UT02A Rifasatura flag 5 testata (intercompany) - Esecuzione di massa
Programma per l'allinemaneto del flag 5 della testata. Vengono lette TUTTE le registrazioni che
hanno come oggetto di testata un ente e quindi agganciando l'anagrafica viene aggiornato il
Flag 5 in funzione del flag 1 del BRENTI0F.
Il prgogramma C5UT02A lancia poi il programma C5UT02B che esegue la rifasatura selle righe, sulle
rate e sull'analitica.
 :  : INI . Sorgente C5UT02A
 :  : CMD CALL B£VED0 PARM('C5UT02A' '' '' '' '0')
 :  : FIN
 :  : INI . Sorgente C5UT02B
 :  : CMD CALL B£VED0 PARM('C5UT02B' '' '' '' '0')
 :  : FIN
 :  : INI . Esecuzione
 :  : CMD CALL C5UT02A
 :  : FIN

### C5UT03 Creazione rate da riga reg. :  Lancio batch
Impostazione della LDA per il lancio del C5UT03A. Permette di schedulare il lancio della creazione
delle rate da riga registrazione.
 :  : INI . Sorgente
 :  : CMD CALL B£VED0 PARM('C5UT03' '' '' '' '0')
 :  : FIN
 :  : INI . Esecuzione
 :  : CMD CALL C5UT03
 :  : FIN

### C5UT03A Creazione rate da riga reg. :  Lancio con Rich.Parametri
 :  : INI . Sorgente
 :  : CMD CALL B£VED0 PARM('C5UT03A' '' '' '' '0')
 :  : FIN
 :  : INI . Richesta parametri
 :  : CMD CALL C5UT03A
 :  : FIN

### C5UT03G Aggiornamento documento su Reg.Convertite
Vedere documentazione del programma all'interno del sorgente.
 :  : INI . Sorgente
 :  : CMD CALL B£VED0 PARM('C5UT03G' '' '' '' '0')
 :  : FIN
 :  : INI . Esecuzione
 :  : CMD CALL C5UT03G
 :  : FIN

### C5UT05A Creazione registrazioni arrotondamento
 :  : INI . Sorgente
 :  : CMD CALL B£VED0 PARM('C5UT05A' '' '' '' '0')
 :  : FIN
 :  : INI . Esecuzione
 :  : CMD CALL C5UT05A
 :  : FIN

### C5UTX05A Attivazione di massa simulate :  Lancio con Rich.Parametri
Il programma rende attive solo le registrazioni derivanti da un tipo di registrzione di pagamento
di gestione titoli (Tabella C5D, campo T$C5DA='06'). Il test nel prgoramma viene fatto sul campo
della rata S5NUTI - numero titolo.
 :  : INI . Sorgente C5UTX05A
 :  : CMD CALL B£VED0 PARM('C5UTX05A' '' '' '' '0')
 :  : FIN
 :  : INI . Sorgente C5UTX05B
 :  : CMD CALL B£VED0 PARM('C5UTX05B' '' '' '' '0')
 :  : FIN
 :  : INI . Richesta parametri
 :  : CMD CALL C5UTX05A
 :  : FIN

### C5UT06A Controllo fasatura importi pagati sulle rate
Questo pgm svolge tre tipologie di controllo : 
 - Importi / Rate :  controlla la congruenza fra gli importi memorizzati sulle rate di dovuto e    gli importi calcolati leggendo le effettive rate di pagato. In esecuzione riallinea gli importi    memorizzati.
 - Importi di Valuta / Valuta di conto. Controlla le rate chiuse in valuta, ma aperte in valuta    di conto. Funziona solo in stampa e non in esecuzione.
 - Rate di pagato non assegnate :  controlla le rate di pagato assegnate ad una rata di dovuto    inesistente. In esecuzione prova a controllare se esistono rate aperte dello stesso importo per    la stessa partita :  se ne trova, associa il pagato a tale rata, altrimenti trasforma la rata di    pagato in un anticipo.
 :  : INI . Sorgente C5UT06A
 :  : CMD CALL B£VED0 PARM('C5UT06A' '' '' '' '0')
 :  : FIN
 :  : INI . Sorgente C5UT06B
 :  : CMD CALL B£VED0 PARM('C5UT06B' '' '' '' '0')
 :  : FIN
 :  : INI . Lancio
 :  : CMD CALL C5UT06A
 :  : FIN

### C5UT0601 Stampa controllo incongruenza importo pagato su rate/rate di pagamento effettive
 :  : INI . Sorgente
 :  : CMD CALL B£VED0 PARM('C5UT0601' '' '' '' '0')
 :  : FIN
 :  : INI . Esecuzione
 :  : CMD CALL C5UT0601
 :  : FIN

### C5UT0602 Stampa controllo incongruenza importo riga/sommatoria delle rate
 :  : INI . Sorgente
 :  : CMD CALL B£VED0 PARM('C5UT0602' '' '' '' '0')
 :  : FIN
 :  : INI . Esecuzione
 :  : CMD CALL C5UT0602
 :  : FIN

### C5UT10A Creazione analitiche mancanti/Cancellazione analitiche di conti non di analitica
 :  : INI . Sorgente
 :  : CMD CALL B£VED0 PARM('C5UT10A' '' '' '' '0')
 :  : FIN
 :  : INI . Richiesta parametri
 :  : CMD CALL C5UT10A
 :  : FIN

### C5UT13A Contabilizzazione di massa degli effetti
Vedere documentazione del programma all'interno del sorgente per secifiche di lancio.
E' possibile lanciare in batch il programma in coda alla contabilizzazione fatture
attive inserendo il richiamo al C5UT13A nel PGM di post contabilizzazione V5FA08_SM
Il programma è presente nel menu della contabilità alla sezione "Incassi/Pagamenti", azione 103120.
 :  : INI . Sorgente
 :  : CMD CALL B£VED0 PARM('C5UT13A' '' '' '' '0')
 :  : FIN
 :  : INI . Esecuzione
 :  : CMD CALL C5UT13A
 :  : FIN

### C5UT15B Controllo congruenza logica delle rate
Viene prodotta una stampa che evidenzia la presenza di rate logicamente non corrette con
l'inidcazione dei campi che non sono inseriti in modo congruo.
 :  : INI . Sorgente
 :  : CMD CALL B£VED0 PARM('C5UT15B' '' '' '' '0')
 :  : FIN
 :  : INI . Esecuzione
 :  : CMD CALL C5UT15B
 :  : FIN

### C5UT16B Ricalcolo di massa degli importi pagati
 :  : INI . Sorgente
 :  : CMD CALL B£VED0 PARM('C5UT16B' '' '' '' '0')
 :  : FIN
 :  : INI . Esecuzione
 :  : CMD CALL C5UT16B
 :  : FIN

### C5UT18 Analisi insoluti per agente
Analisi delle rate di pagato inserite in pratica che hanno esito (flag 19 diverso da *blanks)
con totale per agente
 :  : INI . Sorgente
 :  : CMD CALL B£VED0 PARM('C5UT18' '' '' '' '0')
 :  : FIN
 :  : INI . Richiesta parametri
 :  : CMD CALL C5UT18
 :  : FIN

### C5UT19A Rifasatura flag intercompany - con possibilità di filtri
Rifasatura del flag intercompany con possibilità di indicare dei parametri di lancio
 :  : INI . Sorgente C5UT19A
 :  : CMD CALL B£VED0 PARM('C5UT19A' '' '' '' '0')
 :  : FIN
 :  : INI . Sorgente C5UT19B
 :  : CMD CALL B£VED0 PARM('C5UT19B' '' '' '' '0')
 :  : FIN
 :  : INI . Richiesta parametri
 :  : CMD CALL C5UT19A
 :  : FIN

### C5IN00A/C5IN00B Rifasatura Ente intercompany - Gestione infromazione ente £33
Dopo l'introduzione della gestione dell'informazione £33, ovvero dell'indicazione per ciascun
ente Intercompany della società intercompany assegnata (Tabella C5H), è necessario riportare
in modo corretto sui file contabili la nuova informazione, nei campi SOCO e SOCI.
I programmi di seguito evidenziati eseguono questo aggiornamento.
Sono anche richiamabili dal menù della contabilità, alla sezione "Movimenti Intercompany",
azione 106015.
 :  : INI . Sorgente C5IN00A
 :  : CMD CALL B£VED0 PARM('C5IN00A' '' '' '' '0')
 :  : FIN
 :  : INI . Sorgente C5IN00B
 :  : CMD CALL B£VED0 PARM('C5IN00B' '' '' '' '0')
 :  : FIN
 :  : INI . Richiesta parametri
 :  : CMD CALL C5IN00A
 :  : FIN

### C5UT21A Ricodifica dei conti contabili
Attraverso questo programma è possibile fare una sostituzione di massa dei conti contabili.
Questa attività si basa sull'utilizzo degli alias per individuare il nuovo codice da utilizzare
e sostituire oppure cancellare.
Esiste anche la possibilità di gestire un programma di Exit C5UT21B_X
Vedere documentazione del programma all'interno del sorgente per secifiche di lancio.
 :  : INI . Sorgente C5UT21A
 :  : CMD CALL B£VED0 PARM('C5UT21A' '' '' '' '0')
 :  : FIN
 :  : INI . Sorgente C5UT21B
 :  : CMD CALL B£VED0 PARM('C5UT21B' '' '' '' '0')
 :  : FIN
 :  : INI . Richiesta parametri
 :  : CMD CALL C5UT21A
 :  : FIN

### C5UT22A Differenza Conto/Lista Allegati Bilancio
Analisi dei saldi dei singoli enti attraverso la £C5F (routine per calcolo saldo conto)
mettendo a confronto il saldo dell'ente (inizialmene senza indicare nessun conto) e il saldo
dell'ente indicando il conto contabile memorizzato sull'anagrafica ente.
Questo cotnrollo evidenzia una possibile differenza dovuta alla presenza di registrazioni
per uno stesso ente con conti contabili differenti.
 :  : INI . Sorgente C5UT22A
 :  : CMD CALL B£VED0 PARM('C5UT22A' '' '' '' '0')
 :  : FIN
 :  : INI . Sorgente C5UT22B
 :  : CMD CALL B£VED0 PARM('C5UT22B' '' '' '' '0')
 :  : FIN
 :  : INI . Richiesta parametri
 :  : CMD CALL C5UT22A
 :  : FIN

### C5UT24A Eliminazione esercizi
Eliminare gli esercizi contabili consiste nel cancellare le registrazioni contabili di un determina-
to esercizio. Il programma opera in due fasi distinte : 
RENDERE ELIMINABILE ESERCIZIO
La prima verifica se una registrazione è cancellabile attraverso una serie di controlli.
Innanzittutto viene verificato che la riga sia di conto contabile, ed in tal caso viene posto il
flag 40 al valore 'D' e la riga verrà successivamente eliminata.
Se invece la riga coinvolge un soggetto, è necessario verificare che tutte le rate di quella riga
siano chiuse. Se si verifica questa condizione anche questa riga viene cosniderata cancellabile
ed il flag 40 valorizzato a 'D'. Se invece le rate nonsono chiuse totalmente, bisogno solo modi-
ficare la registrazione ed in questo caso il falg 40 verrebbe calorizzato ad 'U'.
In funzione poi della condizione delle righe una registrazione potrebbe essere interamente cancella-
ta ed allora il programma valorizzerà anche il flag 40 della testata a 'D', altrimenti lo stesso
verrà valorizzato a 'U'.
Verrà quindi aggiornato lo stato dell'esercizio ponendolo in 'L' eliminabile.
ELIMINABRE ESERCIZIO
La fase di cancellazione provvederà a cancellare o ad aggiornare le righe di registrazione in
funzione del valore attribuito al flag 40 e provvederà ad agire anche sui file collegati (nello
specifico sulle rate, sulla contabilità analitca, sulle ritenute).
Verrà quindi aggiornato lo stato dell'esercizio ponendolo in 'E' eliminato fisicamente.
_1_ NOTA :  NON VENGONO EFFETTUATI SALVATAGGI IN FILE DI APPOGGIO, QUINDI PROVVEDERE PREVENTIVAMENTE.
 :  : INI . Sorgente C5UT24A
 :  : CMD CALL B£VED0 PARM('C5UT24A' '' '' '' '0')
 :  : FIN
 :  : INI . Sorgente C5UT24B
 :  : CMD CALL B£VED0 PARM('C5UT24B' '' '' '' '0')
 :  : FIN
 :  : INI . Richiesta parametri
 :  : CMD CALL C5UT24A
 :  : FIN

### C5UT26A Stampa diff.mastro conto/Allegati bilancio
 :  : INI . Sorgente C5UT26A
 :  : CMD CALL B£VED0 PARM('C5UT26A' '' '' '' '0')
 :  : FIN
 :  : INI . Sorgente C5UT26B
 :  : CMD CALL B£VED0 PARM('C5UT26B' '' '' '' '0')
 :  : FIN
 :  : INI . Richiesta parametri
 :  : CMD CALL C5UT26A
 :  : FIN

### C5UT27A Controllo quadratura giornaliera righe/rate
 :  : INI . Sorgente C5UT27A
 :  : CMD CALL B£VED0 PARM('C5UT27A' '' '' '' '0')
 :  : FIN
 :  : INI . Sorgente C5UT27B
 :  : CMD CALL B£VED0 PARM('C5UT27B' '' '' '' '0')
 :  : FIN
 :  : INI . Richiesta parametri
 :  : CMD CALL C5UT27A
 :  : FIN

### C5UT29A  Aggiornamento data scadenza o tipo pagamento su rate
Dati in input Tipo ente, codice ente o lista ente, data scadenza e tipo pagamento provvede ad
aggiornare, se richiesto, le rate riportando data scadenza inseriti e natura pagamento e forzatura
rischio derivati dal tipo pagamento in input.
Produce comunque una stampa delle rate aggiornate.
 :  : INI . Sorgente C5UT29A
 :  : CMD CALL B£VED0 PARM('C5UT29A' '' '' '' '0')
 :  : FIN
 :  : INI . Sorgente C5UT29B
 :  : CMD CALL B£VED0 PARM('C5UT29B' '' '' '' '0')
 :  : FIN
 :  : INI . Richiesta parametri
 :  : CMD CALL C5UT29A
 :  : FIN

### C5UT31X  Post-modifica C5F per allineamento coordinate bancarie
Programma funizzato da inserire in azione di Post-inserimento e Post-modifica della tabella
C5F in modo che al variare di coordinate bancarie (ABI-CAB o conto corrente) di una banca venga
aggiornata anche l'informazione £21 del tipo ente AZI collegata alla banca.
Creare i flussi di inserimento e modifica tabella C5F (elementoi I-TAC5F, M-TAC5F della tabella
B£H) e le azioni del sottosettore legate a questo flusso inserendo il programma di cui all'oggetto.
Per definizione è stabilito che il sottosettore della tabella B£J si il TA ovvero il sottosettore
che raggruppa tutte le azioni che riguardano tabelle.
 :  : INI . Sorgente
 :  : CMD CALL B£VED0 PARM('C5UT31X' '' '' '' '0')
 :  : FIN
 :  : DEC T(ST) P() K(B£H)
 :  : DEC T(ST) P() K(B£JTA)

### C5UT33A Rifasatura numeri protocollo
Dato un tipo e numero protocollo iniziale dacui partire e numero protocollo finale a cui arrivare
è possibile rinumerare i protocolli passando anche il nuovo numero iniziale.
L'aggiornamento viene eseguito solo se la riga di registrazione non è stata stampata su giornale.
E' possibile eseguire il programma in sola stampa prima di procedere all'agiornamento.
 :  : INI . Sorgente C5UT33A
 :  : CMD CALL B£VED0 PARM('C5UT33A' '' '' '' '0')
 :  : FIN
 :  : INI . Sorgente C5UT33B
 :  : CMD CALL B£VED0 PARM('C5UT33B' '' '' '' '0')
 :  : FIN
 :  : INI . Richiesta parametri
 :  : CMD CALL C5UT33A
 :  : FIN

### C5UT34A Controllo quadratura portafoglio
Questo pgm permette di analizzare l'andamento dei movimenti delle rate in rapporto ai movimenti delle rate
 :  : INI . Sorgente
 :  : CMD CALL B£VED0 PARM('C5UT34A' '' '' '' '0')
 :  : FIN
 :  : INI . Richiesta parametri
 :  : CMD CALL C5UT34A
 :  : FIN

### C5UT35A Generazione differenze cambio
 :  : INI . Sorgente C5UT35A
 :  : CMD CALL B£VED0 PARM('C5UT35A' '' '' '' '0')
 :  : FIN
 :  : INI . Sorgente C5UT35B
 :  : CMD CALL B£VED0 PARM('C5UT35B' '' '' '' '0')
 :  : FIN
 :  : INI . Richiesta parametri
 :  : CMD CALL C5UT35A
 :  : FIN

### C5UT36A Modifica condizione di massa
Questo pgm permette di cambiare la condizione (FLAG02) su un gruppo di registrazioni
 :  : INI . Sorgente C5UT36A
 :  : CMD CALL B£VED0 PARM('C5UT36A' '' '' '' '0')
 :  : FIN
 :  : INI . Sorgente C5UT36B
 :  : CMD CALL B£VED0 PARM('C5UT36B' '' '' '' '0')
 :  : FIN
 :  : INI . Richiesta parametri
 :  : CMD CALL C5UT36A
 :  : FIN

### C5UT38A Creazione rate assenti
Data in input una riga ne crea la relativa rata. ATTENZIONE :  NON VIENE FATTO ALCUN CONTROLLO DI PREESISTENZA!!!!
 :  : INI . Sorgente
 :  : CMD CALL B£VED0 PARM('C5UT38A' '' '' '' '0')
 :  : FIN
 :  : INI . Richiesta parametri
 :  : CMD CALL C5UT38A
 :  : FIN

### C5UT41A Storno e ripresa registrazioni contabili
 :  : INI . Sorgente C5UT41A
 :  : CMD CALL B£VED0 PARM('C5UT41A' '' '' '' '0')
 :  : FIN
 :  : INI . Sorgente C5UT41B
 :  : CMD CALL B£VED0 PARM('C5UT41B' '' '' '' '0')
 :  : FIN
 :  : INI . Richiesta parametri
 :  : CMD CALL C5UT41A
 :  : FIN

### C5UT45A Aggiornamento importo rata pagato
Il programma, dato in input importo di differenza, data registrazione iniziale e data registrazione finale, aggiorna le rate di pagato, qualora la differenza tra dovuto-pagato rientri nei limiti scelti. Questo viene utilizzato per risolvere i problemi di squadratura (in genere dell'ordine del 0,05) dopo una conversione.
 :  : INI . Sorgente C5UT45A
 :  : CMD CALL B£VED0 PARM('C5UT45A' '' '' '' '0')
 :  : FIN
 :  : INI . Sorgente C5UT45B
 :  : CMD CALL B£VED0 PARM('C5UT45B' '' '' '' '0')
 :  : FIN
 :  : INI . Richiesta parametri
 :  : CMD CALL C5UT45A
 :  : FIN

### C5UT46A Creazione Aperture/Chiusure Clienti
 :  : INI . Sorgente C5UT46A
 :  : CMD CALL B£VED0 PARM('C5UT46A' '' '' '' '0')
 :  : FIN_
 :  : INI . Sorgente C5UT46B
 :  : CMD CALL B£VED0 PARM('C5UT46B' '' '' '' '0')
 :  : FIN_
 :  : INI . Richiesta parametri
 :  : CMD CALL C5UT46A
 :  : FIN_

### C5UT47A Aggiornamento documento su Reg.Convertite
 :  : INI . Sorgente C5UT47A
 :  : CMD CALL B£VED0 PARM('C5UT47A' '' '' '' '0')
 :  : FIN
 :  : INI . Sorgente C5UT47A
 :  : CMD CALL B£VED0 PARM('C5UT47A' '' '' '' '0')
 :  : FIN
 :  : INI . Richiesta parametri
 :  : CMD CALL C5UT47A
 :  : FIN

### C5UT48A Modifica di Massa su Rate
Questo pgm permette di cambiare alcuni campi in maniera massiva su un raggruppamento di rate.
 :  : INI . Sorgente C5UT48A
 :  : CMD CALL B£VED0 PARM('C5UT48A' '' '' '' '0')
 :  : FIN
 :  : INI . Sorgente C5UT48B
 :  : CMD CALL B£VED0 PARM('C5UT48B' '' '' '' '0')
 :  : FIN
 :  : INI . Richiesta parametri
 :  : CMD CALL C5UT48A
 :  : FIN

### C5UT50A Annullamento Registrazioni di Massa
Questo pgm permette di cambiare alcuni campi in maniera massiva su un raggruppamento di rate.
 :  : INI . Sorgente C5UT50A
 :  : CMD CALL B£VED0 PARM('C5UT50A' '' '' '' '0')
 :  : FIN
 :  : INI . Sorgente C5UT50B
 :  : CMD CALL B£VED0 PARM('C5UT50B' '' '' '' '0')
 :  : FIN
 :  : INI . Richiesta parametri
 :  : CMD CALL C5UT50A
 :  : FIN

### C5UT55A Riallineamento Solleciti
Questo pgm permette di riallineare stato e livello sui solleciti
 :  : INI . Sorgente C5UT55A
 :  : CMD CALL B£VED0 PARM('C5UT55A' '' '' '' '0')
 :  : FIN
 :  : INI . Sorgente C5UT55B
 :  : CMD CALL B£VED0 PARM('C5UT55B' '' '' '' '0')
 :  : FIN
 :  : INI . Richiesta parametri
 :  : CMD CALL C5UT55A
 :  : FIN

### C5UT56A Creazione Casi di Test su Competenza
Questo pgm permette di simulare casi di test sulle date competenza
 :  : INI . Sorgente C5UT56A
 :  : CMD CALL B£VED0 PARM('C5UT56A' '' '' '' '0')
 :  : FIN
 :  : INI . Sorgente C5UT56B
 :  : CMD CALL B£VED0 PARM('C5UT56B' '' '' '' '0')
 :  : FIN
 :  : INI . Richiesta parametri
 :  : CMD CALL C5UT56A
 :  : FIN

### C5UT57A Riconferma Registrazioni
Questo pgm permette di ri-eseguire le azioni alla conferma delle registrazioni.
 :  : INI . Sorgente C5UT57A
 :  : CMD CALL B£VED0 PARM('C5UT57A' '' '' '' '0')
 :  : FIN
 :  : INI . Sorgente C5UT57B
 :  : CMD CALL B£VED0 PARM('C5UT57B' '' '' '' '0')
 :  : FIN
 :  : INI . Richiesta parametri
 :  : CMD CALL C5UT57A
 :  : FIN

### C5UT58A Adeguamento Flag Regime IVA per Cassa
Questo pgm permette di aggiornare i flag necessari al regime iva per cassa.
 :  : INI . Sorgente C5UT58A
 :  : CMD CALL B£VED0 PARM('C5UT58A' '' '' '' '0')
 :  : FIN
 :  : INI . Sorgente C5UT58B
 :  : CMD CALL B£VED0 PARM('C5UT58B' '' '' '' '0')
 :  : FIN
 :  : INI . Richiesta parametri
 :  : CMD CALL C5UT58A
 :  : FIN

### C5UT59A Giroconto Ente/Ente Scadenze Aperte
Questo pgm permette di girocontare le scadenze aperte da ente a ente.
 :  : INI . Sorgente C5UT59A
 :  : CMD CALL B£VED0 PARM('C5UT59A' '' '' '' '0')
 :  : FIN
 :  : INI . Sorgente C5UT59B
 :  : CMD CALL B£VED0 PARM('C5UT59B' '' '' '' '0')
 :  : FIN
 :  : INI . Richiesta parametri
 :  : CMD CALL C5UT59A
 :  : FIN

### C5UT60A Ripristino Interessi
Questo pgm permette di annullare le fatture relative agli interessi di pagamento
 :  : INI . Sorgente C5UT60A
 :  : CMD CALL B£VED0 PARM('C5UT60A' '' '' '' '0')
 :  : FIN
 :  : INI . Sorgente C5UT60B
 :  : CMD CALL B£VED0 PARM('C5UT60B' '' '' '' '0')
 :  : FIN
 :  : INI . Richiesta parametri
 :  : CMD CALL C5UT60A
 :  : FIN
