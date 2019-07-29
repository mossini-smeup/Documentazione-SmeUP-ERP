# QUOTA INDEDUCIBILE

Per alcune tipologie di cespiti, per la linea fiscale la quota ammortizzabile deducibile non è interamente riconosciuta. Per tenere conto di questo aspetto è possibile indicare a livello di categoria, o di piano, la % di ammortamento che dovrà essere scorportata dalla quota lorda. Per far si che tali % vengano prese in considerazione è necessario che sulla tabella della linea venga indicata la causale di indeducibilità, e che ci sia corrispondenza fra tale causale e indicata sul piano, se % viene indicata sul piano invece che nella tabella della categoria.
L'effetto sarà che verranno applicati due movimenti ammortamento, uno per la parte indeducibile,
ed uno per la parte deducibile.

 :  : DEC T(ST) P() K(A5A)
 :  : DEC T(ST) P() K(A5C&AZ)

# QUOTA NON AMMORTIZZABILE

Per alcune tipologie di cespiti, invece, è previsto di poter ammortizzare fino ad una certa quota massima di capitale. In questo caso tale quota va indicata sulla tabella della categoria, e per far si che venga applicata, dovrà essere indicata anche la relativa causale nella tabella della linea.

 :  : DEC T(ST) P() K(A5A)
 :  : DEC T(ST) P() K(A5C&AZ)

# PROBLEMATICHE RELATIVE ALL'ATTIVAZIONE

In fase di attivazione di questi automatismi, una problematica che si può riscontrare è dovuta al fatto che sullo storico non risultino le relative quote. Per ottenere i dati storici sarebbe da eseguire un pgm di riallineamento che adegui il passato. A standard non è ancora stato previsto un pgm di questo tipo.

