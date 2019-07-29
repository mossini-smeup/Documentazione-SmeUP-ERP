# Checklist prima dell'installazione di Web.UP

## Scelta del server

* Avete già un server windows su cui installare Sme.UP Provider?
* Avete già uno Sme.UP Provider? Se si, per cosa lo usate? Volete usare lo stesso o crearne uno nuovo?
* Avete già un payara ? Se si, per cosa lo usate? Volete usare lo stesso o crearne uno nuovo?
* Avete già un server windows su cui installare payara?
* Avete già un server linux su cui installare payara?
* Avete le licenze per poter installare un SO windows adeguato allo scopo?
* Avete i server in cloud e volete usare quelli?

## Scelta della modalità di accesso
* Volete che Web.UP / la app mobile sia raggiungibile dall'esterno o solo dall'interno?
* Volete che Web.UP / la app mobile sia raggiungibile tramite indirizzo ip o tramite nome dns?
* Con quale nome volete che gli utenti raggiungano Web.UP? Esempi :  web.cliente.it? www.cliente.it? web.cliente.it/AmbienteX? www.cliente.it/webup? www.cliente.it : 8080/WebUP? Altro?
* Avete un proxy in ingresso?
* Avete una vpn?
* Avete una dmz? Se si, volete che il server con payara e/o Sme.UP Provider sia in dmz?
* Volete che Web.UP sia raggiungibile via https o http? Se https, avete già un certificato?

## Scelta della modalità di avvio
* Web.UP deve essere raggiungibile 24*7?
* E' possibile ipotizzare un orario di riavvio con cadenza giornaliera o settimanale?
* Avete problemi di perdita connessioni?
* Avete un vpn?
* Avete schedulato lo spegnimento dell'IMBi?
* Avete schedulato la chiusura dei sottosistemi?
* Avete sistemi da integrare che si disattivano in dati momenti?

## Scelta della modalità di accesso
* Gli utenti che accederanno al sistema sono tutti codificati come utenti Looc.UP?
* Avete la necessità di usare una modalità di autenticazione differente da quella classica dell'utente IMBi?
* Avete la necessità di un accesso pubblico non autenticato?

## Grafica e Integrazione
* Dovete integrare Web.UP con qualcosa di esterno?
* Avete esigenze grafiche particolari o potete usare la nostra grafica standard?
* Avete la necessità di utilizzare sia la versione web che la versione mobile?
* Avete la necessità di usare il web per cruscotti di produzione / bordo macchina?
* Avete la necessità di usare il mobile per i dispositivi mobili di produzione/magazzino/raccolta dati?
