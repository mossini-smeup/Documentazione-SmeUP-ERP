# VARIABILI AMBIENTE

##  Utilizzo valori della schiera £BCDVA

01) Imposta la fine nel 30 (???)

02) Errori (_ER)  (???) Superato ??

03)

04)

05) Solo un ordine  (01I) Articolo (30) solo in 5250

06) Nell'11E imposta la fine della schedulazione

07)

08)

09)

10) Ritorna azione al motore BCD dal D3

11) Imposta nel D4 se si rischedula dove si era

12)

13)

14)

15) Se impostato vuol dire che è in consultazione

16)

17)

18)

19)

20) Componente grafico con cui verranno visualizzati i dati (tipicamente EXB o GNT). In S5SMES_D4,
    se si cambia questo valore per passarlo ad un pgm richiamato, è necessario salvarlo prima del
    richiamo del pgm e successivamente ripristinarlo, per poter poi rischedulare correttamente.
    E' quindi necessario fare : 
    £BCDVA(20) --> TMP20
    £UIBPG (nuovo componente richiesto) --> £BCDVA(20)
    CALL
    TMP20 --> £BCDVA(20)

