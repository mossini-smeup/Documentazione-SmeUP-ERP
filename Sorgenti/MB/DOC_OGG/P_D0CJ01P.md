* LowLevelCode
  Per il calcolo del costo medio è stato creato specificatamente un LLC che
  si basa su due concetti predefiniti : 
  - Riferito specificatamente agli eventi estratti in quel range di date
  - Per tutti gli eventi estratti applica il LLC dell'oggetto scelto nel
    campo "Costi per oggetto specifico", se tale campo è blank applica il
    LLC di AR-Articolo
  Tale LLC (denominato £DW) ha la necessità di essere calcolato
  contestualmente al calcolo, in quanto uno degli elementi caratterizzanti
  è proprio il range di date del calcolo stesso.
  Questo LLC viene ricoverato sul file di supporto D0ARDT0F ed è per questo
  motivo che viene consigliato di lanciare i costi in una coda specifica
  che abbia in immissione un solo JOB alla volta, così da evitare generazioni
  di LLC che si ostacolino a vicenda

* Costi per oggetto specifico
  I valori significativi sono i seguenti : 
  - BLANK          No
  - 1              Lotto
  - 2              Collo
  - 3              Lotto dell'ordine produzione
  Questa impostazione assume una valenza in quanto oltre a condizionare
  l'attribuzione del LLC, rimane implicito che, nel caso di
  - BLANKS gli eventi che verranno processati potranno essere : 
    - Ordini di produzione
    - Documenti di Conto lavoro
    - Documenti di Acquisto
    - Costi standard per eventilegati a differenze inventariali
  - 1 o 3 gli eventi processati saranno genericamente : 
    - Lotti, sia di produzione che di acquisto che si cto lavoro
      ma sempre lotti, per cui sarà necessario, in fase di
      pre-calcolo, o comunque preventivamente al calcolo aver
      generato una distinta lotto su lotto.
  - 2 gli eventi processati saranno genericamente : 
      Colli, sarà necessario aver prodotto preventivemente una
      distinta base collo su collo

* Gestione Omaggi
  - BLANK le righe definite OMAGGIO non vengono processate
  - 1 le righe definite OMAGGIO vengono processate

* Estrazione movimenti scarti
  - BLANK le righe movimento di scarti non vengono processate
  - 1 le righe movimento di scarti vengono processate

* Segno movimenti
  - E vengono processati solo 'Movimenti' di Entrata
  - U vengono processati solo 'Movimenti' di Uscita
  - T vengono processati Tutti i movimenti
  La selezione delle causali, oltre eventualmente alla EXIT
  specifica, è demandata all'impostazione degli elementi della
  tabella D0J

* Magazzino Fisico
  - BLANKS Tutti i magazzini fisici
  - XXX Posso processare movimenti SOLO relativamente a quel
    magazzino fisico
* Magazzino Fiscale
  - BLANKS Tutti i magazzini fiscali
  - XXX Posso processare movimenti SOLO relativamente a quel
    magazzino fiscale

* Sottosettore Fonti
  - XX Viene impostato il sottosettore della tabella D0J che
    come caratteristica a quella di poter avere in estrazione
    almeno 4 tipologie di fonti possibili : 
    E1 - Movimenti di magazzino - Fonte principale in selezione
    V5 - Righe documenti        - Fonte di eccezione
    OR - Ordini di produzione   - Fonte di eccezione
    LO - Lotti                  - Fonte di eccezione
  Una fonte di 'selezione' permette di selezionare quelle specifiche
  causali assegnate ai movimenti di magazzino, mentre le
  fonti di 'eccezione' esludono dalla selezione il movimento di
  magazzino selezionato con le causali e lo includono in un
  successivo passaggio di selezione considerandolo con le
  azioni previste dall'elemento della fonte di eccezione.
  Tipici casi che si possono avere nelle fonti di eccezione : 
  - Note di accredito e/o addebito a valore
  - Ordini di conto lavoro di RILAVORAZIONE
  - Ordini interni di RILAVORAZIONE
  - Ordini interni di smontaggio, così da generare un LLC
    con livello inverso da quello previsto nella distinta
    dell'ordine stesso

* Controllo stato oggetto
  I valori significativi sono i seguenti : 
  - BLANK          Solo ordini/lotti chiusi
  - 1              OR/LO chiusi con extra periodo
  - 2              Anche ordini/lotti aperti
  Tali valori hanno il seguente significato applicativo : 
  - BLANK  Si considerano solo ordini o lotti chiusi ma
    alla data del calcolo, considerandoli aperti, anche se in livello
    '8' nel caso vi siano eventi significativi, successivi
    alla data del calcolo, sull'oggetto stesso
  - 1 Si considerano solo ordini chiusi, ma NON per la sola quantità
    prevista nel periodo di selezione delle date 'dal' 'al',
    ma per tutta la quantità versata su quell'ordine (assunta
    direttamente dal P5TEOP




