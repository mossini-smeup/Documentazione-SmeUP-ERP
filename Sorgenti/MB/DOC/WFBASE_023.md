# Cosa tratta

Work.up è un framework per la gestione di processi aziendali.

## I processi

Un processo è un insieme di compiti (impegni) organizzati teso al raggiungimento di un obiettivo.
 * Coinvolge più utenti.
 * Gli impegni non sono necessariamente sequenziali.
 * Gli impegni possono essere svolti su Sme.up (es :  la modifica di un articolo) oppure fuori (es :  una telefonata).

Consideriamo un semplice esempio di processo, relativo alla modifica di documentazione tecnica : 

![WFBASE_002](http://localhost:3000/immagini/WFBASE_023/WFBASE_002.png)Nella figura sono visibili : 
 * l'inizio e la fine del processo.
 * gli impegni di cui è composto (rettangoli) :  ognuno deve essere eseguito da una e una sola persona.
 * i potenziali esecutori di tali impegni.
 * le relazioni di precedenza tra gli impegni.
 * la presenza di scelte in particolari punti del processo.


Molte attività aziendali possono essere viste come processi, ad esempio : 
 * Studio di un nuovo articolo.
 * Revisione di documentazione.
 * Vendita, dall'ordine alla consegna.
 * ...

# Cosa fa

## Supporta l'operatività sui processi

Work.up guida gli utenti nell'esecuzione dei processi : 
 * attiva gli impegni non appena diventano eseguibili.
 * rende visibili gli impegni a tutti e solo gli utenti che li possono eseguire.
 * porta negli impegni tutte le informazioni necessarie per svolgere il lavoro :  oggetti Sme.up, documentazione, chiamate di menù...

## Tracciabilità

Ogni attività sui processi è tracciata ed è visibile : 
 * durante l'esecuzione del processo (percezione del livello di avanzamento).
 * a posteriori (analisi dei processi e benchmarking).


# Come si prova

È stato predisposto un ambiente di demo/test D29 per presentare alcuni processi concreti sviluppati o in sviluppo da clienti. Questi processi agiscono su dati dell'ambiente di sviluppo.

# Come funziona

## Definizione dei processi

Innanzitutto è necessario creare i modelli per i processi che Work.up dovrà gestire. Questo significa, per ogni processo (es. la revisione di documentazione vista in precedenza) specificare : 
 * di quali impegni è composto ("Chiedi modifica", "Modifica", "Delega"...)
 * quali utenti possono eseguire ogni impegno ("Chiedi modifica" :  Verde, "Modifica" :  Giallo1, Giallo2, ...)
 * quali sono le relazioni di precedenza tra gli impegni ("Modifica" viene dopo "Chiedi modifica", ...)
 * cosa deve essere fatto per ogni impegno (in "Chiedi modifica" bisogna specificare un documento, in "Modifica" questo documento va modificato...)

## Esecuzione dei processi

Una volta che il modello del processo è terminato, Work.up è pronto per gestirne l'esecuzione.
Nell'esempio della documentazione verrà creata un'istanza (ordine di workflow) del processo per ogni modifica di documentazione richiesta :  per ogni ordine verranno gestiti gli impegni in base al modello definito nel processo.
Quindi, ad esempio : 
 * l'ordine viene sempre creato dall'utente Verde.
 * l'ordine 1 relativo al Documento 1 potrebbe essere gestito dall'utente Giallo1, l'ordine relativo al Documento 2 dall'utente Giallo2.
 * l'ordine 1 potrebbe essere subito mandato al responsabile Arancio mentre l'ordine 2 passato all'utente Rosa 2...
 * ...e così via.

## Analisi dei processi

Per ogni ordine viene tracciata completamente la storia (chi ha fatto cosa, quando), consultabile durante l'esecuzione dell'ordine oppure a posteriori.
È quindi possibile in ogni momento conoscere in maniera approfondita la situazione presente e passata degli ordini di workflow, al fine di orientarsi nello svolgimento del lavoro oppure di analizzare e migliorare i processi.
