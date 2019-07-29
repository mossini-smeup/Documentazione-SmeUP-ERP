# Obiettivo
Utilizzando le quantità riportate sulle singole non conformità, calcolare ed analizzare i relativi livelli di qualità (LQ).

## Formato guida
![CQ_PARE_07](http://localhost:3000/immagini/MBDOC_OGG-P_CQNS20/CQ_PARE_07.png)
Nelle varie forme abilitate (emissione a video, stampa o file di parcheggio dati) è possibile calcolare gli LQ desiderati fino ad un massimo di 4 (quattro).

_2_Formule
Il calcolo è subordinato all'immissione delle relative formule matematiche utilizzando i valori corrispondenti alle quantità riepilogate su ogni non conformità.
La memorizzazione delle formule a gruppi di 4 oppure singolarmente permette il loro riutilizzo in successive analisi senza la necessità di ridigitarle.

_2_Ordinamento
Con la scelta dell'ordinamento vengono fissati i valori con i quali raggruppare le singole non conformità e sul totale delle quali calcolare ogni singolo LQ.
Sono possibili fino a 3 valori di ordinamento scalare con la obbligatorietà di sceglierne almeno 1.
1 - 2 e 3 indicano la priorità del valore di raggruppamento :  Le non conformità verranno suddivise e totalizzate secondo il valore identificato dal '1'; all'interno del valore '1' l'ordinamento avviene secondo il valore '2'; all'interno del valore'2' l'ordinamento avviene secondo il valore '3'.

Esempio : 
Sono state eseguite le seguenti scelte sull'ordinamento :  1 Codice Articolo, 2 Codice Difetto e 3 Codice Causa Difetto.

Per ogni CODICE ARTICOLO verranno listati tutti i CODICI DIFETTO ad esso abbinati, con la visualizzazione per ogni codice difetto di tutti i CODICI CAUSA DIFETTO a sua volta abbinati.

_2_Ordinamento LQ
l'ordine ascendente o discendente di UNO dei 4 LQ calcolati. E' permesso l'abbinamento di UNO solo dei 4 LQ calcolati per ogniuno dei 3 valori scelti nell'ordinamento.

_2_Limiti
Con l'impostazione dei limiti vengono selezionate le non confor mità con i valori compresi tra quelli impostati.

## Gestione delle formule per gli LQ
Si attiva con il comendo funzione F15 : 
![CQ_PARE_08](http://localhost:3000/immagini/MBDOC_OGG-P_CQNS20/CQ_PARE_08.png)
Utilizzando l'identificativo delle quantità dei non conformi (V01 corrisponde alla quantità LOTTO, V02 alla quantità controllata ecc.) vengono costruite le quattro formule di calcolo degli LQ. Ad ogni formula di calcolo è possibile attribuire un nome (con lunghezza massima di 8 caratteri) per facilitarne l'identificazione.
Il campo posizionato nell'angolo superiore destro della finetra abilita la memorizzazione GLOBALE delle 4 formule di calcolo degli LQ.
A fianco del nome della formula è posizionato il campo con il qualeè possibile attivare la MEMORIZZAZIONE SINGOLA di ogni formula.
La formula di calcolo può essere costruita con un massimo di 40 caratteri rispettando le normali regole algebriche. Il tasto INVIO conferma quanto immesso nella finestra con la segnalazione delle formule scelte anche sul formato guida.

## Scelta dei limiti sui codici
In base agli ordinamenti scelti dal formato guida è possibile fissare un numero massimo di valori da listare per ogni ordinamento selezionato.
Se per l'ordinamento "codice articolo" viene fissato un Nr Massimo di 10, verranno listati solo i PRIMI 10 "articoli" secondo la logica di selezione scelta.

## Scelta dei limiti sugli LQ calcolati
La scelta dei valori da listare può essere ulteriormente mirata fissando anche i limiti INFERIORE e SUPERIORE entro i quali deve posizionarsi il risultato del calcolo degli LQ selezionati.
Il valore inferiore di ordinamento compreso tra i limi impostati condiziona la lista anche dei valori di livello superiore omettendo il controllo sui valori limite degli LQ.

## Selezione al primo livello di dettaglio
![CQ_PARE_09](http://localhost:3000/immagini/MBDOC_OGG-P_CQNS20/CQ_PARE_09.png)
## Selezione al secondo livello di dettaglio
![CQ_PARE_10](http://localhost:3000/immagini/MBDOC_OGG-P_CQNS20/CQ_PARE_10.png)
## Selezione al terzo livello di dettaglio
![CQ_PARE_11](http://localhost:3000/immagini/MBDOC_OGG-P_CQNS20/CQ_PARE_11.png)
Con l'opzione 5 di consulta il dettaglio della non conformità.

