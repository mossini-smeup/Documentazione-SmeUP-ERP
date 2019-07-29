# A£1 - Personalizzazione funzioni A£
 :  : DEC T(ST) K(A£1)
## OBIETTIVO
Definisce i parametri che guidano la gestione delle traduzioni in lingua.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM **Codice**
È un campo fisso '*'
 :  : FLD T$DESC **Descrizione**
Bianco

 :  : FLD T$A£1F Suffisso exit ambiti
Indica il suffisso x della exit A£TR00_x in cui, mediante schiere, sono definiti gli ambiti utilizzabili e modificabili sul sistema, la loro associazione alle librerie e le lingue gestite sul sistema.

 :  : FLD T$A£1H Precompila traduzioni
Se selezionato, quando viene scritto un nuovo record in A£TRDE0F se manca la traduzione vengono scandite le traduzioni esistenti per la stessa frase e se trovato qualcosa ne viene ereditata la traduzione. Per le regole con cui questo viene effettuato verificare la documentazione tecnica in testa al programma A£TR13B.

 :  : FLD T$A£1I Estrazione automatica
Se selezionato, per alcuni oggetti viene automaticamente estratto l'A£TROR0F e preparato il relativo A£TRDE0F per le lingue gestite a sistema (dalla exit definita in T$A£1F).
Attenzione :  funziona per l'estrazione (quindi inserimento, copia, modifica degli oggetti), non per la cancellazione :  lo spegnimento delle frasi cancellate avverrà alla prima riestrazione di massa.
Al momento sono gestiti : 
 * Elementi di tabella.

 :  : FLD T$A£1J Exit estrazione frasi
Indica la exit di default del programma A£TR01 per l'estrazione delle frasi.
Tale exit viene utilizzata per determinare gli oggetti da cui estrarre frasi e per eseguire eventuali operazioni personali al termine dell'estrazione.

 :  : FLD T$A£1K Exit trace
Indica la exit di default del programma A£A£B0 che permette di gestire per quali utenti e con quale valore di priorità va memorizzata la tracciatura delle traduzione.
Va utilizzato in connubio con il campo Tipo trace.
Per maggiori dettagli si veda il sorgente di esempio A£A£BTXX.

