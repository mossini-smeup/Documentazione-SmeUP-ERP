# INIZIARE CON LE MATRICI.

## LE /COPY

### Introduzione
Le /COPY necessarie per poter utilizzare il componente matrice sono : 
Nelle specifiche di tipo D
£JAX_PD1
£JAXD1
£JAXD
£TABJATDS

Nelle specifiche di tipo C
£JAX_C1
£JAX_C
£JAX_O
£JAX_PC1

Tutti questo copy sono incluse nell'elenco delle /COPY standard di un servizio o di un programma prototipo.

### Breve descrizione dei vari componenti

Le varie "componenti" necessarie per la generazione di una matrice sono (in ordine di utilizzo) : 

£JAXSWK -> schiera utilizzata per definire la caratterizzazione delle colonne della griglia (es. : SWK001), ogni riga di tale schiera è associata alla DS £JAXDSCOL, definita in questo modo : 

           £JAXDSCOL       DS
             £JAXCCD            lungh.    10      Nome/Codice
             £JAXCTX            lungh.    29      Descrizione/Intestazione
             £JAXCOG            lungh.    21      Tipo/Parametro ogg.
             £JAXCIO            lungh.    01      I/O/H (Input/Output/Hidden)
             £JAXCLU            lungh.    04      Lunghezza del campo
             £JAXCAL            lungh.    01      Als(da decodificare)
             £JAXCDY            lungh.    01      Forma grafica (Emette l'icona, ecc.)
             £JAXCFI            lungh.    10      Per grafico (Asse/Serie)

 La tipizzazione delle colonne della griglia (£JAXCOG) può essere dinamica.
 La sintassi da utilizzare è analoga a quella  utilizzata nella £11A, vedi il sorgente della /Copy G11

 £JAX_AGRI -> utilizzata per inserire la riga di intestazione della  matrice e per la creazione delle colonne

 £JAX_ARIG_I -> utilizzata per inizializzare la scrittura delle righe

 £JAX_ARIG -> utilizzata per scrivere le righe (solitamente inserita in un  ciclo di scrittura), la riga della matrice

 £JAX_ARIG_F -> utilizzata per la finalizzazione della scrittura delle righe

 E' possibile anche inserire le colonne attraverso un metodo alternativo : 
 Si inizializza l'inserimento delle colonne attraverso la JAX_AGRI_I,  poi (solitamente in un ciclo) si aggiunge una colonna
 alla volta con la £JAXDSCOL a cui si associa una particolare riga della schiera SWK001. Una volta
 schiera SWK001. Una volta definita la colonna si inserisce  eseguendo la JAX_ACOL. Per finalizzare l'inserimento eseguire la £JAX_ARIG_F.

 E' possibile inoltre opzionalmente creare delle tabelle aggiuntive  rispetto alla matrice che permettono di ottimizzare il caricamento di  attributi relativi ai campi contenuti nella matrice.
 Per ottenere ciò è necessario : 
 - Inserire, oltre alle /copy standard anche le /copy £JAX_D2 e £JAX_C2
 - Mettere una 'C' nella posizione '66' (campo £JAXCAL dell DS £JAXDSCOL)    delle definizione delle  colonne alle quali si vogliono    associare degli attributi
 - Eseguire in inizializzazione la £JAX_ATAB_I
 - Eseguire, tutte le volte che si legge un record e per ogni colonna    per cui sono previste delle relazioni, la £JAX_ATAB alla quale si    devono passare nei campi £JAXT1, £JAXP1, £JAXK1 il tipo/parametro/oggetto,    nel campo £JAXD1 il numero della colonna ed in £JAXEN la descrizione    della colonna
 - Eseguire, dopo la finalizzazione delle righe, la £JAX_ATAB_F (prima    dell'esecuzione è possibile valorizzare la schiera £JAXT_AT nella quale    viene passato l'elenco degli attributi di ogni colonna che si vuole calcolare,    di default viene sempre eseguita la decodifica).

## PROGRAMMI ESEMPIO E PROTOTIPO

Per vedere un esempio di richiamo/utilizzo delle /COPY esiste in SMEDEV/JASRC un sorgente esempio contenente un esempio di costruzione di matrice, il sorgente in oggetto è il LOSER_00 (Esempio di un servizio). Questo programma di esempio, contiene oltre ad un esempio di matrice anche altri esempi di alcuni componenti.
E' presente inoltre il sorgente prototipo LOSER_ES, con le /Copy necessarie.

