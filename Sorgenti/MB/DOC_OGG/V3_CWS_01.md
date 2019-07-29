# Web Service per ascoltare un Biglietto da visita


# Introduzione
l'app Business Card Reader Pro (BCR) consente di estrarre i dati di un contatto leggendoli da un biglietto da visita.
L'app è in grado di riconosce le informazioni di contatto e di catalogarle :  riconosce, ad esempio, nome, cognome, il numero di fax, del cellulare o quello aziendale.

L'app BCR può memorizzare i biglietti da visita acquisiti come contatti del telefono e può anche esportarli verso SalesForce, Evernote o verso un Web Service configurabile.
LoocUp è in grado di interfacciarci a BCR e memorizzare i numeri sul server gestionale. Tramite LoocUp è poi possibile consultare i dati acquisiti e gestirli.

# l'app Business Card Reader Pro (BCR)
L'app è disponibile per le principali piattaforme mobile (iOs, Androis, BlackBerry, Windows Mobile).
Per i dettagli consultare il sito ai link seguenti : 

::DEC D(iPhone - iPad) I(http://www.shape.ag/en/products/details.php?product=bcr&platform=iphone)
::DEC D(Windows Mobile) I(http://www.shape.ag/en/products/details.php?product=bcr&platform=pocketpc)
::DEC D(Android) I(http://www.shape.ag/en/products/details.php?product=bcr&platform=android)
::DEC D(Blackberry) I(http://www.shape.ag/en/products/details.php?product=bcr&platform=bb)


## Come configurare BCR
 - Installare l'app BCR (disponibile nel market della propria piattaforma)
 - andare in Esportazione
 - cliccare sull'ingranaggio in alto a destra
 - nel campo sotto BCR API digitare l'url del plugin (per i dipendenti di SmeUp utilizzare http://gilberto.smeup.com/loocup/UploadBSC?username=NOME_UTENTE_AS400, rispettando maiuscole/minuscole )
 - opzionalmente attivare "Invia immagine del contatto" :  l'esportazione dell'immagine se non si è collegati in WIFI è piuttosto lenta
 - attivare "Esportazione automatica "
 - chiudere la configurazione

## Come utilizzare BCR

 - andare su "Scatta foto"
 - posizionare il biglietto da visita in una zona ben illuminata e scattare una foto.

Verranno mostrati i dati del contatto, con in grigio, le parti su cui l'OCR ritiene di aver una bassa affidabilità.
Si può intervenire correggendo gli errori oppure si può decidere di acquisire il biglietto un'altra volta.
In caso ci siano molti errori, si consiglia di posizionare il biglietto in una zona ben illuminata, oppure di provare ad attivare il flash dello smartphone (se disponibile). Di default BCR esegue l'acquisizione senza attivare il flash.
Per attivare il flash andare sulla schermata iniziale e cliccare sull'ingranaggio posto in basso a sx e selezionare la voce "Flash Mode", portando da auto a "sempre attivo"

Dopo di che il contatto verrà esportato automaticamente verso il server gestionale.
Nella sezione "Esportazione" potrò sapere se il biglietto è stato esportato ed eventualmente effetturare una nuova esportazione.

# Consultare i dati acquisiti con LoocUp
Le schede di consultazione dei biglietti sono agganciate all'istanza dell'oggetto V3 CWS 01.


# FAQ
D :  l'app BCR è disponibile solo per iPhone?
R :  No, è disponibile anche per Android, BlackBerry e Windows Mobile Touch : 
http://www.shape.ag/en/products/details.php?product=bcr&platform=pocketpc

D :  per memorizzare i blietti da visita su AS400 è necessario un Loocup Server?
R :  No, è sufficiente un LoocUp che sia configurato come service provider. Normalmente si configura un Loocup Server per farlo funzionare anche come Service Provider. In questpo modo si uniscono le funzionalità di esecuzione di funzioni batch con quelle di WebService.

# Cosa è stato realizzato
Sfruttando la possibilità di LoocUp di funzionare come service provider, è stato realizzato un webservice che riesce ad ascoltare le richieste (via http) di BCR.

## Infrastruttura tecnologica
 - App BCR installata su iPhone
 - Loocup Service Provider con installato il plugin
 - Plugin BSCard Reader

# Come configurare Loocup Service Provider
Per configurare un loocup service provider è sufficiente di disporre di una macchina che sia visibile da internet.
Va poi installato Loocup, versione di test (alla data del 10/02/2014 questo webservice non è stato ancora rilasciato in Stable)
Il webservice va configurato aggiungendo al membro UTENTE_SERVICE_PROVIDER del file SCP_CLO un tag C.CWS, sezione C.SEZ Cod="WebService"
Nella riga di comando aggiungere --http:NNNN, dove NNNN è la porta.



