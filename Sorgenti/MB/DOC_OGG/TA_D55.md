# D55 - Ripresa
 :  : DEC T(ST) K(D55)
## OBIETTIVO
Contenere le informazioni utili alla definizione di un insieme di records di D5COSO e degli algoritmi per la trasformazione della chiave.

## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM Codice
Il codice dell'elemento della tabella D55, viene utilizzato come prefisso (+ '.') nella ricerca di elementi di tabella D56. Tali elementi specificano i 4 codici che servono da eventuale filtro sul D5COSO (CODI, COD1, COD2, COD3).
 :  : FLD T$D55A **Contesto**
Contesto dei records di origine del D5COSO
 :  : FLD T$D55B **Tema**
Tema dei records di origine del D5COSO
 :  : FLD T$D55C **Periodo**
Eventuale specificazione del periodo di origine
 :  : FLD T$D55D **Sottosettore D5R**
Algoritmo di aggancio del gruppo di record di destino, a partire dal record origine (sottosettore D5R ed eventualmente elemento. Se elemento non presente, esegue risalita).
 :  : FLD T$D55F **Periodo Destino**
Eventuale forzatura del periodo di destino
 :  : FLD T$D55J **Filtro D5Z**
Eventuale filtro tramite D5Z
