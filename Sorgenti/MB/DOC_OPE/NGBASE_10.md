# Gestione Buoni di Cassa

## Gestione Buoni di Cassa

Con questa procedura è possibile generare ed utilizzare i Buoni di Cassa
In Negoziando sono attualmente gestite quattro tipologie di Buoni di Cassa : 

 * Buoni per Reso Merce
 * Buoni di Sconto (a Valore)
 * Buoni di Sconto (in Percentuale)
 * Buoni per Pagamento

## Configurazione Applicativa e Tabelle

Per poter gestire i Buoni di Cassa è fondamentale configurare prima le seguenti Tabelle di Negoziando, dal _Menu>Principale>Anagrafiche di Base>Gestione Tabelle_

(vedi capitolo Gestione Tabelle) : 

 * Tabella ALIV - Aliquote IVA
 * Tabella RPCA - Reparti Cassa
 * Tabella RPCR - Relazioni Reparti Cassa
 * Tabella CABU - Causali per Emissioni Buoni di Cassa
 * Tabella INCT - Tipologie Movimenti di Cassa

Dal _Menu>Utilità>Configurazione>Configurazione Applicativa>Cassa-Slave>Parametri per Emissione Buoni/Acconti

**Per i Buoni di Reso Merce definire** : 

 * Stampa Buoni : 
 ** Impostare SI su Stampante se si desidera stampare il Modulo dei Buoni
 ** Impostare SI su Registratore se si intende stampare uno Scontrino Non fiscale con i Riferimenti del Buono
 * Eventuale Nome della Stampante da utilizzare per la stampa del Modulo
 * Numero Copie da stampare del Modulo
 * Stampa Codice a Barre su Modulo SI/NO :  è un'informazione utilizzata nella Stampa del Modulo - Si tratta di un Codice a Barre di tipo Code128
 * Numero Giorni di Validità del Buono :  questo valore serve per preparare la richiesta della Data di Scadenza del Buono in fase di emissione da Cassa
 * Messaggio per Stampa su Registratore. Indicare un Codice Commento per personalizzare la Stampa degli Scontrini Non Fiscali in fase di emissione del Buono, dal _Menu>Principale>Anagrafiche di Base>Gestione Commenti_

**Per i Buoni di tipo Sconto Automatico** : 

 * Impostare SI alla richiesta Attiva Gestione
 * Indicare il Codice Gruppo Parametri Fidelity (per la definizione del Gruppo Parametri vedi sotto)
 * Tipo applicazione parametri : 
 ** Indicare se per tutti i Clienti
 ** solo per i Clienti che non sono Fidelizzati
 * Codice Commento di Stampa :  per stampare le informazioni relative al Buono direttamente sullo Scontrino di emissione utilizzare la funzione di Gestione Commenti e definire un commento di tipo Commento per Stampa Informazioni Buoni su Scontrino. Durante la definizione del commento sarà possibile utilizzare il tasto F2 per inserire nel commento dei valori variabili in base al buono da stampare.  dal _Menu>Principale>Anagrafiche di Base>Gestione Commenti_

Nella parte finale della videata sarà possibile definire : 

 * Codice Articolo per la Scrittura dei Movimenti di Magazzino : nel caso si desideri generare dei movimenti di Magazzino al momento della Emissione e dell'Utilizzo dei Buoni di Reso, così da poterne tenere traccia anche nelle stampe
 * Modalità di Rilascio dei Buoni : nel caso si intenda utilizzare la funzione di Attivazione/Generazione Buoni di Cassa per Clienti Fidelity.
 * Consenti Utilizzo Buoni Scaduti :  indicare se è consentito l'utilizzo di Buoni con Data di Scadenza inferiore alla Data attuale.Se ammesso tale utilizzo verrà richiesta conferma prima di utilizzare il buono.

## Emissione Buoni di Reso Merce in Cassa

In Cassa è possibile attivare l'emissione dei Buoni di Reso Merce e dei Buoni di Sconto (a Valore).
Per attivare l'emissione dei Buoni di Reso Merce occorre definire un Bottone con le seguenti caratteristiche : 

 * FCode="PUTVOUCHER"
 * FAttr="xx;yy;zzzzzz", dove : 
 ** xx = Codice Reparto
 ** yy = Codice Iva
 ** zzzzzzz =Codice identificativo articolo per scrittura tabella Movimenti di Cassa. Questo codice verrà utilizzato esclusivamente per la scrittura della tabella dei Movimenti di Cassa (MOCSH00F), ci permetterà quindi di tenere traccia dell'utilizzo dei buoni per interrogazioni del sistema

Alla pressione del Bottone si aprirà una videata con le seguenti richieste : 

 * Importo del Buono :  tale Importo può essere digitato al momento della richiesta delle Informazioni o prima di premere il Bottone
 * Data Scadenza del Buono :  il programma proporrà una Data di Scadenza in base alla Data di Emissione e al numero di giorni di validità definito in Configurazione. Confermare questa Data o modificarla.
 * Cognome e Nome
 * Annotazioni
 * Codice Causale :  questo codice verrà memorizzato nella tabella relativa gli Impegni di Cassa per eventuali interrogazioni sul motivi di emissione dei buoni.
N.B.Se il registratore di Cassa non è abilitato a gestire un totale parziale Negativo, operativamente, nel caso di emissione del Buono di Reso Merce occorrerà prima effettuare l'emissione del Buono e successivamente premere Reso e leggere il Codice a Barre del prodotto restituito dal cliente.

## Emissione Buoni di Sconto automatici in Cassa

In Cassa è possibile attivare l'emissione di Buoni di Sconto (a valore) automatici a fine Scontrino.
Dal _Menu>Principale>Gestione Fidelity Card>Configurazione>Gestione Parametri Fidelity-Globali_
Inserire un Nuovo Parametro (tasto F6=Inserisci) definendo : 

 * Codice Parametro
 * Descrizione

Premere successivamente F6 per gestire le Date del Parametro e definire obbligatoriamente : 

 * Data Inizio Validità
 * Data Fine Validità
 * Descrizione

Premere nuovamente F6 per inserire le informazioni per la Gestione dei Giorni, degli Orari e delle Condizioni di Validità.

## Nel pannello "Giorni/Ore"

Definire : 

 * Giorno/i della Settimana
 * Orari di Inizio e Ora di Fine
(selezionare Tutti e 00 : 00/23 : 59 se non si intendono porre dei limiti su Giorno/Ora)

## Nel pannello Buoni Automatici

Definire : 

 * Informazioni per Emissione Buoni
 ** eventuale Importo Minino Scontrino : in questo caso il Buono verrà emesso solo nel caso di Scontrini per un importo = > all'importo definito
 ** % di Sconto Automatico :  verrà calcolata dal Programma di Cassa sulla base dell'Importo dello Scontrino
 ** eventuale codice Causale : si tratta di un codice definito nella Tabella CABU -Causali per Emissione Buoni di Cassa. Questo codice verrà memorizzato nella tabella relativa agli Impegni di Cassa per eventuali interrogazioni sul motivo di emissione dei buoni
 * Informazioni per Utilizzo Buoni
 ** Periodo di utilizzo del Buono :  per la definizione del Periodo si possono specificare le Date di Inizio/Fine o il Numero di Giorni - sempre di Inizio/Fine
 ** eventuale Importo Minino Scontrino :  in questo caso il Buono potrà essere utilizzato solo nel caso di Scontrini per un importo = >all'importo definito
 ** % per calcolo Importo Minimo Scontrino :  in alternativa all'Importo Minimo Scontrino, impostando ad es :  50% se viene emesso uno scontrino per 300 Euro significa che lo scontrino dove potrà essere utilizzato il Buono dovrà essere di almeno 150 Euro
 ** Indicare se per il calcolo dell'Importo Minimo dello Scontrino che utilizzerà il Buono occorre considerare o meno articoli già in promozione.

## Emissione Buoni da Negoziando

Esiste inoltre una funzione generica per l'emissione di Gruppi di Buoni.
Dal _Menu>Principale>Gestione Registratori di Cassa>Buoni/Acconti>Generazione Buoni di Cassa_
Definire inizialmente : 

 * Tipologia dei Buoni :  indicare se buoni di Reso, Sconto a Valore, Sconto in Percentuale o Pagamento
 * Data di Inizio Validità dei Buoni
 * Data di Fine Validità dei Buoni
 * Importo dei Buoni :  se Buoni di Reso o Sconto a Valore o Pagamento
 * % di Sconto :  solo se Buoni di Sconto in Percentuale
 * Nominativo
 * Annotazioni
 * Codice Causale :  vedi annotazioni precedenti
 * Numero Buoni da generare
 * Elenco Clienti Fidelity per cui generare i buoni

Definire le informazioni per l'Utilizzo dei Buoni : 

 * Modalità di Attivazione
 ** Nel caso venga indicato Soggetto ad Attivazione il buono non potrà essere utilizzato finchè non viene utilizzata la funzione specifica di Attivazione Buoni per Clienti Fidelity
 * Importo Massimo per Applicazione Sconto :  solo Buoni di Sconto in Percentuale. Se viene definito questo importo in fase di utilizzo del Buono lo Sconto verrà calcolato o su questo valore (se Importo Scontrino > = al valore indicato) o sull'importo dello Scontrino (se importo Scontrino inferiore)
 * Importo Minimo Acquisti per Utilizzo :  se definito, il Buono non potrà essere utilizzato se l'Importo dello Scontrino è inferiore all'importo indicato
 * Modalità di Controllo Importo Minimo Acquisti
 * Escludi Prezzi Promozionali :  SI/NO
 ** nel caso venga impostato a SI il Buono non potrà essere utilizzato nel caso in cui nello Scontrino siano presenti articoli venduti a un prezzo inferiore al prezzo di Listino o nel caso in cui nello scontrino siano presenti righe di Sconto.
 * Codice Elenco Negozi :  nel caso venga definito un Elenco di Negozi il Buono sarà utilizzabile solo se il Negozio in cui si sta tentando l'utilizzo è compreso in questo Elenco.
 * Codice Elenco Articoli :  nel caso venga definito un Elenco di Articoli il Buono sarà utilizzabile solo se nello scontrino sono inseriti Articoli compresi nell'elenco definito.
 * Buoni Cumulabili :  impostando NO a questa richiesta nello scontrino in cui si inserirà il Buono sarà possibile inserire solo un Buono.
 * Consenti Utilizzi Illimitati

Definire infine le informazioni per l'eventuale generazione dei Codici a Barre : 

 * Modalità Generazione Barcode che potrà essere : 
 ** Nessuna
 ** Progressiva
 ** Progressiva con 3 Numeri Casuali
 ** BarCode Alfanumerici Casuali
 * Codice a Barre iniziale  :  questo valore va definito nel caso in cui si intenda attribuire a ciascun Buono un Codice a Barre di tipo EAN13 .Questa impostazione deve essere effettuata nel caso di generazione Barcode in modalità Progressiva o Progressiva con 3 Numeri casuali. Nel primo caso definire un valore di 12 cifre, nel secondo un valore di 9 cifre.
A conferma della Generazione dei Buoni ne verrà visualizzato l'elenco e sarà possibile esportare questo elenco in un file Excel.
N.B. Tramite l'indicazione del Codice Causale (Tabella CABU) sarà possibile impostare anche il Codice Motivo Sconto da indicare sui Movimenti di Magazzino relativi all'utilizzo dei Buoni.
Utilizzare la funzione di Gestione Tabelle e definire appunto il Motivo di Sconto nella Tabella MOTS - Motivazioni Sconti di Cassa


## Gestione Regole di Generazione Buoni da Cassa

Con questa funzione è possibile definire le regole di Generazione dei Buoni di Cassa nel caso di attivazione di una Promozione che preveda come Benefit per il Cliente l'Emissione di un Buono.
 Dal _Menu>Principale > Gestione Registratori di Cassa>Buoni/Acconti>Generazione Buoni di Cassa_
All'attivazione della funzione vengono presentate le regole esistenti.
Nella Gestione della Regola vengono richiesti Codice e Descrizione della stessa e le medesime informazioni per Emissione Buoni e Utilizzo Buoni della funzione di Emissione Buoni da Negoziando.
La modalità di Generazione del Codice a Barre del Buono sarà sempre BarCode AlfaNumerici Casuali
E' stata attivata nella Gestione dei Buoni delle Promozioni la possibilità di generare Buoni Sconto di Importo variabile  (in base all'Importo dello Scontrino o agli articoli della Promo usati nello Scontrino).

Nella Gestione delle Regole per l'Emissione dei Buoni sono state aggiunte due nuove Tipologie di Buoni : 

 * Buoni sconto a Valore :  % su Scontrino
 * Buoni Sconto a Valore :  % su Articoli Promozione

I Buoni Sconto a Valore già esistenti diventano Buoni Sconto a Valore (Importo Fisso)
Per queste due nuove tipologie di Buoni occorrerà indicare la Percentuale di Sconto e non l'Importo
Il programma di Cassa, per queste nuove tipologie, calcolerà l'Importo del Buono in base ai valori dello Scontrino e alla Percentuale indicata ed emetterà quindi Buoni Sconto a Valore normali
In questo caso però l'emissione del Buono è condizionata all'acquisto dei prodotti della Promo.

E' stata aggiunta la possibilità di Gestire la Circolarità per l'utilizzo dei Buoni emessi dalle Promo, Richiesta Metodologia Circolarità
I Valori ammessi sono : 

 * Illimitata :  è il valore di Default e vale per tutti i Buoni già emessi, dove non indicato un Elenco di Negozi specifico
 * Da Elenco Negozi :  il buono potrà essere utilizzato solo nei Negozi dell'Elenco,che dovrà essere indicato
 * Solo Negozio Emittente :  il buono potrà essere utilizzato solo nel Negozio dove è stato emesso
 * Solo Negozi della Società Emittente :  il buono potrà essere utilizzato solo nei Negozi della stessa Società del Negozio che lo ha emesso

Il programma di Cassa nell'utilizzo dei Buoni controllerà la Metodologia di Circolarità.

Nella gestione delle Regole per Emissione dei Buoni di Cassa delle Promozioni sono state aggiunte due nuove richieste : 

 * % per Calcolo Importo Minimo Acquisti
 * Obbligatorietà Lettura Tessera Fidelity. I valori ammessi sono : 
 ** NO (di default)
 ** Si-Qualunque Tessera
 ** Sì-Tessera con la quale è stato Emesso il Buono

Il Programma di Cassa, nell'emissione dei Buoni legati alle Promozioni, terrà conto della prima info per impostare eventualmente l'Importo Minimo Acquisti per Utilizzo del Buono (occorrerà indicare o la percentuale o l'importo Fisso)

La seconda richiesta condiziona sempre l'Utilizzo del Buono.
Nel caso venga impostato SI - Qualunque Tessera,  ma non venga letta nessuna Fidelity, avremo la segnalazione :  Buono Utilizzabile solo con Lettura Fidelity
Nel caso venga impostato SI - Tessera con la quale è stato emesso il Buono, ma in Cassa non abbiano letto nessuna Tessera o ne abbiamo letta una diversa avremo :  Buono Utilizzabile solo con la Tessera Fidelity xxxxxxxxxx.

## Utilizzo dei Buoni in Cassa

Per l'utilizzo dei Buoni in Cassa Slave occorre definire un Bottone con le seguenti caratteristiche : 

 * FCode :  "GETVOUCHER"
 * FAttr :  "xx;yy;zzzzzz;yyy;mmm"
 * xx :  Codice Reparto
 * yy :  Codice Iva
 * zzzzzzz :  Codice identificativo articolo per scrittura tabella Movimenti di Cassa
 * Yyy :  Codice Incasso
 * mmm :  Modalità di Ritiro (facoltativa)
 ** NOR (Normale)
 ** CRN (da Carnet di Buoni)

N.B.Il Codice Incasso serve esclusivamente per i Buoni di Tipo Pagamento e sarà utilizzato nella Gestione delle Chiusure di Cassa.
(Si tratta di un codice della Tabella INCT - Tipologie Movimenti di Cassa).

## Utilizzo dei Buoni in Modalità Standard (Normale)

Alla pressione del Bottone si aprirà la videata di richiesta di selezione del Buono
Vengono richiesti : 

 * Codice a Barre
 * Nodo di Emissione e Numero Buono
L'indicazione del Codice a Barre o del Nodo/Numero sono in alternativa.

E' da tenere presente che il Codice a Barre del Buono può essere di 3 tipi : 

 ** Codice a Barre Stampato sul Modulo dalla Cassa Slave in Fase di Emissione, si tratta della combinazione Nodo+Numero
 ** Codice a Barre (Ean13) definito in fase di Generazione dei Buoni da Negoziando
 ** Il Codice a Barre identificativo dello Scontrino con cui è stato emesso il Buono.Questo codice viene stampato su tutti gli scontrini se la Cassa lo supporta e se definito l'apposito valore nella Configurazione di Negoziando

Per l'utilizzo dei Buoni occorre inoltre considerare : 

 * Buoni di Tipo Reso
 ** Non potranno essere utilizzati se iniziate Operazioni di Chiusura Scontrino (Pagamenti)
 ** Non potranno essere utilizzati come Prima Riga dello Scontrino (se il Registratore non supporta valori parziali Negativi)
 * Buoni di Sconto a Valore
 ** Non potranno essere utilizzati se iniziate Operazioni di Chiusura Scontrino (Pagamenti)
 ** Non potranno essere utilizzati come Prima Riga dello Scontrino
 ** Non potranno essere utilizzati se il Totale dello Scontrino è uguale o inferiore a zero.
 * Buoni di Sconto in Percentuale
 ** Non potranno essere utilizzati se iniziate Operazioni di Chiusura Scontrino (Pagamenti)
 ** Non potranno essere utilizzati come Prima Riga dello Scontrino
 ** Non potranno essere utilizzati se il Totale dello Scontrino è uguale o inferiore a zero.
 ** Prima della lettura del Buono è obbligatorio premere SubTotale
 * Buoni di Pagamento
 ** Potranno essere utilizzati solo se iniziate Operazioni di Chiusura Scontrino (Pagamenti) o se l'ultima riga dello Scontrino è SubTotale.
 ** Non potranno essere utilizzati se il Totale dello Scontrino è uguale o inferiore a zero.
In fase di Selezione del Buono verranno inoltre attivati tutti i controlli in base alle impostazioni dei Buoni stessi (Data Scadenza / Data Inizio Utilizzo / Importo Minimo Acquisto etc....)

## Utilizzo dei Buoni in Modalità con Indicazione Carnet

Se sul Bottone di Cassa viene impostato come attributo la modalità di Ritiro tramite Carnet, alla pressione del Bottone verrà richiesto di indicare il Codice Carnet. Si tratta di un codice che dovrà essere definito nella tabella BUCR - Carnet Buoni
Una volta indicato il Codice Carnet verrà presentato l'elenco dei Buoni ancora utilizzabili del Carnet
Selezionare il Buono da Utilizzare e premere Invio

N.B. In Negoziando attualmente non è attiva nessuna funzione che permette l'impostazione del Codice
Carnet sui Buoni. L'impostazione di tale codice (al momento) potrà essere effettuata solo tramite procedure esterne.

## Gestione Buoni OnLine

Per la Gestione dei Buoni è possibile anche attivare il Servizio OnLine.
Con questo servizio i buoni sono sempre disponibili e sempre aggiornati indipendentemente dal Negozio in cui viene emesso il Buono o in cui viene Utilizzato.
Per attivare questo Servizio (in Sede) definirne l'apposita Configurazione con Negoziando InfoCenter.
Dal _Menu>Utilità>Configurazione>Gestione Configurazione Applicativa>Negoziando InfoCenter Live_
Definire le impostazioni per i Servizi Live nel Pannello Impostazioni Client e Servizi Live
 * Impostare SI alla richiesta Attiva Richieste Buoni
E' da tenere presente che, nel caso il Servizio OnLine non sia disponibile per problemi di linea, sia la scrittura di nuovi Buoni, che la ricerca per l'utilizzo di Buoni esistenti verrà effettuata sul DB Locale
Gli aggiornamenti alla Tabella dei Buoni verranno poi trasmessi a Sede - e quindi anche alServizio OnLine - con le normali trasmissioni di Dati (vedi capitolo Gestione Trasmissioni)

## Gestione Informazioni Buoni

 :  : R03 Dal Menu>Principale>Gestione Registratore di Cassa>Buoni/Acconti>Gestione Buoni/Acconti
Questa funzione permette il completamento (o l'eventuale modifica) delle informazioni relative ai Buoni emessi. La funzione (utilizzabile anche per gli Acconti) richiede inizialmente di selezionare il Codice del
Punto Vendita (facoltativo se elaborazione di Sede) e permette di indicare un range di Date o di Codici Cassa. Una volta effettuata la selezione iniziale viene presentato l'elenco dei Buoni,in base ai Criteri di selezione indicati.
Nell'elenco dei Buoni verranno evidenziate le Informazioni esistenti e i riferimenti allo Scontrino di Emissione.

Sono a disposizione i seguenti tasti funzionali : 

 * Invio per l'aggiornamento delle Informazioni del Buono
 * F7 per la Stampa del Modulo
 * F3 per l'eventuale Forzata Chiusura dl Buono

Premendo Invio è possibile completare le Informazioni del Buono selezionato ed è possibile definire : 

 * la Data di Scadenza del Buono
 * Cognome e Nome
 * Annotazioni

Premendo F3 sarà possibile effettuare la Forzata Chiusura di un Buono.
Una volta chiuso il Buono non potrà più essere utilizzato.

## Attivazione/Generazione Buoni per Clienti Fidelity

Questa funzione permette (in base alle Impostazioni della Configurazione) o di Attivare Buoni precedentemente Generati o di Generare dei Buoni per i Clienti Fidelity.
Per attivare questa funzionalità occorre definire le impostazioni dei Parametri Fidelity - pannello Utilizzo Punti per la determinazione del Numero dei Punti che verranno scalati dal Cliente a fronte
di attivazione/generazione di Buoni.
Nel caso si intenda utilizzare la funzionalità nella modalità di Generazione Buoni definire inoltre, sempre nelle impostazioni dei Parametri Fidelity - Pannello Buoni Automatici - le Informazioni per
l'emissione dei Buoni : 

 * Date Validità
 * Importo Minimo Scontrino per Utilizzo
 * Escludi Prezzi Promozionali
 * Codice Causale

Una volta effettuata la selezione del Cliente vengono effettuati i controlli sui Parametri Fidelity del Cliente (devono essere definite le modalità di Utilizzo Punti) e sui Punti del Cliente. Viene
eventualmente effettuata la segnalazione di anomalia e non sarà possibile proseguire nell'elaborazione.
Ad Es :  Punti Cliente Insufficienti per Attivazione/Generazione Buoni

Se i Parametri sono definiti correttamente e il cliente ha il minimo dei Punti necessari si passa alla Gestione dell'Attivazione/Generazione Buoni
L'utilizzo della funzione è diverso in base alle impostazioni della Configurazione - Richiesta Modalità di Rilascio Buoni (Attivazione/Generazione)

## Modalità di Configurazione Attivazione Buoni

Vengono evidenziati in neretto i valori dei Parametri Fidelity e in blu i valori massimi dei buoni che si potrebbero attivare in base ai punti del Cliente
Premendo il tasto F7 sarà possibile procedere all'attivazione di un Buono (indicare il Codice a Barre o Nodo/Numero Buono) : 
Una volta effettuata l'indicazione del Buono il programma eseguirà i seguenti controlli : 

 * Il Buono deve essere di tipo Sconto a Valore
 * Il Buono non deve essere già stato attivato
 * Il Buono non può essere già stato Utilizzato
 * L'importo del Buono (se indicato in anagrafica buoni) deve essere uno dei valori elencati nei tipi di Buono a Importo Fisso
 * Se Buono di tipo a Importo Fisso viene controllato che il Clienti abbia i punti necessari per l'utilizzo del Buono.
 * Se il Buono è valido, ma di tipo Calcolato, verrà richiesto di indicare l'Importo del Buono da emettere. In quest'ultimo caso, dopo l'indicazione dell'importo il programma controllerà
 ** l'importo del Buono stesso, che deve essere un multiplo dell'importo base
 ** che il Cliente abbia Punti Residui sufficienti per l'attivazione del Buono

Man mano che i Buoni vengono inseriti per l'attivazione, verrà aggiornata la videata riepilogativa coi valori evidenziati in rosso.
In questa videata è inoltre a disposizione il tasto funzionale F5 per visualizzare l'elenco dei Buoni già selezionati per l'attivazione e con questa funzione di Visualizzazione sarà possibile utilizzare il tasto F4 per eliminare un Buono dall'elenco dei buoni da attivare.
Premendo F6 dalla videata riepilogativa si potrà procedere alla effettiva Attivazione dei Buoni. Alla pressione del tasto vengono controllati (se indicati) il numero Minimo dei Punti da utilizzare e il
Numero massimo dei Punti utilizzabili dando eventuale segnalazione di anomalia.
Ad Es :  Punti Utilizzati Superiori al Massimo Consentito

Se impostata nei Parametri Fidelity l'obbligatorietà dell'Emissione Totale dei Buoni, sempre alla pressione del tasto F6 viene controllato se il cliente sta utilizzando tutti i Buoni possibili.
In caso contrario ne sarà data segnalazione non si potrà proseguire.
Se i punti sono validi, viene richiesta Conferma dell'attivazione
A conferma avvenuta i Buoni selezionati verranno attivati e sarà possibile utilizzarli in Casa
Verranno inoltre generati i Movimenti di storno di Punti per il Cliente Fidelity.
Se impostato nei Parametri Fidelity l'azzeramento dei Punti Residui, verrà inoltre generato un Movimento di Storno dei Punti Residui del Cliente.
N.B.Per la scrittura dei Movimenti di Storno dei Punti definire nella Configurazione il Codice Causale da Utilizzare per Utilizzo Punti
 :  : R03 Dal Menu>Utilità>Configurazione>Gestione Configurazione Applicativa>Fidelity e selezionare il Tab Movimenti Fidelity
Al termine verrà data segnalazione dell'attivazione dei Buoni.

## Modalità di Configurazione Generazione Buoni

Una volta selezionata la funzione, vengono evidenziati in neretto i Valori dei Parametri Fidelity e in blu i Valori Massimi dei buoni che si potrebbero attivare in base ai punti del Cliente
Selezionare la riga interessata e premere il tasto Invio per definire la Quantità dei buoni da generare.
 * Nel caso di selezione di un Buono di Tipo Calcolato verrà richiesto di indicare sia la Quantità dei Buoni da emettere, che l'Importo unitario dei Buoni stessi
 * Nel caso di selezione di un Buono di Tipo a Importo Fisso verrà richiesto di indicare solo le Quantità
A conferma se Buono di tipo Calcolato verrà controllato l'importo indicato, che dovrà essere unmultiplo dell'importo base
Verrà inoltre controllato, in base al numero di Buoni indicati e agli Importi, se i cliente dispone dei punti necessari per l'emissione dei Buoni.
In questa modalità di Configurazione è a disposizione il tasto F4 per annullare una errata registrazione dei buoni da emettere

Al termine dell'indicazione del numero di Buoni da Generare sarà possibile premere il tasto F6 per Conferma
Come nella Gestione in modalità Attivazione, se definiti, verranno controllati il Minimo di Punti richiesti, il Massimo di Punti utilizzabili e l'eventuale indicazione di Emissione Totale dei Buoni. Se i
punti sono corretti, viene richiesta conferma
A conferma avvenuta verranno generati i nuovi Buoni di Cassa e verranno generati i movimenti di storno dei punti per il Cliente Fidelity (vedi annotazioni della modalità Attivazione).
In base alle impostazioni della Configurazione (richiesta Stampa Buoni) potrà essere inoltre effettuata la Stampa dei Buoni Emessi.
N.B. La stampa su Scontrini Non Fiscali del Registratore sarà possibile solo se la funzionalità viene attivata da un Bottone di Cassa

## Visualizzazione/Stampa Buoni

 :  : R03 Dal Menu>Principale>Registratori di Cassa>Buoni/Acconti>Visualizza/Stampa Acconti e Buoni di Cassa
In Negoziando è inoltre attiva una funzione che permette di effettuare interrogazioni sui Buoni (e anche sugli Acconti) emessi dalla Cassa o dal programma specifico di Generazione.
All'attivazione della funzione vengono richiesti i parametri (facoltativi) per la selezione dell'elenco dei Buoni da evidenziare. Dopo aver effettuato le selezioni iniziali verrà presentato tale elenco.
Sono a disposizione i seguenti tasti funzionali : 

 * F2 per Ristampa del Singolo Buono
 * F5 per Stampare l'Elenco dei Buoni
