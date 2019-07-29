# C£S - Definizione raggruppamenti
Permette di assegnare esplicitamente ad un oggetto fino a 9 famiglie di raggruppamento. Questo abbinamento viene utilizzato per la costruzione di sintesi (es. se abbiamo un piano di previsione di vendita per articolo e attraverso i raggruppamenti abbiamo abbinato gli articoli ai tipi imballo possiamo ottenere una sitesi del piano per tipo imballo).
Oltre all'assegnazione esplicita possiamo anche indicare N. attributi dell'oggeto da utilizzare come famiglia di
raggruppamento.
 :  : DEC T(ST) K(C£S)
## SOTTOSETTORI
## CONTENUTO DEI CAMPI
 :  : FLD T$KYC1 **Cod. famiglia 1**
Tipo oggetto a cui riferire la famiglia di raggruppamento
 :  : FLD T$PAS1 **Parametro 1**
Parametro oggetto a cui riferire la famiglia di raggruppamento
 :  : FLD T$KYC2 **Cod. famiglia 2**
Vedi T$KYC1
 :  : FLD T$PAS2 **Parametro 2**
Vedi T$PAS1
 :  : FLD T$KYC3 **Cod. famiglia 3**
Vedi T$KYC1
 :  : FLD T$PAS3 **Parametro 3**
Vedi T$PAS1
 :  : FLD T$KYC4 **Cod. famiglia 4**
Vedi T$KYC1
 :  : FLD T$PAS4 **Parametro 4**
Vedi T$PAS1
 :  : FLD T$KYC5 **Cod. famiglia 5**
Vedi T$KYC1
 :  : FLD T$PAS5 **Parametro 5**
Vedi T$PAS1
 :  : FLD T$KYC6 **Cod. famiglia 6**
Vedi T$KYC1
 :  : FLD T$PAS6 **Parametro 6**
Vedi T$PAS1
 :  : FLD T$KYC7 **Cod. famiglia 7**
Vedi T$KYC1
 :  : FLD T$PAS7 **Parametro 7**
Vedi T$PAS1
 :  : FLD T$KYC8 **Cod. famiglia 8**
Vedi T$KYC1
 :  : FLD T$PAS8 **Parametro 8**
Vedi T$PAS1
 :  : FLD T$KYC9 **Cod. famiglia 9**
Vedi T$KYC1
 :  : FLD T$PAS9 **Parametro 9**
Vedi T$PAS1
 :  : FLD T$PGMC **Programma controllo**
Premette di introdurre regole particolari di controllo nella gestione
 :  : FLD T$DAVA **Data validita'**
Se diverso da blank attiva la gestione dei raggruppamenti per data di validità
 :  : FLD T$SSOA **Attributi oggetto**
Indica il sottosettore della tabella C£Z dove sono definiti gli attributi dell'oggetto che possono essere utilizzati dai programmi di raggruppamento esattamente alla stessa maniera di come verrebbero trattate le famiglie di raggruppamento associate esplicitamente nella gestione (programma C£SI01)

