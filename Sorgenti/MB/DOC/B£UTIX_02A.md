# Introduzione
Scopo del documento e delle funzioni che vengono aggiunte a SME.up è quello di facilitare la modifica delle aliquote IVA.
Ciò si otterrà : 
- raccogliendo tutte le indicazioni operative da seguire
- realizzando una scheda di controllo che evidenzia la situazione dei codici IVA
- fornendo un programma si sostituzione automatica in funzione di condizioni impostate

# Impatto della variazione IVA nella Normativa
Con l'introduzione dell'aliquota al 22% dovrà essere aggiornata/inserita una serie di dati nel sistema gestionale.
Nel fare questo va tenuto in particolare conto l'aspetto temporale, relativo alla data di effettuazione dell'operazione oggetto dell'imposta.
Le operazioni con una data di effettuazione inferiore alla data di introduzione dovranno infatti riportare ancora l'aliquota del 21%.

 Questo quindi implica ad esempio che le bolle ancora da fatturare e consegnate con data antecedente all'introduzione della nuova aliquota dovranno mantenere l'aliquota al 21% e che in caso di fatturazione a fine mese potranno anche sussistere documenti con aliquota doppia. Anche le eventuali note di credito emesse dopo l'entrata in vigore della nuova aliquota IVA del 22% devono riportare l'aliquota IVA vigente alla data di effettuazione dell'operazione principale a cui esse si riferiscono.

# Che cosa fare ?
 Al più presto è consigliabile aggiornare i dati sensibili del sistema riportati a seguire :  la fatturazione deve essere eseguita solo dopo tale aggiornamento.
 Se ciò non è possibile, i documenti dovranno essere modificati manualmente in modo che, ove richiesto, riportino l'assoggettamento al 22 prima che vengano stampati e/o contabilizzati.

# I Dati sensibili da adeguare nello standard
* Introduzione nella tabella degli assoggettamenti IVA dei codici al 22%.
 E' obbligatorio il mantenimento degli assoggettamenti al 21%. Si consiglia inoltre di predisporre una tabella della corrispondenza fra vecchi e nuovi codici. Per chi intende seguire la procedura SMEUP di adeguamento (citata nel seguito) dovrà inserire questa informazione negli Alias.

 * Aggiornamento di tutti i dati da cui viene derivato l'assoggettamento iva nella registrazione dei
 documenti e della contabilità : 
 ** Gli assoggettamenti indicati nelle tabelle V51, C51, BRA, C6S, G9S
 ** Le anagrafiche delle articoli
 ** Le anagrafiche degli enti
 ** Estensioni anagrafiche £14 (Dati specifici per modello)
 ** Parametri standard della tabella C5D (Per la creazione dei documenti di autofattura)
 * Vanno poi controllati gli elementi della tabella C5U che iniziano per "IVA". Questi elementi di tabella possono presentare nel 6° e nel 7° carattere un codice della tabella IVA. Se uno di questi codici corrisponde a quelli con aliquota al 21% andranno creati gli elementi della C5U aventi nei caratteri 6/7 il nuovo codice iva corrispondente al 22%.

 * Aggiornamento dei documenti che dovranno essere elaborati con la nuova aliquota : 
 ** Gli ordini aperti, attivi e passivi, valutando se sia opportuno, per le righe evase parzialmente, applicare una suddivisione netta fra quanto già evaso ed il residuo, saldando la riga e riaprendone una nuova per il solo residuo.
 ** Le bolle se successive alla data di introduzione della nuova aliquota. Per questi documenti andranno aggiornati sia i dati di testata che di riga.
 * Se per vari motivi sono stati contabilizzati documenti con aliquota errata questi andranno scontabilizzati, e corretti/ricontabilizzati o in alternativa stralciati e ricreati ex-novo.

## Caso particolare della tabella V5S
Dall'elenco precedente è stata volutamente esclusa la casistica della tabella V5S (spese/sconti). Per questa ci sono alcune considerazioni particolari da fare se negli elementi è stata indicata un'aliquota al 21%. Istruzioni sulla risoluzione di questa casistica verranno rese disponibili all'indirizzo che verrà indicato di seguito. Si consiglia di verificare se si rientra nella casistica e nel caso di allinearsi a tali istruzioni non appena saranno disponibili.

### Adeguamento delle personalizzazioni
Per le eventuali logiche personali si danno invece queste indicazioni : 
 * Verificare presenza di campi utente su tabelle standard che prevedano campi che fanno riferimento alla tabella IVA e conseguente verifica dell'utilizzo di tali campi
 * Verificare presenza di tabelle personali che prevedano campi che fanno riferimento alla tabella IVA e conseguente verifica dell'utilizzo di tali campi
 * Elementi di tabella che contengono riferimenti alla tabella IVA e conseguente verifica dell'utilizzo di tali elementi (es. caso della B£G che può avere molteplici implicazioni)
 * Controllo di programmi personali o personalizzati che contengano riferimenti espliciti ad elementi della IVA o anche solo all'aliquota 21.

## Due Casi Frequenti di Personalizzazione

### Utilizzo dell'Assoggettamento IVA nel CORD
Se è stato utilizzato l'assoggettamento IVA nel CORD viene consigliato nel pgm di adeguamento di inserire le specifiche riportate di seguito, PRIMA dell'istruzione d'aggiornamento della testata :  V5TDOC.

> * i.mod.CORD
D V5TDOC        E DS                  EXTNAME(V5TDOC0F) INZ
 * f.mod.CORD
...
 * i.mod.CORD
C                   EVAL      £V5LFU='A'
C                   EVAL      £V5LME=''
C                   EVAL      £FUNP1=T§TDOC
C                   EVAL      £V5LL1='2'
C                   EVAL      £V5LIM=T§TMOD
C                   EXSR      £V5L
C                   IF        NOT(*IN35)
C                   EVAL      V5A$DS=£V5LT1
C                   ELSE
C                   CLEAR                   V5A$DS
C                   ENDIF
C                   CALL      'V5DO01O'
C                   PARM      'COS'         XXFUNZ           10
C                   PARM      T$V5AG        XXMETO           10
C                   PARM                    V5TDOC
 * f.mod.CORD


### Documento Pre-Bolla
Un altro caso emerso, ma destinato ad esaurirsi a breve, consiste nell'utilizzo di documenti creati prima del 01/10/13, ma destinati essere stampati come bolle in data successiva. Questi documenti non avendo la data bolla non vengono trattati dal pgm di aggiornamento standard. Questo caso va perciò gestito in maniera opportuna :  ad esempio,individuando questi casi dal tipo modello e dell'assenza di data/n° bolla/fattura.

# Impostazioni dell'utility di variazione
All' indirizzo "ftp : //demo.smeup.com/iva22/ "si potranno scaricare istruzioni operative e i sorgenti  dell'utility.

- Prerequisiti
-- Versione V3.R1-2 e V2.R3
-- Utilizzo di LOOC.up come interfaccia grafica
-- Capacità tecniche di attivazione di una PTF scaricata da INTERNET

- Attività
-- Definizione dei nuovi codici IVA
-- Associazione fra codici vecchi e nuovi come ALIAS

- Scheda di comprensione
-- Documentazione delle attività da eseguire
-- Evidenza dei luoghi di interesse su cui agire

- Funzioni di Aggiornamento
-- Modalità strampa / aggiornamento
-- Aggiornamento globale / parziale

