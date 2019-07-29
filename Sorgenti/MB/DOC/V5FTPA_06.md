# Inclusione allegati nel file XML

## Premessa
L'inclusione di allegati nel file XML FatturaPA/B2B non è obbligatoriamente prevista dal tracciato XML
Si è comunque ritenuto di implementare l'inclusione di allegati nell'XML da inviare.

## Prequisiti
* Attivare l'exit del pgm di estrazione. In questo senso l'unica cosa di cui si deve occupare l'exit, è la costruzione dell'indirizzo a cui trovare il file. L'inclusione del file nell'xml avverrà poi tramite un'elaborazione standard
* I file da allegare possono trovarsi o su l'IFS o su un server esterno. Nel caso in cui si trovino su un server esterno, andrà eseguita un'attività di configurazione descritta a seguire.

## Aggiungere allegati alla fattura tramite exit
Nel programma standard di estrazione delle fatture per la fatturazione elettronica (V5ED04B) NON è prevista la creazione del tracciato EDFEIT19 con un percorso predefinito per gli allegati da includere.
La compilazione di tale tracciato viene definita nella exit V5ED04B_xx, dove xx è un codice lungo 2 specificato nel campo T$V50N della tabella V50, solo in funzione ADD di aggiunta.
Occorre aggiungere tanti tracciati EDFEIT19 quanti sono gli allegati che si vogliono allegare.
I file vengono convertiti in testo in BASE64.

In caso di differenze tra quanto riportato nell'xml e nel pdf della fattura eventualmente allegato "vince" fiscalmente quanto presente nell'xml.

Come anticipato in precedenza va solo specificato il percorso per accedere all'allegato. Tale percorso può essere un percorso IFS o di un server remoto. Questa indicazione dipende dal campo F19TPPA, tipo percorso, che può assumere i valori IFS e SMB.

 :  : NPG

## Setup per accesso ad un server remoto
Se i dati sono remoti è necessario eseguire alcuni setup, in parte a carico del consulente applicativo, in parte a carico chi gestisce il provider.

Per il consulente applicativo è necessario settare una variabile di SCP_CLO. Un suggerimento è quello di usare lo script avente nome = utente usato per il provider.
La variabile cambia a seconda che il provider sia Linux o Windows.

Per un provider linux (tutti gli smartkit lo sono) è la variabile PROVIDER_MAPPING. La variabile va così settata : 
* C.VAR Cod="PROVIDER_MAPPING" TVal="J5" PVal="TPRV/A;P" Value="MAP(WIN(xxxxxxx) LIN(/mnt/share_0)|WIN(yyyyyyy) LIN(/mnt/share_1))"
In WIN dove vedo xxxxxx e yyyyyy vanno i percorsi stile windows cui dovrà poter accedere, mentre
LIN costituisce solo una rimappatura di questa cartella. Si usa come modello fisso /mnt/share_n, dove n è un numero progressivo che può andare da 0 in avanti. Il "|" è il carattere che permette di suddivinare i percorsi che voglio, vengano presi in considerazione.

Per un provider windows è la variabile PROVIDER_PATHS. Qui le cose sono più semplici in Value, va solo messo il percorso o l'elenco dei percorsi divisi da ";" cui il provider dovrà poter accedere. La variabile va quindi così settata : 
* C.VAR Cod="PROVIDER_PATHS" Txt="Path accettati dal server remoto" Value="\\SRV005.smeup.com\XRILASCIO;\\SRV005\XRILASCIO"

Una volta settati questi percorsi, sarà necessario che chi gestisce il provider, venga contattato e faccia le attività che abilitino il provider a questi percorsi. Per quanto riguarda il caso Linux (smartkit) sarà necessario montare il percorso Windows. Di questo si occupa chi gestisce lo smartkit.

Il Provider accederà ai soli percorsi (e alle sottocartelle) specificate nella variabile.

Nel caso non venga indicata la coda dati del Provider nella tabella V50 avviene una risalita sulla tabella LOB, prima sull'elemento H80 e poi su **.

**ATTENZIONE : **
Il legame tra percorso Windows e percorso linux è impostabile anche agendo sul file configuration.properties dello Smart Kit.
In questo file sono state predisposte 9 MAPPING_PATH_XX=WIN() LIN()
In caso si definiscano i mapping sia nel SCP_CLO che nel file di configurazione dello Smart Kit, vincono quelli presenti nel file di configurazione (non vengono fusi).
