# BR2 - Personalizzazione Anagrafiche Enti
 :  : DEC T(ST) K(BR2)
## OBIETTIVO
Permettere la personalizzazione della anagrafiche degli enti
## CONTENUTO DEI CAMPI
 :  : FLD T$BR2A Gestione scenari
Se valorizzato indica che è gestita la possibilità di attivare (tramite gli appositi campi della tabella BRE)
la gestione a scenari.
 :  : FLD T$BR2B Suff.pgm ges.scenari
Se indicato indentifica il suffisso del pgm con radice "BRBRE0_" per gestire particolarità sulla gestione degli
scenari
 :  : FLD T$BR2C Fmt Dettaglio Esteso
Attiva la gestione del data entry V2 se non è stata attivata una delle seguenti opzioni, che ne implicano l'attivazione automatica : 
- gestione scenari
- gestione storica
- gestione nominativi
Indicando il valore "L" viene attivata la gestione con componenti grafici dell'anagrafica V2.
 :  : FLD T$BR2D Gestione storica
Se valorizzato indica che è gestita la possibilità di attivare (tramite gli appositi campi della tabella BRE)
la gestione dei dati alla data.
 :  : FLD T$BR2E Tipo Ente Nominativo
Se valorizzato indica che è gestita la possibilità di attivare (tramite gli appositi campi della tabella BRE)
la gestione dei nominativi
 :  : FLD T$BR2F Sottosettore Num.
Indica il sottosettore della CRN in cui vengono gestiti in numeratori degli IDOJ dei file BRENTI0F , BRESCO0F e BRTRAN0F (Elementi OG.BRENTI, OG.BRESCO ed OG.BRTRAN). Di default viene assunto BR.
 :  : FLD T$BR2G Gestione Dati Nominativo da soggetti collegati al nominativo
Se viene attivato questo flag è possibile modificare i dati del nominativo anche da un soggetto collegato
mantenendo la congruenza di dati sia a livello di nominativo che di tutti i soggetti collegati al nominativo.
L'unico svantaggio di questa opzione è che la gestione di un ente provoca l'allocazione di tutti i soggetti
collegati tramite il nominativo.
 :  : FLD T$BR2H Controllo Dati Indirizzo
Se viene attivato questo flag è nel data entry V2 viene attivato il controll dei campi indirizzo : 
* CAP
* Codice Comune
* Provincia
* Codice Regione

 :  : FLD T$BR2I Exit Dich. Intento
Se viene attivato questo flag e viene compilata la exit BRIN01D_A, alla fine dell'aggiornamento del
file BRDINT0F verranno aggiornati i campi dell'anagrafica enti E§DVES, E§CDIN, E§DDIN sulla base
dell'ultima dichiarazione inserita
