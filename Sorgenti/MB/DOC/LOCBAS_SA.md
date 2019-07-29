# Introduzione

L'implementazione standalone fornisce alcune funzionalità di Looc.up (Smetray)
senza l'obbligo di connessione permanente al sistema.
Richiede un database locale che viene periodicamente fasato rispetto a quello centrale
e può costituirne un sottinsieme (ES. Clienti di un agente)

Lo sviluppo grafico avviene tramite editazione di file .jsp contenenti XML di Looc.up.
Lo sviluppo applicativo avviene tramite classi java che tipicamente operano sul DB locale.

Componenti principali : 
* Client
* Server Slave
* Package cliente
* Server Master


## Client

Libreria java che controlla le operazioni base di Smetray :  avvio, apertura/chiusura finestre ...
Il client ha un identificativo univoco tracciabile da server centrale
Supporto per licenze con scadenza temporale e controllo remoto da sede centrale
Controllo di versione e aggiornamento remoto software
Connettore configurabile verso un generico server di F().
Attualmente è disponibile un connettore http verso un server web.


## Server Slave

Server HTTP+application server embedded (Tomcat) responsabile di : 
- Fornire gli XML delle request (Looc.up function) attraverso mapping in web.xml
- Servizio generico di accesso DB (tip UP SQL)
- Ritorna gli XML delle schede tramite parsing di file .jsp
  Analogo del JATRE_18C + SCP_SCH
- Aggiornare il DB locale rispetto a quello centrale.
  Attualmente vengo gestiti DB quali HSQL (embedded) e MySQL (installazione locale)
- Fornisce librerie Java per trattare gli XML di Looc.up (EXB,EXU) e gli aggiornamenti
  rispetto al DB centrale

## Package cliente

Costituisce la personalizzazione del cliente, tipicamente servlet e jsp personalizzate

## Server Master

E' un server Web.up responsabile di : 
- validare i client
- fornire gli XML per aggiornare il DB remoto
- ricevere gli XML per aggiornare il DB centralre

Vengono distribuite delle schede e servizi Looc.up (SCP_SCH) per visualizzare : 
- client installati e relativo livello di aggiornamento
- statistiche di accesso e acquisizione dati

