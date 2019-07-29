## Giacenza
>Se l'origine è GC (giacenza) : 
>Parametro 1 : 
-    Pos.1/2 :  Area giacenza (obbligatoria)
-    Pos.3 :  Giacenza di WIP :  se impostato questa fonte contiene materiale in corso
.           di lavoro. Questa informazione è utilizzata in caso di produzione a
.           disponibilità chiamata :  questa giacenza viene 'tirata' verso il
.           completamento del suo ciclo, costruendo gli impegni di risorse per le
.           operazioni rimanenti.
-    Pos.4/6 :  modo di considerare le varie quantità presenti nell'archivio : 
.             giacenza/allocato/atteso : 
.             Pos : 4     ' '  tratta la giacenza
.                       'N'  non tratta la giacenza
.
.             Pos : 5     ' '  non tratta la quantità allocata
.                       '+'  somma la quantità allocata
.                       '-'  sottrae la quantità allocata
.             Pos : 6     ' '  non tratta la quantità attesa
.                       '+'  somma la quantità attesa
.                       '-'  sottrae la quantità attesa
.             NB :  il segno della giacenza, se trattata, è dato implicitamente dal
.             segno della fonte.
Parametro 2 : 
-    Pos.1/2 : Tipo giacenza (obbligatoria)
-    Pos.3 :  E' un flag che guida la selezione delle righe di giacenza in base ai
.           limiti impostati (lotto, ubicazione, configurazione,  ecc..) nella
.           scansione della disponibilità. Se non è stato impostato nessun limite,
.           tutte le righe dell'area/tipo giacenza sono assunte come valide,
.           indipendentemente dal valore di questo flag.
.           Se questo flag è impostato, i limiti lasciati a blanks non vengono
.           considerati nella selezione delle righe di giacenza.
.           Ad esempio, se il tipo giacenza è per ubicazione/lotto, se si è
.           impostata l'ubicazione 'UB1' ed il lotto è lasciato a blanks, si hanno
.           i seguenti comportamenti : 
.                  Chiavi  di  giacenza
.           Flag 3    Ubicazione     Lotto     Riga valida
.           ' '       UB1            ' '            Si
.           ' '       UB1            'A'            No
.           '1'       UB1            ' '            Si
.           '1'       UB1            'A'            Si
.           Va tenuto inoltre presente che, se nella scansione della disponibilità si
.           impostano dei limiti (lotto, configurazione, ecc..), sono ritenute sempre
.           valide le righe di giacenza il cui tipo giacenza non contiene i tipi di
.           chiavi impostati. Ad esempio, nel caso precedente, se una riga di
.           giacenza ha un tipo giacenza per fornitore/commessa, essa è comunque
.           valida qualsiasi siano i valori impostati di ubicazione e lotto.
.           E' cura di chi compila le fonti e le raccoglie nei gruppi fonti
.           evitare, se lo ritiene opportuno, questa possibile incongruenza.
-    Pos.4/5/6/7/8 :  Se impostati, non verranno totalizzate le giacenze
.                   rispettivamente per i codici 1/2/3/4/5 (NB : il campo 5 è il
.                   collo) verrà ritornato il codice nel campo corrispondente.
.                   Se impostata almeno una tra queste posizioni, viene forzata a
.                   '1' la posizione 3, in quanto si assume che si vogliano ottenere
.                   tutte le giacenze di un area/tipo giacenza, (lasciando quindi in
.                   bianco il codice relativo, ad esempio l'ubicazione, il lotto,
.                   ecc..).
.                   Esempio :  si ha un tipo giacenza per Risorsa/Ubicazione/Lotto,
.                   e questi campi sono impostati ai valori : 
.                       '1'/' '/'1'/' '
.                   vuol dire che si avrà una riga di giacenza per ogni coppia
.                   Risorsa/Lotto, che verranno ritornati nei campi rispettivi
.                   della routine di scansione.
-    Pos.9 :  Definisce se e come azzerare le giacenze negative
.           NOTA :  la fonte giacenza ritorna una disponibilità che potrebbe essere la
.           somma di N record (per esempio quando c'è una seconda chiave di giacenza)
.           Può assumere i seguenti valori
.           ' ' - Vengono trattate tutte le giacenze, quindi nessun azzeramento
.           '1' - Vengono azzerati i record di giacenza con valore negativo
.           '2' - Vengono azzerati gli elementi di disponibilità con valore negativo
.           Esempio :  ci sono due record di giacenza con ubicazione differente, che devono
.           essere raggruppati : 
.           UB1 - Qauntità -3
.           UB2 - Quantità +2
.           Con l'impostazione '1' viene ritornato un elemento con quantità +2,
.           ed un elemento con quantità a zero (viene azzerata la quantità -3).
.           Con l'impostazione '2' viene tornato un elemento con qualtità a zero, dato che essa
.           serebbe negativa -1 = -3 +2.
.           Se non si imposta il ragrupapmento, le impostazioni '1' e '2' sono equivalenti.
.           NOTA IMPORTANTE : 
.           L'effetto del consolidamento disponibilità che avviene quando due o più fonti
.           giacenza hanno lo stesso ordinamento, è applicato a valle di tutte le considerazioni
.           appena fatte.
.           Questa correzione azzera la quantità della fonte, non influisce sul ritnro della fonte,
.           che è condizionato dalla scelta se ritornare o meno le fonti a zero (filtro che
.           agisce a valle di questa correzione).
Parametro 3 : 
-    Pos.1/2 : Tipo giacenza completamento (facoltativa)
.           Se impostato, il tipo giacenza può essere integrato (nei suo oggetti non riempiti)
.           con i campi di questo tipo giacenza.
.           Ad esempio, con la seguente situazione, con TG il tipo giacenza dell'archivio e TC
.           il tipo giacenza complementare, si otterrà questo tipo giacenza "virtuale" TV che sarà
.           trattato nell'analisi disponibilità
.           Posizione   TG        TC       TV
.                1      CM                 CM
.                2      LO        CF       LO
.                3      --        EM       EM
.                4      --        --       --
.           Naturalmente, dopo di ciò si dovranno riempire le posizioni aggiunte, in modo che
.           il record di GMQUAN venga trattato dall'analisi disponibilità come se avesse
.           effettivamente questi campi.
.           Questa azione si può fare sia con la consueta exit della fonte, anche con la funzione di
.           completamento giacenze guidata dalla tabella M5L, impostata nel campo successivo
-    Pos.3/4 :  Modo completamento chiavi giacenza (elemento della tabella M5L)
.           Se impostato questo campo contemporaneamente al precedente, e se effettivamene il tipo
.           giacenza complementare ha arricchito quello base, nell'analisi disponibilità verranno
.           completate le chiavi di giacenza secondo le regole definite nell'elemento di tabella M5L
.           al cui help si rimanda per le modalità di impostazione.

