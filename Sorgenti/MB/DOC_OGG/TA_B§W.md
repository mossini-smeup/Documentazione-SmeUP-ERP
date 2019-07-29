# B§W - Condizioni di conversione
 :  : DEC T(ST) K(B§W)
## OBIETTIVO
Definire le condizioni per le tabelle da convertire.
## CONTENUTO DEI CAMPI
 :  : FLD T$DESC **Descrizione**
Descrive la tabella da convertire.
 :  : FLD T$B§WA **Conversione sospesa**
È un elemento V2SI/NO :  permette di sospendere la conversione della tabella. La tabella viene interamente saltata.
 :  : FLD T$B§WB **Elimina contenuto att.**
È un elemento V2SI/NO :  permette di effettuare l'eliminazione preliminare del contenuto della tabella ad ogni esecuzione.
 :  : FLD T$B§WC **Aggiungere**
È un elemento V2SI/NO :  permette di aggiungere gli elementi non esistenti in tabella.
 :  : FLD T$B§WD **Modificare**
È un elemento V2SI/NO :  permette di modificare gli elementi già esistenti in tabella.
 :  : FLD T$B§WE **Usare alias**
È un elemento TAB£K :  permette di effettuare una trascodifica degli elementi originali durante la conversione. Es. ricodifica del piano dei conti, riconduzione a codici standard, ecc.
 :  : FLD T$B§WF **Condizioni**
 :  : FLD T$B§WG **Scrittura Alias?**
Se compilato con SI, il programma di conversione gestisce la scrittura di tale alias. Il programma di conversione deve ovviamente gestire questo parametro, sia in aggiunta che in modifica, che in cancellazione. Se lasciato blanks la scrittura dell'alias è a carico dell'utente.
