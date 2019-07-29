# Premesse
Il modulo MUCONV è stato pensato per fornire supporto alla comprensione ed all'analisi degli oggetti derivanti dalla conversione al Multipiattaforma.
Sono presenti dei cruscotti in cui sono evidenziati i dati di conversione.

Esempio di cruscotto riepilogativo : 
![MUCONV_01](http://localhost:3000/immagini/MUCONV_05/MUCONV_01.png)
# Consultazione conversione
In questa sezione vengono analizzati i dati del file MUCONV0F, file deputato alla raccolta di informazioni sulla conversione degli oggetti per il multipiattaforma.
I dati presenti nel file MUCONV0F sono strutturati per oggetto di sistema origine, e possono contenere dei messaggi di warning o di errore.
Il messaggio di tipo Warning (giallo - gravità 20) significa che siamo di fronte ad un comportamento dell'oggetto origine non ancora supportato o comunque in fase di studio.
Il messaggio di tipo Error (rosso - gravità 30) significa che siamo di fronte ad un comportamento dell'oggetto origine che non verrà mai supportato.
In questo caso bisogna valutare la possibilià di una modifica del codice sorgente originale.
Quindi l'analisi si concentra maggiormente sulle anomalie riscontrate durante il processo di estrazione.
I componenti che vengono analizzati sono di 3 tipi : 
* OS Operating system - oggetti di sistema operativo
* DB Database - oggetti di database
* IL Integrated language - oggetti derivanti dai programmi (RPG,CLP)
Il primo gruppo raccoglie tutto ciò che riguarda il sistema operativo, quindi oggetti di tipo comando (*CMD) utenti (*USRPRF) etc.
Il secondo gruppo raccoglie tutto ciò che riguarda il database, quindi oggetti di tipo *FILE
Il terzo gruppo raccoglie tutto ciò che riguarda il linguaggio, quindi oggetti di tipo *PGM
I vari grafici che sono proposti si riferiscono alla percentuale di convertibilità del sistema.

### Conversione componente
In quest'area è possibile analizzare la percentuale di convertibilità suddivisa sui 3 componenti principali.
Viene fornita una matrice con i dati riepilogativi per componente (OS,DB,IL), ed il suo relativo dettaglio in formato grafico suddiviso per messaggio (Error, Warning)
con la possibilità di estrarre tutti gli oggetti che concorrono a quello specifico messaggio.
E possibile scegliere la libreria come parametro di filtro
![MUCONV_01A](http://localhost:3000/immagini/MUCONV_05/MUCONV_01A.png)
### Conversione database
In quest'area è possibile analizzare la percentuale di convertibilità del database suddivisa per applicazione Sme.up (TAB£A), dettaglio completo.

__Applicazione Sme.Up__
Viene fornita una matrice con dati riepilogativi per applicazione ed il suo relativo dettaglio in formato grafico suddiviso per messaggio (Error, Warning)
con la possibilità di estrarre tutti gli oggetti che concorrono a quello specifico messaggio.
Come parametro di filtro è possibile scegliere la libreria convertita.
![MUCONV_01B](http://localhost:3000/immagini/MUCONV_05/MUCONV_01B.png)
  __Dettaglio completo__
Viene fornita una matrice con il massimo dettaglio dell'oggetto convertito, in cui è possibile visualizzare le eventuali anomalie legate ad un oggetto specifico.
Come parametro di filtro è possibile scegliere la libreria convertita, l'oggetto convertito, o il codice messaggio MSGMU.
![MUCONV_01C](http://localhost:3000/immagini/MUCONV_05/MUCONV_01C.png)
### Conversione linguaggio
In quest'area è possibile analizzare la percentuale di convertibilità del linguaggio suddivisa per applicazione Sme.up (TAB£A), modulo Sme.Up (TAB£AMO), dettaglio completo.

__Applicazione Sme.Up__
Viene fornita una matrice con dati riepilogativi per applicazione ed il suo relativo dettaglio in formato grafico suddiviso per messaggio (Error, Warning)
con la possibilità di estrarre tutti gli oggetti che concorrono a quello specifico messaggio.
Come parametro di filtro è possibile scegliere la libreria convertita.
![MUCONV_01D](http://localhost:3000/immagini/MUCONV_05/MUCONV_01D.png)
  __Dettaglio completo__
Viene fornita una matrice con il massimo dettaglio dell'oggetto convertito, in cui è possibile visualizzare le eventuali anomalie legate ad un oggetto specifico.
Come parametro di filtro è possibile scegliere la libreria convertita, l'oggetto convertito, o il codice messaggio MSGMU.
![MUCONV_01E](http://localhost:3000/immagini/MUCONV_05/MUCONV_01E.png)
### Conversione sistema
In quest'area è possibile analizzare la percentuale di convertibilità dei seguenti oggetti di sistema : 
* Comando
* Area dati
* Coda dati
* File
* Descrizione lavori
* File messaggi
* Programma
* Utente
* User space

  __Albero oggetti__
Viene fornito un albero di oggetti di sistema per i quali si può visualizzare il dettaglio della conversione.
![MUCONV_01F](http://localhost:3000/immagini/MUCONV_05/MUCONV_01F.png)
  __Dettaglio__
Viene fornita una matrice con il massimo dettaglio dell'oggetto convertito, in cui è possibile visualizzare le eventuali anomalie legate ad un oggetto specifico.
Come parametro di filtro è possibile scegliere la libreria convertita, l'oggetto convertito, o il codice messaggio MSGMU.
![MUCONV_01G](http://localhost:3000/immagini/MUCONV_05/MUCONV_01G.png)