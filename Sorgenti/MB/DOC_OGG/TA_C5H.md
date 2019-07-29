# C5H - Società
 :  : DEC T(ST) K(C5H)
## OBIETTIVO
Definire i caratteri generali delle società del gruppo allo scopo di descrivere la struttura societaria complessiva.
## CONTENUTO DEI CAMPI
 :  : FLD T$DESC Descrizione
Contiene la denominazione della società.
 :  : FLD T$C5HF Codice Azienda
Codice dell'azienda se gestita nel sistema informativo
 :  : FLD T$C5HI Lista Librerie
Definisce la lista delle librerie tramite la quale è possibile reperire i dati della società.
 :  : FLD T$C5HL Quota di controllo
Definisce la quota di controllo della società nel gruppo
 :  : FLD T$C5HM Capogruppo
Se valorizzato indicata che la società è una capogruppo
 :  : FLD T$C5HN Attivazione Movimenti Automatici su Pagamenti Intercompany
Se valorizzato attiva le registrazioni automatiche relative ai pagamenti intercompany :  se il fornitore che rappresenta la società in questione viene pagato da un'altra società del gruppo automaticamente nell'azienda corrispondente alla società in questione verrà scritta una registrazione automatica corrispondente al cliente della società che ha effettuato il pagamento.
Prerequisito è che entrambe le società abbiamo impostato questo campo ed il campo azienda, oltre che la configurazione della tabella C5U (INCIC e GIRIC).
 :  : FLD T$C5HO Attività CBCR
Lista di attività da indicare per la trasmissione dei dati per la Rendicontazione Paese per Paese in applicazione del decreto del ministro dell'economia e delle finanze del 23/02/2017 in materia di scambio automatico obbligatorio di informazioni nel settore fiscale.

