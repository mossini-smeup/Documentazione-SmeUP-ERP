# Configurazione Invio Fatture

## Prerequisiti
Il corretto funzionamento delle funzionalità di invio delle fatture elettroniche presuppone la disponibilità di uno Smart Kit.
Lo stato e la bontà della configurazione della connessione può sempre essere monitorato all'interno della scheda _Cruscotto invio fatture_  all'interno del tab _Controlli di sistema

## Configurazione
Per poter inviare fatture al SdI utilizzando Abletech come intermediario è necessario compilare l'estensione **£56** dell'azienda con i seguenti dati che devono essere forniti da Abletech : 
* Utente
* Password
* Aooid (una stringa alfanumerica di 36 caratteri che identifica l'azienda).

Il codice Aooid, se non fornito all'atto della registrazione da parte di Able Tech, può essere compilato automaticamente selezionando il pulsante 'Richiedi Aooid' posto nella scheda _Cruscotto invio fatture_  all'interno del tab _Controlli di sistema_

Il **provider** utilizzato per l'invio può essere indicato nella tabella V50.
Nel caso non venga indicato in V50 avviene una risalita sulla tabella LOB, prima sull'elemento K11 e poi su **.

I webservice utilizzati per l'autenticazione e l'invio vengono indicati rispettivamente negli elementi **£AB02** (per l'autenticazione) e **£AB01** (per l'invio) della tabella **EDC** .
Per la richiesta di Aooid tramite webservice è stato creato l'elemento **£AB03**.
La PTF V580508A imposta gli SE.SUB.A38 che puntano ai webservice di produzione
* **61.S00.B00** per l'elemento **£AB02** (autenticazione)
* **61.S01.B00** per l'elemento **£AB01** (invio)
* **61.S02.B00** per l'elemento **£AB03** (Richiesta Aooid)

### Configurazione ambiente di test
Per effettuare il test della correttezza dell'invio si rimanda alla documentazione del Criterio di completamento.
Il lancio di questa funzione, infatti, garantisce la corretta installazione di programmi e Smart Kit

### Impostazione ambiente di avvio Smart Kit
L'ambiente sul quale si avvia lo Smart Kit deve essere associato con UP UT5 all'utente di collegamento.
L'ambiente sul quale si avvia lo Smart Kit deve avere in linea gli script SCP_CFG/EDT_SET e SCP_SET/LOA38_61.
Se si mantiene l'impostazione standard dello script LOA38_61 con la coda dello Smart Kit specificata con riferimento alla tabella V50 ( :  : A38.SUPPRV DtaQ="_&_KI.TAV50.*%I/T$V50B" Active="1")  è necessario che l'impostazione della coda nella tabella V50 dell'ambiente di avvio del provider sia uguale a quella dell'ambiente da cui si esegue l'invio delle fatture. Se invece venisse cablata la coda dati nello script assicurarsi che la coda dati impostata in V50 corrisponda a quella specificata nello script.

### Impostazione di un solo Smart Kit per più sistemi informativi
L'ambiente sul quale si avvia lo Smart Kit deve essere associato con UP UT5 all'utente di collegamento.
L'ambiente sul quale si avvia lo Smart Kit deve avere in linea gli script SCP_CFG/EDT_SET e SCP_SET/LOA38_61.
Se si mantiene l'impostazione standard dello script LOA38_61 con la coda dello Smart Kit specificata con riferimento alla tabella V50 è necessario che l'impostazione della coda nella tabella V50 dell'ambiente di avvio dello smart kit sia uguale a quella di tutti gli ambienti da cusi esegue l'invio delle fatture. Se invece venisse cablata la coda dati nello script assicurarsi che la coda dati impostata in V50 in tutti gli ambienti corrisponda a quella specificata nello script.
Ovviamente è anche possibile impostare un diverso Smart Kit per ciascun sistema informativo.

### Configurazione dello Smart Kit
La configurazione dello Smart viene eseguita dai sistemisti dell'infrastruttura.
Per riferimenti : 
http://blog.smeup.com/smartkit-fe/
