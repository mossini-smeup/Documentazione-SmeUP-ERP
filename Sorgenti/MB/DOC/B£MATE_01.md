# Holt Winters :  metodo statistico per costruire le previsioni
Il metodo Holt Winters (HW) si applica ad una serie storica per ottenere una previsione dei periodi futuri.
In fase di messa a punto, per verificarne l'efficacia, esso può essere utilizzato in controllo, vale a dire facendogli fare una previsione per periodi passati, di cui si dispongono già i valori effettivi.

Definiamo : 
 * __Frontiera__, l'ultimo periodo della serie che si assume come storia. Le previsioni iniziano dal periodo successivo. La frontiera non coincide con l'ultimo periodo della serie nel caso del controllo e, come vedremo, nell'autofit;
 * __Periodicità__, il numero di periodi in seguito a cui si assume che la serie presenti una ripetitività;
 * __Storia__, il numero di periodi passati su cui si fonda la previsione. Per il metodo HW è necessaria (e sufficiente) una storia pari a due periodicità;
 * __Numero di periodi di previsione__, il numero di periodi futuri (da quello successivo alla frontiera in poi) per cui si calcola la previsione;
 * __Numero di periodi iniziali__, il numero di periodi, a partire dal primo periodo della storia, su cui si esegue un'interpolazione lineare per ottenere i dati di "innesco" del calcolo. Può essere al massimo pari alla periodicità; un valore minore riduce il peso della storia nel calcolo.

Il metodo HW si basa su tre valori, tutti nella stessa unità di misura della serie, che si determinano alla frontiera : 
 * __Livello __ --> valore medio della previsione nei periodi futuri;
 * __Trend __ --> variazione (che si assume costante) della previsione rispetto al periodo precedente. Se positivo indica una crescita, se negativo una diminuzione;
 * __Stagionalità __ --> una serie di "P" valori (dove "P" è la periodicità) che indica, rispetto al livello, la variazione della previsione dovuta a fenomeni ripetitivi).

La **previsione del periodo "N"** (da 1 al numero di periodi di previsione) è data da : 

**Livello + N x Trend + Stagionalità del periodo N**.

La determinazione di livello, trend e stagionalità, richiede che si impostino tre fattori di smorzamento (il cui valore va da 0 a 1) indicanti il peso dei periodi più recenti rispetto a quelli più in là nel tempo. Il valore 0 significa che conta solo il periodo iniziale. Il valore 1 significa che conta solo l'ultimo periodo (frontiera).

Essi sono : 
- **Alfa** per il livello
- **Beta** per il trend
- **Gamma** per la stagionalità

Si presenta quindi il problema di come impostarli in modo da massimizzare l'efficacia della previsione.
Dall'esperienza, un valore di 0,2 per tutti e tre pare dia risultati accettabili.
Un modo più evoluto (che richiede però tempi di elaborazione molto più lunghi) è l'autofit, in cui si fanno calcolare al sistema i valori ottimi dei tre fattori di smorzamento.
L'ottimo si definisce come la terna dei valori che minimizza un coefficiente generale di bontà della previsione (CB), che può essere scelto tra

![B£MATE_01](http://localhost:3000/immagini/B£MATE_01/BXMATE_01.png)
Disponendo di una serie di tre periodicità, la frontiera viene portata alla fine delle prime due (che costituiscono la zona di training). Viene quindi calcolata la previsione per la terza periodicità (zona di test) per tutte le combinazioni di alfa, beta e gamma (con un passo impostato, ad esempio di 0,2), e si determina il CB, confrontando, nella zona di test, la previsione calcolata con i valori storici.
Viene quindi eseguita la previsione, con la frontiera riportata al valore iniziale, con la terna di fattori che ha minimizzato il CB.
Non disponendo di una serie di tre periodicità, ma solo di due (che è la condizione minima per l'applicabilità di HW), si opera nel seguente modo (autofit senza arretramento) :  durante l'elaborazione, per determinare i coefficienti di livello, trend e stagionalità sulla frontiera, viene calcolata, per ogni periodo della storia, la previsione, partendo dai valori di livello, trend e stagionalità dello stesso periodo; si esegue, come nel caso precedente, l'elaborazione per tutte le combinazioni di alfa, beta e gamma e si determina il CB confrontando la serie storica con la previsione "storica"; la parte successiva del metodo coincide con il caso predecente.

A questo proposito facciamo presente che il sistema comunque calcola sempre i valori dei tre CB consuntivi per la parte storica.

**ESEMPI**
Riportiamo alcuni esempi di previsioni, con le seguenti assunzioni : 
 * Il periodo della serie è il mese.
 * La periodicità è di 12 periodi.
 * La storia è di 24 periodi (12 x 2).
 * Il numero di periodi di previsione è 12.

**A) Previsione con una serie di 24 periodi**
E' la condizione minima per eseguire l'HW.
 * Si può impostare solo l'autofit senza arretramento.
 * In alternativa si fissano i valori dei tre fattori di smorzamento.
 * Vengono calcolate le previsioni per i periodi dal 25 al 36.

**B) Previsione con una serie di 36 periodi**
 * La frontiera è al periodo 36, quindi è possibile eseguire l'autofit "normale", in quanto c'è possibilità di separate i periodi di trainining (i primi 24 mesi) e quelli di test (gli ultimi dodici).
 * In alternativa si fissano i valori dei tre fattori di smorzamento, con la frontiera al periodo 36 e una storia di 24 periodi, ottenendo la previsione per i periodi dal 37 al 48.
 * In questa situazione, sarebbe possibile utilizzare tutti i 36 periodi di storia (nel calcolo finale, non nell'autofit), ma i risultati non sembrano differire significativamente da quelli ottenuti impostando per la storia il valore normale di 24 periodi.

**C) Controllo con una serie di 36 periodi**
In questo caso si vuole controllare, dall'esterno, l'attendibilità della previsione.
 * Si deve fissare la frontiera al periodo 24, in modo che il sistema preveda i periodi dal 25 al 36, impostando comunque che la serie storica è composta di 36 periodi.
 * Ci si riconduce quindi al caso A), e quindi è possibile unicamente l'autofit senza arretramento.
 * In più, dato che il sistema riconosce che è stata fornita una serie storica anche nel futuro (periodi dal 25 al 36) calcola i CB previsionali, confrontando questi valori con quelli calcolati per gli stessi periodi.
 * Dato che vengono comunque calcolati i CB consuntivi, il sistema è in grado di calcolare anche i CB totali, che utilizzano le due serie nella loro completezza  (dal periodo 1 al 36, sia per la per la serie storica che per quella previsionale, composta dai periodi dall'1 al 24 per la previsione nel "passato" e da quelli dal 25 al 36 per la previsione nel "futuro").

**D) Controllo con una serie di 48 periodi**
Anche in questo caso si vuole controllare, dall'esterno, l'attendibilità della previsione.
 * Si deve fissare la frontiera al periodo 36, in modo che il sistema preveda i periodi dal 37 al 48, impostando comunque che la serie storica è composta di 48 periodi, mentre la storia è di 24.
 * Ci si riconduce quindi al caso B), pertanto è possibile utilizzare l'autofit "normale".
 * Le ulteriori considerazioni (calcolo dei CB previsionali e totali) sono le stesse del caso C).

![B£MATE_014](http://localhost:3000/immagini/B£MATE_01/BXMATE_014.png)![B£MATE_015](http://localhost:3000/immagini/B£MATE_01/BXMATE_015.png)![B£MATE_016](http://localhost:3000/immagini/B£MATE_01/BXMATE_016.png)
## Holt Winters :  esposizione dettagliata
La previsione di un periodo futuro **n** dipende dai valori di livello, trend e stagionalità, relativi alla frontiera (ultimo periodo della storia), con la seguente formula : 
![B£MATE_017](http://localhost:3000/immagini/B£MATE_01/BXMATE_017.png)dove : 
![B£MATE_018](http://localhost:3000/immagini/B£MATE_01/BXMATE_018.png)E' necessario quindi determinare i valori di livello, trend e stagionalità alla frontiera.
Si utilizzano le seguenti formule, che permettono di calcolare il valore per il generico periodo **i+1** a partire dal valore del periodo**i**.
**Esse vanno applicate ricorsivamente, a partire dai valori del periodo 1 (inizio della storia) fino a quelli del periodo f (frontiera).
![B£MATE_019](http://localhost:3000/immagini/B£MATE_01/BXMATE_019.png)dove : 
![B£MATE_020](http://localhost:3000/immagini/B£MATE_01/BXMATE_020.png)Da queste espressioni si comprende che fattori di smorzamento prossimi a zero tendono a rafforzare i valori dei periodi iniziali, mentre fattori prossimi a uno tendono a rafforzare i valori dei periodi più recenti.

Anche i valori del periodo **1** vengono calcolati nello stesso modo, partendo dai valori del periodo precedente (periodo 0), che invece si determinano in modo specifico, partendo dai dati della serie storica.
### Calcolo valori al periodo 0
Per il livello e il trend si calcola la retta che interpola la serie storica, a partire dal periodo **1**, per una periodicità. Il livello e il trend sono, rispettivamente, l'ordinata all'origine e il coefficiente angolare di questa retta.

Per la stagionalità, che è costituita da un vettore con un numero di elementi pari a una periodicità, si opera determinando la retta che interpola la serie storica per tutti i periodi e se ne ricava, per ogni periodo, il residuo (differenza tra il valore della serie e quello della retta interpolatrice).

La stagionalità del periodo **n** è data dalla media aritmetica dei residui del periodo **n** , **n+p**, **n+2p**, (dove **p** è la periodicità), fino a che questo indice supera la storia.

Ad esempio, con una storia di 31 periodi e una periodicità di 12, si determina il seguente vettore di stagionalità : 
![B£MATE_021](http://localhost:3000/immagini/B£MATE_01/BXMATE_021.png)dove : 
![B£MATE_022](http://localhost:3000/immagini/B£MATE_01/BXMATE_022.png)Ricordiamo che deve esistere una storia almeno pari a una periodicità :  questa condizione garantisce che si possa calcolare l'intero vettore della stagionalità

# Holt Winters moltiplicativo
Il metodo descritto in precedenza è di tipo additivo :  le tre componenti si sommano per ottenere la previsione e hanno quindi tutte la stessa unità di misura della previsione.
Esiste anche un metodo moltiplicativo in cui, per ottenere la previsione, si sommano il livello e il trend (in modo analogo al metodo additivo) e si moltiplica il risultato per la stagionalità, che in questo caso è un valore adimensionale.

Il metodo moltiplicativo risponde in maniera più nervosa alla stagionalità.


