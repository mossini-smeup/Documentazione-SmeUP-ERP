
## PREREQUISITI CLIENT
I prerequisiti sono i seguenti : 
- PC in Dominio e collegato alla Lan aziendale;
- Server di autenticazione raggiungibile nella lan;
- CA versione 5.3 o successiva
- Sistema Operativo  Windows XP SP2/SP3, oppure Windows 7.

**NOTA** :  Le versioni Home non supportano l'SSO con Kerberos.

## PREREQUISITI INFRASTRUTTURALI
L'accesso in SSO mediante Kerberos richiede un'adeguata configurazione di rete e dell'iSeries. Far riferimento ai documenti tecnici per maggiori dettagli.


**NOTE**
L'SSO non può funzionare se il collegamento all' iSeries viene effettuato via IP pubblico (es. se mi collego da casa).
In questo caso è necessario collegarsi in VPN SSL alla lan aziendale per usufruire delle policy di dominio.

L'accesso in SSO al sistema iSeries avverrà con l'utente associato a quello di Windows, se sarà necessario utilizzare un utente diverso bisognerà configurare un'altra connessione 5250 che NON utilizzi kerberos come metodo di autenticazione.



## COME ABILITARE L'ACCESSO TRAMITE KERBEROS

Avviare la sessione di emulazione, poi selezionare la voce di menù Comunicazioni, configura.

Si aprirà la finestra di dialogo riportata di seguito, cliccare sul pulsante Proprietà : 

![LOBASE_163](http://localhost:3000/immagini/MBDOC_OPE-LOSSON_50C/LOBASE_163.png)
Selezionare nella combo "Informazioni di accesso ID utente", la voce "Utilizza nome principal kerberos, senza richiesta", come nella figura seguente : 

![LOBASE_164](http://localhost:3000/immagini/MBDOC_OPE-LOSSON_50C/LOBASE_164.png)
Confermare con il pulsante OK e poi ancora OK.

Verrà chiesta conferma per la disconnessione : 

![LOBASE_165](http://localhost:3000/immagini/MBDOC_OPE-LOSSON_50C/LOBASE_165.png)
Confermare anche questa richiesta.

Se i prerequisiti sono soddisfatti, comparirà la videata con la scelta degli ambienti (se multipli), oppure si accederà al menù applicativo.

## COME ABILITARE ACCESSI MULTIPI

Se l'accesso al ISeries avviene con almeno due utenti differenti è necessario creare due connessione :  una che utilizzi l'SSO e un'altra in cui si possa indicare l'utente.

La prima si configurerà come indicato al paragrafo precedente, nella seconda sarà necessario indicare nelle Informazioni di accesso :   "ID utente, il valore Utilizza ID predefinito, richiedi se necessario".

Per configurare una nuova connessione, avviare il programma "Avvio o configurazione sessione", disponibile nel percorso :  Start, tutti i programmi, IBM ISeries Access per Windows, Emulazione.

Nella seguente finestra di dialogo, selezionare "Nuova sessione" e procedere poi come nel caso di modifica di una sessione esistente.

![LOBASE_166](http://localhost:3000/immagini/MBDOC_OPE-LOSSON_50C/LOBASE_166.png)
La connessione in SSO utilizzerà l'utente ISeries associato al profilo di windows.
La seconda utilizzerà l'utente indicato.



