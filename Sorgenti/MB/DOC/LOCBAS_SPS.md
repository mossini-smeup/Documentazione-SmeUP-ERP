# Prerequsiti e configurazione SSO in SmeupProvider

Questa modalità di autenticazione avviene in modo diverso da quella utilizzata da LoocUp.
Nasce per consentire di accedere all'iSeries da web (Webup o App).
A differenza di Loocup, in questa modalità l'utente deve fornire le proprie credenziali di accesso al dominio.

## Prerequisiti
 * prerequisiti necessari al funzionamento di WebUp.
 * AS400 e l'AD configurati per il funzionamento in SSO. Far riferimento alla documentazione del modulo LOSSON (*).
 * Il provider deve poter raggiungere l'AD.


## Installazione
Procedere ad una normale installazione di WebUp, ponendo attenzione ai prerequisiti.
Si consiglia di installare l'application server su una macchina in DMZ e posizionare il provider nella lan.
Questa configurazione è quella che garantisce la massima sicurezza in quanto : 
 * l'unica porta aperta tra dmz e lan è la porta di comunicazione tra application server e provider
 * tutte le porte necessarie all'autenticazione sull'AD e di comunicazione con l'AS sono accessibili solo all'interno della lan

## Configurazione
 * Configurare il file krb5.conf del provider
 * creare un modulo di login di tipo SSO

NOTE
(*) In questa configurazione dell'SSO non è necessario intervenire sui client.
