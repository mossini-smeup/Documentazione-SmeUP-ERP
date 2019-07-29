La stampa dei registri IVA può essere eseguita n volte in provvisorio, una volta in definitivo ed n volte in copia; in modalità provvisoria anche su singoli (uno o più) registri.

La videata di selezione della stampa presenta le seguenti informazioni e richieste : 
 * _2_Ultimo periodo stampato Viene presentato come informazione, memorizzato nella tabella B£4.
 * _2_Elaborazione mensile/trimestrale E' funzione dell'impostazione fatta nei dati aggiuntivi azienda. Viene richiesto il mese/trimestre che si intende elaborare, controllato come periodo nella tabella PER.
 * _2_Tipo registro Campo non obbligatorio che, se riempito come da tabella di aiuto, consente di ottenere la stampa di tutti i registri facenti parti del tipo selezionato, senza dover specificare altro nella selezione successiva.
 * _2_Codice registro Campi non obbligatori che, se riempiti come da tabella di aiuto, consentono di ottenere la stampa di tutti i registri facenti parti del range selezionato, senza dover specificare altro nella selezione precedente.
 * _2_Tipo stampa Può essere effettuata n volte in modalità provvisoria ('P'), una volta soltanto in modalità definitiva ('D') e n volte in modalità ristampa ('R').
 ** ATTENZIONE :  la stampa definitiva comporta un aggiornamento della data ultima stampa nella tabella B£4, del numero ultima pagina stampata per ogni registro nella tabella C5R, nonchè il riempimento del flag di stampa registri IVA su tutti i movimenti contabili che compongono la stampa selezionata, rendendo in tal modo protette da modifica al-cune parti della registrazione stessa.
 * _2_Escludi controllo errori Se lasciato vuoto ('NO'), antepone alla stampa dei registri selezionati un controllo di correttezza dei dati che vi compariranno :  se vengono riscontrati problemi (mancanza di partita IVA su enti o errori/buchi nella sequenza dei protocolli), viene emessa una stampa di segnalazione e bloccata l'emissione di tutti i registri eventualmente selezionati. Se posto a '1' ('SI'), consente di forzare la stampa dei registri anche in presenza di errori, sia in definitivo che in provvisorio.
 * _2_Intestazioni Se la stampa viene eseguita su moduli non intestati precedentemente, è possibile ottenere l'intestazione durante la stampa dei registri con o senza dati societari completi.
 * _2_Stampa differite Se richiesto, viene prodotta una stampa apposita per quelle registrazioni con data competenza IVA nel mese selezionato ma data protocollo diversa da essa.
 * _2_Stampa Pag.IVA Esig.Diff. Se richiesto, viene prodotta una stampa dei pagamenti eseguiti nel mese inerenti fatture con IVA in sospensione.
 * _2_Numerazione pagine Se la stampa viene eseguita su moduli non intestati precedentemente, è possibibile ottenere la numerazione delle pagine durante la stampa dei registri.
 * _2_Dati integrativi Se lasciato vuoto ('NO'), sul registro IVA verranno stampati solo ragione sociale e partita IVA/codice fiscale per ente, se posto ad '1' ('SI') verranno aggiunti indirizzo e località dell'ente.
 * _2_Sintesi riepilogativa Se posto ad '1' ('SI'), in coda al registro riepilogativo verrà riportata una sintesi per registro-assoggettamento.

 La stampa va confermata con**F6**, e si compone dei seguenti campi : 
 * _2_Nr/Data Protocollo Rappresentano l'ordinamento con il quale viene organizzata la stampa, devono essere perfettamente sequenziali, nel caso si verifichi un errore nella sequenza una lista ne segnalerà il motivo.
 * _2_Tipo/Numero/Data Documento Estremi del documento registrato e protocollato.
 * _2_Cliente/Fornitore Ragione sociale dell'ente a cui il documento è intestato.
 * _2_Part.IVA/Cod.Fiscale Estremi fiscali riferiti all'ente di cui sopra.
 * _2_Imponibile Imponibile in moneta di conto della riga IVA.
 * _2_Aliq.IVA Codice e % IVA (o descrizione, se non imponibile) abbinata alla riga IVA.
 * _2_Imposta (deducibile) Imposta in moneta di conto calcolata tramite i due valori precedenti.
 * _2_Imposta indeducibile Presente solo per registri acquisti, nel caso l'imposta sia parzialmente o totalmente indeducibile.
 * _2_Importo Fattura Importo del documento.

La stampa, se si è scelto il formato esteso, viene completata eventualmente anche da indirizzo e località dell'ente.

Nel caso il programma che precede la stampa vera e propria trovi delle anomalie, viene bloccata la stampa dei registri ed emessa una lista di errori per ogni registro sul quale ve ne fossero :  come detto, errori sulla sequenza dei protocolli oppure mancanza della partita IVA/codice fiscale per qualche ente.
E' possibile ottenere comunque una stampa dei registri, forzando il controllo errori.

Al termine della stampa del registro si può richiedere la stampa della sintesi per codice IVA, suddivisa in fatture e rettifiche (note credito).
