# CQL - Tipo lotti
 :  : DEC T(ST) K(CQL)
## OBIETTIVO
Definire le varie tipologie possibili dei lotti (produzione, acquisto, conto lavoro...) ed associarle ad una tipologia di ente di riferimento (fornitore, cliente, reparto...).
## CONTENUTO DEI CAMPI
 :  : FLD T$ORDP **Ordine di produzione**
I valori possibili sono : 
- ' '  Lotto non derivante da ordine di produzione
- '1'  Individua un lotto derivante da un ordine di produzione.
 :  : FLD T$ORCF **Ordine Cliente/Fornitore**
I valori possibili sono : 
- ' '  spazio  Lotto non derivante da ordine a fornitore o da un reso da clente
- 'C'  Individua un lotto derivante da un ordine a cliente
- 'F'  Individua un lotto derivante da un ordine a fornitore
 :  : FLD T$CLAV **Conto Lavori**
I valori possibili sono : 
- ' '  Lotto non derivante da conto lavoro
- '1'  Individua un lotto derivante da un conto lavoro
 :  : FLD T$COMM **Numero commessa**
- ' '  Numero commessa facoltativo
- '1'  Numero commessa obbligatorio. Richiede obbligatoriamente il numero della commessa in fase di inserimento lotto.
 :  : FLD T$TIEN **Tipo ente riferimento**
Campo gestito nella tabella '*CNTT' (Codici oggetti applicativi). Identifica la natura dell'ente di riferimento associato al tipo lotto.
_9_Esempio :  Per un Reso da Cliente si metterà il riferimento all'archivio clienti 'CL'.
 :  : FLD T$OBEN **Obbligatorio ente**
- ' '  Immissione 'Ente di Riferimento' facoltativa
- '1'  Immissione 'Ente di Riferimento' obbligatoria.
_9_Esempio :  Per un lotto di acquisto richiederà obbligatoriamente il codice del fornitore, oppure per un lotto di produzione richiederà il codice del Work-Center etc.
 :  : FLD T$OCTR **Obbl.Contr.Certific.**
- ' '  Immissione del certificato di Conformità del lotto facoltativa
- '1'  Immissione del/dei Certificato/i di Conformità che accompagnano il lotto obbligatoria.
_9_Esempio :  Per un lotto di acquisto richiederà obbligatoriamente il certificato di conformità, o il certificato di colata etc.
 :  : FLD T$MDQT **Modifica quantità rilevata**
- ' '  Rende impossibile la modifica della quantità rilevata nel lotto dopo la fase di dichiarazione e di registrazione a magazzino.
- '1'  Rende possibile la correzione delle quantità rilevate nel lotto anche dopo la registrazione del movimento a magazzino. In questo caso la modifica interviene solo sul File della gestione Lotti e non ha effetto sulla quantità registrata a magazzino. Per la modifica della quantità movimentata a magazzino, sarà necessario intervenire nel gestionale con la Manutenzione movimenti di magazzino.
 :  : FLD T$CTRL **Controllo Liv. Modifica**
- ' '  Nella fase di entrata del lotto, non controlla se il livello di modifica associato all'ordine (di produzione, acquisto, etc.) è stato superato a seguito di un intervento. (es. modifica di progetto).
- '1'  Nella fase di entrata del lotto, verifica se il livello di modifica ad esso associato e gestito dal modulo 'Gestione Documenti Emessi/Modificati', è stato nel frattempo superato per un intervento effettuato sul prodotto. Questo è possibile in quanto, nella fase di emissione di un ordine il programma associa all'ordine stesso, mediante un algoritmo di calcolo, il livello di modifica attivo in quel momento. Nella fase di entrata del lotto viene poi verificato se il livello associato è stato superato, nell'arco temporale che va dall'emissione ordine alla entrata del lotto.
Nel caso di livello superato, il programma evidenzia le modifiche intervenute.
 :  : FLD T$TPOR **Tipo Ordine Default**
Campo gestito nella tabella 'V5D'.
Identifica la tipologia dell'ordine, come ad esempio la differenziazione tra ordini chiusi, ordini aperti, etc.
 :  : FLD T$QTCO **Controllo Quantità Conforme**
- ' '  Esclude il campo della Quantità Conforme nel controllo della somma delle quantità dichiarate.
- '1'  Considera anche la Quantità Conforme, nella somma delle quantità di controllo. Il programma, poi, verifica che la suddetta somma sia inferiore o uguale alla quantità totale rilevata.
 :  : FLD T$MG01 **Codice Magazzino (Conforme)**
Indicare il magazzino nel quale deve essere effettuata la registrazione della quantità Conforme del lotto.
Obsoleto - Magazzini assunti da tabella CRP/CRB

 :  : FLD T$QSEL **Controllo Qtà Selezionata**
- ' '  Esclude, nel controllo della somma delle quantità dichiarate, il campo della Quantità Selezionata.
- '1'  Considera, nella somma delle quantità di controllo, anche la Quantità Selezionata. Il programma, poi, verifica che la somma anzidetta sia inferiore o uguale alla quantità totale rilevata.
 :  : FLD T$MG02 **Codice Magazzino (Selezionata)**
Indicare il magazzino nel quale deve essere effettuata la registrazione della Quantità Selezionata del lotto.
 :  : FLD T$QNOC **Controllo Qtà Non Conforme**
- ' '  Esclude, nel controllo della somma delle quantita dichiarate, il campo della Quantità Non Conforme.
- '1'  Considera, nella somma delle quantità di controllo, anche la Quantità Non Conforme. Il programma, poi, verifica che la somma suddetta sia inferiore o uguale alla quantità totale rilevata.
 :  : FLD T$MG03 **Codice Magazzino (Non Conforme)**
Indicare il magazzino nel quale deve essere effettuata la registrazione della Quantità Non Conforme del lotto.
 :  : FLD T$QRLV **Controllo Qtà Rilavorata**
- ' '  Esclude nel controllo della somma delle quantita dichiarate, il campo della Quantità Rilavorata.
- '1'  Considera nella somma delle quantità di controllo anche la Quantità Rilavorata. Il programma poi verifica che la somma anzidetta sia inferiore o uguale alla quantità totale rilevata.
 :  : FLD T$MG04 **Codice Magazzino (Rilavorata)**
Indicare il magazzino nel quale deve essere effettuata la registrazione della Quantità Rilavorata del lotto.
 :  : FLD T$QSCA **Controllo Qtà Scartata**
- ' '  Esclude, nel controllo della somma delle quantità dichiarate, il campo della Quantità Scartata.
- '1'  Considera, nella somma delle quantità di controllo, anche la Quantità Scartata. Il programma, poi, verifica che la somma suddetta sia inferiore o uguale alla quantità totale rilevata.
 :  : FLD T$MG05 **Codice Magazzino (Scartata)**
Indicare il magazzino nel quale deve essere effettuata la registrazione della Quantità Scartata del lotto.
 :  : FLD T$CTAB **Controllo Abilitazione**
Attivazione della procedura di controllo di abilitazione fornitura per l'ente di riferimento.
- ' '  Esegue il controllo dell'abilitazione alla fornitura.
- '1'  Non esegue il controllo di abilitazione.
 :  : FLD T$PGNC **Programma Non Conformità**
Controlla l'esecuzione del programma di gestione Non Conformità.
- ' '  Esegue il Pgm di gestione standard.
- '1'  Esegue il pgm di gestione Non conformità di Produzione.
 :  : FLD T$DFLV **Descrizione fase lavoro se fase = '**'**
Se viene definita la descrizione della fase, quando si entra nelle non conformità e la fase è '**' viene presa questa definizione come descrizione della fase di lavoro.
Obsoleto il default viene ora assunto dalla tabella CQ*LO con elemento = tipo lotto
 :  : FLD T$CQL7 **Data registrazione a magazzino**
Determina la data da utilizzare nell'eventuale movimento di magazzino, generato a seguito del collaudo del lotto.
Questo campo è significativo solo se vengono gestiti un'area o un magazzino di materiale al collaudo, che viene movimentato a seguito della dichiarazione di collaudo del lotto stesso. I valori possibili sono : 
- ' '=Data odierna
- 'B'=Data B.E.M.
- 'C'=Data collaudo
- 'D'=Data documento
 :  : FLD T$CQLO **No Movimenti Mag. PR**
Campo di esecuzione del movimento a magazzino del gestionale.
Può assumere i valori : 
' '  Risale a quanto impostato in tabella CQ1
'1'  Non effettua movimenti di magazzino per il tipo lotto anche se impostata generazione   in tabella CQ1
 :  : FLD T$CQLR **Tipo Risorsa**
Definisce il Tipo risorsa di default assunto in fase di inizializzazione lotto.
 :  : FLD T$CQLE **Ente di controllo**
Definisce l'oggetto assunto dall' ente di controllo, esempio DI01(Dipendente), TAB£U(profilo utente)
 :  : FLD T$CQL1 **Decodifica quantità**
Il campo è un sottosettore della tabella CQ*, se impostato il programma di gestione quantità
in dichiarazione collaudo, sostituisce le intestazioni standard con quelle della tabella
Gle elementi da inserire sono nell'ordine
1  Conforme
2  Scartata
3  Non Conforme
4  Selezionata
5  Rilavorata
