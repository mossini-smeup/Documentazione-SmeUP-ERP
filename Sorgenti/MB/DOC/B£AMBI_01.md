# B£AMBI Gestione ambienti SmeUP
L'obiettivo è di stabilire le modalità di accesso e di presentazione di un utente ai vari ambienti che ha a disposizione. Con modalità di accesso e presentazione si intende : 
* quali dati(librerie dati)
* con quali programmi (relase / aggiornamento / personalizzazioni)
* lingua utilizzata
* modalità di codifica dei dati negli archivi (encoding)

## Processo
Per arrivare definizione degli accessi per un utente sono suggeriti i seguenti passi : 
* Costruzione degli ambienti applicativi
* Definizione dei gruppi di accesso
* Associazione degli ambienti ai gruppi di accesso, definendo anche le modalità di accesso
* Attribuzione di un utente al gruppo di accesso - facendogli quidi ereditare tutti gli accessi del gruppo
Piuttosto che gestire gli accessi per ogni singolo utente è consigliabile definire dei gruppi di accesso a cui assegnare le possibili modalità di accesso e attribuire ad ogni utente il prorpio gruppo di accesso.

## Programma di gestione (B£UT55)
Tutte le funzioni a cui si fa riferimento qui sopra sono disponibili nel programma di gestione B£UT55
 :  : INI Gestione Ambenti
 :  : CMD CALL B£UT55
 :  : FIN

### Funzioni aggiuntive
Nel programma di gestione B£UT55 si possono anche eseguire funzioni aggiuntive : 
* Impostazione del gruppo di accesso di default
* Definizione delle librerie di sistema
* Definizione del gruppo azioni collegate al tasto Escape (Esc)
* Definizione delle librerie di sistema
* Definizione delle impostazioni di encoding
* Gestione della teblla A£B di impostazione localizzazioni


