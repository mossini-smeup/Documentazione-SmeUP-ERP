# CQM - Procedure Manuale qualità
 :  : DEC T(ST) K(CQM)
## OBIETTIVO
Codificare le procedure interne e/o esterne utilizzate in azienda per la gestione della qualità.
Legare alla procedura un responsabile emittente e la data di emissione.
## CONTENUTO DEI CAMPI
 :  : FLD T$DOCU **Tipo Documento/proc.**
Campo controllato dalla tabella 'CQ0' (Tipo documento - Gestione). Identifica la tipologia del documento e le modalità di gestione dello stesso.
 :  : FLD T$NORM **Riferim.norma I/E**
Campo controllato dalla tabella 'CQ*RP' (Riferimento Norma int./esterna). Identifica la Norma di riferimento per la procedura.
 :  : FLD T$SEZI __Sezione Manuale__
Campo controllato dalla tabella 'CQ*SZ' (Sezioni Manuale Qualità). Identifica la Sezione di riferimento per la procedura.
 :  : FLD T$ENTE **Ente Emittente**
Campo controllato dalla tabella, legata all'archivio settato dalla tabella. Normalmente viene collegata con l'archivio dei Centri o Servizi. Esso definisce il settore o l'ente responsabile che ha emesso la norma.
 :  : FLD T$DATA **Data prima emissione**
Immettere la data della prima emissione della procedura.
 :  : FLD T$CQMV **Visualizzazione**
Questo campo può assumere i seguenti valori : 
' '  Non permette la visualizzazione a videoterminale del contenuto della norma.
'X'  Permette di visualizzare, nella fase di interrogazione a terminale, il contenuto della norma.
 :  : FLD T$CQMS **Stampa**
Questo campo può assumere i seguenti valori : 
' '  Non permette la stampa della norma visualizzata a terminale.
'X'  Permette di stampare il contenuto della norma visualizzata a terminale.
 :  : FLD T$GEST **Gestione autorizzata**
Questo campo può assumere i seguenti valori : 
' '  Non permette la gestione o la modifica della norma visualizzata a terminale.
'X'  Permette di modificare il contenuto della norma visualizzata a terminale.
 :  : FLD T$RIC1 **Riclassifica 1/2/3**
Campo controllato nella tabella 'CQ*RQ' (Riclassifica procedure qualità). Permette di riclassificare in vario modo la procedura.
 :  : FLD T$RIC2.T$RIC1 **Riclassifica 1/2/3**
 :  : FLD T$RIC3.T$RIC1 **Riclassifica 1/2/3**
