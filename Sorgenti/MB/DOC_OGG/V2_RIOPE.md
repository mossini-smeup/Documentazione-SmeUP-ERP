# RIOPE     -  RILEVANZA OPERAZIONE
Definisce la rilevanza della riga di operazione di ciclo per quanto riguarda la costruzione degli impegni risorse e
della successiva schedulazione.
Questo campo, a meno che non si sia definito di non portare la riga negli impegni risorse, viene riportato in essi col
valore della riga del ciclo di partenza.

## VALORI POSSIBILI

### ' ' NORMALE
La riga di ciclo ha un comportamento normale :  essa genera un impegno risorse che è successivamente schedulato.

### '1' NON PORTATA IN P5IRIS (IMPEGNI RISORSE)
La riga di ciclo non genera una riga di impegni risorse :  quindi su di essa non viene dichiarato l'avanzamento. Nella
scansione del ciclo del documento essa appare comunque :  se la si volesse escludere anche da esso basterebbe dichararla
non attiva, agendo sul suo stato.

### '2' NON SCHEDULATA
La riga di ciclo genera una riga di impegni risorse, per cui su di essa si dichiara l'avanzamento, ma non è trattata
dalla schedulazione.
