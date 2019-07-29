# CQ0 - Tipo documento - gestione
 :  : DEC T(ST) K(CQ0)
## OBIETTIVO
Questa tabella contiene i codici dei tipi di documento relativi alla gestione e controllo della documentazione aziendale.
Assegnare al tipo documento il tipo griglia necessario alla descrizione e alla gestione dei campi di INPUT.
Legare il tipo documento ad un archivio di gestione.
## CONTENUTO DEI CAMPI
 :  : FLD T$ATGR **Tipo griglia**
Campo controllato dalla tabella 'CQY' (Tipo griglia controlli).
Si deve specificare il tipo griglia associato al tipo documento; il tipo griglia contiene le specifiche per le chiavi di accesso al documento.
 :  : FLD T$GESM **Gestione modifica**
Questo campo può assumere i seguenti valori : 
' '  Non viene attivata la gestione del livello di modifica sul documento.
'X'  Viene attivata la gestione del livello di modifica del documento attraverso il programma 'Gestione della documentazione'
 :  : FLD T$INAU **Indice automatico**
Se questo campo assume valore 'X' l'indice di modifica del documento è generato in automatico e non è consentita l'immissione manuale
 :  : FLD T$GEDO **Gestione documento**
Questo campo può assumere i seguenti valori : 
' '  IL tipo documento non ha un contenuto scritto ed archiviato in un file di testo (es. DISEGNO TECNICO, FMEA, AUDIT etc.).
'X'  IL tipo documento ha un file che contiene fisicamente l'oggetto (testo, disegno....)
 :  : FLD T$PGGE **Pgm. Gestione**
Programma di gestione del documento. Questo programma viene richiamato, se specificato, ogni volta che si modifica lo stato di un documento e serve normalmente ad attivare delle azioni sull'oggetto che contiene fisicamente il documento (es. un file residente sul RISC per i disegni generati con il CAD)
 :  : FLD T$PRGM **Programma richiamo**
Campo controllato. Indica il programma da richiamare per la gestione del documento.
 :  : FLD T$STAM **Stampa autorizzata**
Questo campo può assumere i seguenti valori : 
' '  IL tipo documento non può essere stampato.
'X'  IL tipo documento può essere stampato.
 :  : FLD T$PGST **Pgm stampa**
Programma per la stampa del documento. Tale programma richiamerà tipicamente un programma di stampa per l'oggetto che fisicamente contiene il documento
 :  : FLD T$VISU **Visualizzazione autorizzazione**
Questo campo può assumere i seguenti valori : 
' '  Il tipo documento non può essere visualizzato a videoterminale.
'X'  Il tipo documento può essere visualizzato.
 :  : FLD T$PGVS **Programma di visualizzazione**
Campo controllato. Indica il programma da richiamare per la visualizzazione del documento.
 :  : FLD T$RIFP **Riferimento protetto**
Se questo campo assume valore 'X' il campo riferimento viene protetto
 :  : FLD T$NOT2 **Note strutturate**
Contiene il codice del tipo contenitore (tabella NSC) per la gestione delle note strutturate.
 :  : FLD T$CQ0B **Esponente di partenza**
Contiene il codice dell'esponente iniziale
