# D0A  -  NATURA COSTO
 :  : DEC T(ST) K(D0A)
## OBIETTIVO
Contiene le nature dei costi che permettono di caratterizzare maggiormente gli schemi di costo presenti nel sistema.
Nella gestione dei costi non è necessario utilizzare le nature, esse servono per poter reperire più facilmente aggregazioni di componenti di costo e per renderepiù flessibile la creazione della scheda costo di un oggetto.
## DOVE VIENE UTILIZZATA
La natura costo viene utilizzata nel campo 'Natura costo' della tabella IGI, che è la tabella utilizzata dal modulo D0, per specificare il significato delle componenti di costo di un oggetto, e nel campo 'Natura costo' della tabella D0B dei livelli di costo.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM **Elemento**
La codifica delle nature è libera.
 :  : FLD T$D0AA **Natura collegata**
Se presente, indica che la natura in questione viene aggregata nella sua natura collegata.
_9_Esempio : 
>Natura        Descrizione                  Natura collegata.
ME            Montaggio elettrico          MM
MM            Manodopera montaggio         MD
MD            Costo manodopera
MI            Manodopera indiretta         MD


Supponendo di volere il costo del montaggio elettrico, si dovrà interrogare per natura ME (ovviamente dovranno esistere nella tabella IGI degli elementi con natura costo uguale a ME).
Se invece si volesse conoscere il costo della manodopera, si interrogherà per natura MD e verranno sommati tutti gli elementi che avranno come natura costo o MD o MM o ME o MI (bisogna stare attenti ad eventuali doppi valori).
La catena delle nature collegate può essere lunga a piacere.

