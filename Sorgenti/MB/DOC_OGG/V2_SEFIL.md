# Estensioni File Sme.up
Gli oggetti SEFIL sono oggetti che rappresentano le possibili estensioni file "proprietarie Sme.up"

Allo stato attuale sono presenti i seguenti tipi file gestiti da Loocup.


- File XML prodotti da Smeup
-- Attuale estensione **XML** o **SXF**(Smeup Xml File)
-- Questi file sono i file dati che definiscono le strutture dati di comunicazione Smeup-Loocup. Possono essere file Xml di Matrice, albero, documentazione, messaggi
-- Ipotesi di nuova estensione **S01**
- File di setup
-- Attuale estensione **SIF**
-- Questi file Xml contengono i setup per la generazione di documenti con sorgenti LTX, TEX, DBK, SDF  ed INV
-- Ipotesi di nuova estensione **S02**
- File di log di tipo 1
-- Attuale estensione **LOG**
-- File di log prodotti dai eseguibili Loocup :  Loocup.jar, SmeTray.exe, SmeUIClt.exe e dalla /copy G53 (questi ultimi sull'IFS dell'AS400)
-- Ipotesi di nuova estensione **S03**
- File di log di comunicazione
-- Attuale estensione **CMN**
-- File di log prodotti dalla comunicazione fra il componente base Loocup.jar e i dipendenti SmeTray.exe e SmeUIClt.exe
-- Ipotesi di nuova estensione **S04**
- File Latex : 
-- Attuale estensione **LTX**
-- Questi file, contenenti i sorgenti della documentazione in formato Latex, vengono sottoposti a compilazione tramite MikTex per generare dei PDF
-- Ipotesi di nuova estensione **S05**
- File Wiki
-- Attuale estensione **TXE**
-- Questi file vengono spostati, via FTP, su un server WIKI dove vengono in tal modo pubblicati
-- Ipotesi di nuova estensione **S06**
- File Docbook
-- Attuale estensione **DBK**
-- Questi file, contenenti i sorgenti Docbook in un dialetto xml, dovranno venire sottoposti a compilazione tramite prodotti che effettuano la trasformazione Docbook-->PDF
-- Ipotesi di nuova estensione **S07**
- File sorgente documentazione Smeup : 
-- Attuale estensione **SDF**
-- Questi file con estensione (**S**meup **D**ocumentation **F**ile, contenenti i sorgenti della documentazione Smeup, vale a dire il contenuto di uno o più membri di documentazione di Smeup, vengono compilati dal motore proprietario Loocup di generazione HTML e PDF
-- Ipotesi di nuova estensione **S08**
- File sorgente documenti G53
-- Attuale estensione **INV**
-- Questi file, contenenti il sorgente di documenti da generarsi tramite G53, vengono compilati dal motore di tale /copy allo scopo di produrre documenti PDF
-- **Per adesso nessuna modifica**



Una volta che l'elenco sopra riportato sarà completo, racchiuderà tutti i file che in Looc.up vengono riconosciuti, creati, etc.

