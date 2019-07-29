# Generalità
Introduciamo in alcuni processi aziendali controlli preventivi che impediscono il formarsi di giacenze negative. I controlli sono fatti in modo che attraverso una specifica classe di autorizzazione sia possibile impedire o segnalare la possibilità di creare una giacenza negativa.

## Elenco Processi Aziendali coinvolti
  * Movimenti Magazzino Manuali
  * Flussi Entrata
   ** Entrata Conto Lavoro Pieno
  * Flussi Uscita Materiale
   ** Spedizione Conto Lavoro
   ** Resi Riparazione
   ** Resi Materiale Non conforme
   ** Vendita Ricambi
   ** Vendita da Conto Deposito Cliente
  * Richieste Movimentazione
  * Prelievi Commessa
  * Prelievi Ordini Officina
  * Prelievi Kit
  * Stampa Ddt

# Componente per controllo negativi
E' disponibile una /copy che consente di centralizzare i comportamenti di controllo della giacenza negativa. Questa /copy che si chiama £GNF è stata utilizzata nelle exit e nei programmi personalizzati coinvolti nei processi applicativi descritti in precedenza.
### NOTA BENE
La /copy £GNF viene distribuita come routine standard "as is", come strumento per effettuare i controlli sopra descritti, ma non è utilizzata nelle applicazioni standard.
La sua fornitura e distribuzione, ha come scopo fornire all'installatore uno strumento standard da utilizzare a livello di interfaccia utente per il suddetto controllo, ed è a carico dell'installatore curare l'interfaccia interattiva in caso di giacenza negativa.

 ## Dati Input
  * DS GMTRAN
  * Quantità giacente prima del movimento richiesto
 ## Dati Output
  * Esito Controllo
   ** La decodifica è stata raccolta in messaggi nel file MSGGM
   *** GM00042 non si creano negativi :  ok
   *** GM00043 si creano negativi, ma l'utente è autorizzato :  si può proseguire
   *** GM00044 si creano negativi e l'utente NON è autorizzato :  funzione bloccata
 ## Funzioni / Metodi
  * SING - Singolo articolo
  * INIZ - Inizializzazione gruppo articoli (utile ad esempio per scarico da impegni)
  * RIGA - Transazione articolo
  * FINE - Fine elaborazione
    ** Blanks
    ** PRES  presentazione movimenti che generano negativi

# Classe Autorizzazione
Attraverso la classe autorizzazione ABILITA funzione GMGNF0, è possibile specificare l'abilitazione di un utente a generare giacenze negative.
Viene assunto per default che un utente non possa generare negativi, quindi non è autorizzato.
 :  : INI Gestione autorizzazione ABILITA funzione GMGNF0
 :  : CMD CALL PGM(B£AUA0G) PARM('ABILITA' '' 'GMGNF0')
 :  : FIN

# Eccezioni di controllo - exit utente
La funzione prevede la possibilità di gestire eccezioni utente attraverso la exit GMGNF0_U. Se presente l'oggetto programma, viene richiamato per ogni controllo, riceve la DS GMTRAN contenente la richiesta di transazione, restituisce un return code '1'=attivo / '0'=disattivo in modo da attivare/disattivare il controllo sulla singola transazione.
In questo modo è possibile ad esempio escludere dal controllo determinate aree di magazzino, o determinati articoli che è opportuno non controllare.

# Componenti
## Programmi
 :  : DEC T(MB) P(GMSRC) K(GMGNF0) I(-)
 :  : DEC T(MB) P(GMSRC) K(GMGNF0_U) I(-)

## Tabelle
 :  : DEC T(TA) P(B£P) K(ABILITA) I(Elemento B£P)

## /COPY
 :  : DEC T(MB) P(QILEGEN) K(£GNF) I(-)

## Funzione di test
 :  : INI Richiamo TSTGNF
 :  : CMD CALL PGM(TSTGNF)
 :  : FIN
