## ESEMPI LOA08

In questa scheda è fruibile una serie di esempi sull'utilizzo del LOA08, nelle sue varie modalità. Questi esempi sono costruiti all'interno dello script COS_A08 in SCP_SCHESE.

 :  : TAG Id="A" Txt="Esempio A"

### A. Confronto Utilizzo xx_G30/CF/Griglia Servizio

In questo esempio vengono evidenziate le differenze di richiamo (come cambiano i parametri di richiamo della scheda), di definizione (in un caso vedo il sorgente del programma, nell'altro il sorgente dello script e nell'altro quello del servizio) e di funzionalità (in particolare il nome delle variabili, che nel caso nel pgm _G30 se non viene sfruttata la possibilità di indicare il nome della variabile, porta a creare le variabili G30nnn, mentre nel caso del configuratore e della griglia è nativa l'indicazione del nome della variabile)

 :  : TAG Id="B" Txt="Esempio B"

### B. Orizzontale/Verticale

Vengono evidenziati i risultati ottenibili applicando l'orientamento orizzontale e verticale, presentando o meno anche le decodifiche dei campi.

 :  : TAG Id="C" Txt="Esempio C"
### C. Modalità di Conferma

Vengono evidenziate le varie di conferma dell'esecuzione delle scelte, suddivise fra :  esecuzione immediata (che presuppone che non vi siano campi obbligatori), esecuzione su invio, esecuzione su F06.

 :  : TAG Id="D" Txt="Esempio D"
### D. Con Oggetto J1

In questo esempio viene semplicemente evidenziato come sia possibile superare il limite della lunghezza caratteri a 20 caratteri delle G30 utilizzabili nel 5250. Questo limite non sussiste più.

 :  : TAG Id="E" Txt="Esempio E"
### E. Con Utilizzo Exit

In questo esempio vengono applicate ad una richeista parametri le logiche aggiuntive definite da un pgm di exit.

 :  : TAG Id="F" Txt="Esempio F"
### F. Con Formato Video

In questo esempio viene evidenziato come sia possibile applicare un formato video alla richiesta parametri. (Naturalmente deve esservi compatibilità fra i nomi dei campi video e delle variabili previste per le domande).

 :  : TAG Id="G" Txt="Esempio G"
### G. Con Passaggio Risposte.

In questo esempio viene evidenziato l'utilizzo dei parametri RIS e RIV che permette di passare dei parametri pre-compilati nel richiamo della scheda stessa e di come trattarli.

 :  : TAG Id="H" Txt="Esempio H"
### H. Sola finestra di scelta

In questo esempio viene evidenziata la forma di richiamo del loa08 atta alla sola memorizzazione delle risposte.

 :  : TAG Id="I" Txt="Esempio I"
### I. Utilizzo con variabili G91

In questo esempio viene evidenziata la possibilità di appoggiare la ripresa e la memorizzazione delle risposte in un contesto della £G91.
 :  : TAG Id="J" Txt="Esempio J"
### J. Variabile intestazioni SI

Se valorizzato il parametro SI a 1 si può sfruttare graficamente la variabile (o parametro di input) A08_SI. In essa in modo descrittivo vengono riportate le scelte effettuate.

 :  : TAG Id="K" Txt="Esempio K"
### K. Utilizzo Oggetto di Riferimento Query Q1

E' possibile utilizzare come oggetto di riferimento il Q1. In questo caso invece di passare come oggetto di riferimento un CF verrà passato un oggetto di tipo Q1. Le domande verranno poi reperite a partire dalla struttura dell'oggetto Q1 passato.

 :  : TAG Id="L" Txt="Esempio L"
### L. Utilizzo attributi Web

In questo esempio vengono evidenziati alcuni attributi tipici del web, Layout e ConfirmLabel.
