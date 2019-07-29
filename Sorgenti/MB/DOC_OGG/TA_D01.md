# D01  -  PARAMETRI COSTI AVANZATI
 :  : DEC T(ST) K(D01)
## OBIETTIVO
Contiene le impostazioni generali dell'applicazione costi avanzati
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM **Elemento**
È l'elemento fisso *
 :  : FLD T$D01A **Tipo costo assunto**
È il tipo costo usato in assenza di un codice inserito esplicitamente; ad esempio nella determinazione dei numeri di un oggetto (routine £G37)
 :  : FLD T$D01B **Livello costo assunto**
È il livello costo usato in assenza di un codice inserito esplicitamente; ad esempio nella determinazione dei numeri di un oggetto (routine £G37). Si consiglia vivamente di inserire il livello che rappresenta il costo totale dell'articolo, in quanto questo è il livello utilizzato per leggere i costi nelle routine di calcolo costi.
Si ricorda che per ottenere un costo bisogna sempre esplicitare sia il tipo costo sia il livello.
 :  : FLD T$D01C **1° Liv. Dist. in LIV**
Inserendo il valore 1 nel campo, il programma di calcolo dei costi porta il costo dei materiali del primo livello nel "COSTO MATERIALE AL LIVELLO", lasciandolo 'bianco'. Tutto il costo del materiale viene messo nel "COSTO MATERIALE AL LIVELLO INFERIORE".
 :  : FLD T$D01D **Calcolo effic. std**
Inserendo il valore 1 nel campo, il programma di calcolo dei costi utilizza l'efficienza standard delle risorse per rettificare i tempi del ciclo. Si ricorda che l'efficienza è inserita su base 1 (quindi 0,9 è inefficienza e 1,1 è efficienza) e che nel calcolo viene rettificato il costo di TUTTI i tempi gestiti (quindi anche dell'attrezzaggio)
