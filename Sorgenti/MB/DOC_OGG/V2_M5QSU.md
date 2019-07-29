# M5QSUP    -  TIPO QUANTITA' SUPERFLUA
Definisce i vari tipi di quantità superflua. E' un campo impostato nel consiglio di pianficazione dalla pianficazione
stessa.
I vaLori di tipo "eccedenza" sono assegnati nei consigli specifici di quantità eccedente (origine fonte 'QE'), mentre
i valori di tipo "quantità da ridurre o eliminare" sono assegnati ai consigli su cui si applica il suggerimento.
In questo modo tutti i consigli di qwantità superflua, sia eliminabile (riduzione e annullamento) sia quella non
eliminabile (eccedenza) hanno una caratteristica comune.

## VALORI POSSIBILI

### 'S' Eccedenza presente
E' la quota parte della giacenza che non trova nessun fabbisogno da soddisfare.
### 'F' Eccedenza futura rilasciata
E' la quota parte di un ordine rilascitato che non trova nessun fabbisogno da soddisfare, e che non si può ridurre in
quanto violerebbe i vincoli di lotto minimo e multiplo.
Ad esempio, se si ha la seguente sutuazione : 
.. Fabbisogno 156
.. Ordine rilasciato 234
.. Lotto minimo 100
.. Lotto multiplo 25
Il sistema dà i seguenti comsigli : 
.. Ridurre l'ordine da 234 a 175 (la più bassa combinazione di lotto minimo e multiplo superiore al fabbisogno).
.. Quantità eccedente rilasciata di 19 (differenza tra riduzione (175) e fabbisogno (156).
### 'S' Eccedenza futura fissa
Nel caso di una copertura appartenente ad una fonte fissa, che deve essere ridotta o annullata per assenza di fabbisogni,
viene segnalata, come quantità eccedente, la quantità di riduzione, oppure la quantità totale (qualora l'ordine sia da
annullare).
### 'P' Eccedenza futura pianificata
E' la stessa situazione dell'eccedenza futura rilasciata, con la differenza che si applica ad un ordine pianificato.
### 'U' Eccedenza futura recuperata rilasciata
Nel caso di un recupero (impegno negativo su di un ordine rilasciato) che non trova fabbisogni da coprire, ma che
evidentemente è obbligatorio produrre (essendo un coporodptto dell'assieme che invece è necessario) viene segnalata
un'eccedenza, simile a quella per le fonti fisse.
### 'V' Eccedenza futura recuperata pianificata
E' la stessa situazione dell'eccedenza futura recuperata rilasciata, con la differenza che il recupero viene generato da
un ordine pianificato.
### 'R' Quantità da ridurre
I consigli di riduzione vengono caratterizzati da questo valore.
Questi consigli vengono attribuiti alle coperture rilasciate, la cui quantità ha solo in parte fabbisogni da coprire.
La quantità del suggerimento è quella a cui si deve portare la copertura, non quella di riduzione. La modifica della
copertura avviene sostituendo questa quantità a quella originale.
Esempio : 
.. Quantità ordinata 100
.. Quantità fabbisogno 80
Il sistema dà il seguente comsiglo : 
.. Ridurre la quantità ordinata da 100 a 80
Se la copertura è parzialmente evasa, si fa comunque riferimento per la riduzione, (compresi i controlli di non
violazione dei lotti), alla quantità ordinata.
Esempio : 
.. Quantità ordinata 100
.. Quantità ricevuta 40
.. Quantità residua  60
.. Quantità fabbisogno 50
Il sistema dà il seguente comsiglo : 
.. Ridurre la quantità ordinata da 100 a 90
In tal modo la quantità residua diventa 50 (nuova quantità ordinata 90 - quantitò ricevuta 40), eguqgliando il
fabbisogno.
### 'A' Quantità da eliminare
I consigli di annullamento vengono caratterizzati da questo valore.
Questi consigli vengono attribuiti alle coperture rilasciate, la cui quantità non ha nessun fabbisogno da coprire-
