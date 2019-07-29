_4_Verifiche di presenza
 Se assenti impostare librerie con documento "Verifiche ambiente DEMO"
 Le impostazioni vengono acquisite al prossimo ingresso
> Principali archivi di dati
  :  : DEC T(OJ) P(*FILE) K(ANPA200F) I(Articoli          >>)
  :  : DEC T(OJ) P(*FILE) K(ANCL200F) I(Clienti           >>)
  :  : DEC T(OJ) P(*FILE) K(ANFO200F) I(Fornitori         >>)
  :  : DEC T(OJ) P(*FILE) K(ANCO200F) I(Conti / Vedi nota >>)
  :  : DEC T(OJ) P(*FILE) K(KPJBA) I(*NONE)
> Principali programmi
  :  : DEC T(OJ) P(*PGM) K(B£IAA7)   I(*NONE)
  :  : DEC T(OJ) P(*PGM) K(B£ICA7)   I(*NONE)
  :  : DEC T(OJ) P(*PGM) K(B£ICE_A7) I(*NONE)
  :  : DEC T(OJ) P(*PGM) K(B£IE4_A7) I(*NONE)
  :  : DEC T(OJ) P(*PGM) K(B£IE5_A7) I(*NONE)

_4_Oggetti gestiti
  :  : DEC T(TA) P(B£I) K(C5B) I(_7_Conti **(F A7 Programma C5PDC_A7))
  _7_Articoli
  _7_Clienti/Fornitori

_4_Esecuzione dei TEST
 :  : INI _7_Impostazioni deviatori
 :  : CMD CALL B£IFVE
 :  : FIN
 :  : INI **Ricerca Articoli
 :  : CMD CALL B£AR20 PARM('AR' ' ' '?')
 :  : FIN
 :  : INI **Ricerca Clienti
 :  : CMD CALL B£AR20 PARM('CN' 'CLI' '?')
 :  : FIN
 :  : INI **Ricerca Conti
 :  : CMD CALL B£AR20 PARM('CO' '' '?')
 :  : FIN
 :  : INI **Ricerca Cespiti
 :  : CMD CALL B£AR20 PARM('CE' '' '?')
 :  : FIN

_4_Compilazione programmi in libreria SMEUP_EXT
 :  : INI _7_Compilazione di tutti i programmi (BASE)
 :  : CMD CALL B£UT11 PARM('B£*' 'SRC_A7' 'SMESRC')
 :  : FIN

 :  : INI _7_Compilazione di tutti i programmi (IN SVILUPPO)
 :  : CMD CALL B£UT11 PARM('*ALL' 'SRC_A7' 'SMEDEV')
 :  : FIN
