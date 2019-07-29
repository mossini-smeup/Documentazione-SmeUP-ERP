## OBIETTIVO E FUNZIONALITÀ
Una sezione particolare delle azioni di un oggetto è data dalle azioni di gestione dell'oggetto :  le azioni cioè che permettono di gestire le istanze della classe (inserirle, modificarle, copiarle cancellarle e visualizzarle).

Le azioni di tale sezione vengono generate a partire da due diverse logiche : 
* Dalla configurazione del workflow, quando questa è attiva
* Dalla struttura base standard quando NON è attiva la gestione del workflow

Qui a seguire si tratterà solo la seconda logica. Per la prima si rimanda alla documentazione della relativa applicazione.

## DETERMINAZIONE DELLA FUNZIONE DA ESEGUIRE
Gli oggetti che prevedono azioni di gestione sono fissati dal pgm B£GES0. Questo tipicamente si occupa di determinare : 
* Le autorizzazioni sull'azione (corrispondenti agli oav di classe J/016 e J/017 che restituiscono le informazioni classe e funzione d'autorizzazione).
* Determinare che funzione va eseguita per svolgere l'azione di gestione.

La funzione da lanciare viene a sua volta determinata in questo modo : 
* Tramite la £K04 viene verificata se la classe prevede che la gestione possa essere client (campo £K04O_GC)
* Se la classe prevede che la gestione sia client vengono letti gli script SCP_SET B£GES0 e B£GES0_U al fine di verificare se per tali oggetti è prevista una funzione di gestione.
* In caso affermativo viene usata tale funzione, viceversa il pgm B£GES0 determina quale azione di emulazione eseguire (tipicamente funzione/metodo del deviatore definiti con una schiera in fondo al programma B£GES0).

NOTA BENE :  è inoltre da tenere conto che per attivare le gestioni grafiche dai programmi guida è necessario attivare il flag "Nuova gestione azioni" nella tabella B£2.

 :  : DEC T(MB) P(SCP_SET) K(B£GES0)
 :  : DEC T(MB) P(SCP_SET) K(B£GES0_U)
 :  : DEC T(MB) P(SMESRC) K(B£GES0)

 :  : DEC T(TA) P(B£2) K(*)

## STRUTTURA DELLA FUNZIONE DI GESTIONE
Una volta individuata la funzione da lanciare si possono presentare due scenari : 
* L'oggetto è stato gestito con la nuova struttura basta sul costruttore A36 e/o sulla /COPY £K89
* L'oggetto non è ancora stato gestito con la nuova struttura e si basa sulla struttura "storica".

Nel primo caso la strutturazione è identica per ogni oggetto, mentre nel secondo caso ogni oggetto presenterà le sue specificità. Questa seconda casistica è comunque destinata a scomparire.

Nel primo caso i mattoni della struttura sono sempre gli stessi : 
* Script B£GES0 o B£GES0_U che determina quale funzione lanciare. Questa normalmente corrisponde direttamente alla scheda LOA36 o ad una scheda più complessa che la include.
* Script SCP_A36 o SCP_A36PER con codice = tipo oggetto, in cui viene definito con che parametri richiamare la scheda A36.
* E' importante notare che su tale definizione vengono normalmente fissati : 
** Lo script SCP_LAY che determina che dati si presenteranno all'utente
** L'exit della £K89 che permette di estendere le logiche standard di controllo/aggiornamento

La £K89 sopracitata è la /COPY che ora include tutte le logiche di controllo ed aggiornamento standard di un oggetto.

Quando viene invece applicata la struttura "storica", è necessario analizzare le specificità di ogni oggetto, partendo da quanto viene svolto dal pgm deviatore previsto dal pgm B£GES0.

 :  : DEC T(V2) P(LOCOS) K(A36)
- [£K89](Sorgenti/MB/DOC_OGG/P_TSTK89)
 :  : DEC T(MB) P(DOC_VOC) K(L_EDT_A36)
 :  : DEC T(MB) P(DOC_VOC) K(L_EDT_LAY)
 :  : DEC T(MB) P(SCP_SET) K(B£GES0)
 :  : DEC T(MB) P(SCP_SET) K(B£GES0_U)

## IMPLEMENTAZIONI SU AMBIENTE CLIENTE
Si descrive ora come è possibile integrare/modificare la struttura prevista dallo standard quando questa si basa sulla nuova logica : 

* **Modificare la schermata dei dati presentati a video** :  questa modifica può avvenire a due livelli : 
** Cambiare la scheda proposta dallo standard :  in questo caso è necessario implementare il sorgente B£GES0_U, in modo da poter ridefinire la funzione da lanciare su un'azione di gestione applicata ad un oggetto
** Mantenere la scheda standard, ma cambiare l'insieme di campi presentati all'utente :  è la strada consigliata salvo, l'oggetto debba essere gestito con una logica completamente diversa da quella prevista a standard. In questo caso è necessario implementare lo script del file SCP_A36PER avente codice uguale al tipo oggetto. Per partire si consiglia di partire copiando il sorgente dell'SCP_A36 dell'oggetto AR.Tramite le righe con TAG VAR sarà possibile indicare lo script di SCP_LAY tramite cui è possibile configurare i dati da presentare a video. Sono nativamente usabili tutti gli oav I, P, N e K attribuibili all'oggetto. In questo senso è importante notare che lo standard si riservi gli script di SCP_LAY aventi codice tipooggetto_nnn dove nnn è un codice numerico di 3, mentre per le personalizzazioni è consigliata la codifica tipoggetto_Xnn dove la X è fissa.
* **Integrare i controlli standard con proprie logiche :  va sempre implementato sempre lo script SCP_A36PER come da punto precedente indicando questa volta il pgm di exit. Per costruire l'exit si consiglia di partire dal sorgente di esempio B£K89_XXYY.
* **Eseguire azioni in successione ad un'azione di aggiornamento :  vale ancora la struttura standard dei flussi oggetto strutturabile attraverso le tabelle B£H/B£J.
* **Riattivare la versione storica in emulazione** :  in questo caso è necessario intervenire tramite l'exit della /COPY £K04, avente codice fisso B£K04G_U di cui è fornito un esempio. Tramite quest'exit è necessario per l'oggetto interessato pulire la variabile £K04O_GC.

 :  : DEC T(MB) P(SCP_SET) K(B£GES0_U)
 :  : DEC T(MB) P(SCP_LAY) K(AR)
 :  : DEC T(MB) P(SMESRC) K(B£K89_XXYY)
 :  : DEC T(MB) P(SMESRC) K(B£K04G_U)

## SVILUPPARE LA GESTIONE DI UN OGGETTO UFO
Per lo sviluppo della gestione di un oggetto UFO si rimanda alla documentazione di ciò che è necessario fare quando si crea un nuovo oggetto.

- [Creare un nuovo oggetto](Sorgenti/MB/DOC_OGG/OG_OG_N)

