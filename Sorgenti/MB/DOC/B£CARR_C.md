### Dove sono memorizzati i dati.
Le cartelle sono record dell'archivio B£MEDE0F. Un carrello è l'insieme di cartelle associate allo stesso proprietario (ossia l'insieme di record che hanno gli stessi campi METIPA e MECODI).
SME.up come al solito accede e chiede di accedere ai dati tramite le apposite funzioni di interfaccia (Copy £G97). Ciò in particolare ci permetterà di modificare in futuro il luogo di memorizzazione e l'organizzazione dei dati.
I record riguardanti il carrello sono identificati dall'avere il campo MECOD1="CARRELLO".

### Codifica di una cartella
Esistono tre tipologie di cartella : 
1. Cartelle con prefisso * sono nomi riservati. In particolare abbiamo : 
-	*LAST. Contenuta nel carrello utente, contiene uno ed un solo oggetto per ogni tipo. Ad esempio se inserisco un cliente, questo sostituisce l'ultimo cliente presente.
-	*WORK. Contenuta nel carrello utente, contiene un insieme eterogeneo di oggetti. Serve come contenitore in cui porre facilmente (con un comando rapido) tutti gli oggetti che ad esempio in un momento successivo vogliamo ridistribuire in altre cartelle.
2. Cartelle contenenti un punto. Sono cartelle di oggetti omogenei, ossia contengono solo oggetti il cui tipo e parametro corrispondono alla parte del nome cartella che precede il punto.
3. Altre cartelle. Contengono oggetti eterogenei.

### Identificazione degli oggetti
Gli oggetti sono memorizzati in un campo che è definito con un massimo di 30.000 caratteri. Gli oggetti sono separati da una sequenza di due caratteri "||". Ogni oggetto è identificato da Tipo (inteso come tipo+parametro), codice e descrizione, separati da una coppia di caratteri ",,". La descrizione è facoltativa. La descrizione è particolarmente rilevante per gli oggetti di tipo funzione.
Avremo ad esempio CNCLI,,000001,,Cliente di prova||TAV5D,,OVE,,||J1FUN,,F(EXD;*SCO;) 1(A;B;C),,Estratto conto||.

### COPY di gestione dei dati
Tutte le funzioni sono delegate alla COPY £G97 cui si rinvia per i dettagli.
![B£CARR_003](http://localhost:3000/immagini/B£CARR_C/BXCARR_003.png)
- [Funzioni sul carrello](Sorgenti/MB/DOC_OGG/P_TSTG97)
Documentazione Servizio
Presente in DOC_SER riferita al servizio B£SER_25;
Si accede tramite la Scheda di LoocUp Documentazione/I documenti/Documenti presenti/DOC_SER documentazione dei servizi/B£SER_25
