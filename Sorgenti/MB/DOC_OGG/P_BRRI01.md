# Generalità
In un'azienda le attività produttive vengono eseguite generalmente da macchine presenti all'internodi reparti o di linee di produzione, di solito più macchine aventi caratteristiche uguali vengono identificate come dei centri di lavoro.
In Sme.up linee, centri di lavoro, macchine, lavoratori, reparti, ecc..vengono identificati come risorse e gestiti, con una modalità comune, in un unico anagrafico.

## Tipi risorse
Per differenziare le varie risorse si utilizza il Tipo Risorsa (codificato nella tabella BRR).

## Gestione risorse
Per attivare la gestione risorse si utilizza il seguente formato guida : 

![BR_03_01](http://localhost:3000/immagini/MBDOC_OGG-P_BRRI01/BR_03_01.png)Utilizzando le opzioni si accede al formato di dettaglio dove sono presentati tutti i campi propri
dell'anagrafico risorse : 

![BR_03_02](http://localhost:3000/immagini/MBDOC_OGG-P_BRRI01/BR_03_02.png)
### Descrizione dei campi
Di seguito descriveremo solo i campi significativi : 

- _3_Centro di costo, il campo è la _2_'Risorsa di appartenenza'  definita nella tabella BRR(in questo caso per il tipo risorsa CDL è stato fissato che il tipo risorsa di appartenenza è ilcentro di costo)

- _3_Gruppo risorsa, è un elemento della tabella BRM dove, per ciascun gruppo sono fissate le caratteristiche (tipicamente potremmo avere risorse interne in cui le caratteristiche sono quelle tipiche di una risorsa interna e risorse esterne dove le caratteristiche sono quelle tipiche di un terzista)

- _3_Magazzino / Ubicazione, è possibile assegnare ad una risorsa anche una collocazione fisica, descritta dal magazzino (plant) e ubicazione (di linea)

- _3_Assegnata a, dipende dalla tabella BRM, ad esempio se il gruppo risorsa è una risorsa esterna in questo campo si inserisce il codice fornitore

- _3_Coefficiente efficienza standard, si utilizza nel calcolo (costi e carico macchine) per maggiorare i tempi inseriti nei cicli di produzione tenendo conto dell'efficienza.

- _3_Codice di carico, è un codice che stabilisce quali informazioni del ciclo utilizzare nel calcolo (costi e carico macchine) :  tempo lavoro è il tempo speso dall'uomo asservito alla macchina, tempo macchina è quello della macchina, tempo attrezzaggio è quello speso per attrezzarela macchina)

- _3_Coda media, può essere espressa in giorni o in ore (dipende dalle impostazioni generali della tabella BRM) e rappresenta il tempo medio di attesa per un lotto prima di entrare in lavorazione nella macchina, di solito si usa nel carico macchine. In funzione delle impostazioni può essere un tempo di attesa prima della lavorazione oppure un tempo di fermata successiva prima dell'accodamento alla macchina che esegue la prossima lavorazione.

- _3_Note strutturate, se impostato in tabella BRM da questo campo si accede alla gestione delle note per questa risorsa (cfr. B£NOTE Gestione note)

