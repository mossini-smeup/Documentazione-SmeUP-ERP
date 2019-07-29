# BRQ - Categorie di credito
 :  : DEC T(ST) K(BRQ)
## OBIETTIVI
-    Determina le modalità di controllo da utilizzare nella funzione di controllo del credito cliente.
## SOTTOSETTORI
Non gestiti
## CONTENUTO DEI CAMPI
 :  : FLD T$BRQA **Tipo controllo fido**
Definisce se un controllo fido deve essere **statico** (si considerano tutti i gli ordini aperti + le spedizioni in corso + le fatture non pagate) oppure **dinamico** (si considerano gli ordini in corso solo per la quota compresa nell'orizzonte).
 :  : FLD T$BRQB **Orizzonte fido dinamico**
È espresso in giorni.
 :  : FLD T$BRQC **Valore massimo documento**
È il limite di valore consentito per ciascun ordine.
 :  : FLD T$BRQD **Massimo numero di solleciti**
Numero massimo di solleciti ammessi.
 :  : FLD T$BRQE **Ritardo massimo fatture non pagate**
Numero massimo di giorni di ritardo nel pagamento fatture.
 :  : FLD T$BRQF **Percentuale di supero fido per emissione warning**
Percentuale da 01 a 99.
 :  : FLD T$BRQG **Percentuale di supero fido per blocco ordine**
Percentuale da 01 a 99.
 :  : FLD T$BRQH **Data di prossima revisione categoria di credito**
Data, superata la quale, sarà emessa una segnalazione per cambiare i paramteri caratteristici della categoria.
 :  : FLD T$BRQI **Categoria regole credito**
Settore di tabella nel quale sono raccolte le regole per la verifica del credito di un cliente.
