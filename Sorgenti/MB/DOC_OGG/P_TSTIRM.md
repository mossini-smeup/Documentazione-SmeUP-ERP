# Obiettivi
* Interfacciare il programma in esecuzione con l'ANAGRAFICO RIGHE RICHIESTE DI MOVIMENTAZIONE delle diverse applicazioni previste nella tabella di personalizzazione applicazioni B£1.
* Eseguire la ricerca alfabetica relativa se richiesto

# Input
* £IRMFU :  Funzione
* £IRMME :  Metodo
* £IRMAM :  Ambiente
* £IRMCO :  Contesto
* £IRMPA :  Tipo Riga richiesta movimentazione
* £IRMCD :  Codice Riga richiesta movimentazione
* £IRMRI :  N.ro Record di input

# Output
* £IRMCD :  Codice Rich.Mov. scelta (se eseguita ricerca)
* £IRMDE :  Descrizione richiesta d'acquisto
* £IRMMS :  Codice messaggio ritorno (7)
* £IRMFI :  File   messaggio ritorno (10)
* £IRMCM :  Ultimo Comando :  *IN35  :  se On = Codice errato, ** *IN36  :  se On = eseguita ricerca alfabetica
* £IRMRO :  N.ro Record di output

# Prerequisiti
>DGMRRIM         E DS                  EXTNAME(GMRRIM0F)

# Esempio di chiamata
>C*                  EVAL      £IRMFU='Funzione'
C*                  EVAL      £IRMME='Metodo'
C*                  EVAL      £IRMAM= Ambiente
C*                  EVAL      £IRMCO= Contesto
C*                  EVAL      £IRMPA= Tp_Rich
C*                  EVAL      £IRMCD= Rich_Mv
C*                  EXSR      £IRM
C* N36              EVAL      Righe_Rich_Movim = £IRMCD
C* N35              EVAL      Campo_descrizione= £IRMDE

