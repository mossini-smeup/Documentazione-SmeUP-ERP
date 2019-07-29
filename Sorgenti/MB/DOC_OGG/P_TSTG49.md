# OBIETTIVO
Data una stringa di testo su cui operare, la routine sostituisce una serie di caratteri contigui contenuti in essa con un altra serie di caratteri.
# PREREQUISITI
-
# PARAMETRI
## PARAMETRI DI INPUT
- Funzione :  _campo £G49FU_

- SOS Sostituzione caratteri
- SBL Sostituzione caratteri con BLANK finale
- VER Verifica stringa
- CON Conversione stringa
- CON_E Conversione stringa estesa

- Metodo :  _campo £G49ME_

Funzione SOS : 

- SSI stringa singola (default). Esegue la sostituzione una sola volta ridimensionando la stringa origine in base alle lunghezze dei caratteri sostituiti/sostituenti.
- SSI_TF stringa singola a testo fisso. Esegue la sostituzione una sola volta mantenendo fissa la lunghezza della stringa origine.
- SMU (SV) stringa multipla. Esegue la sostituzione per ogni occorrenza dei caratteri cercati ridimensionando la stringa origine in base alle lunghezze dei caratteri sostituiti/sostituenti.

- Stringa da elaborare :  _campo £G49SI_
- Stringa da sostituire :  _campo £G49SC_
- Stringa sostituente :  _campo £G49SD_
Funzione SBL : 

- SSI stringa singola (default). Esegue la sostituzione una sola volta ridimensionando la stringa origine in base alle lunghezze dei caratteri sostituiti/sostituenti.
- SMU (SV) stringa multipla. Esegue la sostituzione per ogni occorrenza dei caratteri cercati ridimensionando la stringa origine in base alle lunghezze dei caratteri sostituiti/sostituenti.

- Stringa da elaborare :  _campo £G49SI_
- Stringa da sostituire :  _campo £G49SC_
- Stringa sostituente :  _campo £G49SD_
Funzione VER : 

- APO Formatta apostrofi per comando (Raddoppio degli apostrofi).

- Stringa da elaborare :  _campo £G49SI_
Funzione CON : 

- L_C in minuscolo (Lower_Case)
- U_C in maiuscolo (Upper_Case)

- Stringa da elaborare :  _campo £G49SI_
Funzione CON_E : 

- L_C in minuscolo (Lower_Case)
- U_C in maiuscolo (Upper_Case)

- Stringa estesa :  _campo £G49SE_ (lungo 30k)
## PARAMETRI DI OUTPUT
- Stringa risultante :  _campo £G49SI_   (Eslusa funzione CON_E)
- Stringa estesa     :  _campo £G49SE_   (Solo funzione CON_E)
# ESEMPI DI CHIAMATA
EVAL      £G49FU='Funzione'
EVAL      £G49ME='Metodo'
EVAL      £G49SI=Stringa da elaborare
EVAL      £G49SC=Stringa da sostituire
EVAL      £G49SD=Stringa sostituente
EXSR      £G49
# NOTE
-
