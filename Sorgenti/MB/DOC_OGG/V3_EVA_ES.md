_3_La scritta in verde evidenzia il contenuto di una variabile

# Attributi e Assegnazione
_2_Assegno alla variabile di contesto "AZI" il valore 01 e oggetto CNAZI
 :  : PAR L(TAB) T(**Assegnazione**)
- CO.AZI|d=|CNAZI;01

&CO.AZI==CNAZI;01
_2_Documentiamo la variabile appena impostata ritornando l'intestazione, il valore, la descrizione
 :  : PAR L(TAB)
- Intestazione|Valore|Significato
-  CO.AZI**%OD.I/11**| CO.AZI| CO.AZI**%OD.I/01**
- _3_&CO.AZI%OD.I/11|_3_&CO.AZI|_3_&CO.AZI%OD.I/01

_2_Accediamo alla variabile attraverso l'istanza
 :  : PAR L(TAB)
- Intestazione|Valore|Significato
-  KI.CNAZI.01**%OD.I/11**| KI.CNAZI.01| KI.CNAZI.01**%OD.I/01**
- _3_&KI.CNAZI.01%OD.I/11|_3_&KI.CNAZI.01|_3_&KI.CNAZI.01%OD.I/01

_2_Accediamo all'attributo di secondo livello Provincia e documentiamo la Regione
 :  : PAR L(TAB) T(**Provincia** _3_&CO.AZI%I/05** _3_&CO.AZI%OD.I/05**)
- Intestazione|Valore|Significato
-  CO.AZI**%I/05**%OI.I/T$V§PA| CO.AZI**%I/05**%I/T$V§PA| CO.AZI**%I/05**%OD.I/T$V§PA
- _3_&CO.AZI%I/05%OI.I/T$V§PA|_3_&CO.AZI%I/05%I/T$V§PA|_3_&CO.AZI%I/05%OD.I/T$V§PA

_2_Accediamo all'attributo di terzo livello Regione e documentiamo la Nazione
 :  : PAR L(TAB) T(**Regione** _3_&CO.AZI%I/05%I/T$V§PA** _3_&CO.AZI%I/05%OD.I/T$V§PA**)
- Intestazione|Valore|Significato
-  CO.AZI**%I/05**%I/T$V§PA**%OI.I/T$V§RA**| CO.AZI**%I/05**%I/T$V§PA**%I/T$V§RA**|    CO.AZI**%I/05**%I/T$V§PA**%OD.I/T$V§RA**
- _3_&CO.AZI%I/05%I/T$V§PA%OI.I/T$V§RA|_3_&CO.AZI%I/05%I/T$V§PA%I/T$V§RA|   _3_&CO.AZI%I/05%I/T$V§PA%OD.I/T$V§RA

_2_Definisco un alias per accedere all'attributo di terzo livello
&CO.REG==|&CO.AZI%I/05%I/T$V§PA
 :  : PAR L(TAB) T(**Regione** _3_&CO.REG** _3_&CO.REG%I/T$DESC**)
- Intestazione|Valore|Significato
-  CO.REG**%OI.I/T$ELEM**| CO.REG**%I/T$V§RA**|    CO.REG**%OD.I/T$V§RA**
- _3_&CO.REG%OI.I/T$ELEM|_3_&CO.REG%I/T$V§RA|   _3_&CO.REG%OD.I/T$V§RA


_2_Accediamo all'attributo di quarto livello Nazione e documentiamo la sua Appartenenza
 :  : PAR L(TAB) T(**Nazione** _3_&CO.AZI%I/05%I/T$V§PA%I/T$V§RA** _3_&CO.AZI%I/05%I/T$V§PA%OD.I/T$V§RA)
- Intestazione|Valore|Significato
-  CO.AZI**%I/05**%I/T$V§PA**%I/T$V§RA**%OI.I/T$V§NB| CO.AZI**%I/05**%I/T$V§PA**%I/T$V§RA**%I/T$V§NB|    CO.AZI**%I/05**%I/T$V§PA**%I/T$V§RA**%OD.I/T$V§NB
- _3_&CO.AZI%I/05%I/T$V§PA%I/T$V§RA%OI.I/T$V§NB|_3_&CO.AZI%I/05%I/T$V§PA%I/T$V§RA%I/T$V§NB|   _3_&CO.AZI%I/05%I/T$V§PA%I/T$V§RA%OD.I/T$V§NB

_2_E così via...

_2_Assegno alla variabile già dichiarata "AZI" il valore 02 e oggetto CNAZI
 :  : PAR L(TAB) T(**Assegnazione**)
- CO.AZI|d=|CNAZI;02

&CO.AZI==CNAZI;02
_2_Documentiamo la variabile appena impostata ritornando l'intestazione, il valore, la descrizione
 :  : PAR L(TAB)
- Intestazione|Valore|Significato
-  CO.AZI**%OD.I/11**| CO.AZI| CO.AZI**%OD.I/01**
- _3_&CO.AZI%OD.I/11|_3_&CO.AZI|_3_&CO.AZI%OD.I/01

_2_Accediamo all'attributo di secondo livello Provincia e documentiamo la Regione
 :  : PAR L(TAB) T(**Provincia** _3_&CO.AZI%I/05** _3_&CO.AZI%OD.I/05**)
- Intestazione|Valore|Significato
-  CO.AZI**%I/05**%OI.I/T$V§PA| CO.AZI**%I/05**%I/T$V§PA| CO.AZI**%I/05**%OD.I/T$V§PA
- _3_&CO.AZI%I/05%OI.I/T$V§PA|_3_&CO.AZI%I/05%I/T$V§PA|_3_&CO.AZI%I/05%OD.I/T$V§PA

_2_Accediamo all'attributo di terzo livello Regione e documentiamo la Nazione
 :  : PAR L(TAB) T(**Regione** _3_&CO.AZI%I/05%I/T$V§PA** _3_&CO.AZI%I/05%OD.I/T$V§PA**)
- Intestazione|Valore|Significato
-  CO.AZI**%I/05**%I/T$V§PA**%OI.I/T$V§RA**| CO.AZI**%I/05**%I/T$V§PA**%I/T$V§RA**|    CO.AZI**%I/05**%I/T$V§PA**%OD.I/T$V§RA**
- _3_&CO.AZI%I/05%I/T$V§PA%OI.I/T$V§RA|_3_&CO.AZI%I/05%I/T$V§PA%I/T$V§RA|   _3_&CO.AZI%I/05%I/T$V§PA%OD.I/T$V§RA

_2_Accediamo all'attributo di quarto livello Nazione e documentiamo la sua Appartenenza
 :  : PAR L(TAB) T(**Nazione** _3_&CO.AZI%I/05%I/T$V§PA%I/T$V§RA** _3_&CO.AZI%I/05%I/T$V§PA%OD.I/T$V§RA)
- Intestazione|Valore|Significato
-  CO.AZI**%I/05**%I/T$V§PA**%I/T$V§RA**%OI.I/T$V§NB| CO.AZI**%I/05**%I/T$V§PA**%I/T$V§RA**%I/T$V§NB|    CO.AZI**%I/05**%I/T$V§PA**%I/T$V§RA**%OD.I/T$V§NB
- _3_&CO.AZI%I/05%I/T$V§PA%I/T$V§RA%OI.I/T$V§NB|_3_&CO.AZI%I/05%I/T$V§PA%I/T$V§RA%I/T$V§NB|   _3_&CO.AZI%I/05%I/T$V§PA%I/T$V§RA%OD.I/T$V§NB

_2_E così via...

_2_Assegno alla variabile di contesto "PRO" il valore MI e oggetto CO.AZI%OO.I/05
 :  : PAR L(TAB) T(**Assegnazione**)
- CO.PRO|d=|CO.AZI%OO.I/05;MI

&CO.PRO==&CO.AZI%OO.I/05;MI
_2_Documentiamo la variabile appena impostata ritornando l'intestazione, il valore, la descrizione
 :  : PAR L(TAB)
- Intestazione|Valore|Significato
-  CO.PRO**%OD.J/S01**| CO.PRO| CO.PRO**%OD.I/T$ELEM**
- _3_&CO.PRO%OD.J/S01|_3_&CO.PRO|_3_&CO.PRO%OD.I/T$ELEM


# Ambiente
 :  : PAR L(TAB)
- Azienda|Utente|Data|Data formattata|Ora
-  AM.AZ| AM.UT| AM.DT| AM.DF | AM.HR
- _3_&AM.AZ%OV.|_3_&AM.UT%OV.|_3_&AM.DT%OV.|_3_&AM.DF%OV.|_3_&AM.HR%OV.
- _3_&AM.AZ|_3_&AM.UT|_3_&AM.DT|_3_&AM.DF|_3_&AM.HR


# Sistema
 :  : PAR L(TAB) T(**Librerie**)
- Dati|Oggetti|Personalizzazioni
-  LIBDAT| SMEUPOBJ| LIBPER
- _3_&LIBDAT|_3_&SMEUPOBJ|_3_&LIBPER

 :  : PAR L(TAB) T(**Librerie**)
-  Libreria BRARTI0F
- _3_&SY.LIB;BRARTI0F
-  Libreria Membro BRARTI0F in SRCDB
- _3_&SY.LIB;SRCDB;BRARTI0F


# Date variabili
 :  : PAR L(TAB) T(**Oggi**)
- Variabile|Valore
-  D8.OGI| _3_&D8.OGI
-  D8.OGI.D| _3_&D8.OGI.D
-  D8.OGI.d| _3_&D8.OGI.d
-  D8.OGI.Y| _3_&D8.OGI.Y
-  D8.OGI.y| _3_&D8.OGI.y

