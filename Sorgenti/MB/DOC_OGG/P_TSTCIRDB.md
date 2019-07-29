# SCANSIONE CICLI DI LAVORO
# Introduzione
Scopo della routine £CIR è di scandire, in sequenza, le fasi del ciclo di lavorazione.
# Funzioni
## Forma di conversione
I tempi (schiera £CRV), vengono ritornati nel seguente modo : 
-    Se l'unità di misura di presentazione (£CIRUP) è blanks, sono ritornati come sono memirizzati in archivio (in
secondi)  :  questo modo serve nel caso in cui la schiera dei tempi dovrà essere elaborata successivamente con la £BRT,
(ad esempio nel caso di calcolo di costi o di scansione schedulata).
-    Se l'unità di misura di presentazione (£CIRUP) è '**', sono ritornati nell'unità di misura in cui sono stati
inseriti.
-    Se l'unità di misura di presentazione (£CIRUP) è un altro valore, sono ritornati in questa unità di misura.
## Scansione tecnica
Vengono ritornati i valori di tutte le fasi del codice.
## Scansione di produzione
Vengono ritornati i valori delle fasi valide del codice usando i filtri di configurazione, di date di validità, ed
eventualmente, se il codice non ha un ciclo proprio, il gruppo ciclo dell'anagrafica articoli (se il codice da
esplodere è un articolo). Se il codice ha gruppo ciclo blanks e gruppo distinta valorizzato, viene assunto
quest'ultimo.
## Scansione schedulata
## Implosione Risorsa
Vengono ritornati i valori di tutte le fasi della risorsa.
## Dettaglio operazione
Vengono ritornati i valori della fase contrassegnata dal numero di record ricevuto.
# Parzializzazioni
Le parzializzazioni di data di validità e configurazione sono controllate in scansione di produzione e schedulata.
Le parzializzazioni sul ciclo sono controllate in scansione di produzione (sempre),  oppure se il ciclo ricevuto
(£CIRIZ) non è blanks.
Le parzializzazioni di sequenza, stato operazione e tipo operazione sono controllate se i campi ricevuti (£CIRIQ,
£CIRIS e £CIRIO) non sono blank.
