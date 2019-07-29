La generazione di un report è soggetta alla valorizzazione di alcuni attributi di setup che consentono di personalizzare l'output.
Per visualizzare e modificare i valori standard contenuti nel setup del report è necessario entrare nella scheda dell'oggetto J3 e scegliere come forma grafica FRM.REP : 

![LOCREP001](http://localhost:3000/immagini/LOCREP_STP/LOCREP001.png)
All'interno del tab 'Report tabella' sono riportati i setup preconfigurati disponibili. Il setup utilizzato come default nella generazione di report di matrici è l'A01. Selezionandolo e scegliendo il tab 'Script' è possibile visualizzare lo script che definisce i setup preconfigurati : 

![LOCREP_002](http://localhost:3000/immagini/LOCREP_STP/LOCREP_002.png)
Da qui è posibile selezionare il pulsante 'Gestione documento' ed entrare in modifica dello script. Per individuare i record specifici che definiscono il setup standard è necessario cercare all'interno delle righe che iniziano con il comando  :  : G.FRM.REP e indagare con il wizard il setup con Name='A01'.

## Il Setup del report

![setupREP](http://localhost:3000/immagini/LOCREP_STP/setupREP.png)
All'interno del setup le voci di parametrizzazione sono organizzate in 4 sezioni : 

- File
-- Apri dopo la creazione :  permette di visualizzare il report al termine della creazione
-- Directory di creazione del pdf :  imposta il percorso di salvataggio del pdf
-- Nome del file da creare
-- Password sul documento :  per la protezione in lettura del pdf generato
-- Sovrascrivi file generati :  se impostato creando un pdf che riporta lo stesso nome di un file già presente lo sovrascrive, in caso contrario aggiunge al nome del file un progressivo.
-- Elimina file generato in uscita :  se impostato alla chiusura di LoocUP si avrà la cancellazione del PDF prodotto da quella esecuzione.
- Documento
-- Formato foglio :  da A0 a A4 più Letter
-- Orientamento :  orizzontale o verticale (salvo non sia indicato diversamente nel successivo campo **Nome template da usare**, dall'unione del formato e dell'orientamento viene dedotto il file jrxml da usare come template, es :  A4 orizzontale farà utilizzare il template con suffisso A4H, A3 verticale il file con suffisso A3V)
-- Copertina se esiste :  nel caso in cui all'interno del servizio o all'interno della chiamata della funzione che costruisce la matrice sia impostata una copertina permette di visualizzarla o meno all'interno del report
-- Senza colorazione oggetti :  se impostato all'interno del report non appariranno i colori delle colonne "oggettizzate"
-- Nome template da utilizzare :  permette di definire un template personalizzato da utlizzare nella creazione del report
-- Sviluppo subreport :  blocca lo sviluppo del report alla matrice **Master**
-- Comprimi verticale :  compatta al massimo verticalmente il report dove consentito (struttura report-subreport)
- Pagina
-- Indicatori di pagina
-- Colonne di stampa verticali :  numero di colonne impostate nel report
-- Spazio tra colonne di stampa :  spazio fra le colonne contenenti i subreport
-- Titolo su pagina nuova :  forza una nuova pagina all'inizio di una matrice (ha senso nelle stampe schede dove c'è una struttura master/subreport)
-- Disposizione dei subreport :  definisce se disporre i subreport in modo affiancato (orizzontale) oppure incolonnati (verticale)
-- Largh. min. colonna di matrice :  larghezza minima consentita per le colonne della matrice. Comunque non va mai sotto i 2 caratteri(per default).
-- Tipo larghezza colonna di matrice. Valori gestiti : 
--- Calcolata in percentuale su Lun (parametro della scheda in oggetto) :  l'attributo di colonna Lun è il peso della colonna, rispetto alla somma dei Lun di tutte le colonne, nel calcolo dello spazio da assegnare alla stessa
--- Massimo tra percentuale e Lun :  il massimo fra l'attributo Lun e quello calcolato al punto precedente
--- Massimo tra percentuale e testo :  il massimo fra la percentuale e la lunghezza del valore più lungo presente nelle righe della colonna
--- Utilizza Lun :  usa l'attributo Lun della colonna (partendo dalla prima colonna a sinistra, finchè c'è spazio nel foglio)
--- Dimensione largh. max testo :  viene assegnato lo spazio sufficiente per contenere il valore più lungo presente nella colonna (partendo dalla prima colonna a sinistra, finchè c'è spazio nel foglio)
-- Gest. automatica dettaglio
-- Override delle Lun per REP :  possibilità di definire lunghezze campi Custom che avranno la precedenza sulle Lun nel Xml. La sintassi è <codice colonna1>=lun1|<codice colonna2>=lun2|etc. Questo attributo ha senso quando l'impostazione di "Tipo larghezza colonna" si basa su Lun
-- Numero campi per colonna :  numero campi da incolonnare nel dettaglio (<2 viene utilizzato layout a tabella)
-- Titolo Header :  questo campo e i cinque successivi permettono di parametrizzare il layout del report come presentato nell'immagine
-- Sottotitolo header
-- Informazione 1
-- Informazione 2
-- Logo in alto
-- Logo in basso


![LOCREP_003](http://localhost:3000/immagini/LOCREP_STP/LOCREP_003.png)

- Contenuto
-- Righe lettura facilitata :  con righe alternate bianche e grigie (valido se disabilitata colorazione oggetti)
-- Bordi celle :  disegnare o meno il bordo alle celle delle matrici
-- Mostra filtri di matrice applicati :  nel caso siano applicati dei filtri vengono segnalati nel report
-- Forza salto pagina su rott. :  nei report di scheda al termine di un subreport forza il salto pagina, nei report di matrice alla rottura dei raggruppamenti
-- Gruppo su cui effettuare rottura :  permette di definire il codice colonna su cui effettuare la rottura qualora venga utilizzato per il raggruppamento
-- Indentazione gruppi : 
-- Esplosione dei gruppi :  esplode i gruppi nei report con impostato il raggruppamento
-- Subtotali nel piede gruppo :  come default i totali dei raggruppamenti sono riportati in testa al raggruppamento stesso, attraverso questo campo è possibile meterli ai piedi del raggruppamento.
-- Aggiunta car.colonne numeriche : 
-- Dim. max. font dettaglio :  la dimensione massima consentita per il testo delle celle della matrice
-- Altezza celle dettaglio :  è l'altezza forzata della cella, che per default è dimensionata come il font del contenuto + 2
-- Dim. font Dettaglio :  forza la dimensione font per la sezione dettaglio
-- Dim. font Header :  forza la dimensione font per le intestazioni di tabella
-- Dim. font Footer :  forza la dimensione font per i piedi di tabella
-- Dim. font Totali :  forza la dimensione font per la sezione totali
-- Dim. font Raggruppamenti :  forza la dimensione font per le intestazioni dei raggruppamenti
-- Carattere base x dimensioni :  lettera usata come unità di misura per calcorare lo spazio occupato da un carattere nel dimensionamento delle colonne. Il default è la lettera X


### Impostare il setup da servizio
E' possibile impostare da servizio RPG il setup per uno specifico report.
Ciò è possibile aggiungendo al XML prodotto dal servizio, nell'apposito nodo XML Setup/Program, un nodo FRM con attributo Type="REP" in cui esprimere gli attributi che si vogliono impostare.

Es :  < FRM Type="REP" PLGO1="AAA" PLGO2="BBB" Info1="CCCC" Info2="DDDD" Title="SSSS" Subtitle="VVVV"/ >


### Livelli di grigio nei totali
Come abbiamo sulla matrice diversi livelli di colorazione dei subtotali, anche per il report che verra' generato a partire da essa, saranno presenti varie tonalita' di grigio, per distinguere ogni raggruppamento, e quindi riconoscere i totali dedicati ad un campo specifico.
![03COMREP01](http://localhost:3000/immagini/LOCREP_STP/03COMREP01.png)Qui sotto vediamo un esempio con le 3 tonalita' di grigio presenti legate, al tipo oggetto, alla data fattura subito dopo e alla fattura specifica : 
![03COMREP02](http://localhost:3000/immagini/LOCREP_STP/03COMREP02.png)
### Totali dei raggruppamenti
I totali nei vari raggruppamenti sono impostati di default in alto, sull'intestazione del raggruppamento. Questo per facilitare la lettura dei report.
![03COMREP03](http://localhost:3000/immagini/LOCREP_STP/03COMREP03.png)E' inoltre possibile segnalare i subtotali di una colonna tramite evidenziazioni diverse. Nell'esempio sopra e' possibile vedere il primo importo legato al Tipo oggetto con un importo totale cerchiato in verde, un totale sul conto contabile cerchiato in rosa e dei totali sul raggruppamento della data aggiornamento segnati in viola. Comunque se si volesse e' ancora possibile indicare nel setup del componente REP se porre i subtotali in fondo ai raggruppamenti.

### Miglioramenti alle formule, gestione di N/0 e 0/0
E' stata inserita la gestione del valore infinito (N/0) ed indeterminato (0/0) nei campi della matrice. Anche nella produzione successiva di report su matrici viene gestita tale casistica; nel caso il valore di una cella sia 'infinito' la cella si colorera' di arancio ed apparira' '- -' mentre nel caso sia 'indeterminato' nella la cella diverra' di colore verde ed apparira' il valore ' '(blanks)

**N.B.** :  Il logo in alto della pagina, se non diversamente espresso, è l'immagine dell'oggetto V2 COD_SEL LOG_000. Il logo in basso della pagina, se non diversamente espresso, è l'immagine dell'oggetto V2 COD_SEL LOG_001. Per una corretta gestione di questi ultimi si rimanda all'argomento generale della gestione delle immagini degli oggetti. Tale argomento ricade nel modulo LOBASE
A titolo esemplificativo riportiamo la procedura per la personalizzazione di uno dei loghi del report : 

Per variare la copertina o loghi : 
* verificare se nella PER c'è già uno script in SCP_SET che si chiama K09_PER, se non c'è copiare quello della SMEDEV (e svuotarlo)
* in questo script metti queste specifiche : 
** K09.SEZ Ogg="VOCOD_SEL"
** K09.PIG Pth="percorso completo del file eventualmente comprensivo di variabili &"
* riavvia loocup
* da menù in alto UP Rosso, strumenti, cache, svuota cache client
* come sopra svuota cache immagini
