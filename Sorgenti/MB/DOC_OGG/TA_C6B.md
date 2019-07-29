# C6B - Analitica
 :  : DEC T(ST) K(C6B)
## OBIETTIVO
Definire la modalità con la quale si gestisce il dettaglio di analitica.
Un conto è di analitica se impostato nella tabella C5B.
La C6B può contenere il conto contabilie (C5B), la linea di riclassifica del conto (C5NBA) oppure un elemento di default '**'.
La modalità di risalita è : 
Conto -> Linea -> Default.
In immissione il carattere '>>' permette di andare in ricerca sulla linea (C5NBA) e sul conto(C5B).
## CONTENUTO DEI CAMPI
 :  : FLD T$DESC **Descrizione**
Descrive il conto contabile o linea di riclassifica
 :  : FLD T$C6BA **Presenta a Conferma Registrazione**
Nella gestione interattiva, alla conferma della registrazione è possibile scegliere se presentare la gestione dell'analitica secondo le seguenti modalità : 
- " "  :  La modalità viene affidata alla risalita nella tabella C52.
- "1"  :  Non presenta gestione. Se c'è un errore, segnala con la visualizzazione standard dei messaggi.
- "2"  :  Presenta la gestione solo se c'è un errore.
- "3"  :  Presenta sempre la gestione.
 :  : FLD T$C6BB **Nature**
È un elemento della tabella B£G contenente la griglia delle tre nature.
 :  : FLD T$C6BC **Destinazioni**
È un elemento della tabella B£G contenente la griglia delle tre destinazioni.
 :  : FLD T$C6BD **Formato**
Definisce la caratteristica del formato di gestione dell'analitica. Può essere completo o ridotto.
Il formato completo presta le tre nature e le tre destinazioni.
Il formato ridotto presenta tre soli campi a scelta. Il primo campo (principale) viene usato in due formati come fisso :  in altre parole viene presentato una sola volta nell'intestazione della lista (controller) e viene assunto da tutte le righe presenti.
È poi possibile scegliere se attivare lo switch tra i vari formati.
 :  : FLD T$C6BE **Disattiva costruzione automatica modello in gestione**
Se presente un modello di analitica, il sistema automaticamente in gestione, se non presenti righe, le ricostruisce.
Questo campo se valorizzato ne disattiva tale ricostruzione.
 :  : FLD T$C6BF **Suff. pgm aggiustamento costr. analitica contabilità**
È il suffisso X del programma C5GE11A_X che viene lanciato nella costruzione automatica dell'analitica. In questo programma si possono variare nature, destinazioni, importo dell'analitica in essere o decidere di non scrivere la riga stessa. Viene eseguito prima di scrivere la riga di analitica. Contiene il record dell'analitica che verrà eventualmente scritto e i nuovi oggetti o valori ricacolati dal modelllo.
 :  : FLD T$C6BG **Risalita**
È un elemento della stessa C6B utilizzato per un'eventuale risalita. Verranno ripresi tutti i campi non valorizzati con una R nella loro intestazione. L'elemento  scelto non potrà a sua volta contenere una risalita.
 :  : FLD T$C6BH **Suffisso programma aggiustamento funzioni analitica**
È il suffisso X del programma C5C5L_X eseguito alla fine del programma standard C5C5L0 che gestisce tutte le funzioni di conto/struttura/modello dell'analitica. Contiene tutte le stesse informazioni dell'esecuzione della COPY £C5L. È quindi possibile modificarne l'output standard della £C5L.
 :  : FLD T$C6BI **Modello da conto**
Un modello è generalemente ricostruito a partire dal conto in essere. Se presente questo campo il modello viene ricostruito a partire dal conto qui inserito. Modello derivato. (Questa risalita è gestita nel programma specifico del modello)
 :  : FLD T$C6BJ **Suffisso programma modello**
È il suffisso 'X' dei programmi specifici C5C5LM_X e G5C5LMX che rispettivamente scandiscono e gestiscono il modello del conto in essere. Se non presente viene assunto il suffisso di defalut 'A'
 :  : FLD T$C6BK **Parametro programma modello**
È il parametro passato al programma specifico del modello.
 :  : FLD T$C6BL **Accetta solo valori modello**
Definisce se accettare per i campi di analitica solo i valori presenti nel modello
 :  : FLD T$C6BM **Non Caricare modello**
Se valorizzato questo parametro inibisce il caricamento automatico dei parametri del modello. In questo caso il modello serve solo per controllare i dati inseriti).
