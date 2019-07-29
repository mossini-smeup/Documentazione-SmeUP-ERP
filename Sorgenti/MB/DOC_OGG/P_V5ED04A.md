
# Obiettivo

Trasmissione EDI Fatture. Lettura dei documenti gestionali ed estrazione dati relativi alle fatture e note di credito, con creazione file XML.

# Parametri di esecuzione

* **Fatture** :  se selezionato verranno estratte le fatture
* **Note di credito** :  se selezionato verranno estratte le note di credito
* **Cliente** :  indicare cliente iniziale e finale qualora si vogliono estrarre documenti   relativi a determinati clienti, altrimenti verranno estratti tutti i clienti
* **Numero Fattura** :  indicare numero fattura iniziale e finale qualora si vogliono estrarre   particolari documenti, altrimenti verranno estratti tutti i documenti
* **Data Fattura** :  indicare data fattura iniziale e finale qualora si vogliono estrarre    documenti aventi una particolare data documento, altrimenti verranno estratti tutti i documenti
* **Tipo Azione** :  selezionare una delle seguenti azioni possibili : 
** Elabora fatture mai estratte :  vengono estratti i documenti che non sono mai stati estratti.
** Elabora fatture non ancora inviate (già estratte o meno) :  vengono estratti documenti già estratti in precedenza e non inviati allo Sdi e documenti che non sono mai stati estratti.
** Riestrai fatture con XML errato :  riestrazione documenti per i quali è stato generato un errore xml in fase di invio allo Sdi.
** Riestrai fatture che sono state scartate :  riestrae fatture già inviate all'SDI che sono state poi scartate.

