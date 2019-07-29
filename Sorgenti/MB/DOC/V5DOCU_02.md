# Obiettivo
Fornire una base di importazione, per qualsiasi documento di ciclo attivo o passivo, attraverso una funzione comune.
Questa applicazione passa attraverso i vari visualizzatori utente, è quindi a carico dello sviluppatore non utilizzare funzioni con apertura formati video.

# Quando utilizzarla
La funzione è da utilizzare solo per importazioni batch di documenti.

# Funzionamento
Il funzionamento è simile al Mail.UP, vengono generati record contestuali per : 

- DO Testata documento
- DR Righe   documento
- C£ Parametri, sia di testata che di riga
- NT Note strutturate, sia di testata che di riga
- HD Header di testata
- HR Header di riga

Ogni documento deve appartenere interamente ad un lotto, se presenti più documenti all'interno dello stesso lotto dovrà essere assegnato un sottolotto.
Tutti i record dipendenti (note, parametri, righe) dovranno fare riferimento al documento a cui si devono legare.
L'applicazione del lotto genererà i documenti richiesti.

## V5B
L'api V5B è lo strumento con cui lo sviluppatore deve interagire con l'acquisizione batch dei documenti. Vediamo in dettaglio il suo funzionamento.
L'api può essere utilizzata con due modalità : 
- Con Header
- Senza Header
L'header, estende le funzionalità dell'api, permettendo : 
- controllo di integrità del lotto
- possibilità di costruire il documento con modalità di derivazione
- Disabilita la possibilità di avere più documenti nello stesso lotto

### Funzioni e Metodi senza Header

| Funzione | Metodo | Parametri |Descrizione |
| ---|----|----|----|
| INZ | LOT | No | Creazione di un nuovo lotto (Inizio di un nuovo documento) |
| INZ | SLT | Lotto | Crea un nuovo sottolotto (inizio di un nuovo documento, ma all'interno dello stesso lotto) |
| WRI | | Lotto, Sottolotto, Tipo tracciato, immagine | Scrive il tracciato del record richiesto |
| APP | LOT | Lotto | Se il lotto è valido, allora verrà applicato e generati i documenti |
| 


### Funzioni e Metodi con Header

| Funzione | Metodo | Parametri |Descrizione |
| ---|----|----|----|
| INZ |HED | Immagine Header | Creazione di un nuovo lotto (Inizio di un nuovo documento) |
| WRI | | Lotto, Tipo tracciato, immagine | Scrive il tracciato del record richiesto |
| CLO |HED | Lotto | Chiusula del lotto (Senza questa dichiarazione il lotto viene considerato non integro) |
| APP | LOT | Lotto | Se il lotto è valido, allora verrà applicato e generati i documenti |
| 


### Immagine dell'Header

|   Campo   | Descrizione |
| ---|----|
|   £V5BHL  | Nome della DS |
|   £V5BHTD | Tipo documento da generare (se non impostato lo assume dall'immagine passata) |
|   £V5BHMD | Modello documento da generare (se non impostato lo assume dall'immagine passata) |
|   £V5BHND | Numero documento da generare (se non impostato lo assume dall'immagine passata) |
|   £V5BHTR | Tipo riga da generare (se non impostato lo assume dall'immagine passata) |
|   £V5BHTO | Tipo Documento Origine da derivare |
|   £V5BHNO |  Numero Documento Origine da derivare |
|   £V5BHRO | Riga Documento Origine da derivare |
|   £V5BHEI | Ente Intestatario da generare (se non impostato lo assume dall'immagine passata) |
|   £V5BHPE | Uso Utente |
|   £V5BHET | Non evidenziare l'errore sul numero Documento di testata in verifica lotto |
| 


### Parametri di comunicazione

|   Campo DS  | Descrizione |
| ---|----|
|   £V5BTR   | E' l'oggetto che identifica il tracciato. |
|   £V5BOM   | Permette di legare le dipendenze al documento |
|   £V5BOG   | Ad ogni stittura viene ritornato questo campo che contiene l'identificativo univoco del record |
|   £V5BLO   | Viene ritornato a seguito della funzione INZ.LOT o INZ.HED |
|   £V5BID   |  Se impostato a 1, utilizzerà il documento passato nell'Header per attivare la funzione di derivazione. |
|   £V5BIF   | Se impostato a 1, i campi del tracciato non verranno recuperati nel nuovo documento :  |
|   £V5BSS   | è il sottosettore della numerazione del lotto, in assenza assume V5 |
|   £V5BDF   | Se impostato a 1, non eseguirà i flussi oggetto |
|   £V5BIM   | è l'immagine del record in scrittura |
| 


## Esempio con funzione HEADER
> * Preparo il LOTTO
C                   CLEAR                   £V5BHL
C                   EVAL      £V5BFU='INZ'
C                   EVAL      £V5BME='HED'
C                   EVAL      £V5BIM=£V5BHL
C                   EXSR      £V5B
 * Documento
C                   EVAL      £V5BFU='WRI'
C                   EVAL      £V5BME=''
C                   EVAL      £V5BTR='DO'
* Imposto i campi con cui voglio creare il documento, per esempio
C                   EVAL      T§TDOC='OA'
C                   EVAL      T§TMOD='001'
C                   EVAL      T§CDCL='000001
* Ecc... ecc...
C                   EVAL      £V5BIM=V5TDOC
C                   EXSR      £V5B
C                   EVAL      £V5BOM=£V5BOG
C                   EVAL      $V5BOM=£V5BOG
 * ..riga
C                   EVAL      £V5BFU='WRI'
C                   EVAL      £V5BME=''
C                   EVAL      £V5BTR='DR'
* Imposto i campi con cui voglio creare il documento, per esempio
C                   EVAL      R§TDOC='OA'
C                   EVAL      R§TRIG='AR'
C                   EVAL      R§CDOG='ART000001
* Ecc... ecc...
C                   EVAL      £V5BIM=V5RDOC
C                   EXSR      £V5B
* header di riga (solo se necessario)
C                   EVAL      £V5BFU='WRI'
C                   EVAL      £V5BME=''
C                   EVAL      £V5BTR='HR'
C                   EVAL      £V5BIM=£V5BHL
C                   EVAL      £V5BOM=£V5BOG
C                   EXSR      £V5B
C                   EVAL      £V5BOM=$V5BOM
* Note o prametri (Se necessario)
C                   EVAL      £V5BFU='WRI'
C                   EVAL      £V5BME=''
C                   EVAL      £V5BTR='C£'
C                   EVAL      £V5BIM=C£CONR
C                   EXSR      £V5B
* Chiusura dell'Header
C                   EVAL      £V5BFU='CLO'
C                   EVAL      £V5BME='HED'
C                   EXSR      £V5B
* Applico il lotto (creazione dei documenti)
C                   EVAL      £V5BFU='APP'
C                   EVAL      £V5BME='LOT'
C                   EXSR      £V5B


## Esempio senza funzione HEADER (multidocumento)
> * Preparo il LOTTO
C                   CLEAR                   £V5BHL
C                   EVAL      £V5BFU='INZ'
C                   EVAL      £V5BME='LOT'
C                   EVAL      £V5BIM=£V5BHL
C                   EXSR      £V5B
 * Documento
C                   EVAL      £V5BFU='WRI'
C                   EVAL      £V5BME=''
C                   EVAL      £V5BTR='DO'
* Imposto i campi con cui voglio creare il documento, per esempio
C                   EVAL      T§TDOC='OA'
C                   EVAL      T§TMOD='001'
C                   EVAL      T§CDCL='000001
* Ecc... ecc...
C                   EVAL      £V5BIM=V5TDOC
C                   EXSR      £V5B
C                   EVAL      £V5BOM=£V5BOG
 * ..riga
C                   EVAL      £V5BFU='WRI'
C                   EVAL      £V5BME=''
C                   EVAL      £V5BTR='DR'
* Imposto i campi con cui voglio creare il documento, per esempio
C                   EVAL      R§TDOC='OA'
C                   EVAL      R§TRIG='AR'
C                   EVAL      R§CDOG='ART000001
* Ecc... ecc...
C                   EVAL      £V5BIM=V5RDOC
C                   EXSR      £V5B
* Note o prametri (Se necessario)
C                   EVAL      £V5BFU='WRI'
C                   EVAL      £V5BME=''
C                   EVAL      £V5BTR='C£'
C                   EVAL      £V5BIM=C£CONR
C                   EXSR      £V5B
 * Preparo il SOTTOLOTTO per includere nello stesso lotto un'altro documento
C                   CLEAR                   £V5BHL
C                   EVAL      £V5BFU='INZ'
C                   EVAL      £V5BME='SLT'
C                   EVAL      £V5BIM=£V5BHL
C                   EXSR      £V5B
 * Documento
C                   EVAL      £V5BFU='WRI'
C                   EVAL      £V5BME=''
C                   EVAL      £V5BTR='DO'
* Imposto i campi con cui voglio creare il documento, per esempio
C                   EVAL      T§TDOC='OA'
C                   EVAL      T§TMOD='001'
C                   EVAL      T§CDCL='000001
* Ecc... ecc...
C                   EVAL      £V5BIM=V5TDOC
C                   EXSR      £V5B
C                   EVAL      £V5BOM=£V5BOG
 * ..riga
C                   EVAL      £V5BFU='WRI'
C                   EVAL      £V5BME=''
C                   EVAL      £V5BTR='DR'
* Imposto i campi con cui voglio creare il documento, per esempio
C                   EVAL      R§TDOC='OA'
C                   EVAL      R§TRIG='AR'
C                   EVAL      R§CDOG='ART000001
* Ecc... ecc...
C                   EVAL      £V5BIM=V5RDOC
C                   EXSR      £V5B
* Note o prametri (Se necessario)
C                   EVAL      £V5BFU='WRI'
C                   EVAL      £V5BME=''
C                   EVAL      £V5BTR='C£'
C                   EVAL      £V5BIM=C£CONR
C                   EXSR      £V5B
* Applico il lotto (creazione dei documenti)
C                   EVAL      £V5BFU='APP'
C                   EVAL      £V5BME='LOT'
C                   EXSR      £V5B


# Lotti non applicati
In caso di anomalia nell'applicazione, i documenti non saranno creati, ne verrà data evidenzia tramite il gestore delle anomalie V5BCH10 dal quale sarà possibile rieseguire l'applicazione o annullare i singoli tracciati, non è possibile modificare i tracciati già scritti.
