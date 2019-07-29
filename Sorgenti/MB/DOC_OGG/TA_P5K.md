# P5K - Causali rilevazione
## OBIETTIVO
Definisce le caratteristiche relative alla causale di eventi di rilevazione.
Contesualmente alla scrittura di un elemento di questa tabella, viene scritto in
automatico un elemento con lo stesso nome e descrizione, della tabella di causali evento
(settore P5E sottosettore £R).
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM Codice
Indica il codice della causale dell'evento di rilevazione.
 :  : FLD T$DESC Descrizione
Descrizione

 :  : FLD T$P5KA **Natura causale**
È un valore V2/P5RTC :  definisce la natura della causale.

 :  : FLD T$P5KB **Ferma rilevaz.errate**
Definisce il comportamento in casi di presenza di anomalie durante la dichiarazione dell'evento di
rilevazione.
**Si**, consigliata quando è eseguita dall'operatore in tempo reale
**No**, obbligatoria quando è eseguita dalla rilevazione di campo

 :  : FLD T$P5KC **Applica subito**
Definisce la modalità con la quale gli eventi compatibili vengono chiusi generando una attività di
produzione.
**Si**, quando si vuole generare immediatamente le attività di produzione.
**No**, quando si vuole delegare il controllo degli eventi di rilevazione ad un responsabile.
**Batch**, quando si vuole generare immediatamente le attività di produzione, sbloccando il
             richiedente. (solo in fase di Inserimento)

 :  : FLD T$P5KE **Causale attività**
Codice dell'attività da utilizzare nelle attività di produzione

 :  : FLD T$P5KF **Sottocausale attività**
Codice della sotto attività da utilizzare nelle attività di produzione

 :  : FLD T$P5KG **Modifica attività**
Permette la modifica dell'attività di produzione
**Si**, se l'evento di rilevazione viene modificato, ed è associata ad una attività di produzione
          quest'ultima verrà cancellata e rieseguita.
**No**, se l'evento di rilevazione viene modificato, ed è associata ad una attività di produzione
          quest'ultima non verrà modificata.

 :  : FLD T$P5KH **Exit utente**
E' il suffisso della exit B£G950_x, in cui è possibile impostae comportamenti specifici.
Riferirsi al prototipo B£G950_X, per la documentazione dei richiami.
Va tenuto presente che in questo campo si imposta una exit "possibile".
Essa verrà eseguita solo se, nell'elemento della P56 corrispndente al plant che si sta trattando,
è impostato il flag di esecuzione della exit.

 :  : FLD T$P5KI **Associazione singola**
Il responsabile può avere un solo evento di rilevazione attivo.
 :  : FLD T$P5KN **Riapertura multipla**
Se attivata la rilevazione delle presenze a seguito dell'interruzione delle attività per
dichiarazione di uscita, alla sucessivca dichiarazione di entrata non verifica se l'attività
è già stata aperta da un'altro utente. Attiva solo su una causale di tipo entrata.

 :  : FLD T$P5KQ **Sfondo evento**
Lo sfondo potrà essere personalizzato tenedno però conto del codice dei colori stanadrd per la
sicurezza e la segnaletica (NON si dovrebbe utilizzare un colore come il verde per indicare
una situazione di pericolo o potenziale tale)
Il valore sarà espresso nelle sue componenti RGB. Es  :  255,140,200

