## Introduzione
DOOR.up è il modulo di SME.up che raccoglie tutte e sole le funzioni utili all'organizzazione e al conseguente accesso a tutte le informazioni non organizzate come insieme di campi in un DATABASE e tipicamente files del file system. Le aziende hanno creato in questi anni un grande numero di documenti memorizzati in file su un server (documenti di testo, presentazioni, fogli elettronici). Tali documenti sono cresciuti prima come documenti individuali poi come come documenti condivisi ma solitamente senza una organizzazione precisa e in particolare senza una correlazione stretta con il sistema gestionale.

## Obiettivi
Questo modulo di SME.up vuole aiutare l'azienda a gestire un documento in modo analogo a come si gestiscono le altre informazioni aziendali, definendo pertanto un organizzazione, metodologie, autorizzazioni di accesso, modalità di ricerca, associazione di attributi ecc.
Come per gli altri moduli di SME.up anche in questo caso partiamo dal concetto che non necessariamente i documenti sono gestiti da SME.up e quindi DOOR.up sarà una definizione di servizi che fisicamente potranno trovare i dati in applicazioni diverse (così come l'oggetto "cliente" di SME.up può trovare i suoi attributi leggendo nell'archivio delle ACG o altro).
Una seconda importante assunzione è che in una azienda potranno esistere anche diversi sistemi documentali. In tal caso DOOR.up è il portale di accesso unificato che legge ad esempio contemporaneamente da un server mail e dal PDM che cataloga i disegni prodotti dal CAD.

## I documenti in SME.up
In SME.up gestiamo già riferimenti ai documenti in vari modi. Ad esempio
-	Ogni oggetto punta ad un insieme di immagini
-	Nel modulo Q9000 si gestisce un DATABASE di documenti (non stato, distribuzione, livello di modifica) cui è possibile associare un file nel file system
-	Le note strutturate possono essere viste come un documento ( o ogni capitolo come un documento)
-	La documentazione attiva può essere vista come un insieme di documenti fra loro collegati
-	La documentazione di programma, o di campo di tabella ecc. è un documento

DOOR.up aggiunge un nuovo archivio di identificativi di documento specificamente pensato per contenere un record per ogni file (o cartella) che si vuole comprendere nell'organizzazione documentale. Tale identificativo è un oggetto e come tale gode di tutti i benefici di un oggetto SME.up e in particolare potrà avere un numero libero di attributi per caratterizzarlo e per l'individuazione dello stesso nelle ricerche.

Tali documenti potranno essere classificati per categorie (definite tabellarmente) e gli attributi saranno dipendenti dalla categoria. Sostanzialmente alla categoria viene associato un configuratore e ogni documento costituisce una configurazione
