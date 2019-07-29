# CLS - Classi articolo
 :  : DEC T(ST) K(CLS)
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM **Codice**
Codice attribuito alla classe materiale
 :  : FLD T$DESC **Descrizione**
Descrizione della classe
 :  : FLD T$ELSC **Elaborazione Analisi Scarti**
Immettendo il carattere S la classe verrà trattata dalla gestione Scarti.
 :  : FLD T$FSCA **% Std Scarto Assunta per la classe**
L'applicazione utilizza questa % per il calcolo dello scarto standard a meno che questa percentuale sia stata specificata a livello di articolo.
 :  : FLD T$CLSA **Classe funzionale di risalita**
È un elemento della tabella CQQ. Viene utilizzato come classe funzionale di risalita, se mancante sull'anagrafica articoli. In questo caso, gli articoli senza classe funzionale assumeranno quella specificata sulla classe materiale.
 :  : FLD T$CLSB **Nomenclatura combinata di risalita (SV)**
È un elemento della tabella BRN. Viene utilizzato come nomenclatura combinata di risalita, se mancante sull'anagrafica articoli. In questo caso, gli articoli senza nomenclatura combinata assumeranno quella specificata sulla classe materiale.
 :  : FLD T$CICA **Conto Contabile classe**
Utilizzati per condizionare l'immissione dei valori in contabilità analitica, in funzione della classe. Ad essi si fa riferimento in particolare nella tabella SCR.
 :  : FLD T$CISC.T$CICA **Conto Contabile classe**
 :  : FLD SRI,01 **Riclassifiche**
Campi per le riclassifiche utilizzate nelle analisi per articolo. Permettono una sintesi a diversi livelli. Si veda anche GLOSSARIO
 :  : FLD SRI,02 **Riclassifiche**
Vedi SRI,01.
 :  : FLD SRI,03 **Riclassifiche**
Vedi SRI,01.
 :  : FLD SRI,04 **Riclassifiche**
Vedi SRI,01.
 :  : FLD SRI,05 **Riclassifiche**
Vedi SRI,01.
 :  : FLD SRI,06 **Riclassifiche**
Vedi SRI,01.
 :  : FLD SRI,07 **Riclassifiche**
Vedi SRI,01.
 :  : FLD SRI,08 **Riclassifiche**
Vedi SRI,01.
 :  : FLD SRI,09 **Riclassifiche**
Vedi SRI,01.
 :  : FLD SRI,10 **Riclassifiche**
Vedi SRI,01.
 :  : FLD T$VDS **Voce di spese e Centro di costo assunti**
Questi due campi contengono i valori assunti quando non sono specificati nelle registrazioni contabili che li richiedono. In tal modo, è ad esempio possibile portare in una voce di spesa tutti i prelievi di utensili o materiali di consumo ecc...
 :  : FLD T$CDC.T$VDS **Voce di spese e Centro di costo assunti**
 :  : FLD T$PEMA **% Std obsolescenza**
Percentuale di obsolescenza assunta se non specificata a livello di articolo.
 :  : FLD T$COSA **Costo di riordino acquisti**
È il costo utilizzato dall' applicazione nella gestione del punto di riordino ecc...
 :  : FLD T$COSP **Costo di riordino produzione**
Come il campo precedente, ma riferito alla produzione.
 :  : FLD T$FARI **Famiglie ricariche**
È il codice elemento della tabella CSR che contiene i dati relativi al calcolo dei ricarichi per questa classe articolo.
Vedi tabella CSR.
