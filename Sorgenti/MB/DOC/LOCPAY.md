# Componente PAY

## Introduzione

Il componente PAY permette di utilizzare paypal come sistema di pagamento.
Il componente è funzionante solo in WebUP
Nello showcase di webup c'è un esempio di utilizzo di questo componente, Abbiamo previsto la possibilità di utilizzare
anche la versione di test del servizio di pagamento.

Oltre ai parametri di configurazione impostabili tramite setup come si può vedere nello script di esempio dello showcase
si deve compilare il file "paypal.properties"  che in una installazione standard si trova in <User-Home>/etc/webup/WebUP/resources/paypal/.

Questo file definisce la fun da richiamare per la conferma asincrona dell'avvenuto pagamento

Ad esempio : 

ipn_fun = F(EXB;X1SER_B04;IPNPAY) INPUT({0})

La stringa "{0}" verrà sostituita da webup con una del tipo : 
param_name1(value1) param_name2(value2)... param_nameN(valueN)
dove i parametri e i valori dipendono dai dati che si stanno scambiando con paypal. Nello stesso file si definisce inoltre l'indirizzo usato da webup per verificare la correttezza del messaggio di conferma.

Ad esempio : 
ipn_url = https://www.sandbox.paypal.com/cgi-bin/webscr

Infine definiamo l'endpoint a cui paypal invia i messaggi di conferma dei pagamenti : 

Ad esempio : 
ipn_listener = http://www.sito-smeup.com/WebUP/services/paypal/listener

Si rimanda al sito di paypal per la registrazione dell'account dell'esercente e per la documentazione sul funzionamento del sistema di pagamento tramite IPN. Si note inoltre che l'utente
con cui viene chiamata la fun di conferma è quello definito in "connection.properties".

## Funzionalità ed attributi
Le funzionalità, le impostazioni e gli attributi del componente sono consultabili attraverso il configuratore e la sua documentazione.

 :  : DEC K(Clicca qui.) D(Apri il configuratore per vedere tutte le possibilità.) X(F(INT;JA_00_01;GES.EDT) 1(RE;L-;EDT_SCH) 2(**;;&AM.LL) 3(OJ;*USRPRF;&AM.UT) 4(**;;DOCSETUP) P(SECLS(G.SET.PAY))) L(1)

## Schede di esempio
Gli esempi del componente PAY sono consultabili qui : 

 :  : DEC K(Esempi) D(Sezione specifica per il web) X(F(EXD;*SCO;) 1(V2;JAGRA;PAY) 2(MB;SCP_SCH;WETEST_PAY)) L(1)

