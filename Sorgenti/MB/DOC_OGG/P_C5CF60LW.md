## Dettaglio schermata

## Intestazioni

- Fonte :  indica il codice e la descrizione della fonte
- FDo : 
- Dt.Doc. :  nel caso in cui la fonte sia rappresentata da un documento indica la data del documento stesso (nel caso di bolle entrata merce rappresenta la data riportata sulla bolla del fornitore)
- Documento :  nel caso in cui la fonte sia rappresentata da un documento indica il numero del documento stesso (nel caso di bolle entrata merce rappresenta il numero di docuemnto del fornitore)
- Dt Origine :  indica la data del docuemnto inbterno, ad esempio nel caso in cui la fonte sia una bolla entrata merce questo campo indica la data del documento Sme.UP
- N°Rig. :  indica il numero di righe presenti nel raggruppamento
- Quant.Prev. :  indica la quantità prevista per la fonte ovvero quella riportata sulla fonte origine
- Quant.Eff. :  indica la quantità effettivamente riportata in fattura
- Imponib.Prev. :  indica il valore previsto per la fonte, ad esempio nel caso in cui la fonte sia una bolla è l'importo riportato sulla bolla stessa
- Imponib.Effet. :  indica il valore effetivamente riportato in fattura
- N :  indica la presenza di note su origine (se attivata sulla fonte la rilevazione delle note)
- E :  indica la presenza di un errore bloccante nelle righe (es. non presente conto di contabilizzazione)
- W :  indica la presenza di un errore warning nelle righe che impedisce la selezione delle righe stesse (es. la divisa nella fonte è diversa da quella contabile)
- P :  indica se il pagamento della fattura è bloccato già dalla fonte
- V :  indica se la fonte è gestita con validazione o meno
- K :  indica se è presente una riga collegata al gestionale (es. una riga di un documento)


## Opzioni

- S :  Seleziona, permette di spostare in pagamento le righe in attesa
- D :  Deseleziona, permette di spostare in attesa le righe in pagamento
- CA :  Cambio assoggettamento IVA, cambia l'assogettamento IVA su tutte le righe selezionate che fanno parte del raggruppamento o del conto contabile in funzione del tipo di visualizzazione. Non viene eseguito su mancanti che sono già collegati ad altre registrazioni.
- CC :  Cambio conto contabile, cambia il conto contabile su tutte le righe selezionate che fanno parte del raggruppamento o del conto contabile in funzione del tipo di visualizzazione. Non viene eseguito su mancanti che sono già collegati ad altre registrazioni.
- 01 :  Dettaglio - Imm.fonti STD, permette di inserire una nuova fonte dando la possibilità di scegliere tra le fonti standard
- 02 :  Dettaglio - Modifica, permette di entrare e modificare la fonte. Nel caso in cui la fonte sia composta da più righe raggruppate con l'opzione 02 è possibile visualizzare il dettaglio delle righe e poi su di esse digitando nuovamente 02 è possibile modificare la riga.
- 04 :  Dettaglio - Cancella, permette di cancellare la fonte. Nel caso in cui la fonte sia composta da più righe raggruppate con l'opzione 04  è possibile visualizzare il dettaglio delle righe e poi su di esse digitando nuovamente 04 è possibile cancellare la riga.
- 05 :  Dettaglio - Visualizza, permette di visualizzare il dettaglio della fonte. Nel caso in cui la fonte sia composta da più righe raggruppate con l'opzione 05 è possibile visualizzare il dettaglio delle righe e poi su di esse digitando nuovamente 05 è possibile visualizzare la riga
- 12 :  Dett.Seq. - Modifica, permette di modificare il dettaglio delle righe in sequenza nel caso in cui la fonte sia formata da più righe. In pratica presenta in modifica la prima delle righe della fonte confermando con F6 passa alla seconda riga e così via.
- 14 :  Dett.Seq. - Cancella, permette di cancellare il dettaglio delle righe in sequenza.
- 15 :  Dett.Seq. - Visualizza, permette di visualizzare il dettaglio delle righe in sequenza.
- LI :  Dettaglio - Lista campi, visualizza il dettaglio dei dati riportati sul file che contiene la fonte.  Nel caso in cui la fonte sia composta da più righe raggruppate con l'opzione LI è possibile visualizzare il dettaglio delle righe e poi su di esse digitando nuovamente LI è possibile visualizzare il dettaglio dei campi della riga
- VO :  Origine   - Visualizza, permette di visualizzare l'origine della fonte. Ad esempio, nel caso in cui la fonte sia una bolla entrata permette di visualizzare la riga del documento.
- VT :  Origine(T)- Visualizza, permette di visualizzare la testata origine. Ad esempio, nel caso in cui la fonte sia una bolla entrata permette di visualizzare la testata del documento.
- VR :  Registrazione, permette di visualizzare la lista campi della testata della registrazione, ovvero il dettaglio delle informazioni riportate sul file.
- VF :  Fonte, permette di visualizzare la tabella che definisce la fonte.
- NC :  Inserisci non conformità, permette di inseire una non conformità
- NF :  Origine - Da non fatturare, permette di bloccare il pagamento della fattura agendo sulla fonte
- MO :  Origine   - Modifica, permette di modificare la riga origine.
- MT :  Origine(T)- Modifica, permette di modificare la  testata dell'origine (per le fonti con testata)
- DO :  Scheda documento, permette di visualizzare in LoocUP la scheda del documento (nel caso in cui la fonte sia un documento)
- CB :  Scheda controllo bolle/fatture, permette di accedere alla scheda del controllo bolle/fatture
- AO :  Scheda archiviazione ottica, permette di aprire la scheda di archiviazione ottica del fornitore.


## Impostazioni


- Valori previsti :  attraverso questa voce è possibile impostare le voci visualizzate nelle ultime quattro colonne della schermata. Le scelte disponibili sono : 
-- Quantità/Valore previsto :  vengono visualizzati la quantità prevista, quella effettiva, il valore previsto e quello effettivo.
-- Quanittà/Valore scostamento :  vengono visualizzati lo scostamento in quantità, la quantità effettiva, lo scostamento in valore e il valore effettivo.
-- Documento origine/valore previsto :  vengono visualizzati il numero del documento origine, la quantità effettiva, il valore previsto e il valore effettivo.
-- Documento origine/valore scostamento :  vengono visulizzati il numero del documento origine, la quantità effettiva, lo scostamento in valore e il valore effettivo.
- Schema selezionate :  attraverso questa voce è possibile definire uno schema specifico per le fonti selezionate e che quindi compaiono all'interno dell'area 'In pagamento'. Ad esempio in questo caso si è deciso di utilizzare per le righe selezionabili lo schema di default mentre per quelle selezionate vengono visualizzati il numero e la data della bolla, il codice pagamento, il codice IVA e il conto contabile : 
![C5C040_014](http://localhost:3000/immagini/MBDOC_OGG-P_C5CF60LW/C5C040_014.png)- Schema generale :  definisce lo schema generale delle righe visualizzate all'interno della schermata e viene applicato sia alle righe presenti nell'area 'In attesa' che a quelle presenti nell'area 'In pagamento' ad eccezione del caso in cui sia definito uno schema specifico per le righe selezionate.
- Dettaglio in lista :  permette di visualizzare il dettaglio delle righe delle fonti presenti : 
![C5C040_015](http://localhost:3000/immagini/MBDOC_OGG-P_C5CF60LW/C5C040_015.png)- Escludi NON selezionabili :  permette di visualizzare o meno all'intenro dell'area 'In attesa' le fonti non selezionabili.
- Ordinamento raggruppamenti :  permette di definire l'ordinamento dei raggruppamenti delle fonti; gli ordinamenti disponibili sono :  per data/documento origine, per codice/data del raggruppamento e per data/codice del raggruppamento.



## Tasti funzionali


- F04 :  Stampa lista. Permette di stampare la lista visulizzata (anche su file PDF)
- F05 :  Ricostruzione. Ricostruisce completamente la situazione ricreando la situazione presente all'apertura della schermata, di conseguenza effettuando delle selezioni e delle modifiche all'interno del controllo bole-fatture e digitando F5 vengono perse le modifiche fatte.
- F06 :  Conferma. Conferma le azioni eseguite.
- F13 :  Parzializzazioni. Accede alla finestra della parzializzazione
- F14 :  Abbinamento Mancanti. Cerca di collegare i mancanti alle righe in attesa e se li trova li sposta in pagamento. Se non è giroconto cancella il mancante.
- F15 :  Distribuzione Importi Riga. Distribuisce in modo proporzionale un importo sulle righe come prezzo aggiuntivo.
- F16 :  Visualizza raggruppamento/conto. Visualizza le righe totalizzate per raggruppamento o per conto contabile
- F17=Impostazioni. Apre la finestra delle impostazioni.
- F18=Inserimento fonte. Inseriscei una fonte standard (es. differenza prezzo o quantità)
- F19=Gestione Lista Mancanti. Gestione in lista delle fonti "Mancanti"
- F20=NON Conformità. Accede alla gestione non conformità(se attiva)
- F21=Immissione NON Conformità. Immissione di una non conformità(se attiva)
- F22=Selezione globale. Tutte le righe in attesa vengono spostate in pagamento (escluse le righe con warning)
- F23=Deselezione globale. Tutte le righe in pagamento vengono messe in attesa (tranne le righe mancanti già collegate)

