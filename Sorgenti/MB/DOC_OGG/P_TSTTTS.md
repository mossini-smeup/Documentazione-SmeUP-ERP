# SIMULATORE VIDEO DEL TTS

## OBIETTIVO
Questo programma permette di simulare il comportamento di un terminale video TTS e quindi il funzionamento
dei vari programmi creati senza aver bisogno di avere il TTS collegato.

## PREREQUISITI
Per far funzionare il simulatore del TTS occorre lanciare anche il simulatore del master, cosa possibile
manualmente da menù o tramite il tasto funzionale F08.
Uno stesso simulatore di master può gestire più simulatori di slave.

## ATTIVAZIONE DEL SIMULATORE
- Controllare che il simulatore di master sia già stato avviato e in caso contrario premere F08 per avviarlo.
- Inserire a video il nome del master e dello slave da simulare ed eventualmente un video forzato di partenza.
  Se quest'ultimo non viene impostato viene inviato al master il comando di richiesta configurazione e il
  master risponderà normalmente col video presente nell'impostazione dell'unità logica 3 dello slave.
- Premere F06 per avviare il simulatore video del TTS
- Utilizzare il simulatore
- Premere F06 per disattivare il simulatore video
- Premere F23 per disattivare il simulatore del master

## UTILIZZO DEL SIMULATORE
L'aspetto della schermata del video del TTS è diversa da quella reale in quanto ogni riga è stata
suddivisa separando su 2 colonne diverse i campi di output e i campi di input.
A fianco di ogni riga della schermata emulata vengono visualizzate le seguenti informazioni
- Oggetto
  Eventuale campo oggetto che viene passato al TTS (corrisponde all'elemento della PHT che rappresenta la riga)
- IO
  Mostra se la riga è di input (I), di output (O) o di input/output (IO)
- Lu
  Lunghezza dell'eventuale campo di input (T$PHTC)
- T
  Tipo campo (T$PHTB)
- E
  Enter automatico (T$PHTE)

Se il simulatore riceve un comando di accensione del cicalino (unità logica 6) verrà visualizzata una scritta "CICALINO".
Nel caso in cui sia stato configurato anche l'orologio (unità logica 7), l'ora verrà visualizzata come un campo
fisso HH : MM nella posizione indicata dalla stringa di configurazione.

## DIFFERENZE RISPETTO AL FUNZIONAMENTO REALE
- Eventuali comandi associati ai tasti funzionali (per esempio il backspace) NON vengono gestiti dal simulatore,
  che si limiterà a rivisualizzare il video.
- La lunghezza del campo di input è sempre fissa a 20.
- L'enter automatico NON è gestito.
- L'orario NON viene aggiornato, ma viene sempre visualizzato il campo fisso "HH : MM".

## FUNZIONAMENTO TECNICO
Il simulatore dialoga col master tramite code dati passando e ricevendo gli stessi dati di un TTS reale.
Il master legge la coda dati TTS_IN con chiave uguale al suo nome per recepire i dati provenienti dai vari slave
mentre scrive nella coda dati TTS_OUT con chiave nome_master+nome_slave i dati da inviare agli slave
**Esempio
Master  = IPTTS
Slave 1 = 01
Slave 2 = 02
Chiave per la coda dati del master    = IPTTS
Chiave per la coda dati dello slave 1 = IPTTS01
Chiave per la coda dati dello slave 2 = IPTTS02

Il simulatore dello slave gestisce solo i comandi che si riferiscono alle seguenti unità logiche : 
In ingresso
- 3 (video)
- 6 (cicalino)
- 7 (orologio)
In uscita
- 4 (tastiera)

Comunque alla partenza del simulatore viene effettuata anche la configurazione di tutte le altre unità
logiche presenti nello slave. La configurazione iniziale dello slave è quello di default dei TTS.
In questo modo vengono scambiate fra master e slave anche le varie stringhe di configurazione; queste possono
essere visualizzate guardando lo spool di log generato (ovviamente soltanto se è stato attivato da
tabella PH1).
