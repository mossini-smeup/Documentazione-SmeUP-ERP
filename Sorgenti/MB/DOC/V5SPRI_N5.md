# Spedizione in C/Lavoro
Si può decidere di spedire per : 
 * impegno (a bilanciamento)
 * per documento (tutti gli impegni di un documento per una qtà di riferimento dell'assieme)

In questo secondo caso __NON__ viene fatto alcun bilanciamento :  viene proposta la qtà indipendentemente da spedizioni precedenti a fronte dello stesso documento / riga. Viene comunque presentato a fianco il bilanciamento (sommatoria impegni e sommatoria disponibilità c/o il terzista) su cui regolarsi.

Si può selezionare (in V5AT40L) uno dei due modi, con eventuale possibilità di switch all'altro.
**Nota bene**, nella finestra di scelta documento, l'F12 ha l'effetto di fine lavoro nel caso in cui si sia in spedizione per documento e non ci sia nessun documento attivo. Se si era in spedizione per impegno e si è appena passati alla spedizione per documento ha l'effetto di ritornare alla spedizione per impegno (non è facoltativo). Se si è in spedizione per documento e c'è un precedente documento attivo ha l'effetto di ritornare ad esso.
Il caso di uscita si ha subito dopo la conferma di una spedizione per documento quando non si può ritenere attivo il documento da cui si è spedito, oppure all'ingresso, con partenza da spedizione per documento, in cui non c'è niente di attivo :  in questi due casi non si saprebbe a cosa tornare in uscita.

In spedizione per documento si può scegliere di tener traccia, sul documento di bolla generato, del documento origine :  si mette il tipo documento / numero documento / numero riga (con segno negativo per distinguerlo dai documenti di ingresso che chiuderanno l'ordine). Nei movimenti di magazzino questo si tradurrà nel campo S§RES1 in xxxx-SPE (dove xxxx è il numero di riga), il campo S§RES1è alfanumerico lungo 8.

# Bilanciamento spedizioni
Se si è tenuta traccia dei movimenti di spedizione in C/Lavoro a fronte del documento / riga è possibile avere una situazione indicativa del residuo da spedire che è dato da : 

**Impegno residuo + movimenti di consumo - bolle di spedizione (per documento origine / riga)**

