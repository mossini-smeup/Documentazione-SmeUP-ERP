# Obiettivi
 * Ricevere e controllare la domanda verso termini e condizioni di fornitura concordati con il cliente;
 * Creare un Piano Principale di Produzione : 
 ** capace di soddisfare la domanda
 ** livellato (in caso di picchi di domanda)
 ** atto a minimizzare l'inventario
 ** verificato verso la disponibilità di risorse produttive
 ** verificato verso la disponibilità dei componenti
 * Fornire strumenti di verifica se il piano di produzione corrente è in grado di supportare (e quando) eventuali domande aggiuntive.

La domanda e il piano di produzione possono essere controllati ed elaborati sia a livello di singolo dettaglio (es. :  articolo o articolo / cliente) che a livello di famiglia di raggruppamento (es. :  classi di articoli, categorie clienti, responsabile commerciale, ecc...).
Le risorse verso cui eseguire la verifica possono essere le risorse principali e secondarie di produzione (centri di lavoro, persone, attrezzature, ecc...) e i materiali necessari.

# Definizioni
In questa sezione vengono spiegate le definizioni adottate nell'applicazione.

## Piano
Con piano si intendono tutte le informazioni provenienti da sistemi esterni (domanda cliente, programmi di produzione, budget, previsioni, ...) o generate all'interno dell'applicazione (esplosione dei componenti di un piano di produzione, piano di variazione, piano delle risorse richieste).
Un piano è caratterizzato da : 
 * codice;
 * descrizione;
 * impostazione / periodicità;
 * data inizio.

## Vista piano
Ciascun piano è costituito da un insieme di viste di piano, caratterizzate da un tipo record e corrispondenti ciascuna a una determinata necessità.
Ad esempio possiamo avere : 
 * vista del piano degli ordini cliente a livello "Cliente" - "Articolo", che rappresenta la domanda consolidata;
 * vista del piano ordini cliente a livello "Articolo", che rappresenta la domanda consolidata totale;
 * vista del piano delle risorse richieste, che rappresenta il fabbisogno risorse e che, confrontato con la disponibilità data dal calendario risorse, indica il grado di fattibilità.

Una vista piano è una matrice costituita di colonne che rappresentano i periodi e di righe che rappresentano le quantità per periodo delle entità caratteristiche della vista di piano (righe Cliente-Articolo, Qtà-Periodo 1, Qtà-Periodo 2, ecc...).

![MP_001_04](http://localhost:3000/immagini/MBDOC_OPE-MP_OPE/MP_001_04.png)
Un piano può essere visto in forma tridimensionale come una serie di strati, ognuno dei quali rappresentato da una vista piano.

![MP_001_05](http://localhost:3000/immagini/MBDOC_OPE-MP_OPE/MP_001_05.png)
Tutte le funzioni di trattamento di un piano possono essere ricondotte a delle operazioni su una vista o su una coppia di viste e il cui risultato può generare una nuova vista o aggiornarne una esistente.

# Impostazione del piano / Periodicità
Nel piano le quantità vengono sviluppate su 120 periodi, la cui ampiezza dipende dall'impostazione scelta.
Ad esempio, se la periodicità è settimanale, tutti i periodi del piano hanno ampiezza settimanale.
Possiamo avere periodicità : 
 * __giornaliera__ :  tutti i periodi hanno l'ampiezza di un giorno;
 * __settimanale__ :  tutti i periodi hanno l'ampiezza di una settimana;
 * __mensile__ :  tutti i periodi hanno l'ampiezza di un mese;
 * __composte__ :  costituite da un numero di periodi con ampiezza giornaliera, altri con ampiezza settimanale e altri ancora con ampiezza mensile.

Il numero delle periodicità composte può variare a seconda delle diverse necessità.
I tipi di impostazione piano sono registrati nella tabella A£Q (periodicità), in cui è possibile modificare, aggiungere o togliere nuove impostazioni.
