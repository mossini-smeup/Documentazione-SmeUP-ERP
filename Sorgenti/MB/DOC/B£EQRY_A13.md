# Prerequisiti

Per utilizzare le ricerche grafiche, in emulazione deve essere innanzitutto prevista l'attivazione delle stesse in ambito emulazione, attraverso la valorizzazione della variabile di SCP_CLO "*EMUSEARCHTYPE" ad "EXT".

In questo modo è previsto che se il client riesce ad individuare dal file video l'oggetto di un campo, il client prevederà di risolvere la ricerca su tale campo attraverso la ricerca grafica.
In questa affermazione sono contenuti due aspetti fondamentali delle ricerche grafiche : 
* La ricerca parte solo se per il client, se l'oggetto è identificabile (si vedrà a seguire come)
* La ricerca viene intercettata dal client e solo a seguito della risoluzione di tutte le ricerche il pgm di emulazione verrà richiamato. Questo implica che il pgm di emulazione non riceve mai i campi valorizzati con i caratteri di ricerca, in quando risolti a priori dal client.

La tipizzazione del campo deve essere quindi assolutamente precisa e corretta.

# Come far riconoscere al client l'oggetto di un campo video

L'oggetto di un campo può essere indicato in due modalità : 
* Indicando il tipo oggetto nella descrizione del campo video a partire dalla trentesima posizione
* Attraverso l'indicazione di particolari istruzioni di commento da indicare nel file video con la seguente struttura : 
**  :  : F.FLD :  costante iniziale
** K(£Unomeformatovideo.nomecampovideo) :  nel parametro K viene indicato, preceduto da una costante fissa "£U" il nome del formato video, seguito da un "." e dal nome del campo video.
** Ogg="TipoOggetto" :  nell'attributo Ogg viene indicato il tipo oggetto del campo

Per entrambe le modalità se il tipo oggetto è dinamico, è possibile indicare fra parentesi quadre il nome di un'altro campo video (che può essere anche hidden).

Mentre la prima impostazione comporta la ricompilazione sia del file video che del pgm che lo utilizza, per la seconda è sufficiente ricompilare il solo pgm che utilizza il file video.
NOTA BENE :  in concomitanza di entrambe le indicazioni è la seconda che vince sulla prima, in questo caso è possibile inibire un'errata tipizzazione, indicando come tipo oggetto "**".

Sempre per la seconda modalità, esiste un tool che permette di gestire la scrittura dei commenti in modo strutturato ed interattivo. Tale tool è accessibile da linea comandi, attraverso il comando "E" seguito dal nome del pgm che utilizza il file video.

Lanciando questo comando sia aprirà una schermata dove sulla estrema sinistra viene riportata l'indicazione del file video. Da li è possibile accedere attraverso l'opzione "AL" al tool di gestione dei campi video. Qui sarà possibile indicare in modo immediato il tipo oggetto corretto, di ogni campo su tutti i formati video del file.

Con F06 si confermano le scelte e con F08 è possibile inoltre lanciare la ricompilazione del pgm richiamante.

