# CQX - Stato dell'addebito/accredito
 :  : DEC T(ST) K(CQX)
## OBIETTIVO
Classificare gli stati in cui si può trovare un'azione di accredito/addebito avviata a seguito della rilevazione di una non conformità
## CONTENUTO DEI CAMPI
 :  : FLD T$TACC **Obb.Valore Add/Acc.**
Il campo può assumere i seguenti valori : 
' '  la registrazione del valore da addebitare/accreditare al fornitore/cliente è facoltativa.
'X'  la registrazione del valore da addebitare/accreditare al fornitore/cliente è obbligatoria.
 :  : FLD T$TADD **Add./Acc.da eseguire**
Il campo può assumere i seguenti valori : 
' '  L'addebito/accredito al fornitore/cliente non assume significato per il programma.
'X'  L'addebito/accredito al fornitore/cliente è da eseguire.
 :  : FLD T$TESE **Accr./Add. eseguito**
Il campo può assumere i seguenti valori : 
' '  L'addebito/accredito al fornitore/cliente non assume significato per il programma.
'X'  L'addebito/accredito al fornitore/cliente è eseguito.
 :  : FLD T$TNUL **Nessuna azione**
Il campo può assumere i seguenti valori : 
' '  non assume significato per il programma.
'X'  nessuna azione specifica di addebito/accredito deve essere eseguita.
 :  : FLD T$TCVR **Codice Verbale**
Il campo è libero e non controllato. Serve per differenziare la numerazione automatica dei verbali di scarto e non conformità.
 :  : FLD T$TNVR **Num. Progress. Verb.**
Il campo è utilizzato dal programma per la numerazione dei verbali di scarto e non confornità.
 :  : FLD T$TSTA **Nuovo Stato Add/Acc**
Campo controllato dalla tabella 'CQX' (Stato dell'addebito/accredito). Indica al programma la nuova condizione di arrivo, una volta evaso lo stato attuale.
 :  : FLD T$TPGM **Pgm Creaz. Doc.Mag.**
Nome del PROGRAMMA da richiamare per la creazione del documento di scarto dal magazzino.
 :  : FLD T$CMAG **Magazzino Moviment.**
Nome o numero del magazzino che deve essere movimentato nella gestione della non conformità o scarto.
 :  : FLD T$CQXA **Livello Assunto**
E' il livello che verrà assunto automaticamente dall'avanzamento NC.
 :  : FLD T$CQXB **Stato Assunto**
E' lo stato che verrà assunto automaticamnete dall'avanzamento NC.
