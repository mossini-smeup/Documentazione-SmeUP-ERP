# V5A - Modello documento
 :  : DEC T(ST) K(V5A)
## OBIETTIVO
Definisce le caratteristiche relative al modello documento.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM Codice
Indica il codice del modello del documento.
 :  : FLD T$DESC Descrizione
 :  : FLD T$V5AS __S/S tipo riga__
È un sottosettore della tabella V5B che raggruppa i tipi riga di documenti possibili per questo modello.
 :  : FLD T$V5AA __Tipo riga assunto__
È un elemento della tabella V5B, del sottosettore definito in precedenza. È il tipo riga che viene proposto all'inserimento delle righe di questo modello.
 :  : FLD T$V5AN __Numeratore documenti__
È un elemento della tabella CRNV5 che guida l'assegnazione automatica del numero del documento.
 :  : FLD T$V5AC __Contenitore note__
È un elemento della tabella NSC. Definisce il contenitore in cui vengono gestite le note dei documenti di questo modello.
 :  : FLD T$V5AE __Mod.Gestione valuta__
Definisce se il documento viene gestito in valuta.
 :  : FLD T$V5AP __Presentazione ridotta__
Se non si definisce un percorso e viene inserito il carattere 'S' verrà presentata la testata del documento in modalità ridotta (Standard).
 :  : FLD T$V5AQ __Quantità modificabile__
Definisce la quantità da gestire in questo modello documento (da 1 a 5, se blanks si assume 1). Il significato di tale quantità si deriva dal flag tipo quantità.
 :  : FLD T$V5AR __Passo numerazione righe__
Definisce il passo con cui viene assegnata la numerazione alle righe del documento.
 :  : FLD T$V5AF __Forma/Percorso__
È un elemento della tabella B£Q. Se valorizzato, viene usato come visualizzatore di testata il programma inserito in questa tabella.

 :  : FLD T$V5AB __Numeratore bolle__
È un elemento della tabella CRNV5, che guida l'assegnazione automatica del numero di bolla.

 :  : FLD T1V5AA __Suffisso pgm stampa bolle DDT__
Se impostato il programma di stampa bolle (DDT) lancia il programma di stampa V5BO00Sx (dove X=suffisso pgm).
Ricordiamo che il flusso dei programmi è il seguente :  V5BO01S master che lancia il programma V5BO00Sx dove x
assume ' ' se non impostato (V5BO00S programma di stampa standard)

 :  : FLD T$V5AD __Numeratore base fatture__
È un elemento della tabella CRNV5, che guida l'assegnazione automatica del numero della fattura.
Particolare attenzione deve essere riservata alla determinazione della lunghezza di tale numero, che deve essere congruente con la massima lunghezza del documento gestita dall'applicazione contabile interfacciata.
Normalmente tutte le fatture sono gestite da un unico numeratore. Se si vogliono distinguere i numeratori (ad esempio
ITALIA/INTRA/EXTRACEE) si consiglia di utilizzare tale caratteristica come suffisso del numeratore in sede di personalizzazione della stampa fatture.

 :  : FLD T$V5AG __Criterio ordinamento documento__
Definisce il criterio di raggruppamento (tra quelli previsti) dei documenti di bolla per ottenere un solo documento di fattura.
Valori attualmente gestiti nel pgm V5DO01O : 
. '1' e ' ' standard vendite per cod. pagamento e valuta
. '2' standard acquisti per data bolla e n.bolla
. '3' per cod. spedizione, cod. pagamento, valuta, mod. consegna e modello documento
Per i criteri alfabetici bisogna implementare programmi specifici (V5DO01O_x dove x è il criterio selezionato).
 :  : FLD T$V5AH __Causale contabile__
È la causale che viene utilizzata per la contabilizzazione. Questo elemento deve appartenere alla tabella C5A (MODELLO Contab. DOCUMENTI V5), che a sua volta contiente elementi della tabella C5D e della tabella C5V. Per convenzione gli elementi della tabella C5A hanno lo stesso codice degli elementi della C5D.
 :  : FLD T$V5AW __Categoria parametri esterni/interni__
È un elemento della tabella C£E. Definisce il luogo in cui sono contenuti i parametri collegati ai documenti di questo modello.
 :  : FLD T$V5A4 __Categoria parametri interni__
È un elemento della tabella C£I. Definisce il luogo in cui sono contenuti i parametri che descrivono i campi liberi (5 numerici e 5 alfanumerici), contenuti nell'archivio testate documenti di questo modello.
 :  : FLD T$V5AX __Gruppo Flag Testata__
È un elemento della tabella B£Y. Se valorizzato, alle testate documenti vengono assegnati i flag di questo elemento.
 :  : FLD T$V5AY __Gruppo Flag Riga__
È un elemento della tabella B£Y. Se valorizzato (e se non valorizzato il gruppo flag a livello di riga), alle righe documenti vengono assegnati i flag di questo elemento.
 :  : FLD T$V5AZ __Tipo Modello__
È un campo obbligatorio :  definisce la natura di questo modello (se ciclo attivo o passivo, se ordine o entrata o uscita).
 :  : FLD T$V5AM __Magazzino assunto__
È un elemento della tabella MAG.
Se questo campo è valorizzato durante l'inizializzazione della testata documento, viene inserito automaticamente nel campo magazzino. Se viene lasciato vuoto, il programma di inizializzazione lo riempirà con il magazzino unico (se presente).
 :  : FLD T$V5AT __Magazz.Trasf.Assunto__
È un elemento della tabella MAG.
Se questo campo è valorizzato, durante l'inizializzazione della testata documento viene inserito automaticamente nel campo magazzino di trasferimento. Se viene lasciato vuoto, il programma di inizializzazione non imposta nessun valore nel campo.
 :  : FLD T$V5AK __Suffisso caric.lista__
Se presente, per l'inserimento delle righe viene lanciato il programma di caricamento a lista V5DO20x, dove x è questo carattere.
Per la modifica delle righe viene lanciato il programma di caricamento a lista V5DO19x, dove x è questo carattere.
 :  : FLD T$V5AJ S/S __Modello Destinazione__
Serve per indicare il sottosettore del modello documento destinazione.
 :  : FLD T$V5AU __Modello Destinazione__
Va indicato in questo campo il modello documento di destinazione.
Questo modello documento viene utilizzato se  non viene definito nel flusso il modello di destinazione.
 :  : FLD T$V5AI __Tipo lotto Q9000__
È un elemento della tabella CQL.
Se impostato, e il documento è da collegare alla qualità, indica la tipologia del lotto da creare.
Se non impostato, non viene eseguito il collegamento alla qualità, indipendentemente dal flag di collegamento.
 :  : FLD T$V5AO __Controllo presenza righe__
Stabilisce se, in caso di immissione della testata del documento, debba essere effettuato il controllo della presenza di righe : 
- ' '= Documento con testate e righe. Viene proposta l'immissione di righe, e se non presenti, non viene fatto alcun controllo;
- 1 = Documento con testate e righe. Viene proposta l'immissione di righe, e se non presenti, viene segnalato con la proposta di eliminare la testata, con l'eventuale recupero del numero sul numeratore;
- 2 = Documento di sola testata, non viene proposta né permessa l'immissione di righe.
 :  : FLD T$V5A0 __Tipo condizionamento righe__
È un elemento (non controllato) della tabella V5*, sottosettore 'CR'.
Se impostato, vengono accettati solo i tipi riga che hanno un condizionamento uguale a questo. Se lasciato vuoto, non viene eseguito nessun controllo.
Si può quindi impostare la congruenza del documento.
_9_Esempio :  ad un documento di vendita (modello V1) si vogliono assegnare righe sia di vendita (tipo riga R1) sia di conto visione (tipo riga R2), mentre ad un documento di conto visione (modello V2) si vogliono assegnare solo righe di conto visione. In questo caso si devono impostare i condizionamenti nel
seguente modo : 
- V1   =    ' ' . Accetta tutte le righe.
- V2   =    'A' . Accetta solo le righe di tipo A.
- R1   =    ' '
- R2   =    'A'
 :  : FLD T$V5A1 __Suff.controllo campi__
Se impostato, nel programma di gestione della testata documento, viene lanciato il programma V5DO01C_x (dove x = suff.) che permette di modificare la tipologia degli oggetti  dei campi presenti in testata (per esempio si veda  V5DO01C_A).
 :  : FLD T$V5A2 __Tipo data reg. Mag.__
Indica la data da utilizzare come data di registrazione nei movimenti di magazzino.
I valori possibili sono : 
- ' '  -    Assume il campo indicato nel tipo documento (V5D).
- 'A'  -    Data documento interno (è la data di testata del documento).
- 'B'  -    Data documento esterno (è la data bolla).
- 'C'  -    Oggi (è la data di esecuzione del collegamento a magazzino).
- 'D'  -    Data di partenza.
 :  : FLD T$V5A3 __Suff.controllo ente__
Se impostato, nel programma di gestione della testata documento, in fase di inserimento del documento, viene lanciato il programma V5DO01E_x (dove x = suff.) che permette di eseguire dei controlli di validità dell'ente intestatario del documento (per esempio si veda V5DO01E_A).
 :  : FLD T$V5A5 __Tipo rata generata__
È un elemento della tabella C5E.
In presenza di contabilità Sme_Up, se impostato, determina la scrittura nell'archivio rate di rate extracontabili con questo tipo.
 :  : FLD T$V5AV __Livello di nascita__
In fase di inserimento del documento, se specificato, viene assunto come livello di nascita. Se assente, viene assunto quello specificato nella tabella V5D, ed in subordine, se a sua volta assente, viene assunto il livello di default 2.
 :  : FLD T$V5A6 __Stato di nascita__
Se specificato, in fase di inserimento del documento, viene assunto come stato di nascita. Se assente, viene determinato lo stato principale del livello di nascita.
 :  : FLD T$V5A7 __Suff.inizial.__
Se impostato, all'atto dell'inizializzazione di una testata documento con questo modello, come ultima cosa viene eseguito il programma V5V5Y0_X, che permette di modificare il contenuto del record.
 :  : FLD T$V5A8 __Suff.vis.det.doc__
Se impostato, viene chiamato un programma specifico di visualizzazione delle righe di un documento.
Questo programma viene chiamato in alternativa allo standard V5IN01 (il prototipo si chiama V5IN01_X).
 :  : FLD T$V5A9 __Ente ripresa prezzi__
Definisce l'ente da utilizzare per la ripresa dei valori da listino.
Tecnicamente è l'ente passato alla routine di ripresa prezzi dal monitor delle righe dei documenti.
Può assumere i seguenti valori : 
- ' ' - Ente intestatario (default);
- '1' - Ente di conferma;
- '2' - Ente di fatturazione;
- '3' - Ente di spedizione;
- '4' - Ente di destino;
 :  : FLD T1V5AC __Obbl.Documento Rif.
Impostando il campo a '1' diventa obbligatorio l'inserimento di un documento/riga di riferimento
collegato alla testata che si sta manutenzionando.
Questa impostazione può essere necessaria quando si vuole far inserire, per esempio, in una nota di
credito la fattura a cui è collegata
