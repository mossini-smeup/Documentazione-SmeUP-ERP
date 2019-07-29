## CAUSALI

I sottoriportati elementi di tabella vanno riportati/allineati come da modello : 

 :  : DEC T(TA) P(A5G) K(RVS) I(_7_Causali Collegate Movimento Reversal  >>)
 :  : DEC T(TA) P(A5B) K(RS0) I(_7_Causale Standard di Reversal  >>)
 :  : DEC T(TA) P(A5B) K(VN1) I(_7_Causale Standard Fondo Venduto Ordinatio >>)
 :  : DEC T(TA) P(A5B) K(VN2) I(_7_Causale Standard Fondo Venduto Anticipato >>)
 :  : DEC T(TA) P(A5B) K(LN1) I(_7_Causale Standard Fondo Venduto Ordinatio >>)
 :  : DEC T(TA) P(A5B) K(LN2) I(_7_Causale Standard Fondo Venduto Anticipato >>)
 :  : DEC T(TA) P(A5G) K(VEN) I(_7_Causali Collegate Movimento Vendita >>)
 :  : DEC T(TA) P(A5G) K(ALI) I(_7_Causali Collegate Movimento Alineazione >>)

Per gli ultimi due elementi è necessario controllare che tutte le causali di vendita /alienazione presentino tali elementi nel campo "Causali Collegate", o che in alternativa ne presentino degli equivalenti compilati nello stesso modo.

E' inoltre necessario verificare l'allineamento dei totalizzatori delle causali di ammortamento : 

 :  : DEC T(TA) P(A5B) K([TA.A5B.A.A59999]) I(_7_Causali di Ammortamento >>)

## LINEA

Per attivare la gestione del reversal sulla linea fiscale andrà compilato il campo "Causale Reversal" (l'elemento standard è la causale RS0).

 :  : DEC T(ST) P() K(A5C&AZ)

## CONVERSIONI

Una cosa fondamentale per il corretto funzionamento del reversal, arrivando da una conversione, è che alla data dell'ultimo periodo chiuso, siano corretti non solo il totalizzatore "Fondo ammortamento totale" che normalmente è l'unico requisito necessario, ma anche "Fondo ammortamento ordinario" e "Fondo ammortamento anticipato', sui cui valori si basano poi i calcoli del reversal.

In questo senso il principale problema sono i decrementi di valore (fondo venduto/alienato), in quanto il solo fatto di allineare i totalizzatori degli ammortamenti fa si che gli
incrementi vengano alimentati in modo corretto.

