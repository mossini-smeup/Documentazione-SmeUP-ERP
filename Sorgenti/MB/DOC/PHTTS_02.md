# Configurazione del Master tramite telnet
## Premessa
Il Master ha due interfacce TCPIP e quindi due indirizzi IP : 
 * il primo è un indirizzo cablato 140.150.20.xxx, dove xxx varia a seconda del posizionamento degli switch presenti sul master stesso.
Fare riferimento alla documentazione ufficiale PHS (presente nella confezione) per il settaggio di tali switch.
 * il secondo indirizzo è quello disponibile per l'utente e va impostato secondo i criteri aziendali.
ATTENZIONE :  è fondamentale che questo indirizzo sia di tipo STATICO.

## Passi di configurazione
 * Configurare l'AS400 o il proprio PC per essere nella rete 140.150.20.yyy
 * Aprire una sessione telnet : 
TELNET 140.150.20.xxx (indirizzo cablato del Master)

Il sistema risponderà con una scritta del tipo : 
 * PHS srl Mentana (RM) * telnet server *
 * Sistema TTS vers. MTCPXX del gg/mm/aaaa

A questo punto è possibile digitare le stringhe di configurazione.
  Riportiamo qui la sequenza necessaria per un collegamento ad un
  AS400 remoto.

**Parametro C (indirizzo IP del master)**
???1WCxxx.yyy.zzz.www

il sistema risponde con :  ???2WC

**Parametro F (indirizzo IP dell'AS400)**
???1WFxxx.yyy.zzz.www

il sistema risponde con :  ???2WF

**Parametro I (indirizzo IP del default gateway / router)**
???1WIxxx.yyy.zzz.www

il sistema risponde con :  ???2WI

**Parametro E (Utilizzo protocollo TCPIP)**
???1WE1

il sistema risponde con :  ???2WE

**Parametro G (Porta TCP)**
???1WG0023

il sistema risponde con :  ???2WG

 * Scollegarsi dalla sessione telnet
 * Aprire un browser internet
 * Digitare l'indirizzo: http://[indirizzo ip del master]
 * Terminare la configurazione del master con i parametri disponibili.
