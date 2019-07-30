## Dove risiede la documentazione
La documentazione risiede in membri di testo presenti in file DOC_xxx. Ciascun file è dedicato ad una famiglia di documenti : 

- _2_DOC; contiene la documentazione applicativa
- _2_DOC_VIS; contiene i documenti visione delle applicazioni
- _2_DOC_OGG; contiene la documentazione degli oggetti : 
-- _3_Classi di autorizzazioni, il membro è denominato A_xxxxxx (xxxxxxx è la classe)
-- _3_Archivi, il membro è denominato F_xxxxxx (xxxxxxx è il file)
-- _3_Oggetti grafici Loocup, il membro è denominato J1_xxxxxx (xxxxxxx è il componente)
-- _3_Configurazioni Loocup, il membro è denominato L_xxxxxx (xxxxxxx è la configurazione)
-- _3_Oggetti Smeup, il membro è denominato OG_xx (xx è l'oggetto)
-- _3_Info di dettaglio su oggetti Smeup, il membro è denominato OG_xx_D (xx è l'oggetto). _1_Nota; nella documentazione di un oggetto, quando questo è collegato ad un archivio (es. articoli, enti, risorse, ..) viene inserita la chiamata alla documentazione dell'archivio, se invece l'oggetto non è collegato ad un archivio (es. una data, lo schema informazioni, un elemento di settore, ...) viene creato un membro OG_xx_D in cui sono descritti ulteriori dettagli tecnici e implementativi.
-- _3_Programmi, il membro è denominato P_xxxxxx (xxxxxxx è il programma)
-- _3_Tabella Smeup (Settore), il membro è denominato TA_xxx (xxx è la tabella)
-- _3_Valore fisso Smeup, il membro è denominato V2_xxxxxx (xxxxxxx è il valore fisso)
-- _3_Valore dinamico Smeup, il membro è denominato V3_xxxxxx (xxxxxxx è il valore dinamico)
- _2_DOC_SCH; contiene la documentazione delle schede
- _2_DOC_VOC; contiene la documentazione delle voci (glossari, definizioni, suggerimenti operativi, faq ...)
- _2_DOC_SER; contiene la documentazione dei servizi
- _2_DOC_PRE; contiene i membri per la creazione di documenti in formato presentazione
- _2_DOC_BOK; contiene i membri per la creazione di documenti in formato libro (membri indici di documenti di dettaglio). In particolare il membro "C" contiene la lista dei manuali pubblicati e ul membro "C_USR" contiene le regole di autorizzazione per l'accesso ai manuali via internet.
- _2_DOC_ESE; contiene i membri per la creazione di documenti di esempi per la comprensione
- _2_DOC_TAxxx; serve per documentare gli elementi di particolari tabelle (es. Tabella B£P delle classi di autorizzazioni), ogni membro corrisponde all'elemento di tabella e il valore XXX nel file corrisponde al settore di tabella :  es. DOC_TAB£P.


## Responsabile di un manuale
Il programma di composizione del manuale ricerca anche il responsabile e lo stampa nella copertina del documento. Ogni oggetto Sme.up può essere intestato ad un responsabile e ad uno o più assistenti. L'elenco dei responsabili è cablato in fondo al programma B£AR22.
 :  : DEC T(OJ) P(*PGM) K(B£AR22) L(1)

## Come si modifica la documentazione
Si utilizza il componente grafico di Loocup per la gestione dei testi : 
- [Text editor](Sorgenti/MB/DOC_OPE/LOCEDT)

## Elenco macro di documentazione
- [Elenco MACRO di documentazione](Sorgenti/MB/DOC/B£DOCU_40)

## Come si gestiscono le immagini
- [LATEX - Gestire le immagini](Sorgenti/MB/DOC/LOCFRM_LTD)

## Come integrare documentazione specifica del cliente
La documentazione specifica del cliente può essere scritta in memebri di documentazione attiva seguiendo le stesse convenzioni e tecniche utilizzate dalla documentazione standard, l'unica differenza è che i membri di coumentazione attiva risiedono nella libreria degli oggetti specifici del cliente (_2_SME_xxx).

La documentazione attiva può essere anche utilizzata per descrivere altre tipologie di infromazioni utente (es. le procedure operative) in questi casi, dentro la libreria specifica _2_SME_xxx- si utilizza il file _2_DOC_PER.
