# Obiettivi
Questa funzione permette di determinare gli importi da liquidare agli agenti in base al tipo liquidazione previsto per ognuno.

Le tipologie di liquidazione sono : 
 * _2_sul fatturato, all'agente vengono corrisposte le provvigioni in base alle fatture procurate nel periodo preso in esame;
 * _2_sull'incassato (pagato), all'agente vengono corrisposte le provvigioni in base ai pagamenti effettuati nel periodo in esame su fatture da lui precedentemente procurate;
 * _2_sul saldato, all'agente vengono corrisposte le provvigioni in base a fatture da lui precedentementeprocurate e saldate nel periodo preso in esame.

Per determinare gli importi delle ultime due tipologie vengono analizzati i movimenti contabili relativi alle singole fatture procurate dall'agente.

# Formato di lancio

* **Periodicità Liquidazione** :  attraverso questo campo viene identificata la periodicità delle provvigioni da elaborare. E' possibile elaborare solo una periodicità per volta.
* **Codice Intestatario** :  attraverso questo campo è possibile limite l'elaborazione ad un solo agente
* **Data Registrazione Contabile** :  attraverso questo campo è possibile limite il calcolo ad una certa data situazione contabile.
* **Data Limite Insoluti** :  Attraverso tale campo si otterranno due prodotti : 
** Tutti gli effetti con data scadenza inferiore a quella indicata, verranno considerati incassati
** Il saldo della partita verrà calcolata prendendo in considerazione tutte le registrazioni fino dalla data regitrazione contabile, più le sole registrazioni di insoluto registrate fino alla data indicata in questo campo.
_1_NOTA BENE :  se il campo limite insoluti non è specificatamente indicato, assume come valore lo stesso della data registrazione contabile ed a tale data tutti gli effetti aventi data scadenza inferiore saranno considerati incassati.

