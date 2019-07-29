# Introduzione
I grafici sono rappresentazioni di dati numerici.

La caratteristica principale dei grafici è l'impatto visivo che consente di interpretare facilmente il confronto tra dati, nonché gli schemi e le tendenze da essi generati.

![LOCEXA_01](http://localhost:3000/immagini/MBDOC_OPE-LOCEXA_01/LOCEXA_01.png)
In Looc.Up qualsiasi servizio che presenta una matrice può anche presentare gli stessi dati della matrice in forma di grafico, per far questo è necessario specificare quale colonna della matrice sia da considerare come asse (è ammesso un solo asse) e quali colonne siano da considerare come serie (ammesse più serie), asse e serie possono essere già definiti a livello di servizio oppure nel setup del grafico, quando viene presentata una matrice, se questa proviene da un servizio dove sono definiti l'asse e le serie, l'intestazione delle colonne presenta delle icone particolari : 
![LOCEXA_05](http://localhost:3000/immagini/MBDOC_OPE-LOCEXA_01/LOCEXA_05.png)
# Elementi di una finestra di un grafico

## Pannello serie/ dati
Mostra alternativamente le serie (colori assegnati, descrizione, flag di attivazione) ed i dati (matrice con i valori dell'asse e quelli delle serie).
![LOCEXA_02](http://localhost:3000/immagini/MBDOC_OPE-LOCEXA_01/LOCEXA_02.png)Nel pannello delle serie è possibile disattivare o ripristinare una serie.
Nel pannello dei dati si può intevenire manualmente cambiando i numeri oppure aggiungendo nuovi valori, ovvimente queste modifiche hanno effetto solo sul grafico che viene presentato e non sui dati origine forniti da sistema che restano invariati.

## Pannello dei comandi di base
Permettono di intervenire sul grafico, gli stessi comando possono essere impostati nel setup
![LOCEXA_03](http://localhost:3000/immagini/MBDOC_OPE-LOCEXA_01/LOCEXA_03.png)
## Pannello delle opzioni
Permettono la manipolazione della presentazione del grafico, sono funzioni interne al componente non direttamente collegate al setup.
![LOCEXA_04](http://localhost:3000/immagini/MBDOC_OPE-LOCEXA_01/LOCEXA_04.png)
# Setup di un grafico
Permette di definire a livello di scheda la visualizzazione del grafico, nella stessa scheda possiamo avere diversi setup, ciascuno con un proprio nome e con la possibilità di ereditare le impostazioni da un altro setup di grafico.
![LOCEXA_06](http://localhost:3000/immagini/MBDOC_OPE-LOCEXA_01/LOCEXA_06.png)
L'uso delle varie impostazioni è intuitivo, meritano particolare menzione : 
* _2_Imposta come asse, quando non è previsto nel servizio, in questa opzione si deve specificare quale campo considerare come asse
* _2_Imposta le serie, quando non è previsto nel servizio, in questa opzione si devono specificare i campi da considerare come serie separati da un pipe "|"
* _2_Imposta massimo asse X, da usare in grafici di grandi dimensioni se si vuole avere una visualizzazione su più pagine con la possibilità di spostarsi orizzontalmente grazie alla barra di scorrimento. Può essere utile anche per impotare l'ampiezza massima quando non abbiamo ancora tutti i valori dell'asse
* _2_Imposta massimo asse Y, come il precedente ma riferito alle serie
* _1_Tab. Identificazione - Nome, è il nome del setup, da usare in grafici con setup diversi
* _1_Tab. Identificazione - Eredita da, è il nome del setup dal quale ereditare le impostazioni
