# D9AP_01C - Estrattore da MPPIAN
Estrae dall'archivio MPPÌAN0F, relativo ai piani di produzione (PLAN_UP)
_2_Parametri origine : 

- Tabella MPP dei piani :  determina il contesto di estrazione e la chiave del logico di cui farà la scansione. Caratterizza anche i valori.
- Tabella MPC delle viste di un piano :  determina gli oggetti origine per l'estrazione e serve come chave per la scansione
- Si possono impostare fino a due piani con tre viste ciascuno. Deve esserci congruenza negli oggetti interrogati.
- Tipo di incrocio piani :  metodo " " utilizza la vista nr 1 di ogni piano come motore di scansione, estraendo così i record contenuti solo in questa vista, e dove presenti i valori delle altre viste.

Ad esempio se A ha un valore nella vista 2 ma non è presente nella vista 1, con questo metodo non compare nell'estrazione. Metodo "A", estrae tutti i record di ogni piano e vista, indistintamente.

_2_Oggetti origine
Sono determinati dal parametro origine della vista del piano. Sono gli oggetti, o uno o due, contenuti nell'elemenuto di tabella dichiarato. È opportuno che siano compatibili tra di loro. È inoltre presente la gerarchia sul periodo contestuale del piano estratto.

_2_Valori origine
Sono determinati dal parametro del piano, ogni vista fornisce un valore.
