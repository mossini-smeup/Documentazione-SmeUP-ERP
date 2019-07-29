# Configurazione di Fiel.up
## Corrispondenza oggetti fisici con oggetti Sme.up
### Master
Corrisponde alla tabella PHM, che contiene la configurazione del master stesso e alcuni parametri aggiuntivi. Gli indirizzi IP contenuti in questa tabella >devono corrispondere a quelli impostati nel master all'atto della sua configurazione tramite telnet. Eventuali modifiche a questa tabella saranno recepite dal master al prossimo collegamento.
Ulteriori parametri di configurazione sono presenti nella tabella PHN.

### Slave
 :  : DEC T(TA) P(*CNTT) K(UF)
Corrisponde al sottosettore della "tabella slave" indicata in PHM.

### Unità logica
 :  : DEC T(TA) P(*CNTT) K(UF)
Corrisponde all'elemento della tabella degli SLAVE (vedi sopra).
I tipi di unità logiche conosciute da FILD.UP sono rappresentate dai sottosettori della tabella PHC.

## Configurazione del master (TA PHM)
>Tabella Slave
Elemento della tabella B£TUF.
E' la tabella i cui sottosettori rappresentano gli slave collegati al master.
>C-Indirizzo IP
Indirizzo ip del master (specificare sempre nel formato xxx.yyy.www.zzz utilizzando
anche gli zeri non significativi :  ad esempio 172.016.020.123)
>D-RF multiantenna
Configurazione per radiofrequenza multiantenna
>E-Modalità TCP
1=protocollo TPCIP
0=protocollo SNA
>F-Indirizzo IP AS400
Indirizzo ip dell' AS400 (specificare sempre nel formato xxx.yyy.www.zzz utilizzando
anche gli zeri non significativi :  ad esempio 172.016.020.011)
>G-Porta TCP su AS400
Numero della porta utilizzata
>H-Cadenza GET_REQ
Cadenza Get Request
>I-Default Gateway
Indirizzo ip di un eventuale default gateway
>J-Keep alive

>K-Multisessione
Attivazione della multisessione sul master
>L-IP base del VAC
Indirizzo ip base di un eventuale VAC
>Tipo comunicazione
1=interattiva (dft)
2=tramite code dati
>Nome job - RISERVATO
Campo riservato da non usare

Ulteriori parametri sono presenti in tabella PHN.
>M-Lingua
0=italiano
1=inglese
>Sottosettore VAC
Sottosettore della tabella PHV contenente il pgm di controllo del VAC
>N-Dim buffer AS400
0=stringa da 256 byte
1=stringa da 512 byte (preferibile)

## Configurazione degli slave
E' sufficiente creare tanti sottosettori quanti sono gli slave presenti.
Utilizzare la numerazione esadecimale "rivista" dalla PHS : 
01
02
03
04
05
06
07
08
09
0 :  (corrsiponde a 0A)
0; (corrsiponde a 0B)
0< (corrsiponde a 0C)
0= (corrsiponde a 0D)
0> (corrsiponde a 0E)
0? (corrsiponde a 0F)
10

Gli indirizzi devono corrispondere a quelli impostati tramite switch sugli slave fisici.
Il massimo numero di slave configurabili per ogni master è 255 (corrispondente a "??").

## Configurazione delle unità logiche
Ogni tipo di unità logica possiede dei parametri che ne consentono la configurazione.
E' possibile configurare le UL direttamente da Fiel.up (Menu' PH00, opzione 11-configuratore).
Fare riferimento al manuale tecnico ufficiale della PHS per il significato dei singoli parametri.
