# P5T - Tipo ordine produzione
 :  : DEC T(ST) K(P5T)
## OBIETTIVI
Contiene i parametri che guidano l'impostazione di un ordine di produzione interna.
## SOTTOSETTORI
Non gestiti
## CONTENUTO DEI CAMPI
 :  : FLD T$P5TT __Tipo Ente Assunto__
È un elemento della tabella BRE. Viene proposto all'atto dell'inserimento dell'ordine che caratterizza l'Ente che si può collegare all'ordine.
 :  : FLD T$P5TP __Tipo Documento Assunto__
È un elemento della tabella V5D. Viene proposto all'atto dell'inserimento dell'ordine che caratterizza il documento che si può collegare all'ordine.
 :  : FLD T$P5TR __Tipo Risorsa Assunta__
È un elemento della tabella BRR. Viene proposto all'atto dell'inserimento dell'ordine che caratterizza la risorsa che si può collegare all'ordine.
 :  : FLD T$P5TB __Tipo Schedulazione__
(SV)
 :  : FLD T$P5TN __Numeratore Ordine__
È l'elemento della tabella CRN (sottosettore P5) che viene usato per assegnare il numero all'ordine.
 :  : FLD T$P5TC __Contenitore Note__
È l'elemento della tabella NSC che contiene le note dell'ordine.
 :  : FLD T$P5TS __Tipo Sviluppo Quantità__
È l'elemento della tabella B£G. Se impostato, definisce che l'ordine non avrà una quantità singola ma uno sviluppo, nel modo definito in questa tabella
 :  : FLD T$P5TI __Tipo Impegno Materiali__
È l'elemento della tabella P5I. Se impostato, definisce che l'ordine avrà dei materiali collegati, nella modalità definita in questa tabella.
 :  : FLD T$P5TO __Tipo Impegno Risorse__
Se impostato, definisce che l'ordine avrà delle attività collegate, nella modalità definita in questa tabella.
 :  : FLD T$P5TA __Ordine senza articolo__
Se impostato, l'ordine non è destinato alla produzione, quindi viene inibito l'inserimento dell'articolo nella gestione. In questo modo si possono definire, ad esempio, ordini di manutenzione, che impegnano materiali e risorse senza ottenere un prodotto.
Se si vuole comunque riferire l'ordine ad un articolo, esso va inserito come oggetto di riferimento.
 :  : FLD T$P5TW __Gruppo Flag Testata__
Se valorizzato, all'ordine vengono assegnati i flag di questo elemento.
 :  : FLD T$P5TL __Livello di nascita__
Se specificato, in inserimento dell'ordine viene assunto come livello di nascita. Se assente, viene assunto il livello di default 2.
 :  : FLD T$P5TV __Stato di nascita__
Se specificato, in inserimento dell'ordine viene assunto come stato di nascita. Se assente, viene determinato lo stato principale del livello di nascita.
 :  : FLD T$P5TF __Tipo/Parametro oggetto di riferimento__
Il tipo e il parametro oggetto di riferimento sono i campi proposti all'atto dell'inserimento dell'ordine. Definiscono la natura dell'oggetto a cui si può far riferimento nell'ordine.
 :  : FLD T$P5TJ.T$P5TF
 :  : FLD T$P5TM Tipo __Matricola Assunta__
È un elemento della tabella BRU che viene proposto all'atto dell'inserimento dell'ordine. Caratterizza la matricola che si può collegare all'ordine.
 :  : FLD T$P5TG __Priorità Assunta__
È un elemento della tabella B§A che viene proposto all'atto dell'inserimento dell'ordine.
 :  : FLD T$P5TZ __Categoria Parametri__
È un elemento della tabella C£E che definisce i parametri collegabili all'ordine.
 :  : FLD T$P5TX __Commessa obbligatoria__
Se impostato, la commessa è un campo obbligatorio nella manutenzione dell'ordine.
 :  : FLD T$P5TY __Oggetto di riferimento obbligatorio__
Definisce il modo con cui controllare l'oggetto di riferimento, nella manutenzione dell'ordine
Può assumere i seguenti valori : 
-    ' '  campo facoltativo
-    '1'  campo obbligatorio
-    '2'  campo facoltativo, ed il tipo/parametro sono protetti anche in manutenzione.
-    '3'  campo obbligatorio, ed il tipo/parametro sono protetti anche in manutenzione.
 :  : FLD T$P5TD __Proposta data oggi__
Se impostato, la data inizio dell'ordine di produzione viene impostata alla data odierna.
 :  : FLD T$P5TQ __Proposto lotto std__
Se impostato, per la quantità dell'ordine viene proposto il lotto std dell'articolo relativo (se l'ordine è di articolo).
 :  : FLD T$P5TE __Gestione esponente di modifica__
Se valorizzato, e se l'ordine è di articolo, inserisce nell'ordine l'esponente di modifica dell'articolo all'atto dell'inserimento e della variazione, secondo quanto impostato : 
-    '1'  Data ordine
-    '2'  Data inizio richiesta
-    '3'  Data fine richiesta
 :  : FLD T$P5TK __Chiusura impegni risorse__
Se impostato, all'atto del versamento a saldo dell'ordine, verranno cancellati tutti gli impegni di risorse residui.
 :  : FLD T$P5TH __Passaggio oggetto di rottura__
Definisce se e come viene trasferito l'oggetto di rottura del record pianificato, all'atto del rilascio.
Può assumere i seguenti valori : 
-    ' '  nessun passaggio
-    '1'  trasferito nell'oggetto di riferimento (con forzatura del tipo e del parametro).
-    '2'  trasferito nel campo corrispondente (commessa / ente / configurazione). (NB :  questo passaggio ha la precedenza
          sulla scrittura dell'origine, eseguita in caso di pianificazione 1/1).
 :  : FLD T$P5TU __Suff.pgm controllo__
_Se utilizzata versione 1 gestione ordini produzione (senza visualizzatore)_
È il suffisso del pgm P5OR01D_x che permette di gestire controlli e aggiornamenti specifici in fase di gestione del file (es. P5OR01D_F).
_Se utilizzata versione 2 gestione ordini produzione (con visualizzatore)_
È il suffisso del pgm P5OR02C_x :  permette di modificare la tipologia degli oggetti dei campi presenti nel tracciato  (vedi ad esempio :  P5OR02C_A).
 :  : FLD T$P5T0 __Suff.pgm aggiustamemto.__
È il suffisso del pgm P5P5Y0_x che vene lanciato all'atto dell'inizializzazione degli ordini di produzione di questo tipo.
 :  : FLD T$P5T1 __Stati Art.__
Si possono impostare due stati (elementi della tabella B£W/AR) che definiscono gli estremi di validità per gli articoli accettati nell'inserimento degli ordini di produzione di questo tipo.
 :  : FLD T$P5T2.T$P5T1
 :  : FLD T$P5T3 __Plant di default__
Se attiva la gestione multiplant, è il valore assunto di default dal plant in fase di inserimento dell'ordine di produzione, a meno che non impostato diversamente.
 :  : FLD T$P5T6 __Plant fisso__
Se attiva la gestione multiplant ed è impostato il campo "plant di default", in fase di inserimento dell'ordine di produzione il magazzino sarà sempre impostato da tale campo e non sarà possibile modificarlo. Questa impostazione ha priorità anche sull'eventuale valore impostato nel campo Plant di appartenenza dell'anagrafica articoli.
 :  : FLD T$P5T4 __Tipo lotto CQ__
Determina il tipo lotto da utilizzare in inizializzazione dei lotti. Se non impostato, verrà utilizza il codice del tipo ordine stesso.
 :  : FLD T$P5T5 __Forma di presentazione__
È significativo se è stato impostato in tabella P51 il flag di visualizzatore su ordini di produzione.
È un elemento della tabella B£Q, in cui si indica il programma di visualizzazione utilizzato per gli ordini di questo tipo.
 :  : FLD T$P5T7 __Tipo lotto fase__
Determina il tipo lotto da utilizzare nel caso in cui si crei un lotto da avanzamento di fase e la fase non sia l'ultima dell'ordine di produzione.
 :  : FLD T$P5T8 __Tipo MFP__
Se impostato questo campo, gli ordini di produzione di questo tipo avranno un avanzamento di tipo MFP con le caratteristiche presenti nell'elemento qui memorizzato.
 :  : FLD T$P5T9 __Tipo Scarto__
Caratterizza la modalitià di gestione degli scarti. Con reintegro o con nettificazione.
Se NON presente, mantiene il metodo base gestito con il K§FL04 per il reintegro e con il campo di tabella T$P51G per la nettificazione.
La nettificazione viene eseguita solo se non presente il K§FL04.
Se impostato a "1" si vuole gestire il reintegro del materiale scartato : 
. la quantità versata a scarto non riduce il residuo, ma si somma alla quantità ordinata per determinare   la quantità di impegno dei componenti.
Se impostato a "2" NON si vuole gestire il reintegro del materiale scartato.
. la quantità versata a scarto riduce il residuo dell'ordine
 :  : FLD T1P5TA __Categoria parametri interni__
È un elemento della tabella C£I. Definisce il luogo in cui sono contenuti i parametri che descrivono i campi liberi (10 numerici e 10 alfanumerici), contenuti nell'archivio ordini di prorduzione.
!!! ATTENZIONE !!!
La lunghezza massima dell'elemento di C£I inseribile è di 3 caratteri (anche se questo settore permetterebbe fino a
6 caratteri) per non riempire in modo eccessivo il presente settore.
