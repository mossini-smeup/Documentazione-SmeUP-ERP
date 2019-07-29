# Struttura quantità in M5CONS
La scansione disponibilità ritorna Qe (Qtà entrata) o QU (Qtà uscita), normalmente positive e con separato il segno (vale E / U). Nel caso di entrate negative (es. giacenze negative) o uscite negative (es. recuperi) si cambia il segno alla qtà e si inverte il campo segno E/U.
La qtà e il segno sono riportati nei campi "Qtà fonte" e "Segno fonte" di M5CONS.
La scansione disponibilità ritorna anche la qtà (positiva / negativa), se è negativa e la data fonte è zero, si porta la data a oggi ad eccezione del caso di fonte tipo "Scorta" con impostato in M51 la "Scorta dopo tempo di approvvigionamento" in cui si porta la data a oggi + lead time.

La data pianificazione è un record di M5CONS con MAG = "**", art. = "**" e nella data fonte la data di pianificazione.

Nel gruppo fonti per MRP __NON__ mettere gli ordini pianificati :  all'atto dela scansione disponibilità non ci sono ancora e quindi è inutile farli cercare. Mettere invece gli impegni pianificati, che sono stati caricati in precedenza
