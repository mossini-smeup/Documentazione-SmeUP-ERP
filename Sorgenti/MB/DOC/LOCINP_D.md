# Modifica Caratteristiche Campi

Durante la gestione dell'input panel è possibile reinviare al client alcune caratteristiche grafiche che permettono di modificare la struttura di visualizzazione dell'input panel.

Questo si ottiene inviando nell'xml di ritorno da una chiamata *UPDATE oltre che il normale xml di risposta alle domande anche l'xml della griglia, di setup e se è stato utilizzato un formato video, il buffer degli indicatori del file video.

In merito a questo va inoltre considerato che è opportuno che tale struttura venga inviata non ad ogni chiamata, ma solo al cambiare di una sua caratteristica.

# Limiti e Possibilità

Non è possibile modificare tutte le caratteristiche dei campi, ma solo alcune.

La griglia può essere aggiornata, qual'ora non sia utilizzata in connubio con formato video, per queste caratteristiche : 


- Intestazione campi
- Caratteristica grafica (B/O/H)


La definizione del setup, può essere aggiornata per queste caratteristiche : 


- Obbligatorietà
- Caratteristica grafica (B/O/H) - Solo se non è stato utilizzato un formato video.


Il buffer del formato video può essere aggiornato negli indicatori. E' tramite questa caratteristica che può essere pilotata la caratteristica grafica dei campi in presenza del formato video. E' quindi implicito che quando si vuole intervenire dinamicamente su tale caratteristica i campi che vogliono essere modificati, vadano tutti forzati come campi di input/output nella griglia.

 :  : R02 Esempio
 :  : R02     C                   MOVEL(P)  *OFF          *IN
 :  : R02     C                   EVAL      *IN(41)=XINO1
 :  : R02     C                   EVAL      *IN(42)=XINO2
 :  : R02     C                   EVAL      *IN(43)=XINO3
 :  : R02     C                   MOVEA(P)  *IN           A99
 :  : R02     C                   EVAL      £JAXCP='<Buffer><REC '
 :  : R02     C                             +'in="'+A99+'"'
 :  : R02     C                             +' /></Buffer>'
 :  : R02     C                   EXSR      £JAX_ADD

# Tipizzazioni Dinamiche

Altra considerazione, avendo la possibilità di modificare le intestazioni dei campi, va fatta in relazione ai tipi oggetto :  non è possibile forzare tipi oggetto differenti nella griglia, qual'ora si voglia sfruttare tale possibilità è necessario che i campi che cambiano intestazione abbiano come una tipizzazione dinamica e che quindi i campi con i relativi tipi oggetto siano definiti in griglia.

Per ottenere lo stesso risultato utilizzando un formato video è necessario in più : 
- definire come campi di output della griglia le intestazioni
- mettere nel file video sui campi codice la tipizzazione dinamica indicata nella descrizione come per i file video di emulazione (si veda come esempio il file video del comando UP PAR)
- mettere nel file video come campi nascosti i campi relativi ai tipi oggetto  (si veda come esempio sempre il file video del comando UP PAR)
