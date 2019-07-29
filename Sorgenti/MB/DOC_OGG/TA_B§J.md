# B§J - Azioni per radiofrequenza
 :  : DEC T(ST) K(B§J)
## OBIETTIVO
Permettere la definizione di una struttura di menù a più livelli che utilizzano una parte ridotta del video per l'interazione.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM **Codice**
Il codice contiene il livello del menù. Avremo pertanto : 
- 1         Richiamo di un menu di livello 1
- 11        Azione specifica
- 12        Richiamo di un menù di secondo livello
- 121       Azione specifica
- 122       Azione specifica
- 13        Azione specifica
Ecc.
 :  : FLD T$B§JA **Comando**
La costante "GO" indica l'esistenza di un menù di livello successivo. In tutti gli altri casi si deve immettere il comando da richiamare.
