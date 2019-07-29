# Generalità
In un generico programma applicativo si ricorre frequentemente all'utilizzo di tabelle, come per le causali di contabilità, di pagamento, per i codici iva, e cosi via.
Dal punto di vista di : 

- > Utente --> comporta una frequente consultazione di tabulati durante le normali operazionidi data entry o la necessità di memorizzare un numero più o meno elevato di codici.

- >Programmatore --> è necessario scrivere, per ogni singola tabella impiegata, il relativo programma di manutenzione.
Per questo il programmatore ricorre frequentemente alla tecnica di includere direttamente le tabelle nel codice del programma applicativo, riducendo al minimo il lavoro di codifica ed evitando che l'utente possa modificare e aggiornare i dati nelle tabelle.

Le tabelle di Sme.up consentono di conciliare le opposte esigenze dell'utente, che necessita di un applicativo flessibile e facilmente configurabile, e del programmatore, che riduce al minimo i tempi di sviluppo dell'applicazione.

# Scopo
Come si può desumere, l'obiettivo è diverso a seconda del tipo di operatore : 

- Per l'Utente
-- Disporre di un'interfaccia comune in tutte le operazioni di data entry che richiedano di indicare un elemento di una tabella. Tale interfaccia consente l'apertura a video di finestre di ricerca con ordinamento per codice o per ordine alfabetico, eliminando completamente la necessità di consultazione di tabulati
-- Avere la possibilità di aggiornare e modificare le tabelle senza alcun vincolo e senza che questo comporti l'intervento del programmatore
-- Essere in grado di intervenire sulle tabelle (per esempio aggiungendo un nuovo elemento) direttamente dalla procedura di data entry che si sta utilizzando.

- Per il Programmatore
-- Eliminazione di tutto il lavoro di codifica delle procedure di manutenzione delle tabelle
-- Massima semplicità di integrazione delle tabelle nelle applicazioni con un minimo sforzo di programmazione
-- Completa libertà di modificare la struttura di una tabella (aggiunta o modifica di campi) senza dover modificare i programmi in cui era stata precedentemente utilizzata.

- Per il Responsabile EDP
-- Una completa gestione della sicurezza delle informazioni, attraverso esplicita autorizzazione o inibizione degli utenti alle funzioni di aggiornamento delle singole tabelle e registrazione degli autori delle modifiche.

