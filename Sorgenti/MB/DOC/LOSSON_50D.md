## SCOPO DEL DOCUMENTO

In questo documento sono illustrati i prerequisiti per attivare l'SSO con kerberos in un dominio Windows e le procedure per configurare il DC e i client  sia standard che Citrix.

Si farà riferimento non solo al server AD, ma anche al server System-i e ai client.
Tutti gli attori in gioco devono soddisfare dei prerequisiti ed essere configurati opportunamente.

In questo documento verranno indicate le procedure per configurare il dominio windows e alcuni dei prerequisiti dell'i-Series e dei client.
Per una panoramica completa sui prerequisiti e sulla configurazione dei client e dell'i-Series fare riferimento ai relativi documenti.

## PREREQUISITI FONDAMENTALI

 * SO Domain controller Windows Server 2003 o superiore
 * Livello funzionale minimo del domino e della foresta Active Directory minimi :  Windows Server 2003
 * Tutti i client devono essere correttamente uniti al dominio Active Directory in questione.
 * Tutti i client interessati alla funzionalità devono essere Windows 2000 Professional o superiori. Non sono ammesse licenze Home o Home Premium in quanto non unibili all'Active Directory
 * Tutti i client devono aver installato Client Access 5.3 o superiore nel caso di Windows 2000 o XP e Client Access 5.8 o superiori per Vista e Windows 7.
 * L'accesso all'iSeries in SSO tramite un'emulazione telnet 5250 / mocha è non è possibile in quanto ad oggi non supportano SSO.
 * La tabella host del client NON deve contenere riferimenti alla risorsa a cui si vuole accedere (System-i, ecc) in quanto SSO utilizza anche il DNS diretto e inverso per la verifica del ticket di autenticazione.
 * Per poter utilizzare Loocup con accesso in SSO deve essere abilitato il supporto Kerberos. Per ogni client (o tramite policy di dominio) va impostata una chiave nel registro di windows. Vedere l'appendice A per i dettagli.
 * Per poter utilizzare il CA in windows 7 va abilitata la opportuna codifica del ticket. Vedere l'appendice B per i dettagli.


## Prerequisiti Operativi

 * Record Host A relativo al sistema AS400 correttamente registrato nella zona di ricerca diretta (Forward Lookup) con il seguente schema :  <hostname AS400>.<AD domain>.<TLD> (es. :  as400.azienda.local)
 * Puntatore PTR relativo al sistema AS400 correttamente configurato nella zona di ricerca inversa (Reverse Lookup)
 * Sui Domain Controller Windows Server 2003, installare i Support Tools per poter utilizzare il comando KTPASS

## Limiti
 * Non sono stati compiuti test con client Linux.
 * Da verificare ulteriormente la compatibilità in ambienti cross-domain, quelli in cui cioè client appartenenti a più domini Windows accedono allo stesso sistema AS400.
 * Per abilitare Loocup all'accesso in SSO è necessario impostare su ogni client una chiave di registro (manualmente o via Group Policies).

## Fase Operativa
 * Creare, sul server DNS primario utilizzato da Active Directory, i corretti record come da prerequisiti.
 * Creare nel dominio Active Directory un utente per la funzione di passaggio Kerberos. Questa operazione può essere automatizzata :  l'Operation Navigator è in grado di creare un file di configurazione in modo automatico.

### Creazione utenti del DC
Per automatizzare la creazione degli utenti di dominio necessari al dialogo iSeries - DC, fare riferimento al documento **Configurazione iSeries**


## Configurazione dei client 5250 e Loocup

- Far riferimento ai documenti relativi


## Installazione con Citrix
lo scenario e la configurazione è identica a quella di un personal computer, pertanto : 
 * Se il server ha Windows 2003, la configurazione di Citrix equivale a quella di un PC con Windows XP.
 * Se il server ha Windows 2008, la configurazione di Citrix equivale a quella di un PC con Windows 7.

Durante la configurazione di SSO, va posta attenzione a quanti server sono disponibili :  è molto probabile che sia indispensabile poter disporre di due o più pubblicazioni distinte della stessa applicazione configurata opportunamente.
Anche in questo caso è importantissimo che il Dominio funzioni a dovere, compresa la distribuzione delle Policy di Gruppo.

## Possibili problematiche
Alcuni casi di malfunzionamenti : 
 * Indisponibilità di AD
 * Errore nel protocollo NTP
 * Non corretta distribuzione delle Policy di Windows (può succedere specialmente con Windows 7)
 * Caduta del servizio TIVOLI su AS400, può avvenire se una PTF di sistema operativa non viene caricata nel modo corretto


## Appendice A - Abilitazione del supporto kerberos
In Windows 7 o XP il supporto kerberos viene disabilitato di default. Per abilitarlo va attivata la seguente chiave di registro : 
In windows 7 : 

HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Lsa\Kerberos\Parameters
Value Name :  allowtgtsessionkey
Value Type :  REG_DWORD
Value :  0x01  ( default is 0 )

In Windows XP SP2 o SP3 : 

HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Lsa\Kerberos\
Value Name :  allowtgtsessionkey
Value Type :  REG_DWORD
Value :  0x01


La caratteristica 32 o 64 bit non influenza l'accesso tramite Kerberos.
Nel caso di sistema operativo a 64 bit è necessario installare una JVM a 32 bit in quanto Loocup non funziona su JVM a 64 bit.
La JVM da utilizzare è la 1.6.0_xx.


## Appendice B - Definizione codifica ticket in Windows 7
In Windows 7 la codifica di default del ticket non è corretta. Quando si cerca di accedere in SSO con il CA si riceve un messaggio con codice  CWBSYS1011.
Procedere come definito di seguito : 
 - Start > Esegui > gpedit.msc
 -  Espandere Criteri Computer Locale > Configurazione Computer > Impostazioni di Windows > Impostazioni di Sicurezza > Criteri Locali > Opzioni di sicurezza
 -  Nella parte di destra doppio click su Sicurezza di rete :  configura tipi di crittografia consentiti per Kerberos
 -  Selezionare tutte le voci tranne l'ultima.
 -  Premere OK.



Procedura in inglese
 -  Start > Run > gpedit.msc
 -  Expand Local Computer Policy > Computer Configuration > Windows Settings > Security Settings > Local Policies > Security Options
 -  Double click Network security :  Configure encryption types allowed for Kerberos
 -  Select DES-CBC-MD5 (your PC may have others listed, which may need to be enabled as well. For additional information, see Changes in Kerberos Authentication ) in the Microsoft Technet site listed below under References. 5. Press OK.
 -  Click on File menu, and select Exit .
 -  Riavviare il pc
Per i dettagli fare riferimento al seguente documento : 
 :  : DEC T(J1) P(PATHFILE) [http://www-01.ibm.com/support/docview.wss?uid=nas19a3a2d52a849457d862576f10079427c](http://www-01.ibm.com/support/docview.wss?uid=nas19a3a2d52a849457d862576f10079427c)
D(Abilitazione crittografia in Windows 7)

NOTE
Prima di impostare la crittografia si consiglia di definire la chiave che abilita kerberos (vedi appendice A) e solo in seguito di abilitare i tipi di crittografia.
Dai test compiuti è emerso inoltre che le modifiche ai tipi di crittografia supportata sono recepite solo dopo aver riavviato, disabilitato tutte le crittografie, riavviato, reimpostato tutte le crittografie (tranne l'ultima) e riavviato nuovamente.
I test hanno anche evidenziato che l'aver abilitato la crittografia per kerberos ha portato dei temporanei malfunzionamenti nell'accesso alla rete, risolti dopo un riavvio.


E' necessario inoltre impostare la seguente policy : 

![LOBASE_167](http://localhost:3000/immagini/LOSSON_50D/LOBASE_167.png)
## FAQ
D :  L'accesso in SSO funziona, anche se la password su iSeries scade?
R :  Sì, l'accesso in SSO non è influenzato dalla scadenza della password su iSeries

D :  Se cambio la password dell'utente su iSeries l'accesso in SSO viene influenzato?
R :  No.
D :  Se un utente è bloccato posso accedere in SSO?
R :  No. Non è possibile accedere ne in SSO ne in altro modo.
D :  la password di dominio è diversa da quella sull'iSeries?
R :  sì :  la password di dominio rimane differente da quella iSeries
D :  Se non sono connesso al dominio o sono fuori sede, posso utilizzare l'accesso in SSO?
R :  No, è necessario utilizzare la password definita sull'iSeries.


