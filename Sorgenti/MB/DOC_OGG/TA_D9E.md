# D9E - Parametri databeacon
 :  : DEC T(ST) K(D9E)
## OBIETTIVO
Gestione parametri generali per Databeacon. Ogni elemento va associato al lancio della funzione di creazione
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM Elemento
 :  : FLD T$DESC Descrizione
 :  : FLD T$D9EA **Applicaz. client EIS**
Permette di associare la versione di Databeacon da utilizzare
 :  : FLD T$D9EB **Log estrazione dati**
Se attivato produce una stampa dei record estratti. Da utilizzare solo in fase di test, poichè rallenta l'estrazione.
 :  : FLD T$D9EC **Tipo comunicazione Host**
Selezionare tra i tipi di comunicazione possibili, tra As400 e rete PC. Se Blanks utilizza il Pc Organizer di Cliente Access, se 1 utilizza lo Smeup Network service.
 :  : FLD T$D9ED **Directory scripts**
Indicare se si utilizza la pubblicazione su web server quale directory contiene i file .exe o .cgi, utilizzati dal Databeacon.
Questa corrisponde alla directory indicata in fase di installazione del Databeacon su Web server. Generalmente nel
mondo Windows il default è '/scripts/' per server linux è invece '/cgi-bin/'.
 :  : FLD T$D9EE **Pubblicazione su Web server**
Da attivare quando si pubblicano i cubi su un web server. Se compilato, vanno riempiti anche il campo superiore e quello inferiore.
 :  : FLD T$D9EF **Percorso Web server**
Si inserisce, se pubblicato su web server, quale è il percorso http della directory dei cubi da pubblicare. Va inserito un elemento della tabella B§P che da la possibilità di indicare un percorso completo nel campo PERCORSO, oppure concatenando più elementi di tabella includendo fra 2 caratteri & un altro elemento della stessa tabella B§P.
_9_Esempio : 
"http://webserver/reld/user/cubi"
 :  : FLD T$D9EG **Codebase (Path user)**
Punta ad una tabella B§P dei percorsi ed associa la directory dove sono contenute le librerie che interessano al cubo.
Sono collocate nella directory user. Se si producono cubi in directory diverse da quelle sotto user\nome, bisogna associargli il persorso assoluto fino alla cartella user. Se non specificato, recupera il percorso relativo ".." che significa "vai indietro di una directory".
