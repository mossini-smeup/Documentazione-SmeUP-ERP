 :  : T00 Produzione a flusso di materiali

# Ordini MFP
Sono ordini di produzione dove, nella tabella tipo ordine, si definisce il flag tipo di produzione MFP.
L'inserimento di un ordine MFP determina la creazione dei suoi contenitori pianificati, il numero dei contenitori è calcolato sulla base della quantità richiesta e della quantità per contenitore.
La quantità per contenitore è definita nei parametri logistici "£P3", per magazzino/articolo; se  non è presente nei parametri logistici si risale alla quantità del lotto multiplo dell'articolo (da parametri di pianificazione).
In un ordine MFP, oltre alle normali quantità gestite esiste anche la "__quantità contenitori" :  che, per ciascun contenitore, è la somma di
 * quantità pianificata
 * quantità residua
 * quantità riempita
questa qtà è aggiornata ad ogni movimentazione.
La modifica quantità di un ordine determina la rifasatura dei suoi contenitori :  se la quantità ordinata aumenta si genera un nuovo numero di contenitori necessario per coprire la nuova richiesta, se la quantità diminuisce e non è inferiore a quella già riempita nei contenitori, si annullano i contenitori in eccesso. L'eliminazione dei contenitori in eccesso agisce prima sui contenitori che hanno solo quantità pianificata, poi decrementa la quantità pianificata dei contenitori non completamente riempiti. Non è possibile diminuire la quantità ordinata al di sotto della soglia della quantità già riempita. È possibile annullare un ordine solo se nessun suo contenitore è riempito o in fase di riempimento, l'annullamento dell'ordine determina l'annullamento di tutti i suoi contenitori.

# Ciclo logistico
Il ciclo MFP è il ciclo dell'ordine di produzione integrato delle ubicazioni logistiche :  ubicazione "ANTE" a monte del centro di lavoro che esegue l'operazione; ubicazione "POST" a valle del CDL.
Non è obbligatorio che esistano tutte le ubicazioni ANTE / POST, dovranno essere definite solo quelle legate ai punti di "controllo" del ciclo (milestones). Per definizione è obbligatoria l'ubicazione ANTE del CDL della prima fase de ciclo e le ubicazioni ANTE / POST dei CDL delle lavorazioni esterne (conto lavoro di fase).
**Nota Bene**, è possibile associare ad un gruppo di contenitori (anche un solo contenitore può rappresentare un gruppo) un proprio ciclo diverso da quello dell'ordine, questa possibilità viene utile ad esempio per fare avanzamenti parziali o per parallelizzare i carichi su più centri di lavoro.

## Definizioni
Viene definita come "prima lavorazione" una dichiarazione di lavorazione alla prima fase del ciclo.
Viene definita come "prima rilavorazione" una dichiarazione di rilavorazione alla prima fase del ciclo.
Vengono definite definite come "lavorazioni o rilavorazioni successive" tutte le dichiarazioni in fasi DIVERSE dalla prima fase del ciclo.

# Ubicazioni logistiche
Sono le ubicazioni di linea che possono stare a monte (ubicazione ANTE) o a valle di un centro di lavoro (ubicazione POST). Le ubicazioni MFP sono caratterizzate dal tipo ubicazione (tabella GMU) dove è attivato il flag di ubicazione MFP. Le ubicazioni sono codificate con un suffisso "_A"  (ubicazioni "ANTE") o suffisso "_P" (ubicazioni "POST")

## Attribuzione ubicazioni a risorsa
L'attribuzione di una ubicazione ad una risorsa avviene nell'anagrafico risorse :  se nella risorsa è presente una ubicazione e questa è di tipo MFP, se ha suffisso _A è considerata l'ubicazione "ante" e si ricerca in anagrafico ubicazioni se esiste anche l'ubicazione MFP con suffisso _P, lo stesso discorso se l'ubicazione in anagrafico risorse ha suffisso _P (si cerca se c'è anche la _A).
Esempio : 
 * Codice risorsa = AARR012 con ubicazione MFP = A01_A; si cerca se esiste anche l'ubicazione A01_P
 * Codice risorsa = AARR012 con ubicazione MFP = A01_P; si cerca se esiste anche l'ubicazione A01_A
Se in anagrafico la risorsa non ha ubicazioni o l'ubicazione presente non è tipo MFP allora si cerca in anagrafico ubicazioni se esistono delle ubicazioni codificate con lo stesso codice risorsa e suffisso _A o _P.
Esempio : 
 * codice risorsa = AARR012, avente in anagrafcio risorse un'ubicazione non MFP o un'ubicazione blank
 * si cerca se esistono le ubicazioni AARR012_A e AARR012_P

## Ubicazioni per conto lavoro
Con l'eccezione dell'ubicazione ante del CDL della prima fase del ciclo non esistono obblighi di avere ubicazioni ante e/o post nei vari CDL :  si codificano quelle che necessitano ai fini del controllo avanzamento produzione.
A questa regola si deroga per le ubicazioni ante e post delle risorse esterne :  tutte le risorse esterne __devono__ avere sia l'ubicazione ante (dove si spostano i contenitori in attesa di essere spediti in conto lavoro) sia l'ubicazione post (dove arrivano i contenitori restituiti dai terzisti).

# Contenitori
Sono contenitori MFP quelli che derivano da un ordine MFP. In ogni contenitore sono definite due quantità : 
 * la "quantità pianificata",  viene memorizzata alla creazione del contenitore
 * la "quantità riempita" viene incrementata ad ogni prima lavorazione, è usata per determinare la "quantità pianificata residua" (pianificata - riempita).
La "quantità pianificata residua" è calcolata come differenza tra la "quantità pianificata" e la "quantità riempita" a meno del flag 4 "Saldo pianificato" :  se questo è attivo la "quantità pianificata residua" è sempre nulla. Il flag di "Saldo pianificato" viene gestito solo alle dichiarazioni di prima lavoraizone e viene memorizzato se si fa una dichiarazione con "Saldo alla fase".

La creazione di un nuovo contenitore pianificato determina la rifasatura delle quantità del suo ordine.

I contenitori per gli scarti sono contenitori speciali identificati con flag 6, quando si fa una dichiarazione di produzione a scarto la qtà può essere versata solo in un contenitore per gli scarti (e viceversa quando si movimentano i pezzi buoni questi non possono andare in un contenitore scarto); questi contenitori sono esclusi dal ciclo e dagli impegni risorse dell'ordine.

# Impegni materiali
Non esistono particolari indicazioni o limitazioni, nella defnizione del tipo impegno, tipicamente questa è una produzione che prevede lo scarico dei materiali alla fase quindi di solito si usa la Modalità scarico = ID.
Da notare che gli impegni materiali che vengono creati sono per contenitore.

# Impegni risorse
Vale lo stesso discorso fatto per gli impegni materiali. Anche in questo caso gli impegni risorse creati sono per contenitore. Nel flag 20 di S5IRIS viene riportato il Tipo MFP dalla testata dell'ordine produzione.

# Giacenza
La produzione MFP __deve__ avere un'area di giacenza interna definita per :  Ubicazione, Fase, Contenitore; ed un'area di gaicenza esterna (C/Lavoro di fase) definita per :  Fornitore, Fase, Contenitore.

# Avanzamento
L'avanzamento MFP genera : 
 * un prelievo da :  contenitore / ubicazione / fase - origine;
 * un versamento in :  contenitore / ubicazione / fase - destinazione;
 * la dichiarazione di tutte le attività comprese tra fase origine e fase destinazione.
Nella prima lavorazione non viene eseguito lo scarico dall'ubicazione ante (la dichiarazione attività della prima fase genera, per modalità di scarico = ID, il prelievo dei componenti da magazzino)
Nell'ultima fase non viene eseguito il versamento nell'ubicazione post, (la dichiarazione attività dell'ultima fase genera il versamento del prodotto a magazzino). In questo caso se si dichiarano produzioni parziali e si vuole eseguire un unico versamento a magazzino solo quando l'intero contenitore è riempito, occorre introdurre nel ciclo come ultima fase il carico a magazzino che sarà una fase in cui si esegue solo l'avanzamento del contenitore intero.

## Flusso MFP
### Creazione contenitori pianificati.
I contenitori sono generati alla creazione dell'ordine. Per ciascun contenitore viene memorizzata la "quantita pianificata".
I contenitori possono essere fittizi o effettivi. I contenitori fittizi servono per pianificare il carico risorse alle varie fasi, alla prima dichiarazione della prima lavorazione si crea un contenitore effettivo decrementando della quantità corrispondente i contenitori fittizi. Se si utilizzano i contenitori effettivi, la prima dichiarazione crea una quantità riempita nel contenitore, le dichiarazioni successive incrementeranno la qtà riempita fino al saldo alla fase.

### Prima lavorazione
È una dichiarazione di avanzamento che include la prima fase del ciclo; è identificata tale quando nell'avanzamento non viene indicato il contenitore e l'ubicazione origine
 * __non __ viene eseguito alcun prelievo del contenitore origine
 * la dichiarazione della prima fase determina il prelievo dei componenti (comportamento standard, funzione della modalità di scarico, non sottoposto al controllo dei programmi MFP)
 * se la dichiarazione è a saldo viene saldata la "quantità pianificata"
La prima lavorazione è eseguita secondo le due diverse modalità : 
 * __contenitori pianificati effettivi__, si verifica quando i contenitori pianificati sono i contenitori effettivi usati nell'avanzamento.
 ** in questo caso si versa nel contenitore pianificato.
 ** la dichiarazione determina l'incremento della "quantità riempita" del contenitore, con la corripondente diminuzione della "quantità pianificata residua"
 * __contenitori pianificati fittizi__, si verifica quando i contenitori pianificati sono solo fittizi e NON sono i contenitori usati nell'avanzamento. La modalità di avanzamento è divisa in due fasi : 
 ** primo riempimento; si versa in un nuovo contenitore. Se esistono contenitori pianificati disponibili il sistema decrementa la qtà pianificata.
 ** riempimenti successivi; si versa nel contenitore creato nel primo riempimento fino al saldo alla fase

### Lavorazioni successive
È una dichiarazione di avanzamento che NON include la prima fase; è identificata tale quando nell'avanzamento vengono indicati il contenitore e l'ubicazione origine.
 * esegue il prelievo del contenitore origine dall'ubicazione e fase origine.
 * esegue il versamento nel contenitore destinazione nell'ubicazione e fase di destinazione (tranne per l'ultima fase)
 * esegue tutte le dichiarazioni di attività comprese tra la fase origine e la fase destinazione

### Prima rilavorazione
È una dichiarazione di avanzamento che include la prima fase del ciclo; è identificata tale quando nell'avanzamento viene indicato il contenitore ma non viene indicata l'ubicazione origine.
Trattandosi di una rilavorazione viene eseguito il prelievo del contenitore origine dalla prima fase del ciclo e la dichiarazione della prima fase NON determina il prelievo dei componenti
 * si versa nel contenitore destinazione che può essere un contenitore esistente oppure un nuovo contenitore.
 * non viene eseguita alcuna funzione sulle quantità pianificata e riempita del contenitore

### Rilavorazioni successive
Come lavorazioni successive.

 ### Trasferimento.
È una dichiarazione in cui non vengono eseguite attività; generalemente si usa tra l'ubicazione post di una fase e l'ubicazione ante della fase successiva (in questo caso si potrebbe usare anche l'avanzamento in quanto tra l'ubicazione post e l'ubicazione ante della fase successiva non ci sono dichiarazioni di attività)
 * si dichiara il contenitore origine
 * il sistema recupera la sua giacenza; se esiste giacenza sia nell'ubicazione ante che in quella post utilizza la ante, da questa giacenza deriva ubicazione, fase e quantità
 * se si avanza lo stesso contenitore in fasi diverse la quantità NON può essere inferiore alla giacenza
 * si dichiara l'ubicazione di destinazione ed eventualmente la fase (se il ciclo non prevede di ritornare sullo stesso CDL l'ubicazione è monofase ed è sufficiente l'ubicazione)
**Nota**; un'ubicazione si definisce monofase quando il ciclo attraversa il suo centro di lavoro una sola volta, mentre è multifase quando il ciclo ripassa più volte nello stesso CDL.

### Controllo del contenitore pieno
È attivabile in sede di impostazione; tranne quando si avanzi lo stesso contenitore nella stessa fase (stesso contenitore da ubicazione ante a ubicazione post dello stesso centro di lavoro) controlla che non sia possibile
 * versare ancora in un contenitore pieno (flag "Contenitore pieno" =  "1" nel contenitore destinazione)
 * prelevare da un contenitore NON pieno (flag "Contenitore pieno" =  " " nel contenitore origine " ")
In avanzamento di un contenitore, se è impostato il campo "Saldo alla fase" : 
 * si iposta il flag di saldo nell'attività
 * si imposta "1" nel flag "Contenitore pieno"
se il campo "Saldo alla fase" non è impostato, si forza blanks nel flag "Contenitore pieno"

## Conto Lavoro
Il conto lavoro permette la gestione dell'uscita e del rientro quando la fase è di lavorazione esterna. Per l'invio il contenitore deve essere trasferito o avanzato nell'ubicazione ANTE della risorsa esterna.
**Nota**; a differenza della generalità delle risorse interne nelle risorse esterne l'ubicazione ante e quella post sono associate a più risorse (terzisti) ed ssumono il significato di "Ubicazione invio in conto lavoro" e "Ubicazione rientro da conto lavoro" : 
### Invio contenitore
* flusso creazione bolla spedizione da giacenza in Ubicazione ANTE; in alternativa flusso RF di creazione righe da collo
* il collegamento della bolla trasferisce il matriale dall'ubicazione ANTE ad una area di conto lavoro per contenitore
* nel flusso di uscita si può inserire un'azione che crea l'ordine di C/Lavoro dalla bolla
### Rientro
* flusso ricezione materiale da ordine di conto lavoro, in alternativa flusso RF di creazione righe da collo (interno, esterno, esterno con alias)
* azione di distribuzione righe entrate attribuendole, in funzione delle quantità, agli ordini di conto lavoro, di produzione ed ai contenitori giacenti c/o terzista
* avanzamento dei contenitori usciti in area conto lavoro nei nuovi contenitori in Ubicazione POST del CDL esterno
