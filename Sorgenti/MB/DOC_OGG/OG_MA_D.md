## Codice Oggetto (in TA/*CNTT)
'MA'                                          £FUNT1
## Chiave primaria
Codice macchina                               £FUNK1

La macchina è una specializzazione dell'oggetto Risorsa (RI) con il tipo fissato (MAC).
 :  : DEC T(OG) K(RI)
 :  : DEC T(TA) P(BRR) K(MAC)

Questo oggetto NON è utilizzato, nelle tipizzazioni statiche, all'interno di Sme.Up.
Se ne sconsiglia quindi l'utilizzo nelle proprie tipizzazioni dinamiche (griglie, parametri, ecc..)

NON va comunque utilizzata l'interfaccia obsoleta £IFMAC, ma l'interfaccia generale delle risorse.
 :  : DEC T(MB) P(QILEGEN) K(£IRI)

Per impostare un tipo risorsa come macchina, si deve inserire il tipo risorsa secondaria nella tabella dello scenario base ('**') degli impegni risorse.
 :  : DEC T(TA) P(S5B) K(**)
Per attivare la gestione delle risorse specifiche, va inserito un valore diverso dal tipo risorsa principale.



