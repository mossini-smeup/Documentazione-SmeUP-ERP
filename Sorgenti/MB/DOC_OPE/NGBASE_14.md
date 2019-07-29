# Gestione Motivazioni Sconto

## Gestione Motivazioni Sconto

Questa funzione permette di gestire le Motivazioni per le quali vengono effettuati gli Sconti in Cassa
E' da tenere presente che anche la Forzatura di un Prezzo inferiore al Prezzo di Vendita normale viene considerata come concessione di uno Sconto

 :  : R03 Dal Menu>Principale>Registratori di Cassa>Gestione Motivazioni Sconto

## Definizione Codici Motivazioni di Sconto

Per attivare questa funzionalità occorre definire i Codici relativi alle Motivazioni di Sconto.

 :  : R03 Dal Menu>Principale>Anagrafiche di Base>Gestione Tabelle>Tabella MOTS - Motivazioni Sconti di Cassa

Apparirà la maschera contenente tutte le Motivazioni già esistenti. In basso troverete i soliti tasti funzionali, premere F6=Inserisci per codificarne una nuova. Indicare il Codice Motivo, che può essere un codice numerico, alfabetico oppure alfanumerico e confermare.
Verranno richiesti : 

 * Descrizione :  descrizione della Motivazione
 * Note Obbligatorie :  permette di rendere obbligatoria o meno l'indicazione delle note alla richiesta della Motivazione Sconto. Se impostato a Sì, non ci sarà il trinagolo giallo accanto al campo delle note,  ma apparirà il messaggio Note Obbligatorie se si cerca di confermare senza averle indicate.
 * Evidenzia Sconti su Scontrino :  indicare se si desidera visualizzare una riga sullo scontrino che evidenzi lo Sconto applicato riportando la descrizione richiesta nel campo seguente
 * Descrizione su Scontrino
 * Blocca Utilizzo Manuale in Cassa :  Se impostato a Sì, permette di NON visualizzare questa Motivazione di Sconto tra quelle disponibili nell'utilizzo in cassa

## Definizione Codici a Barre Motivazioni di Sconto

Per facilitare la definizione dei Motivi di Sconto è possibile definire dei Codici e Barre che li identifichino. Per attivare questa possibilità definire gli appositi Codice a Barre nella Tabella delle Operazioni di
Cassa

 :  : R03 Dal Menu>Principale>Anagrafiche di Base>Gestione Tabelle>Tabella OPCA - Operazioni Registratore di Cassa

Apparirà la schermata con l'elenco delle Operazioni esistenti e in basso i soliti tasti funzionali. Premere F6=Inserisci per crearne una nuova.
Innanzitutto indicare il codice a barre che si vuole utilizzare (serve un Generatore di Codici a Barre, se non si avessero già a disposizione codici a barre disponibili) e premere Invio
Verranno richiesti : 

 * Descrizione
 * Descrizione su Registratore :  la Descrizione che dovrà apparire in Cassa
 * Tipo Operazione :  selezionare Motivazione Sconto

Premere Invio e a questo punto associare all'Operazione di Cassa il Codice Motivazione Sconti - Tabella MOTS e confermare


## Gestione Motivazioni Sconto in Cassa Slave

Anche in Cassa Slave sarà possibile effettuare la lettura del Codice a Barre della tabella OPCA prima dell'utilizzo degli appositi tasti di Sconto dell'interfaccia di Cassa.
In Cassa Slave è però possibile attivare questa gestione anche senza definire i Codici a Barre della Tabella OPCA.
 :  : R03 Dal Menu>Utilità>Configurazione>Gestione Configurazione Applicativa>Cassa-Slave>Altri Parametri ed impostare a Si la Richiesta Motivazioni Sconti
Se viene attivata la Configurazione, in Cassa Slave, in occasione della Concessione di uno Sconto o della Forzatura Prezzo (nel caso non sia stato letto in precedenza l'apposito Codice a Barre) verrà
richiesto di indicare la motivazione dello Sconto effettuato
Non sarà possibile proseguire nell'utilizzo della Cassa se non viene fornita la motivazione dello Sconto.
L'obbligatorietà delle Annotazioni è condizionata al Codice Motivo utilizzato e alle impostazioni della Tabella MOTS.
P.S. La videata di richiesta del Motivo Sconto può essere presentata anche nel caso in precedenza sia stata effettuata la lettura di un Codice OPCA relativo ai Motivi di Sconto. Questo però avverrà solo nel caso in cui le Annotazioni siano obbligatorie.

## Gestione Informazioni Motivazioni di Sconto

Nel Menu di Negoziando è attiva una funzione che permette il completamento (o l'eventuale modifica) delle informazioni relative alle Motivazioni di Sconto.
 :  : R03 Dal Menu>Principale>Registratori di Cassa>Gestione Motivazione Sconti
La funzione richiede inizialmente di selezionare il Codice del Punto Vendita (facoltativo se elaborazione di Sede) e permette di indicare un range di Date o di Codici Cassa.
In base ai criteri di selezione indicati viene presentato l'elenco delle vendite di Cassa effettuate con degli Sconti
Sono a disposizione i seguenti tasti funzionali : 

 * Invio = per modificare le Motivazioni di Sconto
 * F5 = per visualizzare lo Scontrino relativo al movimento di Sconto



