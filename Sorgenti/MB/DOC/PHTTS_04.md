# Gestione di display
## Programmi
I programmi che interagiscono con un display sono definiti dalla tabella PHT.
Gli elementi della PHT sono le singole videate con i singoli comandi da gestire (F1,F2,F3...)
Il programma **PHVID1** è quello che gestisce il richiamo dei vari display in sequenza leggendo la tabella PHT.
La tabella PHF mi definisce le varie funzioni sul video. E' utile per verificare i video che vengono richiamati.
La tipologia di oggetti passati nei vari video è definita nella tabella PHD. Attenzione per inserire nuovi elementi chiamare la definizione di tabella (l'UP DEF) della PHD.


## Specificità programmi di emissione video
I video condividono una DS di dati. Nella DS inserisco tutti i dati/oggetti che mi si presentano nel flusso. Es :  £PHDATI_SK
Un video viene visto come una serie di righe. Nei programmi le righe sono identificate tramite la schiera SK_OUT. Gli elementi della schiera sono le righe (fino a 4 o 16 righe).

### Ciclo di vita del video
* F_INZ  :  funzione richiamata solo se il video è il primo di una sequenza. Utile per inizializzare la schiera dei dati
* F_PRE  :  funzione utile per precaricare i dati nel video prima dell'emissione.
* F_POS  :  funzione chiamata dopo l'emissione del video per controllare o per eseguire funz. esterne

Il metodo F_INZ pur essendo presente in tutti i video viene richiamata solo nel video iniziale.
Il metodo F_PRE carica i dati da inserire nei campi video. Attenzione non può essere utilizzata per richiamare funzioni su slave differenti perchè non comunica con il PHMAN0.

F_POS  è composta da vari richiami tra cui : 
* CTR_VID (faccio i controlli) in cui ho
** P$IN35 indica che è in erore
** P$INOUT indica di emettere il video
* ESE_FUN esecuzione di scritture su file specifici(ad es. dichiarazioni del P5ATTI)

## Particolarità nel flusso
Attenzione se è necessario chiamare un altro slave per richiedere informazioni o per lanciare funzioni specifiche è necessario usare la schiera SK_UTE.
Solitamente la schiera SK_UTE dovrebbe essere riempita
Gli elementi della schiera SK_UTE sono comandi TTS che vengono mandati al programma PHVID1 che prima di lanciare il prossimo video della sequenza li invia al PHMAN0. Il PHMAN0 a sua volta li invia ai programmi specifici dello SLAVE determinandoli dalla tabella.
Poichè i programmi di gestione delle videate possono essere chiamati da più slave viene utilizzata una gestione chahe tramite la schiera in  OCCUR WRKPGM che viene interrogata nelle varie fasi del flusso.

