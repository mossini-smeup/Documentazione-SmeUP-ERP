# ESDIS     -  TIPO ESPLOSIONE CICLO
Definisce le modalità di scansione in esplosione di un ciclo di produzione, a partire da un tipo ciclo, da un assieme,
e da ulteriori condizionamenti (data, configurazione).

## VALORI POSSIBILI

### 1 TECNICA
Viene eseguita la scansione di tutte le fasi legate all'assieme.
Non vengono tratatti i filtri di data e la configurazione.

### 3 DI PRODUZIONE
E'come la scansione tecnica con le seguenti differenze : 
-    se l'assieme ha un gruppo ciclo viene scandito quest'ultimo (in questo caso l'assieme deve essere un articolo)
-    vengono esclusi i legami non validi per data (a meno che sia esplicitamente chiesto di ritornare tutte le fasi)
-    viene applicata la configurazione (sia come esclusione di fasi, sia come variazione del loro contenuto)
