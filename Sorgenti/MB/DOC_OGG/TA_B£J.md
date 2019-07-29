# B£J - Gruppi di azioni
 :  : DEC T(ST) K(B£J)
## OBIETTIVO
!!! ATTENZIONE :  DOCUMENTAZIONE IN FASE DI COMPLETAMENTO.
Nell'elemento di questa tabella viene impostato un passo elementare del flusso, vale a dire un'azione che verrà lanciata durante l'esecuzione del flusso stesso.
La composizione della tabella dipende dal tipo di flusso che si sta impostando.
I vari campi dipendono dalla natura del flusso che si sta eseguendo : 

- Flusso batch
- Flusso avanzato
- Flusso di collegamento
- Flusso di scelta
- Flusso di esecuzione

Riferirsi all'aiuto della tabella B£H per la loro definizione.
## CONTENUTO DEI CAMPI
 :  : FLD T$ATTI **Attivazione**
interpostato 'N', l'azione non viene eseguita.
Se impostato 'J', l'azione di tipo F viene eseguita solo in ambiente client.
La si definisce nei campi di tabella. Questa modalità è attualmente deprecata, in quanto è
preferibile impostare la seguente modalità 'F' di più semplice compilazione e puù estesa.
Se impostato 'F', l'azione di tipo F viene eseguita solo in ambiente client.
La definizione della funzione avviene attraverso l'utilizzo del campi libero utente.
NOTA BENE :  solo per i flussi di tipo "A-" è possibile in loocup sulle F sfruttare le variabili _&_di scheda relative all'oggetto 1 (_&_OG.T1/P1/K1) ed i relativi OAV (_&_OA).

- Flusso batch.
 (controllo non attivato nel flusso batch).
- Flusso avanzato.
-- Se impostato 'O', l'azione è obbligatoria :  se al termine del flusso non è stata eseguita, viene richiesta esplicitamente la rinuncia.
-- Se impostato 'R', l'azione è obbligatoria e ripetibile :  al termine del flusso viene presentata una finestra con possibilità di ripetizione delle azioni ripetibili, oltre alla possibilità di esecuzione delle azioni non obbligatorie.
- Flusso di scelta
- Flusso di esecuzione

 :  : FLD T$VIN1 **1. Vincolo esecuzione**

- Flusso batch
- Flusso avanzato
- Flusso di collegamento
- Flusso di scelta
-- Se si imposta 'M' oppure 'I', è un'azione selezionabile solo se lanciata
rispettivamente dall'interno della manutenzione oppure dall'interrogazione (tramite F10).
- Flusso di esecuzione
-- È l'azione (B£J dello stesso sottosettore) che verrà eseguita a cascata, se la prima azione si sarà conclusa positivamente.

 :  : FLD T$VIN2 **Condizioni di esecuzione**

- Flusso batch
- Flusso avanzato
- Flusso di collegamento
-- Se il flusso di collegamento è stato lanciato in modalità ridotta
(programma B£FUNG/B£FUNGA con la funzione 'ESFR' e non 'ESF') vengono trascurate le
azioni che hanno valorizzato questo campo.
Un utilizzo di questa modalità è nella generazione di ordini di produzione dipendenti a partire da un ordine master.
-- Nel flusso di inserimento dell'ordine è impostato il passo di creazione degli ordini dipendenti, che esegue, a sua volta, un flusso di inserimento ridotto.
Per evitare la ricorsione (oltre che un'incongruenza applicativa :  non si devono creare gli ordini dipendenti di un ordine dipendente), l'elemento di tabella che individua il passo di creazione degli ordini dipendenti ha questo campo impostato, in modo da essere eseguito solo nel flusso di creazione dell'ordine master.
- Flusso di scelta
- Flusso di esecuzione

 :  : FLD T$VIN3 **Condizioni di selezione**

- Flusso batch
- Flusso avanzato
- Flusso di collegamento
- Flusso di scelta
- Flusso di esecuzione

 :  : FLD T$PGM **Nome programma**
È il programma che viene eseguito in questo passo.
Flusso batch
??? Definire con che parametri viene lanciato.
Flusso avanzato/di collegamento/di scelta /di esecuzione
Deve essere un programma che riceve la lista dei parametri standard (lanciabie via £FUN2).
 :  : FLD T$ESEG **Stato esecuzione**

- Flusso batch
- Flusso avanzato
- Flusso di collegamento
- Flusso di scelta
- Flusso di esecuzione

 :  : FLD T$SWS **Indicatori esterni**

- Flusso batch
- Flusso avanzato
- Flusso di collegamento
- Flusso di scelta
- Flusso di esecuzione
--  1. carattere : 
--- Se impostato a 1, significa che l'oggetto viene creato in questa azione (ad esempio la generazione di un collo) :  all'atto del lancio l'oggetto deve essere blanks, al ritorno viene portato a video il valore della £FUNK1, impostata dal programma chiamato, in modo da poter eseguire ulteriori azioni su questo oggetto.
--- Un'altra possibilità è quella di eseguire ricerche particolari :  il programma lanciato dalla funzione chiede ulteriori informazioni e, in base ad esse, guida un programma di ricerca specifica il cui effetto è di individuare e restituire un oggetto su cui si potranno eseguire altre funzioni.
-- 2. carattere : 
Definisce come apparirà il formato video dopo l'esecuzione dell'azione : 
--- Se impostato ad 1 verrà pulito l'oggetto
--- Se impostato a 2 verrà pulita l'azione
--- Se impostato a 3 verranno puliti entrambi
--- Se impostato a 4 viene pulito l'oggetto e reimpostata l'azione originale
--- Se impostato a 5 torna al menu' precedente
-- 3. carattere : 
--- Se impostato a 1, viene chiesta conferma prima dell'esecuzione.

 :  : FLD T$PAR1 **Parametro  1**

- Flusso batch (B)
????
- Flusso avanzato/di collegamento/di scelta/di esecuzione
È la funzione con cui si esegue il programma

 :  : FLD T$PAR2 **Parametro  2**

- Flusso batch
????
- Flusso avanzato/di collegamento/di scelta/di esecuzione
È il metodo con cui si esegue il programma

 :  : FLD T$LDA1 **Parametri aggiuntivi**

- Flusso batch
- Flusso avanzato
- Flusso di collegamento
- Flusso di scelta
- Flusso di esecuzione

 :  : FLD T$RISE **Righe di separazione**

- Flusso batch
- Flusso avanzato
- Flusso di collegamento
- Flusso di scelta
- Flusso di esecuzione

 :  : FLD T$B£JP **Gruppo protezione**
Per i flussi batch e di scelta permette di specificare il gruppo di appartenenza dell'azione stessa ai fini del controllo di autorizzazione. Ciò vale se il gruppo di azioni definito in B£H è definito sotto controllo di autorizzazione.
Possiamo avere 10 gruppi di azioni definiti nella tabella B£SGF.
Ad ogni gruppo possiamo assegnare, mediante la gestione delle autorizzazioni, l'abilitazione per un utente (o gruppo di utenti).
 :  : FLD T$B£JS **Sezione Menù/Popup**
Solo per azioni appartenenti al gruppi "A-". Se impostato questo campo l'azione verrà presentata nel gruppo qui descritto. Se tale campo non viene impostato l'azione finirà sotto "azioni specifiche dell'oggetto".

* F Fly
* S Surf
* R Azioni rapide

Le azioni rapide sono quelle che stanno sotto "dashboard" nel menù e sotto il richiamo della scheda nel popup.
 :  : FLD T$B£JA **Phone**
Se impostato attiva questa funzione (se di tipo F) su un Device di Tipo Phone
 :  : FLD T$B£JB **Tablet**
Se impostato attiva questa funzione (se di tipo F) su un Device di Tipo Tablet
 :  : FLD T$B£JC **Client Loocup**
Se impostato disattiva questa funzione (sia A sia F) dal Client Loocup
 :  : FLD T$B£JD **Web**
Se impostato disattiva questa funzione (sia A sia F) dal Client Web
 :  : FLD T$B£JE **Solo interattivo**
Sui flussi oggetto indica che un'azione F non verrà eseguita se il flusso è lanciato in batch.
NOTA BENE :  senza questa indicazione un flusso batch va volutamente in CPF, e la funzione non è F(FBK....), al fine di evidenziare il problema.

