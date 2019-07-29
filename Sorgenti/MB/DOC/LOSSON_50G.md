 :  : HEA PRIV(001)

## Introduzione

Il Single sign-on (SSO) è un sistema che permette all'utente di autenticarsi una sola volta e di accedere a tutte le risorse informatiche alle quali è abilitato.
Tra i diversi sistemi disponibili Kerberos è quello che risponde meglio alle nostre esigenze.
I principali vantaggi di Kerberos sono : 
 * semplificazione della gestione delle password :  maggiore è il numero delle password da gestire, maggiore è la possibilità che vengano utilizzate pass- word simili le une alle altre e facili da memorizzare, abbassando così il livello di sicurezza;
 * semplificazione della gestione delle autorizzazioni agli accessi ai vari servizi;
 * compatibilità con i più diffusi sistemi operativi;
 * sicurezza anche su reti insicure.

## Kerberos
### Principi di funzionamento

Kerberos[1] è un protocollo di autenticazione standard sviluppato al MIT.
E' implementato nelle reti Windows, nei sistemi Unix, sul Machintosh e sull'AS400.
Loocup è basato su tecnologie che rendono l'integrazione con Kerberos semplice e affidabile.
Kerberos è fondato sul principio del terzo fidato. Un client (di solito un utente o un servizio) invia al KDC (Key Distribution Center) una richiesta per ottenere un ticket. Il KDC consegna al client uno speciale ticket, detto ticket-granting- ticket (TGT) crittato con la password del client registrata nel proprio database.
Il client decritta il TGT, usando la password in suo possesso. Se il client riesce a decrittare il TGT (cioè, se la sua password è corretta), lo conserva come prova della propria identità. Il TGT, che scade in un tempo prefissato, permette al client di ottener ulteriori ticket che gli permettono di accedere a determinati servizi. Il processo di richiesta del ticket e la consegna sono trasparenti al client.
Una buona analogia è uno ski pass per il weekend valido per diversi impianti sciistici. Si mostra lo ski pass a uno qualsiasi degli impianti (fino alla scadenza) e si riceve un biglietto di risalita per quell'impianto. Con il biglietto, si può sciare su qualsiasi pista di quell'impianto. Se il giorno successivo si va in un altro impianto, ancora una volta si mostra lo ski pass e si ottiene un altro biglietto.
La differenza è che con Kerberos è il sistema ad accorgersi automaticamente che si è in possesso di uno ski pass. In questo modo il sistema può avviare in modo trasparente il processo di richiesta e consegna del  ticket per il servizio.


![LOBASE_50](http://localhost:3000/immagini/LOSSON_50G/LOBASE_50.png)
### Kerberos e Windows

Le reti Windows implementato kerberos con Active Directory.
A seconda della particolare versione di Windows che si sta usando può essere necessario intervenire sul registro di sistema per consentire alle applicazioni l'accesso ai token Kerberos salvati nella sessione utente.

# Casi d'uso
## SSO in un'applicazione desktop

Un'applicazione lanciata da una sessione utente autenticata con Active Directory si autentica  atomaticamente a un servizio "Kerberizzato".
### Autenticazione dell'applicazione a un AS400

In azienda vogliamo in particolare che Loocup, se lanciato da un utente autenticato in rete, si colleghi all'AS400 senza richiedere di nuovo l'inserimento delle credenziali. L'AS400 deve essere configurato in modo da partecipare al protocollo Kerberos.
### Autenticazione dell'applicazione a un server IMAP

Vogliamo inoltre che Loocup si connetta automaticamente a un server imap.
Quest'ultimo deve essere configurato per usare l'autenticazione Kerberos. Più
in generale il server viene impostato per usare i protocolli GSS o SASL che si devono appoggiare comunque (per le nostre esigenze) su Kerberos. Bisogna assicurarsi tra l'altro che queste API non facciano capo al meccanismo di autenticazione NTLM che costituisce un'alternativa non portabile a kerberos (perché specifica di Windows).
Il programmatore deve impostare alcune property prima di effettuare la connessione

final Properties props = new Properties();
{
props.put("mail.imap.auth.plain.disable", "true");
 props.put("mail.imap.sasl.enable", "true");
 props.put("mail.imap.sasl.mechanisms", "GSSAPI");
 props.put("mail.imap.host", host);
}
// Get session
final Session session = Session.getInstance(props);
// Get the store
Store store = null;
try {
 store = session.getStore("imap");
 store.connect(host, "nome-utente", "");

 // Get the folder
 final Folder folder = store.getFolder("INBOX");
folder.open(Folder.READ_ONLY);
 // Get directory
 final Message message[] = folder.getMessages();

 for (int i = 0, n = message.length; i < n; i++) {
  System.out.println(i + " :  " + message[i].getFrom()[0] + "\t"
      + message[i].getSubject());
 }

 // Close connection
 folder.close(false);
 store.close();

} catch (final NoSuchProviderException e) {
 // TODO Auto-generated catch block
 e.printStackTrace();
} catch (final MessagingException e) {
 // TODO Auto-generated catch block
e.printStackTrace();
}


## SSO in un applicazione web

Lo scenario nell'applicazione web si complica leggermente perchè in questo caso dobbiamo sia configurare il browser che l'applicazione web o l'application server. Per fortuna i principali browser devono essere soltanto abilitati all'uso di SPNEGO che è un altro meccanismo compatibile con GSS ma che serve a contrattare il meccanismo di autenticazione che in generale potrebbe essere Kerberos o NTML (non per noi). Per quanto riguarda la parte server abbiamo due possibilità. Una è quella di installare un modulo al ivello di application server capace di capire il Kerberos. L'altra è di applicare un modulo software alla particolare applicazione web. Nel primo caso il modulo sara disponibile a tutte le applicazione web installate nello stesso application server.
Una volta autenticati sulla rete, l'applicazione web chiederà, per ogni sessione utente, il corrispondente username mappato sull'AS400. Questo è necessario perchè nel caso dell'as400 non è possibile usare direttamente gli username della rete Windows a causa della limitazione a dieci caratteri degli username su questo server.
## SSO in Loocup
### JAAS

The JavaTM Authentication and Authorization Service(JAAS)[2] è un'API presente nel JRE standard a partire dalla versione 1.4 di java. L'architettura di JAAS prevede la possibilità di intercambiare i meccanismi di autenticazione.
Questo permette alle applicazioni Java di rimanere indipendenti dalla sottostanti tecnologie di autenticazione. Tecnologie nuove o aggiornate possono essere inserite senza dover modificare l'applicazione. La particolare implementazione del meccanismo di autenticazione può essere definita in un file di configurazione (per noi Kerberos).
Il codice di base per la nostra implementazione in Loocup è tratto da un tutorial in rete [5] : 
import javax.security.auth.*;
import javax.security.auth.callback.*;
import javax.security.auth.login.*;
import com.sun.security.auth.callback.TextCallbackHandler;

/**
 * This JaasAcn application attempts to authenticate a user
 * and reports whether or not the authentication was successful.
 */
public class JaasAcn {

  public static void main(String[] args) {

      // Obtain a LoginContext, needed for authentication. Tell
      // it to use the LoginModule implementation specified by
      // the entry named "JaasSample" in the JAAS login
      // configuration file and to also use the specified
      // CallbackHandler.
      LoginContext lc = null;
      try {
           lc = new LoginContext("JaasSample",
                      new TextCallbackHandler());}
      } catch (LoginException le) {
          System.err.println("Cannot create LoginContext. "
              + le.getMessage());
          System.exit(-1);
      } catch (SecurityException se) {
          System.err.println("Cannot create LoginContext. "
              + se.getMessage());
          System.exit(-1);
      }

      try {

          // attempt authentication
      lc.login();}

      } catch (LoginException le) {

          System.err.println("Authentication failed :  "
          System.err.println("  " + le.getMessage());
          System.exit(-1);

      }

      System.out.println("Authentication succeeded!");

    }
}

Prima di costruire il LoginContext bisogna specificare la posizione del file di configurazione di JAAS. E' possibile farlo come opzione nella chiamata di java : 

-Djava.security.auth.login.config=jaas.conf

o equivalentemente con l'istruzione : 

System.setProperty("java.security.auth.login.config", "jass.config");

Il file di configurazione deve contenere una entry come la seguente : 

JaasSample {
com.sun.security.auth.module.Krb5LoginModule required useTicketCache=true;
}
Si noti che "JassSample" scritto in jaas.conf deve coincidere con l'argomento passato a new LoginContext. Il parametro "useTicketCache"[8] impostatato a true richiede al modulo di Login di usare se possibile un ticket già reperito (ad esempio in fase di login alla workstation in rete).
Il modulo ha inoltre bisogno di sapere la posizione del KDC(1) e deve conoscere il REALM a cui ci si vuole autenticare. Queste informazione possono essere specifica come prima. I nomi delle proprietà sono : 
java.security.krb5.realm
java.security.krb5.kdc
Alternativamente questi dati possono essere scritti nel file di configurazione di Kerberos la cui posizione varia a seconda del sistema operativo[6].  E' possibile anche specificare la posizione di questo file come proprietà di sistema : 
java.security.krb5.conf
Ecco un esempio del contenuto di questo file : 
[libdefaults]
        default_realm = SMEA.IT
        -default_tkt_enctypes = rc4-hmac
        -default_tgs_enctypes = rc4-hmac
[realms]
        SMEA.it  = {
               kdc = dc1.smea.it
               default_domain = SMEA.it
}

[domain_realm]
       .smea.it = SMEA.IT

### JGSS

L'API JGSS[9] è usata per realizzare il SSO in java. Di solito è usata indirettemente dalle API che ne hanno bisogno come fa ad esempio javamail. Il programmatore deve comunque associare al thread corrente un contesto di controllo di accesso (AccessControlContext). Si ottiene questo risultato implementando l'interfaccia "PrivilegedAction" e inserendo nel metodo run il codice che ha bisogno di accedere al ticket. Il metodo "run" viene quindi eseguito indirettamente attraverso l'istruzione : 
Subject.doAs(lc.getSubject(), action);
### Collegamento all'AS400

L'implementazione di Kerberos in Loocup è stata realizzata utilizzando il modulo di login "Krb5LoginModule". Siccome JTOpen2, il framework di connessione che usiamo per comunicare con l'AS400, incorpora le API JGSS, il processo di autenticazione avviene in modo trasparente al  programmatore. In pratica grazie a JAAS JTOpen può reperire dalla sessione utente il token di Kerberos
(TGT) per ottenere il token TGS. Prima di effettuare la richiesta di connessione è necessario eseguire le istruzioni : 
AS400 as400 = new AS400(serverName);
as400.setGSSName(this.loginContext.getSubject().getPrincipals()
.iterator().next().getName());

### Collegamento a un server IMAP

Anche l'API javamail è in grado di usare il protocollo GSS con il meccanismo Kerberos. Come per JTOpen(2) anche in questo caso il processo di autenticazione al servizio è trasparente al programmatore.
Come server IMAP in particolare abbiamo usato Dovecot[4] perché è lo stesso usato dalla SMEA. Nel caso si utilizzino server imap diversi bisogna verificare che supportino l'autenticazione Kerberos.
## SSO nell'Agenda di SmeUP

I principali browser utilizzano il protocollo SPNEGO per realizzare SSO. In particolare il protocollo è  supportato da Internet Explorer, Firefox, Safari. Non è supportato per il momento da Chrome.
### Internet Explorer
I passaggi fondamentali per abilitare SSO su Internet Explorer[12] possono variare a seconda delle combinazioni Browser/versione-di-Windows ma in generale sono i seguenti : 
 * In Internet Explorer Strumento -> Opzioni Internet (in inglede Tools -> Internet Options).
 * Clicca sulla scheda Protezione (in inglese Security).
 * Clicca Rete Locale -> Siti (in inglese Local intranet -> Sites).
 * Assicurarsi che "Includi tutti i siti che non usano il proxy" (in inglese "Include all sites that bypass the proxy server") sia selezionato.
 * Cliccare su Avanzate (in inglese Advanced) e aggiungere il nome del sito a cui ci si deve autenticare.
 * Cliccare se OK.

### Firefox

 * Apri firefox, and digita "about : config" nella barra delle url. Appariranno tutte le voci di configurazione di Firefox.
 * Vai alla voce "network.negotiate-auth.trusted-uris".
Imposta il valore ">" cliccando due volte sulla voce e digitando ">" nel dialog che appare.
 * Ora vai alla vode "network.negotiate-auth.delegation-uris"
Imposta il valore ">" cliccando due volte sulla voce e digitando ">" nel dialog che appare.

### SPNEGO

SPNEGO[3] è uno "pseudo meccanismo" dell'API GSS usato per negoziare un reale meccanismo di autenticazione (nel nostro caso Kerberos).
Modulo di login per Glassfish è stato aggiunto il supporto a "SPNEGO" a Glassfish nella forma di un modulo di autenticazione (SAM) conforme alla specifica JSR 192. Internamente il modulo utilizza JGSS per accedere al meccanismo SPNEGO. Il servlet container effettuerà le chiamate JGSS in modo trasparente all'applicazione web installata. L'unica responsabilità del programmatore è quella di esprimere in modo dichiarativo (all'interno del file web.xml) la richiesta di verifica del possesso delle credenziali per l'accesso alle funzionaltà esposte dall'applicazione web. [10]
## Agenda SmeUp

Dobbiamo intervenire sui sorgenti dell'Agenda per rimappare l'utente Kerberos (Active Directory) su quello dell'AS400. In pratica si apre una connessione all'A400 in modo del tutto analogo a quanto fatto per Loocup e si estrae dalla connessione lo username.
//Deve essere gia stabilita una connessione
String as400userId=as400.getUserId();

# Troubleshooting

## Dovecot

Per far funzionare Dovecot oltre alle istruzioni di cui all'url "http://wiki.dovecot.org/Authentication/Kerberos", abbiamo dovuto impostare la proprietà "auth gssapi hostname".
## Regitry di Windows

Un'utile url per risolvere i problemi più diffusi di malfunzionamento e la seguente
http://download-llnw.oracle.com/javase/1.5.0/docs/guide/security/jgss/tutorials/Troubleshooting.html.
Si noti che anche per Windows 7 bisogna impostare una chiave nel registry.
GLOSSARIO

 * Principal :  qualsiasi utente, computer e servizi forniti dai server deve essere definito come come Kerberos Principal.
 * Instance :  le Instance sono usate dai servizi Principal e dai Principal amministrativi.
 * Realm :  è il nome univoco del contesto a cui appartengono i Principal. Di solito corrisponde al dominio DNS trasformato in lettere maiuscole.
 * Key Distribution Center :  (KDC) consiste di tre parti, un database di tutti i Principal, il server di autenticazione e il server dei ticket granting ticket. Per ciascuno realm ci deve essere un KDC.
 * Ticket Granting Ticket :  è fornito da un server di autenticazione (AS), il Ticket Granting Ticket è crittato con la password dell'utente che è nota solo all'utente e al KDC.
 * Ticket Granting Server :  fornisce i Ticket ai client su richiesta.
 * Ticket :  conferma l'identità di due Principal. Uno è l'utente e l'altro è il servizio richiesto dall'utente. I Ticket stabiliscono una chiave di crittografia usata per una comunicazione sicura durante una sessione autenticata.
 * Keytab File :  file estratto dal database dei Principal del KDC e conteniene la chiave di crittografia per un servizio o per un host.

NOTE
(1)In realtà queste informazioni sarebbero reperibili dal DNS[7]. Probabilmente "Krb5LoginModule" non interroga il DNS. Il programmatore potrebbe inserire del codice JNDI per automatizzare la richiesta rendendo più semplice la configurazione di Kerberos.
(2) Abbiamo verificato che le API di Kerberos sono implementate almeno dalla JTOpen versione 6.7.
Bibliografia

[1] Kerberos V5 UNIX User's Guide
[http://web.mit.edu/kerberos/www/krb5-1.8/krb5-1.8.3/doc/user-guide.html](http://web.mit.edu/kerberos/www/krb5-1.8/krb5-1.8.3/doc/user-guide.html)
[2] JavaTM Authentication and Authorization Service (JAAS) Reference Guide.
 :  : DEC T(J1) P(PATHFILE) [http://download.oracle.com/javase/6/docs/technotes/guides/security/jaas/JAASRefGuide.html](http://download.oracle.com/javase/6/docs/technotes/guides/security/jaas/JAASRefGuide.html)
[3] SPNEGO
[http://en.wikipedia.org/wiki/SPNEGO](http://en.wikipedia.org/wiki/SPNEGO)
[4] Kerberos
[http://wiki.dovecot.org/Authentication/Kerberos](http://wiki.dovecot.org/Authentication/Kerberos)
[5] JAAS Authentication
 :  : DEC T(J1) P(PATHFILE) [http://download-llnw.oracle.com/javase/1.4.2/docs/guide/security/jgss/tutorials/AcnOnly.html](http://download-llnw.oracle.com/javase/1.4.2/docs/guide/security/jgss/tutorials/AcnOnly.html)
[6] Kerberos Requirements
 :  : DEC T(J1) P(PATHFILE) [http://download-llnw.oracle.com/javase/1.4.2/docs/guide/security/jgss/tutorials/KerberosReq.html](http://download-llnw.oracle.com/javase/1.4.2/docs/guide/security/jgss/tutorials/KerberosReq.html)
[7] Kerberos V5 System Administrator's Guide, Using DNS
 :  : DEC T(J1) P(PATHFILE) [http://web.mit.edu/kerberos/www/krb5-1.8/krb5-1.8.3/doc/krb5-admin.html-Using%20DNS](http://web.mit.edu/kerberos/www/krb5-1.8/krb5-1.8.3/doc/krb5-admin.html-Using%20DNS)
[8] Class Krb5LoginModule
 :  : DEC T(J1) P(PATHFILE) [http://download.oracle.com/javase/1.5.0/docs/guide/security/jaas/spec/com/sun/security/auth/modul+
](http://download.oracle.com/javase/1.5.0/docs/guide/security/jaas/spec/com/sun/security/auth/modul+
)
e/Krb5LoginModule.html)
[9] Single Sign-on Using Kerberos in Java, Mayank Upadhyay, Ram Marti, Oracle and/or its affiliates
 :  : DEC T(J1) P(PATHFILE) [http://download.oracle.com/javase/1.4.2/docs/guide/security/jgss/single-signon.html](http://download.oracle.com/javase/1.4.2/docs/guide/security/jgss/single-signon.html)
[10] Configuring An Existing Glassfish Domain for SPNEGO
 :  : DEC T(J1) P(PATHFILE) [https://spnego.dev.java.net/documentation/configuring_spnego_in_glassfish.html](https://spnego.dev.java.net/documentation/configuring_spnego_in_glassfish.html)
[11] Browser Configuration for SPNEGO
 :  : DEC T(J1) P(PATHFILE) [https://spnego.dev.java.net/documentation/browser_configuration_for_spnego.html](https://spnego.dev.java.net/documentation/browser_configuration_for_spnego.html)
[12] Configure the Internet Explorer Client Browser,
 :  : DEC T(J1) P(PATHFILE) [http://download.oracle.com/docs/cd/E13169_01/ales/docs21/integrateappenviron/spnego.html-1067149](http://download.oracle.com/docs/cd/E13169_01/ales/docs21/integrateappenviron/spnego.html-1067149)
[13] HTTP-Based Cross-Platform Authentication by Using the Negotiate Protocol
[http://msdn.microsoft.com/en-us/library/ms995329](http://msdn.microsoft.com/en-us/library/ms995329)
