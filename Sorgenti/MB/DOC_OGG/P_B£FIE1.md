# IMPOSTAZIONE DEL FILTRO ESTERNO
Il filtro esterno permette di eseguire delle parzializzazioni su attributi (OAV) degli oggetti presenti nell'archivio di competenza.
In questo modo è per esempio possibile filtrare dei documenti basandosi su caratteristiche dell'articolo (classe materiale, tipo parte, ...) anche se queste caratteristiche non sono scritte direttamente nell'archivio dei documenti.
_7_ATTENZIONE :  i filtri esterni sono comuni ai vari programmi e quindi potenzialmente un filtro potrebbe essere utilizzato sia nella stampa articoli sia nella stampa documenti. Non è detto però che tutti i filtri presenti possano essere impiegati indifferentemente da una parte o dall'altra.
# Scelta dell'oggetto da filtrare
Normalmente il tipo oggetto sul quale si vogliono eseguire le parzializzazioni viene specificato nel filtro stesso (tabella B§S sottosettore B£) a meno che nella videata non venga evidenziato il comando 'F08=Cambia ogg.'.
In questo caso premendo F08 si accede ad un'ulteriore videata nella quale è possibile specificare direttamente i 5 tipi e parametri del filtro, che numero di oggetto deve essere considerato e se deve essere utilizzato un programma esterno per effettuare il filtro.
In questo modo è quindi possibile filtrare contemporaneamente su OAV appartenenti a oggetti diversi.
## Numero oggetto
Questo campo ha significato se nell'archivio utilizzato sono presenti più istanze dello stesso oggetto.
Per esempio nelle commesse sono presenti due campi contenenti una commessa :  quello della commessa stessa e quello della commessa madre. Nel caso in cui si volesse parzializzare per degli OAV della commessa madre bisognerà specificare '2' nel campo Numero oggetto.
Per sapere a che numeri oggetto sono associati i vari campi dell'archivio premere ancora il tasto F08
## Usa pgm esterno
Questo campo permette di eseguire una chiamata ad un programma esterno per l'esecuzione del filtro.
I valori ammessi sono : 
'1' :  Programma standard SMEUP
'2' :  Programma utente
Nel primo caso viene chiamato il programma standard B£FIE4, nel secondo caso occorre specificare un
programma utente (un esempio è il programma B£FIE4_U).
Il programma B£FIE4 permette di gestire liste di oggetti o di attributi tramite la /COPY £G40.
E' quindi possibile parzializzare per uno o più range di oggetti oppure per oggetti appartenenti
ad una lista utente.
