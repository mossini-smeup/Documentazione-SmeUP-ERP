# CCC  -  CADENZA CONSEGNE
 :  : DEC T(ST) K(CCC)
## CASO 1
Tipo consegna  : 'G'  Consegna mensile uguale a 0
Consegna settimanale diversa da 0
Suddivide la quantità mensile nei giorni impostati nelle consegne settimanali.
_9_Esempio :       Consegna settimanale =   X--X---
Suddivide la quantità in tutti i Lunedì (G.1) e Giovedì (G.4) del mese.
## CASO 2
Tipo consegna  : 'G'  Consegna mensile diversa da 0
Consegna settimanale uguale a 0
Cadenza con giorni fissi.
Suddivide la quantità mensile nei giorni impostati nelle consegne mensili.
_9_Esempio :       Consegna mensile =  1 ,10, 31
Suddivide la quantità al 1° , 10° e ultimo (da 31 arretra) del mese.
## CASO 3
Tipo consegna  : 'G'  Consegna mensile diversa da 0
Consegna settimanale diversa da 0
Suddivide la quantità mensile nei giorni della settimana, impostati nelle consegne settimanali relative alle settimane, impostate nei campi consegne mensili.
_9_Esempio :       Consegna mensile     =   1 ,3
Consegna settimanale =   -X--X--
Suddivide la quantità nel 1° e 3° Martedì e Giovedì del mese.
## CASO 4
Tipo consegna  : 'S'  Consegna mensile diversa da 0
Consegna settimanale diversa da 0
Cadenza con giorni fissi.
Suddivide la quantità nelle settimane impostate nella consegna mensile (NB :  la settimana 1 è la prima totalmente appartenente al mese),e , per ciascuna di esse, suddivide la quantità nei giorni impostati nel campo consegne settimanali.
_9_Esempio :       Consegna mensile     =   1 ,3
Consegna settimanale =   -X--X--
Suddivide la quantità in quattro consegne :  il Martedì ed il Venerdì della 1° e 3° settimana del mese.
## CASO 5
Tipo consegna  : '*BLANKS'      Consegna mensile non significativa.
Consegna settimanale diversa da 0
Cadenza con giorni fissi.
Suddivide la quantità (settimanale) nei giorni impostati nel campo consegne settimanali.
_9_Esempio :       Consegna mensile     =   1 ,3
_9_Esempio :       Consegna settimanale =   X----X-
Suddivide la quantità in due consegne :  il Lunedì ed il Sabato della settimana a cui appartiene la data.
