# MOSCA     -  MODALITÀ SCARICO MATERIALI
Definisce le varie modalità con cui possono essere scaricati in modo automatico i componenti di un ordine o di una riga di ciclo esterno.
                                      !!! ATTENZIONE !!!
Se è stata valorizzata, nel legame di distinta base, una quantità per lotto, viene forzato lo scarico manuale.

## VALORI POSSIBILI

### ' ' SCARICO MANUALE
Viene generato l'impegno di produzione, mentre lo scarico viene eseguito manualmente, tramite la funzione dei prelievi pianificati a fronte d'ordine/documento.

### 'A' NESSUN SCARICO/IMPEGNO
Non viene generato l'impegno di produzione, nè viene eseguito lo scarico automatico all'atto del versamento dell'assieme. I componenti con questo valore verosimilmente vengono riapprovviginati a punto di riordino, (minuteria, barattoli di grasso, ecc...), e la presenza in distinta base serve solo per imputarne il costo all'articolo.
NB :  il fatto che non siano generati gli impegni non vuol dire che essi non appaiano nella distinta del documento. In questo modo, qualora si voglia produrre la documentazione di reparto per illustrare le modalità di produzione dell'assieme, essi possono essere riportati.

### 'B' SCARICO AUTOMATICO PERCENTUALE
Viene generato l'impegno di produzione, e viene eseguito lo scarico automatico all'atto del versamento dell'assieme, per la quantità dell'assieme moltiplicata per il coefficiente di impiego del componente.

### 'C' SCARICO AUTOMATICO SU RESIDUO SV
E' come il caso precdente, con la differenza che, si confronta la quantità da scaricare del componente con la quantità di impegno residua, e si scarica quest'ultima se è minore della precedente.In questa modalità si tiene conto di eventual prelievi eseguiti manualmente a fronte dell'ordine.

### 'D' SCARICO AUTOMATICO ALLA FASE
Viene generato l'impegno di produzione, e all'atto della dichiarazione di avanzamento di una fase, vengono scaricati tutti i materiali che appartengono a questa fase, per la quantità che si avanza (buona + scarti) moltiplicata per il coefficiente di impiego del componente.

### 'E' SCARICO MANUALE FORZATO
Lo scarico avviene comunque in modo manuale, anche se è stata specificata la modalità di scarico IM (scarico automatico di tutti i componenti) nella tabella del tipo impegno (P5I).
