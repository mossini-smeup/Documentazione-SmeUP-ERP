## Esempi di applicazioni del modulo MPS
Le caratteristiche di disegno del modulo ne permettono l'utilizzo rivolto, non solo al raggiungimento degli obiettivi principali descritti, ma aperto al soddisfacimento di esigenze diverse.

A titolo di esempio di seguito vengono riportati alcuni possibili scenari di utilizzo.

### Determinazione Piano Principale di Produzione
È l'obiettivo primario e consiste nel determinare un Piano valido nel breve termine, sulla base della nuova figura di domanda e del piano precedente.
L'applicazione esegue i seguenti passi : 
**1) Ricezione domanda e controllo verso termini e condizioni di fornitura**
**2) Questa funzione permette l'ingresso della domanda su una scala temporale.**
La distribuzione della scala temporale è parametrica e può essere costituita di periodi giornalieri, settimanali o mensili, combinati fino a un massimo di 120 periodi.
La domanda può essere verificata verso le condizioni di fornitura (Terms and Conditions), che possono essere generali o specifiche per coppie di entità (es. :  articolo, cliente, famiglia di articoli/cliente, ecc...) e la cui applicazione può essere sequenziata e condizionata dalla data (time effective).

### Creazione Piano Principale Produzione in base a raggruppamenti, regole e politiche
È disponibile una funzione di raggruppamento per gestire facilmente un elevato numero di articoli attraverso la creazione di famiglie.
La struttura dei raggruppamenti si sviluppa su più livelli (il cui numero è illimitato), ciascuno dei quali permette fino a nove diverse classificazioni.
La creazione del Piano principale di Produzione è condizionata dall'applicazione alla domanda di politiche e regole parametriche (es. :  P.Prod.= Domanda, P.Prod.= Maggiore tra Domanda e P.Prod.
precedente, Politica del lotto minimo, ...).

### Analisi impatto del nuovo Piano sulle entità di produzione
Ciascun piano può essere visualizzato sotto forma di quantità da produrre per periodo oppure sotto altre forme di rappresentazione (es. :  carico di lavoro per periodo, costo mantenimento inventariale per periodo, ...), che visualizzano l'impatto del nuovo Piano sulle entità che condizionano l'andamento produttivo.

### Suddivisione nuovo Piano sulle linee di produzione
Il piano viene suddiviso sulle varie linee produttive in base all'applicazione di regole (quantità minima / massima per ciclo, percentuale di distribuzione sulle linee, ...).

### Analisi impatto del nuovo Piano sulle risorse di linea
Può essere visualizzato l'impatto sulle risorse di linea :  carico macchina, carico persone, fabbisogno componenti.

### Gestione del Piano e verifiche (riciclo sulle analisi precedenti)
Onde eliminare problemi di risorse o linearizzare il Piano, sono possibili interventi (manuali o automatici), in seguito ai quali è possibile rilanciare le verifiche (sia in interattivo che in batch) di impatto sulle risorse.

### Rilascio del Piano ai sistemi MRP
Quando il Piano è ottimizzato sotto tutti i punti di vista, può essere rilasciato e passato ai sistemi MRP, registrato e memorizzato.
E' possibile mantenere in linea più livelli (il cui numero è parametrico).

### Determinazione preventivo fabbisogno centri di lavoro
È un modo di utilizzo dell'applicazione per la determinazione della figura di fabbisogno di risorse di lavoro (equipment, people,...) nel medio e lungo periodo, sulla base della previsione di domanda.
Il fabbisogno potrebbe essere utilizzato ad esempio per decisioni concernenti il recupero o l'avvicendamento di risorse.
L'applicazione esegue i seguenti passi : 
**1) Ricezione previsione domanda**
Questa funzione permette l'ingresso della previsione su una scala temporale i cui periodi saranno costituiti di settimane e mesi.
**2) Raggruppamento in famiglie**
Si utilizza la funzione di raggruppamento che permette di poter gestire facilmente un elevato numero di articoli attraverso la creazione di famiglie.
Unitamente alla funzione di raggruppamento esiste l'opposta funzione di **spread**, che permette di passare da un piano raggruppato per famiglia ad uno suddiviso sugli articoli.
**3) Esplosione della previsione di domanda sulle entità di produzione**
La domanda viene esplosa secondo cicli (di tipo tecnico o di pianificazione, a seconda delle necessità), per ottenere la figura del fabbisogno risorse (le risorse possono essere sia macchine che persone).
**4) Eventuale raggruppamento in famiglie delle risorse**
Si utilizza la funzione di raggruppamento, che permette di poter gestire facilmente un elevato numero di risorse attraverso la creazione di famiglie.
**5) Gestione della previsione e verifiche (riciclo sulle analisi precedenti)**
Sono possibili interventi (manuali o automatici) di modifica del piano di previsione.
Successivamente agli interventi si possono rilanciare le verifiche (sia in interattivo che in batch) di impatto sulle risorse.

### Determinazione piano fabbisogno materiali
È un modo di utilizzo dell'applicazione per la determinazione della figura di fabbisogno di componenti (normalmente solo componenti critici) nel medio e lungo periodo, sulla base della previsione di
domanda.
Il fabbisogno potrebbe essere utilizzato ad esempio per la definizione di contratti di fornitura sul medio periodo (ordini aperti).
L'applicazione esegue i seguenti passi : 
**1) Ricezione previsione domanda**
Questa funzione permette l'ingresso della previsione su una scala temporale i cui periodi saranno costituiti di settimane e mesi.
**2) Raggruppamento in famiglie**
Si utilizza la funzione di raggruppamento che permette di poter gestire facilmente un elevato numero di articoli attraverso la creazione di famiglie.
Unitamente alla funzione di raggruppamento esiste l'opposta funzione di **spread**, che permette di passare da un piano raggruppato per famiglia ad uno suddiviso sugli articoli.
**3) Esplosione della previsione di domanda sui componenti**
La domanda viene esplosa secondo la distinta base (tutti i componenti o soltanto quelli critici, a seconda delle necessità) per ottenere la figura del fabbisogno componenti.
**4) Eventuale raggruppamento in famiglie dei componenti**
Si utilizza la funzione di raggruppamento che permette di poter gestire facilmente un elevato numero di articoli attraverso la creazione di famiglie.
**5) Gestione della previsione e verifiche (riciclo sulle analisi precedenti)**
Sono possibili interventi (manuali o automatici) di modifica del piano di previsione.
Successivamente agli interventi si possono rilanciare le verifiche (sia in interattivo che in batch) di impatto sui componenti.
