

## Struttura di Looc.Up e processi in esecuzione

Il client grafico Looc.Up è composto da vari moduli in esecuzione contemporanea. Ognuno di questo moduli presiede al funzionamento di una parte del client grafico e dialoga in continuo con tutti gli altri moduli che compongono il prodotto. Questa struttura di esecuzione modulare permette a Looc.Up di integrare in un unico contesto parti di codice scritte in linguaggi o ambienti diversi, senza però che questa struttura modulare ed eterogenea venga percepita dall'utente finale come un insieme disomogeneo di applicazioni.

## Moduli software di Looc.Up

 T(I moduli principali che compongono il client Looc.Up sono : )
- **Modulo di avvio** :  è il modulo che si occupa delle operazioni di avvio di Looc.Up. Gestisce anche l'integrazione con il modulo di sincronizzazione RSync, dedicato all'upgrade automatizzato.
- **Modulo base** :  è il modulo che presiede alle funzioni di comunicazione e fornisce il framework di base su cui si attestano le comunicazioni tra i moduli operativi. E' scritto in linguaggio Java.
- **Modulo schede** :  è il modulo che gestisce la visualizzazione e il funzionamento delle schede Looc.Up e dei sottomoduli in esse contenuti. E' scritto in linguaggio Delphi.
- **Modulo emulatore** :  modulo che fornisce una versione grafica dell'emulatore telnet 5250, integrata con le funzionalità di Looc.Up. E' scritto in Delphi.


## Lista dei processi Windows attivati da Looc.Up

 T(I processi Windows avviati dal client Looc.Up durante il suo funzionamento sono i seguenti : )
- Per il modulo di avvio :  in alternativa, **Loocup.exe**, **Loocup_w.exe** oppure **Loocup_con.exe**. Dipende da come è stato avviato Looc.Up.
- Per il modulo base :  **SmeBase_w.exe**
- Per il modulo schede :  **SmeTray.exe**
- Per il modulo emulatore :  **SmeUiClt.exe**



La seguente figura, mostra la struttura di esecuzione di una istanza del client Looc.Up, vista dal gestore processi di WIndows.

![LOBASE_106](http://localhost:3000/immagini/LOBASE_035/LOBASE_106.png)
L'esempio riportato è relativo ad una istanza del client Looc.Up avviata utilizzando la finestra grafica per la gestione delle connessioni (processo **Loocup_con.exe**). Il modulo di avvio crea una istanza del modulo base (**SmeBase_w.exe** nella figura) che a sua volta avvia i sottomoduli della scheda (**SmeTray.exe**) e dell'emulatore 5250 (**SmeUiClt.exe**). Per il corretto funzionamento del client Looc.Up tutti i moduli devono essersi attivati correttamente e nell'ordine mostrato nella figura.

Nel caso vengano avviate più istanze di Looc.Up sulla stessa macchina, la struttura dei processi attivi è la seguente : 

![LOBASE_107](http://localhost:3000/immagini/LOBASE_035/LOBASE_107.png)
Si nota che il modulo di avvio Loocup_con non viene replicato per ognuna delle istanze attive ma rimane un'unica istanza.




