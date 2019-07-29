# Inclusione allegati nel file XML

## Premessa
L'inclusione di allegati nel file XML FatturaPA/B2B non è obbligatoriamente prevista dal tracciato XML
Si è comunque ritenuto di implementare l'inclusione di allegati nell'XML da inviare, L'inclusione di allegati nell'XML è stato implementato a partire da percorsi IFS tramite £G80 e a partire da cartelle di rete condivise tramite £H80, che presuppone Sme.UP Provider.

Nel caso si alleghino allegati a partire da cartelle di rete è necessario che nello script di SCP_CLO dell'utente dello Smart Kit, in linea nell'ambiente su cui viene avviato lo Smart Kit stesso, contenga nella variabile PROVIDER_MAPPING i percorsi delle cartelle che contengono i file da allegare.
Lo Smart Kit accederà ai soli percorsi (e alle sottocartelle) specificate nella variabile PROVIDER_MAPPING.
La variabile PROVIDER_MAPPING, ha come valori un insieme di coppie WIN() LIN() separate da "|",  poste all'interno dei MAP(), esempio : 
.  :  : C.VAR Cod="PROVIDER_MAPPING" TVal="J5" PVal="TPRV/A;P" Value="MAP(WIN(\\AS400.dominio.com\cartella1) LIN(/mnt/payara/cartella1)|WIN(\\AS400.dominio.com\cartella2) LIN(/mnt/payara/cartella2)|...|WIN(/mnt/payara/cartellann) LIN(/mnt/payara/cartellann))"

NOTA :  prima e dopo il "|" non ci devono essere spazi.

In caso si utilizzi un unico Smart Kit per più sistemi informativi è necessario che nello script di SCP_CLO in linea all'ambiente di avvio del Provider siano specificati i percorsi utilizzati da tutti gli ambienti interessati.

Nel caso non venga indicata la coda dati del Provider nella tabella V50 avviene una risalita sulla tabella LOB, prima sull'elemento H80 e poi su **.

**ATTENZIONE : **
Il legame tra percorso Windows e percorso linux è impostabile anche agendo sul file configuration.properties dello Smart Kit.
In questo file sono state predisposte 9 MAPPING_PATH_XX=WIN() LIN()
In caso si definiscano i mapping sia nel SCP_CLO che nel file di configurazione dello Smart Kit, vincono quelli presenti nel file di configurazione (non vengono fusi).

## Aggiungere allegati alla fattura tramite exit
Nel programma standard di estrazione delle fatture per la fatturazione elettronica (V5ED04B) NON è prevista la creazione del tracciato EDFEIT19 con un percorso predefinito per gli allegati da includere.
La compilazione di tale tracciato viene definita nella exit V5ED04B_xx, dove xx è un codice lungo 2 specificato nel campo T$V50N della tabella V50, solo in funzione ADD di aggiunta.
Occorre aggiungere tanti tracciati EDFEIT19 quanti sono gli allegati che si vogliono allegare.
I file vengono convertiti in testo in BASE64.

In caso di differenze tra quanto riportato nell'xml e nel pdf della fattura eventualmente allegato "vince" fiscalmente quanto presente nell'xml.

 :  : NPG
