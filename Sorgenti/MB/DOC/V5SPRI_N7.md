# Reso a fornitore nel conto lavoro di fase
Nella gestione dei resi non conformi a fornitore in presenza di conto lavoro di fase si devono considerare : 
 * lo scarico della giacenza interna, che può essere : 
 ** area di magazzino, se l'entrata era sull'ultima fase del ciclo
 ** area non conformi (prodotti finiti) se ultima fase ed è attiva la gestione giacenze non conformi
 ** area di produzione interna semilavorati alla fase, se viene gestita una giacenza interna del prodotto alla fase
 ** area interna di non conformi semilavorati alla fase, se viene gestita una giacenza interna del prodotto alla fase ed è attiva la gestione giacenze non conformi
 *  il ricarico della giacenza esterna del terzista, che a sua volta può essere : 
 ** area di conto lavoro componenti, se l'entrata era sulla prima fase del ciclo (oppure, per componenti consumati alla fase, quando la fase è quella del consumo)
 ** area di conto lavoro di fase
 * lo storno dell'avanzamento produzione

# Possibile soluzione
Una modalità possibile è quella di un reso a fornitore con storno dell'ordine di conto lavoro : 
 * la testata del documento di reso può avere il flag 19 = "n" se si vuole dar luogo all'attesa di una nota di credito da parte del fornitore
 * il tipo riga deve avere : 
 ** causali di movimentazione proprie di scarico (rispetto al tipo riga di entrata merci eseguono lo scarico, dalle opportune aree / tipo giacenza interne)
 ** lo stesso parametro di conto lavoro utilizzato nel tipo riga di entrata merci
 ** flag 7 di di inversione qtà/valore = "1". **Nota Bene**, il valore del flag 7 può essere impostato da gruppo flag o secondo regole diverse, riferirsi all'help di tabella V51.
 ** causale di avanzamento produzione simile a quella della riga entrata merce con la differenza di avere impostato il flag 11 di storno.
