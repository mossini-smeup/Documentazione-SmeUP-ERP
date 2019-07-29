# MM1 - Personalizzazione manutenzioni
## CONTENUTO DEI CAMPI
 :  : FLD T$TICO Tipo Costo
Definisce il tipo costo utilizzato per i calcoli relativi ai costi della manodopera (centro di costo del dipendente che esegue) e del fermo macchina (centro di costo definito nell'anagrafica) degli interventi.
 :  : FLD T$TICS __Tipo Costruttore__
Serve per indicare a quale anagrafica o tabella si riferisce il campo 'COSTRUTTORE' (campo presente nella scheda impianti).
 :  : FLD T$PACS __Parametro Costruttore__
Indica da quale tabella ricavare il Costruttore. Da specificare solo se il campo 'Tipo Costruttore' è uguale a TA(tabella).
 :  : FLD T$TIFO __Tipo Fornitore__
Specificare l'anagrafico fornitori o una tabella fornitori se si desidera decodificare un codice
 :  : FLD T$PAFO __Parametro Fornitore__
Indicare a quale tabella accedere per interrogare i codici fornitori
 :  : FLD T$OBB1 __Obbligatorietà Costruttore__
Gestisce il modo di decodificare il campo Costruttotre / Fornitore.
Il campo può assumere tre significati diversi  : 
**1** :  la lettera C implica che il campo può contenere solo un codice ricavato dall'anagrafica/tabella indicata nel Tipo Costruttore/Fornitore.
**2** :  la lettera N fa in modo che non vengano eseguiti controlli su quello che l'utente scrive. Con un "?" o "!" si interroga l'anagrafica o la tabella specificata e nel campo è riportata la descrizione del codice selezionato.
**3** :  con la lettera L nel campo si può digitare qualsiasi cosa.
 :  : FLD T$OBB2.T$OBB1 __Obbligatorietà Fornitore__
 :  : FLD T$MM1N __Tipo data intervento__
Nella registrazione di un intervento, la data inizio può essere pre-impostata in tre diversi modi; il campo può assumere quindi tre significati diversi : 
- **0** :  la data non viene impostata;
- **1** :  la data viene impostata ad oggi;
- **2** :  la data viene impostata a quella di prevista esecuzione.
 :  : FLD T$MM1A __Note Dichiar.Intervento__
Permette di indicare quale contenitore note associare alla dichiarazione d'intervento.
 :  : FLD T$MM1B __Scheda dich. Intervento__
È un elemento della C£E
 :  : FLD T$MM1C __Tipo e Parametro Oggetto Intervento__
Indica l'oggetto di dettaglio che si vuole riportare sulla dichiarazione di intervento.
Indica, inoltr, se l'oggetto di intervento è obbligatorio in dichiarazione intervento sugli interventi di tipo : 
 - (1) pianificati eseguiti;
 - (2) pianificati non eseguiti;
 - (3) straordinari.
 :  : FLD T$MM1D __Obbligatorietà oggetto di rif. intervento__
Il campo è sensibile alla posizione e accetta i valori : 
1.2._    _.2.3    1._.3    1._._    _.2._  _._.3  1.2.3
 :  : FLD T$MM1E __Obbligatorietà tempi di intervento__
Indica se il tempo di intervento è obbligatorio in dichiarazione intervento. La codifica è simile all'obbligatorietà dell'oggetto di rif. intervento.
 :  : FLD T$MM1G __Obbligatorietà 1°esecutore intervento__
Indica se il primo esecutore di intervento è obbligatorio in dichiarazione intervento. La codifica è simile all'obbligatorietà dell'oggetto di rif. intervento
 :  : FLD T$MM1F __Obbligatorietà causale di intervento : __
Indica se la causale di intervento è obbligatoria in dichiarazione intervento. La codifica è simile all'obbligatorietà dell'oggetto di rif. intervento
 :  : FLD T$MM1H __Obbligatorietà esito intervento : __
Indica se l'esito di un intervento è obbligatorio in dichiarazione intervento. La codifica è simile all'obbligatorietà dell'oggetto di rif. intervento
 :  : FLD T$MM1I __Obbligatorietà causale intervento__
Indica se la causale di un intervento è obbligatoria in dichiarazione intervento. La codifica è simile all'obbligatorietà dell'oggetto di rif.intervento
 :  : FLD T$MM1M __Tipologia materiali__
Richiama un elemento della tabella MMM, se valorizzato accetta solo la tipologia impostata.
 :  : FLD T$MM1L __Limite superiore ore intervento__
Indica il numero massimo di ore dichiarabili in un intervento.
 :  : FLD T$MM1P __Parametri impliciti Intervento__
È un elemento della C£I
 :  : FLD T$MM1Q __Gruppo Flag__
È un elemento della B£Y, determina l'impostazione dei flag dell'intervento in fase di creazione.
 :  : FLD T$MM1R __Gruppo Flag__
È un elemento della B£Y, determina l'impostazione dei flag nell'archivio materiali in fase di creazione.
 :  : FLD T$MM1S __Parametri interventi Pian/Sched.__
È un elemento della C£E
 :  : FLD T$MM1T __Parametri interventi Pian/Sched.__
È un elemento della C£I
