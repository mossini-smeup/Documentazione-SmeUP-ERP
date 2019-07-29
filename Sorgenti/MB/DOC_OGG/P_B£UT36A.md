# SOSTITUZIONE CARATTERI NON VALIDI
Lo scopo di questa utility è la sistemazione del contenuto del campo di un file, qualora contenga caratteri non validi, che possono ad esempio causare errori xml in Loocup.

## File  :  file su cui eseguire la sostituzione

## Campo  :  campo del file su cui eseguire la sostituzione

## Car. da sostituire  : 
**1 - Caratteri non validi**
     Quando viene inserito un carattere non compreso nel code page del job viene sostituito      dal sistema operativo con l'esadecimale x'3F' che indica carattere non valido.
     La sostituzione dei caratteri non validi non comporta rischi.
**2 - Car.non validi e di controllo**
     I caratteri di controllo sono quei caratteri con valore esadecimale inferiore a x'3F' tra      cui ad esempio l'a capo (x'0D' e x'25') e il tab (x'05').
### ATTENZIONE!  Questa opzione va utilizzata con estrema cautela. I caratteri di controllo    potrebbero essere caratteri validi (ad esempio in un campo note).
   In alcuni casi potrebbero però essere il risultato di un errore in un programma di conversione,    ad esempio causati da un operazione di MOVE/MOVEL di un campo varying invece che un EVAL.

## Car. sostituente  : 
**1 -  ' '**
Sostituisce i caratteri non validi con uno spazio
**2 -  '?'**
Sostituisce i caratteri non validi con uno punto di domanda
**3 -  '_'**
Sostituisce i caratteri non validi con un underscore

## Esecuzione  : 
**1 - Solo stampa**
Produce una stampa che indica riga per riga la presenza di caratteri non validi nel campo.
**2 - Esecuzione + Stampa**
Esegue l'aggiornamento del campo sostituendo i caratteri non validi con il carattere scelto.
Produce una stampa che indica riga per riga la presenza di caratteri non validi nel campo.
**3 - Stampa riepilogo caratteri**
Produce una stampa che riepiloga quali sono i caratteri non validi presenti nel campo.
