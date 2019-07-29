# WFP - Tipo Promemoria
## CONTENUTO DEI CAMPI
 :  : FLD T$WFPA **Tipo data riferim.**
E' la data utilizzata come data di riferimento per il calcolo della data ora di emissione del promemoria (tramite i valori del V2/WF_24) : 
 * 0 - Data libera;
 * 1 - Data attivazione impegno;
 * 2 - Data rich.esec.impegno;
 * 3 - Data rich.esec.ordine.
 :  : FLD T$WFPB **Modalità calcolo**
La data ora di emissione del promemoria può essere calcolata in due modi (V2 WF_23)
 * 1 - Orario assoluto  :  la data ora di emissione viene indicata direttamente nel record del promemoria.
 * 2 - Tempo prima della data riferim.  :  la data ora di emissione viene ricalcolata in base alla  data di riferimento (sul record vengono indicati giorni, ore e minuti di anticipo rispetto alla  data di riferimento ai quali emettere la notifica).
 :  : FLD T$WFPC **Rimanda di minuti**
Minuti dopo i quali posporre il promemoria se l'utente sceglie l'azione "Ricordamelo dopo"
 :  : FLD T$WFPD **Contenitore note**
Indica quale contenitore note utilizzare per la costruzione del corpo del messaggio del promemoria.
Possono essere usati contenitori di F3 (promemoria), F1 (ordine workflow) e F2 (impegno).
Se questo campo non è compilato verrà composto un testo standard a seconda della data di riferimento utilizzata (es. attivazione, richiesta esecuzione, ...).
 :  : FLD T$WFPE **Limita su principale**
Se questo campo è flaggato viene testato, all'atto dell'emissione dei promemoria, se l'utente del promemoria è utente principale oppure no.
Questo serve per distribuire promemoria a tutti i potenziali esecutori di un impegno, evitando però di attivarli a tutti quando uno degli utenti prende in carico l'impegno.
 :  : FLD T$WFPI **Tipo notifica**
Indica il tipo notifica associato al tipo promemoria. Deve essere un tipo notifica push.
Se impostato, alla scadenza di un promemoria viene incrementato il tipo notifica specificato.
 :  : FLD T$WFPL **Tipo mail**
Indica il tipo mail associato al tipo promemoria. Se impostato, alla scadenza di un promemoria viene inviata una mail al responsabile del promemoria (una mail per ciascun promemoria).
