La documentazione, in Sme.Up, si presenta in forme eterogenee, (schede, alberi, matrici, modelli dinamici, ecc...). Ciò non significa che la parte testuale non abbia un ruolo preminente.
La caratteristica più importante di Sme.Up è probabilmente il suo rigore nell'implementare un'architettura applicativa ad oggetti.
Nel presente documento vengono quindi descritti gli oggetti che sono (o potrebbero essere) corredati da una documentazione testuale, con i dettagli tecnici del luogo in cui essa risiede, delle convenzioni sul suo nome, ecc...

## Classi e istanze
In una impostazione ad oggetti, anche le classi sono particolari istanze di classi superiori.
Per chiarire il livello a cui esse si dispongono, nell'albero degli oggetti, diamo le seguenti definizioni.
 * _1_Oggetto, è identificato da tre campi :  tipo XX, parametro YYY, codice ZZZ.
 * _1_Classe, è un oggetto di tipo "OG", senza parametro e con codice ZZ (di due caratteri)
 * _1_Sottoclasse, é un oggetto di tipo "OG", con parametro YY (di due caratteri) e codice ZZZ. Una sottoclasse si può identificare anche nel seguente modo :  "OG"  YYZZZ. La si distingue dalla classe perché il suo codice è lungo almeno tre caratteri.
 * _1_Istanza, é un oggetto di tipo XX (diverso da "OG"), con, opzionalmente, il parametro YYY, e con il codice ZZZZ.


## Oggetti documentati
Un oggetto è potenzialmente corredato di un documento se è fornito con Sme.Up, e non inserito dall'utente.

Si documentano i seguenti oggetti : 
 * _1_Tutte le classi. La classe ZZ, nel membro OG_ZZ del file sorgente DOC_OGG.
 * _1_Alcune sottoclassi. Se la sottoclasse non appartiene alle sottoclassi documentate (riportate nel seguito), la sua documentazione è quella della sua classe, vale a dire, data la sottoclasse "OG" YY ZZZ, l'oggetto "OG" .ZZ.
 ** _2_I settori di tabella (OG TA XXX), nel membro TA_XXX del file sorgente DOC_OGG. Questa sottoclasse si riconduce all'oggetto ST  XXX, ed è equivalente all'oggetto RE T- XXX.
 ** _2_I codici fissi V1 (OG V1 XXX), nel membro V1_XXX del file sorgente DOC_OGG. Questa sottoclasse si riconduce all'oggetto V2 TIPV1 XXXX
 ** _2_I codici fissi V2 (OG V2 XXX), nel membro V2_XXX del file sorgente DOC_OGG. Questa sottoclasse si riconduce all'oggetto V2 TIPV2 XXXX
 ** _2_I codici fissi V3 (OG V3 XXX), nel membro V3_XXX del file sorgente DOC_OGG. Questa sottoclasse si riconduce all'oggetto V2 TIPV3 XXXX
 ** _2_I tipi voce (OG VO XXX), nel membro TIPVO del file sorgente DOC_VOC (la documentazione è parte del membro). Questa sottoclasse si riconduce all'oggetto VO TIPVO XXXX
 ** _2_I tipi oggetti grafici J1 (OG J1 XXX), nel membro J1_XXX del file sorgente DOC_OGG. Questa sottoclasse si riconduce all'oggetto V2 JAOLC XXXX
 * _1_Alcune istanze
 ** _2_Gli archivi (OJ *FILE XXXXXXXX), nel membro F_XXXXXXXX del file sorgente DOC_OGG. Questa istanza è equivalente all'oggetto RE F- XXXX. Se presente, ha la precedenza la documentazione della seguente voce :  VO GLO_B£_SRC XXXXX. In questa voce si documentano gli archivi sorgenti (QILEGEN, BRSRC, ecc...).
 ** _2_Le Librerie (OJ *LIB XXXXXXXX), si documentano come voci VO GLO_B£_LIB.
 ** _2_I campi di archivi (CS F-XXXXXXXX YYYYYY), nel membro F_XXXXXXXX del file sorgente DOC_OGG (sezioni all'interno della documentazione generale dell'archivio).
 ** _2_I campi di tabella (CS T-XXX YYYYYY), nel membro TA_XXX del file sorgente DOC_OGG (sezioni all'interno della documentazione generale del settore di tabella).
 ** _2_I programmi (OJ *PGM XXXXXX), nel membro P_XXXXXX del file sorgente DOC_OGG. Questa istanza si riconduce all'oggetto PG XXXX
 ** _2_I setup estesi (RE L- XXXXXXX), nel membro L_XXXXXXXX del file sorgente DOC_OGG
 ** _2_I campi di setup estesi (CS L-XXXXXXXX YYYYYY), nel membro L_XXXXXXXX del file sorgente DOC_OGG (sezioni all'interno della documentazione generale del setup esteso.
 ** _2_Gli elementi di alcune tabelle (TA XXX YYYYY), nel membro YYYYY del file DOC_TAXXX. E' il caso di elementi di tabella necessari a Sme.Up. Un esempio è dato dalle classi di autorizzazione (B£P), che sono documentati nel file DOC_TAB£P.
 ** _2_Le voci (VO XXX YYY), sezioni all'interno del membro XXXX del file sorgente DOC_VOC.
 ** _2_I book (MB DOC_BOK ZZZZZ), nel membro ZZZZ del file sorgente DOC_BOK. Se assente si tenta la costruzione di una documentazione virtuale (eseguita nel programma B£BAT04).
 ** _2_I membri di voci (MB DOC_VOC), la documentazione è contenuta nella voce omonima al suo interno. Ad esempio, il membro XXX viene deviato all'oggetto VO XXX XXX.
 ** _2_Le api (MB QILEGEN £XXXZZZ), viene reperita la documentazione dell'oggetto PG TSTXXX.
 ** _2_I membri generici (MB XXXX ZZZZ), dove XXXX è diverso da DOC_BOK, DOC_VOC e QILEGEN, in se stessi.
 ** _2_I servizi (V3 ASE ZZZZZ), nel membro ZZZZ del file sorgente DOC_SER.
 ** _2_I listener (V3 CLI ZZZZ), dove il codice può essere ZZ,per la prima istanza, e ZZ.NN (con NN da 01 a 99 per le istanze successive). Tutte le istanze della stessa radice ZZ sono documentate nel membro V3_CLI_ZZ del file sorgente DOC_OGG.
 ** _2_I server (V3 CSEI ZZZZ), dove il codice può essere ZZ,per la prima istanza, e ZZ.NN (con NN da 01 a 99 per le istanze successive). Tutte le istanze della stessa radice ZZ sono documentate nel membro V3_CSE_ZZ del file sorgente DOC_OGG.
 ** _2_Le variabili (V3 EVA ZZZZ), sono documentate nel membro V3_EVA del file sorgente DOC_OGG, in cui sono presenti tutte variabili

L'utente può utilizzare questa struttura per documentare i propri oggetti, se sono della stessa natura degli oggetti documentati, riempiendo un membro nella propria libreria di personalizzazioni, con le stesse convenzioni di nome e di file.

Ad esempio, può documentare nuovi programmi, archivi (e relativi campi), settori di tabella (e relativi campi).

Riferirsi agli schemi seguenti : 

### Istanze documentate
![B£DOCU_006](http://localhost:3000/immagini/B£DOCU_09/BXDOCU_006.png)
### Sottoclassi documentate
![B£DOCU_007](http://localhost:3000/immagini/B£DOCU_09/BXDOCU_007.png)
### Classi documentate
![B£DOCU_008](http://localhost:3000/immagini/B£DOCU_09/BXDOCU_008.png)
### Risalita dall'istanza alla classe o alla sottoclasse
![B£DOCU_009](http://localhost:3000/immagini/B£DOCU_09/BXDOCU_009.png)