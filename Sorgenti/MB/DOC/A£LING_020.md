# Impostazione tecnica dell'applicazione

## File origine - A£TROR0F

Il file A£TROR0F contiene le frasi in italiano estratte da Sme.UP (parte standard e parte personalizzata).
Contiene un record per ogni frase in ogni oggetto di Sme.UP. Se l'oggetto è personalizzato contiene solo le frasi aggiunte rispetto all'oggetto standard.
Esempio : 
 * Programma standard con frasi a, b, c.
 * Programma personalizzato con frasi a, b, d.
 * Nell'A£TROR0F avremo le frasi a, b, c nell'ambito standard (00) e la frase d nell'ambito personalizzato (10).

## File destinazione - A£TRDE0F

L'A£TRDE0F contiene le frasi tradotte nelle varie lingue. Una frase presente in A£TROR0F appare n volte nell'archivio A£TRDE0F, una per ogni lingua installata.
Tornando all'esempio precedente, supponendo un'installazione con le lingue EN e FR, avremo : 
 * Frasi a,b,c ambito 00 lingua EN;
 * Frasi a,b,c ambito 00 lingua FR;
 * Frase d ambito 10 lingua EN;
 * Frase d ambito 10 lingua FR.

Considerazioni importanti : 
 * A runtime (esecuzione di uno Sme.UP in lingua) l'unico file letto è l'A£TRDE0F. L'A£TROR0F esaurisce il suo compito nella generazione dell'A£TRDE0F.
 * Ogni frase di Sme.UP ha il suo record in A£TRDE0F, indipendentemente dal suo stato di traduzione (le frasi non tradotte avranno il record con traduzione vuota).
 * Per motivi di semplicità e performance non sono previste risalite :  data una frase per determinarne la traduzione si aggancia direttamente il suo record in A£TRDE0F. Se la traduzione non è presente viene tornata la frase in italiano.

## Struttura dei programmi

La traduzione di Sme.UP in una lingua avviene secondo un determinato iter logico, a cui viene fatta corrispondere la nomenclatura dei programmi coinvolti : 
 * Estrazione dei record delle frasi in italiano nel file A£TROR0F :  programmi che cominciano con A£TR0;
 * Preparazione dei record delle frasi in una determinata lingua nel file A£TRDE0F :  programmi che cominciano con A£TR1;
 * Generazione degli oggetti in lingua leggendo l'A£TRDE0F :  programmi che cominciano con A£TR4.

## Supporto in compilazione
Per ottenere una corretta estrazione e traduzione delle frasi nei programmi Sme.UP, è possibile attivare un supporto in compilazione.
- [Programmi da tradurre e supporto in compilazione](Sorgenti/MB/DOC/A£LING_012)
