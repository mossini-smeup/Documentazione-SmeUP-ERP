## Previsioni :  Correzione serie
Nel processo di previsione spesso è necessario apportare correzioni alle serie coinvolte nel processo.
Ad esempio, in caso di sostituzione di un articolo, se essa è avvenuta nel passato, ma comunque all'interno del periodo su cui si basano le previsioni, si deve conglobare la storia dell'articolo sostituito in qella del sostituente, mentre, se avverrà nel futuro, si dovrà, a partire dal periodo di cambio, sostiture la previsione dell'articolo sostituito, con quella del sostituente.
Inoltre, una serie di input che rappresenta il consuntivo delle vendite, potrebbe essere sottoposta ad un "lisciamento", che taglia i picchi anomali, oppure all'eliminazione degli effetti di una promozione, prima di essere utilizzata nella generazione della previsione.

Questo passo esegue la seguente funzione : 
 * data una vista di input e una serie di azioni, determina una vista di correzioni, ed una vista di output che è la somma algebrica delle due precedenti.
 * la vista di correzione ha unicamente uno scopo documentativo, isolando le correzioni, che vengono "annegate" nella vista di output.
 * la serie di azioni è contenuta in uno script (Par. di scelta) risiedente in SCP_SET :  per default viene assunto il membro MPAP53.
 * ogni azione esegue una correzione specifica (lisciamento, sostituzione, ecc...)
 * le tre viste (input, correzione e output) sono tutte obbligatorie (e necessariamente diverse tra loro) e intestate alla stessa copia di oggetti.
Questo passo non è un generico strumento di correzione di una vista (per far questo vi sono altre funzioni), ma trova il suo utilizzo all'interno di un flusso di previsioni.
E' quindi necessario fornire alcune caratteristiche della vista di input, utilizzate dai passi di correzione : 
 * Si deve inserire (obbligatoriamente) la _2_frontiera (ultimo periodo della storia). Questa informazione (statica) insieme al piano (rolling) permette di stabilire dinamicamente se la sostituzione di un codice è avvenuta nel passato oppure avverrà nel futuro.
 * Si deve inoltre specificare se la serie di input è una _2_serie storica od una _2_serie di previsioni. In questo modo è possibile condizionare un'azione (ad esempio di lisciamento) :  farla eseguire solo se la serie è storica, senza dover duplicare gli script.
 * Bisogna inoltre impostare anche il _2_numero di periodi di storia (per default assume la frontiera) e il _2_numero di periodi di previsione.
In questo modo si fissano gli estremi dei periodi su cui si eseguono le correzioni : 
* Per la serie storica dall'inizio della storia alla frontiera
* Per la serie di previsioni dal periodo successivo alla frontiera fino al numero di periodi di previsioni.

## Sostituzione articolo
Si inserisce nello script (default MPAP53 di SCP_SET) il passo ..M53_01

Il legame tra sostituto e sostituente si inserisce nel tipo distinta fisso £CS, in cui gli oggetti sono entrambi articoli.
E' possibile utilizzare un tipo distinta diverso specificandolo all'interno dello script in posizione 10-11-12 (Es. :  ..M53.01 XXX utilizzo del tipo distinta XXX).

L'assieme è il codice sostituito; il componente è il codice sostituente; la quantità di legame è la percentuale di sostituzione; la data di inizio validità (opzionale) è il punto in cui avviene la sostituzione, in caso di sostituzione a rampa; dalla data si risale al periodo MPS a cui essa appartiene, una data a zero ha il significato di sostituzione "da sempre" nel passato.

E' gestita la sostituzione uno a uno :  viene considerato solo il primo componente. Ovviamente nel caso di sostituzione a rampa esso va ripetuto, ma viene comunque considerato solo il primo codice.

Sono implementati i seguenti assunti e forzature : 
 * Non è importante che i legami siano in data crescente :  il sistema li riordina.
 * I coefficienti di impiego maggiori di 1, e quello dell'ultimo periodo di rampa, vengono portati a 1.
 * Non viene controllato che essi siano crescenti per data.
 * Se vi è più di un legame nello stesso periodo, viene trattato quello con la data più alta.
 * Se vi sono sia legami senza data sia legami con data, i primi vengono eliminati.

### Esempi grafici di sostituzione
![MPAP53_01](http://localhost:3000/immagini/MBDOC_OGG-P_MPAP53/MPAP53_01.png)![MPAP53_02](http://localhost:3000/immagini/MBDOC_OGG-P_MPAP53/MPAP53_02.png)![MPAP53_03](http://localhost:3000/immagini/MBDOC_OGG-P_MPAP53/MPAP53_03.png)![MPAP53_04](http://localhost:3000/immagini/MBDOC_OGG-P_MPAP53/MPAP53_04.png)![MPAP53_05](http://localhost:3000/immagini/MBDOC_OGG-P_MPAP53/MPAP53_05.png)![MPAP53_06](http://localhost:3000/immagini/MBDOC_OGG-P_MPAP53/MPAP53_06.png)![MPAP53_07](http://localhost:3000/immagini/MBDOC_OGG-P_MPAP53/MPAP53_07.png)![MPAP53_08](http://localhost:3000/immagini/MBDOC_OGG-P_MPAP53/MPAP53_08.png)![MPAP53_09](http://localhost:3000/immagini/MBDOC_OGG-P_MPAP53/MPAP53_09.png)![MPAP53_10](http://localhost:3000/immagini/MBDOC_OGG-P_MPAP53/MPAP53_10.png)![MPAP53_11](http://localhost:3000/immagini/MBDOC_OGG-P_MPAP53/MPAP53_11.png)![MPAP53_12](http://localhost:3000/immagini/MBDOC_OGG-P_MPAP53/MPAP53_12.png)

## Sostituzione articolo 1 -> N
Si inserisce nello script (default MPAP53 di SCP_SET) il passo ..M53_03

Il legame tra sostituto e sostituenti si inserisce nel tipo distinta di default £CN in cui gli oggetti sono entrambi articoli. E' possibile utilizzare un tipo distinta diverso specificandolo all'interno dello script in posizione 10-11-12 (Es. :  ..M53.03 SOS utilizzo del tipo distinta SOS).

L'assieme è il codice sostituito; il componente è il codice sostituente; la data di inizio validità è il punto in cui avviene la sostituzione (data a zero ha il significato di sostituzione "da sempre" nel passato).
Nell'inserimento della distinta deve essere tenuto in considerazione l'accorgimento che le date di validità dei sostituenti allo stesso livello devono essere uguali.

Il processo di sostituzione si comporta in modo diverso a seconda che la sostituzione sia nel passato o nel futuro.

### Sostituzione nel passato
I sostituenti sono individuati leggendo la distinta di sostituzione riepilogata ai materiali base con data di validità uguale alla data fine della frontiera (ultimo periodo della storia).

### Sostituzione nel futuro
I sostituenti sono individuati leggendo la distinta di sostituzione con il programma di interfaccia B£IDIBM creato allo scopo di scandire ed elaborare le distinte di sostituzione.  La data di inizio validità è la data inizio del primo periodo successivo alla frontiera.
E' possibile utilzzare il programma TSTDIBM, che presenta questa scansione a video.

### Esempio grafici di sostituzione
 _2_Distinta di sostituzione dell'assieme A01.

![MPAP53_13](http://localhost:3000/immagini/MBDOC_OGG-P_MPAP53/MPAP53_13.png)
 _2_Sostituzione nel passato considerando come data fine della frontiera (ultimo periodo della storia) il 29/02/2008.

![MPAP53_14](http://localhost:3000/immagini/MBDOC_OGG-P_MPAP53/MPAP53_14.png)
_2_Sostituzione nel futuro considerando come data di inizio (inizio del primo periodo successivo alla frontiera) il 01/03/2012.

![MPAP53_15](http://localhost:3000/immagini/MBDOC_OGG-P_MPAP53/MPAP53_15.png)
