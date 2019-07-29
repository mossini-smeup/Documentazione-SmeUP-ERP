# Aggiornamenti
## Versione 18
 T(Completata la gestione del setup del G30 :  adesso è possibile abilitare e disabilitare)
- la toolbar
- i pulsanti funzione F da F1 a F24.
- i pulsanti specifici. Per ora solo il tasto Auto compilazione, il tasto Avanti, il tasto Indietro e il tasto Pulisci. Questi pulsanti sono disponibili solo quando si compilano configurazioni di questionari rappresentati come alberi (oggetti REQ-)
- le azioni presenti sulla sezione conclusiva (definita solo per i questionari REQ-) :  Visualizzazione Griglia risposte, Salva, Salva con Nome, Elimina, Nuova Configurazione, Salva e Ricomincia.


 :  : R01 Il setup del modulo G30 è definito dello script GRA_G30 libreria SCP_CFG.

Disbilitate le regole quando si apre una configurazione in lettura

Corretta la gestione dell'assegnazione delle risposte alle domande con lista di valori associate :  se uno dei valori viene rimosso la risposta non viene assegnata.

## Versione 19

- cambiato comportamento dopo una ricerca scatenata dal tasto **INVIO** :  il componente non si chiude e propone la scelta effettuata.
- accettati anche caratteri **"/"** e **"%"** nei campi non tipizzati o di tipo "**"



## Versione 20

- Eliminata la dipendenza dalla JVM
- Potenziato il motore dinamico includendo tutte le caratteristiche del motore statico.



## Versione 21

- Implementata la possibilità di automatizzare autocompilazione e/o salvataggio di una configurazione. Se nel parametro l'attributo  EXEC contiene una C, il modulo eseguirà l'autocompilazione, se contiene S eseguirà il salvataggio. Se contiene C e S, separate dalla virgola, verrà eseguita prima l'autocompilazione e poi il salvataggio.
In questa modalità tutti gli eventuali messaggi di errore verranno loggati. Sarà quindi ad esempio possibile l'esecuzione di n compilazioni in automatico.
- Aggiunta funzione getLoocupVarValue('nome_variabile_loocup') :  restituisce il valore di una variabile di Loocup.
- VERSIONE TEST :  Aggiunto pulsante per la visualizzazione della modifiche apportate ad una configurazione
- In manutenzione tabelle corretta gestione F15




# Sviluppi in corso

