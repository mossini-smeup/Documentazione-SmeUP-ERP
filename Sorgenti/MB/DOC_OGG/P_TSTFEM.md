# OBIETTIVO
   Presentare un S/File a due livelli

# PREREQUISITI
   /COPY QILEGEN,£FEM

# PARAMETRI
## PARAMETRI DI INPUT
     - Funzione : _campo £FEMFU_
                              SEL) Selezione
                              CON) Controllo funzione/metodo immessi

     - Metodo (solo per funzione SEL) : _campo £FEMME_
    ' ') Standard
    C) Completa
    R) Ridotta
    E) Estesa
    A) Automatica

    - Funzione gestita (solo per funzione SEL) : _campi £FEM$F/£F_

    - Metodo gestito (solo per funzione SEL) : _campi £FEM$M/£F _

    - Ambiente : _campo £FEMAM_

    - Titolo primo livello : _campo £FEMT1 _
                                     Assume 'Funzioni'

    - Titolo secondo livello : _campo £FEMT2_
                                    Assume 'Metodi'

    - Titolo 1° e 2° livello combinati : _campo £FEMT3 _
                                    Assume 'Funzioni e Metodi'

    - Schiera funzioni e metodi

Le schiere delle funzioni e metodi da utilizzare vanno inserire nei 5 campi in fondo.
La modalità di riempimento di questi campi deve rispettare il seguente schema : 
Nei 10 caratteri sotto la scritta F/M vanno inseriti i nomi delle funzioni e dei metodi ricordando che i metodi devono
essere contraddistinti da un punto prima del nome del metodo. Ad esempio
LET(Funzione) .STD(Metodo). La desrizione della funzione e del metodo deve essere posta al di sotto della
corrispondente scritta in intestazione.
E' possibile dare come metodo un parametro. In questo caso va inserito sotto la scritta TA il tipo Parametro da
utilizzare e ovviamente sotto parametro il tipo di parametro se necessario.
Si ricorda inoltre che se per una funzione si inseriscono piu metodi di tipo parametrico la scelta possibile sarà
ristretta ai primi 200 elementi trovati.

# ESEMPIO DI RICHIAMO

           MOVEL<Funz.FEN>£FEMFU
           MOVEL<Meto.FEM>£FEMME
           MOVEL<Funz.Sel>£FEM$F
           MOVEL<Met.Sel.>£FEM$M
           Z-ADD<Indic.1 >£FEM1
           Z-ADD<Indic.2 >£FEM2
           MOVEL<Ambiente>£FEMAM
           MOVEL<Tit Liv1>£FEMT1
           MOVEL<Tit Liv2>£FEMT2
           MOVEL<Tit Liv3>£FEMT3
           MOVEL<Ricostr.>£FEMRI
           MOVEL<Ges.Aut.>£FEMAU
           EXSR    £FEM
           MOVEL £FEM$F    <Funz.>
           MOVEL £FEM$M    <Metodo>
           MOVEL £FEM£F    <Descr.Funz.>
           MOVEL £FEM£M    <Descr.Metodo>
        36                SETON                     10
        35                SETON                     60

