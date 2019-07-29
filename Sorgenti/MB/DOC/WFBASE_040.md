# Obiettivo

Dichiarare sotto script (invece che scrivere programmi) dei check da fare affinchè un avanzamento possa essere dichiarato.

# Tipologie di check

I check possono essere : 
* Generici, cioè eseguiti SEMPRE prima dell'avanzamento;
* Di scelta, cioè associati a una scelta utente WHN/OTH ed eseguiti solo se l'utente effettua quella scelta.

I check di scelta, in particolare, nascono con l'obiettivo di risolvere il tema dell'obbligatorietà di campi da non controllare in caso si scelgano strade di tipo "annullamento".
Quando, ad esempio, ho una modifica di oggetto seguita da una scelta di tipo Prosegui/Annulla :  se scelgo Prosegui non devo potere avanzare se non ho inserito i dati necessari, mentre se scelgo Annulla non voglio introdurre vincoli non necessari.

Tipologia di controlli, rappresentati dalle diverse istruzioni che cominciano con CHK : 
* Espressione con variabili relative a oggetti del workflow (es. &AWF.OMS%I/10<>CLASSE1) - istruzione CHK.CON.
* Chiamata a un programma specifico, passando un parametro - istruzione CHK.PGM.


# Un esempio

Si consideri questo script, che definisce una transizione : 

 :  : PAR F(04)
 :  : TRA Name="005" Des="Modifica articolo" Sst="1"  ecc...
   :  : DIC.FUN Fun="A(WFAZB£_02;GES;02) 3(AR;;&AWF.OMS)" Des="Avanza"
   :  : FROM
     :  : LUO Name="L01" Tip="I" Des="Partenza"
   :  : TO Tip="C"
     :  : WHN Con="1" Des="Prosegui"
       :  : LUO Name="005"
       :  : CHK.CON Chk="&AWF.OMS%I/10<>" Msg="X100001" Fil=" MSGX1"
     :  : OTH Des="Annulla"
       :  : LUO Name="025"


Esso rappresenta il passo di modifica di un articolo, alla fine della quale si sceglie (tramite scelta standard) se avanzare o annullare il tutto.
Solo sulla scelta "Prosegui" è stato aggiunto un check (la classe materiale deve essere valorizzata), quindi : 
* Se all'esecuzione, dopo la modifica articolo, scegliamo "Prosegui" la classe materiale deve essere compilata, altrimenti il workflow non avanza (restituendo il messaggio MSGX1/X100001).
* Se invece scegliamo "Annulla" si avanza senza particolari controlli.

# Osservazioni e limitazioni

Si noti bene che : 
* I check sono associabili solo a impegni eseguiti da utente, non a impegni ad esecuzione automatica.
* I check di scelta sono associabili solo a scelte standard (attributo Sst valorizzato), ovvero a scelte effettuate dall'utente tramite G08. Se la scelta è automatica, infatti, (e.g. condizioni su OAV dell'oggetto master) le condizioni stesse sono già una forma di check.
* La chiamata a WFA in CHK assume che sto lavorando sull'ordine con cui sono entrato nell'attività. Se una DIC.FUN chiamasse la £WFA con lo stesso livello di chiamata su ordini diversi (es. sottoworkflow) darebbe problemi.


