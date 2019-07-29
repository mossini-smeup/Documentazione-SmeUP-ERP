# Programma impostazione generale

## V5STA05_C
E' possibile gestire la configurazione di alcune impostazioni generali sulla statistica, attraverso il programma V5STA05_C, intervenendo sulla schiera situata in fondo al sorgente.

In particolare, è possibile configurare i seguenti parametri : 
 * **GES_CONTAB**
 ** Di default la creazione della statistica del fatturato contabilizzato effettua la quadratura tra i documenti V5 e le relative scritture contabili. Impostando a '1' il parametro, il pgm di creazione della statistica non esegue il controllo con la registrazione e quindi non scrive quadrature e/o rettifiche.
 * **GES_COMPET**
 ** Di default sul fatturato contabilizzato, viene eseguita la ripartizione dei valori in base alle date di competenza, attraverso l'analisi delle scritture contabili. Impostando a '1' il parametro, il pgm di creazione della statistica non esegue la ripartizione sulle date di competenza.
 * **TIP_COSTO**
 ** Di default il tipo costo considerato in statistica viene derivato dalla tabella D01 ('Parametri Costi Avanzati'). Impostando in questo parametro un tipo costo (Elemento della tabella TCO), viene forzato come assunto.
