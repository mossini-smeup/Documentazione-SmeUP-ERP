Lo scopo di Build.up è sostanzialmente uno :  definire un oggetto in ogni sua parte attraverso un
meccanismo di domande e risposte.
Le funzionalità di base di Build.up dovranno pertanto essere le seguenti : 

- Definizione di un questionario
   In Build.up un questionario è denominato configuratore.
   La costruzione avviene utilizzando LoocUp.
- Compilazione di un questionario
   La compilazione di un questionario è possibile sia in LoocUp sia da internet.
   La compilazione ha il compito di raccogliere le risposte date dall'utente e, dopo averle
   controllate, memorizzarle nel modo opportuno.
   Un configuratore eseguito completamente dà luogo ad un oggetto chiamato configurazione
   (concettualmente un questionario compilato).
- Memorizzazione della configurazione :  viene salvata nel file CFVARI0F oppure nel B£MEDE0F, che viene
   usato come contenitore di tutte le configurazioni realizzate.
   Sono possibili due metodi di salvataggio :  con progressivo automatico e con chiavi definite nella
   B£G. Se la chiave è un progressivo automatico allora la prima chiave di configurazione deve
   essere la tabella CFC subsettore associato al questionario.
   Il salvataggio creerà un nuovo record nella tabella CFC e verrà memorizzata la descrizione
   fornita dall'utente.
   Con questo metodo di gestione della configurazione viene gestito anche il LOCK è il livello

