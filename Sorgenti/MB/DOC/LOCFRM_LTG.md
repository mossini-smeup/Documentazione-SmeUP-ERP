# Da doc. attiva a PDF
In Looc.up è possibile visualizzare la documentazione attiva seguendo vari percorsi, a seconda del tipo di documentazione o dell'argomento trattato.

## Come reperire la documentazione
In generare per reperire documentazione è possibile seguire il seguente percorso : 
My Loocup -> Documentazione
e da qui cliccare sulla scheda **"i documenti"** per visualizzare tutti i documenti presenti.
![LOCFRM_029](http://localhost:3000/immagini/LOCFRM_LTG/LOCFRM_029.png)
Per documentazioni specifiche, come ad esempio documentazione sulle applicazioni o sui componenti, esistono percorsi preferenziali.
Per visualizzare la documentazione relativa alle applicazioni, ad esempio, è possibile seguire il seguente percorso da menù : 
My Loocup -> Applicazioni
e da qui cliccare sull'applicazione desiderata dall'albero **"Le applicazioni"**, e cliccare sulla sottoscheda "Documentazione" per visualizzarne la documentazione attiva suddivisa per tipologia.
![LOCFRM_030](http://localhost:3000/immagini/LOCFRM_LTG/LOCFRM_030.png)
Per visualizzare la documentazione relativa ai componenti, è possibile seguire il percorso da menù : 
My Loocup -> Per lo sviluppatore -> i componenti
e da qui cliccare sul componente desiderato dall'albero **"I componenti grafici e logici"**, e cliccare sulla sottoscheda "Documentazione" per visualizzarne la documentazione attiva suddivisa per tipologia.
![LOCFRM_031](http://localhost:3000/immagini/LOCFRM_LTG/LOCFRM_031.png)
_2_Nota : 
Per visualizzare la documentazione relativa ad un componente di scheda è possibile anche scrivere "h : " + NomeComponente dalla linea di comando della scheda, visualizzata premendo ALT+F9 (o CTRL+F). Se viene scritto solo "h : " viene aperta la documentazione relativa al componente con il fuoco.

## La scheda di un documento (OGDOCU)
Individuato il documento che vogliamo consultare attraverso le navigazioni appena descritte, la scheda di un documento permette una serie di funzionalità che permettono di visualizzare il documento, modificarlo, controllarne la sintassi, esportare in formato PDF o wiki, ...
Queste funzionalità sono suddivise in 3 tab : 

- Documentazione;
- Composizione;
- Set 'n play.


![LOCFRM_032](http://localhost:3000/immagini/LOCFRM_LTG/LOCFRM_032.png)
Nel tab **"Documentazione"** è possibile consultare il documento ed eventualmente modificarlo premendo il tasto F20 - "Gestione documento" per aprire l'editor di testo.
![LOCFRM_033](http://localhost:3000/immagini/LOCFRM_LTG/LOCFRM_033.png)pulsante "Gestione documento")

Nel tab **"Composizione"** è possibile visualizzare le sezioni e sottosezioni, gli oggetti e le immagini contenute nel documento. Nel caso delle immagini è possibile eventualmente anche aprire la cartella del filesystem dove sono contenute,  cliccando sul tab "Cartella", e/o modificare le immagini dall'editor grafico interno di Loocup o da un editor esterno, cliccando sul tab "Immagine" e quindi sul tab "Gestione immagine" o sul pulsante di sezione "Modifica immagine".
![LOCFRM_034](http://localhost:3000/immagini/LOCFRM_LTG/LOCFRM_034.png)
Nel tab **"set 'n play"** è possibile generare il PDF del documento cliccando sulla sottoscheda **"Comandi LATEX"** e da qui selezionare il comando desiderato : 

- "Compilazione - Mod (BAT) -", per generare e salvare il PDF in modalità batch
- "Chiede, Assume apre e non salva", per generare e visualizzare un'anteprima del PDF
- "Chiede, Assume non apre e salva", per generare e salvare il PDF nella cartella  di default di Smeup (DOC o DOC_BOK)
- "Presenta senza chiedere e salva", per generare e salvare il PDF nella cartella  di default di Smeup (DOC o DOC_BOK) senza visualizzare il questionario relativo
- "Presenta senza chiedere e pubblica", per generare e salvare il PDF nella cartella  di default di Smeup (DOC o DOC_BOK) e nella cartella pubblica raggiungibile dal sito web, senza visualizzare il questionario relativo


![LOCFRM_035](http://localhost:3000/immagini/LOCFRM_LTG/LOCFRM_035.png)
![LOCFRM_036](http://localhost:3000/immagini/LOCFRM_LTG/LOCFRM_036.png)di un documento)

Nel caso vi siano errori nella generazione del PDF è possibile fare un'analisi del documento dalla sottoscheda **"Trasformazione"** del tab "set 'n play". In questa sottoscheda è infatti possibile analizzare le conversioni di sintassi da documentazione attiva a LaTeX (anche per singoli tag), così da poter individuare eventuali conversioni errate o mancanti. Cliccando infatti su ogni tag presente nella matrice della sottosezione "memoria" viene visualizzata la conversione in formato LaTeX (ed anche in formato HTML e Wiki) nella sottosezione "Paragrafo". In questa scheda è possibile anche visualizzare l'intera conversione del documento nel formato LaTeX (o eventualmente anche nel formato HTML e Wiki) cliccando sui rispettivi tab "Tutto LaTeX" (o "Tutto HTML", "Tutto Wiki").
![LOCFRM_037](http://localhost:3000/immagini/LOCFRM_LTG/LOCFRM_037.png)