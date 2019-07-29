# 1.1 Obiettivo generale
Il presente documento si pone l'obiettivo di descrivere l'approccio Sme.Up alla Business Intelligence, la scelta di QlikView come soluzione del gruppo Sme.Up e in che modo QlikView si interfaccia con Sme.Up ERP per la ripresa dati.

Nello specifico verranno illustrati i seguenti aspetti : 

- QlikView :  soluzione leader di mercato
- Cosa si intende e cosa contiene un documento Qlik (.qvw)
- Con quali modalità QlikView si collega a Sme.Up per accedere ai dati in esso contenuti

NB. La parte relativa alla presentazione dei dati (front-end grafico), che consente la creazione di tutta la reportistica di Qlik, non è obiettivo di questo documento.

QlikView è un software che consente a tutti i tipi di utenti, dai principianti agli esperti di recuperare e facilmente i dati da qualsiasi fonte :  da un database come SQL Server o Oracle oppure da file di Excel, XML o di testo.
In particolare QlikView recepisce i dati di Sme.UP attraverso connessioni ODBC o con collegamenti integrati con FUN di Sme.UP attraverso un'interfaccia automatica in terminal service.



# 1.2 QlikView :  soluzione leader di mercato
Negli ultimi vent'anni le aziende si sono concentrate sull'automatizzazione dei loro processi di business e sull'applicazione di tecnologie tradizionali di Business Intelligence per reperire e mostrare i dati "intrappolati" nei sistemi gestionali sottostanti.
Molte di queste implementazioni però non sono andate a buon fine. Gli utenti finali che si supponeva dovessero essere aiutati da questi enormi investimenti ad incrementare le prestazioni e i risultati, stanno ancora lottando per ottenere l'informazione appropriata al momento giusto per migliorare l'efficacia delle proprie decisioni giornaliere. Il costo di queste complesse implementazioni è stato enorme.

L'industria della Business Intelligence sta attraversando un momento di radicale cambiamento guidato da alcune organizzazioni 'visionarie'. L'impatto maggiore arriva dalle tecniche di analisi e reporting in-memory che portano semplicità, flessibilità e scalabilità anche nei progetti di Business Intelligence più ambiziosi, con il risultato di uno sviluppo più rapido di soluzioni analitiche altamente scalabili ed efficaci ad una frazione del costo delle soluzioni tradizionali di BI.
QlikView è leader mondiale nelle tecniche di analisi in-memory ed è riconosciuta come la piattaforma di Business Intelligence con il più rapido tasso di diffusione al mondo. QlikView propone una nuova classe di soluzioni analitiche facili da utilizzare, veloci e flessibili che supporta gli individui nel miglioramento delle prestazioni delle organizzazioni nelle quali operano e nel governo dell'innovazione e del cambiamento. QlikView utilizza un'innovativa tecnologia associativa brevettata, che elabora dinamicamente i dati in memoria, per rendere drasticamente più semplice lo sviluppo, l'utilizzo e la manutenzione di sofisticate applicazioni di analisi e reporting.




# 1.3 Documento Qlik (.qvw)
Un'applicazione qlikview è completamente contenuta all'interno di un documento Windows con estensione .qvw. Il documento Qlik contiene sia la parte di programmazione e di modellazione dello script che serve per il caricamento e l'ottimizzazione dei dati, sia la parte di interfaccia utente.
La parte dello script deve essere fatta dal programmatore :  infatti è necessaria una profonda conoscenza degli strumenti disponibili e della struttura della base dati per potere caricare correttamente i dati. Per la parte di interfaccia e di presentazione dei dati invece possiamo suddividere gli interventi in due momenti distinti :  inizialmente servono le competenze di un programmatore per progettare e organizzare le modalità di esposizione del dato, ma una volta consegnato il progetto l'utente finale può in autonomia personalizzarsi le estrazioni esistenti o crearsi estrazioni semplici con una conoscenza base del prodotto.

In dettaglio, in un documento .qvw troviamo : 

-  Script di importazione dati
-  Database associativo relativo ai dati caricati
-  Tabelle, grafici e cruscotti per la presentazione dei dati


## 1.3.1 Accesso ai dati Sme.UP
Nei progetti dove è presente Sme.UP ERP, si utilizzano 3 modalità di connessione al database : 

-  Accesso diretto ODBC / OLE DB
-  Accesso attraverso estrazioni dati predisposte (tabelle D9)
-  Accesso Web utilizzando le FUN di Sme.UP

### 1.3.1.1 Accesso diretto ODBC / OLE DB
E' necessario :  dichiarare la stringa di connessione Inserire l'istruzione sql dopo la parola chiave sql.

![D9QLIK_01](http://localhost:3000/immagini/D9QLIK_01/D9QLIK_01.png)

Si usa Principalmente per l'accesso a file statistici, nei quali sono rappresentati per esteso valori e attributi. Per esempio viene utilizzato per leggere il V5STAT.

Qlikview utilizza come nome del campo la descrizione del campo stesso ed associa automaticamente i nomi uguali; per questo motivo spesso serve rinominare i campi già in fase di estrazione. Se è necessario rinominare solo alcuni campi, si può utilizzare il comando "as" per creare degli alias. Nel caso in cui serve rinominare in maniera completa e strutturata un intero file, la nomenclatura campi può essere fatta attraverso un foglio Excel o csv di mapping.


 :  : R01 Vantaggi
Velocità di caricamento poiché solitamente durante l'accesso al database non vengono effettuati calcoli, in quanto i dati sono già scritti.

 :  : R01 Svantaggi
Non è possibile utilizzare le funzioni Sme.Up, parametri e OAV.
I campi devono essere rinominati, non si possono solitamente usare i nomi originali dei campi all'interno del database.


### 1.3.1.2 Accesso attraverso estrazioni predisposte (tabelle D9)
E' necessario configurare le estrazioni tramite le tabelle D9B, D9C.
I nomi dei campi possono essere definiti direttamente dall'estrazione Nello script è necessario generare le istruzioni di Caricamento (fig. 1.4).

![D9QLIK_05](http://localhost:3000/immagini/D9QLIK_01/D9QLIK_05.png)
Le estrazioni poi devono essere schedulate per garantire l'aggiornamento dei file .csv generati.

 :  : R01 Quando si usa
Per dati anagrafici, per l'estrazione dei quali è possibile confezionare tabelle personalizzate per ogni progetto

 :  : R01 Nomenclatura campi
Le intestazioni di colonna devono necessariamente essere univoche. Se l'estrazione viene appositamente progettata, in QlikView i campi non devono essere rinominati.
Se si utilizza un'estrazione già sviluppata, potrebbe essere necessario rinominare.

 :  : R01 Vantaggi
Utilizzo delle logiche applicative di Sme.UP :  OAV e api Sme.UP di calcolo valori.
Le tabelle possono essere caricate direttamente con minimi interventi nello script di Qlikview. Le estrazioni possono essere configurate liberamente, senza dover rispettare una struttura statica, in modo semplice e tabellare.

 :  : R01 Svantaggi
E' necessario configurare un'estrazione. Esiste un limite sulla lunghezza massima della stringa di dati estratta. La schedulazione notturna dell'estrazione deve essere sincronizzata con l'aggiornamento di QlikView.

 :  : R01 Caratteristiche
La fase di calcolo dei dati (OAV, Valori ....) è sganciata dalla fase di aggiornamento dati QlikView. Qlikview legge una tabella precedentemente calcolata

### 1.3.1.3 Accesso WEB utilizzando le FUN di Sme.UP

Il connettore per l'accesso ai dati di Sme.UP ERP tramite lo script di QlikView, sfrutta le potenzialità dei servizi FUN Sme.UP, tramite delle richieste HTTP inoltrate ad un webserver propriamente configurato (nelle installazioni fatte è stato utilizzato GlassFish).

In dettaglio, essendo QlikView in grado di effettuare richieste web (HTTP, FTP, ...) e di analizzare dei dati in formato XML, il processo può essere riassunto : 

- Richiesta HTTP inoltrata da QlikView al web server GlassFish
- Richiesta di esecuzione del servizio Fun inoltrata da GlassFish a Sme.UP ERP
- Elaborazione della FUN richiesta da parte di Sme.UP ERP e incapsulamento del risultato in uno streaming XML (lo stesso normalmente utilizzato per gli oggetti MATRICE delle schede di Looc.UP)
- Inoltro dello streaming XML al webserver GlassFish da parte di Sme.UP ERP
- Inoltro dello streaming XML a QlikView da parte del webserver GlassFish
- Analisi dello streaming XML da parte dello script di QlikView e normalizzazione dei dati in un file qvd o in una tabella logica

E' necessaria quindi la conoscenza delle FUN in modo che si sia in grado di creare delle FUN che ritornino i dati in formato matriciale.
Le FUN devono essere inserite in una chiamata http nello script QlikView (fig. 1.5)


![D9QLIK_03](http://localhost:3000/immagini/D9QLIK_01/D9QLIK_03.png)


 :  : R01 Nomenclatura campi
Come già detto in precedenza, QlikView utilizza come nome del campo la descrizione del campo stesso ed associa automaticamente i nomi uguali; per questo motivo spesso serve rinominare i campi già in fase di estrazione. Per rinominare in maniera completa e strutturata un intero file, la nomenclatura campi può essere acquisita attraverso una FUN specifica.
In particolare la struttura dei campi di un file può essere descritta attraverso uno schema contenuto nello script SCP_QRY di riferimento.

![D9QLIK_02](http://localhost:3000/immagini/D9QLIK_01/D9QLIK_02.png)
La FUN che caricherà la struttura dei campi dovrà richiamare lo schema definito in SCP_QRY attraverso un una chiamata del tipo F(EXB;JASER_02S;FMI.EXB) 1(Q2;IDV5STAT0F;S/QLIKVEN) dove QLIKVEN è lo schema descritto nello script SCP_QRY.

 :  : R01 Caratteristiche
La fase di calcolo dei dati (OAV, Valori ....) è contestuale alla fase di aggiornamento dati QlikView.
Qlikview effettua la richiesta http ed attende la risposta al termini dei calcoli iSeries.

 :  : R01 Vantaggi
Pieno utilizzo delle logiche applicative detenute da Sme.UP, utilizzo OAV, api Sme.Up di calcolo valori. Essendo un servizio a chiamata, non è necessario schedulare processi notturni lato iSeries.

 :  : R01 Svantaggi
E' necessario configurare un'estrazione.
I tempi di aggiornamento richiesti potrebbero allungarsi in funzione del numero di righe da estrarre e della complessità e numero di calcoli da effettuare.

## 1.3.2 Modello associativo

Il modello dati associativo rappresenta il cuore dell'applicazione.
Viene automaticamente generato e modificato da Qlik, al termine dell'esecuzione dello script di importazione dati.

Un esempio di modello evidenzia alcune particolarità : 
Lo schema dati è solitamente misto Star-Snowflake schema
Il nome dei campi è determinante, definisce i legami tra i dati all'interno del modello associativo


![D9QLIK_04](http://localhost:3000/immagini/D9QLIK_01/D9QLIK_04.png)


 :  : R01 Considerazioni
I collegamenti fra due tabelle vengono fatti in automatico da Qlikview fra campi con lo stesso nome. Per questo motivo il nome dei campi deve essere progettato con cura durante la preparazione dei dati da caricare in QlikView e non può essere acquisito passivamente da un database progettato con altre logiche.



## 1.3.3 Struttura dei documenti Qlik e accesso ai dati Sme.Up.

Il documento .qvw contiene anche tutta la parte di visualizzazione del dato. Gli oggetti disponibili in Qlikview possono essere modellati secondo le esigenze del cliente.
Alcune operazioni possono essere eseguite direttamente dall'utente finale.

# 1.4 Salvataggio dati in Qlikview (.qvd)

Qlik permette salvare dati in un formato proprietario .qvd Il salvataggio in qvd rende il successivo reload performante rispetto alla lettura diretta da AS400.
I file .qvd infatti vengono utilizzati per effettuare un aggiornamento dati incrementale.

 :  : R01 Obiettivi
Ottimizzazione tempi aggiornamento

 :  : R01 Utilizzo
Nelle tabelle dei documenti, gestendo una data limite per i dati consolidati, permette di caricare dati storici da qvd con l'aggiunta dei soli dati recenti da as400.
Nelle tabelle anagrafiche, l'utilizzo dei file qvd permette di caricare le anagrafiche una sola volta direttamente dal gestionale e di poter riutilizzare la stessa anagrafica in tutte le applicazioni Qlikview collegate.

 :  : R01 Esempio
- Carico l'anagrafica articoli con il connettore WEB-FUN
- Salvo la mia anagrafica in un file Articoli.qvd
- Utilizzo la mia anagrafica rileggendola da Articoli.qvd in tutte le applicazioni del progetto (Vendite, Acquisti, Magazzino..)



# 1.5 Requisiti di Sistema

Prima di procedere all'installzione di QlikView è bene controllare quali siano i requisiti di sistema necessari per il corretto funzionamento dell'applicazione.

Per quanto riguarda QlikView versione Desktop : 




| 
| .COL Txt="QlikView Desktop" LunAut="1" A="L" |
| ---|----|
| 
| .COL Txt="32-bit (x86) " LunAut="1" A="L" |
| 
| .COL Txt="64-bit (x64) " LunAut="1" A="L" |
| Operating system | Windows XP SP3 | Windows XP Professional x64 SP2 |
|  | Windows Vista | Windows Vista x64 |
|  | Windows 7 | Windows 7 x64 |
|  | Windows Server 2003 | Windows 8 x64 |
|  | Windows Server 2008 | Windows Server 2003 x64 Edition |
| | | Windows Server 2008 x64 Edition |
|  | | Windows Server 2008 R2 |
|  | | Windows Server 2012 |
|  |
| Processor | Intel Core Duo or higher recommended | Intel Core 2 Duo or higher recommended |
|  |
| Memory | 1 GB minimum. Depending on data volumes more may be required | 2 GB minimum. Depending on data volumes more may be required |
|  |
| Disk space | 250 MB total required to install | 300 MB total required to install |
|  |
| Security | Microsoft Active Directory | Microsoft Active Directory |
|  | NTLM | NTLM |
|  | Third-party security | Third-party security |
| 


Per quanto riguarda QlikView versione Server : 


| 
| .COL Txt="QlikView Server" LunAut="1" A="L" |
| ---|----|
| 
| .COL Txt="32-bit (x86)" LunAut="1" A="L" |
| 
| .COL Txt="64-bit (x64)" LunAut="1" A="L" |
| Platform | Windows 74 | Windows XP Professional x64 SP2 |
| |Windows Server 2003 | Windows Vista x64 |
| |Windows Server 2008 | Windows 7 |
| ||Windows Server 2003 x64 Edition |
| ||Windows Server 2008 x64 Edition |
| ||Windows Server 2008 R2 |
| ||Windows Server 2012 |
|  |
| Processor | Intel Core Duo compatible or higher recommended | Multi-core x64 compatible processors |
|  |
| Memory | 4 GB minimum. Depending on data volumes more may be required | 8 GB minimum. Depending on data volumes more may be required |
|  |
| Disk space | 450 MB total required to install | 450 MB total required to install |
|  |
| Security | Microsoft Active Directory | Microsoft Active Directory |
|  | NTLM | NTLM |
|  | Third-party security | Third-party security |
|  |
| Web server | QlikView web server | QlikView web server |
| |Microsoft IIS 6 or 7 | Microsoft IIS 6, 7, 7.5 or 8 |
|  |
| Management console | Microsoft Internet Explorer 7, 8, 9 & 10 | Microsoft Internet Explorer 7, 8, 9 & 10 |
| |Firefox 18 | Firefox 18 |
|  |
| .NET framework | 4.0 | 4.0 |
|  |
| 





