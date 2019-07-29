# Chiusure di Cassa Versione 3 - Con Gestione Cassaforte e Turni Operatori

## Chiusure di Cassa Versione 3 - Con Gestione Cassaforte e Turni Operatori

## Premessa

In Negoziando esistono diverse versioni di gestione delle chiusure di cassa, dalla meno articolata a questa, la più completa e ormai la più diffusa ed utilizzata.
La Chiusura in oggetto permette di gestire : 

 * aperture e chiusure dei turni degli operatori di cassa
 * distinte in valuta estera
 * distinte di prelievo dal cassetto di cassa verso la cassaforte
 * successivo controllo delle distinte in cassaforte
 * versamento in banca o a sede delle distinte in cassaforte
 * successivo controllo del versamento in banca
 * chiusura serale della singola cassa
 * chiusura serale del negozio
 * controllo delle spese e associazione dell'immagine del documento di ricevuta

Per attivare la funzionalità di Chiusura di Cassa con gestione Operatori e Cassaforte occorrerà : 

 * definire le tabelle standard delle chiusure di cassa
 * definire le nuove tabelle specifiche di questa modalità
 * definire le informazioni specifiche in anagrafica di magazzino
 * impostare la configurazione di Negoziando

## Tabelle da Configurare

Ecco l'elenco delle Tabelle da configurare per l'utilizzo di questa versione di Chiusura di Cassa

_Dal Menu>Principale>Anagrafiche di Base>Gestione Tabelle_

 * VATG - Tagli Valute
 * TDSC - Tipi Distinta di Cassa
 * INCA - Anagrafica Cassa
 * CASN - Registratori di Cassa - Negozi
 * FIPA - File e Percorsi (da configurare solo se si vogliono definire tastiere diverse per Negozi)
 * INCT - Tipologie Movimenti Cassa
 * VALU - Valute

## Tabella INCA - Anagrafica Cassa

E' in questa tabella che definiamo la Tipologia della Cassa, che può essere Cassa Contabile, ovvero il Cassetto di ogni Registratore, oppure la Cassaforte (se gestiamo la Chiusura con Gestione Cassaforte)
Per ciascuna Cassa occorre definire un Codice Cassa (codice alfanumerico di tre caratteri) e poi confermare. A questo punto verranno richiesti : 

 * Descrizione
 * Tipo Cassa. Si può definire se
 ** Cassa dei Registratori (quindi Cassetto)
 ** Cassaforte (deve essercene una sola)

## Tabella CASN - Registratori di Cassa - Negozi

In questo tabella vengono definiti i Registratori di Cassa di ciascun Negozio. Viene definito il Cassetto di ogni Cassa (due Casse, ad esempio, potrebbero avere un unico Cassetto in comune) associando al Registratore l'Anagrafica Cassa appena creata.
E' opportuno indicare : 

 * Codice Negozio
 * Codice Registratore
 * Descrizione
 * Matricola
 * 5 righe di Intestazione Scontrino. Principalmente utilizzata per le Casse Non Fiscali o per le Casse Fiscali che supportano la modifica dell'intestazione
 * Anagrafica Cassa. E' qui che associo il Registratore al Cassetto/Cassaforte precedentemente creato nella Tabella INCA - Anagrafica Cassa
 * File Definizione Tastiera Cassa. Nel caso si voglia utilizzare in Cassa Slave una Tastiera diversa a seconda del Negozio/Cassa, definire un Codice della Tabella FIPA. In questa tabella verranno richiesti
 ** Codice
 ** Descrizione
 ** File o Percorso. Definire percorso e nome del File della Tastiera (Plates).
 * Prefisso Barcode Scontrini per Utilizzo in Emergenza

## Tabella INCT -Tipologie Movimenti di Cassa

In questo tabella vengono definite le tipologie dei Movimenti di Cassa.
Per ciascuna Tipologia di Movimento è opportuno compilare SOLO i campi qui sotto indicati, gli altri riguardano versioni precedenti : 

 * Tipo Movimento. Può essere : 
 ** E = Entrata
 ** I = Incasso
 ** U = Uscita
 * Codice Movimento. Codice alfanumerico di 3 caratteri

Premere Invio e a questo punto definire : 

 * Descrizione Operazione (Es. Contanti, Carte, etc..)
 * Richiedi Anagrafica Sì/No. In determinati casi, come per il pagamento tramite Assegni, è possibile richiedere delle informazioni anagrafiche aggiuntive al momento del pagamento (es. Nome e Cognome, Numero Assegno, Banca d'Emissione). Queste informazioni andranno definite nella Tabella INCP - Campi Anagrafici da Richiedere per Registratore Cassa
 * Numero Sequenza. E' la sequenza in base alla quale verrà visualizzato l'elenco dei Tipi Movimento nella maschera delle Chiusure. Consigliamo di attribuire numeri in decine (10, 20,..) in modo da poter aggiungere valori intermedi in futuro.
 * Stampa Bollettina Sì/No. Una sorta di bolla di consegna stampata da una stampante NON fiscale
 * Tipologia. E' possibile scegliere tra : 
 ** Incasso Assegni
 ** Incasso Contanti
 ** Pagamenti
 ** Prelievo per Cassaforte
 ** Versamento in Banca
 ** Incasso con Carte di Credito
 ** Spesa
 * Richiedi Data Competenze Sì/No. Valore legato alla Richiesta Anagrafica. Oltre ai dati anagrafici aggiuntivi, è possibile richiedere la Data Emissione Scontrino in modo da avere un riferimento per quel preciso tipo di pagamento
 * Univocità Dati Anagrafici : 
 ** Sì, con Blocco
 ** Sì, con Richiesta
 ** Nessun Controllo. Riguarda i dati definiti nella Tabella INCP (esisterà 1 solo assegno n° X emesso in tal data dalla tal banca)
 * Versamento - Cassa Entrate. Questa informazione deve essere definita in caso di Tipologia Movimento = Prelievi per Cassaforte. Premere F1 per specificare il Codice della Cassaforte (Tabella INCA)
 * Versamento - Tipo Movimento Entrate. Questa informazione deve essere definita in caso di Tipologia Movimento = Prelievi per Cassaforte. Premere F1 per specificare il Tipo Movimento per la Registrazione del Movimento di Entrata in Cassaforte (Tabelle INCT)
 * Codice Valuta. Premere F1 per selezionare la Valuta (Tabella VALU)
 * Codice Incasso per il Resto. Premere F1 per selezionare il tipo incasso (Tabella INCT). Potrei incassare in Euro, ma emettere il resto in Franchi
 * Richiesta Annotazioni. Utilizzabile per la Registrazione delle Entrate/Uscite di Cassa per richiedere annotazioni alla registrazione ed é possibile indicare : 
 ** No
 ** Annotazioni Facoltative
 ** Annotazioni Obbligatorie
 * Codice Workflow. Da definire solo se si intende utilizzare la Gestione del Workflow sui Movimenti di Cassa. Premere F1 e selezionare il Tipo Workflow (Tabella WFLT)
  :  : DEC T(MB) P(DOC_OPE) K(NGBASE_XX)
 * Utilizzabile nella Gestione Spese Sì/No. Serve ad indicare se, in cassa, è possibile utilizzare il Tipo Movimento come causale per la registrazione di Entrate o Uscite di Cassa
 * Tipo Distinta di Cassa. Da impostare solo se viene attivata la Gestione dei Tipi Distinta di Cassa. Premere F1 per selezionare il Tipo Distinta (Tabella TDSC)

N.B. E' opportuno codificare un solo Movimento di Tipo Prelievi per Cassaforte.


## Tabelle da configurare per attivare questa specifica Chiusura di Cassa

Per attivare la Gestione della Chiusura di Cassa in questa modalità occorre definire le impostazioni delle seguenti tabelle : 

 * VATG - Tagli Valute **Obbligatoria**
 * TDSC - Tipi Distinte di Cassa **Facoltativa**
 * BANC - Banche **Facoltativa**
 * BACC - Conti Correnti Bancari **Facoltativa**

## Tabella VATG - Tagli Valute

In questo tabella occorre definire i Tagli per ciascuna Valuta utilizzata nei Negozi, che serviranno per la compilazione delle Distinte di Cassa. Oltre ai Tagli delle Valute è possibile codificare anche i Buoni e gli Assegni, se gestiti.
Premere F6 per inserire una Nuova Valuta e definire : 

 * Codice Valuta. Premere F1 e selezionare la Valuta (Tabella VALU)
 * Sequenza. E' la sequenza con la quale verranno presentati i Tagli nelle Richieste delle Distinte, è l'ordine in cui vengono visualizzati. Conviene sempre utilizzare valori come 10,20,30 etc, per poter aggiungere valori intermedi in futuro
 * Descrizione. Es. Pezzi da 20 Euro
 * Importo Taglio
 * Nome File Immagine. Al momento non utilizzato
 * Tipo Taglio. Può essere : 
 ** Contanti
 ** Buoni di Pagamento
 ** Assegni
 * Tipo Contanti. Specificare se Banconota o Moneta (solo in caso di Taglio Contanti)
 * Numero Massimo Pezzi per Taglio. Per un eventuale controllo nella digitazione delle Distinte di Cassa

## Tabella TDSC - Tipi Distinte di Cassa

La definizione delle informazioni di questa tabella è facoltativa. Occorre definirla se si desidera differenziare le modalità di Richiesta nelle Distinte di Cassa e nelle funzioni di Versamento.
Premere F6 per inserire un nuovo tipo Distinta, attribuire un codice alfanumerico di tre caratteri e confermare.
A questo punto specificare : 

 * Descrizione
 * Richiedi Banconote Sì/No
 * Richiedi Monete Sì/No
 * Richiedi Assegni Sì/No
 * Richiedi Buoni Sì/No
 * Tipo Versamento. Può essere : 
 ** In Banca
 ** In Sede

 :  :  T02 Tabelle BANC- Banche e BACC - Conti Correnti Bancari

La definizione delle informazioni di queste tabelle è facoltativa. Occorre impostare queste due tabelle se si intendono stampare i riferimenti dei Conti Correnti Bancari nella Distinta di Cassa utilizzata per i Versamenti in Banca.

 ## Tabella BANC - Banche

Per inserire una nuova Banca premere F6 ed attribuire un codice alfanumerico. Confermare e proseguire con la definizione dei campi seguenti : 

 * Descrizione
 * Ragione Sociale
 * Indirizzo
 * Cap
 * Località
 * Provincia
 * Nazione
 * Codici ABI e CAB
 * Codice BIC (Swift)

## Tabella BACC - Conti Correnti Bancari

Per inserire un nuovo Conto Corrente premere F6 ed attribuire un codice alfanumerico. Confermare e proseguire con la definizione dei campi seguenti : 

 * Descrizione
 * Codice Banca. Premere F1 per selezionarlo dalla Tabella BANC
 * Numero Conto Corrente Bancario
 * Codice IBAN
 * Codice Valuta. Premere F1 per selezionarlo dalla Tabella VALU

## Aggiornamento Tabella VALU - Valute, se attiva la Gestione Distinte di Cassa

Nel caso sia stata attivata la Gestione dei Tipi Distinte di Cassa, all'interno della Tabella VALU occorre impostare il Tipo Distinta di Cassa  che sarà utilizzato nelle richieste delle distinte non legate ai
Prelievi per Cassaforte.
Es. Richieste Fondo Cassa Iniziale/Finale, etc ...

## Distinta di Cassa

Si tratta del modulo per l'indicazione in dettaglio dei tagli compresi in un importo da prelevare per cassaforte, per il versamento in Banca, etc, oppure di numero e importo nel caso di assegni e buoni.
Nella Gestione delle Distinte, nel pannello iniziale vengono normalmente evidenziati la tipologia di Distinta di Cassa, la Valuta (se gestione Valuta attiva), il Tipo di Distinta (se attiva la gestione
della Tabella dei Tipi Distinta).

Subito sotto vengono evidenziate le informazioni del Negozio e dell'Operatore che sta effettuando la registrazione della Distinta di Cassa.

Nel pannello più grande vengono richieste le informazioni sul Numero di Banconote/Monete (o Assegni/Buoni) che compongono la Distinta di Cassa.
Sempre in questo pannello, a seconda della Tipologia di Distinta, possono essere evidenziati l'Importo Richiesto e la Differenza tra i valori digitati e l'Importo Richiesto.
Sono a disposizione i seguenti tasti funzionali per modificare le modalità di richiesta dati : 

 * F2 per richiedere Solo le Quantità
 * F3 per richiedere Solo gli Importi
 * F4 per richiedere Quantità e Importi
 * F8 Dati da Bilancia Conta Soldi (il tasto è attivo solo se è collegata la Bilancia Conta Soldi)

Le richieste effettuate nelle Distinte di Cassa sono condizionate alle impostazioni della Tabella dei Tagli Valute - VATG (in base alla Valuta utilizzata) ed eventualmente, se gestite, alle impostazioni
della Tabella dei Tipi Distinta.

N.B. Le Distinte di Cassa sono numerate progressivamente e possono sempre essere stampate (o su Modulo o su Scontrino Non Fiscale) in modo da poterle allegare a ciascuna Busta in cui verranno
inserite le relative Banconote/Monete.
La parola Busta viene talvolta utilizzata come sinonimo di Distinta di Cassa.

## Configurazione Anagrafica di Magazzino

Per attivare la Gestione delle Chiusure occorre attivare la Gestione degli Operatori per ogni negozio

_Dal Menu>Principale>Anagrafiche di Base>Gestione Anagrafica Magazzini_

Premere Invio fino ad arrivare alla quarta videata e alla Richiesta Gestione Turni Operatori impostare Sì
Sempre in questa videata è possibile specificare la Modalità di Gestione delle Chiusure Negozio, alla voce Modalità Gestione Chiusure di Cassa. In alternativa questa informazione può essere definita nella Configurazione : 

_Dal Menu>Utilità>Configurazione>Gestione Configurazione Applicativa>Chiusure di Cassa_

N.B.La definizione di questa informazione sull'Anagrafica di Magazzino ha priorità rispetto a quanto indicato nella Configurazione di Negoziando.

Se nella gestione dei Versamenti in Banca si desiderano stampare i riferimenti Bancari occorre indicare il Codice del Conto Corrente Bancario (dopo aver impostato le Tabelle BANC e BACC) nella prima  videata dell'Anagrafica Magazzino.

## Gestione Configurazione Applicativa - Chiusure di Cassa

_Dal Menu>Utilità>Configurazione>Gestione Configurazione Applicativa>Chiusure di Cassa_

Le informazioni sono divise in vari Pannelli : 

_Pannello Chiusure di Cassa_

Qui vengono definite le informazioni generiche delle Chiusure di Cassa.
Definire obbligatoriamente SOLO i campi qui elencati, gli altri sono relativi alle versioni di Chiusura Cassa precedenti : 

 * Modalità Incasso per il Resto. Selezionare il Tipo Incasso dalla Tabella INCT
 * Modalità Gestione Chiusure di Cassa. Indicare "Versione 3 - con Gestione Cassaforte"
 * Tipi Movimento per Differenze Positive/Negative. Selezionare il Tipo Movimento dalla Tabella INCT
 * Tipo Movimento per Versamento in Banca. Selezionare il Tipo Movimento dalla Tabella INCT
 * Tipo Movimento per Uscita Prelievo per Cassaforte. Selezionare il Tipo Movimento dalla Tabella INCT
 * Tipo Richiesta Data Registrazione nei Prelievi per Cassaforte
 ** Data Prelievo uguale a Data Odierna
 ** Data Prelievo da Richiedere
 * Importo Fondo Cassa

_Pannello Altre Informazioni Versione 3 (1)_

Per la configurazione della Modalità di Gestione Chiusure Versione 3 occorre definire SOLO le richieste riportate di seguito, le altre voci riguardano le vecchie tipologie di Chiusura : 

 * Richiedi Importi per Corrispettivi da Rapporto Zeta Sì/No
 * Richiedi Importo Note di Credito da Rapporto Zeta Sì/NO
 * Richiedi Importo Scontrini Annullati Sì/NO
 * Richiedi Importo Corrispettivi di Emergenza SI/NO
 * Richiedi Importo Documenti di Vendita SI/NO
 * Richiedi Importo Tessere Regalo SI/NO
 * Segnala Mancanza del Rapporto Zeta dalla Cassa. Si può scegliere tra : 
 ** No
 ** Sì - Solo Segnalazione
 ** Sì - Con Blocco Elaborazione
 * Richiedi Numero Scontrini SI/NO
 * Segnala Importo previsto del Prelievo nella Chiusura Turno SI/NO
 * Attività da chiudere nella Chiusura Negozio di Fine Giornata (vedi Gestione Attività)
  :  : DEC T(MB) P(DOC_OPE) K(NGBASE_XX)
 * Modalità Selezione Buste per Versamento in Banca che potrà essere : 
 ** Nessuna Proposta
 ** Buste Controllate di Giornate Chiuse con possibilità di Forzatura se giornata Non Chiusa
 ** Buste Controllate di Giornate Chiuse con Blocco
 * Blocca Versamento in Banca se Buste non Controllate SI/NO

_Pannello Informazioni Versione 3 (2)_

Queste informazioni sono specifiche della Modalità di Gestione Chiusure Versione 3.
Definire : 

 * Tipo Movimento Uscita da Cassaforte per Monete. Obbligatorio (Tabella INCT). In caso di Versamento in Banca, in presenza di Monete, il sistema chiede se si vogliono versare anche quelle o meno. Se si decide di NON versarle, verrà scritto un movimento con la causale impostata qui
 * Tipo Movimento Uscita da Cassaforte per Versamenti a Sede. Da compilare solo se attiva la Gestione Tipi Distinta di Cassa che prevedono Versamenti a Sede (Tabella INCT)
 * Gestione Distinte di Cassa in Valuta SI/NO. Impostare SI per i Negozi che Incassano in Valute diverse
 * Richiedi Annotazioni Commerciali nelle Chiusure Negozio
 ** NO
 ** Sì - Obbligatorie
 ** Sì - Facoltative
 * Tipi Movimenti specifici per Differenze.Questi 10 Tipi Movimento sono tutti facoltativi e servono per differenziare i Movimenti di Rettifica nelle analisi dei Movimenti di Cassa (Tabella INCT)
Se non definiti, verranno utilizzati i Tipi Movimento di Rettifica Positive/Negative definiti nel pannello iniziale di Configurazione Chiusure di Cassa
_Pannello Chiusure di Cassa_

_Pannello Bilancia Conta Soldi_

In questo pannello è possibile definire le Informazioni per l'eventuale Collegamento di una Bilancia Conta Soldi. Verranno richiesti : 

 * Nome. Viene proposta la Bilancia CashMaster, che è l'unica supportata da Negoziando al momento
 * IP
 * Porta

N.B. Se definite queste impostazioni, nella Gestione delle Distinte di Cassa verrà attivato il tasto F8 Dati da Bilancia Contasoldi per ricevere le informazioni richieste alla bilancia.

## Configurazione Applicativa - Parametri Cassa Slave

_Dal Menu>Utilità>Configurazione>Gestione Configurazione Applicativa>Cassa - Slave>Pannello Gestione Operatori

Per attivare le Chiusure di Cassa con Gestione Cassaforte e Operatori, in Cassa Slave, all'interno del Pannello Gestione Operatori, occorre impostare : 
 * Indica Operatore di Cassa. OBBLIGATORIO
 * Tipo Stampa Distinte di Cassa. Se la Gestione Distinte è attiva, indicare qui quale tipo Stampa si desidera, scegliendo tra : 
 ** Stampa Modulo
 ** Stampa Scontrino NON Fiscale
 ** Stampa Scontrino NON Fiscale e Modulo
 ** Nessuna Stampa

## Configurazione Applicativa - Parametri Casse Generali

_Dal Menu>Utilità>Configurazione>Gestione Configurazione Applicativa>Cassa - Generali_

Se si desidera impostare il controllo del Contante nel Cassetto ed ottenere la segnalazione per effettuare i Prelievi per Cassaforte al raggiungimento di un certo importo, occorre indicare : 

 * Tipo Controllo Importo Massimo Contanti nel Cassetto. E' possibile scegliere tra : 
 ** Controllo alla Chiusura di ogni Scontrino
 ** Controllo a Intervalli di Tempo Configurati
 ** Controllo a Chiusura Scontrino a Intervalli di Tempo Configurati
 ** Nessun Controllo

A seconda della scelta impostata, vanno poi compilate le due richieste seguenti : 

 * Importo Massimo Contanti nel Cassetto (escluso Fondo Cassa). Raggiunto questo limite scatterà la Richiesta di Prelievo per Cassaforte
 * Intervallo (in Secondi) per Controllo Importo Massimo Contanti nel Cassetto

## Funzionalità di Negoziando

Di seguito l'elenco delle funzionalità specifiche della Chiusura in oggetto : 

_Dal Menu>Principale>Chiusure di Cassa>Cassa_  : 

 * Registrazione Chiusure di Cassa
 * Conferma Registrazione Entrate/Uscite di Cassa
 * Conferma Chiusura di Fine Giornata - Negozio
 * Visualizza Distinte Cassa
(Oltre alle funzioni utilizzabili in tutte le modalità)

_Dal Menu>Principale>Chiusure di Cassa>Operatori_  : 

 * Apertura Turno Operatori
 * Chiusura Turno Operatori
- [Gestione Operatori](Sorgenti/MB/DOC_OPE/NGBASE_12)

_Dal Menu>Principale>Chiusure di Cassa>Cassaforte_  : 

 * Registrazione Prelievi per Cassaforte
 * Controllo Cassaforte

_Dal Menu>Principale>Chiusure di Cassa>Versamenti_  : 

 * Registrazione Versamenti in Banca
 * Controllo Versamenti in Banca
 * Analisi Versamenti in Banca
 * Registrazione Versamenti a Sede

E' inoltre possibile definire dei Bottoni in Cassa Slave che possono essere associati ad alcune delle funzionalità sopra indicate.
In cassa l'utilizzo del Bottone specifico potrà essere leggermente diverso dall'attivazione della funzione da Menù, infatti alcune informazioni non verranno richieste poiché verranno utilizzate direttamente quelle già presenti nel programma di Cassa.
Vedi annotazioni specifiche per la Gestione delle Chiusure in Cassa Slave.

## Apertura Turno Operatore

_Dal Menu>Principale>Chiusure di Cassa>Operatori>Apertura Turno Operatori _  : 

A questo punto l'Operatore dovrà indicare : 

 * Data
 * Ora
 * Registratore di Cassa
 * Codice Operatore
 * Password

N.B. Per effettuare l'Apertura Turno occorre che l'operatore di Cassa precedente abbia effettuato la Chiusura del suo. In caso contrario, è opportuno recuperare Utente e Password per poter chiudere quel turno e, se non reperibili, occorrerà rivolgersi al responsabile, il quale avrà un Codice col più alto livello di autorizzazione e potrà chiudere il Turno

Una volta indicati questi dati, l'Operatore potrà premere Invio per Confermare il Fondo Cassa che viene visualizzato in basso nella finestra, oppure F2 per Modificarne l'Importo specificando in dettaglio il Fondo Cassa trovato al suo arrivo tramite la compilazione.
A conferma della Distinta verrà richiesto di indicare delle annotazioni a riguardo della differenza riscontrata.
Indicare le Annotazioni e premere F6 Conferma Registrazione.
Se l'importo digitato non corrisponde all'Importo del Fondo Cassa, verrà generato un Movimento di Rettifica sulla Cassa del Registratore

## Prelievo per Cassaforte

_Dal Menu>Principale>Chiusure di Cassa>Cassaforte>Registrazione Prelievi per Cassaforte _  : 

In qualsiasi momento del turno, l'Operatore potrà effettuare un Prelievo di Contanti (o Assegni/Buoni) e depositarli in Cassaforte.
Indicare le seguenti informazioni e premere Invio : 

 * Data Prelievo
 * Ora Prelievo
 * Registratore di Cassa
 * Valuta
 * Operatore
 * Password

N.B. La Richiesta del Codice Valuta viene effettuata solo se è Attiva la Gestione delle Valute

Una volta effettuata la Conferma, se è attiva la Gestione del Tipi Distinta (TDSC) e, se per la Valuta specificata esistono più Tipi Distinta, viene richiesto di selezionare il Tipo Distinta da utilizzare.
Si accederà poi alla richiesta della Distinta di Cassa per il Prelievo per Cassaforte. Non viene indicato un Importo standard da versare, l'Operatore è libero di decidere la somma. Viene sempre effettuato un Controllo, con richiesta di Conferma, nel caso in cui l'importo indicato con la compilazione della Distinta sia maggiore dell'importo calcolato dal programma come incassato.
Viene successivamente richiesta conferma della Registrazione del Prelievo per Cassaforte
Al termine della Registrazione (in base alle impostazioni della Configurazione) sarà possibile effettuare la Stampa della Distinta di Cassa relativa al Prelievo effettuato.
Come già anticipato, tramite le impostazioni definite in Configurazione, è possibile decidere di segnalare all'Operatore l'obbligo di effettuare il Prelievo per la Cassaforte avendo raggiunto un certo limite di Contanti nel Cassetto.

## Chiusura Turno Operatore

_Dal Menu>Principale>Chiusure di Cassa>Operatori>Chiusura Turno Operatori _  : 

La gestione delle Chiusure di Cassa prevede che l'Operatore, al termine del suo turno di lavoro, effettui la Chiusura del proprio compilando richieste simili a quelle dell'apertura.
Dopo aver confermato le informazioni iniziali occorrerà procedere alla compilazione delle varie Distinte di Cassa : 

La prima Distinta Richiesta è quella relativa al Fondo Cassa che viene lasciato nel cassetto. Nella Gestione di questa Distinta di Cassa è obbligatorio quadrare l'Importo della Distinta rispetto
al Fondo Cassa definito in Configurazione.
Verrà richiesta Conferma della Registrazione e sarà possibile Stampare il Dettaglio della Distinta di Cassa.
In seguito verranno richieste tutte le Distinte di Cassa in base alle modalità di Incasso utilizzate nell'emissione degli scontrini (es. Euro, Buoni, Dollari...)

Per ciascuna Distinta di Cassa sarà possibile indicare delle Annotazioni e poi potrà essere stampata.

N.B. In questa fase non è obbligatorio quadrare l'importo richiesto. Se l'Importo indicato non corrisponde all'Importo Richiesto, sarà obbligatorio indicare delle annotazioni. Se il Prelievo per Cassaforte non è necessario, ne verrà data segnalazione

 :  :  T02 Registrazione Entrate o Uscite in Cassa

Nell'utilizzo del Programma di Cassa è possibile definire dei Bottoni per la Registrazione delle Spese (Uscite di Cassa) e di eventuali Entrate.
Per attivare questa funzionalità occorre definire un Bottone di Cassa che abbia queste caratteristiche : FCode="CASHMOVEMENTS" FAttr="y;yyy" dove, nella definizione degli Attributi (FAttr), occorre tenere presente : 

x = Tipo Movimento (Obbligatorio) dovrà essere o "U" per le Uscite o "E" per le Entrate
yyy = Codice Movimento (Facoltativo) dovrà essere un Codice della Tabella INCT - Tipologie Movimenti di Cassa

Alla pressione del Tasto, se il Codice Movimento non è definito sul Bottone, verrà richiesto di selezionarlo
Verranno poi richieste le informazioni per la registrazione del Movimento di Uscita / Entrata : 

 * Importo
 * Tipo
 * Data
 * Numero
 * Eventuali Note

Premere F6 per Confermare.
N.B. Il Movimento andrà poi confermato prima della Chiusura di Cassa tramite l'apposita funzione.


## Registrazione Movimenti di Cassa e Conferma Entrate/Uscite di Cassa

Se durante il proprio turno l'Operatore avesse registrato Entrate/Uscite di Cassa, la Conferma delle stesse deve essere effettuata prima della Registrazione della Chiusura di Cassa

_Dal Menu>Principale>Chiusure di Cassa>Cassa>Conferma Registrazione Entrate/Uscite di Cassa _  : 

Impostare Registratore di Cassa e Data e confermare. Verrà evidenziato l'elenco delle Entrate/Uscite effettuate.
Sono a disposizione, oltre ai soliti tasti funzionali, anche i seguenti : 

 * F5 Note. Per Visualizzare le note inserite in fase di registrazione
 * F9 Allega Ricevuta
 * F10 Visualizza Ricevuta

## Registrazione Chiusura di Cassa

Al termine della giornata occorrerà effettuare la Chiusura della Cassa

_Dal Menu>Principale>Chiusure di Cassa>Cassa>Registrazione Chiusure di Cassa _  : 

Indicare la Data della Chiusura e il Codice del Registratore di Cassa per cui effettuare la chiusura.
Prima di proseguire con l' elaborazione, il programma effettuerà le seguenti verifiche : 

 * Deve essere stata effettuata la Chiusura Turno dell'ultimo operatore. Se non effettuata, verrà richiesto di effettuarla al momento (indicazione Fondo Cassa, Prelievi etc....)
 * Deve essere stata effettuata la stampa del Rapporto Zeta dalla Cassa. In caso contrario il sistema ne darà segnalazione o bloccherà l'elaborazione (in base alle impostazioni definite in Configurazione)
 * Devono essere state effettuate anche tutte le Chiusure di Cassa dei giorni precedenti, altrimenti l'elaborazione verrà bloccata. Apparirà un messaggio che riporta anche le date con Chiusura mancante.
 * Se nella giornata sono state effettuate registrazione di Entrate o Uscite di Cassa, queste dovranno essere state confermate (vedi annotazioni precedenti)

Dopo le verifiche iniziali si passa alla Registrazione della Chiusura di Cassa : 

Nel pannello superiore vengono evidenziate le Informazioni del Negozio e della Cassa e i valori dei Corrispettivi Calcolati da Negoziando.
Le tre voci visualizzate sono : 

 * Valore Corrispettivi da Movimenti Cassa. Questo importo terrà conto di tutte le vendite effettuate in Cassa
 * Valore Corrispettivi da Magazzino. L'importo proposto quì comprende tutte le vendite che hanno movimentato il Magazzino, quindi scaricate correttamente con Codice
 * Valore Corrispettivi da Scarichi Manuali NON Elaborati. Questo importo indica invece tutte le vendite effettuate a Reparto, quindi senza Codice

Viene inoltre visualizzata l'eventuale differenza tra l'importo dei Corrispettivi da Rapporto Zeta del giorno e la differenza tra i GranTotali (prelevati dai rapporti Zeta) della chiusura del giorno corrente
con l'ultima chiusura effettuata.

Nel pannello centrale, il pannello dei Corrispettivi, sono evidenziati gli Importi che Negoziando riceve dal Registratore di Cassa in fase di stampa del Stampa del Rapporto Zeta (se il registratore di cassa è dotato di questa specifica funzionalità).
Esistono tre colonne : 
 * Importo Dichiarato. In automatico viene calcolato e proposto dal Sistema, ma è possibile per l'Operatore modificare gli importi proposti in questa colonna.
 * Importo Calcolato. In automatico viene calcolato e proposto dal Sistema, ma, a differenza di quello Dichiarato, questo campo non è modificabile.
 * Differenza. Propone l'eventuale differenza che potrebbe esserci nel momento in cui l'Operatore apportasse delle modifiche a qualche valore

Nella parte inferiore abbiamo i pannelli Incassi e il Riepilogo.

Nel pannello degli Incassi, vengono evidenziati gli importi del giorno suddivisi per tipologia di pagamento (anche qui vale il discorso delle tre colonne con Importi Dichiarati, Calcolati e Diferenza)
Questi importi vengono calcolati e proposti da Negoziando. Devono essere confermati o, eventualmente, modificati. Ad esempio, uno scontrino può essere stato chiuso in Cassa mediante il tasto Carte, anzichè Contanti. Modificando l'importo delle Carte in Chiusura, in automatico verrà ricalcolato quello dei Contanti e la colonna della Differenza ne riporterà l'importo.
A fianco resteranno sempre evidenziati gli Importi teorici calcolati da Negoziando.
In caso di Incasso effettuato in Valuta Estera, verrà evidenziato anche l'importo Calcolato nella Valuta di Incasso.

Premendo Invio o selezionando il pannello apposito verranno evidenziate le Informazioni di Riepilogo : 

Qui viene proposto l'elenco di eventuali Entrate/Uscite di Cassa Confermate. La Chiusura di Cassa deve essere normalmente effettuata senza che vengano evidenziate delle Differenze, il Versamento a Cassaforte dovrebbe già essere stato effettuato in fase di Chiusura
Turno con gli importi Corretti. E' naturalmente possibile effettuare la Chiusura di Cassa anche in presenza di Differenze, basterà specificarne la motivazione nella richiesta di annotazioni Finali.
Sono a disposizione i seguenti tasti funzionali : 

 * Invio. Per Confermare la Chiusura di Cassa
 * F7/F8 Giorno Precedente/Giorno Successivo. Per effettuare la Chiusura di Cassa di giorni Precedenti/Successivi
 * F11 Visualizza Rapporto Zeta. Per Visualizzare le Informazioni ricevute dal Registratore di Cassa in fase di stampa del Rapporto Zeta
 * F5 Visualizza Movimenti Cassaforte.

Premendo Invio per confermare la Chiusura vengono richieste le annotazioni : 

 * Indicare se Chiusura Corretta SI/NO
 * Eventuali Annotazioni. OBBLIGATORIE se la Chiusura Non è Corretta

E' possibile effettuare la Stampa del Riepilogo della Chiusura impostando a SI l'apposita richiestaStampa Chiusura. A questo punto premere F6 per Confermare.

## Chiusure Negozio di Fine Giornata

_Dal Menu>Principale>Chiusure di Cassa>Cassa>Conferma Chiusura di Fine Giornata - Negozio_  : 

Dopo avere effettuato le Chiusure di Cassa di tutti i Registratori utilizzati nella giornata deve essere eseguita la Chiusura Negozio di Fine Giornata.
La funzione richiede la Data di Chiusura e l'indicazione di un Operatore che sia autorizzato all'esecuzione della Chiusura del Negozio (vedi Manuale Gestione Operatori).

- [Gestione Operatori](Sorgenti/MB/DOC_OPE/NGBASE_12)

Prima di proseguire nella elaborazione il programma effettuerà le seguenti verifiche : 

 * Devono essere state effettuate le Chiusure di Cassa di Tutti i Registratori. In caso contrario ne verrà data segnalazione.
 * Devono essere state effettuate le Chiusure del Negozio delle giornate precedenti, altrimenti apparirà una segnalazione
 * Viene effettuato un controllo sulle Registrazioni delle giornate precedenti e se ne esistono di Non Confermate ne verrà data segnalazione con la possibilità di visualizzarne l'elenco (tasto F5)

A questo punto si accede alla funzione di Chiusura Negozio tramite una maschera di riepilogo che riporta l'elenco di tutte le Casse (i Cassetti) del Negozio, indicando lo Stato di ognuna, quindi se Chiusa o Non Utilizzata.
Sulla sinistra viene visualizzata la colonna  che riporta tutte le voci già compilate nella Registrazione della Chiusura siddivise in : 

 * Transazioni
 * Corrispetivi
 * Incassi
 * Riepilogo
 * Cassaforte

Sono a disposizione i seguenti tasti funzionali : 

 * F6 Conferma Chiusura
 * F5 Dettaglio. Per Visualizzare il Dettaglio dei Movimenti di ciascuna tipologia. Posizionarsi sulla cella interessata prima di premere F5
 * F7 Stampa
 * F8 Esporta in Excel

Si potrà visualizzare il Dettaglio dei Movimenti anche facendo il Doppio Clic sulla cella interessata. Premendo F6 se esistono Registratori di Cassa non utilizzati nella giornata ne verrà data
segnalazione con richiesta di Conferma prima di proseguire nell'elaborazione.
Premendo F6, se esistono Registratori di Cassa non utilizzati nella giornata, ne verrà data segnalazione con richiesta di Conferma prima di proseguire nell'elaborazione.
Successivamente verranno richieste le annotazioni della Chiusura del Negozio.
Indicare se la Chiusura è Corretta (SI/NO) e indicare eventuali annotazioni (Obbligatorie in caso di Chiusura Non Corretta)
Premere F6 per terminare la Registrazione della Chiusura Negozio, a questo punto verrà richiesta un'ulteriore Conferma

## Controllo Cassaforte

Prima di poter effettuare i Versamenti in Banca (o a Sede) occorrerà effettuare il Controllo delle Distinte di Cassa (o Buste) presenti in Cassaforte.

_Dal Menu>Principale>Chiusure di Cassa>Cassaforte>Controllo Cassaforte_  : 

All'attivazione del programma viene effettuata la richiesta dell'Operatore che sta effettuando tale Controllo, il quale dovrà essere abilitato a questa funzionalità. Viene visualizzato l'elenco delle Buste  non ancora controllate o non ancora confermate presenti in Cassaforte (in ordine decrescente di Data).
Posizionarsi sulla Busta da controllare, premere Invio e apparirà la Distinta. I valori sono proposti in base al dettaglio specificato in fase di Prelievo per Cassaforte o Chiusura Turno.
Premere Invio per Confermare.
Dopo la Conferma di ogni singola Busta si tornerà all'Elenco delle Buste da Controllare.
Per quelle già controllate verrà evidenziato l'importo Controllato e il nuovo Stato (Controllata).
Le buste Controllate non sono ancora abilitate per il Versamento in Banca (o a Sede). Premere F6 Aggiorna per abilitarle.
Alla conferma sarà possibile effettuare una nuova Stampa delle Distinte di ogni singola Busta. La stampa evidenzierà il Numero della Busta iniziale e il Numero di Busta attribuito in fase di Controllo Cassaforte.

## Registrazione Versamenti in Banca

_Dal Menu>Principale>Chiusure di Cassa>Versamenti>Registrazione Versamenti in Banca_  : 

Le Buste controllate presenti in Cassaforte potranno essere versate in Banca.
All'attivazione del programma viene effettuata la richiesta dell'Operatore che sta effettuando il Versamento in Banca e che, ovviamente, dovrà essere abilitato alla funzione. Se è attiva la Gestione delle Valute verrà richiesto inizialmente di indicare la Valuta per la quale si vuole effettuare il Versamento in Banca.
Se è attiva la Gestione dei Tipi Distinta di Cassa e se esistono più Tipi Distinte per la stessa Valuta,verrà richiesto la selezione del Tipo Distinta per il quale effettuare il Versamento.

N.B.Vengono considerati solo i Tipi Distinta per i quali, nella definizione delle informazioni della Tabella TDSC, è stato specificato Tipo Versamento in Banca.

Se in Configurazione è stato specificato di Bloccare i Versamenti in Banca, in presenza di Buste Non Controllate verrà eseguita tale verifica e, nel caso, ne verrà data segnalazione.
Verrà successivamente presentato l'elenco delle Buste per le quali è possibile effettuare il Versamento in Banca. Premere Invio per Selezionarle/Deselezionarle.
Man mano che si selezionano le Buste, verranno evidenziate con il segno verde di Spunta e verranno visualizzati gli Importi Totali da versare in Banca.
Premere F6 per confermare il Versamento in Banca e procedere alla compilazione della Distinta per il Versamento in Banca
I valori delle Banconote/Monete sono proposti in base alla somma dei dettagli specificati in fase di Controllo Cassaforte.
Premere Invio per Conferma
A conferma avvenuta, se l'importo della Distinta di Cassa non corrisponde all'importo proposto, vengono richieste delle Annotazioni (obbligatorie in questo caso)
Viene infine richiesto quale tipo di Versamento si intende effettuare :  se solo Banconote (F3) oppure Totale (F2), quindi sia Banconote, che Monete.
Nel caso non venga effettuato il versamento delle Monete, per queste ultime verrà creata automaticamente una nuova Busta, già controllata e pronta per un successivo versamento.
Una volta confermato il Versamento sarà possibile stampare la Distinta riepilogativa che sarà utilizzata nel Versamento in Banca.

N.B. Nella Distinta verranno automaticamente stampati i riferimenti Bancari (Banca/Conto Corrente/IBAN) se in Anagrafica di Magazzino è stato specificato il Codice della Tabella BACC - Conti
Correnti Bancari.

## Registrazione Versamenti a Sede

_Dal Menu>Principale>Chiusure di Cassa>Versamenti>Registrazione Versamenti a Sede_  : 

La funzione di Versamento a Sede è del tutto simile alla funzione di Versamenti in Banca.
Questa funzione considererà solo i Tipi Distinta per i quali nella definizione delle informazioni della Tabella TDSC è stato specificato Versamento a Sede.

N.B.Con questa funzione non sarà possibile distinguere nel Versamento tra Banconote e Monete, ma occorrerà sempre fare un versamento totale.


## Controllo Versamenti in Banca

_Dal Menu>Principale>Chiusure di Cassa>Versamenti>Controllo Versamenti in Banca_  : 

Questa funzione consente di controllare i Versamenti in Banca effettuati
All'attivazione della funzione viene effettuata la richiesta dell'Operatore che effettuerà il Controllo e che dovrà chiaramente essere abilitato a questa funzionalità.
Dopo la richiesta dell'operatore verranno visualizzati i versamenti in Banca non ancora controllati
Premendo Invio si procede al Controllo del Versamento, con la possibilità di confermarne l'importo Effettivo o modificarlo e di indicare eventuali annotazioni
Premere F6 per Confermare.

Nella maschera iniziale del Controllo Versamenti saranno inoltre disponibili i seguenti tasti funzionali : 

 * F8 Allega Ricevuta. Per allegare al versamento l'immagine della ricevuta rilasciata dalla Banca
 * F9 Visualizza Ricevuta. Per visualizzare l'eventuale ricevuta allegata mediante la funzione precedente
 * F10 Visualizza Tutti i Versamenti. Permette di passare dalla Visualizzazione dei soli Versamenti da Controllare alla Visualizzazione di tutti i Versamenti e viceversa

## Come Allegare una Ricevuta

Dopo aver premuto il tasto F8 Allega Ricevuta si apre una finestra che richiederà : 

 * Tipo. E' opportuno aver prima codificato il Tipo di Ricevuta nella Tabella ARTD - Tipo Documento di Archiviazione
 * Data
 * Numero
 * Descrizione

A questo punto premere F11 Scansione Ricevuta e, al termine dell'operazione, premere F9 Allega Ricevuta

## Analisi Versamenti in Banca

_Dal Menu>Principale>Chiusure di Cassa>Versamenti>Analisi Versamenti in Banca_  : 

Questa funzione permette di analizzare i Versamenti in Banca effettuati dai Negozi.
Viene inizialmente richiesto di indicare il Codice del Negozio e il Periodo da analizzare. Dopo le selezioni iniziali viene presentato l'elenco dei versamenti effettuati dal Negozio nel periodo
Premere F7 per stamparlo oppure F8 per Esportarlo in Excel.

## Visualizzazione Distinte di Cassa

Questa funzione permette di Visualizzare tutte le Distinte di Cassa registrate.

_Dal Menu>Principale>Chiusure di Cassa>Cassa>Visualizza Distinte di Cassa_  : 

Verranno richiesti : 

 * Negozio
 * Registratore di cassa
 * Codice Cassa
 * Tipologia. E' possibile scegliere tra
 ** Apertura Turno - Controllo Fondo Cassa
 ** Chiusura Turno - Controllo Fondo Cassa
 ** Chiusura Turno - Prelievo per Cassaforte
 ** Controllo Cassaforte
 ** Prelievi per Cassaforte
 ** Versamento in Banca
 ** Versamento a Sede
 * Operatore
 * Da Data/A Data

Tutti i valori sono facoltativi, se non ne viene indicato nessuno, verrà presentata la maschera con tutte le Distinte presenti a sistema

 :  :  T02 Gestione Chiusure in Cassa

Nell'utilizzo del Programma di Cassa è possibile definire dei Bottoni per le funzioni relative alle Chiusure di Cassa.
A differenza delle medesime funzioni utilizzate nel Menù di Negoziando, però, il Programma di Cassa utilizza le informazioni conosciute (Operatore, Cassa ecc ... ) e non ne effettuerà la richiesta.

## Apertura Turno

Per questa funzionalità non è necessario nessun Bottone di Cassa.
All'attivazione del Programma, dopo l'indicazione iniziale dell'operatore (se la Gestione Operatori è attiva), viene verificato automaticamente se è necessario effettuare l'apertura del Turno.
 In questo caso apparirà la finestra di Dichiarazione del Fondo Cassa Iniziale
Confermare l'importo, se corretto, oppure premere F2 Modifica Fondo Cassa e compilare la Distinta di Cassa.

## Prelievi per Cassaforte

Per attivare questa funzionalità dal programma di Cassa è necessario attivare un Bottone con la caratteristica FCode="WITHDRAWFORSAFE"
Alla pressione del Bottone verrà richiesto se indicare il Codice Valuta (se la Gestione Valute è attiva)
L'operatività proseguirà successivamente come nell'utilizzo della funzione da Menu (Richiesta Tipo Distinta etc...)
In base alle impostazioni della Configurazione (Parametri Cassa - Generali) il programma di Cassa effettua controlli periodici sull'importo dei Contanti del Cassetto.
Se viene raggiunto il limite specificato in configurazione appare una notifica che segnala il raggiungimento del Limite dei Contanti nel Cassetto e proporrà l'Importo da versare calcolato in base alle informazioni definite in Configurazione (i valori sono arrotondati al Taglio minimo delle Banconote)
Sarà possibile utilizzare il tasto F6 per effettuare immediatamente il Prelievo per Cassaforte

## Chiusura Turno

Per attivare questa funzionalità dal programma di Cassa è necessario attivare un Bottone con la caratteristica FCode="SHIFTCLOSURE"
Rispetto alla funzione eseguita dal Menu di Negoziando non verranno richieste le informazioni iniziali, ma occorrerà procedere alla compilazione delle varie Distinte di Cassa (Fondo Cassa, Prelievi
per Cassaforte divisi per Valuta e Tipo Distinta, etc...).
Al termine della Chiusura Turno il programma di Cassa si Blocca automaticamente. Se la Chiusura turno è effettuata dall'ultimo Operatore della giornata e se in cassa non è disponibile la funzionalità di Chiusura Cassa, premere F4 per uscire dal programma. Altrimenti sarà l'operatore successivo che premerà il tasto F8 Sblocca e al quale verranno a questo punto richieste le informazioni di Apertura Turno.

## Registrazione Chiusure di Cassa

Per attivare questa funzionalità dal programma di Cassa è necessario attivare un Bottone con le caratteristiche FCode="INTFUN" FAttr="REGCHIUSURA"
L'operatore di fine giornata che deve eseguire questa funzione può anche non effettuare la Chiusura Turno tramite l'apposito tasto, perchè all'attivazione di questa funzione il programma verifica se è stata effettuata la Chiusura o meno e, se non effettuata, la richiede.
L'operatività poi prosegue come nella funzione eseguita da Menu.

## Registrazione Versamenti in Banca

Per attivare questa funzionalità dal programma di Cassa è necessario attivare un Bottone con le caratteristiche FCode="INTFUN" FAttr="REGVERBANCA"
L'operatività è esattamente identica alla funzione eseguita dal Menu di Negoziando.

## Registrazione Versamenti a Sede

Per attivare questa funzionalità dal programma di Cassa è necessario attivare un Bottone con le caratteristiche FCode="INTFUN" FAttr="REGVERSEDE"
L'operatività è esattamente identica alla funzione eseguita dal Menu di Negoziando.

## Conferma Registrazione Entrate/Uscite di Cassa

Per attivare questa funzionalità dal programma di Cassa è necessario attivare un Bottone con le caratteristiche FCode="INTFUN" FAttr="CNFREGSPESE"
Rispetto alla funzione eseguita da Menù non vengono richiesti il Codice del Registratore e la Data, ma si accede direttamente all'elenco delle Entrate/Uscite di Cassa della giornata.
Per le altre funzionalità descritte in questo Manuale non è prevista la possibilità di definire Bottoni specifici nel Programma di Cassa.
E' comunque sempre possibile definire dei Bottoni che richiamano la specifiche funzionalità mediante il FCode='EXTFUN'



