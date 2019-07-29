
# Obiettivo

Estrarre i record da includere nella comunicazione liquidazione periodica iva.

# Prerequisito
E' importante che per il periodo selezionato, siano già stati stampati i registri iva
e relative liquidazioni mensili o trimestrali.

Prima di procedere è necessario controllare i dati anagrafici aziendali : 
* Ragione sociale
* Partita Iva
* Codice Fiscale
* Dati soggetto tenuto alla comunicazione (persona fisica che firmerà la comunicazione)
* Eventuali dati intermediario
* Parametro azienda compensazione iva (AA6) qualora ci sia una controllante
* Parametro aziende del gruppo (AAF) qualora ci sia la necessità di effettuare la liquidazione   del gruppo

Si suggerisce inoltre di verificare la configurazione del campo T$C57S (Imponibile passivo LIPE)
per definire la modalità di estrazione dell'imponibile delle operazioni passive. Per maggiori
dettagli si rimanada alla documentazione del campo della tabella C57.

# Parametri
 * Modalità di esecuzione : 
 ** Solo stampa :  verranno generate solo le stampe di controllo dei dati che verrebbero estratti
 ** 1 Stampa ed Esecuzione :  verranno prodotte le stampe di controllo e popolato l'archivio della comunicazione periodica iva.
 * Tipo Ripresa : 
 ** Scrivi solo mancanti :  non vengono apportate modifiche ai record già estratti ma vengono aggiunti eventuali nuovi record rilevati in contabilità
 ** V Scrivi tutti :  l'archivio viene cancellato e riscritto. Quindi, nel caso in cui si siano apportate modifiche sui record già estratti, queste verranno perse.
 * Anno :  viene riportato l'anno indicato nella prima videata
 * Trimestre :  viene riportato il trimestre indicato nella prima videata
 * Liquidazione del gruppo :  viene riportato qualora si voglia fare l'estrazione    della liquidazione iva del gruppo
 * Metodo Acconto :  qualora ci sia un acconto, indicare il metodo. Il metodo verrà comunque    valorizzato solo se ci sarà effettivamente un acconto, ed è possibile modificarlo    in manutenzione dati.
 * Dati Soggetto Tenuto alla Comunicazione
  ** Contatto :  tipo e codice contatto dell'anagrafica enti utilizzato per il soggetto  in questione
  ** Codice Carica :  codice carica del soggetto
 * Dati Soggetto Intermediario
  ** Contatto :  tipo e codice contatto dell'anagrafica enti utilizzato per il soggetto   in questione
  ** Data dell'impegno :  è la data in cui chi si occupa della trasmissione se ne è assunto l'impegno.
 * Esclusioni
  ** Assoggettamenti iva :  lista assoggettamenti iva da escludere dal calcolo dal totale delle   operazioni attive/passive del periodo selezionato

# Output
Verranno prodotte 2 stampe : 
 ** LIQ_CTR :  Dati estratti necessari alla comunicazione periodica iva selezionata.              Verrà stampato l'origine del dato.
 ** LIQ_QUA :  Controllo quadratura imponibili delle operazioni attive/passive del periodo selezionato

Al termine della funzione verrà prodotta una stampa che riporterà gli errori rilevati in fase di estrazione.

# PASSAGGI LIQUIDAZIONE IVA DI GRUPPO
Si ricorda che bisogna presentare le liquidazioni di ogni singola azienda, compresa la capogruppo, per poi comunicare la liquidazione dell'intero gruppo.
 * Compilare su tutte le aziende il parametro azienda compensazione iva (AA6), anche sulla    capogruppo
 * Compilare sull'azienda capogruppo il parametro (AAF) che indica tutti i codici azienda    appartenenti al gruppo (compresa la capogruppo)
 * Estrare i dati di ogni singola azienda, senza impostare il flag liquidazione gruppo (compresa    per la capogruppo)
 * Entrare nell'azienda capogruppo ed estrarre i dati impostando il flag liquidazione gruppo.    In questo passaggio verranno sommate tutte le voci delle aziende definite nel parametro    AAF ed estratte precedentemente.
