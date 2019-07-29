# C6D - Destinazione Non Conformità controllo fatture
 :  : DEC T(ST) K(C6D)
## OBIETTIVO
Indicare la destinazione di una "non conformità" generata nel controllo fatture di acquisto.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM **Codice**
Indica il codice di destinazione della "NON CONFORMITA"
 :  : FLD T$DESC **Descrizione**
 :  : FLD T$C6DA **Utente (**Gruppo)**
Indica l'utente destinatario della non conformità. È possibile definire anche un "gruppo utenti", inserendo '**' prima del codice gruppo (tabella B£*GU)
 :  : FLD T$C6DB **Lista di distribuzione**
Indica il sottosettore di una lista di distribuzione. La non conformità sarà indirizzata a tutti gli elementi della tabella NSLxx (xx=lista distribuzione) con oggetto 'UP','TAB£U','OJ*USRPRF' e TAJAU.
Da notare inoltre che è possibile inserire il campo anche in presenza del campo utente, in questo caso la destinazione della non conformità sarà l'utente e la lista.
 :  : FLD T$C6DC **Intestatario documento**
Se attivato, il messaggio viene inviato anche all'intestatario della fattura. Negli invii standard è valida solo per e-mail.
