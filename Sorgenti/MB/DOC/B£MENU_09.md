# Gli oggetti MP ed ME

Per le prime due classificazioni di menù è importante notare che i menù e le voci che lo compongono all'interno di SmeUP, vengono identificate attraverso gli oggetti : 
* MP :  parametro voce di menù (cioè dell'oggetto ME). Questo oggetto identifica il menù ed a partire dai primi caratteri del codice è possibile identificarne la tipologia : 
** "*"+sottosettoretabella MEA indica un menù di accesso
** "M_"+codicemodulo indica il menù di un modulo SmeUP (istanza tabella B£AMO)
** "O_"+codiceclasse indica il menù di un oggetto SmeUP (istanza della classe OG)
* ME :  voce di menù. Identifica la singola voce di menù. In merito ad essa è molto importante notare che questo oggetto può assumere una consistenza "dinamica", in quanto certe voci possono esistere o meno a seconda dell'istanza utilizzata nel menù (si fa questo esempio :  all'interno del menù certe voci possono essere presenti o meno a seconda di certe caratteristiche dell'istanza di oggetto, per tale motivo non è possibile identificarle senza specificare l'istanza). Per supplire a questo inconveniente, ovunque si analizzano tali voci si tende a dare la possibilità di indicare anche l'istanza di riferimento oltre che il parametro di riferimento del menù).

A questi oggetti fanno riferimento le copy di interfaccia £IMP e £IME.

 :  : DEC T(OG) K(MP)
 :  : DEC T(MB) P(QILEGEN) K(£IMP) L(1)
 :  : DEC T(OG) K(ME)
 :  : DEC T(MB) P(QILEGEN) K(£IME) L(1)
