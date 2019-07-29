
Tramite questo programma è possibile conciliare i movimenti di accredito/addebito ricevuti dal
remote con le partite aperte presenti nel sistema.

# TESTATA

Nella prima parte della schermata vengono riportati i filtri applicabili alle scadenze aperte : 

* RSoc. :  per Ragione Sociale e Ragione Sociale Aggiuntiva.
* Doc. :  per N° di Documento.
* del. :  per Data Documento.
* CF/PI :  per codice fiscale/partita IVA - questo campo viene automaticamente riempito con quanto
viene riportato nel relativo campo del tracciato del remote.
* N° Ass. :  permette di applicare un filtro per n° di titolo, viene presentato solo se la banca ha trasmesso anche un n° di assegno.
* Ind. :  per Indirizzo
* Loc. :  per Località
* CAP  :  per CAP
* Pr   :  per Provincia
* Nz   :  per Provincia
Tutti i filtri a parte quello per data documento vengono applicati con una funzione di scansione
(basta perciò che il codice indicato nel filtro sia contenuto nel/i campo/i in cui viene effettuata la ricerca.

Nella parte successiva vengono riportate le principali informazioni rilevanti del movimento di
remote : 
* CF/PI :  codice fiscale/partita IVA;
* N° Ass. :  n° di assegno (viene visualizzato solo se presente);
* Descr :  è il risultato della concatenazione di tutti i campi descrittivi trasmessi dal remote;
* Rf.Ban. :  è il n° di CRO;
* Dt.Op.  :  è la Data Operazione Bancaria;
* Dt.Vl.  :  è la Data Valuta Bancaria;

# DETTAGLIO

In questa sezione vengono riportate le scadenze aperte risultati dai filtri applicati. Queste
vengono ordinate secondo questo criterio di ordinamento : 
* Corrispondenza della natura di pagamento :  se non è presente il n° di assegno, vengono presentati
prima i bonifici e di seguito le altre nature.
* Differenza in valore assoluto fra la data operazione e la data scadenza.
* Differenza fra importo origine del movimento e del residuo della scadenza.

Se fra le scadenze filtrate viene individuata una corrispondenza per importo, la prima scadenza
corrispondente viene automaticamente selezionata.

## COLONNE

* ?  :  mi permette di eseguire le azioni di riga : 
** S  :  Salda l'importo residuo della rata
** R  :  Salda il residuo della riga
** D  :  Deseleziona l'importo da saldare
** Z  :  Visualizza le funzioni della scadenza
** E  :  Visualizza le funzioni dell'ente
* Soggetto :  in questo campo vengono contenute le seguenti informazioni
** Il codice del soggetto o il codice fiscale/partita iva se viene applicato un filtro per questo
campo;
** La ragione sociale del soggetto;
** In presenza di filtro per n° assegno, il n° di titolo;
* Dt.Doc.  :  Data Documento
* N° Doc.  :  N° Documento
* Dt.Sca.  :  Data Scadenza
* N  :  Natura Pagamento della rata
* Importo da Sald. :  Importo che si vuole saldare
* A :  mi permette di eseguire una forma di abbuono per il reisudo della rata
* Residuo  :  Importo residuo della scadenza


# PIEDE

In questa sezione vengono riportati tutti gli importi rilevanti dell'operazione : 
* Div. Mov. :  Divisa del movimento bancario;
* Imp. Mov. :  Importo del movimento bancario;
* Div. Ori. :  Divisa dell'accredito/addebito di origine (potrebbe perciò non corrispondere a quella
del movimento,
bancario);
* Imp. Ori. :  Importo dell'accredito/addebito di origine;
* Totale    :  Indica l'importo totale delle scadenze selezionate;
* Residuo   :  Indica la differenza fra il totale delle scadenze selezionate e l'importo originale del
movimento (il campo è visualizzato solo se l'importo è diverso da 0);

## TASTI FUNZIONE

* F02 :  Help
* F06 :  Conferma - Se presente residuo verrà richiesto se si vuole creare un anticipo per tale importo
* F12 :  Abbandono

