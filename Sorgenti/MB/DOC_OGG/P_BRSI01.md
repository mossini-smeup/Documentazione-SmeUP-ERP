## Interrogazioni
Sono possibili tutte le funzioni classiche di interrogazione.

È possibile interrogare una distinta, sia in esplosione (vengono visualizzati i componenti relativi all'oggetto) che in implosione (vengono mostrati gli assiemi che contengono l'oggetto).

Sono previste varie tipologie di esplosione / implosione, per le quali si rimanda al paragrafo sulle funzioni di esplosione e implosione.

![BR_02_05](http://localhost:3000/immagini/MBDOC_OGG-P_BRSI01/BR_02_05.png)
Nel lista emessa si possono operare delle ulteriori opzioni.

![BR_02_06](http://localhost:3000/immagini/MBDOC_OGG-P_BRSI01/BR_02_06.png)
Si può immettere uno schema di visualizzazione, modificarlo o crearlo.

È possibile anche da qui modificare il tipo di interrogazione, la tipologia della distinta e l'oggetto che si va ad interrogare.


È anche possibile indicare una configurazione (si veda l'apposita documentazione), indicare una quantità dell'assieme, oppure visualizzare solo la distinta valida ad una data particolare.

Si può accedere ad una finestra con altre impostazioni avanzate di interrogazione : 

![BR_02_07](http://localhost:3000/immagini/MBDOC_OGG-P_BRSI01/BR_02_07.png)
In aggiunta, sono previste delle opzioni a livello riga ('?' per avere la lista) : 

![BR_02_08](http://localhost:3000/immagini/MBDOC_OGG-P_BRSI01/BR_02_08.png)
### Tipi di esplosione/implosione
Per esplosione si intende la visualizzazione dei componenti dato un assieme.
Sono possibili varie tipologie di esplosione, qui elencate : 

- _2_al livello :  mostra tutti i componenti di primo livello, a prescindere dalla data di validità e dalla configurazione
![BRDIST_01](http://localhost:3000/immagini/MBDOC_OGG-P_BRSI01/BRDIST_01.png)
- _2_scalare :  mostra i componenti a tutti i livelli che sono contenuti nell'assieme. Anche questo tipo non considera le date di validità e la configurazione
![BRDIST_02](http://localhost:3000/immagini/MBDOC_OGG-P_BRSI01/BRDIST_02.png)
- _2_di produzione :  mostra i componenti al primo livello non fittizio, e visualizza solamente i legami validi
![BRDIST_03](http://localhost:3000/immagini/MBDOC_OGG-P_BRSI01/BRDIST_03.png)
- _2_di produzione totale :  mostra i componenti a tutti i livelli, esplodendo completamente un assieme, mostrando solo i legami validi
![BRDIST_04](http://localhost:3000/immagini/MBDOC_OGG-P_BRSI01/BRDIST_04.png)
- _2_ai materiali di base :  mostra tutti e solo i componenti al livello più basso (foglie)
![BRDIST_05](http://localhost:3000/immagini/MBDOC_OGG-P_BRSI01/BRDIST_05.png)
- _2_riepilogata :  percorre tutti i rami della distinta ed esegue la somma a parità di articolo
![BRDIST_06](http://localhost:3000/immagini/MBDOC_OGG-P_BRSI01/BRDIST_06.png)
- _2_riepilogata ai materiali base :  esegue la somma a parità di articolo delle foglie
![BRDIST_07](http://localhost:3000/immagini/MBDOC_OGG-P_BRSI01/BRDIST_07.png)
- _2_riepilogata di produzione :  come l'esplosione di produzione sommando a parità di articolo
![BRDIST_08](http://localhost:3000/immagini/MBDOC_OGG-P_BRSI01/BRDIST_08.png)
Per implosione si intende la visualizzazione degli assiemi a cui appartiene un legame, i vari tipi di implosione seguono la stessa logica (invertita) vista per l'esplosione.

Il tasto F9 stampa la lista visualizzata.
