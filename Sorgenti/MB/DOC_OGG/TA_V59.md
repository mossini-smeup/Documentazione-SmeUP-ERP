# V59 - Parametri anticipi
 :  : DEC T(ST) K(V59)
## OBIETTIVO
Definisce i parametri generali relativi agli anticipi.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM Elemento
È un elemento fisso.
 :  : FLD T$DESC Note
 :  : FLD T$V59A **Tipo documento per soli anticipi**
Contiene il tipo documento da utilizzare per gli acconti non legati ad un ordine che verranno recuperati alla prima spedizione del cliente.
 :  : FLD T$V59B **Sottosettore del modello**
Contiene il sottosettore del modello per gli acconti non legati ad un ordine che verranno recuperati alla prima spedizione del cliente.
 :  : FLD T$V59C **Modello per soli anticipi**
Contiene il modello per gli acconti non legati ad un ordine che verranno recuperati alla prima spedizione del cliente.
 :  : FLD T$V59D **Recupero per scenario**
Se attivo questo flag la spedizione recupererà solo gli acconti a parità di scenario altrimenti  verrano recuperati tutti gli acconti inseriti indipendentemente dallo scenario
