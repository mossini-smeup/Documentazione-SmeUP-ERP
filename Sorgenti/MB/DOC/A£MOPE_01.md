## Funzioni per il testing di performance interne a Sme.UP

Per il controllo delle performance in fase di collaudo dal cliente è possibile lanciare alcune funzioni interne all'applicazione quali ad esempio le schede per la valutazione delle performance di comunicazione dell'as400 o del provider, le schede per le performance delle dec, la funzione di monitoraggio comparata di web.UP, provider, as400, etc...

Per dettagli si consiglia di visualizzare il capitolo Test Performance del modulo A£MOPE.


## Introduzione ai test di performance

Per un'introduzione ai test di performance si consiglia di leggere il seguente articolo del blog Sme.UP
https://www.smeup.com/blog/blog-software-gestionali-erp/test-di-performance-in-sme-up-erp

## Introduzione agli application performance manager

Gli APM (application performance manager o anche monitor) sono dei tool che monitorano un'applicazione e le sue dipendenze. Sul mercato esistono una miriade di prodotti di tal genere per diverse tecnologie e per tutti i gusti. Ci sono APM a pagamento e altri open source. Alcuni richiedono numerose modifiche al codice e configurazioni complesse e altri invece sono più facili da installare e poco intrusivi.

Essi possono operare a diversi livelli, tra cui ad esempio :  controllo delle transazioni e delle richieste individuali, controllo dell'uso e delle performance delle dipendenze (ad esempio dei database o dei web services utilizzati dall'applicazione), controllo delle metriche del o dei server che ospitano l'applicazione (cpu della macchine, memoria), controllo delle metriche dei runtime applicativi (per java ad esempio controllo della jvm), profilazione del codice.

In Sme.UP stiamo attualmente valutando l'apm glowroot per monitorare le istanze di test di performance di Web.UP e del Provider del laboratorio. Glowroot è open source, facile da installare, non servono modifiche al codice e ha un basso overhead dichiarato (rallentamento delle performance dovuto all'aggiunta del software di monitoraggio). Siccome non monitora il server ospitante è stato aggiunto uno stack tig (ovvero telegraf + influxdb + grafana).

## I test di carico di Web.UP

L'infrastruttura attualmente presente per i test di carico di Web.UP svolti in laboratorio è così composta : 
- una macchina dedicata che lancia più istanze di browser contemporanee
- una macchina dedicata su cui è ospitato un Web.UP di test performance
- una macchina dedicata su cui è ospitato un provider di test di performance
Viene testata ogni giorno ad una data ora l'ultima versione di sviluppo di Web.UP lanciando una suite di test di carico. In caso di valori di performance non corrispondenti a quelli attesi la build assume un colore rosso e vengono inviate mail di alert.

Per lanciare test di carico simulando più utenti contemporanei è stato utilizzato il software jmeter. Grazie a jmeter è infatti possibile runnare uno o più script diversi su n utenti contemporanei per quanto desiderato.
Gli script lanciati sono stati scritti utilizzando selenium webdriver, il quale permette di automatizzare i click fatti su un browser, creando dei percorsi automatici utente, ad esempio dei percorsi di login, apertura di schede e logout. E' possibile creare i percorsi automatici che si desiderano.

Il browser utilizzato dai test è chrome headless, ovvero la versione di chrome senza interfaccia grafica.

I risultati di jmeter vengono inviati su influxdb in maniera tale da poterli visualizzarli real time con grafana.

Le istanze di Web.UP e del provider testate sono monitorate attraverso l'apm glowroot, installato su ciascuna di esse.

Grazie a glowroot è possibile analizzare i tempi delle request, indagare le request più lente, osservare i valori della JVM, osservare i tempi dei metodi di interesse, anche facenti parte del proprio codice, attraverso la profilazione.

Ad ogni build di test di carico sono associati automaticamente i report di statistiche di jmeter su grafana, di glowroot per Web.UP e per il Provider e dello stack tig per il monitoring della macchina che hosta Web.UP (memoria, disco usato...).



