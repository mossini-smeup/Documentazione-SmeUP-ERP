## Codice Oggetto (in TA/*CNTT)
'MG'                                          £FUNT1
## Chiave primaria
Codice magazzino                              £FUNK1

Il magazzino è contenuto nel settore di tabella MAG.
Può quindi essere oggettizzato come : 

## Codice Oggetto (in TA/*CNTT)
'TA'                               £FUNT1
## Chiave primaria
'MAG'    Settore di tabella        £FUNP1
XXCDMG   Codice magazzino          £FUNK1

Questa seconda oggettizzazione è preferibile in quanto non è presente un'interfaccia specifica del magazzino (£IMG) che ritorni i campi del tracciato record :  tale funzione è svolta dall'interfaccia generale degli elementi di tabella £RITES.

 :  : DEC T(ST) K(MAG)

