# C56 - Impostazioni base Controllo fatture
 :  : DEC T(ST) K(C56)
## OBIETTIVO
Definisce i parametri generali di impostazione per i programmi di Controllo fatture
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM **Elemento**
È un elemento fisso.
 :  : FLD T$C56A  **Funzioni iniziali immissione**
Controlla la gestione iniziale di immissione registrazione : 
- ' ' Nessuna impostazione (se presente una parzializzazione di default verranno proposti in attesa solo i dati richiesti).
- '1' Assume tutti i dati presenti già impostati in pagamento (se presente una parzializzione di default verranno proposti solo i dati scelti).
- '2' Presenta prima del controllo la finestra di parzializzazione (se presente una parzializzione di default a video verrà proposta la parzializzazione).
- '3' Presenta prima del controllo la finestra di parzializzazione. Tutto ciò che risulta scelto verrrà proposto in pagamento (se presente una parzializzione di default a video verrà proposta la parzializzazione)
- '4' Non presenta il controllo ma la finestra di immissione documenti della fattura (fonte £06). La merce viene abbinata al conto presente nella fonte £06 (Conto ingresso). NON ATTIVA PER NOTA ACCREDITO
- '5' Prima del controllo presenta la finestra di immissione documenti della fattura e successivamente propone l'abbinamento con i documenti effettivi in attesa. Se non trovati crea il mancante.
 :  : FLD T$C56B  **Solo righe validate**
Se valorizzato, verranno caricate in attesa di pagamento solo quelle righe di fonte che sono state precedentemente validate. (Nel caso di
fonti std V5 la validazione è identificata dal FL24="0"). Una funzione apposita gestisce la validazione delle fonti.(Nel caso di fonti std V5 passaggio FL24 da " " a "0" e viceversa).
 :  : FLD T$C56C  **IVA da fonti utente**
Se valorizzato il codice IVA viene ripreso dalla fonte utente
 :  : FLD T$C56D  **Conto Omaggi (facoltativo)**
È il conto contabile di storno nella gestione "OMAGGI". Se non indicato viene assunto il conto della merce.
 :  : FLD T$C56E  **Modifica fonte utente**
Indica la modalità di modifica dati fonte utente : 
- ' ' Quantità e prezzo non modificabile.
- '1' È possibile modificare solo il prezzo.
- '2' È possibile modificare prezzo e quantità.
- '3' È possibile modificare prezzo, quantità e permette di entrare in modifica direttamente sulla fonte origine.
 :  : FLD T$C56Q  **Codice blocco pagamento 1**
È il codice di blocco pagamento che viene assunto se si utilizza la funzione di immissione '4', ovvero se si decide di effettuare la registrazione delle fatture e successivamente il controllo delle bolle. In questo caso nel momento i cui vengono registrate le fatture vengono registrati solamente il numero e la data del documento di riferimento e le rate vengono bloccate fino al controllo delle bolle. Blocco amministrativo.
 :  : FLD T$C56F  **Codice blocco pagamento 2**
È il codice di blocco pagamento che viene assunto se presente una non conformità nella registrazione della fattura. Blocco gestionale.
 :  : FLD T$C56G  **Codice blocco pagamento 3**
È il codice di blocco pagamento che viene assunto quando si procede allo sblocco del codice blocco 2. Con questa gestione nel momento in cui si sblocca una rata che era stata bloccataa a causa della presenza di una non conformità, la rata non viene completamente sbloccata ma resta bloccata con il codice blocco presente in questo campo. Blocco conferma.
 :  : FLD T$C56H  **Tipo registrazione giroconto mancanti**
È il tipo di registrazione usato nella registrazione del giroconto per la chiusura dei mancanti.
 :  : FLD T$C56I  **Giroconto parziale mancanti**
Se valorizzato permette di risolvere i mancanti con varie registrazioni di giroconto che saldano parzialmente la registrazione della fattura. In caso contrario è ammessa una sola registraione di giroconto.
 :  : FLD T$C56J  **Gestione "NON CONFORMITÀ"**
Attiva le non conformità : 
_9_" "= NO.
Gestisce le anomalie della fattura e relativo blocco pagamento con le fonti standard £ e i vari flag. Le non conformità possono essere usate per memorizzare e visualizzare a dettaglio eventuali informazioni di anomalie. Tuttavia non hanno alcuna influenza sul blocco pagamento della fattura.
_9_"1"= SI.
Gestisce le anomalie della fattura e relativo blocco pagamento attraverso le "non conformità".
 :  : FLD T$C56K  **Codice "NON CONFORMITÀ" mancanti**
- Se sono gestite le non conformità, indica il codice mancanti.
- Se non sono gestite le non conformità, presenta la richiesta blocco pagamento per macanti solo se valorizzato questo campo.
 :  : FLD T$C56L  **Codice "NON CONFORMITÀ" differenza prezzo**
- Se sono gestite le non conformità, indica il codice di differenza prezzo.
- Se non sono gestite le non conformità, presenta la richiesta blocco pagamento per differenze prezzo solo se valorizzato questo campo
 :  : FLD T$C56M  **Codice "NON CONFORMITÀ" differenza quantità**
- Se sono gestite le non conformità, indica il codice di differenza quantità.
- Se non sono gestite le non conformità, presenta la richiesta blocco pagamento per differenze quantità solo se valorizzato questo campo
 :  : FLD T$C56N  **Codice "NON CONFORMITÀ" differenza modalità pagamento**
- Se sono gestite le non conformità, indica il codice di differenza modalità di pagamento.
- Se non sono gestite le non conformità, presenta la richiesta blocco pagamento per differenze mod.pagam. solo se valorizzato questo campo
 :  : FLD T$C56O  **Codice "NON CONFORMITÀ" prestazione da validare**
- Se sono gestite le non conformità, indica il codice di prestazione da validare. Se valorizzato, viene scritta una non conformità di questo tipo alla conferma.
- Se non sono gestite le non conformità, presenta la richiesta blocco pagamento per prestazioni da validare solo se valorizzato questo campo
 :  : FLD T$C56P  **Codice "NON CONFORMITÀ" non conforme qualità**
- Se sono gestite le non conformità, indica il codice di non conforme dalla qualità. Se valorizzato, viene scritta una non conformità di questo tipo alla conferma.
- Se non sono gestite le non conformità, presenta la richiesta blocco pagamento per lotti non conformi qual. solo se valorizzato questo campo
 :  : FLD T$C56R  **Codice "NON CONFORMITÀ" Attesa nota di accredito**
Se sono gestite le non conformità, indica il codice di attesa nota di accredito. Se valorizzato, viene scritta una non conformità di questo tipo alla conferma dell'azione correttiva che genera la nota di accredito. La non conformità è legata alla fattura che ne blocca il pagamento fino a quando non si riceve la corrispondente nota di accredito.
 :  : FLD T$C56S  **Quadratura fattura**
È utilizzato nel controllo batch delle fatture. Se il residuo della fattura è in valore assoluto minore del valore qui specificato, la fattura viene chiusa con una quadratura. Il conto contabile è quello indicato nella corrispondente fonte £05. Se non presente, è quello della prima riga di fonte utente trovata.
 :  : FLD T$C56W  **Tipo lock**
È il tipo di lock scelto per controllare l'utilizzo di una stessa fonte da parte di due diversi utenti, nello stesso istante.
. _Oggetto testata_
Due utenti non possono eseguire contemporanemante il controllo fatture sullo stesso fornitore.
Il blocco è inserito/controllato all'immissione della registrazione.
Il blocco è eliminato alla conferma/abbandono della registrazione.
. _Oggetto origine_
Due utenti non possono eseguire contemporanemante il controllo fatture sulla stessa riga origine.
Il blocco è inserito/controllato nell'istante di selzione della riga.
Il blocco è eliminato nell'istante di deselezione della riga e in ogni caso alla conferma/abbandono della registrazione.
 :  : FLD T$C56X  **Residuo**
Controlli nel caso sia presente del residuo.
Se non impstostato esegue la modalità di controllo standard : 
* Chiede la conferma
* Genera un non conformità
* Chiede l'eventula blocco di pgamento
Se impostato a "1"
* Chiede la conferma
* Genera un non conformità
* NON Chiede l'eventula blocco di pgamento
Se impostato a "2"
* Non è possibile confermare la registrazione
 :  : FLD T$C56Z  **Disabilita Aggiornamento Automatico Piano Contributi Provvigioni
Se impostato disattiva l'aggiornamento automatico del piano contributi delle provvigioni
(tema £PC del contesto TAAGE sul D5COSO) in presenza di eventuali modifiche ai valori
ripresi nella registrazione.
 :  : FLD T$C561  **Condizione registrazione EDI
Se impostato la registrazione contabilizzata dal controllo fatture automatico nasce con la condizione indicata in questo campo. Se la registrazione passa la fase di controllo con esito positivo allora la condizione passa automaticamente ad attiva.
In fase di caricamento delle registrazioni da controllare verranno scartate le registrazioni con
condizione differente da quella impostata in questo campo.
 :  : FLD T$C56T  **Filtro iniziale su woirk
Se impostato presenta la schermata delle parzializzazioni prima della schermata del controllo bolle/fatture.
 :  : FLD T$C562  **Validazione :  Tipo registrazione Fattura**
E' il tipo di registrazione di fattura utilizzato nella funzione di
validazione. Serve solo come impostazione non esistendo ancora la
registrazione contabile in fase di validazione
 :  : FLD T$C563  **Validazione :  Tipo registrazione Nota accredito**
Vedi sopra ma per note accredito
 :  : FLD T$C564  **Righe contabili
Nel controllo fatture, di default, le righe contabili sono sempre
ricostruite in automatico a partire dai documenti in attesa. E'
poi possibile in registraizione contabile modificare le righe di
conto. In questo caso si determina una incongruenza tra la contabilità
e il gestionale.
Col seguente campo è possibile : 
-  se impostato a "2" bloccare la modifica delle righe contabili;
   in questo modo si è obbligati ad effettuare modifiche sono nel
   controllo fatture. La contabilità e il gestionale saranno sempre
   allineati.
-  se impostato a "3" non ricostruire le righe contabili (richiesta
   a video). La contabilità potrebbe essere non allineata al gestionale
 :  : FLD T$C565  **Risalita conto mancanti su contropartita ente in £17
Nella registrazione contabile il valore residuo, non attribuito a documenti
in attesa, viene associato al conto presente nella Fonte £02 mancanti.
Se si attiva questo campo il valore residuo viene associato al conto di
contropartita dell'ente (£17 dei dati di estensione dell'ente).
Nel caso non fosse presente rimane associato al conto mancanti.
 :  : FLD T$C566  **Workflow collegato**
Inserendo un flusso di workflow (elemento tabella WFA) si attiva la gestione del workflow stesso
per tutte le non conformità gestite nella registrazione. Il programma di gestione non conformità
provvederà a creare i flussi WF in fase di inserimento e/o di cancellazione.
Da notare il significato del flag 19 della non conformità (N§FL19 di CQNCOG0F) può essere utilizzato
dal flusso WF per bloccare una NC aperta ma con flusso iniziato e non finito (il flusso ha già avuto
avanzamenti e quindi controlli). Sarà compito del flusso stesso impedire la modifica della NC
portando il flag (19) a valore '0'.


