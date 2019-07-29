## La reportistica in Looc.up
La reportistica in Looc.up utilizza un motore di generazione chiamato **JasperReport** ed incluso nella distribuzione standard di Looc.up.
Il componente Looc.up preposto alla generazione della reportistica è il componente REP.

## Il componente REP
La generazione del report in Looc.up si applica in due differenti contesti : 
 * La generazione del report di una matrice, utilizzabile attraverso le funzioni che le sezioni matrice mettono a disposizione.
 * La generazione del report originato da uno script di scheda _particolare_ (con una struttura report-subreport) e tramite una funzione di Loocup.

### Elementi generali
E' possibile definire dei template di documento che poi il generatore utilizzerà come base per generare il documento finale. Un insieme di template standard è incluso nella distribuzione standard di Looc.up all'interno della cartella LoocUP_XML/REP.
Tali template si possono visualizzare e modificareare tramite uno strumento chiamato **iReport_n_ che consente anche la creazione di nuovi template personalizzati.
Looc.UP si interfaccia ad una versione specifica di iReport. Tale versione è scaricabile dal nostro sito
 :  : DEC T(J1) P(URL) [http://www.smeup.com/loocup_downloads/tools/iReport-1.3.3-windows-installer.zip](http://www.smeup.com/loocup_downloads/tools/iReport-1.3.3-windows-installer.zip)
Informazioni aggiuntive sono disponibili direttamente sul sito del prodotto (http://jasperforge.org/sf/projects/ireport)
Di seguito iReport in azione
![ireport](http://localhost:3000/immagini/LOCREP_INT/ireport.png)
Una volta definiti i template è possibile, ad esempio basandosi su una scheda predisposta per tale scopo, generarne il report prevedendo il lancio della stessa funzione che apre la suddetta "scheda predisposta" sostituendo il componente EXD con REP (es. :  F(EXD;*SCO;)..... diventerà F(REP;*SCO;)....... )
![scheda](http://localhost:3000/immagini/LOCREP_INT/scheda.png)oppure, su una sezione matrice di una scheda, generarne il report anche in questo caso sostituendo il componente EXB con REP (es. :  F(EXB;LOSER_XX;)..... diventerà F(REP;LOSER_XX;)....... ).
Come ultima possibilità si può generare il report di una matrice attraverso le funzioni specifiche della sezione
![visual](http://localhost:3000/immagini/LOCREP_INT/visual.png)
Attraverso le impostazioni di setup si possono decidere il formato del documento, il tipo di file da generare, la collocazione, etc.
![setupREP](http://localhost:3000/immagini/LOCREP_INT/setupREP.png)Il file che viene generato è un file PDF
![pdf](http://localhost:3000/immagini/LOCREP_INT/pdf.png)che può essere fornito opzionalmente di una copertina
![pdfCover](http://localhost:3000/immagini/LOCREP_INT/pdfCover.png)
Nel caso di Visualizzazione di una matrice come Report eventuali impostazioni di visualizzazione, raggruppamento, ordinamento, filtro, totalizzazione della sezione presenti al momento della richiesta vengono mantenute anche nel report

### Elementi tecnici
La generazione dei report utilizza 3 differenti repository : 
 * La cartella degli script di template :  se è presente nella configurazione di Loocup (file scp_clo) la variabile di nome **REP.SRC** essa viene interpretata come percorso da cui pescare i files di template. Se tale variabile non è presente viene assunto il default **LOOCUP_XML/REP** presente nella cartella di installazione di Looc.up.
 * La cartella temporanea di lavoro :  se è presente nella configrazione di Loocup la variabile Loocup di nome **REP.TMP** essa viene interpretata come percorso da cui pescare i files di template. Se tale variabile non è presente viene assunto il default **%Temp%\LOOCUP_TMP\<codicesessione>\REP** presente nella cartella di installazione di Looc.up. In tale cartella vengono creati files temporanei utili alla generazione del report.
 * La cartella di destinazione dei report generati :  se è presente nella configurazione di Looc.up (file scp_clo) la variabile Looc.up di nome **REP.OUT** essa viene interpretata come percorso in cui creare i files dei report. Se tale variabile non è presente viene assunto il default **LOOCUP_OUT/REP** presente nella cartella di installazione di Looc.up. Se non viene specificato differentemente nel setup in tale cartella vengono creati files finali del report.

## Il report di una matrice
Di una qualsiasi sezione matrice di una scheda è possibile generare un report. Tramite il tasto destro del mouse sul tab di una sezione matrice, selezionando **Visualizza come -> Report** parte la funzione di creazione del report. Viene eventualmente richiesto il setup di generazione del report che raccoglie informazioni utili alla generazione (formato, orientamento, ecc...). Per l'impostazione del setup standard associato al report di una matrice si veda il relativo capitolo al'interno della presente documentazione.

## La funzione Report
La funzione F(REP;*SCO;) è in grado di generare il report di una scheda se tale scheda è stata costruita con alcune caratteristiche particolari e contiene determinate specifiche nello script.

All'interno degli esempi di LoocUP sono riportati numerosi utilizzi del componente report sia come funzione che associato a una matrice. In ogni caso qualunque matrice di Loocup può essere esportato come report.
