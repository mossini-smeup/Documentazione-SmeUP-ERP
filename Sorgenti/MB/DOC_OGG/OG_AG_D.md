## Codice Oggetto (in TA/*CNTT)
'AG'                                          £FUNT1
## Chiave primaria
Codice Agtente                                £FUNK1

L'agente è contenuto nel settore di tabella AGE.
Può quindi essere oggettizzato come : 

## Codice Oggetto (in TA/*CNTT)
'TA'                               £FUNT1
## Chiave primaria
'AGE'    Settore di tabella        £FUNP1
XXCDAG   Codice agente             £FUNK1

 :  : DEC T(ST) K(AGE)

Questa seconda oggettizzazione è preferibile in quanto non è presente un'interfaccia specifica dell'agente o (£IAG) che ritorni i campi del tracciato record :  tale funzione è svolta dall'interfaccia generale degli elementi di tabella £RITES.

 :  : DEC T(MB) P(QILEGEN) K(£RITES)

