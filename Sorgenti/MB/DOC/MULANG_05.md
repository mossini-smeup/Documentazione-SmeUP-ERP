# Descrizione


### Unary

### Multiple

### Atomic

### Compound

### Contigous

# Operazioni dati bufferizzati


|  Nam="Tipo dati" |
| 
| .COL Txt="Oggetto" LunAut="1" A="L" |
| ---|----|
| 
| .COL Txt="Metodo" LunAut="1" A="L" |
| 
| .COL Txt="Parametro" LunAut="1" A="L" |
| 
| .COL Txt="Supporto" Ogg="V2SI/NO" A="L" |
| 
| .COL Txt="Varying" Ogg="V2SI/NO" A="L" |
| 
| .COL Txt="Tipo Buffer" LunAut="1" A="L" |
| Element|move/movel|Element|1|1|element| |
| Element|move/movel|Special|1|1|element| |
| Element|move/movel|Filler|1|1|element| |
| Element|move/movel|List|||| |
| Element|movea|Element|||| |
| Element|movea|List|1||contiguo |
|  |
| List|move/movel|Element|1|1|element| |
| List|move/movel|Special|1|1|element| |
| List|move/movel|Filler|1|1|element| |
| List|move/movel|List|1|1|element| |
| List|movea|Element|1||contiguo |
| List|movea|List|1||contiguo |
| List|movea|Special|1||element |
| List|movea|Filler|1||element |
|  |
| 


# Gestione valori di default
I valori di default vengono generalemnte indicati tramite attributi dell'annotazione java @DataDef _value_ oppure _values_ se il dato è multiplo

_value_ può assumere i seguenti valori : 
* numerico se campo numerico
* alfanumerico se campo alfanumerico
* valore speciale del tipo *BLANK, *HIVAL, *ZEROS, ...

i campi alfanumerici non vogliono apici a racchiuderne il valore, salvo nel caso in cui si voglia indicare una stringa con valore coincidente con speciale, esempio : 
- '*BLANKS', '*HIVAL'

nel caso il campo sia multiplo, il valore dell'attributo _value_ verrà assegnato a tutti gli elementi del campo multiplo; i valori dell'attributo _values_ verranno invece assegnati allo specifico indice del campo multiplo

per il dettaglio dei valori speciali si rimanda alla sezione successiva


# Valori speciali

// TODO
