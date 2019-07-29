# M5LMX     -  TRATTAMENTO LOTTO MASSIMO IN PIANIFICAZIONE
Definisce le varie modalità con cui viene trattato in pianificazione il lotto massimo dell'articolo, impostato nei
parametri di pianificazione.
NB :  se il consiglio pianificato è stato assegnato ad un ente, non viene eseguito il trattamento del lotto massimo.

## VALORI POSSIBILI

### ' ' NESSUNO
Il lotto massimo è puramente indicativo

### '1' SOLO SEGNALAZIONE
Se un ordine pianificato supera il lotto massimo viene impostato un flag di segnalazione sul record del suggerimento.

### '2' SUDDIVISIONE ORDINI IN PARALLELO
Se un ordine pianificato supera il lotto massimo viene spezzato in 'n' ordini pianificati, che hanno tutti come fine
la stessa data, con quantità pari al lotto massimo, tranne, eventualmente, l'ultimo con il resto della divisione.
La quantità viene calcolata dopo l'applicazione del lotto minimo e multiplo :  è quindi cura di chi inserisce questi
valori garantire la loro congruenza.
Non è necessario che il lotto massimo sia superiore al lotto minimo :  il secondo è una caratteristica di pianificazione
(faccio non meno di n pezzi), il primo è una caratteristica produttiva (faccio insieme n pezzi :  potrebbe essere una
quantità per unità di movimentazione).
          Esempio : 
          Quantità pianificata 4 - Lotto minimo 5 - Lotto multiplo 1 - Lotto massimo 2
          In questo caso la quantità pianificata, con la lottizzazione, è 5 : 
          Vengono emessi i seguenti ordini : 
          -    O1 :   2
          -    O2 :   2
          -    O3 :   1

### '3' SUDDIVISIONE ORDINI IN SERIE (SV)
