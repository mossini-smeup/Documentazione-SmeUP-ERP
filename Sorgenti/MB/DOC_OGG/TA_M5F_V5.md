## Riga di ciclo esterno
>Se l'origine è V5 (riga di ciclo esterno)
Parametro 1 : 
-    Pos.1/3   Tipo Documento (obbligatorio);
-    Pos.4/6   Tipo Riga (opzionale);
-    Pos.7/9   Modello Documento (opzionale);
-    Pos.10    Data rettificata :  se impostato, e se non si è scelto che la fonte sia
.              disponibile (posizione 2 del parametro 2), la data della fonte verrà
.              avanzata dei giorni di rettifica. Verranno usati i giorni di
.              rettifica di acquisto o lavorazione, reperiti dai dati di
.              pianificazione per articolo, in base alla caratteristica della riga
.              (flag 10 del record di riga).
.              Verrà usato il magazzino su cui si sta eseguendo l'analisi
.              disponibilità, sia per reperire i dati di pianificazione sia per
.              reperire il calendario (posto che non si sia impostato, in tabella
.              M51, di trattare giorni solari).
.              Questa rettifica è significativa per coperture (fonti positive).
.              In questo modo si interpone una 'sicurezza' tra la data di consegna
.              del materiale e quella del suo utilizzo. Inoltre, dato che la
.              pianificazione propone ordini che tengono conto di questo tempo, se,
.              dopo il loro rilascio non se ne continuasse a tenere conto, la
.              pianificazione successiva suggerirebbe un anticipo, del tutto
.              superfluo, pari al tempo di rettifica.
Parametro 2 : 
.    Pos.1     '1' se al netto dell'attesa spedizione/entrata;
-    Pos.2     '1' se fonte disponibile (con data 0). Questo campo va impostato nel
.                  caso di una riga di documento di spedizione o ricevimento non
.                  ancora collegata. In questa situazione la quantità del documento
.                  va a incrementare o a decrementare la giacenza; questa fonte,
.                  avendo la data a 0, diventa implicitamente una fonte esistente.
-    Pos.3     '1' se non controllo flag collegamento. Questo campo va impostato nel
.                  caso di una riga di ordine, (è obbligatorio farlo se essa deriva
.                  da un documento precedente come previsione/ordine aperto), oppure
.                  se si è impostato esplicitamente che è una riga da non collegare,
.                  nel flag opportuno. Va invece lasciato in bianco nel caso di
.                  documenti di spedizione o di ricevimento.
-    Pos.4     Se impostato, vengono trattate solo le righe che hanno il tipo
.              modello riga (flag 12) concorde con questo valore.
.              _9_Esempio :  si possono escludere in un tipo documento di uscita,
.               le righe di entrata (resi), e viceversa.
-    Pos.5     Se impostato 'I' mostra la quantità in unità di misura interna.
.              Se impostato 'E' mostra la quantità in unità di misura esterna.
.              Se impostato ' ' e se ricevuta una unità di misura, mostra la
.              quantità corrispondente. Se l'unità di misura ha blanks, mostra la
.              quantità in unità di misura interna.
-    Pos.6     Se impostato, calcola la quantità al netto della quantità in richieste
.              di movimentazione.
-    Pos.7     Ente del documento (su cui si esegue la parzializzazione e che viene
.              ritornato tra i campi della fonte).
.              -- ' ' ente di spedizione.
.              -- 'I' ente intestatario del documento.
.              -- 'P' ente preferenziale.
.              -- 'D' ente di destino.
-    Pos.8     Se impostato, l'ente precedente è solo di parzializzazione ed il
.              seguente è quello ritornato
.              -- 'S' ente di spedizione.
.              -- 'I' ente intestatario del documento.
.              -- 'P' ente preferenziale.
.              -- 'D' ente di destino.
.              NB :  in questo caso l'ente si spedizione va impostato in quanto il
.              default non è, come per il caso precedente, l'ente di spedizione,
.              ma per il fatto che l'ente di ritorno è uguale all'ente di
.              parzializzazione.
-    Pos.9     Si imposta la data fonte a cui si riferisce la fonte. Se la fonte è
.              'attuale', la data è comunque a zero, se è invece attiva la rettifica,
.              essa viene eseguita a partire da questa data.
.              Si può scegliere tra le seguenti date : 
.              -- ' ' consegna confermata.
.              -- '1' consegna richiesta.
.              -- '2' inserimento.
.              -- '3' bolla, se assente consegna confermata.
.              -- '4' partenza, se assente bolla, se assente consegna confermata.
-    Pos.10    Se impostato, viene considerato il plant di trasferimento.
Parametro 3 : 
.    Pos.1     Flag7 Inversione Qtà/Valore :  consente di specificare comportamenti
.              specifici in funzione del valore assunto dal campo R§FL07 della riga
.              del documento V5 :  I valori possibili sono : 
.                             Il campo R§FL07 vine ignorato
.              1              La quantità della riga viene invertita se il campo
.                             R§FL07 è impostato
.              2              La quantità della riga viene invertita se il campo
.                             R§FL07 non è impostato
.              3              La riga viene esclusa se il campo R§FL07 è impostato
.              4              La riga viene esclusa se il campo R§FL07 non è
.                             impostato
.              Uno dei possibili utilizzi potrebbe essere ad esempio quello di
.              un'unica fonte che comprenda tutti i documenti di tipo Ordine ciclo
.              attivo, dove si  vogliano correttamente impostare le quantità
.              positive e negative a fronte di righe di ordine di vendita e righe
.              di ordine di reso materiale.
.    Pos.2     Si inserisce un valore 1,2,... 9,A In tal modo viene assunta, se
.              presente, la data libera (1 - 10), corrispondente al valore impostato.
.              Se essa è a zero, ci si riconduce alla modalità normale di
.              assegnazione data (definita in precedenza).
.              **NB** :  il flag 'fonte disponibile' ha la priorità su questa
.              impostazione.
.    Pos.3     No filtro fase. Se impostato, NON verrà eseguito alcun controllo
.              della fase presente sulla riga di documento, ma verranno ritornate
.              tutte le righe (con il campo operazione R§OPER ritornato nel campo
.              sequenza).
.              Questa forzatura può essere utile, ad esempio, per ritornare le righe
.              di conto lavoro di fase, indipendentemente dalla sequenza eseguita).
.              Essa va impostata con molta attenzione, in quanto accomuna gli ordini
.              di TUTTE le fasi eseguite.
.              Il filtro fasi, nelle righe V5, opera nel seguente modo : 
.              - se la riga ha una fase significativa (flag 13 valorizzato a B o a
.                C), è valida se la sua fase è uguale a quella ricevuta (la fase
.                bianca è una fase come un'altra, non viene assunta come fase
.                qualsiasi).
.              - negli altri casi (flag 13 con un valore diverso dai precedenti),
.                la riga è valida se la fase ricevuta non è bianca (in questo caso
.                sono valide solo le righe precedenti).

