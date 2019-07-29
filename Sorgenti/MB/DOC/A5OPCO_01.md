
## Metodo di costruzione di registrazione dato un movimento
_2_N.B. : 
L'operazione descritta va ripetuta per tutti i tipi di movimenti di cui si vuole ottenere automaticamente la scrittura di contabilità.

Il file utilizzato è >C£CONR0F e sarà necessario creare un programma specifico di gestione.
Condizioni importanti : 

- Azienda
- Linea di ammortamento
- Categoria cespite
- Tipo movimento
- Cespite

Si hanno a disposizione due campi in >C£CONR : 

- Campo Codice 1 con struttura XXYYLLC, dove : 
-- XX  Tipo Movimento
-- YY  Azienda
-- LL  Linea ammortamento
-- C   Tipo codice 2  (1=Cespite 2=Categoria 3=Default '**')

- Campo Codice 2
Può contenere il codice cespite oppure la categoria contabile e dipende dal valore (1-2-3) inserito nel settimo carattere del campo sopra descritto.
I codici dei parametri sono fissi ed identificano il conto dare/avere, il tipo registrazione e la causale contabile.


Ora bisogna determinare la sequenza di lettura dei record : 
1. XXYYLL1  Specifico con cespite
2. XXYYLL2       "     "  categoria
3. XXYYLL3       "     "  '**'
4. XXYY**1       "     "  cespite
5. XXYY**2       "     "  categoria
6. XXYY**3       "     "  '**'
7. XX**LL   (1) (2) (3)
8. XX****   (1) (2) (3)

I parametri, che sono standard e che il programma di gestione si preoccuperà di creare se mancanti, sono definiti nell'elemento '£A5' della tabella >C£E e nel sottosettore >B£N/>£5.

## Elementi tabella gestiti : 

| **Sottosettori tabelle** |
| ---|
| B£N£5                   Contabilizzazione cespiti |
| 



| **Tabella**               | **Elemento**                     | **Descrizione** |
| ---|----|----|
| C£E                     | £A5                            | Parametri per contab. cespiti |
| B£G                     | £A5                            | Gestione contab. cespiti |
| B£N£5                   | A05                            | Tipo registrazione |
| B£N£5                   | A10                            | Causale registrazione |
| B£N£5                   | A15                            | Conto dare |
| B£N£5                   | A20 	                          | Conto avere |
| 


Per il momento è prevista una sola registrazione (1 dare + 1 avere) e una sola riga di analitica (in futuro, se necessario, si potranno utilizzare i parametri multipli con le % nel numero).
Le**registrazioni gestite** sono : 

- **Ammortamento base**
Comprende i tipi movimento : 
-- AO = Ammortamento ordinario
-- AR = Ammortamento ritardato
-- AC = Ammortamento accelerato
-- AA = Ammortamento anticipato

- **Ammortamento finanziario**
Comprende i tipi movimento : 
-- AF = Ammortamento finanziario

- **Plusvalenza**
Comprende i tipi movimento : 
-- PV = Plusvalenza

- **Minusvalenza**
Comprende i tipi movimento : 
-- MV = Minusvalenza


## Metodo di costruzione analitica di una riga di registrazione
Il programma di contabilizzazione £A5M controlla se il conto di contabilizzazione è di analitica e, in caso affermativo, prova a reperire gli oggetti della relativa struttura dai dati anagrafici del cespite, attribuendoli poi alla riga di registrazione.

