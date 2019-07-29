## Generalità
Con la gestione degli Alias è possibile creare dei  'legami' tra gli oggetti di_3_dueambiti diversi.
Questi legami consentono di tradurre il codice di un certo  oggetto riferito all'ambito 1, nel codice dello stesso oggetto riferito però all'ambito 2.

Esempi classici di utilizzo degli Alias sono : 
 * _2_DEFINIZIONE DI UN SISTEMA EDI (interno / esterno), si rimanda alla documentazione del modulo.
 * _2_CREAZIONE  ARCHIVIO  DI  APPOGGIO  PER  LA CONVERSIONE  DI ANAGRAFICHE TRA SISTEMI DIVERSI

## Impostazione
Per impostare la gestione degli ALIAS è necessario : 

 *_2_Definire il contestodi  gestione degli Alias :  esso definisce l'oggetto o gli oggetti (max 2), per cui devo generare gli Alias.

Il contesto è un elemento della Tabella_4_C£K : 
 :  : DEC T(ST) K(C£K)
Esempio : 
 :  : DEC T(TA) P(C£K) K(ART/CLI)

 * _2_Inserire gli Alias, il legame tra i due ambiti, attraverso la gestione degli stessi, opzione 01 = Aggiunta.

### Caso particolare :  Conversioni
Un caso particolare di gestione degli alias è quelle delle conversioni che vengono eseguite per migrare da un altro sistema a Sme.UP.
In questi casi si utilizzano i contesti CON ed eventualmente altri contesti COx (x è un carattere a piacere).

La particolarità di questi contesti è l'inversione tra campo 2 e alias : 
 * _2_campo 1, rappresenta l'oggetto Sme.UP (tipo e parametro) per cui definire l'alias
 * _2_campo 2, è di libera compilazione (anche se come interstazione mantiene quella dell'oggeto di campo 1), in questo campo si inserisce un valore esterno (es. una causale di magazzino)
 * _2_alias, è un'istanza dell'oggetto Sme.UP corrispondente all'alias inserito in campo 2 (es. un elemento della tabella GMC)

## Test
E' possibile testare il funzionamento di quanto fatto attraverso il test della /copy C£A : 
 :  : INI _4_CALL TSTC£A
 :  : CMD CALL TSTC£A
 :  : FIN
