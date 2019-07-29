## Costruzione Distinta Rifa Documento

Costruisce la distinta effettiva di una riga di documento attraverso i suoi movimenti di versamento e prelievo di magazzino.
Il tipo distinta può essere intestata alla riga di documento o al suo lotto.
Per riga documento si intente il codice NumeroDocumento+RigaDocumento

>Distinta della riga di documento
E' la distinta della riga stessa. L'assieme è la riga e i componenti sono gli articoli prelevati.
Il coefficiente di ciascun articolo è la media sul totale versato, di tutti i prelievi dell'articolo stesso.

>Distinta del lotto
L'assieme è il lotto della riga documento, e i componenti sono i lotti prelevati. Se non presente si assume "**". Il coefficiente di ciascun lotto è la media sul totale versato, di tutti i prelievi del lotto stesso.

>La costruzione della distinta della riga segue la seguente logica : 
 * Per Versamenti con prelievi a back-flushing
 ** Verifica tutti i versamenti esterni di conto lavoro pieno del documento_9_(Movimenti DO o VE che hanno il documento in S§TIDI, S§NRDI, S§CAST e con S§FLG1="1")
 ** Prende i relativi prelievi pianificati collegati a tali versamenti _9_(campo S§DTFF del GMMOVI con tipo movimento PE)

 * Va a verificare se ci sono prelievi generici e non associbili ai versamenti
 Prenderà i tipi di prelievo PE sulla riga documento _9_(Movimenti che hanno il documento in il documento in S§TIDI, S§NRDI, S§CAST) ma senza legami ad altri movimenti _9_(S§DTFF=0)



