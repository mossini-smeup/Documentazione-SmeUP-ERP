# Descrizione

Con applicazione intendiamo un aggregato di componenti, moduli e servizi software finalizzato alla fornitura di una o più funzionalità.

# File configurazione Application.xmi

Caratteristiche di un applicazione sono : 
* Nome :  Nome dell'applicazione, applicazioni con lo stesso nome costituiscono un cluster
* Text :  Descrizione dell'applicazione
* Port :  All'interno di un cluster indirizzamento logico di un nodo

A un'applicazione possono essre collegati servizi di tipo 'hook' per gestirne il ciclo di vita
(vedi servizi di tipo hook), ad esempio per attivare disattivare funzionalità di sistema quali
un DBMS o il TCP.

## Variabili configurazione
E' possibile indicare come valori nel file Application.xmi delle variabili speciali
contraddistinte dalla sintassi ${mio_nome}

Elenco variabili disponibili

| 
| .COL Txt="Nome" LunAut="1" A="L" |
| ---|----|
| 
| .COL Txt="Descrizione" LunAut="1" A="L" |
| rt.core.application.name|Nome applicazione |
| osgi.instance.area|Root dell'applicazione |
| 


