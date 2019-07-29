## Esempio apertura membro
 :  : I.XML
<?xml version="1.0" encoding="UTF-8"?>
<Base Testo="X1CRU  - ">
 <Service Titolo1="" Titolo2="" Funzione="F(EDT;*EDTLET;LET) 1(MB;SCP_SCH;....)"
  Servizio="JATRE_29C" TSep="." DSep="," IdFun="1228110434145" NumSes="848336"/>
   <Header>
 <Livello Caratteristiche="A01"/>
 </Header>
   <Key>
     <K1 Tipo="MB" Parametro="SCP_SCH" Codice="X1CRU" Testo="" Obb="3" Mod="1"/>
     <K2 Tipo="OJ" Parametro="*LIB" Codice="SME_WU3" Testo="Sviluppo WebUP 3" Obb=" " Mod="2"/>
   </Key>
   <Setup>
     <Program>
       <EDT Tipo="FIX" Lung="100" NoMod="1" Control="EDT_SCH"/>
     </Program>
   </Setup>
   <Contenuto>
   <![CDATA[* ==============================================================<br>
   * MODIFICHE Ril.  T Au Descrizione<br>
   * gg/mm/aa  nn.mm i xx Breve descrizione<br>
   *===============================================================<br>
   * 07/10/18  V5R1  i BS Aggiunta sottoscheda analisi componenti<br>
   * 08/10/18  V5R1  i BS Rollback modifica precedente<br>
   *===============================================================<br>
   //X1CRU.<br>
   <br>
    :  : S.EXD.LAY Menu="F(TRE;LOA12_SE;MNU.TRE) 1(;;) 2(;;) P(MN(WEDEMO_001))"
    :  : G.STY Name="A01" FontSize="12" FontItalic="Yes"<br>
    :  : G.STY Name="A02" FontSize="10" FontBold="Yes" Align="center"<br>
    :  : G.STY Name="A03" Align="center"<br>
    :  : G.STY Name="A04" FontColor="R153G000B000" FontBold="Yes" Align="center"<br>
  <br>
  <br>
   :  : I.IF.OPE F1(&AM.DV) OP(NE) F2(C)<br>
       :  : G.SEZ Pos(1)<br>
         :  : G.SUB.SCH Flat="Yes" Tit="*NONE"<br>
         :  : D.SCH Nam(Presentazione)<br>
   :  : I.IF.ELSE<br>
       :  : G.SEZ Pos(1) Dim(20%)<br>
         :  : G.SUB.SCH Flat="Yes" Tit="*NONE"<br>
         :  : D.SCH Nam(Presentazione)<br>
   :  : I.IF.END<br>
       :  : G.SEZ Pos(2)<br>
         :  : G.SUB.SCH Tit="*NONE"<br>
         :  : D.SCH Nam(IMLCOMP) P(TEST([WEBUP.TESTMODE][WEBUP.SNAPSHOT]))<br>
   :  : I.SCH.END<br>
  <br>
  ]]>
   </Contenuto>
     <Messaggi>
       <Esito Stato="OK"/>
     </Messaggi>
   </Base>
 :  : I.XML.END
