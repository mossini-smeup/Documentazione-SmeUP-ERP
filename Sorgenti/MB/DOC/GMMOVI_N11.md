# Struttura legami movimenti derivati
### Attività > Prelievi
Nel movimento di magazzino di prelievo : 
 * S§DTFF = N. registrazione attività
 * S§FLG2 = "2"

### Attività > Versamenti
Nel movimento di magazzino di versamento : 
 * S§DTFF = N. registrazione attività
 * S§FLG2 = "1"

### Versamenti > Prelievi
Nel movimento di magazzino di prelievo : 
 * S§DTFF = N. registrazione magazzino di versamento
 * S§FLG2 = "3"

Il logico che lega tutto questo è : 
GMMOVIGL
K1 - S§FLG2 (omessi il blanks)
K2 - S§DTFF

### Attività in milestone > Attività automatica
Nel movimento di magazzino di prelievo : 
 * W§TPRG  = blank
 * W§CODR = blank
 * W§NUMR  = N. attività milestone
 * W§FL08  = "P"/"S" flag di tipo operazione automatica

Il logico che lega tutto questo è : 
P5ATTIAL
K1 - W§TPRG
K2 - W§CODR
K3 - W§NUMR

**Nota Bene**; non ha omit nè c'è il flag 8 perchè potrebbe servire per altri raggruppamenti (es. per legare più operai) quello che individua il legame tra operazioni automatiche è : 
 * la presenza del flag 8 di operazione automatica
 * tipo raggruppamento = blanks
 * codice raggruppamento = blanks
