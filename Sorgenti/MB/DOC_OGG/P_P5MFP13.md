# Rilavorazione contenitore disperso
Questa funzione permette di riportare in produzione MFP uno o più contenitori provenienti dall'esterno, generalmente questo tipo di azioni si esegue per attivare la rilavorazione di articoli in precedenza usciti dal flusso produttivo ed esempio per non conformità.
### Formato di lancio
![P5PMFP_15](http://localhost:3000/immagini/MBDOC_OGG-P_P5MFP13/P5PMFP_15.png)### Lista di scelta
Il sistema presenta nel formato lista tutte le giacenze compatibili con la scelta e le impostazioni
![P5PMFP_15A](http://localhost:3000/immagini/MBDOC_OGG-P_P5MFP13/P5PMFP_15A.png)sulle righe giacenza sono possibili diverse opzioni : 
![P5PMFP_15B](http://localhost:3000/immagini/MBDOC_OGG-P_P5MFP13/P5PMFP_15B.png)in particolare, selezionando con S la giacenza da cui attingere, il sistema presenta la riga totale della qtà che sarà riportata nel flusso MFP : 
![P5PMFP_15C](http://localhost:3000/immagini/MBDOC_OGG-P_P5MFP13/P5PMFP_15C.png)se la qtà richiesta è superiore alla giacenza selezionata viene portato solo il totale giacenza disponibile.
Confermando con F6 viene mostrata una nuova lista in cui si può indicare quanti nuovi contenitori MFP creare : 
![P5PMFP_15D](http://localhost:3000/immagini/MBDOC_OGG-P_P5MFP13/P5PMFP_15D.png)la quantità viene divisa per il numero di contenitori, ma comunque si possono forzare quantità diverse purché il totale sia rispettato, è possibile anche scrivere delle note di contenitore che poi possono essere stampate nell'etichetta bar-code. Con F6 si conferma la creazione contenitori ed i movimenti di trasferimento dall'esterno al flusso MFP.
