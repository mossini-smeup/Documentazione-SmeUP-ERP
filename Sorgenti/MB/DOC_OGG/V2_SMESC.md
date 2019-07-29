# _$_PIPE_$_ - Carattere pipe
Attraverso questo escape è possibile inviare nei campi della matrice il carattere "pipe".
Il carattere "pipe" è anche il separatore di colonna, per questo motivo, se la colonna contiene il carattere "pipe" privo del suo formato di escape "_$_PIPE_$_", la colonna verrà scomposta in più colonne.
La trasformazione da carattere "pipe" al carattere escape "_$_PIPE_$_" è eseguita dalla procedura P_RxSOS passando come secondo parametro il carattere "P".
# _$_STXT_$_ - Inizio del testo
Attraverso questo escape è possibile comunicare che tutto quello che segue è da intenersi testo.
L'attributo deve iniziare e finale con le sequenze escape di aperura e chiusura.
La procedura P_RxATT escluderà la parte di testo dalle considerazioni di tag.
# _$_ETXT_$_ - Fine del testo
Attraverso questo escape è possibile comunicare che tutto quello che precede è da intenersi testo.
L'attributo deve iniziare e finale con le sequenze escape di aperura e chiusura.
La procedura P_RxATT escluderà la parte di testo dalle considerazioni di tag.
