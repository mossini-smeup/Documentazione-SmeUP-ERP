# CONTROLLO FATTURE - LISTA

>INTESTAZIONI
    N = Presenza note su origine
    E = Presente un errore bloccante nelle righe
    W = Presente un errore warning nelle righe : 
        . B=blocco ricezione riga;
        . D=divisa fonte diversa da divisa contabile;
        . V=riga da validare;
        . ...
        la riga non è selezionabile
    P = Blocco pagamento fattura
    V = Blocco ricezione
    K = Presente una riga collegata al gestionale

>IMPOSTAZIONI
    - Possibilità di visualizzare il valore previsto o lo scostamento
      tra il valore previsto e effettivo
    - Possibilità di visualizzare il dettaglio mancanti

>OPZIONI
    S  = Seleziona
         . sposta in pagamento le righe in attesa
    D  = Deseleziona
         . sposta in attesa le righe in pagamento
    CA = Cambio assoggettamento IVA
         . cambia l'assogettamento IVA su tutte le righe selezionate
           che fanno parte del raggruppamento o del conto contabile in
           funzione del tipo di visualizzazione .
           Non viene eseguito su mancantiche sono già collegati ad
           altre registrazioni.
    CC = Cambio conto contabile
         . cambia il conto contabile su tutte le righe selezionate
           che fanno parte del raggruppamento o del conto contabile in
           funzione del tipo di visualizzazione .
           Non viene eseguito su mancantiche sono già collegati ad
           altre registrazioni.
    02 = Dettaglio - Modifica
         . modifica dettaglio riga (*)
    04 = Dettaglio - Cancella
         . cancella dettaglio riga(*)
    05 = Dettaglio - Visualizza
         . visualizza dettaglio riga(*)
    12 = Dett.Seq. - Modifica
         . modifica dettaglio righe in sequenza senza passare a
           gestione lista dettaglio se pià di una riga
    14 = Dett.Seq. - Cancella
         . cancella dettaglio righe in sequenza senza passare a
           gestione lista dettaglio se pià di una riga
    15 = Dett.Seq. - Visualizza
         . visualizza dettaglio righe in sequenza senza passare a
           gestione lista dettaglio se pià di una riga
    LI = Dettaglio - Lista campi
         . lista campi dettaglio riga(*)
    NC = Inserisci non conformità
         . inserimento non conformità (se attiva gestione)
    MO = Origine   - Modifica
         . modifica riga origine se autorizzati (*)
    VO = Origine   - Visualizza
         . visualizza riga origine (*)
    MT = Origine(T)- Modifica
         . modifica testata origine se autorizzati
           (per le fonti con testata)
    VT = Origine(T)- Visualizza
         . visualizza testata origine se autorizzati
           (per le fonti con testata)
    VR = Registrazione
         . visualizza lista campi testata registrazione
    VF = Fonte
         . visualizza tabella fonte
    (*) se presente più di una riga opzione gestita a lista dettaglio

>TASTI FUNZIONALI
    F05=Ricostr.
        . ricostruisce completamente la situazione
    F06=Conferma
        . conferma finale
    F13=Parzializz.
        . finestra parzializzazione
    F14=Abb.Manc.
        . cerca i mancanti fra le righe in attesa e se trovati li
          sposta in pagamento. Se non è giroconto cancella il mancante.
    F15=Distr.Imp.Riga
        . distribuzione proporzionale di un importo sulle righe come
          prezzo aggiuntivo.
    F16=Visualizza raggruppamento/conto
        . Visualizza le righe totalizzate per raggruppamento o per
          conto contabile
    F17=Impostaz.
        . finestra di impostazioni di visualizzazione
    F18=Inserim.fonte
        . inserimento di una fonte non utente
    F19=Gest.Lis.Manc.
        . gestione in lista fonte mancanti
    F20=NON Conf.
        . gestione non conformità(se attiva)
    F21=Immissione NON Conf.
        . immissione non conformità(se attiva)
    F22=Sel.glob.
        . tutte le righe in attesa vengono spostate in pagamento
          (vengono escluse le righe con warning)
    F23=Des.glob.
        . tutte le righe in pagamento vengono messe in attesa
          (tranne le righe mancanti già collegate)

>ANALITICA
_9_Caricamento iniziale dettaglio analitica da fonte utente
. da campi corripondenti della fonte
. risalita alla 1° riga del modello. Solo se ha percentuale 100.
_9_Gestione dettaglio analitica (Dati con F18)
. propone dettagli ricevuti dalla fonte.
. al cambio del conto contabile ripresa dettaglo della 1° riga del modello. Solo se ha percentuale 100.
. possibilità di modifica dati
_9_Costruzione resgistrazione contabile
. se ricevuti tutti i dettagli crea una solo riga di analitica con valore di riga
. se ricevuti parzialmente i dati di dettaglio completa con le righe di modello.
_9_ESEMPIO
                   VdS     CdC      %
                   ------------------
  modello          V01     C01     20
                   V02     C02     30
                   V03     C03     50

. esempio 1 :  nessun dato di input
                   VdS     CdC      %
                   ------------------
  input             -       -

  registrazione    V01     C01     20
                   V02     C02     30
                   V03     C03     50

. esempio 2 :  Input CdC
                   VdS     CdC      %
                   ------------------
  input             -      C99

  registrazione    V01     C99     20
                   V02     C99     30
                   V03     C99     40

. esempio 3 :  Input VdS e CdC
                   VdS     CdC      %
                   ------------------
  input            V99     C99

  registrazione    V99     C99    100
