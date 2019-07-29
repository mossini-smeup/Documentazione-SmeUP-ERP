## Codice Oggetto (in TA/*CNTT)
'CL'                                          £FUNT1

## Chiave primaria
Codice Cliente                                £FUNK1

Il cliente è una specializzazione dell'oggetto Ente (CN) con il tipo fissato (CLI).
 :  : DEC T(OG) K(CN)
 :  : DEC T(TA) P(BRE) K(CLI)

Questo oggetto NON è utilizzato, nelle tipizzazioni statiche, all'interno di Sme.Up.
Se ne sconsiglia quindi l'utilizzo nelle proprie tipizzazioni dinamiche (griglie, parametri, ecc..)

Per caratterizzare un tipo contatto come cliente, va invece impostata la natura ente nel campo "tipo contatto"
 :  : DEC T(CS) P(T-BRE) K(T$BREM)

NON va comunque utilizzata l'interfaccia obsoleta £IFCLI, ma l'interfaccia generale degli enti.
 :  : DEC T(MB) P(QILEGEN) K(£IFCON)

