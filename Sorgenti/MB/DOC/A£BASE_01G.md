## Introduzione
La tecnica dell'OVL consiste nel memorizzare il risultato di una stampa PC sull'AS400 e utilizzare poi quest'ultima in sovrapposizione ad una qualsiasi stampa AS.
Questa tecnica ha il vantaggio di ottenere i risultati direttamente dall'AS senza alcun prerequisito da parte dell'utilizzatore. Per lo stesso motivo, tuttavia, questo aspetto può creare problemi di performance nel caso la linea di trasmissione non sia abbastanza larga, in quanto la sovrapposizione appesantisce l'esecuzione fisica della stampa.

## Creare un OVL
I passi per la creazione di un OVL sono i seguenti : 
 * nel caso non ne esista già uno, è necessario creare un apposito PF sull'AS400 in cui memorizzare le sovrapposizioni da utilizzare e definendo la lunghezza del record in mancanza DDS di 32766, il numero massimo di membri *NOMAX, il parametro LVLCHK (Controllo livello form.record) con valore *NO;
 * se non è installata sul PC (questo vale solo per chi crea l'OVL e non per chi lo utilizza), installare la stampante IBM AFP, che, se non inclusa tra le stampanti disponibili IBM, è recuperabile tramite un'installazione completa del Client Access. Nell'aggiunta della stampante bisognerà impostare alla voce "Utilizza porta seguente" FILE :  (Stampa su file);
 * sul PC aprire l'applicazione da cui ricavare la stampa da sovrapporre;
 * stampare il documento utilizzando la stampante AFP. Sarà necessario impostare in Proprietà anche il parametro "Output Type" con valore "Overlay" e "Print Text as Graphics" ad "On" , in modo da creare su pc un file (con il nome e il percorso da indicare in esecuzione) contenente il risultato della stampa;
 * portare il file PC in AS400 caricandolo all'interno di una cartella della QDLS. Nota bene :  perchè il comando successivo funzioni il nome del file nella qdls deve essere <= 12 caratteri.
 * lanciare il comando CPYFRMPCD  FROMFLR('CartellaQDLS') TOFILE(Libreriaas/Fileas) FROMDOC(nomefileinqdls) TOMBR(nomemembrofileas) TRNTBL(*NONE) TRNFMT(*NOTEXT).
 * indicare come "tipo" sul membro creato "OVL".
 * lanciare il comando CO per il membro creato nel file.

## Utilizzo di un OVL
Per l'utilizzo dell'OVL, a seconda che il PRTF sia definito internamente o esternamente, è necessario lanciare il comando OVRPRTF in compilazione del PRTF o prima della sua apertura nel pgm di utilzzo, compilando i seguenti parametri :  DEVTYPE(*AFPDS) PAGRTT(90) (questo solo se il printer è 198 o 132 caratteri) FRONTOVL(Nome OVL).
