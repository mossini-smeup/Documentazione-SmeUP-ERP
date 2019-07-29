## Verifiche di presenza
###  Principali archivi di dati
  :  : DEC T(OJ) P(*FILE) K(ANPRO00F) I(Articoli  >>)
  :  : DEC T(OJ) P(*FILE) K(ANACF00F) I(Clienti   >>)
  :  : DEC T(OJ) P(*FILE) K(ANACF00F) I(Fornitori >>)
  :  : DEC T(OJ) P(*FILE) K(ANCON00F) I(Conti     >>)
  :  : DEC T(OJ) P(*FILE) K(DISTI00F) I(Distinte  >>)
###  Principali programmi
  :  : DEC T(OJ) P(*PGM) K(B£IAG6) I(*NONE)
  :  : DEC T(OJ) P(*PGM) K(B£IFCO_G6) I(*NONE)

## Oggetti gestiti
  :  : DEC T(TA) P(B£I) K(C5B) I(_7_Conti **(F G6 Programma C5PDC_A7))
 Articoli
 Clienti/Fornitori

## Esecuzione dei TEST
 :  : INI Impostazioni deviatori
 :  : CMD CALL B£IFVE
 :  : FIN
 :  : INI Ricerca Articoli
 :  : CMD CALL B£AR20 PARM('AR' ' ' '?')
 :  : FIN
 :  : INI Ricerca Clienti
 :  : CMD CALL B£AR20 PARM('CN' 'CLI' '?')
 :  : FIN
 :  : INI Ricerca Conti
 :  : CMD CALL B£AR20 PARM('CO' '' '?')
 :  : FIN
 :  : INI Ricerca Cespiti
 :  : CMD CALL B£AR20 PARM('CE' '' '?')
 :  : FIN

## Compilazione programmi in libreria SMEUP_EXT
 :  : INI Compilazione di tutti i programmi (BASE)
 :  : CMD CALL B£UT11 PARM('B£*' 'SRC_G6' 'SMESRC')
 :  : FIN
 :  : INI Compilazione di tutti i programmi (IN SVILUPPO)
 :  : CMD CALL B£UT11 PARM('*ALL' 'SRC_G6' 'SMEDEV')
 :  : FIN
