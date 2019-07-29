# OBIETTIVI

Fornire una serie di funzionalità per la presentazione ed esecuzione di azioni associate a oggetti di Sme.up.

Alla COPY £G99 è associato un deviatore funizzato, B£G99D, per agevolare le chiamate (ad esempio chiamata a modifica oggetto da schiera azioni G18).



# FUNZIONI E METODI

## LIS
Lista le azioni eseguibili in questo momento su un oggetto di Sme.up.
Esempi : 
 * Azioni di gestione (modifica, cancellazione...).
 * Azioni da B£H.
 * Navigazioni per oggetto.
 * ...e così via.
Si ricorda che la lista di azioni viene caricata dal servizio JATRE_06C sulla base dello script al suo interno oppure delle ridefinizioni per oggetto.

## ESE
Esegue direttamente (senza passare per la scelta dalla lista) particolari tipi di azioni, nell'ipotesi che siano eseguibili da un particolare utente in un determinato momento (altrimenti non fa nulla) : 
 * Azioni di gestione (01, 02, ...).

## CTR
Restituisce se per un particolare tipo/parametro di oggetto le azioni sono gestite : 
 * Alla vecchia maniera.
 * Secondo le nuove modalità (£G99MS='NEW').
Questa chiamata serve ai programmi di lista (es. BRAR01L) per decidere cosa eseguire e cosa presentare dalla casella opzioni associata alle righe di lista.

## SCA
Permette di scandire le funzioni del popup. Le funzioni vengono tornate nel campo £G99DO, che
va rimappato con la DS £G99FO.

