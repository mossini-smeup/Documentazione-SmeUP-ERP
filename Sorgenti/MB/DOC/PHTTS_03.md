# Descrizione dell'impianto di esempio
Dominio di rete :  192.168.0.0
Subnet mask     :  255.255.255.0
IP AS400        :  192.168.0.100
IP Master TTS   :  192.168.0.200
User profile    :  IPTTS

# Creazione oggetti su AS400
## Profilo utente
CRTUSRPRF USRPRF(IPTTS) PASSWORD(*USRPRF) PWDEXP(*NO)
Specificare una jobd adeguata. Normalmente si usa la stessa assegnata agli utenti finali.

## Tabelle di configurazione
 :  : DEC T(ST) K(PHU01)
(o un'altra **con la stessa struttura campi**)
I sottosettori di questa tabella rappresentano gli slave collegati

 :  : DEC T(ST) K(B£TUF)
Inserire la PHU appena creata (o equivalente)

 :  : DEC T(ST) K(PHM)
Descrizione          Master TTS - TCPIP
Tabella Slave        TT1
C-Indirizzo IP       192.168.000.200
D-RF multiantenna    0000000000000000
E-Modalità TCP       1
F-Indirizzo IP AS400 192.168.000.100
G-Porta TCP su AS400 0023
H-Cadenza GET_REQ    00
I-Default Gateway    000.000.000.000
J-Keep alive         02
K-Multisessione      0
L-IP base del VAC    000.000.000.000
Tipo comunicazione   1
Nome job - RISERVATO

 :  : DEC T(ST) K(PHN)
Descrizione          Utente TTS in Tcp/Ip
M-Lingua             0
Sottosettore VAC
N-Dim buffer AS400   1

# Configurazione del Master
## Configurazione iniziale tramite Telnet
La prima configurazione va fatta tramite telnet, utilizzando l'indirizzo IP cablato del Master.
__Attenzione__ :  l'indirizzo IP cablato è modificabile tramite l'impostazione degli switch sul retro del master stesso.
Fare riferimento alla documentazione ufficiale PHS per i dettagli.

 * TELNET '140.150.20.128'
 ** Impostare indirizzo di rete del master : 
>???1WC192.168.000.200
 ** Impostare indirizzo di rete dell'AS400 : 
>???1WF192.168.000.100
 ** Impostare il funzionamento in TCP/IP : 
>???1WE1
 ** Uscire dal telnet, spegnere il master e riaccenderlo
 ** Dopo circa un minuto, tramite wrkactjob, verificare che un lavoro intestato all'utente IPTTS sia attivo.

## Completamento della configurazione
I parametri non impostati tramite telnet vengono letti direttamente dalle tabelle PHM e PHN.
