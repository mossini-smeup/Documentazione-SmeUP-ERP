## Premessa
Si sfrutta la comunicazione SNA basata su Anynet (SNA over IP)

## Configurazione dei due sistemi
La configurazione della parte TCP/IP e della parte CTL/DEVICE deve essere effettuata su entrambi gli AS400, invertendo i ruoli nelle parole chiave "nomehost" e "nomelocale" sottodescritte.

## Configurazione TCP/IP
 * Impostazione del TCP per permettere le comunicazioni *ANYNET :  CHGNETA ALWANYNET(*YES)
 * Aggiunta alla tabella hosts del sistema degli alias dei due sistemi : 
 ** indirizzoIPhost    nomehost.idrete.SNA.IBM.COM
 ** indirizzoIPlocale  nomelocale.idrete.SNA.IBM.COM
 *** dove
 *** nomehost :  sistema remoto,
 *** nomelocale :  sistema locale
 *** idrete :  id rete visualizzabile tramite il comando DSPNETA

Esempi : 
 * 172.16.2.11       S44256CA.APPN.SNA.IBM.COM
 * 172.16.2.12       S65E4A2A.APPN.SNA.IBM.COM

## Creazione delle ctl/device anynet
 * Creare la CTL del sistema remoto :  CRTCTLAPPC CTLD(nomehost) LINKTYPE(*ANYNW) RMTNETID(idrete) RMTCPNAME(nomehost)
 ** dove : 
 ** nomehost :  sistema remoto
 ** idrete :  id rete visualizzabile tramite il comando DSPNETA

 * Creare il DEVICE del sistema remoto : 
 ** CRTDEVAPPC DEVD(nomehost) RMTLOCNAME(nomehost)
 ** LCLLOCNAME(nomelocale) RMTNETID(idrete) CTL(nomehost)
 *** dove : 
 *** nomehost :  sistema remoto
 *** nomelocale :  sistema locale
 *** idrete :  id rete visualizzabile tramite il comando DSPNETA

Modificare il neta chgneta alwanynet(*yes) e aggiungere alla tabella host 'nomehost.nomerete.SNA.IBM.COM' con alias nomehost e indirizzo IP di nomehost, dove "nomehost" è il nome sna dell'host remoto e nomerete è il nome della rete sna dell'host remoto (questi due nomi appaiono nel neta dell'host remoto con il comando dspneta) e lo stesso avviene per il nome locale (nomehostlocale.nomeretelocale.SNA.IBM.COM alias nomehostlocale IP locale).
Creare le CTLl anynet e relativi device (prima è necessario cancellare quelli vecchi, in modo da utilizzare gli stessi nomi) con il comando : 
 * CRTCTLAPPC CTLD(nomehost)
 * LINKTYPE(*ANYNW) RMTNETID(nomerete)
 * RMTCPNAME(nomehost)
e il comando
 * CRTDEVAPPC DEVD(nomehost) RMTLOCNAME(nomehost)
 * LCLLOCNAME(nomehostlocale) RMTNETID(nomerete) CTL(nomehost)

Attivare CTL e device in entrambe le parti e aprire la porta anynet (servizio APPCoverTCPIP numero porta 397) per i protocolli TCP e UDP su eventuali router e firewall.
