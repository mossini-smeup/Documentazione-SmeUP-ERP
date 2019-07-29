# C£R - Risposte
 :  : DEC T(ST) K(C£R)
## OBIETTIVO
Catalogare in sottosettori le scelteche si possono presentare come risposta alle domande. Alla risposta potranno essere associati parametri aggiuntivi e commenti specifici.
## SOTTOSETTORI
Permettono di separare i gruppi di risposte
## CONTENUTO DEI CAMPI
 :  : FLD T$C£RT **Tipo opzione**
Indica se l'opzione aggiuntiva alla risposta deve essere controllata come oggetto presente sul sistema : 
-    Articoli
-    Attrezzature
-    Modalità di pagamento
-    Altra tabella a piacere
Il valore ** indica che è ammesso un valore di opzione non controllato. Si userà tale valore per indicare una opzione libera.
 :  : FLD T$C£RP **Parametro tipo opzione**
Se indicata una tabella permette di definire il nome di tale tabella.
 :  : FLD T$C£RO **Gestione opzione N/O**
N =  Non si presenta
O =  Obbligatoria
Indica che per questa risposta è obbligatoria la compilazione del valore nel campo opzione. Questo valore potrà essere controllato o meno in funzione delle altre caratteristiche della tabella.
 :  : FLD T$C£RN **Gestione note**
.    S = Si
Permette l'associazione delle note libere alla risposta
.    V = Verifica
Permette l'associazione delle note libere alla risposta; all'emissione del formato verifica la presenza di commenti.
Si segnala che la verifica rallenta l'emissione dei formati.
 :  : FLD T$C£RA **Nota assunta**
Valore assunto se non diversamente specificato per il campo nota. Poichè il contenuto del campo nota è variabile, potremo specificare nel valore assunto, ad esempio, il codice del materiale associato ad una scelta ecc.
 :  : FLD T$C£RQ **Valore assunto**
Valore scritto nel record della risposta.
 :  : FLD T$C£RV **Quantità assunta**
Valore scritto nel record della risposta. Utilizzato, ad esempio, come quantità nella costruzione della distinta.
 :  : FLD T$C£R0 **Gestione valore N/O**
N =  Non si presenta
O =  Obbligatorio
 :  : FLD T$C£R1 **Gestione quantità N/O**
N =  Non si presenta
O =  Obbligatorio
