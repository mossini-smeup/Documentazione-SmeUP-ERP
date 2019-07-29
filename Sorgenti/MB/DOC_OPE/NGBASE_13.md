# Gestione Promozioni di Cassa

## Gestione Promozioni di Cassa

Negoziando è dotato di un motore che rende possibile gestire Promozioni di Cassa articolate e complesse.

Le Promozioni consentono alla Sede centrale o al singolo PV di creare delle situazioni di vendita che permettono al cliente di beneficiare di Sconti, di Omaggi o di Buoni acquisto, sia nello scontrino corrente che in acquisti successivi. Possono generarsi con un singolo scontrino oppure maturare tenendo conto dello storico cliente. Le Promozioni possono essere cumulative (es. uno sconto e un omaggio) ed è inoltre possibile applicarle secondo ordini prestabiliti (es. prima lo sconto percentuale, poi, se sussistono ancora le condizioni, quello a valore).

Il programma verifica con la pressione del tasto Subtotale della Cassa quali siano le promozioni applicabili in base allo scontrino corrente e propone eventualmente il premio (o i premi) a cui il cliente ha diritto.

Le Promozioni vanno programmate impostando : 


-  La condizione che fa scattare il beneficio. Ci sono 2 categorie di eventi : 
-- Promozione a Quantità :  il cliente acquista un numero predeterminato di articoli appartententi a una lista
-- Promozione a Importo :  il cliente raggiunge di una soglia di spesa

- Gli articoli (i gruppi) che concorrono come quantità o come importo al raggiungimento della condizione

- Il tipo di beneficio
-- Prezzo Fisso Complessivo :  il Prezzo di Vendita complessivo degli articoli è di importo prefissato. Questa Promozione è valida solo nel caso di Promozioni a Quantità.
-- Sconto in Percentuale :  viene applicato un sconto in percentuale prefissato su tutti gli articoli appartenenti alla promozione o su tutti gli articoli dello Scontrino.
-- Sconto a Valore :  viene applicato uno Sconto fisso al totale dello scontrino
-- Sconto Percentuale/a Valore Articolo Meno Costoso :  sull'articolo (o più articoli) meno costoso dello scontrino corrente viene applicato uno Sconto in percentuale o a Valore
-- Prezzo Fisso su Articolo Meno Costoso :  all'articolo (o più articoli) Meno Costoso dello scontrino viene applicato un prezzo fisso (indicando prezzo a zero, l'articolo è dato in Omaggio)
-- Prezzo Fisso Unitario :  viene applicato un Prezzo di Vendita prefissato a ciascun articolo della promozione
-- Articolo a Prezzo Speciale :  possibilità di acquistare un articolo appartenente ad un certo gruppo ad un prezzo ridotto (indicando prezzo a zero, l'articolo è dato in Omaggio)
-- Articolo a Sconto Speciale :  possibilità di acquistare un articolo appartenente ad un certo gruppo ad un prezzo scontato in percentuale
-- Prezzo Fisso Unitario :  il Prezzo di Vendita di ciascun articolo della Promozione è di importo ridotto rispetto al prezzo di listino vendita
-- Bonus Punti Fidelity :  vengono attribuiti Punti addizionali al cliente fidelizzato
-- Emissione Buoni di Cassa :  generazione di un Buono Acquisto da utilizzare per ulteriori acquisti
- Il periodo entro cui il raggiungimento della condizione fa scattare la promozione :  è possibile impostare periodi di giorni/mesi continuativi ma anche selezionare solo particolari giorni della settimana o fasce orarie
- La tipologia di cliente che può accedere alla promozione (tutti, solo fidelizzati, gruppi predefiniti, ecc.)


## Gestione Eventi

Come prima cosa occorre definire gli Eventi a cui collegare le Promozioni. Un Evento definisce QUANDO la Promozione è attiva e CHI ne può usufruire. A ciascun evento possono essere associate più Promozioni

Dal Menu _Principale>Gestione Promozioni di Cassa>Gestione Eventi_
Attivando la funzione di Menù viene visualizzato l'elenco degli Eventi esistenti. In basso sono a disposizione i tasti funzionali : 

 * Invio :  per Modificare le impostazioni di un Evento
 * F6 :  per Inserire un nuovo Evento
 * F4 :  per Annullare
 * F8 :  per definire Eventuali Elenchi di Clienti Fidelity che potranno utilizzare la promozione (vedi _Principale>Fidelity Card> Configurazione>Gestione Gruppi Fidelity_)
Premere F6 per definire un nuovo evento, definire un Codice, quindi attribuire il nome all'evento e confermare
A questo punto verranno richiesti : 

 * Descrizione
 * Applicabilità :  tutti i Clienti o Solo Clienti Fidelizzati
 * Codice Gruppo Clienti Fidelity :  Indicare questo valore se si intende limitare l'utilizzo delle promozioni associate a questo evento solo a Clienti Fidelity appartenenti al gruppo Indicato (vedi note successive Gestione Elenchi Clienti Fidelity per Eventi).
 * Giorni della settimana :  utilizzare i flag per abilitare la Promozione solo alcuni giorni della settimana.
 * Ora di Inizio e Ora di Fine Promozione :  compilare i capi per restringere la validità della Promozione a una fascia oraria; lasciare in bianco Ora di Inizio e indicare 23 : 59 come Ora di Fine se non si intendono porre limiti di orario.
 * Orari Specifici per Giorni della Settimana :  nel secondo pannello è possibile eventualmente definire Orari specifici di Inizio/Fine Promozione validi solo per il Giorno della settimana indicato.Se i valori specifici del giorno non vengono definiti, valgono quelli impostati nel primo pannello.

## Gestione Elenchi Clienti Fidelity per Eventi

Tramite il tasto F8 nella Gestione degli Eventi è possibile associare gli Elenchi di Clienti Fidelity che potranno utilizzare la promozione.
Questi Elenchi potranno essere definitivi solo se l'evento selezionato è applicabile unicamente a Clienti Fidelizzati.
Dal Menu>_Principale>Anagrafiche di Base>Gestione Elenchi/Composizioni_ per creare un nuovo elenco di Clienti Fidelity
Premendo il tasto F8 verrà visualizzato l'elenco degli Elenchi associati all'Evento
Premere F6 per inserire un nuovo Elenco o F4 per cancellarne uno esistente.

N.B. In Cassa le promozioni applicabili Solo a Clienti Fidelity scatteranno solo con lettura in cassa della Tessera Fidelity e se si verifica una delle due seguenti condizioni : 
 * non vengono effettuate selezioni sulle tessere Fidelity, ovvero nella definizione dell'Evento non viene associato nessun Elenco Fidelity (accessibile tramite il tasto F8 dalla lista degli Eventi) e nessun Gruppo Fidelity (impostato nella scheda di ogni singolo Evento).
 * la Tessera appartiene al Gruppo Fidelity indicato o è presente in uno degli Elenchi associati.
Attenzione :  nel caso in cui sia definito un Gruppo Fidelity, viene controllata solamente l'appartenenza della tessera al Gruppo, eventuali Elenchi associati verranno ignorati.

## Gestione Gruppi Promozioni

E' possibile che un articolo (o un gruppo di articoli) concorra a più di una Promozione e che queste Promozioni siano attive nello stesso periodo per gli stessi clienti. Negoziando prepara una lista delle Promozioni attive e controlla l'applicabilità di tutte separatamente, eventualmente con una priorità. Tramite la gestione dei Gruppi Promozione, però, possiamo modificare questo comportamento e decidere se la lista delle Promozioni vada applicata tutta e in quale ordine, oppure di interrompere la scansione della lista dopo l'applicazione di una Promozione.
Ad esempio, ipotizziamo che l'articolo X appartenga ad una promozione A che genera uno sconto a tutti i clienti e ad un'altra B in cui l'articolo genera dei punti Bonus ai clienti Fidelizzati. Supponiamo inoltre che le Promozioni A e B siano attive contemporaneamente e che la priorità di A sia maggiore di quella di B. Possiamo far si che il programma scelga uno tra i seguenti comportamenti : 
 * al cliente fidelizzato vengono applicate entrambe le Promozioni. Al cliente generico solo la A;
 * a tutti i clienti, fidelizzati o no, viene applicata solo la A;
 * al cliente fidelizzato viene applicata la B e al cliente generico la A.
Per riunire singole Promozioni all'interno di un Gruppo occorre definire la Tabella dei Gruppi di Promozioni.
Dal Menu _Principale>Gestione Promozioni di Cassa>Gestione Gruppi Promozioni_
Attivando la funzione di Menù vengono visualizzati i Gruppi Promozioni esistenti. Premendo il tasto F6 sarà possibile inserire un Nuovo Gruppo, definire il Codice del Gruppo e la sua Descrizione e confermare.
La selezione del comportamento descritto sopra viene definito all'interno della scheda della Promozione (vedi Gestione Promozioni)

## Gestione Promozioni

Una volta creato l'evento, sarà possibile definire la/e promozione/i associate.
Dal Menu _Principale>Gestione Promozioni di Cassa>Gestione Promozioni di Cassa_
Attivando la funzione di Menù viene visualizzato l'elenco delle Promozioni esistenti
Sono a disposizione i tasti funzionali : 

 * Invio :  per modificare le impostazioni di una Promozione
 * F6 :  per inserire una Nuova Promozione
 * F4 :  per Annullare una Promozione
 * F8 :  per modificare la composizione (gruppo Articoli) di una Promozione

Premendo F6 è possibile definire una nuova Promozione. In questa scheda definiamo COSA fa scattare una Promozione e COME si comporta in termini di vantaggi per il cliente. Attribuiamo un Codice e confermiamo. Apparirà la maschera di richiesta informazioni della Promozione (prima Parte).
Definiamo le informazioni base : 

 * Descrizione :  un semplice campo mnemonico
 * Modalità Promozione : 
 ** Quantità = la Promozione scatta in seguito a conteggi sui pezzi acquistati
 ** Importi = la Promozione scatta in seguito a importi spesi
 * Tipo di Ricorsione : 
 ** Ricorsiva= ogni N pezzi acquistati (se a Quantità) oppure ogni X euro di spesa (se a Importo) la promozione si ripete (es. se OGNI 3 pz viene dato un omaggio, con 3 pz viene consegnato appunto un omaggio, con 6 pz 2 omaggi e cosi via)
 ** Non Ricorsiva= all'acquisto di almeno N pezzi (se a Quantità) o al di sopra di un certo importo di spesa (se a Importo), quindi al raggiungimento di una soglia e solo una volta all'interno dello scontrino (es. se con ALMENO 20 euro di spesa viene dato un omaggio, uno e un solo omaggio viene consegnato sia per una spesa di 20 che di 100 euro)
 * Tipo di Promozione. Già anticipate nell'introduzione, le riportiamo per comodità
 ** Prezzo Fisso Complessivo :  il Prezzo di Vendita complessivo degli articoli sarà di importo prefissato. Questa Promozione è valida solo nel caso di Promozioni a Quantità.
 ** Sconto in Percentuale :  viene applicato un sconto in percentuale prefissata su tutti gli articoli appartenenti alla promozione o su tutti gli articoli dello Scontrino.
 ** Sconto a Valore :  viene applicato uno Sconto fisso al totale dello scontrino
 ** Sconto Percentuale Articolo Meno Costoso :  sull'articolo meno costoso dello scontrino corrente verrà applicato uno Sconto in percentuale
 ** Sconto a Valore Articolo Meno Costoso :  sull'articolo meno costoso dello scontrino corrente viene applicato uno sconto fisso
 ** Prezzo Fisso su Articolo Meno Costoso :  all'articolo Meno Costoso dello scontrino viene applicato un prezzo fisso (indicando prezzo a zero, l'articolo sarà dato in Omaggio)
 ** Prezzo Fisso Unitario :  viene applicato un Prezzo di Vendita prefissato a ciascun articolo della promozione
 ** Articolo a Prezzo Speciale :  possibilità di acquistare un articolo appartenente ad un certo gruppo ad un prezzo ridotto (indicando prezzo a zero, l'articolo sarà dato in Omaggio)
 ** Articolo a Sconto Speciale :  possibilità di acquistare un articolo appartenente ad un certo gruppo ad un prezzo scontato in percentuale
 ** Prezzo Fisso Unitario :  il Prezzo di Vendita di ciascun articolo della promozione è di importo ridotto rispetto al prezzo di listino vendita
 ** Bonus Punti Fidelity :  vengono attribuiti Punti addizionali al cliente fidelizzato
 ** Emissione Buoni di Cassa :  generazione di un Buono Acquisto da utilizzare per ulteriori acquisti
* Evidenzia Sconto su Scontrino :  indicare No se non si desidera Stampare lo Sconto sullo Scontrino,in questo caso verrà diminuito direttamente il Prezzo della riga
 * Eventuale Descrizione per Scontrino :  inserire una descrizione che verrà stampata sullo scontrino
 * Priorità Promozione :  verrà eventualmente utilizzata dal Programma di Cassa nel caso in cui con gli Articoli dello Scontrino sia possibile comporre più Promozioni per stabilire quale applicare per prima. A priorità più alta corrisponde la precedenza di applicazione. Se tra due o più Promozioni la priorità è identica o se non viene indicata, Negoziando propone una finestra pop up da cui selezionare una delle Promozioni.
 * Promozione Abilitata : indica se la Promozione é abilitata o meno. Ricordiamo che la Promozione deve anche essere attivata in un Evento in corso.

Definiamo le informazioni per limitare l'utilizzo, ovvero per fissare il numero massimo di volte che la Promozione può scattare. Vediamo il dettaglio : 
 * Numero Massimo Utilizzi nello Scontrino :  in caso di Promozioni con Tipo Promozione = Ricorsiva, permette di decidere quante volte far scattare la promozione all'interno dello stesso scontrino.
 * Tipo Limitazione :  le limitazioni possono essere : 
 ** per Tutti i Negozi :  le condizioni che determinano lo scattare della Promozione vengono conteggiate in tutti i Negozi della catena (es. raggiungimento di un limite di spesa). Attenzione, in questo caso occorre attivare in Cassa i Servizi On Line.  (vedi capitolo)
 ** per il Singolo Negozio :  la Promozione in un PV scatta sulla base degli acquisti fatto nel negozio stesso.
 ** per il Singolo Cliente (in Tutti i Negozi) : la Promozione scatta sulla base degli acquisti fatti nell'intera catena da una singola Tessera Fidelity.
 ** per il Singolo Cliente (nel Singolo Negozio) : la Promozione in un PV scatta sulla base degli acquisti fatti nel negozio stesso dallo stesso cliente fidelizzato.
 ** Nessuna Limitazione : la Promozione scatterà indipendentemente dal numero di volte in cui è già scattata precedentemente.
 * Periodo Utilizzo :  formula per determinare la Data Iniziale dalla quale cominciare il Controllo sul Numero di Utilizzi Complessivi (vedi campo)
 ** T02 Creazione Formula per Calcolo Data : 
 * Numero Massimo Utilizzi Complessivi : è possibile definire il numero di volte in cui la Promozione può scattare o in termini assoluti o relativamente a un periodo.
In termini assoluti è sufficiente compilare il campo col numero desiderato lasciando vuoto il Periodo di utilizzo :  ad esempio inserendo 3 nel campo la Promozione scatterà al massimo 3 volte nell'Evento.
Se intendiamo invece far scattare la Promozione una volta al mese o solo dopo 7 giorni dalla volta precedente bisogna combinare il numero di Numero Massimo con il campo Periodo Utilizzo. Per l'impostazione di questo campo consultare il link  (Calcolo data)
Questo campo è anche abbinato al Tipo Limitazione :  supponiamo di impostare il valore 1 nel campo Numero massimi complessivi. Il comportamento con Tipo limitazione sarà il seguente : 
 * per Tutti i Negozi :  la Promozione scatterà solo una volta in tutta la Catena (col primo scontrino che raggiunge la condizione)
 * per il Singolo Negozio :  la Promozione scatterà solo una volta in ogni negozio
 * per il Singolo Cliente (in Tutti i Negozi) :  la Promozione scatterà solo una volta nella Catena per ogni Tessera Fidelity.
 * per il Singolo Cliente (nel Singolo Negozio) :  la Promozione scatterà una volta in ogni negozio per ogni Tessera Fidelity
 * Nessuna Limitazione :  la Promozione scatterà sempre, ignorando il valore del campo Numero Massimi Utilizzo

Definiamo le eventuali Informazioni che permettono la Cumulabilità tra le Promozioni : 
 * Codice Gruppo Promozioni :  obbligatorio se si intende gestire la Cumulabilità
 * Cumulabile all'Interno del Gruppo :  indicando SI potranno essere utilizzati per questa Promozione anche eventuali Articoli già utilizzati per altre Promozioni dello stesso Gruppo.
 * Cumulabile all'Esterno del Gruppo :  indicando SI potranno essere utilizzati per questa Promozione eventuali Articoli già utilizzati per altre Promozioni Non appartenenti allo stesso Gruppo.
 * Applica ulteriori Promozioni :  con questa richiesta è possibile interrompere l'utilizzo degli Articoli compresi nella Promozione per le promozioni successive. I Valori ammessi sono : 
 ** Si :  si potrà continuare a usare gli articoli per altre promozioni
 ** Interrompi Gruppo :  gli Articoli Non potranno più essere utilizzati per Promo dello Stesso Gruppo
 ** Interrompi Altri Gruppi :  gli Articoli Non potranno più essere utilizzati per Promo di Altri Gruppi
 ** Interrompi Tutto :  gli Articoli Non potranno più essere Utilizzati per altre Promo
 * Modalità Calcolo Soglia Importi : determina se la base di calcolo per determinare l'applicabilità di una Promozione è : 
 ** Lordo Sconti : sempre il prezzo di partenza
 ** Netto Sconti :  il prezzo già ridotto da un'altra Promozione applicata
N.B. :  Nel caso di cumulo di due o più Promozioni, il campo Modalità Calcolo Soglia Importi applica il valore Netto Sconto alle promozioni successive alla prima solo nel caso di Promo sconto a Valore. Nel caso di sconto in percentuale viene sempre applicato al valore Lordo sconto.

Definiamo le eventuali Informazioni di Validità : 
 * Valida se Lettura Buono con Causale :  se specificato Codice Causale la Promozione sarà Valida solo nel caso in cui nello Scontrino sia stato registrato l'utilizzo di un Buono con la stessa Causale indicata.
 * Buono Riutilizzabile nello Scontrino :  se sono attive due o più Promozioni che scattano con validità Buono con la stessa Causale (vedi campo precedente), impostando a SI le Promozioni scattano in contemporanea, con NO scatta solo 1 Promo. Per far scattare le successive bisogna leggere un altro Buono della stessa Causale.
 * Valida se Utilizzato Incasso di Tipo :  se specificato Codice Incasso la Promozione sarà Valida solo nel caso in cui nello Scontrino venga utilizzato l'Incasso indicato. Dato che la Promozione viene rilevata al momento della pressione del tasto SubTotale e ancora non è stata definita quale sarà la modalità di pagamento, Negoziando mostra la seguente finestra di avviso : 

![WARNINGMODPAG](http://localhost:3000/immagini/MBDOC_OPE-NGBASE_13/WARNINGMODPAG.png)
Quindi premere F6 Conferma se il cliente paga con la modalità necessaria per usufruire della Promozione o Esc se il cliente declina l'offerta.

Premiamo Invio per confermare e accediamo alla scheda successiva dove ci vengono richieste ulteriori informazioni  a seconda del Tipo di Promozione specificato : 

 * In caso di Promozioni a Prezzo Fisso Complessivo o Prezzo Fisso su Articolo Meno Costoso verrà richiesto tale Prezzo con la possibilità, nel caso di Prezzo Fisso su Articolo Meno Costoso, di lasciarlo a zero per dare l'articolo in Omaggio.Per Prezzo Fisso su Articolo Meno Costoso viene anche chiesto di indicare il numero di Articoli a cui verrà applicato il prezzo ridotto.
 * in caso di Promozioni a Sconto in Percentuale o Sconto in Percentuale Articolo Meno Costoso viene richiesta la percentuale di Sconto da utilizzare.Nel caso di Promozioni a Sconto in Percentuale verrà richiesto inoltre di indicare come calcolare lo Sconto. Le selezioni possibili sono : 
 ** Su Articoli della Promozione - Prezzi in Vigore, ovvero lo sconto viene applicato solo agli articoli della Promozione utilizzando come base da scontare il prezzo riportato nello scontrino, anche se questo fosse già un prezzo promozionale
 ** Su Articoli della Promozione - Prezzi in Vigore Non Promozionali, ovvero lo sconto viene applicato solo sugli articoli della Promozione utilizzando come base il prezzo del listino di vendita, quindi al lordo di eventuali prezzi promozionali già applicati
 ** Su Tutto lo Scontrino, cioè su tutti gli articoli inseriti nello scontrino appartenenti o meno alla Promozione.
  Viene anche richiesto come arrotondare l'importo. Per Sconto in Percentuale Articolo Meno Costoso viene anche chiesto di indicare il numero di Articoli a cui verrà applicato il prezzo scontato.
 * In caso di Promozioni a Sconto a Valore o Sconto a Valore Articolo Meno Costoso viene richiesto l'Importo dello Sconto.Per Sconto a Valore Articolo Meno Costoso viene anche chiesto di indicare il numero di Articoli a cui verrà applicato il prezzo ridotto.
 * Nel caso di Promozioni a Sconto a Valore verrà richiesto dove applicare lo Sconto indicato. Le selezioni possibili sono : 
 ** Su Articoli della Promozione
 ** Su Tutto lo Scontrino
 * Per le Promozioni Articolo a Prezzo Speciale o Articolo con Sconto Speciale viene richiesto il Gruppo Articoli (tra cui dovrà essere selezionato l'Articolo da vendere a prezzo speciale) e il Prezzo
o lo Sconto da attribuire a tale articolo. Viene anche richiesto se Ricercare Articolo a Prezzo Speciale nello Scontrino : 
 ** SI (di default) :  se il sistema trova un articolo in promozione all'interno dello scontrino, in automatico attribuirà il prezzo scontato a quell'articolo
 ** NO  :  il programma NON effettua la ricerca di un articolo del Gruppo nello Scontrino  a cui applicare lo Sconto, ma richiede sempre l'indicazione di un Nuovo Articolo che verrà aggiunto con il relativo sconto.
 * Per le Promozioni a Prezzo Fisso Unitario verrà richiesto di indicare tale Prezzo.
 * Per le Promozioni a Bonus Punti Fidelity viene richiesto il Numero dei Punti addizionali da attribuire.
 * Per le Promozioni per Emissione Buoni viene richiesto il Codice Regola per l'emissione e il Numero di Buoni da Emettere.Per Definire le Regole per Emissione Buoni utilizzare la funzione specifica
Dal Menu _Principale>Registratori di Cassa>Buoni/Acconti>Regole per Generazione Buoni_ (vedi inoltre manuale di Gestione Buoni di Cassa)

A questo punto inseriamo i valori necessari e confermiamo.

Dopo aver definito le informazioni di Testata della Promozione, oppure premendo F8=Gestione Righe Promozione nell'elenco iniziale di Promozioni, si accede alla lista dei gruppi di Articoli il cui acquisto è necessario allo scatto della Promozione. Gli Elenchi si gestiscono dal Menu _Principale>Anagrafiche di Base>Gestione Elenchi e Composizioni_
Ogni Elenco contiene una serie di articoli che concorrono con la quantità o con l'importo al raggiungimento della Promozione. Affinché la Promozione scatti, il cliente dovrà acquistare articoli che soddisfino la condizione di ogni elenco.
Sono a disposizione i normali tasti funzionali : 
 * Invio :  per modificare le impostazioni dell'Elenco di Articoli (non il contenuto)
* F6  :  per inserire un nuovo Elenco di Articoli
* F4 :  per Annullare l'associazione dell'elenco di Articoli alla Promozione

Premendo uno dei tasti funzionali si accede alla videata di richiesta informazioni del Gruppo Articoli della Promozione. Specificare : 
* Codice Elenco :  il gruppo a cui appartengono gli articoli che fanno scattare la Promozione
* Quantità / Importo (la scelta dipende dalla Modalità Promozione) :  quantità o importo di tali articoli necessaria per l'attivazione.
* Escludi Articoli con Prezzi in Vigore Promozionali :  indicare se gli articoli aventi un prezzo di listino promozionale devono essere inclusi nell'elenco.
Facciamo un esempio :  intendiamo attivare una Promozione che scatta all'acquisto di un rossetto di due mascara. Prima di compilare i dati della Promozione avremo quindi predisposto 2 elenchi distinti :  nel primo avremo inserito il rossetto e nel secondo il mascara. Nella scheda Promozione li abbineremo entrambi alla Promozione con quantità 1 per il primo e 2 per il secondo.

## Gestione Listini di Vendita Promozioni

Dal Menu _Principale>Gestione Promozioni di Cassa>Gestione Listini Vendita Promozioni di Cassa_

Questa funzione è utilizzabile per le promozioni di tipo : 

 * Prezzo Fisso Complessivo
 * Prezzo Fisso
 * Articolo Meno Costoso
 * Articolo a Prezzo Speciale
e permette di differenziare il Prezzo di Vendita della Promozione a seconda dei Listini utilizzati nel Negozio.
Es. il prezzo della Promozione che sto configurando potrebbe essere di 25,00 ¤ per i negozi che utilizzano il listino 001 e di 30,00 ¤ per quelli che utilizzano lo 006
Per creare un Listino di Vendita : 
dal Menu _Principale>Anagrafiche di Base>Listini di Vendita>Generazione Listini di Vendita_ (vedi capitolo Generazione Listini di Vendita)

Sono a disposizione i normali tasti di Negoziando per Inserimento/Modifica/Annullamento.
Premendo uno dei tasti funzionali si accede alla videata nella quale occorre specificare : 

 * Codice Listino
 * Codice Promozione
 * Prezzo

## Associazione Eventi Promozioni

Una volta definiti gli Eventi e le Promozioni (ed eventuali Listini di vendita delle promozioni) occorre definire l'Associazione tra gli stessi. Con questa funzione definiamo DOVE e QUANDO la Promozione è attiva.
Dal Menu _Principale>Gestione Promozioni di Cassa>Associa Eventi/Promozioni/Negozi_
La griglia mostra gli abbinamenti già effettuati.
Sono a disposizione i normali tasti di Negoziando per Inserimento/Modifica/Annullamento. Premendone uno si accede alla videata di dettaglio nella quale vengono richiesti : 

 * Codice Evento
 * Codice Promozione
 * Codice Negozio, Codice Società, Codice Elenco di Negozi :   sono informazioni facoltative e servono a limitare l'utilizzo della Promozione solo in alcuni Negozi in base appunto al Codice Negozio, alla Società a cui appartiene il Negozio, al fatto che il Negozio sia inserito nell'elenco dato.
N.B. Lasciare in bianco questi 3 campi se si intende attivare la Promozione su tutti i Negozi
 * Data di Inizio Validità della Promozione
 * Data di Fine Validità della Promozione

## Configurazione applicativa

Per attivare le Promozioni in Cassa è necessario impostare l'apposita richiesta nella Configurazione di Negoziando
Dal Menu _Utilità>Configurazione>Configurazione Applicativa>Cassa-Generali_
Impostare a SI la richiesta di Gestione Promozioni di Cassa

## Utilizzo Promozioni in Cassa

Per utilizzare le Promozioni in Cassa occorre inizialmente leggere gli Articoli in Vendita per il Cliente
Una volta effettuata la lettura degli Articoli, alla pressione del tasto di SubTotale, Negoziando verificherà se con gli Articoli compresi nello Scontrino è possibile comporre una Promozione e applicherà Sconti/Prezzi Speciali in base alle definizioni effettuate.
N.B.Questo discorso vale per tutte le promozioni ad eccezione delle promo Articoli a Prezzo Speciale, per Emissione Buoni e Punti Bonus Fidelity

Sme.UP
Last Rev18/03/2016
