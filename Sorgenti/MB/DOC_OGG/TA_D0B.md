# D0B  -  LIVELLI DI COSTO
 :  : DEC T(ST) K(D0B)
## OBIETTIVO
Contiene i livelli di costo di un oggetto e permette di indicare in vari modi quali componenti di costo rappresentano il livello di costo voluto. Questo perchè nelmodulo D0 la scheda delle componenti di costo può essere costruita direttamente dall'utente e occorre indicare al sistema quali sono le componenti significative per lui.
_7_N.B. :  Nel modulo D0 per reperire un costo di un oggetto bisogna specificare sia un tipo costo sia un livello di costo.
Nel caso in cui non siano esplicitati, il sistema li reperirà dalla tabella D01 di impostazione generale.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM **Elemento**
La codifica dei livelli di costo è libera.
 :  : FLD T$D0BA **Natura costo**
Se presente indica che il costo del livello è rappresentato da questa natura costo.
 :  : FLD T$D0BB **Riclassifica**
Viene utilizzato nel caso in cui venga specificato anche il campo 'Natura costo'.
Può assumere i seguenti valori
- ' ' :  leggi il valore della natura dello schema costo dettagliato.
- 'A' :  leggi il valore della natura della riclassifica A dello schema costo (vedi tabella IGI per il significato della riclassifica).
- 'B' :  leggi il valore della natura della riclassifica B dello schema costo.
 :  : FLD T$D0BC **Elemento IGI**
Se presente indica che il costo del livello è rappresentato da questo particolare indice della tabella IGI
 :  : FLD T$D0BD **Livello/Livello inf.**
Campo significativo solo se viene utilizzata la versione SM dei costi (/COPY £G17).
Se impostato, questo campo viene scritto nel campo £G17TL della /COPY e il livello non viene passato.
Può assumere i seguenti valori : 
- 'L' :  Costi del livello.
- 'I' :  Costi del livello inferiore.
