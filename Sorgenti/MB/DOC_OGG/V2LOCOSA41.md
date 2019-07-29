 ## Obiettivo
Costruire un dashboard attraverso uno script di configurazione.

## Descrizione
Il dasboard è una rappresentazione grafica strutturata in : 
* 9 righe
* 12 Colonne
Un qualsiasi componente può essere inserito nel dashboard.
L'esplosione dello script non deve superare le 299 righe.

## Attività dell'installatore
L'installatore deve definire il proprio dashboard nel sorgente **SCP_A41**.

### Tag dello script
Elenco delle tag e del loro significato


| 
| .COL Cod="AA" Txt="Tag" A="C" |
| ---|----|
| 
| .COL Cod="BB" Txt="Significato" A="C" |
| ROW.SEZ|Nuova riga |
| DAS.SEZ|Nuovo Dash |
| DAS.SET|Setup dell Dash |
| DAS.FUN|Funzione del Dash |
| DAS.Q3 |Creazione di un filtro al click |
| DAS.DIN|Esecuzione di un dinamismo o di una funzione al click |
| DAS.OGG|Dichiarazione di un oggetto |
| DAS.LIS|Lista di oggetti |
| DAS.ELE|Elenco |
| DAS.OAV|Elenco di OAV |
| DAS.A15|Report |
| 



Ora vediamo in dettaglio gli attributi di ogni tag

### ROW.SEZ Nuova riga
Sono ammesse un massimo di 9 righe visualizzabili simultaneamente per dashboard. Vengono presentate nello stesso ordine con cui sono state inserite nello script.
Ogni Riga può essere estesa occupando la riga sucessiva, in questo caso diminuiscono le righe che possono essere presentati sul dashboard.
 :  : PAR L(TAB)
Attributo|Significato|Descrizione
Txt|Descrizione|Ad uso interno
Aut|Autorizzazione|Se non autorizzato la riga viene esclusa dal dashboard. La classe è la**LO.EXD**con Funzione**A41.**seguita dal nome dello script
Usr|Autorizzazione user level|Se non si dispone del livello minimo richiesto la riga viene esclusa dal dashboard. Classe**USRLVL**
Dim|Dimensione|Occupazione del dash in numero di colonne, minimo 1.


### DAS.SEZ Nuovo dash
Sono ammessi  un massimo di 12 dash visualizzabili simultaneamente per riga. Vengono presentate nello stesso ordine con cui sono state inserite nello script.
Ogni dash può occupare più colonne, in questo caso diminuiscono i dash che possono essere presentati sulla riga.
se non definito l'attributo **ToolBarState** sarà assunto il valore **Invisible**

 :  : PAR L(TAB)
Attributo|Significato|Descrizione
Txt|Descrizione|Titolo del dash
Id|Identificativo|Codice univoco di sezione del dash, non deve essere replicato su altri dash.
Dim|Dimensione|Occupazione del dash in numero di colonne, minimo 1.
Cmp|Componente|Indica il componente grafico che verrà utilizzato dal dash


### DAS.SET Setup del dash
Il setup del dash dipende dal componete utilizzato, fare riferimento ai vari componenti per i valori ammessi.
Se non definito viene istanziato un setup di default con il parent "DAS.001"

Elenco dei componenti supportati : 
* ACC Accordion
* BTN Bottoniera
* BOX BoxList (SV)
* CAL Calendario
* CAM Camera
* CDE Code editor
* CHA Grafico
* DEV Device
* GAU Cruscotto
* GNT Gantt
* HTM HTML/Browser
* IMG Immagine
* IML Lista immagini
* INP Pannello di Input
* LAB Label
* MAT Matrice
* MIN Mind Map
* MSG Messaggio
* OCX Controllo ActiveX
* OGN Organigramma
* OUT Pannello di Output
* PDF Pdf Viewer
* PRW Preview
* TMP TreeMap
* SCH Scheda
* SEM Semaforo
* SHE SpreadSheet
* SPL Spotlight
* TRE Albero
* TXT Testo
* TCL Tag Cloud

### DAS.DIN Dinamismo del dash
Il dinamismo si occupa di informare altri dash di eventuali cambiamenti e di invocare altre funzioni specifiche relative al dash.
L'unico dinamismo gestito è il**click**

 :  : PAR L(TAB)
Attributo|Significato|Descrizione
Id|Identificativo|Identivicativo univoco definito nel_DAS.SEZin cui attivare un refresh
F|Funzione|Funzione da eseguire


### DAS.Q3 Creazione di un filtro di campo
Al**click**verrà creato il filtro di campo desiderato, il filtro è sempre di uguaglianza.

 :  : PAR L(TAB)
Attributo|Significato|Descrizione
T|Tipo|Tipo oggeto
P|Parametro|Parametro oggetto
K|Nome filtro|Indica il filtro in cui aggiungere il campo
F|Nome Campo|Nome del campo su cui eseguire il filtro
V|Valore|Valore da filtrare
N|Notifica|iIdentivicativo univoco definito nel_DAS.SEZin cui attivare un refresh


### DAS.FUN Funzione del dash
E' la funzione che si occupa di ritornare le informazioni necessarie alla presentazione grafica del componente scelto

 :  : PAR L(TAB)
Attributo|Significato|Descrizione
F|Funzione|Funzione da eseguire


### DAS.OGG Dichiarazione di un oggetto
Viene restituito un oggetto.

 :  : PAR L(TAB)
Attributo|Significato|Descrizione
T|Tipo|Tipo oggeto
P|Parametro|Parametro oggetto
K|Codice|Codice oggetto
D|Descrizione|Testo libero


### DAS.A15 Interrogazione di un report
Il componete di questo dashboard può assumero solo il valore di scheda.
 :  : PAR L(TAB)
Attributo|Significato|Descrizione
R|Nome|Indica il nome del report
E|Emissione|Indica il tipo di report da richiamare


Elenco dei tipi di emissione disponibili : 
* Matrice
* Drill Down
* Report
* Foglio di lavoro
* Analisi di pareto
* Analisi tabellare
