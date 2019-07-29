# C5Y - Fonti Controllo fatture
 :  : DEC T(ST) K(C5Y)
## OBIETTIVO
Definisce tutte le fonti che caratterizzaziono il controllo fatture.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM **Codice**
È l'elemento che definisce la fonte. Se inizia per "£" la fonte è riservata SMEUP.
 :  : FLD T$C5YA  **Fonte attiva**
Assume i seguenti valori : 
- " "=La fonte è attiva per il ciclo passivo (acquisti).
- "1"=La fonte è attiva per il ciclo attivo (vendite).
- "2"=La fonte è attiva sia per il ciclo passivo che attivo.
- "9"=La fonte non è attiva.
 :  : FLD T$C5YB  **Origine fonte**
È il suffisso XX del programma C5CF60_XX che gestisce la fonte.
 :  : FLD T$C5YC  **Parametro fonte**
È un campo specifico per la fonte passato al suo corrispondente programma.
__Fonte £02 :  Chiudere Aut.Manc.__
Chiude/riapre automaticamente il mancante se il conto è rispettivamente uguale/diverso da quello della fonte £02.
 :  : FLD T$C5YD  **Attiva pgm exit**
Attiva il programma di exit C5CF60_XXE richiamato dal programma specifico della fonte C5CF60_XX.
 :  : FLD T$C5YE  **Tipo/Param.Cod.Raggr.**
Indica il tipo/parametro del codice raggruppamento usato dalla fonte
 :  : FLD T$C5YF  **Conto assunto**
Indica il conto contabile associato alla fonte. È utilizzato per le fonti riservate SMEUP "£", solo nella contabilizzazione delle
fatture passive.
 :  : FLD T$C5YG  **Normalizzazione raggruppamento**
Indica se si vuole normalizzare il campo raggruppamento secondo le seguenti modalità : 
- alfanumerico, allineamento e compattazione a sinistra :  A-B CDE = A-BC (per lunghezza raggruppamento 4).
- numerico, allineamento a destra con riempimanto di zeri a sinistra :  1 = 0001 (per lunghezza raggruppamento 4).
 :  : FLD T$C5YH  **Lunghezza raggruppamento**
Indica la lunghezza a cui si vuole normalizzare il campo.
 :  : FLD T$C5YI  **Conto assunto prioritario**
Indica se, nella ripresa del conto contabile della riga, viene data priorità al "conto assunto" presente in questa tabella, rispetto al conto contabile determinato dall prima riga di fonte, presente nella registrazione.
 :  : FLD T$C5YJ  **Ripristino valore origine per delta prezzo**
Campo significativo solo se attiva la gestione delle Non Conformità. La modifica di un prezzo sulla fonte genera una Non conformità di tipo delta prezzo. Se la differenza di prezzo è dovuta al fornitore viene generato un documento e una corrispondente Non conformità di attesa nota di accredito. Se questo campo è valorizzato, viene ricalcolato il prezzo effettivo della fonte origine come (prezzo effettivo - valore della NC attesa documento). Per quadrare contabilmente la fattura il valore della NC attesa documento crea una riga aggiuntiva di tipo £03 sulla regitrazione contabile della fattura. Se il campo è valorizzato a "1"  il processo si innesca nella azione correttiva £DP. Se il campo è valorizzato a "2"  il processo si innesca nella registrazione contabile della Nota accredito.
 :  : FLD T$C5YK  **Programma exit per righe aggiuntive di output**
Suffisso XX del programma C5CF60L_XX. Costruisce righe di output aggiuntive visualizzate nei programmi C5CF60L e C5CF60M.
 :  : FLD T$C5YL  **Gestione conto differenza prezzo/quantità**
Se attivo carica i valori di delta prezzo/quantità presenti nella fonte su un conto contabile specifico e non sul proprio conto merce. Il conto specifico è quello indicato  nella fonte "£03" per i delta prezzo e "£04" per i delta quantità.
Da tener presente che questo si verifica sono in contabilità. Nel gestionale l'intero importo effettivo, compreso quindi il valore di delta, rimane sul proprio conto merce.
.
Esempio delta prezzo : 
.
Documento ContoContabile   ValorePrevisto   ValoreEffettivo   DeltaPrezzo
BOLLA01   CONTOMERCE               100,00            110,00         10,00
.
Contabilità
Riga ContoContabile           Valore
0001 CONTO-MERCE              100,00
0002 CDNTO-DELTAPREZZO         10,00
.
Gestionale
Documento Riga ContoContabile           Valore
BOLLA01   0001 CONTO-MERCE              110,00
