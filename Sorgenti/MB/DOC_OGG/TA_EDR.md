# EDR - Messaggi ricevuti
## OBIETTIVI
Definire le caratteristiche di ricevimento di un messaggio
## SOTTOSETTORI
Non gestiti
## INTRODUZIONE
L'elemento di tabella è il codice messaggio in fase di ricevimento. Lo stesso elemento deve essere presente nella tabella dei codici messaggi trasmessi ed esso costituisce il riferimento base nella gestione di Mail-Up.
Attraverso il codice messaggio, definiamo la tipologia del messaggio stesso (origine, destinazione, metodo di elaborazione, etc.).
## CONTENUTO DEI CAMPI
 :  : FLD T$DESC Descrizione
 :  : FLD T$EDRA __Griglia ricerca__
Determina la griglia di controllo per i 3 codici di ricerca utili per le parzializzazioni.
 :  : FLD T$EDRK __Commit__
Attiva il controllo di sincronia.
 :  : FLD T$EDR1 __Tipo e nome tracciato.__
Determina il tracciato di riferimento della parte dati del messaggio necessario a visualizzazione, controllo, trasformazione (ALIAS) e applicazione dello stesso.
Può riferirsi ad un file, ad una tabella, ad un tracciato utente, a dati da tabella  e ad attributi oggetto.
 :  : FLD T$EDR2.T$EDR1  __Nome tracciato__
 :  : FLD T$EDRC __Contesto__
Determina le relazioni esistenti tra due oggetti.
Tipo oggetto TA tabella C£K.
 :  : FLD T$EDRM __Metodo di controllo/applicazione__
Nome programma che verifica la bontà dei dati contenuti nel messaggio per poi essere applicati.
 :  : FLD T$EDRP __Parametro del metodo di controllo/applicazione__
Eventuale parametro.
 :  : FLD T$EDRF __Stato dopo applicazione__
È il valore che assume lo stato del messaggio dopo l'applicazione. Attraverso lo stato del messaggio si gestiscono tutte le fasi successive di elaborazione.
Tipo oggetto TA tabella B£W sottosettore E2.
 :  : FLD T$EDRG __Congruenza per lotto__
Durante le fasi elaborative in fase di scelta messaggio permette di riferirsi ad un intero lotto messaggi, diversamente le elaborazioni avverranno sul singolo record indirizzato.
Questo significa ad esempio che l'applicazione del messaggio, possa avvenire : 
- sempre sull'intero lotto, se scelta la congruenza per lotto
- sul singolo record, se non scelta la congruenza per lotto
