# Tessere Regalo (Gift Cards)

## Tessere Regalo (Gift Cards)

Questa funzione permette di gestire l'emissione, l'attivazione e l'utilizzo delle Tessere Regalo. Sono ammesse tipologie diverse che permettono di predeterminare gli importi delle Tessere oppure stabilirli caso per caso in fase di Attivazione. Gli importi caricati sulle tessere possono essere utilizzati anche parzialmente. Le tessere possono essere a esaurimento oppure ricaricabili. La singola tessera può essere gestita sull'intera catena, su un insieme di negozi o limitata al punto vendita di attivazione.
Le operazioni per la generazione prevedono i seguenti passi : 
 * Configurazione :  definizione delle specifiche del lotto di tessere che si intende generare;
 * Produzione :  generazione dei numeri delle singole tessere. Questi numeri andranno eventualmente comunicati alla tipografia per la stampa sulla tessera fisica;
 * Distribuzione :  attribuzione dei lotti di tessere al punto vendita.
Le tessere sono a questo punto disponibili nei punti vendita per essere Attivate (vendute a cliente), Utilizzate e Ricaricate.
Sono poi disponibili gli strumenti per tracciare ogni singolo movimento delle tessere.

## Configurazione
Iniziamo con la configurazione della Tipologia di Tessera Regalo.
Dal Menu di _Negoziando>Principale>Anagrafiche di Base>Gestione Tabelle>GFTP Tipologie Tessere Regalo

Premere Invio=Conferma ed in seguito F6=Inserisci per creare una nuova tipologia.
Inserire il Codice Tipologia, es. 001 e confermare.
Verranno richiesti : 
 * Descrizione Tipologia
 * Prefisso Tessera :  i primi 4 caratteri del codice tessera, valori compresi tra 1000 e 9999. Sono ammesse tipologie differenti con lo stesso prefisso
 * Giorni di validità tessera :  per quanti giorni la tessera è valida a partire dalla sua attivazione (consegna al cliente)
 * Tessera a Importo Prefissato :  SI= la tessera viene generata con un valore predefinito; NO= il valore viene determinato in fase di attivazione
 * Tessera Ricaricabile  :  SI=la tessera può essere ricaricata (anche senza essere esaurita); NO=una volta esaurito il credito non è più valida
 * Emissione Live :  permette di attivare le tessere tramite un WebService (vedi InfoCenter)
 * Importo Minimo Caricabile : sse la tessera è Ricaricabile, imposta l'importo minimo che la tessera deve raggiungere dopo una ricarica. Quindi, l'importo che il cliente ricarica, sommato all'eventuale residuo, deve essere pari o superiore a quanto indicato nel campo.
 * Importo Massimo Caricabile : sse la tessera è Ricaricabile, imposta l'importo massimo che la tessera può raggiungere dopo una ricarica. Quindi, l'importo che il cliente ricarica, sommato all'eventuale residuo, deve essere inferiore o pari a quanto indicato nel campo
 * Articolo per movimenti di Magazzino :  articolo che viene utilizzato nei movimenti di magazzino per tenere traccia dei movimenti di tutte le tessere appartenenti a questa tipologia. Dato che normalmente non è necessario interrogare la giacenza di questo articolo, è opportuno utilizzarne uno NON GESTITO a magazzino (vedi Anagrafica Articoli)
 * Causale per Movimenti di Magazzino : creare una Causale di Magazzino da associare ai movimenti di vendita e di utilizzo delle Gift (che avrà segno negativo, visto che scarica il magazzino). La ricarica, invece, avrà segno positivo (vedi _I_Principale>Anagrafiche di base>Gestione Tabelle, Tabella CAMA Causali di Magazzino)
 * Modalità Emissione : 
 ** Inclusa nello Scontrino=la transazione viene inserita nello scontrino fiscale come vendita a fronte di un corrispettivo, quindi la chiusura Z Fiscale terrà conto anche di questo importo. __Gli importi caricati in questa modalità potranno essere utilizzati solo a diminuzione dell'importo dovuto all'interno dello scontrino come RESO ARTICOLO (righe con quantità negativa)
 ** Scontrino Non Fiscale=lo scontrino relativo alla Gift sarà uno scontrino NON Fiscale, riporterà solo una nota con la descrizione della transazione.Se nello stesso scontrino c'è anche la vendita normale di un articolo, quella verrà stampata per prima su scontrino fiscale, seguirà poi un commento che riporta la transazione relativa  all'emissione della Gift. __Gli importi caricati potranno essere utilizzati negli Scontrini di Cassa soltanto come forma di Pagamento.

Configuriamo ora le Causali Movimenti Regalo, ovvero differenziamo quali siano le operazioni che vengono svolte con le Tessere, suddivise per 4 tipologie.
Dal Menu di Negoziando_Principale>Anagrafiche di Base>Gestione Tabelle>GFCA Causali Movimenti Tessere Regalo

Premere Invio=Conferma ed in seguito F6=Inserisci per creare una nuova Causale, attribuendole un Codice
Definire : 
 * Descrizione Causale
 * Tipo Causale :  scegliere una tra le 4 tipologie (Attivazione/Ricarica/Utilizzo/Annullamento)

## Circolarità delle Tessere Regalo

Con la definizione della Metodologia di Circolarità ed eventualmente dell' Elenco di Circolarità vengono determinati i criteri di utilizzo delle tessere al di fuori del negozio di attivazione. Tali regole devono essere impostate sull'Anagrafica dei Magazzini che utilizzeranno le Tessere.
In _Principale>Anagrafiche di Base>Gestione Anagrafica Magazzini_
Selezionare il magazzino sul quale definire la circolarità, premere 3 volte Invio e a questo punto definire l'ultima parte della videata : 
 * Metodologia Circolarità : 
 ** Solo negozio emittente :  La tessera potrà essere utilizzata solo nel Negozio in cui è stata attivata.
 ** Solo Punti Vendita della Società :  La tessera potrà essere utilizzata solo nei Negozi che appartengono alla stessa Società del Negozio che ha attivato la tessera
 ** Da Elenco :  La Tessere potrà essere utilizzata solo nei Negozi che appartengono all'Elenco Negozi indicato nella richiesta successiva
 * Elenco Circolarità :  lista dei negozi in cui la tessera può essere utllizzata (vedi Elenchi/Composizioni)
 * Giorni di Validità Tessere Regalo :  per quanti giorni la tessera è valida a partire dalla sua attivazione (*)
 * Importo Minimo Carica Tessere Regalo :  se la tessera è Ricaricabile, imposta l'importo minimo della ricarica (*)
 * Importo Minimo Carica Tessere Regalo :  se la tessera è Ricaricabile, imposta l'importo massimo della ricarica (*)
(*) questi 3 campi sono gli stessi già impostati precedentemente in _Principale>Anagrafiche di Base>Gestione Tabelle, tabella GFTP Tipologie Tessere Regalo. Vengono utilizzati se in GFTP sono stati lasciati in bianco.

## Utilità
## Produzione Tessere Regalo

Con la presente funzione è possibile produrre le tessere regalo, ovvero creare una serie di numeri di tessera abbinati opzionalmente a un valore in contanti, in funzione della tipologia selezionata. L'operazione può essere ripetuta più volte sulla stessa tipologia di tessera :  la numerazione prosegue generando sempre nuovi numeri.
Dal Menu>_Principale>Gestione Tessere Regalo>Utilità>Produzione Tessere Regalo_
Vengono richiesti : 
 * Codice Tipologia Tessere :  (vedi sopra Configurazione, da Tabella GFTP)
 * Codice Valuta :  la valuta
 * Importo Tessera :  l'importo della tessera. Il campo compare solo se la tipologia selezionata prevede l'Importo Prefissato.
 * Numero Tessere da Produrre :  il numero di Numeri progressivi che verranno generati in questa sessione. La numerazione è strutturata nel seguente modo : 
 ** prefisso tessera (4 cifre) :  impostato nella Tipologia tessera
 ** numero progressivo (8 cifre) :  progressivo all'interno del prefisso specificato
 ** numerazione casuale (4 cifre) :  generata per evitare che possano essere utilizzati indebitamente numeri di tessera senza essere titolari della tessera stessa

Premere F6=Crea Tessere, verificare il messaggio che appare e confermare la creazione
Una volta generate le tessere, apparirà un messaggio di conferma.
Premendo OK, si aprirà l'elenco delle tessere prodotte. Col tasto F6 è possibile esportare questo elenco su Excel. E' opportuno effettuare l'esportazione per comunicare la numerazione al tipografo nel caso in cui le tessere vengano stampate su un supporto fisico.

## Distribuzione Tessere Regalo

Ogni tessera, anche se generata in sede, va assegnata a un singolo negozio dove sarà attivata tramite la vendita a cliente.
Questa funzione quindi permette di memorizzare sull'archivio anagrafico delle tessere il codice del negozio al quale è stata inviata la tessera e la data dell'invio.
Dal Menu _Principale>Gestione Tessere Regalo>Utilità>DistribuzioneTessere Regalo_
Vengono richiesti : 
 * Range di Tessere (DA/A) da aggiornare :  il primo e l'ultimo numero (il più basso e il più alto) delle tessere da distribuire.
 * Codice Negozio di Distribuzione
 * Data di Distribuzione

Dopo aver premuto il tasto Invio il programma controlla se per alcune/tutte le tessere indicate sia già stata effettuata la distribuzione o se le tessere siano già state attivate. Il programma segnala l'eventuale presenza di tessere già distribuite e, dietro conferma, modifica negozio e data con i dati della distribuzione corrente. Il programma segnala anche tessere già Attivate ma su queste NON effettua l'aggiornamento del Negozio/Data di Distribuzione.
Dopo la verifica appena descritta il programma richiederà conferma dell'Aggiornamento dei dati sull'archivio anagrafico delle tessere, quindi premere OK per procedere.

## Analisi Tessere Regalo Attivate

Questa funzione permette di effettuare analisi sulle tessere attivate
Dal Menu>_Principale>Gestione Tessere Regalo>Utilità>Analisi Tessere Regalo Attivate_
Vengono richieste obbligatoriamente : 
 * Da Data attivazione
 * A Data attivazione
E' poi possibile specificare (facoltativamente) per analisi specifiche : 
 * Codice Negozio
 * Codice Società
 * Codice Elenco di Negozi
 * Tipologia Tessera
 * Importo Originale Tessera
 * Codice Valuta

Una volta effettuate le selezioni e premuto invio verrà visualizzato un Riepilogo delle Tessere Regalo Attivate : 
I dati vengono riepilogati per Codice Negozio / Tipologia Tessera / Importo Tessera / CodiceValuta.
Vengono visualizzati : 
 * Numero Tessere Attivate
 * Importo Tessere Attivate
 * Numero Tessere Ricaricate
 * Importo Tessere Ricaricate
 * Numero Transazioni
 * Importo Tessere Utilizzate
 * Numero Tessere Residuo
 * Importo Tessere Residuo
Tramite il tasto F6 è possibile esportare queste informazioni in un Foglio Excel.

## Analisi Tessere Regalo Distribuite

Questa funzione permette di effettuare analisi sulle tessere Distribuite.
Dal Menu _Principale>Gestione Tessere Regalo>Utilità>Analisi Tessere Regalo Distribuite_
I parametri di selezione di questa analisi sono identici a quelli della precedente
Anche qui i dati vengono riepilogati per Codice Negozio / Tipologia Tessera / Importo Tessera / Codice Valuta.
Vengono visualizzati : 
 * Numero Tessere Distribuite
 * Importo Tessere Distribuite
 * Numero Tessere Attivate
 * Importo Tessere Attivate
 * Numero Tessere Disponibili
 * Importo Tessere Disponibili
Anche qui, tramite il tasto F6 è possibile esportare queste informazioni in un Foglio Excel

## Analisi Dettaglio Tessere Regalo

Questa funzione permette di effettuare analisi sulle tessere Emesse (Attivate) o Distribuite.
Dal Menu _Principale>Gestione Tessere Regalo>Utilità>Analisi Dettaglio Tessere Regalo _
I parametri di selezione di questa analisi sono : 
Codice Negozio
Società
Elenco Negozi
Da data a data
sia per le tessere già Emesse sia per quelle solamente Distribuite. E' inoltre possibile filtrare sulle sole tessere Emesse o non Emesse o includere tutte le tessere.
E' possibile anche filtrare sul periodo di Produzione.

Vengono visualizzate singolarmente le tessere che rientrano nella selezione con tutti i dati di tipologia, importo, data produzione e distribuzione, negozio e data emissione, data ultimo utilizzo, importo residuo, data scadenza e segnalato l'eventuale stato di tessera Bloccata. Anche queste informazioni sono esportabili in Excel tramite il tasto F6.
Posizionandosi su una tessera e premendo il tasto F5 si apre la griglia con il dettaglio dell'utilizzo della tessera negli scontrini di vendita. Viene visualizzato anche l'eventuale movimento di Annullo (vedi Annullo Tessera Regalo).

## Blocco Tessere Regalo

Questa funzione permette di bloccare l'Utilizzo di una Tessera Regalo.
Dal Menu _Principale>Gestione Tessere Regalo>Utilità>BloccoTessere Regalo_
Viene richiesto di indicare il Codice della Tessera da bloccare.
Una volta indicato il Codice Tessera e premuto F6 verrà richiesta conferma del blocco della tessera specificata, premere OK per bloccare l'Utilizzo della Tessera.
Prima della richiesta di Conferma, il programma esegue un controllo sullo stato della tessera dando eventuale segnalazione di errore se dovesse risultare già bloccata. Dopo l'operazione, un tentativo dell'utilizzo della tessera in Cassa restituisce il messaggio 'Tessera Bloccata'.

## Sblocco Tessere Regalo

Questa funzione permette di riattivare l'utilizzo di una Tessera Regalo precedentemente Bloccata.
Dal Menu _Principale>Gestione Tessere Regalo>Utilità>SbloccoTessere Regalo_

Le modalità di utilizzo della funzione (richiesta Codice Tessera e Conferma) sono identiche alla funzione di Blocco Tessere.

## Annullo Tessera Regalo
Questa funzione permette di annullare una Tessera Regalo.
Dal Menu _Principale>Gestione Tessere Regalo>Utilità>Annulla Tessera Regalo_
Le modalità di utilizzo della funzione (richiesta Codice Tessera e Conferma) sono identiche alla funzione di Blocco Tessere, in aggiunta è possibile inserire un commento.
Un tentativo dell'utilizzo di questa tessera in Cassa restituisce il messaggio 'Tessera Bloccata'.

## Visualizzazione Estratto Conto Tessere Regalo

Questa funzione permette di visualizzare/stampare l'Estratto Conto di una singola tessera.
Viene inizialmente richiesto il Codice Tessera
Premendo Invio verrà Visualizzato il dettaglio dei movimenti della tessera selezionata. E' possibile stampare l'Estratto Conto (tasto F4) o effettuarne l'esportazione su un foglio Excel (tasto F6).
N.B. La stessa funzionalità è attivabile anche nella tastiera di Cassa con un bottone specifico (vedi annotazioni successive).


## Movimenti

## Quadratura Saldi/Movimenti Tessere Regalo

Questa funzione effettua la verifica di quadratura tra il Saldo della Tessera indicato sull'Anagrafica e il Saldo calcolato sulla base dei movimenti.
Dal Menu _Principale>Gestione Tessere Regalo>Movimenti>Quadratura Saldi/Movimenti Tessere Regalo
Vengono evidenziate le Tessere per le quali i due Saldi non corrispondono
Sono a disposizione i seguenti tasti funzionali : 
F5 Per effettuare la correzione del saldo di una singola tessera
F6 Per effettuare la correzione del saldo di tutte le tessere in elenco
F9 Per visualizzare i movimenti della tessera

## Quadratura Movimenti Tessere Regalo Negozio/Sede
Per motivi di sicurezza ogni operazione svolta sulle Tessere viene effettuata una doppia registrazione dei dati, una in locale sul PC del punto vendita e una direttamente sul Server grazie al servizio InfoCenter. Possono verificarsi dei casi in cui questa doppia registrazione non è possibile. Il caso più comune consiste nell'assenza temporanea della connessione Internet :  in questo situazione avremo la sola registrazione sul punto vendita. Il dato locale viene trasmesso successivamente al Server, dove la funzione di Quadratura Negozio/Sede consente di verificare le anomalie dei dati ed eventualmente di allinearli.
Dal Menu _Principale>Gestione Tessere Regalo>Movimenti>Quadratura Movimenti Tessere Regalo Negozio/Sede
Vengono evidenziati i Movimenti di Sede che non hanno l'esatta corrispondenza con i Movimenti del Negozio (e viceversa). Il punto in cui è registrato il movimento è chiaramente indicato nella prima colonna (Negozio o Sede). E' possibile stampare l'elenco delle anomalie con il tasto F4 o esportarlo in Excel con il tasto F6. Il tasto F9 permette di generare il movimento di Sede mancante che corrisponde al movimento di PV.

E' possibile stampare l'elenco delle anomalie con il tasto F4 o esportarlo in Excel con il tasto F6.

## Configurazione per l'Utilizzo in Cassa

Per attivare la funzionalità in Cassa occorre definire alcuni parametri nella Configurazione di Negoziando
E' da tenere presente che per attivare questo Servizio occorre attivare Negoziando InfoCenter Live (vedi capitolo Negoziando InfoCenter Live)
Dal Menu _Utilità>Configurazione>Negoziando InfoCenter Live_
Nella Scheda Servizi Live
Definire : 
 * Attivazione Richieste Tessere Regalo (SI/NO) = SI
 * Codice Reparto Cassa da utilizzare per l'emissione dello Scontrino = Reparto cassa abbinato all'aliquota IVA attribuita alla vendita della Tessera
Nella Scheda Info Tessere Regalo

Utilizzando il tasto F1 per accedere alla tabella GFCA Causali Movimenti Tessere Regalo descritta in precedenza : 

 * Codice Causale per Attivazione
 * Codice Causale per Ricarica
 * Codice Causale per Utilizzo
 * Codice Causale per Annullamento
Poi
 * Codice Articolo (Facoltativo) per l'eventuale scrittura dei Movimenti di Magazzino (vedi Configurazione Tabella GFTP, Articolo per movimenti di Magazzino)

Impostiamo anche i Codici Messaggio Fine Scontrino. Sono diciture libere che vengono stampate in calce allo scontrino in cui viene utilizzata la tessera.
 * Messaggio Generico :  su tutti gli scontrini con tessera, se non sono definiti i campi successivi
 * Messaggio per Attivazione :  in calce alle attivazioni
 * Messaggio per Ricarica :  in calce alle ricariche
 * Messaggio per Utilizzo :  in calce agli utilizzi
Questa selezione è differenziata per scontrini Fiscali e NON Fiscali stampati in base alla modalità di Emissione della tessera (vedi Configurazione Tabella GFTP, Modalità Emissione)

Per la costruzione dei messaggi fare riferimento alla tabella Commenti (Principale>Anagrafiche di base>Gestione Commenti)

N.B.
Nella definizione dei record della tabella Commenti per il Codice Messaggio di Fine Scontrino, per i messaggi con Tipologia Commento=Commento per Stampa Informazioni Tessere Regalo su Scontrino, è possibile utilizzare le seguenti variabili : 
 * %CODTES% stampa il Codice della Tessera (12 caratteri iniziali+ 'XXXX')
 * %TESSERA% stampa il Codice della Tessera (tutti i caratteri)
 * %DTSCTESS% stampa la Data della Scadenza
 * %SALPRE% stampa il Saldo Precedente
* %IMPCAR% stampa l'Importo Caricato sulla Tessera
* %IMPUTI% stampa l'Importo Utilizzato della Tessera
* %SALFIN% stampa il Saldo Finale della Tessera
* %DATORA% stampa la Data e l'Ora

## Altre Configurazioni per l'Utilizzo in Cassa

Elenchiamo altre possibilità di configurazione
Dal Menu _Utilità>Configurazione>Gestione Configurazione Applicativa>Cassa-Slave>Altri Parametri (3)
 * Blocca Modalità Pagamenti Tessere regalo se Scontrino sole Tessere Regalo :  impostato a SI non permette di accettare Tessere con Modalità Emissione 'Scontrino NON fiscale' come pagamento se nello scontrino ci sono solo attivazioni di Tessere
 * Escludi Importi con decimali nell'Attivazione/Ricarica Tessere Regalo : impostato a SI, in fase di Attivazione o Ricarica obbliga ad accettare solo importi interi
 * Richiedi Modalità di Utilizzo Tessera Regalo : 
 ** NO=fanno fede gli importi precaricati in fase di generazione tessera, che deve essere a Importo Prefissato. La selezione tra attivazione e utilizzo viene effettuata col tasto RESO (vedi ATTIVAZIONE E UTILIZZO TESSERA)
 ** SI=viene proposto/richiesto l'importo per l'attivazione/utilizzo/ricarica al momento in cui la tessera viene passata in cassa
 * Aggiungi SubTotale dopo utilizzo Tessera Regalo :  impostando a SI viene inserita automaticamente una riga di SubTotale nello Scontrino dopo la lettura di una tessera.

## Tastiera di Cassa e Funzionalità

## Attivazione Tessera

L'interfaccia dell'attivazione varia a seconda dell'impostazione di Richiedi Modalità Utilizzo Tessera Regalo (vedi Altre Configurazioni per l'utilizzo in cassa)
Con Richiedi Modalità Utilizzo =NO :  lSe la tessera ha un importo fisso predefinito è sufficiente leggere il codice tessera in Cassa la tessera viene inserita nello scontrino. Se la tessera non ha l'importo predefinito, digitare l'importo per l'Attivazione e premere il tasto Imposta Prezzo, poi leggere il codice tessera.
Con Richiedi Modalità Utilizzo =SI :  oOccorre semplicemente leggere il Codice a Barre della Tessera e si aprirà una maschera che presenta una Tab Attivazione in cui viene mostrato l'importo già precaricato e non modificabile nel caso di tessera a importo fisso, con la possibilità di inserire l'importo in caso contrario. Premere Invio e poi terminare il pagamento.
L'attivazione della Tessera avverrà solo a chiusura dello scontrino.

## Ricarica Tessera
Con Richiedi Modalità Utilizzo Tessera Regalo=NO :  digitare l'importo per la Ricarica e premere il tasto Imposta Prezzo, poi leggere il codice tessera
Con Richiedi Modalità Utilizzo Tessera Regalo =SI :  leggendo il Codice a Barre della Tessera e si aprirà una maschera. Selezionare il Tab Ricarica e digitare l'importo che si intende caricare sulla Tessera, premere Invio e poi terminare il pagamento.
La ricarica della Tessera avverrà solo a chiusura dello scontrino.

## Utilizzo della Tessera con Modalità Emissione = Scontrino Fiscale (vedi Configurazione, Tabella GFTP)

Per le tessere emesso con Scontrino Fiscale, anche l'utilizzo è condizionato dal parametro Richiedi Modalità Utilizzo Tessera Regalo (vedi Altre Configurazioni per l'utilizzo in cassa)
Con Richiedi Modalità Utilizzo =NO :  premere il tasto RESO e leggere il codice tessera. Viene creata nello scontrino una riga di RESO ARTICOLO che quindi va a diminuire il SUbTotale scontrino. Non è possibile agire sull'importo utilizzato, per cui il residuo tessera viene utilizzato o fino all'azzeramento del SubTotale scontrino o fino all'azzeramento del credito residuo stesso.
Con Richiedi Modalità Utilizzo =SI :  per utilizzare la tessera leggere inizialmente gli articoli in vendita. A questo punto leggere il codice a barre della Tessera e si aprirà la stessa schermata dell'attivazione.
Selezionare il Tab Utilizzo, che in automatico ci propone l'importo da scalare. In questo caso si può ridurre l'importo scalato dalla tessera.Confermare e procedere con la chiusura dello scontrino
Nel caso in cui l'importo della Gift non bastasse a coprire l'intero acquisto, l'importo ancora dovuto verrà visualizzato nel display operatore.

## Utilizzo Tessera con Modalità Emissione = Scontrino NON Fiscale  (vedi Configurazione, Tabella GFTP)

Queste Tessere vanno utilizzate come metodo di Pagamento, per cui va aggiunto un apposito bottone nella Cassa (vedi capitolo Draw Plates). Il Bottone deve essere creato con _FunctionCode= GIFTPAYMENT_ e negli Attributi del Bottone occorre specificare il Codice Incasso (da Tabella INCT).
Dopo aver premuto il SubTotale, premendo il Bottone di Pagamento viene richiesto il numero di tessera.
Nel caso in cui l'importo della Gift non bastasse a coprire l'intero acquisto, l'importo ancora dovuto verrà visualizzato nel display operatore.

## Visualizzazione/Stampa Estratto Conto in Cassa

E' possibile definire un apposito Bottone per l'interrogazione dell'Estratto Conto delle Tessere Regalo (vedi capitolo Draw Plates).
Il Bottone dovrà avere come caratteristica :  _FunctionCode= DSPGIFTINFORM_
Alla pressione del bottone verrà richiesto di indicare il codice della Tessera. Una volta indicato tale codice verrà Visualizzato l'Estratto conto della Tessera.E possibile Stampare l'Estratto Conto o su carta (tasto F7) o su uno scontrino di cassa Non Fiscale (tasto F8).

## Saldo Residuo

In qualsiasi momento è possibile ottenere dal programma di cassa la visualizzazione del Saldo Residuo della Tessera Regalo.
Il Bottone dovrà avere come caratteristica _FunctionCode=DISPLAYPRICE_ stesso bottone utilizzato anche per visualizzare i prezzi degli articoli
Per ottenere questa informazione premere il tasto Visualizza/Prezzo  e successivamente leggere il Codice a Barre della Tessera stessa.


Sme.UP
Last Rev. : 15/03/2016
