# PARAMETRI FISSI AZIENDA OLD

Questa interrogazione restituisce ulteriori parametri relativi all'azienda.
- Divisione unica :  è un elemento della C5Q ed è un campo usato solo nella contabilità :  individua la presenza di settori nell'azienda.
- Divisione fiscale :  è un campo sì/no che consente di suddividere anche i registri IVA e i giornali nel momento in cui sono presenti più divisioni nell'azienda.
- Lista librerie :  è un elemento della B£B ed elenca le librerie utilizzate dall'applicazione.
- Periodo / Giorno liquidazione IVA :  individua la modalità di liquidazione dell'IVA scelta dall'azienda (mensile, annualeo trimestrale) e il giorno in cui tale liquidazione viene effettuata.
- % Interesse Liquidazione :  indica la percentuale da utilizzare per il calcolo degli interessi nella liquidazione IVA.
- Azienda di compensazione IVA :  è un campo che interessa gruppi di aziende :  si ha, infatti, una compensazione dei debiti e dei crediti IVA tra aziende appartenenti allo stesso gruppo, in questo campo viene riportata la capogruppo ovvero quella che verserà l'IVA al fisco.
- Dati integrativi registri IVA :  è un campo sì/no grazie al quale è possibile definire il default visualizzato nel formato guida della stampa registri IVA. Se verrà scelto di visualizzare anche i dati integrativi sui registri IVA verranno riportate le informazioni relative agli enti coinvolti (ragione sociale e indirizzo)
- Sintesi registri riepilogativi IVA :  è un campo sì/no grazie al quale è possibile governare il default visualizzato nel formato guida della stampa registri IVA. Se verrà scelto di stampare una sintesi in coda al registro IVA verrà riportata un'analisi per codice IVA.
- Plafond Mobile :  il plafond è il tetto massimo di acquisti che possono essere effettuati senza pagare IVA e può essere annuale o mensile. E'previsto per quelle aziende che esportano molto e hanno difficoltà nel recupero dell'IVA, di conseguenza il fisco mette a disposizione la possibilità di dichiarare la percentuale di fatturato dovuto alle esportazioni e chiedere ai fornitori di emettere fatture senza IVA (art. 8/c legge 641/1973) fino al raggiungimento di un certo importo attraverso una dichiarazione d intento . In questo campo si dichiara semplicemente se l'azienda ha a disposizione o meno questa possibilità.
- % Pro-Rata :  le aziende che effettuano sia prestazioni esenti da IVA che prestazioni soggette a IVA, non possono detrarre completamente l'IVA degli acquisti dall'ammontare che devono pagare al fisco ma possono detrarne solo una % proporzionale al volume di prestazioni soggette a IVA (art. 19bis DPR 633/72). Questa percentuale è chiamata pro-rata ed è determinata una volta all'anno basandosi sulle operazioni eseguite l'anno precedente con la seguente formula :  A/(A+B) dove A sono le operazioni che danno diritto a detrazione e B quelle esenti. Se a fine anno la % risulta differente si dovrà effettuare un conguaglio. Il calcolo della %pro-rata può essere effettuato tramite un'apposita interrogazione.
- Cessione Credito IVA :  è un campo sì/no con il quale è possibile indicare che l'azienda cede i propri crediti IVA ad altre aziende.
- Plafond in liquidazione IVA :  in questo campo viene dichiarato se il plafond deve essere riportato sul registro IVA oppure no.
- Stampa bollato estesa :  se viene flaggato sul sì verrà stampato il giornale a 198 righe, in caso contrario verrà stampato a 132 righe.
- Paginazione bollato :  permette di gestire il default che consente di inserire i numeri di pagina sul bollato.
- Descrizioni aggiuntive sul bollato :  imposta se stampare sul bollato maggiori informazioni sull'azienda oppure se limitarsi a quelle obbligatorie.
- Note E4 sul bollato :  E4 è l'oggetto Testata dei documenti :  qui viene dichiarato se stampare le note relative alle testate sul bollato o meno.
- Note E5 sul bollato :  E5 è l'oggetto Riga dei documenti :  qui viene dichiarato se stampare le note relative alle righe sul bollato o meno.
- Anno riferimento da data inizio :  è un campo sì/no attraverso cui viene definito se riportare l'anno a cui si riferisce il giornale sul bollato o meno.
- Pagina bolli su bollato :  viene dichiarato se all'interno del bollato andranno inserite delle pagine bianche per l'apposizione dei bolli.
Sono di seguito riportati alcuni programmi che permettono di visualizzare il valore finale del bollato nei diversi anni (Progressivo Giornale/1000), l'ultima riga e l'ultima pagina del bollato per ogni esercizio e l'ultima pagina del registro presenze.

Sotto si trovano i parametri relativi all'identificazione dell'azienda come il capitale sociale, la data di inizio attività, la natura giuridica e il codice SIA.

Le fonti fisse ADF sono quelle utilizzate per la determinazione della disponibilità finanziaria dell'azienda nel tempo mentre l'intermediario è la persona autorizzata a presentare documenti fiscali in sostituzione dell'azienda (di solito è il commercialista).


