# NAVIGAZIONE

## Aggiunta di funzioni/metodi navigazione per oggetto
Aggiungere funzioni proprie nella navigazione per oggetto è possibile tramite l'implementazione del pgm di exit**C5NO00_X**.

Tale pgm svolge quattro funzioni : 
 * FUN :  il pgm viene chiamato per integrare la schiera delle funzioni/metodi per oggetto gestita dal pgm C5NO00N.
 * IMP_SIG :  il pgm viene chiamato per integrare la schiera dei significati delle impostazioni (chiamata dal C5NO00_IM)
 * IMP_RIT :  il pgm viene chiamato per ritornare la schiera di gestione (£30A) di un codice impostazione specifico non gestito a standard
 * IMP_PAR :  il pgm viene chiamato per ritornare la schiera di gestione (£30A) di un codice di parametri specifico non gestito a standard

Per ulteriori approfondimenti al suo utilizzo si rimanda all'analisi del sorgente del pgm di esempio.

 :  : INI . Sorgente pgm di esempio
 :  : CMD CALL B£VED0 PARM('C5NO00_X' '' '' '' '0')
 :  : FIN

## Aggiunta opzioni funizzate nelle interrogazioni
Per aggiungere funzioni alle opzioni disponibili nelle interrogazioni delle navigazioni è possibile implementare il pgm di exit**C5N000_X**richiamato dal pgm C5N000P che si occupa della costruzione delle azioni funizzate da utilizzare in ogni pgm di navigazione.
Per il suo funzionamento si rimanda all'analisi del sorgente del pgm di esempio.

 :  : INI . Sorgente pgm di esempio
 :  : CMD CALL B£VED0 PARM('C5N000_X' '' '' '' '0')
 :  : FIN
