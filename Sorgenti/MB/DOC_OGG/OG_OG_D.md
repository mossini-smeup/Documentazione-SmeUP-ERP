Esistono due classificazioni : 

A) Oggetto / Classe

## Codice Oggetto (in TA/*CNTT)
'OG'                               £FUNT1
## Chiave primaria
Codice Classe (elemento *CN/TT)   £FUNK1

B) Oggetto / Classe /Sottoclasse

## Codice Oggetto (in TA/*CNTT)
'OG'                               £FUNT1
Codice Classe (elemento *CN/TT)    £FUNP1

## Chiave primaria
Tipo definito dalla classe        £FUNK1

 Esempio A)
 Tipo  'OG'
 Parametro ' '
 Oggetto 'CN'
 Identifica l'oggetto "Ente"

 Esempio B)
 Tipo  'OG'
 Parametro 'CN'
 Oggetto 'FOR' (elemento della tabella BRE, che è l sottoclasse in cui si sviluppa la classe CN)
 Identifica l'oggetto "Fornitore"

