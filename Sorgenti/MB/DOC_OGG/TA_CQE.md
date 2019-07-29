# CQE - Caratterizzazioni non conformi
 :  : DEC T(ST) K(CQE)
DOCUMENTAZIONE IN FASE DI COMPLETAMENTO
## OBIETTIVO
Codificare le azioni intraprese a seguito di non conformità.
_9_Esempio : 
Difetto................ :   Dimensione lineare non corretta.
Causa.................. :   Mancata lubrificazione.
Grado di accertamento.. :   Molto probabile.
Tipo caratterizzazione. :   Scarto lotto.
## CONTENUTO DEI CAMPI
 :  : FLD T$TCOS __Tipo Costo__
Questo campo può assumere valori  :  1, 2, 3.
È il tipo costo a cui il programma si deve riferire nel collegamento con la 'Gestione Costi' del Gestionale, per la valorizzazione del particolare oggetto della non conformità.
 :  : FLD T$TCAL **Tipo Calcolo Costo**
Campo controllato dalla tabella 'CQ3' (Definizione Calcolo Costo). Permette di differenziare la valorizzazione del particolare non conforme in funzione della caratterizzazione della Non Conformità. Tale valorizzazione viene proposta in automatico nel campo 'Costo Unitario' della finestra 'Costi' della 'Gestione delle Non Conformità'.
 :  : FLD T$FORZ **Forzatura esito controllo**.
Campo forzatura 'Esito Controllo' del lotto interessato dalla non conformità.
' '  Non esegue nessun collegamento per la modifica dell'esito del controllo del lotto in cui è stata rilevata la non conformità.
'X'  Al termine della dichiarazione della Non Conformità si collega, nella 'Gestione Lotti', al lotto oggetto della N.C. onde permettere la modifica della causale di accettazione del lotto (Es. Lotto con N.C. rilevate dopo il collaudo) ed eventualmente definire le azioni da eseguire sulla successiva consegna.
 :  : FLD T$FORR **Forzatura esito controllo resp.**.
Campo forzatura 'Esito Controllo' del lotto responsabile della non conformità. Non sempre, infatti, il lotto su cui viene rilevata la non conformità è direttamente responsabile della stessa.
_9_Esempio :  Lotto lavorato di una fusione (articolo1) nel quale affiorano delle soffiature (articolo2=materia prima).
' '  Non esegue nessun collegamento per la modifica dell'esito del controllo del 'Lotto Responsabile' della non conformità.
'X'  Al termine della dichiarazione della Non Conformità si collega, nella 'Gestione Lotti', al lotto oggetto della N.C. onde permettere la modifica della causale di accettazione del lotto (Es. Lotto con N.C. rilevate dopo il collaudo) ed eventualmente definire le azioni da eseguire sulla successiva consegna.
 :  : FLD T$ESIT **Esito Negativo**
Indica che l'elemento assume risultato negativo
Si vedano le tabelle CQK e CQT.
È indicato come Responsabile della N.C. onde permettere la modifica della sua originaria causale di accettazione ed eventualmente la definizione delle azioni da eseguire sulla consegna successiva.
 :  : FLD T$CRI1 **Riclassifica 1/2/3**
Campo controllato dalla tabella 'CQ*CR' (Riclassifica causali N.C./ACC.).
Viene utilizzato nelle analisi statistiche.
 :  : FLD T$CRI2.T$CRI1 **Riclassifica 1/2/3**
 :  : FLD T$CRI3.T$CRI1 **Riclassifica 1/2/3**
