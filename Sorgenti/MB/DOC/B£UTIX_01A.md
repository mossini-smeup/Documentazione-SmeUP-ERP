# Introduzione
Scopo del documento e delle funzioni che vengono aggiunte a SME.up è quello di facilitare la modifica delle aliquote IVA.
Ciò si otterrà : 
- raccogliendo tutte le indicazioni operative da seguire
- realizzando una scheda di controllo che evidenzia la situazione dei codici IVA
- fornendo un programma si sostituzione automatica in funzione di condizioni impostate

# Impatto della variazione IVA nella Normativa
Con l'introduzione dell'aliquota al 21% dovrà essere aggiornata/inserita una serie di dati nel sistema gestionale.
Nel fare questo va tenuto in particolare conto l'aspetto temporale, relativo alla data di effettuazione dell'operazione oggetto dell'imposta.
Le operazioni con una data di effettuazione inferiore alla data di introduzione dovranno infatti riportare ancora l'aliquota del 20%.

 Relativamente alla data effettuazione rammentiamo che  : 
 * Le cessioni di beni si considerano effettuate : 
 ** al momento della stipulazione dell'atto se hanno ad oggetto beni immobili
 ** al momento della consegna o spedizione se riguardano beni mobili
 ** Tuttavia, se anteriormente a tali momenti sia stata emessa la fattura o sia stato pagato in tutto o in parte il corrispettivo, l'operazione si considera effettuata, limitatamente all'importo fatturato o pagato, alla data di emissione della fattura o a quella di effettuazione del pagamento.
 * Le prestazioni di servizi secondo quanto disposto dall'art. 6, commi 2 e 3, D.P.R. n. 633/1972, si considerano effettuate : 
 ** all'atto del pagamento del corrispettivo o
 ** alla data di emissione della fattura se antecedente.

 Questo quindi implica ad esempio che le bolle ancora da fatturare e consegnate con data antecedente all'introduzione della nuova aliquota dovranno mantenere l'aliquota al 20% e che in caso di fatturazione a fine mese potranno anche sussistere documenti con aliquota doppia. Anche le eventuali note di credito emesse dopo l'entrata in vigore della nuova aliquota IVA del 21% devono riportare l'aliquota IVA vigente alla data di effettuazione dell'operazione principale a cui esse si riferiscono.

# Che cosa si può fare venerdì 16 settembre 2011
Se non si vuole incorrere nella presenza della doppia aliquota con fatturazione a fine mese è consigliabile fatturare tutto quello che si ha ancora da emettere entro la data odierna.
 Per questo tipo di operazione si potrebbe anche attendere fino a lunedì purchè vengano incluse solo le bolle che arrivano fino a venerdì.
 Alternativamente sempre per non incorrere nella presenza della doppia aliquota si può valutare al momento della fatturazione di filtrare i documenti in modo che sia abbia una suddivisione netta tra i documenti al 20 e quelli al 21.
 La presenza della doppia aliquota diventa un problema nel caso di moduli di fattura che abbiano lo spazio per una sola aliquota.

# Che cosa fare da sabato 17 settembre 2011
 Al più presto è consigliabile aggiornare i dati sensibili del sistema riportati a seguire :  la fatturazione deve essere eseguita solo dopo tale aggiornamento.
 Se ciò non è possibile, i documenti dovranno essere modificati manualmente in modo che, ove richiesto, riportino l'assoggettamento al 21 prima che vengano stampati e/o contabilizzati.

# I Dati sensibili da adeguare nello standard
* Introduzione nella tabella degli assoggettamenti IVA dei codici al 21%.
 E' obbligatorio il mantenimento degli assoggettamenti al 20%. Si consiglia inoltre di predisporre una tabella della corrispondenza fra vecchi e nuovi codici. Per chi intende seguire la procedura SMEUP di adeguamento (citata nel seguito) dovrà inserire questa informazione negli Alias.

 * Aggiornamento di tutti i dati da cui viene derivato l'assoggettamento iva nella registrazione dei
 documenti e della contabilità : 
 ** Gli assoggettamenti indicati nelle tabelle V51, C51, BRA, C6S, G9S
 ** Le anagrafiche delle articoli
 ** Le anagrafiche degli enti
 ** Estensioni anagrafiche £14 (Dati specifici per modello)
 ** Parametri standard della tabella C5D (Per la creazione dei documenti di autofattura)
 * Vanno poi controllati gli elementi della tabella C5U che iniziano per "IVA". Questi elementi di tabella possono presentare nel 6° e nel 7° carattere un codice della tabella IVA. Se uno di questi codici corrisponde a quelli con aliquota al 20% andranno creati gli elementi della C5U aventi nei caratteri 6/7 il nuovo codice iva corrispondente al 21%.

 * Aggiornamento dei documenti che dovranno essere elaborati con la nuova aliquota : 
 ** Gli ordini aperti, attivi e passivi, valutando se sia opportuno, per le righe evase parzialmente, applicare una suddivisione netta fra quanto già evaso ed il residuo, saldando la riga e riaprendone una nuova per il solo residuo.
 ** Le bolle se successive alla data di introduzione della nuova aliquota. Per questi documenti andranno aggiornati sia i dati di testata che di riga.
 * Se per vari motivi sono stati contabilizzati documenti con aliquota errata questi andranno scontabilizzati, e corretti/ricontabilizzati o in alternativa stralciati e ricreati ex-novo.

## Caso particolare della tabella V5S
Dall'elenco precedente è stata volutamente esclusa la casistica della tabella V5S (spese/sconti). Per questa ci sono alcune considerazioni particolari da fare se negli elementi è stata indicata un'aliquota al 20%. Istruzioni sulla risoluzione di questa casistica verranno rese disponibili all'indirizzo che verrà indicato di seguito. Si consiglia di verificare se si rientra nella casistica e nel caso di allinearsi a tali istruzioni non appena saranno disponibili.

### Adeguamento delle personalizzazioni
Per le eventuali logiche personali si danno invece queste indicazioni : 
 * Verificare presenza di campi utente su tabelle standard che prevedano campi che fanno riferimento alla tabella IVA e conseguente verifica dell'utilizzo di tali campi
 * Verificare presenza di tabelle personali che prevedano campi che fanno riferimento alla tabella IVA e conseguente verifica dell'utilizzo di tali campi
 * Elementi di tabella che contengono riferimenti alla tabella IVA e conseguente verifica dell'utilizzo di tali elementi (es. caso della B£G che può avere molteplici implicazioni)
 * Controllo di programmi personali o personalizzati che contengano riferimenti espliciti ad elementi della IVA o anche solo all'aliquota 20.

# Impostazioni dell'utility di variazione
All' indirizzo "ftp : //demo.smeup.com/iva21/ "si potranno scaricare istruzioni operative e i sorgenti  dell'utility. Dalle ore 14 di oggi (Venerdì 16 settembre) sarà disponibile la documentazione relativa alla V5S. Da Lunedì 19 settembre saranno disponibili (in versione beta) i sorgenti dell'utility e la documentazione completa, che verranno eventualmente aggiornati (riferirsi alla data/ora di pubblicazione per verificare il livello di aggiornamento). Nel corso della stessa settimana ci proponiamo di rilasciare la versione definitiva, informandovi via News.

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
