# Scheda Pianificazione
Questa scheda presenta una panoramica degli indicatori principali dell'elaborazione MRP e permette di accedere alle schede di dettaglio di navigazione suggerimenti e di analisi degli indici e delle quantità superflue.

## Presentazione
La scheda si può presentare in forme diverse a seconda che siano attive o meno la gestione multiscenario e la gestione multiplant : 

In una gestione miltiscenario / multiplant, prima di presentare gli indicatori dell'elaborazione MRP viene chiesto di scegliere nelle liste scenari e plant quelli da analizzare, dopo la scelta si popolano i cruscotti.

![M5CMRP_020](http://localhost:3000/immagini/MBDOC_SCH-M5CMRP/M5CMRP_020.png)
Se invece la gestione è monoscenario e monoplant la parte relativa alla scelta non viene visualizzata e si presentano direttamente gli indicatori dell'ultima elaborazione MRP.

![M5CMRP_021](http://localhost:3000/immagini/MBDOC_SCH-M5CMRP/M5CMRP_021.png)
## Indici
Vengono presentati degli indici relativi alla bontà del processo di pianificazione : 

- Suggerimenti scaduti di pianificazione (totale e per tipologia), indicano la tempestività nell'applicazione dei suggerimenti stessi oppure l'entrata improvvisa di una domanda sotto il lead time cumulato
- Consigli di eliminazione ordini in corso (totale e per tipologia), indicano la presenza di ordini che non coprono nessun fabbisogno, potrebbe essere anche il sintomo di una caduta della domanda
- Overcover, indica per quanti mesi sono coperto da scorte e quantità eccedenti in magazzino
- Immobilizzo superfluo, è il rapporto tra il valore dell'eccedenza presente, rispetto alla somma dei valori dell'eccedenza presente e della scorta.

**N.B.**, per attivare il calcolo degli indici si deve impostare opportunamente il relativo flag nello scenario (tab. M5B).

## Navigazione
Con i bottoni di questa sezione si passa ad aprire delle schede di dettaglio dedicate alla navigazione, secondo vari criteri, dei suggerimenti MRP : 

- Per articolo (o per articolo e oggetto di rottura se quest'ultimo è gestito in Tab. M51)
- Per oggetto di riferimento (se è impostato nello scenario - Tab. M5B) e suggerimento
- Per suggerimento
- Per fonte
- Per ente


## Analisi
Con i bottoni di questa sezione si passa ad aprire delle scehde di dettaglio dedicate all'analisi MRP : 

- Quantità superflue
- Indici



- [Scheda Pianif. Navigazione](Sorgenti/MB/DOC_SCH/M5CMRP_N)
- [Scheda Pianif. Indici](Sorgenti/MB/DOC_SCH/M5CMRP_I)
- [Scheda Pianif. Quantità superflua](Sorgenti/MB/DOC_SCH/M5CMRP_A)
- [Scheda Analisi nel tempo per periodo](Sorgenti/MB/DOC_SCH/M5)
