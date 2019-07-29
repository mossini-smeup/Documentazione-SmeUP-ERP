# Righe Richieste Movimentazione
Nelle righe richieste di movimentazione sono gestite le quantità di articoli da movimentare,
le date richieste e le informazioni di origine e destinazione.

Alle righe delle richieste di movimentazione vengono abbinate, sia per la parte di origine che
per la parte di destinazione, le relative causali e chiavi di giacenza, cosicché quando la
richiesta viene applicata, automaticamente vengono lanciati i due movimenti di scarico e carico.

Nella normalità, in fase di creazione i campi chiave dell'origine e della destinazione non sono
completamente compilati, altri programmi di elaborazione successiva si occupano del trattamento delle righe,
compreso il completamento dei dati origine e destinazione.

Se la riga di una richiesta di movimentazione proviene da un documento gestionale (ordine produzione o
documento ciclo attivo/passivo) nella riga vengono riportati i riferimenti al documento origine.

Per l'esecuzione di particolari attività (es. attribuzione ubicazione e versamento a magazzino) sono
previste richieste di movimentazione di sole righe.
La ragione è essenzialmente pratica, in questi casi esistono richieste di movimentazione create
temporaneamente (per permettere l'esecuzione dell'attività, dopo vengono cancellate automaticamente)
e con una sola riga, è inutile quindi creare contestualmente anche la testata.
