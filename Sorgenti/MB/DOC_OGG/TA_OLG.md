# OLG - Orari di lavoro giornalieri
 :  : DEC T(ST) K(OLG)
## OBIETTIVO
Codificare gli orari di lavoro adottati in azienda, in modo da rendere più semplice l'impostazione del calendario di
disponibilità delle risorse.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM __Codice__
 :  : FLD T$DESC __Descrizione__
 :  : FLD HI,1   __Ore inizio__
Permettono di definire fino ad un massimo di 6 intervalli lavorativi per ogni giorno.
Il formato di questo campo è HH,MM (ore,minuti) o HH,CC (ore,centesimi) in conformità a quanto impostato in
tabella di personalizzazione B£2 nel campo 'U.Mis.fraz.tempo C/S'.
Per le giornate non lavorative tutti questi campi dovranno rimanere vuoti.
Per le giornate con orario continuato, su tre turni, si dovrà compilare solo la prima riga con 0 - 24.
 :  : FLD HF,1.HI,1  Ore fine
 :  : FLD HI,2.HI,1  Ore inizio
 :  : FLD HF,2.HI,1  Ore fine
 :  : FLD HI,3.HI,1  Ore inizio
 :  : FLD HF,3.HI,1  Ore fine
 :  : FLD HI,4.HI,1  Ore inizio
 :  : FLD HF,4.HI,1  Ore fine
 :  : FLD HI,5.HI,1  Ore inizio
 :  : FLD HF,5.HI,1  Ore fine
 :  : FLD HI,6.HI,1  Ore inizio
 :  : FLD HF,6.HI,1  Ore fine
 :  : FLD T$OLGA __Orario in Spostamento__
Nel caso l'orario sia festivo, tramite questo campo è possibile fissare un range di giorni al quale
saltare, quando si sta eseguendo la ricerca del primo giorno lavorativo valido.
