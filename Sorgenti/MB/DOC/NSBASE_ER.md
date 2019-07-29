# Errori Frequenti
## Sottosistema con numero job attivi diverso da *NOMAX
**Sintomi** : 
Errore segnalato nel joblog : 
Rilevato errore nella sessione QSH, codice di errore 4, numero di errore 3489.
Causa : 
Il sottosistema in cui sta girando il B£G53G ha un numero massimo di lavori attivi diverso da *NOMAX.
E' possibile controllare questa caratteristica con il comando DSPSBSD SBSD(nomesottosistema) - opzione 1
**Correzione** : 
Cambiare il numero massimo di lavori attivi nel sottosistema o eseguire il comando in un altro sottosistema
# Performance scadenti
## Errata configurazione delle informazioni di dominio
Le chiamate della G53 che utilizzano richiami alla strqsh (FTP-AS_HOST, FTP-HOST_AS, EXEC-PGM,
MAILTO, MAILTO-AS400, OPEN-FILE, PDF, SPLPDF-GEN, SPLPDF-G&M,MAILTO e G&M_AS4) possono risultare
lente nel caso in cui la configurazione delle informazioni di dominio (CHGTCPDMN, oppure CFGTCP,
opz. 12 non sia a posto.
Tale configurazione è relativa alle funzioni di risoluzione DNS dell'OS400.
Se le informazioni riportate non sono corrette ogni chiamata alla strqsh con relativa chiamata java
spreca fino a 30 secondi in attesa di un timeout di sistema, dopo di che svolge il proprio lavoro.
Sistemando le configurazioni precedentemente indicate il tempo di tale timeout si riduce a 0.

Le informazioni che vanno inserite, agendo come SECOFR, sono indicativamente le seguenti : 
HOSTNAME ----> Nome AS400
DMNNAME ----> Dominio di rete
DMNSCHLIST ----> *DFT
HOSTSCHLIST ----> *LOCAL
INTNETADR ----> Indirizzo IP DNS di rete

L'inserimento di indirizzi DNS particolarmente lenti peggiora sensibilmente le performance delle
chiamate citate.
Si consiglia di verificare (mediante comando PING) l'effettivo tempo di risposta dei DNS inseriti.

