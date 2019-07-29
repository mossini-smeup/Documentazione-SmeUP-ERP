# D5F - Formule
 :  : DEC T(ST) K(D5F)
## OBIETTIVO
Contenere un insieme di formule per l'utilizzo tramite £FOR

## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM **Codice**
È costituito da un prefisso più il carattere '.'  e più due caratteri che specificano l'elemento della schiera, dove andrà caricato il risultato della formula (da 01 a 99).
Formule con lo stesso prefisso si considerano applicate alle medesime schiere di valori. Il numero massimo di formule con lo stesso prefisso è pari a 15 per limitazioni della £FOR.
_9_Es :           FORMUL.03
prefisso  <---->.<> codice elemento destino
 :  : FLD T$D5FA **Formula 1**
Primi 50 caratteri della formula.
La sintassi segue le specifiche della £FOR.
 :  : FLD T$D5FB **Formula 2**
Secondi 50 caratteri della formula.
La sintassi segue le specifiche della £FOR.
