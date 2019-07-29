# CQO - Tipo di controllo
 :  : DEC T(ST) K(CQO)
## OBIETTIVO
Gestire l'indirizzamento della fase del ciclo di collaudo sui vari tabulati di stampa.
## CONTENUTO DEI CAMPI
 :  : FLD T$AUTO **Autocontrollo Operatore**
Stampa della fase sul tabulato di Autocontrollo dell'operatore e rende obbligatorio l'inserimento del campo "Gruppo controllo" e del campo "Periodo". Il campo può assumere i seguenti valori : 
-' '  Non stampa
-'X'  Stampa la fase sul ciclo collaudo assegnato all'operatore (fasi di autocontrollo in produzione)
 :  : FLD T$GRIL **Griglia Controllo**
Stampa della fase sul tabulato Griglia di controllo per l'esecuzione del collaudo del lotto. Il campo può assumere i seguenti valori : 
-' '  Non stampa
- 'X '  Stampa la fase di collaudo sul tabulato della griglia di controllo lotto.
 :  : FLD T$GRFO **Griglia Fornitore**
Stampa della fase sul tabulato Griglia di controllo del fornitore. Nella fase di emissione di un ordine di Acquisto o C.to lavori, se richiesto nella 'Gestione Fornitori', il programma stampa assieme all'ordine, anche la griglia di controllo per il fornitore, in modo che possa essere consegnata all'interessato con l'ordine.
- ' '  Non stampa la fase sulla griglia Fornitore
- 'X'  Stampa la fase di collaudo sulla griglia di controllo a fornitore.
 :  : FLD T$STRU **Griglia Strumento**
Indica al programma che la fase del ciclo è riferita al controllo di uno strumento di misura.
- ' '  La fase non è relativa ad uno strumento di misura.
- 'X'  La fase è relativa ad uno strumento di misura.
 :  : FLD T$AUDI **Griglia Audit**
Indica al programma che la fase del ciclo è riferita al controllo ispettivo (AUDIT)
- ' '  La fase non è relativa ad un Audit.
- 'X'  La fase è relativa ad un Audit.
