**Sistemati**
   1. SMESRC/CQSRC va in errore  su CQNS12...
      _7_(Mancava libreria ACGGAA)
   2. Entrando in definizione schemi, se si modifica un record va in errore. (Cannot focus a disabled or invisible window)
      _7_Emulatore
   3. Entrando in definizione schemi, se si modifica un record va in errore. (Access violation SmeUiClt)
      _7_Emulatore
   4. Se tento di aprire un filtro esterno mi dice superato numero massimo sessioni.
      _7_Errato Richiamo XML iniziale
   5. Se si effettua una scelta emette l'errore "Invalid Variant  Type Conversion" in Gestione Filtri.
      _7_Emulatore
   6. Nei formati video nei quali vengono "eliminate" o "riclassificate" le informazioni presenti sulle prime 2 righe del DSPF, si potrebbe alzare di 2 righe tutti i campi successivi.
      _7_Se non presenti lo fa
   7. Se un PC è configurato con "Caratteri Grandi" i campi di 1 byte non sono modificabili
      _7_Su Emulatore
   8. Ordinare i comandi in ordine crescente
      _7_Su Emulatore
   9. Sistemare la firma dei DSP come x tutti gli altri oggetti.
      _7_JAXML1A
  10. Inserire nell'XML EdtCde e EdtWrd
      _7_JAXML1A
  11. La finestra di un subfile non contiene le informazioni dimensionali posizionamento corrette, tasti funzionali descrittivi
      _7_JAXML1A
  12. Accesso facilitato alle funzioni Articolo, Apro gli attributi dell'oggetto ed ottengo vari errori :  - Interrogando l'attributo non mostra nulla
      _7_Emulatore
  13. Gestione Schemi, Non viene documentato il tasto funzionale F06=Nuovo Schema
      _7_JAXML1A
  14. Se il valore del campo contiene caratteri speciali \/ : *?"<>| va in errore il retrieve delle icone
      _7_Emulatore
  15. Aggancio a Gestore Java Stack
      _7_Emulatore
  16. Se il formato "Window" non porta in se la dimensione della finestra ma la deriva da un'altro formato, non riesce a definire la dimensione   della finestra
      _7_JAXML1A
  17. Corretto visualizzazione Descrizione Tasto Funzionale su F13=Parzializzazione
      _7_Emulatore
  18. Gest.Distinte :  Se si passa dal videata rid. a videata compl. da errore '   ' is not a valid floating point value!!!
      _7_L'emulatore del subfile non gestiva campi costante
  19. Errore di schiera durante l'elaborazione dell'EDTCDE
      _7_JAXML1A
  20. Attivata gestione Campi ND su Subfile
      _7_Emulatore
  21. G08 : Vengono visualizzati 2 volte i tasti funzionali F12 e F13.
      _7_OkAS
  22. Analisi Attributi Articolo :  Nell'XML non è presente la dimensione della finestra
      _7_Ok
  23. Paginazione talvolta non funziona su subfile
      _7_Emulatore
  24. Posizionamento Cursore se manca PC su Subfile e se SFLRRN non è il primo record visualizzato sulla pagina.
      _7_Emulatore
  25. L'Evidenziazione dei tasti funzionali presenti nella bottoniera di destra si traduce nel pulsante con sfondo grigio anzichè giallo.
      _7_Emulatore
  26. Attivata Gestione Campi di Tipo CommandText
      _7_Emulatore
  27. Attivata gestione Finestre con posizionamento variabile
      _7_Emulatore
  28. I campi di tipo 'P' (Programma) vengono automaticamente convertiti in tipo 'H' (Hidden)
      _7_Emulatore
  29. Il Tasto F10 sospende l'esecuzione del programma aprendo il "System Menu del Form"
      _7_Emulatore
  30. Subfile, Nell'Xml di una griglia l'attributo Sfp (SFLPAG) è moltiplicato 10
      _7_JAXML1A
  31. Gestione Cambi In un attributo xml sono contenuti dei doppi apici (") Sostituire nell'xml i doppi apici (") con la stringa "ecomm"quot; o eliminare i doppi apici in favore di apici singoli Per testare :   Dati di base/Altri/Gestione Cambi Opzioni :  Aggiunta Gestione :  E Tipo cambio :  E  Divisa :  DEM Data divisa :  05/05/2002 <INVIO> <F08=Progressione>
       _7_JAXML1A
  32. Convertitore_7_Utilizzata la Key INDTXT JAXML1A Creare nuove key da attivare sui formati video utilizzando la chiave TEXT. La nomenclatura dovrà seguire le seguenti logiche : 
      da 1 a 1 £
      da 2 a 4 oggetto
      da 5 a 7 contesto
      ES : 
     **£CMDTXT **Variabile che contiene informazioni descrittive dei tasti comando.
     **£SFLINT **Intestazione di subfile, deve essere seguita dalla costante o dal riferimento del campo contenente l'intestazione che deve essere preceduto dal carattere**"ecommerciale"**
                    £SFLINT Scelta
                    £SFLINT [_W$INT1]
                    £SFLINT [_W$TITO : 3 : 5], dalla terza posizione del campoW$TITO per lunghezza 5
     **£OGGHID **Il campo o costante a cui si riferisce è nascosta, se è un campo deve essere trattato come "HIDDEN", se costante ignorata
     **£FMTINT **Formato contenente le intestazioni di subfile
     **£TESTO  **Il campo o costante a cui si riferisce non è da considerasi un'intestazione di colonna.
                 **x**Sta per un progressivo
     **£ACTxx  **Campo dell'azione
     **£ACTLSTxx**Lista delle azioni
     **£OPZxx  **Campo dell'opzione
     **£OPZLSTxx**Lista delle opzioni
     **£BUTxx  **Campo del bottone
     **£BUTLSTxx**Lista del bottone
     **£TABxx  **Campo del tab
     **£TABLSTxx**Lista dei tab
       _7_Ok sia su AS che su emulatore
  33. Funzioni Gestione Tempi B£UIA0 Perdeva stack SFL Se nel subfile di Modifica si inseriscono '?' su tutti gli elementi l'emulatore si comporta diversamente dal 5250.
      Per Testare :  Dati di base/Cicli/S P Tempi di una fase
                Funzione :  GE
                Metodo :  02
                Altre Condizioni :  X  <INVIO>
                 Su tutti i campi del subfile :  ?
                  <INVIO> e osservare la diversità di comportamento
      _7_Ok AS/400
  34. In Scelta Ordinamenti Stampa Articoli se selezionati ordinamenti viene sempre richiesto anche il livello di totalizzazione (su AS/400 non lo fa). Verificare Buffer in ricezione AS
      _7_Dopo le ultime modifiche il problema non si ripresenta
  35. Le "ecommerciali" presenti in un DSPF devono essere scritte nell'XML come "ecommerciale"amp;
      _7_Ok AS/400
  36. Definizione Periodicità
      Dalla schermata di dettaglio, dando <invio> il programma RPG
      va in errore
      _7_Ok AS/400
  37. Non impostare icone oggetto se tipo oggetto='NR' o 'NP'
      _7_Ok Emulatore
  38. Manca l'apertura alla Memorizzazione Dati Video (MDV)
      _7_Ok Inserito su Xml e Inserito (provvisorio?) su emulatore
  39. Vari problemi nel riconoscere i tasti funzionali presenti nei
      subfile.
      _7_JAXML1A
  40. Eccezioni Calendario, Il campo W$MESG viene trattato come Message
      _7_JAXML1A, deve essere un carattere per divenire Message
  41. Stampa Disponibilità Risorse, non veniva convertito perchè
      il testo del membro conteneva un apicino.
      _7_JAXML1A
  42. La visualizzazione Icone Oggetto, su form già esistenti,
      funzionava solo alla prima emissione del formato video
      _7_Emulatore
  43. L'emulatore va in errore se non descritto alcun tasto funzionale
      _7_Emulatore
  44. Attivata Gestione OptionList su Subfile
      _7_Emulatore
  45. Attivata Gestione Scelta Record Subfile mediante doppioclick
      _7_Emulatore
  46. Tasti Funzionali
      In alcune finestre non sono descritti i tasti funzionali
      (Es : G08 per Tasti Funzionali (F24))
      ES :  Dati Pianificazione Articolo/Magazzino (B£CRI0)
      I Tasti funzionali sono mappati erroneamente (F01=Window, ...) ed
      alcuni tasti funzionali sono mancanti
      Per Testare :  Dati di base/Articoli/Accesso Facilitato alle funzioni
                   Articolo : A01; Scelta : 6; Pianificazione : 1 <INVIO>
      ES :  Analisi Attributi Articolo (B£OAV2L)
          I Tasti funzionali sono mappati erroneamente (F02=F24>>>, F01=F12)
      _7_JAXML1A
  47. Impostazioni di Visualizzazione in Confronto Distinte
      Le costanti con apici talvolta non contengono gli apici
      Per Testare :  Dati di base/Distinta/Confronto Distinte, F17
      _7_JAXML1A
  48. Modificata Gestione Shortcut per visualizzazione Xml, Performance
      Configurazione, Configurazione; aggiunta in System Menu
      _7_Emulatore
  49. Interrogazione Campi Tabelle
      Nel subfile è presente una colonna di "costanti" DM'?) che in
      5250 non è presente
      _7_JAXML1A, Omessi i valori controllati da SDA "key VALUES"
  50. Interrogazione Settori Tabelle
      Non vengono eseguiti i tasti funzionali **Perchè a programma torna
      un indicatore rimappato dalla SDA Es :  F03=indicatore 03, noi
      ritornia £F03 o KC.
      _7_B£UT24A
  51. Aggiunta Gestione Oggetti "Emulatore" e "Programma"
      _7_Emulatore
  52. Su Emulatore se premuto CTRL per abilitare/disabilitare icone
      oggetto, occorre fare un "refresh" del subfile
      _7_Emulatore
  53. Nei formati deriva i condiz. di tasti funzionali da ogni formato.
      Nei formati se deriva i comandi dal livello file deve verificare
      la loro assenza a livello record
      _7_JAXML1A
  54. Corretta Paginazione su Subfile se il campo SflRcdNbr conteneva
      caratteri speciali (£,$,§)
      _7_Emulatore
  55. Subfile
      Gestione SflEnd :  se abilitata paginazione viene definito un tasto RUP
      Condizionarlo sulla base dell'indicatore di SFLEND.
      _7_JAXML1A
  56. Generale
      Non tutti i tasti funzionali vengono convertiti da DSPF a XML
      _7_JAXML1A
  57. Distinta Base, Le Optionlist dei due campi di opzione
      sono "mischiate"
      _7_Così anche sui campi AS/400
  58. Generale
      Mancano le seguenti informazioni : 
      1) Nome del sistema
      2) Nome del programma
      3) Nome dell'unità
      4) Nome dell'utente
      _7_Emulatore
  59. Generale
      Rendere JACACH0F a len variabile
  60. Se interrogo le tabelle x ! o x ? mi dice che la lista è ordinata per
      Descrizione ( attenzione è solo il titolo sbagliato ).
      _7_Emulatore
  61. SubFile
      Abilitata gestione tasto destro su campo subfile
      _7_Emulatore
  62. G18
      Completata Gestione G18
      _7_Emulatore
  63. Modificata gestione Griglie. L'ultima colonna si ridimensiona
      contemporaneamente al ridimensionamento della griglia
      _7_Emulatore
  64. Le /Copy con inclusi gli operatori EXFMT non funzionano.
      _7_Gestite le /copy £VS_C e £MOV1D_$C in B£UT24A
  65. G18
      Corretto errore su mancata cancellazione delle voci di popup
      nel caso di oggetti multipli
      _7_Emulatore
  66. Oggetti "Variabili"
      Corretto errore in gestione oggetti "variabili" in campi hidden
      Corretto errore di presentazione nell'hint se non definita
      lunghezza nella definizione dell'oggetto variabile
      _7_emulatore
  67. Subfile
      Le OptionList riferite a campi protetti davano errore
      _7_emulatore
  68. Subfile
      Aggiunta Gestione Alta Intensità Campi
      _7_Emulatore
  69. Popup Oggetti
      Corretto errato richiamo a Popup oggetti
      _7_Emulatore
  70. Tasti Funzionali
      Eliminata Stringa 'F24 >>'
      _7_JAXML1A
  71. Intestazioni Subfile
      Suddivisione stringa unica di intestazione sulle colonne sotto
      stanti. L'espressione viene espressa nel formato : 
      [ecommamp;<campo> : <inizio> : <lunghezza>]|........
      N.B. il pipe '|' indica una separazione di riga
      _7_JAXML1A
  72. Errato posizionamento finestra
      Non veniva reinizializzata la coordinata Y nel caso di sflctl
      _7_JAXML1A
  73. Invio talvolta non viene recepito
      Aggiunta impostazione £ENTER
      _7_£UIA
  74. Monitorato errore se caratteri non validi in XML ed invio mail
      _7_Emulatore
  75. Intestazioni Subfile
      Gestite intestazioni su righe multiple e nuova sintassi
      _7_Emulatore
  76. Flicker in aggiornamento campi input subfile
      Eliminato Flicker nascondendo il campo fino alla sua
      visualizzazione definitiva
      _7_Emulatore
  77. Alcuni Tasti Funzionali non hanno descrizione
      Errore dovuto alla presenza di tasti senza caption e quindi
      ridefiniti "invisibili". Adesso vengono mappati in una barra
      senza pulsanti
      _7_Emulatore
  78. La visualizzazione degli XML avviene secondo la mappatura
      del programma Windows
      _7_Emulatore
  79. Campi Packed in Subfile
      Diversi Subfile contengono l'immagine del record!
      Es :  Navigazione su Documenti V5FUC0L
      Aggiunta Conversione di x'1F' e x'0A' nel formato '[*nnn*]'
      _7_Emulatore
  80. Non funziona la paginazione se non ci si trova in un Subfile
      _7_Emulatore
  81. Paginazione formati non subfile
      _7_Emulatore, B£UT24A
  82. Attributi Video
      Se viene ritornato all'AS/400 un record di subfile occorre
      riempirlo ancora con gli attributi video eliminati in favore
      dei blank
      _7_Emulatore
  83. Icone Oggetti Subfile
      L'attivazione della visualizzazione icone su subfile è stata
      separata dall'attivazione della visualizzazione icone campi
      _7_Emulatore
  84. Configurazione
      Tutti i parametri di configurazione sono gestiti esternamente
      _7_Emulatore
  85. Reload Configurazione
      Attivato Ricaricamento Configurazione
      _7_Emulatore
  86. Invio Messaggi di Errore
      Aggiunta descrizione Messaggio Errore del Parser Xml
      _7_Emulatore
  87. Errore se esecuzione multipla
      Aggiunto controllo via Mutex per esecuzione singola
      _7_Emulatore
  88. Se manca il file di configurazione l'emulatore va in crash
      Risolto
      _7_Emulatore
  89. La chiusura da utente ('X') della finestra viene interpretata
      come Invio
      Adesso viene interpretato come F3 o F12. Se non definiti
      la finestra rimane visibile
      _7_Emulatore
  90. Eliminare gli asterischi dal titolo della finestra
      _7_Emulatore
  91. Campi Numerici Negativi
      Nel caso di campo a video con segno, viene ritornato il valore
      negativo zonato, causando un invalid floating point value
      _7_Emulatore

_2_ 
_2_                   RILASCIO BETA VERSION 1.0
_2_ 

  92. La visualizzazione dei documenti XML avviene sempre tramite
      Internet Explorer.
      _7_Emulatore (Il verbo "open" dell'estensione XML rimane sempre
      _7_mappato a iExplore.exe. Modificato l'emulatore per utilizzare
      _7_il verbo di default
  93. Aggiunto Menu Popup anche su campi non "Oggetto"
      _7_Emulatore
  94. Aggiunta Azione di default definita in Popup se click su Icona
      Oggetto
      _7_Emulatore
  95. Aggiunta Deregistrazione Emulatore da Stack se *ERR o *EOF
      (*EOF solo se prima frame)
      _7_Emulatore
  96. Aggiunta Gestione Intestazioni Multilinea Miste
      (Parte Variabili/Parte Costanti)
      _7_Emulatore
  97. Corretta Chiusura Finestre Emulatore se ricevuto *ERR
      _7_Emulatore
  98. Unificate Tipo e Algoritmo icone Oggetti con Java
      _7_Emulatore
  99. Aggiunta Funzione Completamento Automatico per memorizzazione
      ultimi valori oggetto
      _7_Emulatore
 100. Implementata keyword SFLINZ
      _7_Emulatore, JAXML1A, B£UT24A
 101. Implementato SflCsrLoc
      _7_Emulatore
 102. Migliorata Gestione Intestazioni Subfile
      _7_JAXML1A
 103. Ritorno informazioni posizionamento cursore
      Attivate a livello di record le Key
      CLocR = RTNCRSLOC a livello Record
      CLocC = RTNCRSLOC a livello Campo
      CLocP = RTNCRSLOC a livello Pozsizionamento all'interno del campo
      _7_JAXML1A, Emulatore
 104. Prodotta la tabella JA*IS contenente il nome del formato video
      avente un subfile senza intervento esterno (chiave £SFLINT)
      _7_?
 105. Aggiunta evidenziazione Campi di Input
      _Emulatore_
 106. Corretta Emissione Popup su Campi di Input e Icone
      _Emulatore_
 107. Modificato Ridimensionamento Colonne Subfile
      _7_Emulatore
 108. Aggiunta Possibilità di specificare Dimensione Font
      _7_Emulatore
 109. Eliminata visualizzazione dei decimali nelle griglie se
      il campo vale 0
      _7_Emulatore
 110. Aggiunto funzionalità doppio click=Enter su subfile che
      non hanno un campo di input
      _7_Emulatore
 111. Modificata funzionalità di doppioclick=Enter su campi di input
      ora è abilitata solo se i campi sono "ReadOnly"
      _7_Emulatore
 112. Se presenti più subfile nello stesso video perdeva il puntamento
      al subfile.
      _7_B£UIA0
 113. E' possibile salvare la dimensione/posizione della finestra
      salvando anche la dimensione della griglia contenuta
      _7_Emulatore
 114. Se Invio di Xml G18 non viene più richiesto il Display File
      _7_Emulatore
 115. Attivata nuova Key "£TESTO" da utuilizzare nelle righe superiori
      al subfile per idicarne la non appartenenza
      _7_JAXML1A
 116. Aggiunta Visualizzazione Nome Campo su Hint
      _7_Emulatore
 117. Aggiunta Funzionalità di Visualizzazione/Cancellazione Cache
      Formati Video
      _7_Emulatore
 118. Aumentata Lunghezza Colonne Subfile (+1 Carattere) e allineata
      lunghezza colonne alla matrice
      _7_Emulatore
 119. Aggiunta Visualizzazione Oggetto OJ*FILE in intestazione
      _7_Emulatore
 120. Inibita possibilità di modifica campi protetti
      _7_Emulatore
 121. Modificata Routine di Comunicazione per effettuare richieste di
      servizi senza bisogno di ricevere necessariamente una risposta
      (i.e. Richiamo Editor RPG)
      _7_Emulatore
 122. Migliorate performance nella gestione degli attributi video
      a RunTime
      _7_Emulatore
 123. Corretto Errore su mancato aggiornamento buffer video nel
      caso di aggiornamento campo di input subfile di un carattere
      attraverso Popup
      _7_Emulatore
 124. Caratterizzato con il colore "verde" i campi di tipo "NR"
      _7_Emulatore
 125. Implementata Gestione Edit Code e Edit Word
      _7_Emulatore e JAXML1A
 126. Corretto Errore se nella definizione del DSPF non venivano
      specificati gli indicatori in sequenza, ma venivano lasciati
      degli spazi in bianco (ES :  01   N99 in luogo di 01N99)
      _7_Emulatore
 127. Modificata Gestione Buffer Subfile e Stack Programmi per
      Considerare anche il caso di stesso File Video gestito da
      più programmi RPG ricompilati (es :  G18 in contabilità)
      _7_Emulatore
 128. Gestito Allargamento automatico formati che contengono il
      solo subfile. L'allargamento avviene sia a livello della
      griglia che sul form.
      _7_Emulatore
 129. Inserita gestione Tabsheet
      _7_Emulatore
 130. Inserita Gestione Bottoni (Button e ButtonList)
      _7_Emulatore
 131. Modificata Gestione Bottoni per spostare il bottone in modo
      conforme rispetto all'eventuale rimappatura del campo a cui
      è legato
      _7_Emulatore
 132. Aggiunto Monitoraggio Errori in Refresh Buffer Video ed in
      assegnazione valore a campo del form per evitare il riavvio
      di Loocup
      _7_Emulatore
 133. Corretto EditCode per campi numerici di tipo data nel caso
      in cui il campo data sia vuoto
      _7_Emulatore
 134. Nel merge dei tasti funzionali definiti in un formato
      passato in Write, adesso vengono controllati anche gli
      attributi ND e NV.
      _7_Emulatore
 135. Corretto errore nella gestione dei campi CommandText.
      Nel caso in cui un unico campo contiene la descrizione
      di più tasti funzionali adesso i tasti vengono correttamente
      separati
      _7_Emulatore
 136. Inserita funzionalità di gestione corretta dei tasti
      funzionali nella caso sia descritti in un campo di tipo
      Commandtext in un formato passato in write e nello stesso
      formato non sono stati definiti come CFxx o CAxx
      _7_Emulatore
 137. Modificati Direttori per logging performance ed errori
      _7_Emulatore
 138. Inserita gestione subfile emessi in write
      _7_Emulatore
 139. Eliminata gestione subfile emessi in write
      (per la sua riattivazione occorre inserire nell'XML del DSPF
      anche un attributo OVERRIDE)
      _7_Emulatore
 140. Eliminato errore "List Index Out of Bouds"
      _7_Emulatore
 141. Corretta Gestione Combobox se modifica del suo valore e non
      scatenato un evento "OnExit" non veniva aggiornato correttamente
      il valore del campo "Maskedit" a lui legato
      _7_Emulatore
 142. Eliminata Forzatura Assegnazione Tasto Funzionale F12
      _7_Emulatore
 143. Eliminato Messqaggio di Errore in popup se non viene ricevuto
      un XML valido da AS/400 (il popup veniva nascosto da Java e non
      era visibile)
      _7_Emulatore
 144. Aggiunta Gestione DoppioClick nel ListBox di memorizzazione
      ultimi valori
      _7_Emulatore
 145. Aggiunta Evidenziazione (con rettangolo rosso) anche dei combobox
      _7_Emulatore
 146. Modificata gestione intestazione finestre :  ora è possibile
      specificare piu' intestazione da concatenare; risolto inoltre
      errore nella mancata pulizia dell'intestazione finestre nel caso
      di riemissione della stessa
      _7_Emulatore
 147. Aggiunta Possibilità di selezionare l'elemento vuoto di un
      "ComboBox" premendo "BarraSpaziatrice"
      _7_Emulatore
 148. I tasti funzionali di tipo CommandText presenti in un formato
      di cui effettuare il merge, adesso consentono la derivazione
      non solo del testo ma anche dell'attributo di Reverse Image
      sul corrispondente Tasto Funzionale del Control
      _7_Emulatore
 149. Le costanti adesso vengono ridimensionate sulla base del loro
      contenuto così da lasciare più spazio alle icone. Ciò potrebbe
      avere degli effetti collaterali nella gestione dei campi
      sovrapposti
      _7_Emulatore
 150. Viene adesso gestito il titolo di una finestra anche se la sua
      definizione si trova in un formato di intestazione emesso
      precedentemente in write (se il formato di exfmt è un sflctl)
      _7_Emulatore
 151. L'evidenziazione del campo su cui è attivo il fuoco è attiva
      solo se il campo è disponibile all'input
      _7_Emulatore
 152. La "colorazione" dei campi di input numerici avviene solo se
      il campo è disponibile all'input
      _7_Emulatore
 153. Spostati Subfile, precedentemente il subfile veniva emesso
      1 riga più in basso rispetto al 5250
      _7_Emulatore
 154. Aggiunta Gestione EdtCde nei campi di Output
      _7_Emulatore
 155. I campi presenti nel piede delle videate contenenti un Subfile
      vengono adesso ancorati al bordo inferiore della finestra,
      per evitare che il subfile li ricopra
      _7_Emulatore
 156. Corretto Errore su OnHint di un'Icona. Il testo era "paddato" a 1024
      caratteri
      _7_Emulatore
 157. Aggiunta Memorizzazione Valori Recenti anche per campi non "oggetto"
      (basato sul nome del campo)
      _7_Emulatore
 158. Attivato Panning Automatico su campi di input in Subfile
      _7_Emulatore
 159. Evidenziata Colonna Opzione
      _7_Emulatore
 160. Aggiunta Possibilità di Richiamare Azioni non 5250 da Azione Default
      (Click su Icona)
      _7_Emulatore
 161. Aggiunto Monitoraggio se errore in creazione campo video
      _7_Emulatore
 162. Velocizzata (anche se di poco) creazione componenti video
      _7_Emulatore
 163. Definito limite minimo per numero di righe di un subfile allineato alla
      finestra
      _7_Emulatore
 164. Corretto errore nell'ancoraggio dei componenti al bordo inferiore della
      finestra
      _7_Emulatore
 165. Monitorato errore se Xml del Popup errato
      _7_Emulatore
 166. Tentativo di monitoraggio dell'errore se "Out of System Resources"
      (da collaudare)
      _7_Emulatore

_2_ 
_2_                   RILASCIO BETA VERSION 2.0
_2_ 

 167. Ottimizzato e Migliorato Gestione Memoria
      _7_Emulatore
 168. Gli Attributi RI e HI vengono ora visualizzati sul subfile
      anche se la cella non è di input
      _7_Emulatore
 169. Modificato Dimensione Griglia Subfile per averla coerente
      al numero di righe presenti in SFLPAG indipendentemente
      dalla dimensione del carattere
      _7_Emulatore
 170. Modificata Gestione tImageList per Tasti Funzione
      Adesso viene creata una ImageList all'apertura del programma
      (Sperando così di evitare l'errore "Out of System Resources")
      _7_Emulatore
 171. Corretto Errore nell'input su Subfile di dati numerici con
      picture (con particolare riferimento alle date)
      _7_Emulatore
 172. Inibito Inserimento valori alfanumerici da popup in campi
      numerici
      _7_Emulatore
 173. Aggiunta Gestione Instanze Multiple
      _7_Emulatore
 174. Aggiunta Gestione Sessioni Multiple
      _7_Emulatore
 175. Reso Configurabile la visualizzazione della riga di evidenziazione
      della selezione subfile
      _7_Emulatore
 176. Corretto Problema nel posizionamento nei campi di input di subfile
      nel caso in cui i campi fossero protetti (solo posizionamento dopo
      il cambiamento di riga)
      _7_Emulatore
 177. Modificata Gestione Icone per adeguarla al rinnovato standard
      _7_Emulatore
 178. Corretto Errore posizionamento Finestre su Sessioni Multiple
      _7_Emulatore
 179. Inserite Icone su Popup
      _7_Emulatore
 180. Visualizzati Hints in StatusBar
      _7_Emulatore
 181. Corretto Errore su non visualizzazione del Sottomenu del System Menu
      _7_Emulatore
 182. Uniformato Colori di tutti i componenti del Form
      _7_Emulatore
 183. Modificato Listbox selezioni per uniformare Font
      _7_Emulatore
 184. Ottimizzata Gestione Cache Formati Video
      _7_Emulatore
 185. Modificato Posizionamento Cursore su Subfile. Ora ignora i posizionamenti
      su pagine diverse da quella correntemente visualizzata
      _7_Emulatore
 186. Corretto errore di non visualizzazione campi di input subfile se riemissione
      e riposizionamento sul primo record
      _7_Emulatore
 187. Aggiunta evidenziazione riga subfile mediante Frame Blu se Cfg_MarkSelectedRow
      =No
      _7_Emulatore
 188. Corretto problema di visualizzazione campi di input su subfile a causa di
      refresh continuo della griglia. Errore introdotto nell'ultima versione
      _7_Emulatore
 189. Aggiunta gestione degli attributi BL e UL su campi di Output del Subfile
      _7_Emulatore
 190. Lo spostamento tra record di subfile determina adesso la selezione
      automatica del campo di input
      _7_Emulatore
 191. I campi stringa non vengono più trimmati a destra
      _7_Emulatore
 192. Aggiunto abbozzo di gestione immagine Sistema,Ambiente,Utente
      _7_Emulatore
 193. Aggiunta Specifica Tasti Funzionali (Ctrl-Alt-Shift) Premuti in richiamo Popup
      ed in richiamo Azione
      _7_Emulatore
 194. Corretto disallineamento buffer video dopo richiesta Action Esterne forzate da RPG
      _7_Emulatore
 195. Corretto Fuoco Finestra quando ripristinata
      _7_Emulatore
 196. Inserita Invio Frame Richiesta Informazioni Inizializzazione
      _7_Emulatore
 197. Corretto mancata attribuzione oggetto a campi subfile
      _7_Emulatore
 198. Introdotta cancellazione contenuto campo se all'atto del fuoco sono contenuti
      solamente spazi per facilitare l'input con posizionamento mediante mouse
      _7_Emulatore
 199. Modicata visualizzazione Icone campi di input se campo legato a subfile
      non è compito del maskedit la visualizzazione dell'icona
      _7_Emulatore
 200. Corretto ridimensionamento griglia nel caso in cui l'Header Bar abbia  una
      Scroll Bar all'atto del collocamento dei componenti e che tale scrollbar non
      fosse più presente (probabilmente a causa di un refresh) all'atto della
      visualizzazione del form. L'effetto visibile era una griglia con l'ultima
      riga vuota nonostante ci fossero ulteriori record
      _7_Emulatore
 201. Inibita possibilità di visualizzazione multipla stesso tasto funzionale.
      (Prima di aggiungere un tasto funzionale viene adesso controllata la sua
      eventuale precedente esistenza)
      _7_Emulatore
 202. Aggiunta Gestione FunctionBar
      _7_Emulatore
 203. Inibito Click su Immagini Sistema,Ambiente,Utente
      _7_Emulatore
 204. Corretto errore AV in fase di distruzione FunctionBar
      _7_Emulatore
 205. Inserita Gestione Shortcuts un FunctionButton
      _7_Emulatore
 206. Inserita Gestione Avanzamento Record Automatico
      _7_Emulatore
 207. Corretto Ordine di Posizionamento Bottoni FunctionBar
      _7_Emulatore
 208. Aggiunta Gestione Sostituzione Contenuto Campi nelle azioni di FunctionBar
      _7_Emulatore
 209. Modificata gestione popup per inibire la selezione di opzioni relativa a
      campi protetti su subfile
      _7_Emulatore
 210. Corretta imperfezione nella gestione Tasti Funzionali. Se adesso un tasto
      funzionale viene definito due volte nell'XML e non presenta un testo
      nella seconda definizione, ciò non comporta più la sua mancata visualizzazione
      _7_Emulatore
 211. Modificata Memorizzazione Gestione Visualizzazione Icone Subfile.
      _7_Emulatore
 212. Corretto errore nella memorizzazione degli attributi video runtime su subfile
      (Se veniva ricevuta una videata senza attributi runtime subfile, venivano
      eliminati gli attributi precedentemente memorizzati)
      _7_Emulatore
 213. Modificata la logica con la quale venivano richiamate le "azioni" (es :  funzioni
      di popup, g30 da RPG, etc...). Ora non viene più costruita la stringa, ma viene
      inviata direttamente la stringa ricevuta.
      _7_Emulatore
 214. Aggiunto in configurazione possibilità di abilitare/disabilitare la gestione
      dei combobox (OptionsInCombo)
      _7_Emulatore
 215. Nella visualizzazione dell'errore nella StatusBar viene adesso cambiato il
      colore per evidenziarlo meglio
      _7_Emulatore
 216. Aggiunta Gestione dell'azione di default alternativa (nel caso in cui il
      campo non contenga un valore)
      _7_Emulatore
 217. Aggiunti due Campi nel Documento Xml di configurazione nella sezione ObjectActions
      per attribuire un Codice alle "Azioni" configurate e poter così definire un codice
      Azione alternativa (se il campo è vuoto)
      _7_Emulatore
 218. Disabilitato SearchListBox nei campi presenti nell'HeaderBar
      _7_Emulatore
 219. Modificata gestione Avanzamento Automatico Record (adesso viene richiamata
      automaticamente al riempimento del campo)
      _7_Emulatore
 220. Inibito Doppio Click su intestazione Subfile
      _7_Emulatore
 221. Modificata Gestione Cache DSPF :  ora è per Sistema/Ambiente
      _7_Emulatore
 222. Se riemissione di un form già presente, e nessun PC attivato, il fuoco viene
      posizionato sul primo campo di input
      _7_Emulatore
 223. Nell'Header Bar vengono adesso nascosti i pannelli contenenti campi non
      visualizzati
      _7_Emulatore
 224. Aggiunto Controllo sull'esistenza di finestra per evitare il messaggio sporadico
      "List Index out of bounds" in chiusura di una sessione
      _7_Emulatore
 225. Aggiunto Monitoraggio AV in fase di Abilitazione/Disabilitazione form
      per cercare di risolvere gli AV in chiusura applicazione probabilmente
      dovuti da problemi di sincronizzazione nella ricezione delle frame HIDE e *EOF
      _7_Emulatore
 226. Corretto errore in cancellazione automatica cache all'apertura dell'applicazione
      quando non erano ancora conosciuti Sistema e Ambiente
      _7_Emulatore
 227. Gestito nuovo attributo XML NCV (Numero Caratteri da visualizzare) per implementare
      la keyword CNTFLD
      _7_Emulatore
 228. Non viene + passato come modificato un record di subfile sul quale ci si posiziona
      con il cursore; viene passato solo se cambia il suo contenuto
      _7_Emulatore
 229. Corretto errore nell'assegnazione dei tasti funzionali descritti nei campi di tipo
      "CommandText". Venivano elaborati solo se nel formato era presente un F24
      _7_Emulatore
 230. Corretto errore posizionamento finestre :  nel caso di riemissione finestra con subfile
      allineato "alClient" e WindowState=wsMaximized la riemissione avveniva con coordinata
      sinistra=desktop.width!
      _7_Emulatore
 231. Modificato reperimento Configurazione :  adesso viene effettuata una risalita secondo
      il seguente criterio : 
       LOOCUP_SET\CFG\EMU\<ambiente>\<utente>\SmeuiClt.xml
       LOOCUP_SET\CFG\EMU\DEFAULT\<utente>\SmeuiClt.xml
       LOOCUP_SET\CFG\EMU\<ambiente>\DEFAULT\SmeuiClt.xml
       LOOCUP_SET\CFG\EMU\DEFAULT\DEFAULT\SmeuiClt.xml
       LOOCUP_SET\CFG\EMU\SmeuiClt.xml
      Se nessuno dei criteri di risalita trova un Xml corretto, il programma parte con
      delle impostazioni "minime" di default. (minime minime!)
      _7_Emulatore
 232. Eliminato il "beep" alla pressione di Enter sulla videata.
      _7_Emulatore
 233. Corretto errore introdotto al punto 228. I campi di input subfile modificati mediante
      popup menu o doppio click non impostavano il flag "riga modificata".
      _7_Emulatore
 234. Corretta segnalazione AV se presenti Tablist e non Tab in un Formato video
      _7_Emulatore
 244. Corretta mancata evidenziazione dei campi di input se numerici e Reverse Image
      _7_Emulatore
 245. Il messaggio di errore appare adesso in grassetto nella Status Bar
      _7_Emulatore
 246. Aggiunto Panning Orizzontale mediante tastiera su griglia
      _7_Emulatore
 247. Aggiunta Shortcut (CTRL+F10) su cancellazione Cache Xml Formati Video
      _7_Emulatore
 248. Modificata Gestione Tasti Funzionali. Adesso vengono prima elaborati i tasti
      Funzionali con descrizione e poi quelli senza. Se un tasto funzionale già esiste
      non viene aggiunto il secondo. Ciò significa precedenza ai tasti con descrizione!
      _7_Emulatore
 249. Rimosso il valore Max5250 dal file di configurazione :  non era più utilizzato
      _7_Emulatore
 250. Aggiunti 3 nuovi parametri in configurazione : 
       AutoComplete (Yes|No) = Abilita il completamento automatico dei campi
       AutoCompleteAutoProposal (Yes|No) = Se abilitato appare automaticamente l'elenco
                                           a discesa dei valori precedenti. Se disabilitato
                                           per visualizzarlo occorre premere freccia su-giu
       AutoCompleteHistoryLength         = Numero massimo delle voci memorizzabili nell'elenco
      _7_Emulatore
 251. Non vengono più memorizzati i valori che iniziano con ?!/\+ nell'elenco di autocompletamento
      _7_Emulatore
 252. Aggiunta Possibilità di Cancellazione Storia Valori Campi/Oggetti
      _7_Emulatore
 253. Aggiunta Possibilità di Visualizzazione Cartella Contenente Storia Valori Campi/Oggetti
      _7_Emulatore
 254. Attivata Gestione Storia Valori per Ambiente/Utente
      _7_Emulatore
 255. Modificata Estensione Nomi File memorizzazione Storia Valori in .hst
      _7_Emulatore
 256. Aggiunta funzione (CTRL+F5) di visualizzazione Traccia Comunicazione
      _7_Emulatore
 257. Modificata sintassi definizione intestazioni colonne subfile
      (Da adesso può essere specificata sia nel formato [ecomm;campo]
      che nel formato [campo])
      _7_Emulatore
 258. Attivata gestione attributi video a runtime nei campi di output
      _7_Emulatore
 259. Definito in Configurazione Attributo Video di Default
      <DefaultAttribute></DefaultAttribute>
      _7_Emulatore
 260. Perfezionato controllo inserimento campi numerici. Eliminato errore
      run time se digitati più di 2 segni (+/-).
      _7_Emulatore
 261. Corretto errore AV se nel buffer di un campo di output erano presenti
      attributi video a run time non defniti nell'xml. adesso viene assunto
      il font di Default del campo di output.
      Uniformato il comportamento anche del subfile anche se non presentava
      AV.
      _7_Emulatore
 262. Le Voci di popup menu senza associato un "Exec" adesso vengono disabilitate
      _7_Emulatore
 263. I Tasti Funzionali definiti come "standard" vengono adesso visualizzati anche
      se non hanno testo
      _7_Emulatore
 264. Aggiunta Gestione Oggetti Variabili nei campi di output subfile.
      (Oggetti Variabili=Oggetti il cui Tipo è definito in altri campi video)
      _7_Emulatore
 265. Modificata Gestione reperimento campi video di immissione subfile. Non
      viene più effettuata mediante una ricerca per nome, ma associando alla
      riga 0 di ogni colonna di tipo 'B' un campo di immissione.
      _7_Emulatore
 266. I controlli su subfile vengono creati alle coordinate -Width e -Height
      per evitare la loro visualizzazione a coordinata 0,0 nel caso di
      subfile di input avente panning orizzontale
      _7_Emulatore
 267. Modificata gestione larghezza colonne subfile. Adesso la larghezza di una
      colonna è il massimo tra i dati contenuti e l'ampiezza dell'intestazione
      _7_Emulatore
 268. Implementato prototipo invio subfile come tabella via CTRL+F6
      _7_Emulatore
 269. Aggiunta in Configurazione possibilità di configurare alcuni aspetti dei
      subfile differenziando tra G18 e Standard. I nodi aggiunti sono : 
      <Grid>
        <Default|G18>
           <FullScreen>Yes|No</FullScreen>
           <GridLine>Yes|No</GridLine>
           <AlternateRowColor>Yes|No</AlternateRowColor>
        </Default|G18>
      </Grid>
      _7_Emulatore
 270. Modificata evidenziazione riga selezionata su Subfile
      Precedentemente non venivano correttamente selezionati le celle
      contenenti campi di inpout protetti.
      Inoltre è stata modificata l'altezza della linea inferiore
      dell'indicatore di selezione per consentire la visualizzazione
      anche se non sono visualizzate le righe di separazione tra celle
      _7_Emulatore
 271. Corretto errore :  se ambiente=blank e Sistema Operativo Windows98,
      il path del direttorio temporaneo conteneva due backslash consecutivi
      impendendo l'esecuzione dell'emulatore.
      _7_Emulatore
 272. Migliorata la serializzazione della ricezione della frame di *EOF
      che causa la distruzione dell'Handler e di tutte le form. Precedentemente
      poteva essere eseguita contemporamente alla frame di HIDE e causare degli AV
      _7_Emulatore
 273. Corretto errore nella mancata riassegnazione dei riferimento all'indice della
      lista degli Handler nel popup menu della Systray. Nel caso di più sessioni
      attive contemporaneamente e termine di una sessione dall'indice 'x', tutti i
      puntatori delle sessioni 'x+n' non venivano riadeguati.
      _7_Emulatore
 274. Gli attributi runtime video vengono adesso applicati a partire dal carattere
      successivo rispetto quello nel quale è indicato l'attributo stesso
      _7_Emulatore
 275. Corretto errore sulla mancata attribuzione di TipoOggetto e valore se richiamata
      l'azione di default su una delle icone presenti nella HeaderBar
      _7_Emulatore
 276. Inserita evidenziazione dei campi di input su subfile
      _7_Emulatore
 277. Attivato invio Subfile a Tabella
      _7_Emulatore
 278. Aggiunto funzione di Aggancio Emulatore 5250 mediante tasto Esc
      _7_Emulatore
 279. Corretto Ulteriore errore nell'input di campi numerici se presenti più segni
      (+,-) e non decimali
      __Emulatore
 280. Se un campo optionlist non conteneva valori nel popup veniva comunque inserito
      un elemento vuoto
      _7_Emulatore
 281. Corretto Errore su disabilitazione voci di popup nel caso in cui siano nodi foglia
      di tipo ExecuteProgram ed il campo Exec è vuoto :  nel caso di riemissione del popup
      le voci non erano più disabilitate
      _7_Emulatore
 282. Nell'evidenziazione mediante riquadro dei campi di input su subfile, nel caso in
      cui il campo di input conteneva attributi video runtime, il riquadro di evidenziazione
      veniva disegnato parzialmente
      _7_Emulatore
 283. Attivate Funzioni CTRL+PAGEUP e CTRL+PAGEDOWN; Rispettivamente Rispristinano e
      Massimizzano la finestra prima di eseguire la paginazione
      _7_Emulatore
 284. Aggiunta Gestione "Accelerator Key" su TabSheet
      _7_Emulatore
 285. Aggiunta Esportazione Subfile su Excel mediante tasti CTRL+F7
      _7_Emulatore
 286  Se un campo di Input è protetto e vuoto, viene eliminato il bordo
      _7_Emulatore
 287. Se un campo di input contiene solo un carattere speciale (!?/+%) e viene
      effettuato un click sull'azione di default e l'azione di default ha associato
      un azione da eseguire in sostituzione se il campo è vuoto, quest'ultima viene
      eseguita (Es :  il campo contiene !, viene "cliccata" l'icona dell'oggetto,
      il campo viene trattato come se fosse vuoto)
      _7_Emulatore
 288. Nel passaggio del valore del campo alle funzioni (Exec) viene omesso il primo
      carattere nel caso in cui esso sia un carattere speciale
      _7_emulatore
 289. Inseriti tasti per paginazione.
      _7_Emulatore

_2_ 
_2_                   RILASCIO VERSION 1.1
_2_ 

 290. Modificata Gestione Picture nei campi di Maskedit. Gli '0' vengono sostituiti
      con '-'
      _7_Emulatore
 291. Inserito Attributo FillMethod5250 nelle ObjectActions. Consente di specificare se
      il valore indicato nell'attributo Valore5250 deve essere prefissato al contenuto del
      campo (Pre), aggiunto in coda al valore del campo (Post), sostituito al valore del
      campo (Over).
      _7_Emulatore
 292. Aggiunto Campo in Configurazione <SubfileOptionsAsButtons> che determina se
      visualizzare le opzioni di un subfile come Bottoni.
      _7_Emulatore
 293. Aggiunto Nuovo Componente "OptionBar" che gestisce le opzioni di un subfile
      presentandole come bottoni
      _7_Emulatore
 294. Aggiunta Gestione Oggetti su Subfile dipendenti da altri campi del subfile
      (sia hidden che visualizzati)
      _7_Emulatore
 295. Inserita condizione di visualizzazione dell'OptionBar. Ora non viene visualizzata
      se uno dei campi di tipo "Optionlist" è di tipo 'H' (Hidden)
      _7_Emulatore
 296. Ottimizzata velocità creazione griglia nel caso di G18
      _7_Emulatore
 297. Ottimizzata velocità disegno griglia
      _7_Emulatore
 298. Corretto errore introdotto nella versione rilasciata il 30.10.03 che causava un AV
      se ricevuto un Subfile vuoto
      _7_Emulatore
 299. Inserita gestione campo generico £UIOGG contenente fino a 3 oggetti di riferimento
      sulla riga di subfile.
      _7_Emulatore
 300. Corretto errore sul riposizionamento di un Subfile nel caso in cui la commandbar
      presentava una barra di scorrimento
      _7_Emulatore
 301. Corretto errore :  se premuto Shift+PageUp/Down veniva causata un AV
      (Errore introdotto il 23.10.03)
      _7_Emulatore
 302. Attivata Gestione Schemi Dinamici
      Se nell'Xml di definizione delle colonne di un Subfile, il tipo di oggetto di
      una colonna inizia con £SP, la definizione della colonna è rappresentata da uno
      schema il cui codice è il tipo stesso di oggetto. Viene così richiesto dall'emulatore
      in "modalità sincrona" l'xml di definizione dello schema mediante una richiesta
      display dove il codice formato equivale al codice stesso dello schema.
      La definizione delle colonne risultanti viene poi così sostituita alla colonna
      contenente la definizione dello schema.
      Limitazioni : 
       - Il nome dello schema definito nel parametro Ogg della colonna può essere
         variabile ma la sua variabilità è limitata ai campi contenuti nel buffer
         del formato control del subfile
       - I campi numerici vengono trattati come alfabetici, poichè è l'AS/400 stesso
         che applica le picture ed i codici di editazione
       - Solo uno schema può essere applicato ad un subfile; non vengono cioè gestiti
         subfile con schemi multipli
       - Ad ogni colonna dello schema viene aggiunto un carattere in coda per omogeneità
         rispetto quanto effettuato per le colonne di un subfile "normale"
       - Le colonne "eccedenti" la dimensione del buffer non vengono processate
      _7_Emulatore
 303. Attivata cache richieste estese sincrone
      _7_Emulatore
 304. Definita dimensione massima file di traccia dati comunicazione
      E' possibile definire nel file di configurazione (/UiEmulator/Logging/SockDataTraceSize)
      la dimensione massima del file di traccia dati
      <DatiApplicazioni>\Loocup\<Utente>\Logging\SocketData.log
      La dimensione nel file di configurazione è espressa in KB, ed il default è 1024.
      Quando viene raggiunta la dimensione massima, il file di log esistente viene
      ridenominato con estensione .bak e viene creato un nuovo file.
      _7_Emulatore
 305. Attivata Gestione Memorizzazione Appearance Form e Griglie su File in luogo
      della registry
      _7_Emulatore
 306. Corretto Errore di Ripristino coordinate Form
      _7_Emulatore
 307. Introdotto lo schema come elemento determinante al salvataggio/ripristino
      delle informazioni di appearance
      _7_Emulatore
 308. Aggiunto controllo livello nel salvataggio delle apparenze
      _7_Emulatore
 309. Modificata Gestione Icone per risparmiare risorse GDI
      _7_Emulatore
 310. Aggiunta Impostazione per Griglia G11
      _7_Emulatore
 311. Aggiunta Impostazione Visualizzazione Icone su Impostazioni Griglie
      _7_Emulatore
 312. Aggiunta Impostazione Visualizzazione Intestazione Colonne su Impostazioni Griglie
      _7_Emulatore
 313. Aggiunte Definizioni Costanti Mnemoniche in configurazione : 
       *WINBCK = Colore Standard Sfondo Finestre
       *WINTXT = Colore Standard Testo
 314. Aggiunta possibilità di specificare dimensione carattere se video a 132 colonne
      nel nodo General/FontSize132
      _7_Emulatore
 315. Corretto Errore nell'attribuzione sfondo trasparente a label con Attributi
      Video Runtime (errore introdotto nel punto 313)
      _7_Emulatore
 316  Eliminata possibilità di specificare dimensione del font negli attributi video
      variabili
      _7_Emulatore
 317. Corretto errore su Popup di Oggetti Multipli in G18
      _7_Emulatore
 318. Abilitata Visualizzazione Messaggi Errore come Costanti
      _7_Emulatore
 319. Corretto errore se click su icona per eseguire azione di default
      _7_emulatore

_1_Versione 1.3.a
 320. Corretto Errore su mancata visualizzazione colori in G18 se le stringhe
      contengono "pipe".

_1_Versione 1.3.b
 321. Corretto Problema MemoryLeak nel contatore delle righe subfile.

_1_Versione 1.3.c
 321. Aggiunta Possibilità di gestire il tasto Invio con una descrizione
      in modo analogo a quanto succede per gli altri tasti funzionali
 322. Aggiunta Gestione Virgola Decimale su Tastierino Numerico
 323. Corretto errore su gestione campi con attributo LC (lowercase)

_1_Versione 1.3.d
 324. Aggiunta possibilità di specificare azioni in un popup menu
      utilizzando una sintassi ridotta [parametro] in luogo della
      sintassi estesa [parametro : inizio : lunghezza]
 325. Cablato "Invio=" come parte iniziale della descrizione del
      tasto Invio in luogo di "ENT="
 326. Aggiunta fusione della descrizione del tasto Invio se presente
      solo su piede del Subfile

_1_Versione 1.3.e
 324. Corretto errore nel richiamo di azioni da FunctionBar.
      Era errato il puntatore all'oggetto causando l'inserimento
      di caratteri "spuri" nella frame di richiesta esecuzione azione.
      Se uno di questi caratteri era un "pipe" la frame non era più
      formalmente corretta. Errore introdotto nella 1.3.d.

_1_Versione 1.3.f
 325. Aggiunto gestione Overlay

_1_Versione 1.3.g
 326. Aggiunto Scrolling e Panning di FieldPanel per consentire la visualizzazione completa
      (mediante scrolling e/o panning) delle videate nel caso di utilizzo a bassa risoluzione
      Panning e Scrolling possono essere attivati anche mediante Alt+Shift+<frecce>
 327. Corretto errore mancata visualizzazione Xml mediante programma esterno su Win95 e Win98
 328. Eliminato notepad come editor di default per i file di log. Adesso viene utilizzato
      il programma associato all'estensione
 329. Aggiunta in configurazione possibilità di modificare molti dei colori degli elementi di
      emulatore
         <PositiveNumberFieldColor>128;255;000</PositiveNumberFieldColor>
         <NegativeNumberFieldColor>255;255;000</NegativeNumberFieldColor>
         <ObjectFieldColor>128;255;255</ObjectFieldColor>
         <GridOddLineColor>255;255;255</GridOddLineColor>
         <GridEvenLineColor>196;251;253</GridEvenLineColor>
         <GridSelectedLineColor>016;000;091</GridSelectedLineColor>
         <AttributeColorHI>255;000;000</AttributeColorHI>
         <AttributeColorBL>255;000;255</AttributeColorBL>
         <AttributeColorRI>000;000;255</AttributeColorRI>
         <StatusBarErrorColor>000;000;255</StatusBarErrorColor>
         <FocusRectColor>000;000;255</FocusRectColor>

_1_Versione 1.3.h
 330. Aggiunta Gestione Livello su Display File

_1_Versione 1.3.i
 331. Corretto errore su dimensionamento Subfile introdotto nella
      versione 1.3.g

_1_Versione 1.3.j
 332. Corretto ulteriore errore su dimensionamento Subfile introdotto nella
      versione 1.3.g

_1_Versione 1.3.k
 333. Aggiunta Possibilità di specificare nell'attributo i di una functionbar
      Tipo,Parametro,Codice separati da pipe per gestire la risalita nella
      ricerca icone.

_1_Versione 1.3.l
 334. Corretto ulteriore errore su dimensionamento Subfile introdotto nella
      versione 1.3.g
 335. Corretto errore "List Index Out of Bound" che occorreva quando la sessione
      non veniva correttamente deregistrata dall'icona in SysTray.

_1_Versione 1.3.m
 336. Modificato il comportamento nella gestione campi di I/O con attributo ND
      ma abilitati all'input.

_1_Versione 1.3.n
 337. Risolto il problema nel richiamo popupmenu dalle righe di un subfile G18. Era errata la
      mappatura degli oggetti; essi si riferivano infatti alla riga precedente.

_1_Versione 1.3.o
 338. Risolto problema "Access Violation" nel caso di assenza dell'icona di default generale.

_1_Versione 1.3.p (Rilasciato il 19-04-2005)
 339. Risolto messaggio di errore "List Index Out of Buond" se inviato un comando ACTION senza aver prima emesso un formato video.

_1_Versione 1.3.q (Rilasciato il 21-04-2005)
 340. Risolto messsaggio di errore "Access Violation" nel caso in cui il titolo di una "videata" sia variabile, dipendente da un campo contenuto nel buffer video ed il campo stesso non sia presente nel documento XML di definizione Display.

_1_Versione 1.3.r (Rilasciato il 30-05-2005)
341. Risolto un errore che generava un messaggio di "Access Violation" nel caso di non presenza di un campo necessatio nel buffer video. Risolto un problema che generava il messaggio di "Index out of Bound" alla creazione di un SubFile. Eliminato un memory leak che si aveva dopo la creazione delle "maschere" per l'inserimento nei campi di un SubFile. Le maschere non venivano distrutte correttamente alla chiusura del SubFile. Risolti alcuni problemi che generavano dei messaggi di tipo "Access Violation" nel caso in cui il formato video presente nell'XML non sia valido o riconosciuto correttamente (Problema con multilingua).

_1_Versione 1.3.s (Rilasciato il 17-06-2005)
342. Risolto problema nella mancata sovrapposizione di formati video introdotto in 1.3.r. I campi dei formati video di piede emessi in overlay non venivano visualizzati
343. Corretto AV nel caso in cui un campo numerico di un Subfile contenga dati non validi.

_1_Versione 1.3.t (Rilasciato il 23-06-2005)
344. Modificata visualizzazione icona in avvio. Ora durante l'inizializzazione viene visualizzata un'icona grigia.

_1_Versione 1.3.u (Rilasciato il 14-07-2005)
345. Fissato un problema sulla pressione consecutiva del tasto F12.

_1_Versione 1.3.v (Rilasciato il 19-07-2005)
346. Fissato un ulteriore problema sulla pressione consecutiva del tasto F12.

_1_Versione 1.3.w (Rilasciato il 04-08-2005)
347. Risolto Errore "Out of Memory" al caricamento di Subfile contenenti migliaia di record.
348. Velocizzato caricamento Subfiles contenenti migliaia di record.
349. Implementato Posizionamento su colonna subfile mediante attributo PC.

_1_Versione 1.3.x (Rilasciato il 03-11-2005)
350. Corretta anomalia nella visualizzazione delle FunctionBar. Se veniva visualizzato un form senza FunctionBar, non era più possibile visualizzarla successivamente sullo stesso form. Sostanzialmente la proprietà "Visible" della FunctionBar rimaneva impostata a "False", inibendo così la visualizzazione successiva.
