# Cosa sono
Per variabili Loocup si intendono le variabili, relative alla sessione, quindi utilizzabili all'interno dell'esecuzione di un'istanza di Loocup, e che sono accessibili da qualunque entità in Loocup.
# Come vederle
Qualora si sia autorizzati, le variabili definite in Loocup sono visualizzabili all'interno della scheda di informazioni di sistema, visualizzabile tramite dal menù di Looc.Up selezionando la voce "Servizi-->Informazioni di sistema" oppure "Help-->About-->Informazioni di sistema".
# Classificazione
La classificazione della variabili avviene tramite il parametro **Origine**.
Tale parametro può assumere 4 differenti valori : 

- WIN :  sotto questa categoria ricadono le variabili del sistema operativo su cui è in esecuzione Loocup. Nel caso di un Windows sono le variabili di sistema e le variabili dell'utente Windows che sta eseguendo Loocup. Es. :  directory utente (USER.HOME), directory di esecuzione di Loocup (USER.DIR)
- JVM :  sotto questa categoria ricadono le variabilii messe a disposizione dalla Java Virtual Machine all'interno di cui sta girando Loocup. Es. :  versione della Java Virtual Machine (JAVA.VERSION)
- INI :  sotto questa categoria ricadono le variabili definite negli script presenti nei files SCP_CLO in Smeup e caricate durante l'inizializzazione di Loocup
- LOC :  sotto questa categoria ricadono le variabili definite o calcolate da Loocup. Es. :  istante attuale (*NOWMILLIS), codice sessione (*SESSION_ID), utente di collegamento (*USER)


# Le variabili di scheda
La gerarchia è questa : 
* Loo.Var :  di loocup
* Sch.Var :  di form di scheda (si può dire che valga per tutta la schermata)
* Ssc.Var :  di sottoscheda (vale solo per una particolare sottoscheda)
* Sec.Var :  di sezione (vale solo per una sezione di scheda)

Dato un nome di una variabile viene sempre cercato a tutti i livelli partendo da quello di sezione.

NOTA BENE :  Non esiste il concetto di variabile a valore nullo, per cui in una sezione se una variabile avrebbe valore nullo, tale variabile non viene considerata e viene cercata nei livelli precedenti.

Queste variabili possono essere stanziate : 
* In sezione in modo automatico, tramite i dati presenti nella sezione (vedasi la documentazione di ogni componente)
* Negli script di scheda tramite i tag S.VAR.VAL
* Negli script di scheda tramite i corrispondenti attributi indicabili sui tag di definizione dei dinamismi (G.DIN)
* Tramite la scrittura del pertinente xml dai servizi richiamati (vedasi routine JAX_BVAR_I/VAR/VAR_F della COPY £JAX_C1)

# Scope della variabili

![LOBASE_11A](http://localhost:3000/immagini/LOBASE_11A/LOBASE_11A.png)