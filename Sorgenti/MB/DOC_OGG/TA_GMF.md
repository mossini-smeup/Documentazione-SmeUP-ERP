# GMF - Forme presentazione giacenze
## OBIETTIVO
Definire l'ordinamento di un'interrogazione dell'archivio GMQUAN0F Giacenze di Magazzino.
Ciò implica la costruzione di una vista logica (eseguita in modo trasparente all'utente) che realizzerà l'ordinamento selezionato.
La prima volta che si interrogano le giacenze con una forma di presentazione che usa una nuova vista logica, il sistema emette una finestra in cui chiede di autorizzare la creazione con F24.
## CONTENUTO DEI CAMPI
 :  : FLD T$K,1 __Campo chiave 1/8 __
Definiscono l'ordinamento (fino ad 8 chiavi) dell'interrogazione selezionata.
Si possono selezionare :  l'articolo (A), il magazzino (M), l'area (R), il tipo giacenza (T), e le chiavi specifiche del tipo giacenza (1/2/3/4).
Deve essere impostato almeno il primo campo.
Non è possibile specificare due volte la stessa chiave, né lasciare spazi bianchi intermedi. Inoltre, non si possono specificare le chiavi 1/4 più in alto del tipo giacenza T (in quanto il loro significato è dato dal tipo giacenza, e quindi sono individuabili solo dopo che esso è stato fissato).
 :  : FLD T$K,2.T$K,1  __Campo chiave__
 :  : FLD T$K,3.T$K,1  __Campo chiave__
 :  : FLD T$K,4.T$K,1  __Campo chiave__
 :  : FLD T$K,5.T$K,1  __Campo chiave__
 :  : FLD T$K,6.T$K,1  __Campo chiave__
 :  : FLD T$K,7.T$K,1  __Campo chiave__
 :  : FLD T$K,8.T$K,1  __Campo chiave__
 :  : FLD T$GM,1 __Totale (1/8)__
Stabiliscono se devono essere calcolati i totali per la chiave.
Non può essere specificato un totale per l'ultima chiave valida (massimo dettaglio).
Non si può specificare il totale se non si specifica la chiave relativa.
**NOTA** :  il calcolo dei totali può rallentare l'elaborazione.
 :  : FLD T$GM,2.T$GM,1 __Totale__
 :  : FLD T$GM,3.T$GM,1 __Totale__
 :  : FLD T$GM,4.T$GM,1 __Totale__
 :  : FLD T$GM,5.T$GM,1 __Totale__
 :  : FLD T$GM,6.T$GM,1 __Totale__
 :  : FLD T$GM,7.T$GM,1 __Totale__
 :  : FLD T$GM,8.T$GM,1 __Totale__
 :  : FLD T$NRVL __Nome vista logica__
Definisce il nome che assumerà nel sistema la vista logica costruita per questa interrogazione.
Si consiglia di chiamarla GMQUANnX dove n è un carattere alfanumerico (Evitare il nome GMQUANXL che è l'archivio sorgente di esempio).
 :  : FLD T$GMFA __Area di default__
È un elemento della tabella GMR :  se impostato verrà proposto questo valore nell'interrogazione.
 :  : FLD T$GMFB __Area protetta__
In presenza del campo precedente, se impostato impedirà la variazione dell'area.
 :  : FLD T$GMFC __Tipo giacenza di default__
È un elemento della tabella GMQ :  se impostato verrà proposto questo valore nell'interrogazione.
 :  : FLD T$GMFD __Tipo giacenza protetta__
In presenza del campo precedente, se impostato impedirà la variazione del tipo giacenza.
 :  : FLD T$GMFE __Magazzino di default__
È un elemento della tabella MAG :  se impostato verrà proposto questo valore nell'interrogazione.
 :  : FLD T$GMFF __Magazzino protetto__
In presenza del campo precedente, se impostato impedirà la variazione del magazzino.
 :  : FLD T$GMFG __Visualizzazione estesa__
Stabilisce la forma di visualizzazione da utilizzare. La forma estesa prevede la presentazione di tutte le quantità presenti nel file delle giacenze, mentre la forma ridotta presenta solo il valore della giacenza.
 :  : FLD T$GMFH __Riempimento progressivo codici__
Se impostato, quando si inserisce un codice di selezione (area, articolo, magazzino, ecc...), devono essere riempiti tutti i codici precedenti ad esso, previsti da questa forma di interrogazione. In questo modo si riduce la possibilità di richiedere interrogazioni non ottimizzate.
