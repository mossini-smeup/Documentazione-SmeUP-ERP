# Xml servizio

## Xml base

<?xml version="1.0" encoding="ISO-8859-1"?>
<Base Testo="generazione xml flusso azioni - ">
 <Service Titolo1="generazione xml flusso azioni" Titolo2="" Funzione="F(FLU;LOSER_22;G53.ES1) 1(;;) 2(;;)" Servizio="LOSER_22"/>
     <Header>
              <Livello Caratteristiche="A01"/>
     </Header>
     <Setup>
          <Program Show="Yes">
                  <FLU>
                    <Setup Show="Yes" Edit="Yes" ExecMode="INT" ShowStep="Yes" Name="99.A01.B01" Desc="Schede degli utenti" Prog="001" Type="STA/DYN" StepFun="F(FBK;XYZ;)" />
                  </FLU>
          </Program>
 </Setup>
         <Oggetto Nome="" Tipo="" Parametro="" Codice="" Testo="Scheda Utente AA" Exec="F(EXD;*SCO;) 1(TA;B£U;AA)" Fld="" Leaf=""/>
         <Oggetto Nome="" Tipo="" Parametro="" Codice="" Testo="Scheda Utente AA" Exec="F(EXD;*SCO;) 1(TA;B£U;BB)" Fld="" Leaf=""/>
         ...
         <Oggetto Nome="" Tipo="" Parametro="" Codice="" Testo="Scheda Utente AA" Exec="F(EXD;*SCO;) 1(TA;B£U;ZZ)" Fld="" Leaf=""/>
</Base>

