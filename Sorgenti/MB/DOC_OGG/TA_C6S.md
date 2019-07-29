# C6S - Spese aggiuntive controllo fatture
 :  : DEC T(ST) K(C6S)
## OBIETTIVO
Definisce tutte le spese che caratterizzaziono il controllo fatture di acquisto. Ad ogni spesa è possibile legare gli oggetti della rispettiva analitica, mediante i parametri della tabella.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM **Codice**
È l'elemento che definisce la spesa.
 :  : FLD T$DESC **Descrizione**
Descrizione della spesa
 :  : FLD T$C6SA  **Spesa automatica**
Indica se la spesa viene ripresa automaticamente in immissione.
 :  : FLD T$C6SB  **Codice IVA**
È il codice IVA associato alla spesa. Viene assunto in immissione e controllata la congruenza con quello immesso in modifica.
 :  : FLD T$C6SC  **Conto contabile**
È il conto associato alla spesa. Viene assunto in immissione e controllata la congruenza con quello immesso in modifica.
 :  : FLD T$C6SD  **Non conformità**
Attiva una non conformità di blocco pagamento fattura, per validazione spesa
