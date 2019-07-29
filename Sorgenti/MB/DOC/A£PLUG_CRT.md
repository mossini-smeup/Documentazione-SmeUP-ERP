# Regola codifica elementi di tabella
Per ogni applicazione vengono suggeriti i criteri di codifica degli elementi di tabella di competenza di quella applicazione
Ricordiamo che una tabella può appartenere a più applicazioni (es. B£Y)

# Gruppi flag
 :  : DEC T(ST) K(B£Y)
_3_Criterio = Xpp

- X=in funzione del file di riferimento : 
-- A=C5TREG0F
-- B=C5RREG0F
-- C=A5CESP0F
-- D=C5RATE0F
-- E=C5MOAN0F
-- F=GMCOLL0F
-- G=GMTRIM0F
-- H=GMRRIM0F
-- M=GMMOVI0F
-- P=P5TEOP0F
-- Q=P5ATTI0F
-- R=V5RDOC0F
-- T=V5TDOC0F
- pp = progressivo


# Causali Movimentazione
 :  : DEC T(ST) K(GMC)
_3_Criterio = AApp

- AA = area
- pp = Causale movimento.E'un Codice NUMERICO codificato nella tabella GM*CM dove i numeri che vanno da 00 a 49 sono causali di Carico magazzino mentre i restanti (50-99) sono causali di Scarico. Inoltre si considerano simmetrici i numeri 1/51 23/73 e quindi il primo è l'esatto contrario dell'altro(esempio 01=acquisto 51=reso fornitore 03=Versamento esterno 53=Prelievo esterno)


# Tipo giacenza
 :  : DEC T(ST) K(GMQ)
_3_Criterio = pp
 La codifica di questa tabella è così inserita : 

- se il tipo giacenza prevede UN solo oggetto il nome della tabella è il nome dell'oggetto (es. AR=articolo LO=lotto)
- se il tipo giacenza prevede + oggetti il nome della tabella sarà un numero progressivo

Da notare che nel limite del possibile un oggetto è SEMPRE nella stessa posizione (es. Fornitore sempre nel campo 1 Lotto nel 3 etc) questo anche se ci sono campi iniziali liberi

Qui indichiamo le principali scelte fatte
>           Cod1     Cod2     Cod3     Cod4
           CNFOR    OO       LO       CNCLI

