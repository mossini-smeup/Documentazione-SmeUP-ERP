# GM2 - Parametrizzazione packing list
## OBIETTIVO
Impostare i parametri che guidano la preparazione del packing list
## CONTENUTO DEI CAMPI
 :  : FLD T$GM2A__ Tipo documento richiesta di movimentazione__
È un elemento della tabella GMO.
Definisce il tipo di richiesta di movimentazione creata in estrazione del ciclo attivo.
 :  : FLD T$GM2B __Contenitore note__
È un elemento della tabella NSC.
Definisce il contenitore delle note della testata di spedizione (SV).
 :  : FLD T$GM2C __Tipo collo__
È un elemento della tabella GMD.
Definisce il tipo di collo che verrà utilizzato nella creazione dei colli del packing list.
 :  : FLD T$GM2D __Tipo e parametro sessione__
Definiscono l'oggetto (facoltativo) a cui si intesterà la sessione nella preparazione dei colli.
 :  : FLD T$GM2F __Imballo solo su assegnati__
È un elemento V2 SI/NO :  se impostato, la modalità di spedizione sarà con trasferimento ad un area specifica. In questo caso si potrà imballare solo la quantità assegnata.
 :  : FLD T$GM2G __S.S.B£J Azioni PK__
È il sottosettore delle tabella B£J che contiene le azioni eseguibili durante la creazione del packing list.
 :  : FLD T$GM2M __Gest.CORD righe RRIM__
Se impostato a 1, viene riportato in fase di creazione sulla riga del RRIM il CORD del documento origine. Questo verrà utilizzato dal programma dei viaggi per la creazione dei documenti di destinazione.
 :  : FLD T$GM2N __Stato Massimo TRIM PK__
Se impostato, viene utilizzato come stato massimo dopo il quale le quantità, sia richieste che preparate, vengono bloccate e quindi non più modificabili dai programmi che gestiscono il packing list.
 :  : FLD T$GM2O __Suf.Pgm Agg.terzisti__
Se impostato, viene abilitato nel programma gestione viaggi il tasto funzionale F19, che permette di gestire eseguire la chiamata al programma utente V5FUTRI_X.
L'esempio presente nella libreria sorgenti (X=Z) gestisce lo scarico ordini terzisti dal programma viaggi creando automaticamente le bolle entrata da conto lavoro.
 :  : FLD T$GM2P __Suf.Pgm Creazione automatica PK__
Se impostato viene nel programma di estrazione interattiva ordini viene chiamata il programma GMPK09C_X che si occupa di creare automaticamente i colli della spedizione.
L'esempio presente nella libreria sorgenti (X=Z) genera automaticamente i colli della spedizione, basandosi sulla gestione imballi, definta tramite la tabella GMB e la /COPY £G44.
 :  : FLD T$GM2Q __Presenza doppia unità misura__
È un elemento V2 SI/NO :  se impostato, nella  gestione documento origine da packing list, vengono presentate con possibilità di gestione la quantità in unità misura di magazzino e in quella esterna.
 :  : FLD T$GM2R __Quantità riferimento in unità di misura esterna__
È un elemento V2 SI/NO :  se impostato, verrà usata nel confezionamento la quantità in unità di misura esterna.
 :  : FLD T$GM2S __Gruppo fonti Giacen.__
Se viene specificato un gruppo fonti nei programmi abilitati del packing list, viene ripresa la disponibilità trovata nella quantità evasa.
 :  : FLD T$GM2T __Ges.Dettaglio Riga.__
Se impostato a '1' nella gestione del packing list, verrà sempre presentato il dettaglio della riga anzichè il dettaglio per articolo.
 :  : FLD T$GM2U __Agg. da PK Righe V5.__
Se impostato verrà aggiornata, in caso di gestione per riga di V5, la quantità della riga. La quantità aggiornata sarà quella specificata dal valore di questo campo.
 :  : FLD T$GM2V __Can.Righe V5 con Qtà 0.__
Viene utilizzato solo se si esegue aggiornamento righe V5.
In questo caso, se una riga non è stata preparata mediante Packing List, verrà fisicamente cancellata dal documento in questione.
