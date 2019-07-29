# Preparazione
 - Impostare correttamente la tabella EUR per fissare data e divise
 :  : DEC T(TA) P(EUR) K(*)

 - I programmi di conversione possono funzionare in modalità di simulazione producendo la sola stampa di controllo. Impostare pertanto le tabelle di controllo programmi nel modo desiderato
 :  : DEC T(TA) P(PGM) K(C5UT0501)
 :  : DEC T(TA) P(PGM) K(C5UT0502)
 :  : DEC T(TA) P(PGM) K(C5UT0503)

 - Eseguire il salvataggio della situazione di partenza : 
 -- della libreria di contabilità completa
 -- in ogni caso almeno degli archivi sottoelencati, tenendo conto che i programmi non gestiscono la ripartenza
 :  : DEC T(OJ) P(*FILE) K(C5TREG0F)
 :  : DEC T(OJ) P(*FILE) K(C5RREG0F)
 :  : DEC T(OJ) P(*FILE) K(C5RATE0F)

# Azioni di analisi correttezza dati
 :  : INI Controllo quadratura importi tra righe e rate
 :  : CMD CALL C5UT0602
 :  : FIN
 :  : INI Controllare la stampa prodotta
 :  : CMD WRKSPLF
 :  : FIN

 :  : INI Controllo quadratura interna rate
 :  : CMD CALL C5UT0601
 :  : FIN
 :  : INI Controllare la stampa prodotta
 :  : CMD WRKSPLF
 :  : FIN

# Azioni di conversione
 :  : INI Creazione registrazione di chiusura/apertura
 :  : CMD CALL C5UT0503
 :  : FIN

Controllare quadratura conti di chiusura/apertura e verificare la correttezza della registrazione di quadratura eseguita automaticamente.
Stampare il giornale definitivo e ultimo in lire.

 :  : INI Conversione valori delle registrazioni
 :  : CMD CALL C5UT0501
 :  : FIN
 :  : INI Controllare la stampa per registraz.squadrate oltre la soglia
 :  : CMD WRKSPLF
 :  : FIN

 :  : INI Conversione valori delle partite
 :  : CMD CALL C5UT0502
 :  : FIN
 :  : INI Controllare la stampa per rate chiuse squadrate oltre la soglia
 :  : CMD WRKSPLF
 :  : FIN

# Azioni post-conversione
Verificare la prima nota e/o il giornale in EURO.
