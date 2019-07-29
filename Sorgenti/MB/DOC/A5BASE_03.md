# CONSIDERAZIONI GENERALI

Al fine di poter conoscere il valore delle quote di di ammortamento civilistico infrannuale  e di di poterne effettuare la contabilizzazione tramite registrazioni di tipo gestionale e non fiscale, va creata un'apposita linea di ammortamento, solitamente denominata linea "industriale" o "gestionale".

Lo storico dei fondi, nel caso si provenga da una conversione che non prevedeva questa linea aggiuntiva, può essere generato tramite l'apposito programma di copia, riprendendo lo storico della linea civilistica.
 :  : INI Copia movimenti di una linea
 :  : CMD CALL A5UT03A
 :  : FIN

Nel caso in cui non si abbia l'esigenza della contabilizzazione o di differenziare la pertinenza delle registrazioni infrannuali, le considerazioni sottoriportate, possono essere applicate direttamente anche alla linea civilistica.

# SETUP DELLA LINEA

L'elemento della tabella della linea dovrebbe presentare la stessa configurazione della linea civilistica, se non che con queste eccezioni : 


-**Linea Piano**dovrebbe essere valorizzata con il codice della linea civilistica in modo che da essa vengano riprese tutte le varie % e tipologie di ammortamento, senza doverle replicare appositamente per la linea industriale;

-**Ammortamenti mensili**deve risultare valorizzato

-**Valori alla data**va riempito se si vuole che l'ammortamento attribuito infrannualmente rispecchi le sole operazioni avvenute sino a quel momento. Altrimenti i calcolo avverrà sempre in funzione delle operazioni di tutto l'anno. Per questo tipo di calcolo è consigliato l'utilizzo del calendario commerciale che rende più uniformi i risultati. Ecco un esempio dell'effetto di questo campo : 
-- si è a metà luglio e si vuole conoscere gli ammortamenti al 30 giugno;
-- si prenda in considerazione un cespite con % ammortamento al 10% che in data 1 Luglio è stato alienato per la metà del suo valore;
--- se è valorizzato il campo "valori alla data", al 30 giugno risulterà un ammortamento del 5% in quanto a tale data il cespite risultava ancora per il suo intero valore;
--- al contrario viene preso in considerazione il valore di fine esercizio del cespite, per tale
motivo risulterà un ammortamento pari al 2,5%.

-**Base del calcolo alla data**è fondamentale nel caso in cui sia stato riempito il campo "Valori alla data" e si voglia che l'ammortamento totale corrisponda sempre a quello calcolato su base annua (in modo che la linea industriale non sia che una suddivisione mensile della linea civilistica). Nel qual caso il campo va valorizzato ad 1. Riprendendo il precedente esempio, a seconda di come viene valorizzato questo campo si avrebbe il seguente effetto : 
-- se il campo viene valorizzato sui mesi fino al 30 giugno avrò un ammortamento pari al 5% del del valore iniziale del cespite, mentre per i mesi successivi non verranno più imputate altre scritture in quanto in funzione dell'alienazione è già stata raggiunta la quota di ammortamento ottenuta applicando la % al valore di fine anno (base annua);
-- al contrario, sui mesi fino al 30 giugno si avrà sempre un ammortamento pari al 5% del valore iniziale del cespite, mentre per i mesi successivi verrà calcolato l'ammortamento sul valore residuo del cespite. A fine anno rispetto al valore di inizio anno si avrà perciò un ammortamento totale del 7,5%. Quindi nel primo caso il "Calcolo alla data" è una distribuzione della quota di ammortamento calcolata a fine anno sui periodi infrannuali in funzione delle operazioni avvenute, mentre nel secondo caso corrisponde applicazione delle quota di ammortamento al valore, così come risulta dal singolo sottoperiodo infrannuale (giornaliero se anno solare, mensile se commerciale).
Se si vuole l'allienamento fra linea civilistica e industriale, il secondo caso andrebbe applicato solo se anche per la linea civilistica sono stati previsti i valori alla data ed una base di calcolo periodica.


 :  : DEC T(ST) P() K(A5C&AZ)

# SETUP DELLA CONTABILIZZAZIONE DEGLI AMMORTAMENTI

Per la contabilizzazione di questa linea dovrebbero essere previsti dei tipi di registrazione gestionali ed autostornanti.

 :  : INI Set'n'play Creazione Registrazioni Automatiche >>
 :  : CMD CALL C5N000G PARM('OF' 'W F' 'AZ')
 :  : FIN
 :  : DEC T(ST) P() K(C5D&AZ)
