# Obiettivo
Utilizzando le funzioni abilitate (Video, Stampa o File di lavoro) consultare le non conformità rilevate.
## Formato guida
![CQ_PARE_02](http://localhost:3000/immagini/MBDOC_OGG-P_CQNS10/CQ_PARE_02.png)
Utilizzando le scelte del formato guida è possibile listare le non conformità secondo diversi valori di ordinamento,
con 3 livelli di totale e scegliendo se visualizzare le quantità o il valore di ogni non conformità.

_2_Ordinamento
Con la scelta dell'ordinamento vengono fissati i valori con i quali raggruppare le singole non conformità e sulle quali eseguire i calcoli dei totali (se scelti). Sono possibili fino a 3 valori di ordinamento scalare con la obbligatorietà di sceglierne almeno 1.
1 - 2 e 3 indicano la priorità del valore di raggruppamento :  le non conformità verranno suddivise e totalizzate secondo il valore identificato dal '1'; all'interno del valore '1' l'ordinamento avviene secondo il valore '2'; all'interno del valore'2' l'ordinamento avviene secondo il valore '3'.

Esempio : 
Sono state eseguite le seguenti scelte sull'ordinamento :  1 Codice Articolo, 2 Codice Difetto e 3 Codice Causa Difetto.
Per ogni CODICE ARTICOLO verranno listati tutti i CODICI DIFETTO ad esso abbinati, con la visualizzazione per ogni codice difetto di tutti i CODICI CAUSA DIFETTO a sua volta abbinati.

_2_Scelta Livello di Totale
In base agli ordinamenti scelti è possibile eseguire dei totali intermedi sui valori di ordinamento stesso. I livelli di totale 1 - 2 e 3 corrispondono esattamente ai livelli di ordinamento.
Pertanto se nell'ordinamento in corrispondenza del codice articolo viene immesso '1', la scelta del livello di totale '1' (inserendo un qualsiasi carattere nel campo sottostante) permetterà la totalizzazione dei valori scelti su ogni codice articolo.

_2_Scelta Quantità/Valore
Tenendo presente che il programma costruisce un MASSIMO di 4 colonne ogniuna delle quali contiene UNA o LA SOMMA DI PIU' quantità o valori selezionati.Le 4 colonne corrispondono esattemente ai quattro valori permessi per eseguire le scelte ovvero 1 - 2 - 3 - 4; la medesima scelta ripetuta più volte indica al programma che i valori corrispondenti verranno SOMMATI tra di loro.

_2_Limiti
Con l'impostazione dei limiti vengono selezionate le non confor mità con i valori compresi tra quelli impostati.

## Scelta valori in dettaglio
Si attiva dal fomato guida con F15 : 
![CQ_PARE_03](http://localhost:3000/immagini/MBDOC_OGG-P_CQNS10/CQ_PARE_03.png)
Con la scelta di consultazione di dettaglio viene costruita una riga contenente i dati propri di ogni singola non conformità. La costruzione del dettaglio può essere personalizzata selezionando i valori desiderati tra quelli indicati nella finestra di scelta. Sia pur permettendo la scelta su tutti i valori è scontato che, per esigenze di spazio, la riga conterrà tutto quanto selezionato fino alla sua campienza massima.

## Consultazione correlazione causa - difetto (esempio a 1 livello)
![CQ_PARE_04](http://localhost:3000/immagini/MBDOC_OGG-P_CQNS10/CQ_PARE_04.png)
## Selezione ordinamento non conformità (esempio a 2 livelli)
![CQ_PARE_05](http://localhost:3000/immagini/MBDOC_OGG-P_CQNS10/CQ_PARE_05.png)
## Consultazione non conformità per analisi difetti e costi ricorrente (esempio a 2 livelli)
![CQ_PARE_06](http://localhost:3000/immagini/MBDOC_OGG-P_CQNS10/CQ_PARE_06.png)
Per ognuna delle non conformità riportate è prevista una serie di opzioni tra cui la consultazione delle registrazioni effettuate tramite il modulo di gestione; il programma permette quindi di recuperare tutte le informazioni relative alla non conformità tra cui : 
 * azioni intraprese per risolvere il problema;
 * gli esiti di tali azioni;
 * quantità coinvolte;
 * i costi comportati dalla non conformità;
 * i responsabili;
 * il lotto di appartenenza della caratteristica su cui è stata rilevata la non conformità;
 * le note che sono state allegate durante la gestione delle non conformità;

Per un codice di difetto è possibile consultare tutti i lotti responsabili ed apparenti delle non conformità oltre che le non conformità per quei lotti.

_2_Nota; per lotto apparente si intende il lotto al quale appartiene il complessivo della caratteristica difettosa; per lotto responsabile si intende invece il lotto di origine della caratteristica responsabile della difettosità.
