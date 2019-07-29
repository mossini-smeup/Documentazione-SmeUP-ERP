## Codice Oggetto (in TA/*CNTT)
'FO'                                          £FUNT1

## Chiave primaria
Codice Fornitore                              £FUNK1

Il fornitore è una specializzazione dell'oggetto Ente (CN) con il tipo fissato (FOR).
 :  : DEC T(OG) K(CN)
 :  : DEC T(TA) P(BRE) K(FOR)

Questo oggetto NON è utilizzato, nelle tipizzazioni statiche, all'interno di Sme.Up.
Se ne sconsiglia quindi l'utilizzo nelle proprie tipizzazioni dinamiche (griglie, parametri, ecc..)

Per caratterizzare un tipo contatto come fornitore, va invece impostata la natura ente nel campo "tipo contatto"
 :  : DEC T(CS) P(T_BRE) K(T$BREM)

NON va comunque utilizzata l'interfaccia obsoleta £IFFOR, ma l'interfaccia generale degli enti.
 :  : DEC T(MB) P(QILEGEN) K(£IFCON)

