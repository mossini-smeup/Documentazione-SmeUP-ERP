# BRU - Tipo matricola
 :  : DEC T(ST) K(BRU)
## OBIETTIVI
-    Caratterizzare la tipologia delle matricole in modo da poterla utilizzare per impostare comportamenti comuni a matricole dello stesso tipo
## SOTTOSETTORI
Non gestiti
## INTRODUZIONE
Per ogni tipo matricola si possono definire caratterizzazioni che verranno utilizzate per tutte le matricole dello stesso tipo
## CONTENUTO DEI CAMPI
 :  : FLD T$BRUC **Sottosettore categoria matricole**
Indica il sottosettore della tabella BRW dove sono contenute le categorie delle matricole valide.
 :  : FLD T$BRUA **Categoria assunta**
Indica la categoria (elemento della tabella BRW) assunta per default per questo tipo matricola.
 :  : FLD T$BRUS **Struttura costruzione**
È un elemento della tabella B£F e rappresenta il flusso di domande che sovrintende alla costruzione del codice (ed eventualmente alle altre caratteristiche) di una matricola di questo tipo.
 :  : FLD T$BRUT **Tipo codice collegato**
È la tipologia dell'oggetto collegato alla matricola
 :  : FLD T$BRUP **Parametro codice**
È il parametro del tipo codice
 :  : FLD T$BRUL **Livello di nascita**
È un elemento della tabella B£W00 :  le matricole di questo tipo nasceranno con il livello qui impostato e con il primo stato di questo livello.
 :  : FLD T$BRUB **Separatore per trasformazione**
Quando un oggetto (A), gestito a matricole, viene trasformato in un altro (B), l'oggetto nuovo eredita il numero di matricola di A mentre la matricola di A cambia codice secondo la seguente modalità :  al codice di A viene attaccato un eventuale separatore specificato da questo campo di tabella e anche un contatore numerico la cui dimensione può essere specificata nel campo 'Dim. contatore x trasf.'.
 :  : FLD T$BRUN **Dim. contatore per trasformazione**
Indica quante cifre decimali devono essere usate nel contatore delle matricole trasformate (vedi campo precedente per le matricole trasformate).
Esempio :  se la matricola A010 venisse trasformata con impostato come separatore il carattere '/' e come dimensione del contatore 2, la matricola diverrebbe A010/01.
