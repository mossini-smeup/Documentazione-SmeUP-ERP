# A5C - Linea di ammortamento
 :  : DEC T(ST) K(A5C)
## OBIETTIVO
Definisce i parametri che caratterizzano ogni linea di ammortamento, vale a dire le diverse modalità di calcolo dell'ammortamento per lo stesso cespite.
## SOTTOSETTORE
Va specificato :  è l'azienda per cui è attiva questa linea di ammortamento. In tal modo si può attivare una linea solo per alcune aziende.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM **Codice**
Indica il codice della linea di ammortamento.
 :  : FLD T$A5CA **Modo trattamento primo anno**
Queste informazioni sono sigificative se è stato lasciato in bianco il campo 'valori alla data'.
 :  : FLD T$A5CB **Parametro trattamento primo anno**
Se il modo di trattamento vale '1' il parametro contiene la percentuale di riduzione dell'ammortamento del primo periodo.
 :  : FLD T$A5CC **Numero max anni ammortamento anticipato cespiti nuovi**
Definisce il numero di anni per i quali è ammesso eseguire l'ammortamento anticipato, per i cespiti nuovi.
_7_NB :  questo valore ha un significato di soglia :  è indipendente dal fatto che, negli anni per i quali era possibile eseguire l'ammortamento anticipato, lo si sia effettivamente eseguito.
_9_Esempio :  se vale tre, il cespite è stato ammortizzato per i primi due anni in modo anticipato e per il terzo in modo ordinario, non è possibile, nel quarto anno recuperare l'ammortamento anticipato non eseguito nel terzo anno, in quanto si è superata la soglia di anni ammessi per l'anticipato.
Se non impostato viene considerato zero :  non viene mai eseguito l'ammortamento anticipato, anche se inserito nel piano.
È possibile sfruttare questo comportamento per comprendere il seguente caso :  se si volessero distinguere due linee (normalmente fiscale e civilistica) solo per il fatto che nella prima si esegue anche l'ammortamento anticipato e per la seconda solo l'ordinario, è sufficiente definire un unico piano a livello di categoria, con impostato sia l'ammortamento ordinario sia l'anticipato ed inserire in questa tabella, per la linea fiscale, il numero di anni di ammortamento anticipato, e lasciare il campo vuoto per la linea civilistica. In tal modo per quest'ultima viene automaticamente escluso l'ammortamento anticipato, senza dover codificare un piano apposito.
 :  : FLD T$A5CD **Numero max anni ammortamento anticipato cespiti usati**
Definisce il numero di anni per i quali è ammesso eseguire l'ammortamento anticipato, per i cespiti usati (individuati dal campo di anagrafica).
Valgono le stesse considerazioni fatte per i cespiti nuovi.
 :  : FLD T$A5CF **Ammortamenti mensili**
Se impostato, viene scritto un movimento di ammortamento per ogni mese, se invece lasciato in bianco, viene scritto un unico movimento per tutto l'esercizio.
Il primo caso è tipico di cespiti industrali, in cui si vuol rilevare l'incidenza dell'ammortamento per ogni singolo mese; il secondo riguarda invece i cespiti fiscali, in cui l'importo dell'ammortamento è significativo su base annua.
In particolare , se impostato '1' vengono scritti movimenti mensili per tutti gli esercizi, se impostato '2' solo per l'esercizio in corso.
 :  : FLD T$A5CG **Valori alla data**
Se impostato, i movimenti di variazione del valore aggiornato del cespite (nuovi acquisti, vendite, rivalutazioni), non vengono considerati di competenza di tutto l'esercizio, ma a partire dalla data effettiva della loro registrazione. Di conseguenza il valore aggiornato nel cespite può avere un andamento variabile all'interno del periodo e, quindi, far variare anche l'ammortamento.
_9_Esempio :  nel caso in cui per un cespite, acquistato il primo settembre, si determini una quota di ammortamento annuale di 12 e se questo valore è stato impostato, l'ammortamento vale :  12 x (122/365) (dove 122 sono i giorni dal primo settembre al 31 dicembre).
Se invece viene lasciato in bianco, vale 12 (salvo ulteriori correzioni definite nella modalità del trattamento del primo anno).
 :  : FLD T$A5CI **Valore massimo cespiti minor**i
I cespiti, per i quali nel primo periodo di ammortamento il valore aggiornato del cespite è inferiore o uguale a questo valore, vengono ammortizzati totalmente in questo periodo.
Se questo valore non è impostato, non viene applicato l'ammortamento totale (ciò risulta automaticamente, non essendovi un cespite con valore minore di zero).
Se è stato impostato un valore specifico nel piano per il singolo cespite, esso ha la precedenza sul calcolo dei cespiti minori.
 :  : FLD T$A5CJ **Causale indeducibilità**
È un elemento della tabella A5B. Se impostato, e se presente la percentuale di indeducibilità sulla categoria, all'atto del calcolo dell'ammortamento, verrà scritto un movimento di ammortamento indeducibile con questa causale, che ridurrà la quota di ammortamento effettivo.
E' necessario che la causale abbia tipo movimento AN.
 :  : FLD T$A5CK **Causale non ammortizzabile**
È un elemento della tabella A5B. Se impostato, e se presente il valore massimo di capitale ammortizzabile sulla categoria, all'atto del calcolo dell'ammortamento, verrà scritto un movimento di riduzione capitale ammortizzabile con questa causale per la parte eccedente il massimo, che avrà l'effetto di ridurre la quota di capitale su cui eseguire l'ammortamento.
E' necessario che la causale abbia tipo movimento AQ.
 :  : FLD T$A5CL **Causale cespiti minori**
È un elemento della tabella A5B. Va impostato se è stato valorizzato il campo 'valore massimo cespiti minori'. È la causale di ammortamento assunta per eseguire il movimento per i cespiti minori, che sostituirà quanto speCiFicato nel piano di ammortamento. Dovrà essere una causale con tipo movimento di ammortamento ordinario, oppure di ammortamento istantaneo, se si vuole tenere un totalizzatore separato.
 :  : FLD T$A5CM **Risalita parametri cespiti**
È un elemento V2SI/NO. Se impostato, attiva il controllo di risalita sui parametri fissi del cespite per linea, al fine di controllare eventuali comportamenti specifici del cespite rispetto alla linea.
 :  : FLD T$A5CN **Esclusione Ammortamento periodo vendita/alienazione**
Tramite questo campo è possibile disattivare il calcolo dell'ammortamento nel periodo di vendita/alineazione del cespite.
Può assumere i seguenti valori : 
* " " = Si, ma solo se non è attiva la gestione per data. Se è attiva la gestione per data il calcolo rimarrà commisurato al periodo di possesso del cespite.
* "1" = No, il calcolo verrà sempre effettuato, anche nell'anno di vendita/alienazione del cespite.
* "2" = Si. A differenza del valore blank disattiva il calcolo anche in presenza della gestione per data.

 :  : FLD T$A5CP **Base calcolo valori alla data**
Questo campo ha significato in presenza di questi fattori : 

* Attivo calcolo alla data
* Linea con ammortamento mensile
* Cespite con criterio d'ammortamento per %

In presenza di questi fattori l'effetto su questi cespiti è che il totale degli ammortamenti eseguiti nell'esercizio va a corrispondere all'ammortamento calcolo con il valore del cespite aggiornato a fine esercizio, ma viene distribuito sui mesi in base alla movimentazione.

Esempio :  se acquisto al 1° luglio un cespite di 120 da ammortizzare al 10%, avrò un ammortamento mensile di 2, su tutti i mesi partire da luglio per un totale di 12 (senza attivare il campo invece avrei un ammortamento mensile di 1, su tutti i mesi a partire da luglio per un totale di 1).

E' da notare che per effetto di vendite parziali, può succedere che possa avere per i mesi successivi alla vendita, anche quote negative (al fine di ribilanciare i maggior ammortamenti avvenuti nei mesi precedenti alla vendita).

 :  : FLD T$A5CQ **Linea Piano**
Permette di definire una linea di riferimento per la determinazione del piano di ammortamento. In sostanza
se questo campo viene valorizzato non sarà necessario definire un piano di ammortamento specifico per la linea
in quanto verrà ripreso il piano previsto per la linea indicata. Ad esempio se all'interno dell'elemento 03 compilo questo
campo con 02 la linea 03 erediterà i piani della linea 02.
 :  : FLD T$A5CR **Data Limite**
Se impostato, con attivato anche il campo "valori alla data", è possibile forzare che il calcolo dell'ammortamento venga concluso per tutti i cespiti con residuo alla ivi indicata.
 :  : FLD T$A5CT **Ultimo esercizio**
In caso di ammortamento mensile, con calcolo alla data, indica come si vuole distribuire il residuo da ammortizzare dell'ultimo esercizio. Ci sono due opzioni : 
* Di default viene distribuito in modo omogeno l'importo residuo sui 12 mesi
* Valorizzando il campo ad 1 è possibile invece dire che ad ogni mese venga applicata la quota piena dell'ammortamento previsto, sino al mese in cui non rimane che un residuo.
Es. se la quota mensile fosse di 10 e l'ultimo esercizio avessi un residuo di 60, con il primo
metodo avrei una quota di 5 distribuita su 12 mesi, nel secondo caso invece avrei una quota di 10 per i primi 6 mesi e 0 da luglio in poi.

