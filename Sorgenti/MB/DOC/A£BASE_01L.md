## Premessa
Un Trigger è una procedura (routine o metodo) di un database associata ad una tabella e viene attivato quando la tabella viene modificata. Si tratta di uno strumento molto utile, che può essere utilizzato, per esempio, per tenere un log delle modifiche o per restringere l'accesso ai dati.

## Impostazione
La gestione del Trigger in Sme.up è gestita dalla tabella _2_FIL.
Per attivare il trigger su un file è quindi necessario compilare la tabella inserendo come elemento il file fisico su cui attivarlo.
All'interno della tabella sono da indicare anche le informazioni relative a : 
 * Programma di Trigger (Nome Pgm standard). Il programma standard di gestione del trigger è **XXTRG0**, dove XX è la sigla dell'applicazione. sarà necessario quindi creare un programma specifico - richiamato nel XXTRG0 - che esegue di fatto il trigger. Il nome di tale programma dovrà essere dato dai primi 6 caratteri del nome del file + _ + la desinenza impostata nell'ambiente specifico.
 * Indicare quando e in che casi chiamare il pgm di Trigger
 * Ambiente specifico, ovvero la desidenza del pgm specifico di trigger (SM,QR,A7, ecc...)
 * Parametro specifico, ovvero il valore specifico che si vuol far arrivare al pgm specifico di trigger

Per maggiori dettagli sulla corretta compilazione della tabella, consultare la documentazione relativa.
 :  : DEC T(ST) P() K(FIL)

## Attivazione
Per attivare il trigger su un file, in SmeUp è possibile sfruttare una utility richiamabile tramite il comando **UP AZI** .
In essa è necessario specificare : 
 * l'applicazione per la quale si vuole attivare un trigger(B£,BR,ecc...).
 * il contesto specifico dell'applicazione (enti, articoli, ecc.. )
 * il file per il quale si vuole attivare il trigger : OJ - Tipo;*FILE - Parametro;NOMEFILEFISICO - Codice
 * il programma da utilizzare per la gestione del trigger (XXTRG0)

Ciò comporterà che ogni volta che avviene un'operazione su quel file, verrà lanciato il programma di trigger.

## Controllo
Per controllare l'attivazione dei trigger è sufficiente eseguire il comando DSPFD NOMEFILEFISICO e cercare la stringa '**trigger**' (con caratteri in minuscolo).
 :  : INI Esempio di DSPFD sul BRENTI0F
 :  : CMD DSPFD FILE(BRENTI0F)
 :  : FIN

## Esempi di programmi trigger
 :  : DEC T(MB) P(SRCES) K(TRG)
