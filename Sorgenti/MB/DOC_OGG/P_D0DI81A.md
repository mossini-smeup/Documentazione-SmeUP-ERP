## Costruzione Distinta Ordine di Produzione

Costruisce la distinta effettiva di un ordine di produzione attraverso i suoi movimenti di versamento e prelievo di magazzino.
Il tipo distinta può essere intestata all'ordine di produzione o al lotto.

>Distinta dell'ordine
E' la distinta dell'ordine stesso. L'assieme è l'ordine e i componenti sono gli articoli prelevati.
Il coefficiente di ciascun articolo è la media sul totale versato, di tutti i prelievi dell'articolo stesso.

>Distinta del lotto
A standard Smeup si assume che l'ordine di produzione corrisponda al lotto.
L'assieme il lotto, che corrisponde all'ordine, e i componenti sono i lotti prelevati.
Il coefficiente di ciascun lotto è la media sul totale versato, di tutti i prelievi del lotto stesso.

>La costruzione della distinta d'ordine ha la seguente logica : 
 * Per Versamenti con prelievi a back-flushing
 ** Verifica tutti i versamenti di prodotti dichiarati buoni interni _9_(Movimenti VP che hanno l'ordine in S§NR01)
 ** Prende i relativi prelievi pianificati collegati a takli versamenti _9_(campo S§DTFF del GMMOVI con tipo movimento PP)
 ** Verifica tutti i versamenti di prodotti dichiarati buoni esterni _9_(Movimenti VE che hanno l'ordine in S§NR02)
 ** Prende i relativi prelievi pianificati collegati a takli versamenti _9_(campo S§DTFF del GMMOVI con tipo movimento PE)
 ** Verifica tutti i versamenti di prodotti dichiarati scarti interni _9_(Movimenti VS che hanno l'ordine in S§NR01)
 ** Prende i relativi prelievi pianificati collegati a takli versamenti _9_(campo S§DTFF del GMMOVI con tipo movimento PS)

 * Va a verificare se ci sono prelievi generici e non associbili ai versamenti
 _9_Prenderà tutti i tipi di prelievo (PP - PE - PS, dove difficilmente per i PE la condizione sarà verificabile) che non hanno il campo S§DTFF popolato e che hanno l'ordine di produzione conla seguente logica : 
 ** _9_PP con S§NRO1 = Ordine
 ** _9_PE con S§NRO2 = Ordine (Non riscontrabile genericamente)
 ** _9_PS con S§NRO1 = Ordine 

 * Flag "Versamenti a scarti"
 ** Se è impostato uguale a *BLANKS = NO il sistema non porterà al denominatore la quantità degli scarti penalizzando i prodotti buoni anche della quantità di materiale prelevata per gli scarti.
 ** Se è impostato uguale a "1" = SI, al denominatore si porterà il numero dei buoni più gli scarti, non penalizzando il costo del prodotto (caso che potrebbe essere utilizzato laddove il materiale utilizzato per gli scarti viene recuperato per altre produzioni e si devida di non penalizzare questa produzione).


>La costruzione della distinta di lotto ha la seguente logica : 
 * Controlli idi carattere generale sui vari metodi : 
 ** Vi saranno controlli di congruenza se il lotto corrisponde a quell'articolo
 ** Vi saranno controlli di validità del lotto assegnato al movimento che deve esistere

 * Per "Metodi di costruzione *BLANKS = Un ordine n lotti" : 
 ** I lotti assunti saranno quelli del versamento e dei prelievi senza alcuna forzatura
 ** Se viene versato più di un lotto per ordine verrà generata una distinta di lotto per     ogni lotto versato, anche se distinte equivalenti nei componenti e nei coefficienti

 * Per "Metodi di costruzione 1 = Un ordine un lotto fittizio" : 
 ** Verrà eseguita una forzatura dove ad ogni ordine verà assegnato un lotto fittizio     di tipo £D0, creando una distinta base relativa a tutti i lotti versati che avranno     come assieme il relativo lotto fittizio
 ** Verrà creato il lotto fittizio sull'anagrafico dei lotti


 * Per "Metodi di costruzione 2 = Un ordine n lotti raggruppati su lotto ordine" : 
 ** Sarà obbligatoria la presenza del lotto sulla testata dell'ordine di produzione
 ** Tutti i versamenti, anche se eseguiti su lotti diversi, verranno intestati al lotto     presente sull'ordine di produzione
 ** Per ogni lotto di prelievo arà controllata la presenza sull'anagarfico lotti dell'ordine     di produzione che lo ha generato, affinchè si possa recuperare il lotto intestato a tale     ordine e sostituirlo al lotto individuato nel versamento, così da normalizzare sia i     versamenti che i prelievi
 ** Verrà generata una sola distinta che come assieme ha il lotto legato all'ordine di     produzione

