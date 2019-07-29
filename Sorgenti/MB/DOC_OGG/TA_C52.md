# C52 - Impostazioni base analitica
 :  : DEC T(ST) K(C52)
## OBIETTIVO
Definisce i parametri generali relativi al Modulo di Contabilità analitica.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM **Elemento**
È un elemento fisso.
 :  : FLD T$C52A **Analitica attiva?**
Se impostato (valore '1'), viene attivata la gestione della contabilità analitica. Lasciandolo bianco viene inibita tale gestione.
 :  : FLD T$C52B **Gestione Qtà e UM.**
Se impostato (valore '1'), viene attivata la gestione di rilevazione delle quantità. Lasciandolo bianco è attiva solo la rilevazione dei valori.
 :  : FLD T$C52D **Presenta a Conferma Registrazione**
Nella gestione interattiva, alla conferma della registrazione è possibile scegliere se presentare la gestione dell'analitica secondo le seguenti modalità : 
- " " o "1" :  Non presenta gestione. Se c'è un errore segnala con la visualizzazione standard dei messaggi.
- "2"       :  Presenta la gestione solo se c'è un errore.
- "3"       :  Presenta sempre la gestione.
 :  : FLD T$C52E **Riclassifica Analitica**
Definisce la riclassifica dei conti contabili usata per la risalita nella costruzione delle righe di analitica.
 :  : FLD T$C52F **Salvataggio in uscita set'n'play modelli analitica**
Se attivo richiede in uscita dal set'n play analitica, se si vogliono salvare i modelli in un file di appoggio C5MOAIN0F_S. È utile nel caso venga pulito il C5MOAN0F per eventuali conversioni.
 :  : FLD T$C52G **Data di riferimento**
Definisce le risalite predefinite per valorizzazione della data competenza delle righe di analitica.
Può assumere i seguenti valori : 
- " "=Data competenza della registrazione in inizializzazione (solo alla creazione della riga di analitica)
- "1"=Data registrazione in inizializzazione (solo alla creazione della riga di analitica)
- "2"=Data registrazione fissa (l'allinamento fara data registrazione/riga analitica viene mantenuta
      per tutta la vita della riga di analitica)
 :  : FLD T$C52H **Data Attivazione**
Definisce la data registrazione a partire dalla quale l'analitica risulta attivata.
 :  : FLD T$C52L **Exit Riclassifica**
È il suffisso del programma di exit per la determinazione della riclassifica nella scheda analitica.
Innesca il richiamo del programma **C5C6M0_x** (x è il suffisso).
Tale programma viene richiamato dall'api £C6M.
Il prototipo del programma è costituito dal sorgente C5C6M0_X.
