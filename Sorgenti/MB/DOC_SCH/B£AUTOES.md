# Ridefinire il livello di autorizzazione
Il livello di autorizzazione specificato per una scheda viene ereditato dalle sezioni e dalle sottosezioni in essa contenute.
Attraverso il comando  :   : S.EXD.AUT è comunque possibile ridefinire la funzione e il livello di autorizzazione di una sottoscheda.
Se ad esempio per visualizzare la scheda principale è sufficente un livello di autorizzazione tipo : df

Classe :  LO.EXD
Funzione :  B£AUTO_ES1
Livello :  05

è possibile modificare la funzione e il livello in modo che le sottoschede siano visibili solo ad utenti con un più alto livello di autorizzazione, esempio : 

Classe :  LO.EXD
Funzione :  CNCLI
Livello :  09

# Interpretare l'esempio

## Come interpretare la scheda delle autorizzazioni sull'intera scheda
Nella scheda principale sono definite 4 schede.
In ogni scheda è definita un'etichetta e quattro sottoschede.
Vediamo per ogni scheda (e sottoscheda) quali sono le funzioni e il livello di autorizzazioni richiesti.
## SCH 1
Nel "main" di questo script non è definita l'istruzione S.EXD.AUT, di conseguenza per poter visualizzare questa scheda è necessario avere un record di autorizzazione LO.EXD / B£AUTO_ES1 con livello almeno 05 (cioè 05, 06, 07, 08 o 09).
Questa scheda a sua volta contiene 4 sottoschede, vediamo per ogni sottoscheda le funzioni e il livello richiesti.
### SCH 1-A
In questa sottoscheda non è utilizzata l'istruzione S.EXD.AUT, quindi viene utilizzata la funzione e il livello impostati nel main di questo script. Dato che tale istruzione non è utilizzata nemmeno lì, vengono usati i valori di default (funzione = nome script = B£AUTO_ES1 ; livello = 05)
### SCH 1-B
In questa sottoscheda è utilizzata l'istruzione S.EXD.AUT Lev="07". La funzione di autorizzazione non è specificata, quindi viene assunto il default, cioè il nome dello script. Quindi per poter visualizzare questa sottoscheda è necessario avere un livello di autorizzazione 07 sulla funzione B£AUTO_ES1.
### SCH 1-C
In questa sottoscheda è utilizzata l'istruzione S.EXD.AUT Src="CNCLI". Il livello di autorizzazione non è specificato, quindi viene assunto il default, cioè 05. Quindi per poter visualizzare questa sottoscheda è necessario avere un livello di autorizzazione 05 sulla funzione CNCLI.
### SCH 1-D
In questa sottoscheda è utilizzata l'istruzione S.EXD.AUT Lev="07" Src="CNCLI". Quindi per poter visualizzare questa sottoscheda è necessario avere un livello di autorizzazione 07 sulla funzione CNCLI.
## SCH 2
Nel "main" di questo script è definita l'istruzione S.EXD.AUT Lev="03". La funzione di autorizzazione non è specificata, quindi viene assunta uguale allo script e quindi B£AUTO_ES2. Di conseguenza per poter visualizzare questa scheda è necessario avere un record di autorizzazione LO.EXD / B£AUTO_ES2 con livello almeno 03 (cioè 03, 04, 05, 06, 07, 08 o 09).
Questa scheda a sua volta contiene 4 sottoschede, vediamo per ogni sottoscheda le funzioni e il livello richiesti.
### SCH 2-A
In questa sottoscheda non è utilizzata l'istruzione S.EXD.AUT, quindi viene utilizzata la funzione e il livello impostati nel main di questo script. Quindi per poter visualizzare questa sottoscheda è necessario avere un livello di autorizzazione 03 sulla funzione B£AUTO_ES2.
### SCH 2-B
In questa sottoscheda è utilizzata l'istruzione S.EXD.AUT Lev="07". La funzione di autorizzazione non è specificata, quindi viene assunto il default, cioè il nome dello script. Quindi per poter visualizzare questa sottoscheda è necessario avere un livello di autorizzazione 07 sulla funzione B£AUTO_ES2.
### SCH 2-C
In questa sottoscheda è utilizzata l'istruzione S.EXD.AUT Src="CNCLI". Il livello di autorizzazione non è specificato, quindi viene assunto il default, cioè 05. Quindi per poter visualizzare questa sottoscheda è necessario avere un livello di autorizzazione 05 sulla funzione CNCLI.
### SCH 2-D
In questa sottoscheda è utilizzata l'istruzione S.EXD.AUT Lev="07" Src="CNCLI". Quindi per poter visualizzare questa sottoscheda è necessario avere un livello di autorizzazione 07 sulla funzione CNCLI.
## SCH 3
Nel "main" di questo script è definita l'istruzione S.EXD.AUT Src="AR". Il livello di autorizzazione non è specificato, quindi viene assunto 05. Di conseguenza per poter visualizzare questa scheda è necessario avere un record di autorizzazione LO.EXD / AR con livello almeno 05 (cioè 05, 06, 07, 08 o 09).
Questa scheda a sua volta contiene 4 sottoschede, vediamo per ogni sottoscheda le funzioni e il livello richiesti.
### SCH 3-A
In questa sottoscheda non è utilizzata l'istruzione S.EXD.AUT, quindi viene utilizzata la funzione e il livello impostati nel main di questo script. Quindi per poter visualizzare questa sottoscheda è necessario avere un livello di autorizzazione 05 sulla funzione AR.
### SCH 3-B
In questa sottoscheda è utilizzata l'istruzione S.EXD.AUT Lev="07". La funzione di autorizzazione non è specificata, quindi viene assunto il default, cioè il nome dello script. Quindi per poter visualizzare questa sottoscheda è necessario avere un livello di autorizzazione 07 sulla funzione B£AUTO_ES3.
### SCH 3-C
In questa sottoscheda è utilizzata l'istruzione S.EXD.AUT Src="CNCLI". Il livello di autorizzazione non è specificato, quindi viene assunto il default, cioè 05. Quindi per poter visualizzare questa sottoscheda è necessario avere un livello di autorizzazione 05 sulla funzione CNCLI.
### SCH 3-D
In questa sottoscheda è utilizzata l'istruzione S.EXD.AUT Lev="07" Src="CNCLI". Quindi per poter visualizzare questa sottoscheda è necessario avere un livello di autorizzazione 07 sulla funzione CNCLI.
## SCH 4
Nel "main" di questo script è definita l'istruzione S.EXD.AUT Src="AR" Lev="03". Di conseguenza per poter visualizzare questa scheda è necessario avere un record di autorizzazione LO.EXD / AR con livello almeno 03 (cioè 03, 04, 05, 06, 07, 08 o 09).
Questa scheda a sua volta contiene 4 sottoschede, vediamo per ogni sottoscheda le funzioni e il livello richiesti.
### SCH 4-A
In questa sottoscheda non è utilizzata l'istruzione S.EXD.AUT, quindi viene utilizzata la funzione e il livello impostati nel main di questo script. Quindi per poter visualizzare questa sottoscheda è necessario avere un livello di autorizzazione 03 sulla funzione AR.
### SCH 4-B
In questa sottoscheda è utilizzata l'istruzione S.EXD.AUT Lev="07". La funzione di autorizzazione non è specificata, quindi viene assunto il default, cioè il nome dello script. Quindi per poter visualizzare questa sottoscheda è necessario avere un livello di autorizzazione 07 sulla funzione B£AUTO_ES4.
### SCH 4-C
In questa sottoscheda è utilizzata l'istruzione S.EXD.AUT Src="CNCLI". Il livello di autorizzazione non è specificato, quindi viene assunto il default, cioè 05. Quindi per poter visualizzare questa sottoscheda è necessario avere un livello di autorizzazione 05 sulla funzione CNCLI.
### SCH 4-D
In questa sottoscheda è utilizzata l'istruzione S.EXD.AUT Lev="07" Src="CNCLI". Quindi per poter visualizzare questa sottoscheda è necessario avere un livello di autorizzazione 07 sulla funzione CNCLI.
