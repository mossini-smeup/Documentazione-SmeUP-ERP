# Obiettivo
Creare un link Web.UP per il richiamo di una funzione predefinita, genera URL che possono essere inseriti automaticamente in email, in documenti, come pubblicati in qualsiasi sito web.

## Link interno/esterno
La funzione LNK per la creazione di un link può essere eseguita col metodo INT o EXT.
INT crea un link interno, che prevede l'autenticazione, invece il metodo EXT crea un link esterno che contiene un hash che sostituisce l'autenticazione.

Le variabili previste in input per la creazione del link Web.UP sono : 

|  Nam="Variabili" |
| 
| .COL Txt="Nome" |
| ---|----|
| 
| .COL Txt="Descrizione" |
| 
| .COL Txt="Obbligatorio" |
| url(...)|indirizzo web di collegamento|Si |
| mod(...)|modulo di login|Solo per metodo INT |
| p(...)|parametro specifico per l'autenticazione, per esempio l'email|Solo per metodo INT |
| sfunction(...)|funzione di avvio (funzione brevedefinita in SCP_CLO)| |
| fun(...)|funzione di avvio (FUN completa)| |
| var(...)|variabili da passare alla funzione di avvio |
| callBack(...)|url da chiamare al ritorno dell'applicazione |
| secret(...)|segreto condiviso per il calcolo dell'hash|Solo per metodo INT |
| Con timestamp(...)|indica se si vuole un link con timestamp |
| Senza hash(...)|indica se si vuole un link senza hask |
|  |
| 


Per ulteriori dettagli sul significato delle variabili si rimanda alla documentazione specifica di Web.UP : 
- [Moduli Login](Sorgenti/MB/DOC/WEBASE_011)

## Variabili da SCP_CLO

Per il caricamento automatico delle variabili url e mod sono state previste le variabili standard da SCP_CLO *WEBUP.URL e *WEBUP.MOD, in modo da poterne centralizzare la gestione ed eventualmente gestirne di diverse per i singoli ambienti applicativi.

## Nota
Per la creazione del link viene utilizzato il timestamp con data e ora UTC, in formato yyyyMMddhhmmss, pertanto per eventuali test è stata prevista in input la variabile t(...)
che può essere passata per sostutirla al timestamp attuale nella creazione del link, al solo fine di verificare che un link creato in precedenza avesse l'hash corretto.

## Esempi

Funzione LNK metodo INT

Input : 
url(http://mobile.smeup.com/AreaRiservata) mod(areaRiservata) sfunction(AR_FAT) callBack(http://areariservata.smeup.com/area-personale.html) p(info@smeup.com) var(P(V1 .16.10)K(160005182))
Output : 
http://mobile.smeup.com/AreaRiservata/views/webuplogin.jsf?mod=areaRiservata&p=info@smeup.com&sfunc[160005182](160005182)

Funzione LNK metodo EXT

Input : 
url(http://mobile.smeup.com/AreaRiservata) mod(areaRiservata) sfunction(AR_FAT) callBack(http://areariservata.smeup.com/area-personale.html) secret(PluToqw1231dxm12j9st98u3) p(info@smeup.com) var(P(V1 .16.10)K(160005182)) t(20160810130603)
Output : 
http://mobile.smeup.com/AreaRiservata/views/webupExtLogin.jsf?mod=areaRiservata&p=info@smeup.com&sfunction=AR_FAT&t=20160810130603&hash=4b6039b220fe2ca3910931132687ad107b1e7a12&callBack=http://areariservata.smeup.com/area-personale.html&var=P(V1 .16.10)K(160005182)
