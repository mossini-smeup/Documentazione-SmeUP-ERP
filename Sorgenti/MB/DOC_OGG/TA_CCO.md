# CCO - Modalità di consegna
 :  : DEC T(ST) K(CCO)
## OBIETTIVO
Definire le modalità di consegna
## CONTENUTO DEI CAMPI
 :  : FLD T$DESC **Descrizione**
Descrive la modalità di consegna
 :  : FLD T$CCO1 **Modo consegna INTRA**
È la trascodifica della modalità di consegna con la tabella standard delle condizioni di consegna INTRA
 :  : FLD T$CCO2 **Costo Trasporto**
Se indicato, è il costo applicato ad ogni KG di massa legata al documento
 :  : FLD T$CCO3 **1=(-) 2=(+) Vend.**
Indica se l'importo ottenuto dall'applicazione dei calcoli, va sottratto o aggiunto al valore statistico per le vendite
 :  : FLD T$CCO4 **% Calcolo Valore Statistico Vendite**
Se indicata, è la percentuale che viene applicata all'importo per determinare il valore statistico per le vendite
 :  : FLD T$CCO6 **% Calcolo Valore Statistico Acquisti**
Se indicata, è la percentuale che viene applicata all'importo per determinare il valore statistico per gli acquisti
 :  : FLD T$CCO7 **1=(-) 2=(+) Acq.**
Indica se l'importo ottenuto dall'applicazione dei calcoli, va sottratto o aggiunto al valore statistico per gli acquisti
 :  : FLD T$CCO8 **Trasporto a nostro carico**
Riservato : utilizzare per indicare se il costo della spedizione è a carico dell'azienda così da poter determinare i documenti destinati al controllo fatture corrieri (in sviluppo).
Valori definiti :    1-trasporto a ns.carico (SV)
....
