# Generalità
Le viste e le impostazioni colori vengono sempre salvate nella cartella LOOCUP_DAT/GNT presente nella root di  installazione di Looc.UP. Quindi se l'installazione è locale o sincronizzata, le viste e i set dei colori valgono solo per quella istanza di Looc.UP. Se invece Looc.UP viene avviato da una cartella di rete condivisa, le impostazioni di viste e colori sono comuni.
Negli upgrade all'interno di una data versione i file non vengono sovrascritti  quindi non è necessario salvarli.
Se invece si aggiorna Looc.UP da una versione all'altra, bisogna ricordarsi di effettuare una copia dei file prima di effettuare l'aggiornamento. Anche perché è l'unico modo per portare i setup della vecchia versione a quella nuova.

# Viste
Le viste sono salvate nel file uiganttviews.xml.

Il formato delle chiavi per le viste è il seguente : 

<View code="VISTA1" description="Vista di prova" key="FUN-GNT-S5SER_01-RI-CDL----------------">

Dove : 

code :  è il codice associato alla vista
key :  è l'identificativo dello schedulatore a cui è associata la vista. Questo identificativo viene normalmente passato nell'XML dello schedulatore. Nel caso non venisse passato, viene calcolato dinamicamente a partire dalla F() dello schedulatore (è questo il caso dell'esempio riportato).

# Colori
Il set dei colori viene salvato nel file uiganttcolor.xml

Il formato delle chiavi è il seguente : 

<GanttColors>
  <ColorSet Key="K1-K2-K3">
    <Color Key="M.I.1.046" Value="204;255;204"/>
    <Color Key="M.E.2.181" Value="255;000;102"/>
  </ColorSet>
</GanttColors>

ColorSet è un insieme di colori, identificato da una chiave Key composta da : 

K1 :  ambiente AS400
K2 :  codice colonna del gantt che fa da chiave colore
K3 :  tipo+parametro della colonna che fa da chiave colore

Il singolo colore viene salvato con : 

Key :  codice del colore (è uno dei valori possibili per la colonna del gantt che definisce i colori)
Value :  il codice RGB del colore

Da notare però che nelle ultime versioni dello schedulatore si preferisce forzare la lista colori direttamente dall'XML dello schedulatore e bypassare la gestione sopra descritta.

Ad esempio, passare nel Setup del Gantt una cosa del tipo : 

<Setup>
<GNT>
<Colors>
               <Color id="BIANCO" Desc="Mia descrizione molto lunga e annoiante">R255G255B255</Color>
               <Color id="NERO" Desc="Altra dec">R000G000B000</Color>
               <Color id="ROSSO" Desc="">R255G000B000</Color>
               <Color id="VERDE" Desc="">R000G255B000</Color>
               <Color id="RANDOM" Desc=""/>
               <Color id="BLU" Desc="">R000G000B255</Color>
</Colors>
                               </GNT>
                               </Setup>

In modo da forzare la lista dei colori presenti nello schedulatore.

Se viene passato questo Setup, i colori della tabella uiganttcolor.xml non vengono considerati.
