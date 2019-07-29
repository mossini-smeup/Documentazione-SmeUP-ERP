
 # Obiettivo
 Leggere dati da un Json e presentarli in formato albero o matrice, pertanto input/output panel  o matrice di solo output/aggiornamento.

 # Prerequisiti
 Necessita di avere in linea la libreria specifica per il parsing Json, copyright di Scott C.  Klement. Per ulteriori dettagli vedere qui : 
- [Parsing Json](Sorgenti/MB/DOC/WSBASE_01)

 ## Scheda LOSER_37
 Dalla scheda LOSER_37 (in ambiente web) è possibile caricare i dati da un file Json in locale,  da IFS, da K11 tramite un webservice, in quest'ultimo caso anche con payload in formato stringa  piuttosto che da file in IFS.

 Una volta caricato il Json in memoria ne viene visualizzata la struttura ed i dati in un albero.

 Cliccando su un nodo dell'albero viene visualizzata la singola informazione in formato output  panel. E' possibile cliccare sul tab matrice per vedere l'output con eventuale esplosione  delle righe, comodo soprattutto quando si è cliccato su un array.
 Viene proposta la discesa ad un livello, pertanto vengono visualizzati tutti gli elementi  contenuti nell'array, ma è possibile scendere ulteriormente fino al quarto livello.
 In caso di array che contiene un array, tipicamente se il json è di provenienza da un excel,
 è possibile esploderne le colonne indicandone il numero nel campo apposito.

 ## Servizio LOSER_37

 Il servizio è composto da 2 sole funzioni.metodi, NAV.TRE per la navigazione in albero e  NAV.MAT per la navigazione in matrice.
 E' possibile copiare comodamente le fun dalla scheda di cui sopra una volta che viene visualizzato l'output richiesto, per esempio posso copiare la fun di una matrice, metterla in una scheda,  pertanto avere a disposizione le relative variabili per eventuali dinamismi o impostare un  input panel, esempi di questo tipo sono disponibili nella UPP BR_069 Integrazione S-Peek.

 ### Parametri del servizio
 Ai fini dell'utilizzo di una fun generata dalla scheda è bene conoscere questi parametri : 
 - Buffer   Indica di non caricare un Json ma di utilizzare quello che c'è in memoria, pertanto
            quando viene copiata una fun dalla scheda che visualizza una matrice è necessario
            pulire questo parametro, perchè indica al servizio di utilizzare il Json precedentemente
            caricato dall'albero.
 - Path     Indica il percorso del Json da caricare
 - Provider Indica il provider specifico per il reperimento del Json tramite H80
 - PathIFS  Indica il percorso IFS del Json da caricare
 - K11      Indica la subsezione K11 da utilizzare per il reperimento del Json
 - Nodo     Indica il nodo da reperire
 - Pos1 2.. Indica il posizionamento gerarchico del nodo 1, nodo 2 ..
 - ScpInt   Indica lo script di integrazione (SCP_INT) che permette la ridefinizione dei campi e la
            loro oggettizzazione. Per ulteriori informazioni a tal proposito visualizzare il wizard
            o la API £K37.
