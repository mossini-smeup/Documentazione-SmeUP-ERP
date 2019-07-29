
## SSO
Il Single sign-on (SSO, traducibile come autenticazione unica o identificazione unica) è un sistema specializzato che permette ad un utente di autenticarsi una sola volta e di accedere a tutte le risorse informatiche alle quali è abilitato.

Una buona analogia è uno ski pass per il weekend valido per diversi impianti.
Si mostra lo ski pass a uno qualsiasi degli impianti (fino alla scadenza)e si riceve un biglietto di risalita per quell'impianto. Con il biglietto, si può sciare su qualsiasi pista di quell'impianto. Se il giorno successivo si va in un altro impianto, ancora una volta si mostra lo ski pass e si ottiene un altro biglietto.
La differenza è che con Kerberos sarà il sistema ad accorgersi automaticamente che si è in possesso di uno ski pass. In questo modo il sistema è possibile avviare automaticamente, in modo trasparente all'utente, il processo di richiesta e consegna del ticket per il servizio.

In SmeUp l'SSO è realizzato con Kerberos.
Questo protocollo è compatibile con i più diffusi sistemi operativi.
Ecco uno schema del suo funzionamento.

![LOBASE_50](http://localhost:3000/immagini/LOSSON_50P/LOBASE_50.png)

Segue un dettaglio relativo alle diverse fasi di autenticazione (completamente trasparenti all'utente).


 - Un programma client richiede al KDC (Key Distribution Center) per conto dell'utente un TGT (Ticket Granting Ticket), cioè una certificazione temporanea dell'identità dell'utente.
 - Se le credenziali fornite dall'utente sono corrette il programma ottiene il TGT e lo conserva per accedere ai servizi previsti.
 - Il programma client presentando il TGT richiede al KDC un TGS (Ticket Granting Server), cioè un permesso temporaneo di accesso a un particolare servizio.
 - Il server KDC fornisce il TGS.
 - Il programma client si presenta al servizio con il proprio TGS.
 - Il servizio verifica l'identità del client e fornisce una prova della propria identità.

Una volta completata la verifica delle credenziali il client può usufruire del servizio (ad esempio un servizio di posta, un database ecc.).

## GLOSSARIO
 * **KDC - Key Distribution Center** :  consiste di tre parti, un database di tutti i Principal, il server di autenticazione e il server dei ticket granting ticket. Per ciascuno realm ci deve essere un KDC.
 * **Principal** :  qualsiasi utente, computer e servizi forniti dai server deve essere definito come come Kerberos Principal.
 * **TGT - Ticket Granting Ticket** :  è fornito da un server di autenticazione (AS), il Ticket Granting Ticket è crittato con la password dell'utente che è nota solo all'utente e al KDC.
 * **TGS - Ticket Granting Server** :  fornisce i Ticket ai client su richiesta.
 * **Ticket** :  conferma l'identità di due Principal. Uno è l'utente e l'altro è il servizio richiesto dall'utente. I Ticket stabiliscono una chiave di crittografia usata per una comunicazione sicura durante una sessione autenticata.
