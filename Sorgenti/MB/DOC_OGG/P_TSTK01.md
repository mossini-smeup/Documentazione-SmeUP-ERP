# OBIETTIVO

Questa /copy si occupa di svolgere tutte le funzioni di gestione delle relazioni che intercorrono fra modulo, oggetto e parametro dell'oggetto.

# FUNZIONI / METODI

* MOD :  funzioni sul modulo
** TIP :  Dato in input il modulo mi restituisce il tipo oggetto corrispondente al modulo (es. BRENTI - CN)                                                          \
** TPA :  Dato in input il modulo mi restituisce il tipo oggetto corrispondente al modulo ed il tipo oggetto del parametro del tipo oggetto (es. BRENTI - CN - TABRE)
* OGG :  funzioni su oggetto
** MOD :  Dato in input un oggetto restituisce il modulo di appartenenza
* PAM :  funzioni su parametro oggetto
** POS :  Dato in input un modulo multiparametro, restituisce il primo parametro corrispondente N.B. :  se un modulo ha un solo parametro collegato verrà ritornato il valore "1" nel campo "Unico"
** LET :  Eseguita a seguito della precedente metodo permette di continuare la scansione
* JOB :  funzioni di Job
** LPA :  Ritorna per modulo a parametri, il parametro valido per il job al momento della chiamata,
tale codice può essere recuperato in due modi :  se il modulo è monoparametro, dal singolo parametro valido, se è multiparametro dal parametro memorizzato l'ultima volta che è stata eseguito il metodoWPA
** WPA :  Come anticipato nel precedente metodo, permette di scrivere in memoria per l'utente ed ambiente, il parametro attivo per il modulo in un dato momento.

# REPERIMENTO DATI OGGETTO/MODULO

In caso di relazione Oggetto/modulo la /copy K01 utilizza delle logiche di risalita diverse a seconda dell'oggetto di partenza : 
 * OJ*PGM, OJ*DSPF, OJ*PRTF :  Assegna il modulo a partire dalla descrizione dell'oggetto                              o del sorgente. In seconda istanza analizza se il programma ha
                             un'applicazione forzata, infine analizza il nome dell'oggetto.
 * OJ*MSGF :  Assegna il modulo a partire dal nome :  se MSGBA il modulo è B£BASE, altrimenti             controlla il quarto e quinto carattere del nome per stabilire l'applicazione e di             conseguenza il modulo. Infine se nel quarto e quinto carattere non hanno             corrispondenza tra le applicazioni, viene assegnata di default l'applicazione X1 e             di conseguenza il modulo.
 * MB :  Assegna il modulo a partire dai primi 6 caratteri del codice. Se appartengono ad un        modulo, viene assegnato quello; altrimenti vengono analizzati i tipi di membri di file : 
       ** SCP_WFA :  il modulo è WFBASE
       ** SCP_CLO oppure un costruttore :  il modulo è LOBASE
       ** SCP_MNU si risale alle tabelle o ad una schiera interna stabilire il modulo
 * TA, ST, RET-, OGSP :  Si assegna il modulo a partire dalla definizione del settore o                        sottosettore (TABDS); Altrimenti viene derivata l'applicazione dal nome                        del settore, e si assegna il modulo base di tale applicazione. La tabella                        MEA è un caso particolare perchè 'applicazione viene assegnata dal                        sottosettore.
 * REF-, OJ*FILE :  Per i file e i campi di file si cerca di determinare l'applicazione                   dal nome. Se inizia con X si cerca di determinare l'applicazione dai caratteri                   successivi e poi si assegna il modulo base di tale applicazione. Altrimenti                   si controlla se il file è esplicitato in una schiera interna, o se i primi 6                   caratteri del file sono un modulo, oppure se i primi due appartengono ad una                   applicazione viene assegnato il modulo base di tale applicazione.
 * Oggetti generici :  per tutti gli oggetti non rientranti nelle precedenti esiste una schiera                      interna di assegnazione tra oggetto e modulo.
