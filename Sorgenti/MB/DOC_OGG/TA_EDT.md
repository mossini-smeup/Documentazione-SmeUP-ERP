# EDT - Messaggi inviati
## OBIETTIVI
Definire le caratteristiche di trasmissione di un messaggio
## SOTTOSETTORI
Non gestiti
## INTRODUZIONE
L'elemento di tabella è il codice messaggio in fase di trasmissione. Lo stesso elemento deve essere presente nella tabella dei codici messaggi ricevuti ed esso costituisce il riferimento base nella gestione di Mail-Up.
Attraverso il codice messaggio definiamo la tipologia del messaggio stesso (origine, destinazione, metodo di elaborazione, etc.).
## CONTENUTO DEI CAMPI
 :  : FLD T$DESC Descrizione
 :  : FLD T$EDTI __Indirizzo origine assunto__
In fase di creazione del messaggio determina l'indirizzo origine.
Tipo oggetto TA tabella EDI.
 :  : FLD T$EDTA __Numeratore messaggi__
In fase di creazione del messaggio determina la numerazione del lotto.
Tipo oggetto TA tabella CRN sottosettore ED.
 :  : FLD T$EDTB __Metodo lista di distribuzione__
In fase di creazione del messaggio determina il o i destinatari del messaggio.
 :  : FLD T$EDTC __Parametro lista di distribuzione__
Parametro associato al metodo lista di distribuzione.
 :  : FLD T$EDTD __Griglia ricerca__
Determina la griglia di controllo per i 3 codici di ricerca utili per le parzializzazioni.
 :  : FLD T$EDTT __Tipo e nome tracciato__
Determina il tracciato di riferimento della parte dati del messaggio necessario alla visualizzazione, controllo, trasformazione (ALIAS) e applicazione dello stesso.
Può riferirsi ad un file, ad una tabella, ad un tracciato utente, a dati da tabella e ad attributi oggetto.
 :  : FLD T$EDTS.T$EDTT  __Nome tracciato__
 :  : FLD T$EDTF __Stato dopo invio__
È il valore che assume lo stato del messaggio dopo la trasmissione. Attraverso lo stato del messaggio si gestiscono tutte le fasi successive di elaborazione. Tipo oggetto TA tabella B£W sottosettore E2.
## Invio automatico
In fase di creazione permette di inviare il messaggio direttamente al destinatario con le modalità di trasmissione/ricezione definite dal metodo di comunicazione (EDC) derivato dall'indirizzo di destinazione (EDI).
 :  : FLD T$EDTG __Congruenza per lotto__
Durante le fasi elaborative in fase di scelta messaggio permette di riferirsi ad un intero lotto messaggi.
 :  : FLD T$EDTE __Contesto alias__
Definisce il contesto di alias attraverso il quale, i programmi di generazione flussi edi, reperiscono i codici che devono essere transcodificati tra interni ed esterni per l'invio al destinatario del flusso. Un esempio di questo è rappresentato dall'invio del flusso di delivery note, dove codici di destinazione merce vengono transcodificati con quelli noti al destinatario.
 :  : FLD T$EDTH __Test flag__
Definisce se il flusso edi in trasmissione è di tipo "test", quindi il flagtest definito all'interno del tracciato da trasmettere deve essere valorizzato con il valore di test.
Questo flag viene utilizzato tipicamente durante i periodi di avviamento di una nuova trasmissione edi, in cui i flussi non hanno valore effettivo.
