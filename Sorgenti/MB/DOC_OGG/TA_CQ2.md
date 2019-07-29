# CQ2 - Stato rilascio/approvazione pr
 :  : DEC T(ST) K(CQ2)
## OBIETTIVO
Questa tabella contiene gli stati in cui cui può trovarsi un documento in relazione all'emissione, approvazione, rilascio.
## CONTENUTO DEI CAMPI
 :  : FLD T$BOZZ **Proposta**
Campo Proposta. Può assumere i seguenti valori : 
' '  Non esegue nessuna azione.
'X'  Lo stato del documento è da considerarsi al livello di 'PROPOSTA'.
 :  : FLD T$APPR **Approvata**
Campo Approvata. Può assumere i seguenti valori : 
' '  Non esegue nessuna azione.
'X'  Lo stato del documento è da considerarsi al livello di documento 'APPROVATO'.
 :  : FLD T$RILA **Rilascio-Distribuzione**
Campo Rilascio per la Distribuzione del Documento. Può assumere i seguenti valori : 
' '  Non esegue nessuna azione.
'X'  Lo stato del documento è da considerarsi al livello di documento 'RILASCIATO'.
È il controllo più importante in quanto solo il documento rilasciato diventa il documento ufficiale per l'AZIENDA.
Questo FLAG causa l'aggiornamento automatico dei documenti, cicli, procedure... al livello di modifica RILASCIATO più recente.
 :  : FLD T$LOCL **Lista Ordini Clienti**
Campo LISTA ORDINI CLIENTI. Può assumere i seguenti valori : 
' '  Non esegue nessuna azione.
'X'  Permette l'accesso agli ordini dei clienti aperti relativi al codice del documento che si stà modificando.
Tipicamente questo campo viene utilizzato per i documenti di tipo disegno
 :  : FLD T$LOPR **Lista Ordini Produzione**
Campo LISTA ORDINI PRODUZIONE. Può assumere i seguenti valori : 
' '  Non esegue nessuna azione.
'X'  Permette l'accesso agli ordini di produzione aperti, relativi al codice del documento che si sta modificando.
Tipicamente questo campo viene utilizzato per i documenti di tipo disegno.
 :  : FLD T$LOFO **Lista Ordini Ac/C.la**
Campo LISTA ORDINI ACQUISTO/CONTO LAVORO Può assumere i seguenti valori : 
' '  Non esegue nessuna azione.
'X'  Permette l'accesso agli ordini di acquisto e di conto lavoro, relativi al codice del documento che si sta modificando. Tipicamente questo campo viene utilizzato per i documenti di tipo disegno
Campo LISTA ORDINI ACQUISTO. Può assumere i seguenti valori : 
' '  Non esegue nessuna azione.
'X'  La distribuzione del documento viene associata alla lista di distribuzione dei documenti relativi agli 'ORDINI DI ACQUISTO'.
 :  : FLD T$CTDO **Contr.Esp.Modif.Doc.**
Campo Controllo Esponente di Modifica del Documento. Può assumere i seguenti valori : 
' '  Non esegue nessuna azione.
'X'  Viene attivata la gestione del livello di modifica del documento.
 :  : FLD T$AM01 **Aggiunta impedita**
Se questo campo assume il valore 'X', un documento che associato a questo stato non potrà subire nuove emissioni.
Questo campo serve ad impedire che ci siano nuove emissioni del documento quando ci siano già delle modifiche in corso.
