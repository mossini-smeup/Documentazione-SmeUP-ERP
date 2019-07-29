### Obiettivo
Tenere sotto controllo la movimentazione iva al fine delle quadrature contabili.
L'analisi può essere effettuata secondo due criteri : 
* Controllo Movimentazione Conti IVA :  vengono estratte tutte le registrazioni di pura iva e le registrazioni ove viene usato un conto iva, come conto di generale (giroconti o altro). I conti iva vengono ripresi dalla tabella C5U, prendendo in considerazione tutti gli elementi che iniziano con la dicitura "IVA". Da questo controllo vengono esclusi i movimenti con conto, tipo registrazione e causale definiti nella tabella C5U elemento IVAGC (Giroconto iva liquidazione).
* Differenza Data Registrazione - Data Competenza :  Controllo ove la data registrazione è differente dalla data competenza, prendendo in considerazione sia i movimenti con data registrazione pari al periodo selezionato sia i movimenti con data competenza pari al periodo selezionato. Per periodo differente si intende anno/mese.
