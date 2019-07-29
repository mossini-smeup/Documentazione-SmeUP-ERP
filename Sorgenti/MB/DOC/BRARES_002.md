# Introduzione
In realtà multiplant, specialmente se attivato l'MRP multiplant (sia in modalità singola sia in modalità completa) in tabella M51
- [Modalità pianifi.multimagazzino](Sorgenti/MB/DOC_OGG/V2_M5TPM)
risulta utlie definire il legame tra ente e articolo, e la priorità di un ente, di norma impostata nell'archivio
 :  : DEC T(OJ) P(*FILE) K(BRARES0F)
a livello di singolo plant, in quanto, specie nel caso di plant molto distanti tra di loro, l'assegnazione dell'ente preferenziale di articoli comuni può diversificarsi (il fornitore di viti in Lombardia è verosimile che non sia lo stesso di quello in Polonia).
Inoltre può essere utile diversificare l'assegnazione in base al tipo di ordine (fornitura piena o conto lavoro).

A questi scopi è presente un archivio di estensione del precedente
 :  : DEC T(OJ) P(*FILE) K(BRAREP0F)
che permette di aggiungere l'informazione (a livello di singolo plant, e/o di tipo fornitura)
 :  : DEC T(VO) P(F.BRAREP0F) K(EPPOLF)
e  di sovrascrivere le seguenti informazioni (sempre a livello di singolo plant, e/o di tipo fornitura)
 :  : DEC T(VO) P(F.BRAREP0F) K(EPAPRI)
 :  : DEC T(VO) P(F.BRAREP0F) K(EPQUOC)
ed inoltre permette dl'esclusione dell'ente (sempre a livello di plant e/o di tipo fornitura)
 :  : DEC T(VO) P(F.BRAREP0F) K(EPFL01)

L'attivazione di questo archivio (ed il livello di sovrapposizione rispetto a quello generale) è guidata dal flag sviluppo verticale BRARES della tabella C£E, nell'elemento ART_xxx, dove xxx è il tipo ente a cui si riferisce.
 :  : DEC T(VO) P(T.C£F) K(T$C£F1)

## Gestione
Se inserito, in C£F, un valore di sviluppo verticale, nel formato di dettaglio dell'archivio ente/articolo viene presentato il campo di input "Sviluppo verticale" che permette il passaggio alla gestione dell'archivio estensioni.
Viene presentata la lista delle estensioni presenti, che si possono modificare, o aggiungerne di nuove.
Nel successivo formato di dettaglio si inseriscono i campi : 
* Plant, se attivo sviluppo per plant o totale (campo obbligatorio)
* Politica per fornitura, se attivo sviluppo per politica fornitura o totale (campo obbligatorio)
* Priorità (campo facoltativo)
* Quota di copertura fabbisogni (campo facoltativo)
* Ente da escludere (campo facoltativo)

## Modo di risalita
La risalita, se è attivato in tabella lo sviluppo, è eseguita nella routine
 :  : DEC T(MB) P(QILEGEN) K(£G26) D(Funzioni Generali - interfaccia ente/articolo) L(1)
nella sola funzione "ENP" (ente preferenziale, in tutti i suoi metodi) a cui si passa l'informazione del plant nel campo £FUNK3 (se assente si assume il plant di competenza dell'articolo) e l'informazione se fornitura o lavorazione in £FUNK4 (se assente si assume l'informazione dalla politica master).

Il reperimento delle informazioni avviene nel seguente modo : 
* Si leggono tutti i BRARES dell'oggetto di livello n.
* Se non ne è stato trovato nessuno si risale a livello n+1 (determinando preventivamente il nuovo oggetto di risalita).
* Se invece è stato trovato almeno un record di BRARES, ed è attiva l'estensione al BRAREP, si legge, per ogni BRARES, il relativo BRAREP (impostando il plant e/o il tipo fornitura ricevuti) dello stesso livello. Se si trova il record, se è impostato il flag di esclusione, viene invalidato il BRARES di partenza, altrimenti gli si sovrappone priorità e % di copertura fabbisogni.
* Si determina infine la preferenza/ordinamento tra tutti i BRARES del livello n (eventualmente corretti con le informazioni dei BRAREP) e si esce, sia che siano stati trovati record validi, sia che siano state trovate soltanto esclusioni.

Si opera quindi sempre sull'insieme dei record al livello più basso in cui si trovano informazioni. L'esclusione non fa risalire di un livello, in quanto si potrebbe trovare lo stesso ente. Ammettere la risalita solo quando l'ente è diverso, vorrebbe dire non avere un chiaro controllo delle informazioni che contribuiscono a produrre il risultato.
L'esclusione va quindi bilanciata con un'inclusione con la stessa chiave (e naturalmente un ente diverso). Riferirsi all'esempio sottostante (caso del plant 003) per un'esposizione dettagliata.

Nella determinazione dell'ente preferenziale, a pari priorità, viene data la precedenza ad un ente se assegnato al plant ricevuto.

Esempio : 

Con questa impostazione di archivi (assumiamo di aver attivato lo sviluppo verticale unicamente per plant)

| N.Record|Ente|Plant|Esclusione|Priorità|Archivio |
| ---|----|----|----|----|----|
| 1|000001|||99|BRARES |
| 2|000001|003|Sì||BRAREP |
| 3|000002||||BRARES |
| 4|000002|002||99|BRAREP |
| 5|000002|003|||BRAREP |
| 


L'ente preferenziale calcolato per i vari plant è il seguente (routine £G26 funzione e metodo ENP / PR1)

| Plant|Ente|Motivo |
| ---|----|----|
| 001|000001|Record 1 :  è un plant non specificato in dettaglio, ed è scelto rispetto al record 3 in quanto ha priorità maggiore |
| 002|000002|Record 4 :  ha la precedenza sul record 1 (con la stessa priorità) in quanto specificato a livello di plant |
| 003|000002|Record 5 :  il record 1 (generale con priorità maggiore del 5) è stato invalidato dal record 2 (esclusione per questo plant) |
| 


Attenzione :  nel caso del plant 003, l'invalidazione del'ente 000001 non sarebbe superfula, anche nel caso di attribuzione, all'ente 000002 della priorità 99 (nel record 5). In entrambi i casi sarebbe ritornato, come ente preferenziale, l'ente 000002, ma, nel ritorno sequenziale di tutti gli enti ammessi, nel primo caso sarebbe ritornato solo l'ente 000002, mentre nel secondo anche l'ente 000001, meno prioritario ma comunque valido.










