# GAR - Tipo richiesta di acquisto
## OBIETTIVO
Identificare le tipologie di Richieste di Acquisto gestibili dal modulo. Questa tabella andrà a definire quali saranno gli oggetti ordinabili ed a chi. Inoltre, permetterà di indicare l'eventuale origine della richiesta (es. Budget).
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM Elemento
Tipo Richiesta.
 :  : FLD T$DESC Descrizione
Descrizione.
 :  : FLD T$TIOG __Tipo Oggetto della Richiesta__
Elemento della tabella *CNTT che indica l'oggetto richiesto.
 :  : FLD T$PAOG __Parametro Oggetto Richiesta__
Parametro.
 :  : FLD T$TIOR __Tipo Fornitore Suggerito__
Elemento della tabella *CNTT che indica il tipo di Fornitore suggerito.
 :  : FLD T$GARN __Parametro Fornitore Suggerito__
Parametro Fornitore Suggerito
 :  : FLD T$TIRI __Tipo Oggetto Origine__
Elemento della tabella *CNTT che indica il tipo di oggetto da cui ha avuto origine la richiesta. (Es. Budget)
 :  : FLD T$PARI __Parametro Oggetto Origine__
Parametro.
 :  : FLD T$OROB __Origine obbligatoria__
Indica se il campo origine a dettaglio è obbligatorio o meno.
 :  : FLD T$GARE __Parametro Generaz.Ordine__
Definisce le caratterizzazioni usate nella generazione della testata dell'ordine di acquisto e dipende dall'ambiente impostato in tabella generale B£2.
Nel caso di ordini di acquisto SME_UP, è il modello del documento che viene controllato nel sottosettore presente nel tipo documento degli ordini d'acquisto, definito in questa stessa tabella (se assente viene assunto il tipo documento definito in tabella GA1).
 :  : FLD T$GARC __Tipo Riga Ordine__
Definisce il tipo di riga utilizzata nella generazione delle righe dell'ordine di acquisto e dipende dall'ambiente impostato in tabella generale B£2.
Nel caso di ordini di acquisto SME_UP, è il tipo riga che viene controllato nel sottosettore presente nel modello tipo documento degli ordini d'acquisto, definito in questa stessa tabella.
 :  : FLD T$GARD __Classificazione assunta__
È un elemento del settore GAC. Se impostato, esso verrà proposto all'atto dell'inserimento delle richieste di questo tipo.
 :  : FLD T$GARF __Pgm controllo esterno__
Se impostato, nella manutenzione delle richieste di questo tipo viene eseguito questo programma per implementare controllo specifici.
 :  : FLD T$GARA __Livello di protezione__
È un elemento della tabella B£W/RA che può essere utilizzato per autorizzare un singolo elemento di questa tabella.
Per maggiori informazioni, si rimanda all'help del programma di gestione settori, sotto il paragrafo : 
CONDIZIONAMENTO RICERCA / AUTORIZZAZIONI ALL'UTILIZZO.
**NB** :  il sottosettore di questi stati (RA) NON ha nessuna relazione con il sottosettore degli stati delle richierste d'acquisto (GA).
 :  : FLD T$GARG __Categoria parametri__
È un elemento della tabella C£E :  se impostato, definisce i parametri agganciabili alle richieste d'acquisto di questo tipo.
 :  : FLD T$GARH __Tipo documento__
È un elemento della tabella V5D :  se impostato, viene assunto all'atto del passaggio da richiesta ad ordine di acquisto (se lasciato in bianco viene assunto il valore impostato a livello generale, nella tabella GA1).
 :  : FLD T$GARI __Suffisso programma di aggiustamento__
Se impostato, subito prima della scrittura della riga di documento V5, verrà lanciato il programma 'GARD_GRSMx', dove x è il suffisso qui impostato. In questo modo è possibile modificare il contenuto della riga che si sta per scrivere.
 :  : FLD T$GARL __Tipo impegno__
È un elemento della tabella P5I :  se impostato, le richieste di questo tipo si intendono di conto lavoro. Saranno contraddistinte dal fatto di avere il flag '3' impostato.
 :  : FLD T$GARM __Parametri di pianificazione per riferimento__
Se impostato, e nella tabella generale M51 è stato definito il tipo oggetto intestatario dei parametri, verranno usati, se presenti, i tempi di approvvigionamento specifici per datare gli impegni di questo tipo richiesta.
_9_Esempio :  se si è prevista in M51 la possibilità di definire i parametri di pianificazione a livello di ente, e questo campo è valorizzato, la ricerca dei tempi di approvvigionamento verrà eseguita tenendo conto anche dell'ente.
Questo campo va valorizzato in abbinamento a quello corrispondente nella politica di pianificazione, e a quello del tipo riga in cui questa richiesta si tramuterà.
In tal modo gli impegni terranno conto dell'eventuale tempo di approvvigionamento 'corretto' : 
- in fase di pianificazione (se impostato nella politica).
- in fase di costruzione impegni rilasciati (se impostato in questa tabella).
Questa informazione ridondante ha lo scopo di migliorare le prestazioni :  se i tempi di approvvigionamento di lavorazione esterna non sono definiti per riferimento, anche se la politica dell'articolo lo è (ad esempio, per diversificare i lotti a livello di ente), e se nella costruzione degli impegni ci si basasse sull'informazione della politica, verrebbero ricercati inutilmente i parametri di pianificazione per riferimento.
 :  : FLD T$GARP __Descrizione Oggetto__
Consente di ricalcolare o meno la descrizione del campo-descrizione al cambio oggetto, eventualmente bloccando il campo.
Valori possibili : 
 - ' ' = Campo descrizione libero e non ricalcolato al cambio oggetto.
 - '1' = Campo descrizione libero e ricalcolato al cambio oggetto.
 - '2' = Campo descrizione bloccato e ricalcolato al cambio oggetto.
Se l'oggetto è generico questi valori non sono presi in considerazione. La descrizione è sempre libera.
 :  : FLD T$GARO __Stato libero?__
Consente di lasciare il campo dello STATO modificabile, solo se inferiore alla validazione "20" per tutti gli utenti autorizzati alla classe "GARDAT" (l'utente deve essere il proprietario della Rda). Gli stati ammessi sono quelli della B£WGA. Non è possibile arretrare lo stato dopo la validazione, ma solo avanzarlo.
