Se si verifica qualche malfunzionamento, è possibile controllare i log di SmePD salvati nel file lpd.log contenuto nella cartella di installazione del server (per problemi con SmePD) oppure i log dell'attività del servizio contenuti nel file wrapper.log nella sottocartella serviceNT\logs (es :  problemi di avvio del servizio o di comunicazione con AS400).

Qui di seguito alcune casistiche di problemi che si possono presentare

## Fase d'installazione
### Il servizio non s'installa
* Su alcuni sistemi Windows, pur operando con utente dichiarato amministratore, è necessario lanciare lo script di installazione del servizo tramite la vose **Esegui come amministratore** fra le voci visualizzabili con il tasto destro.
* Le credenziali dell'utente con cui si è configurato debba essere eseguito il servizio sono errate
## Fase di avvio
### Il servizio è installato ma non si avvia
* Innanzitutto fare riferimento la visualizzazione degli eventi di Windows. Quasis sempre c'è lo spunto per capire il perchè, eventualmente consultando un sistemista in grado di interpretare quanto scritto.
* Vedere quanto riportato nel fil di log del wrapper. Tale file di log è nel percorso relativo alla cartella d'installazione **servicent\logs**
## Fase di funzionamento
### il servizio si avvia ma non escono le stampe
* Verificare che gli spool su AS400 vengano correttamente spediti e che nei log di SmePD appaia la traccia della richiesta. Se ciò non accade : 
** Controllare che la configurazione del remote printer AS400 sia corretta, soprattuttop in riferimento all'indirizzo del server SmePD
** Controllare nel firewall di windows non stia bloccando l'applicazione o la porta TCP (515)
* Se gli spool vengono inviati ma le stampe non escono : 
** verificare se cambia il comportamento se il programma è attivo come servizio o in modalità di test (avviabile tramite serviceTest.bat)
** verificare che il servizio non sia attivo come utente LocalSystem (o Sistema Locale) perchè non è stata impostata correttamente l'assegnazione dell'utente di esecuzione al servizio
** verificare nei file di log che ci sia traccia della richiesta ed eventualmente vedere se la segnalazione è esplicativa del motivo ultimo
** verificare che il percorso dell'eseguibile del motore di stampa con cui verrà trattata il documento (Ghostprint o Acrobat) siano corretti
** verificare le autorizzazioni dell'utente di esecuzione del servizio, per accedere agli eseguibili di cui sopra, siano a posto
** verificare che il nome stampante sia come atteso dal motore di stampa di cui sopra
** verificare che lo spooler di sistama non abbia problemi
** verificare che la stampante non abbia problemi

Problema nella stampa dei font nel file pdf :  se i font nel file pdf vengono stampati in modo non corretto (ad esempio, si verificano problemi di allineamento dei singoli caratteri), significa che il font utilizzato per la generazione del pdf non è presente sul PC su cui è stato installato il servizio. Per risolvere il problema è necessario modificare i tag < font_setting > nel file di configurazione lpd_config.xml nella cartella di installazione del server : 
>                  < font_settings >
                                    < default_font > Courier New < /default_font >
                                    < font name="Courier New" >
                                                   < alias > Courier < /alias >
                                     < /font >
                   < /font_settings >

L'esempio mostra la configurazione del font "Courier New" come font utilizzato di default dal sistema con il file pdf, nel caso in cui il suo font interno non sia presente sul PC su cui è stato installato il servizio. E' inoltre possibile specificare font alternativi da usare al posto di altri all'interno del file pdf :  nell'esempio mostrato, il font "Courier" (specificato tramite il tag < alias > ) viene sostituito dal font "Courier New" specificato dall'attributo name del tag < font >.
E' inoltre possibile caricare font da cartelle esterne tramite il tag < external_font_dirs >, specificandone il percorso come nel seguente esempio (che carica i font di Windows) : 
>                                    < external_font_dirs >
                                                      < dir > c : /WINDOWS/Fonts/< /dir >
                                                      < dir >c : /WINNT/Fonts/< /dir >
                                    < /external_font_dirs >

