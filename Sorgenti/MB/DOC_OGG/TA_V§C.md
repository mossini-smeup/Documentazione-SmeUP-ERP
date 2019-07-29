# V§C - Comuni
 :  : DEC T(ST) K(V§C)
## OBIETTIVO
Lo scopo della V§C è quello di dare una tabella standard che contenga le informazioni sui comuni.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM Codice
È il codice del comune. Esso è utilizzato nella costruzione del codice fiscale :  gli ultimi 5 caratteri del codice fiscale sono rispettivamente il codice del comune (primi 4) e un carattere di controllo.
Per gestire il caso dei cittadini italiani nati all'estero sono codificate anche le nazioni estere (elementi Z*).
 :  : FLD T$DESC Descrizione
Campo descrittivo del comune.
 :  : FLD T$V§CA **Provincia**
Indica la provincia di appartenenza.
 :  : FLD T$V§CB **CAP / ZIP**
Indica il CAP del comune.
 :  : FLD T$V§CC **Prefisso telefonico**
Indica il prefisso telefonico del comune.
 :  : FLD T$V§CD **Cod.ISTAT del comune**
Indica il codice ISTAT del comune. Le prime 3 cifre indicano la provincia di appartenenza, le ultime sono univoche per comune nell'ambito della provincia.
