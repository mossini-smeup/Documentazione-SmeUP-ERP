# CQY - Tipo griglia controlli
 :  : DEC T(ST) K(CQY)
## OBIETTIVO
Descrivere il significato dei campi legati alla griglia.
Collegare questi campi alle tabelle o ad archivi dati.
## CONTENUTO DEI CAMPI
 :  : FLD T$KYC1 **Codice 1**
È un elemento della tabella *CNTT e specifica il tipo della chiave.
 :  : FLD T$KYC2.T$KYC1 **Codice 2**
 :  : FLD T$KYC3.T$KYC1 **Codice 3**
 :  : FLD T$PAR1 __Parametro codice 1__
È il parametro aggiuntivo nel caso sia necessario per specificare ulteriormente la chiave.
_9_Esempio : 
Codice    : TA  --> Collegarsi alla gestione Tabelle
Parametro : CQQ --> Tabella 'CQQ' (Classi Funzionali)
 :  : FLD T$PAR2.T$PAR1 **Parametro codice 2**
 : FLD T$PAR3.T$PAR1 **Parametro codice 3**
 :  : FLD T$DES1 **Descrizione 1**
Fornisce una descrizione della chiave che sarà poi riportata nella videata di gestione del programma.
 :  : FLD T$DES2.T$DES1 **Descrizione 2**
 :  : FLD T$DES3.T$DES1 **Descrizione 3**
 :  : FLD T$OBB1 **Valore obbligatorio 1**
Il campo può assumere i seguenti valori : 
' '  Non viene richiesta obbligatoriamente la digitazione del campo nella fase di immissione dati in archivio.
'O'  Viene richiesta obbligatoriamente la digitazione del campo nella fase di immissione dati in archivio.
 :  : FLD T$OBB2.T$OBB1 **Valore obbligatorio 2**
 :  : FLD T$OBB3.T$OBB1 **Valore obbligatorio 3**
 :  : FLD T$CNOT **Contenitore Note**
Campo controllato dalla tabella 'NSC' (Note strutturate - contenitori). Indirizza il programma di gestione delle note strutturate nel contenitore associato all'archivio.
