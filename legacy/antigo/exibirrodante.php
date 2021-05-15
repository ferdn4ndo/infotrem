<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />
<title>Exibir Material Rodante</title>
<link href="estilo.css" rel="stylesheet" type="text/css" />
</head>
<body><?
//Includes
include "includeslocalhost.php"; //Conecta ao banco de dados

//Pega os dados da URL
$CodRodante = AntiInjection($_GET["Cod"]);

//Pega a categoria
$sqlcat = "SELECT Categoria FROM tblRodante WHERE CodReg = " . $CodRodante . ";";
$rescat = mysql_query($sqlcat);
while ($rowcat = mysql_fetch_array($rescat)) {
	$CodCategoria = $rowcat['Categoria'];
}

//Pega os demais dados, de acordo com a categoria
//Prepara a string e o SQL
if ($CodCategoria == 1) { //Locomotivas
	$Nome = "Locomotivas";
	$sql = "SELECT tblRodante.*, tblModelos.CodModelo, tblModLoco.ModeloLoco, tblFabricantes.NomeFabricante, tblTracao.Tracao, tblFerrovias.Nome AS Ferrovia1, tblFerrovias2.Nome AS Ferrovia2, tblLocais.Nome AS Local, tblLocais.Sigla, tblEstadoRodante.Estado FROM ((((((((tblRodante INNER JOIN tblModelos ON tblRodante.CodModelo = tblModelos.CodModelo) INNER JOIN tblModLoco ON tblModelos.CodModLoco = tblModLoco.CodModLoco) INNER JOIN tblFerrovias ON tblRodante.FerroviaAtual = tblFerrovias.CodFerrovia) INNER JOIN tblFerrovias tblFerrovias2 ON tblRodante.FerroviaOrigem = tblFerrovias2.CodFerrovia) INNER JOIN tblLocais ON tblRodante.UltimoLocal = tblLocais.CodLocal) INNER JOIN tblEstadoRodante ON tblRodante.Estado = tblEstadoRodante.CodEstado) INNER JOIN tblTracao ON tblModLoco.TracaoLoco = tblTracao.CodTracao) INNER JOIN tblFabricantes ON tblModLoco.FabricanteLoco = tblFabricantes.CodFabricante) WHERE tblRodante.CodReg = " . $CodRodante . ";";
} elseif ($CodCategoria == 2) { //Vagões
	$Nome = "Vag&otilde;es";
	$sql = "SELECT tblRodante.*, tblModelos.CodTipoVag, tblModelos.CodPesoVag, tblFerrovias.Nome AS Ferrovia1, tblFerrovias2.Nome AS Ferrovia2, tblLocais.Nome AS Local, tblLocais.Sigla, tblEstadoRodante.Estado, tblTipoVags.TipoVag, tblPesoVags.LetraPesoVag, tblFaixasNumericas.NumeroInicial, tblFaixasNumericas.NumeroFinal, tblFaixasNumericas.Descricao AS FaixaNumerica, tblTipoVags.Descricao AS TipoVagDesc, tblPesoVags.PesoVag FROM ((((((((tblRodante INNER JOIN tblModelos ON tblRodante.CodModelo = tblModelos.CodModelo) INNER JOIN tblFerrovias ON tblRodante.FerroviaAtual = tblFerrovias.CodFerrovia) INNER JOIN tblFerrovias tblFerrovias2 ON tblRodante.FerroviaOrigem = tblFerrovias2.CodFerrovia) INNER JOIN tblLocais ON tblRodante.UltimoLocal = tblLocais.CodLocal) INNER JOIN tblEstadoRodante ON tblRodante.Estado = tblEstadoRodante.CodEstado) INNER JOIN tblTipoVags ON tblModelos.CodTipoVag = tblTipoVags.CodTipoVag) INNER JOIN tblPesoVags ON tblModelos.CodPesoVag = tblPesoVags.CodPesoVag) INNER JOIN tblFaixasNumericas ON tblFaixasNumericas.NumeroInicial <= tblRodante.Numero AND tblFaixasNumericas.NumeroFinal >= tblRodante.Numero) WHERE tblRodante.CodReg = " . $CodRodante . ";";
} elseif ($CodCategoria == 3) { //Carros
	$Nome = "Carros";
	$sql = "SELECT tblRodante.*, tblModelos.CodTipoCarro, tblModelos.CodMatCarro, tblFerrovias.Nome AS Ferrovia1, tblFerrovias2.Nome AS Ferrovia2, tblLocais.Nome AS Local, tblLocais.Sigla, tblEstadoRodante.Estado, tblTipoCarro.LetraTipoCarro, tblTipoCarro.TipoCarro, tblMatCarro.LetraMatCarro, tblMatCarro.MatCarro FROM (((((((tblRodante INNER JOIN tblModelos ON tblRodante.CodModelo = tblModelos.CodModelo) INNER JOIN tblFerrovias ON tblRodante.FerroviaAtual = tblFerrovias.CodFerrovia) INNER JOIN tblFerrovias tblFerrovias2 ON tblRodante.FerroviaOrigem = tblFerrovias2.CodFerrovia) INNER JOIN tblLocais ON tblRodante.UltimoLocal = tblLocais.CodLocal) INNER JOIN tblEstadoRodante ON tblRodante.Estado = tblEstadoRodante.CodEstado) INNER JOIN tblTipoCarro ON tblModelos.CodTipoCarro = tblTipoCarro.CodTipoCarro) INNER JOIN tblMatCarro ON tblModelos.CodMatCarro = tblMatCarro.CodMatCarro) WHERE tblRodante.CodReg = " . $CodRodante . ";";
} elseif ($CodCategoria == 4) { //Autos de Linha
	$Nome = "Autos de Linha";
	$sql = "SELECT tblRodante.*, tblTipoAuto.TipoAuto, tblTipoAuto.Descricao AS NomeTipoAuto, tblFerrovias.Nome AS Ferrovia1, tblFerrovias2.Nome AS Ferrovia2, tblLocais.Sigla, tblLocais.Nome AS Local, tblEstadoRodante.Estado FROM ((((((tblRodante INNER JOIN tblModelos ON tblRodante.CodModelo = tblModelos.CodModelo) INNER JOIN tblTipoAuto ON tblModelos.CodTipoAuto = tblTipoAuto.CodTipoAuto) INNER JOIN tblFerrovias ON tblRodante.FerroviaAtual = tblFerrovias.CodFerrovia) INNER JOIN tblFerrovias tblFerrovias2 ON tblRodante.FerroviaOrigem = tblFerrovias2.CodFerrovia) INNER JOIN tblLocais ON tblRodante.UltimoLocal = tblLocais.CodLocal) INNER JOIN tblEstadoRodante ON tblRodante.Estado = tblEstadoRodante.CodEstado) WHERE tblRodante.CodReg = " . $CodRodante . ";";
} elseif ($CodCategoria == 5) { //Automotrizes / Trens-Unidade
        $Nome = "Automotrizes / Trens-Unidade";
        $sql = "SELECT tblRodante.*, tblTipoMotrizes.TipoMotriz, tblTipoMotrizes.Descricao AS NomeTipoMotriz, tblFerrovias.Nome AS Ferrovia1, tblFerrovias2.Nome AS Ferrovia2, tblLocais.Sigla, tblLocais.Nome AS Local, tblEstadoRodante.Estado FROM ((((((tblRodante INNER JOIN tblModelos ON tblRodante.CodModelo = tblModelos.CodModelo) INNER JOIN tblTipoMotrizes ON tblModelos.CodTipoMotriz = tblTipoMotrizes.CodTipoMotriz) INNER JOIN tblFerrovias ON tblRodante.FerroviaAtual = tblFerrovias.CodFerrovia) INNER JOIN tblFerrovias tblFerrovias2 ON tblRodante.FerroviaOrigem = tblFerrovias2.CodFerrovia) INNER JOIN tblLocais ON tblRodante.UltimoLocal = tblLocais.CodLocal) INNER JOIN tblEstadoRodante ON tblRodante.Estado = tblEstadoRodante.CodEstado) WHERE tblRodante.CodReg = " . $CodRodante . ";";
}


//Executa o comando
$res = mysql_query($sql);
while ($row = mysql_fetch_array($res)) {
	//Prepara os dados
	$CodCategoria = $row['Categoria'];
	if ($CodCategoria==1) {
		$Modelo = $row['ModeloLoco'];
		$Fabricante = $row['NomeFabricante'];
		$Tracao = $row['Tracao'];
	} elseif ($CodCategoria==2) {
		$Modelo = $row['TipoVag'] . $row['LetraPesoVag'];
		$TipoVag = $row['TipoVag'];
		$TipoVagDesc = $row['TipoVagDesc'];
		$PesoVag = $row['LetraPesoVag'];
		$PesoVagDesc = $row['PesoVag'];
		//Checa a bitola
		if ($PesoVag < "I") {
			$Bitola = "1,00 m";
		} else {
			$Bitola = "1,60 m";
		}
	} elseif ($CodCategoria==3) {
		$Modelo = $row['LetraTipoCarro'] . $row['LetraMatCarro'];
		$TipoCarro = $row['LetraTipoCarro'];
		$TipoCarroDesc = $row['TipoCarro'];
		$MatCarro = $row['LetraMatCarro'];
		$MatCarroDesc = $row['MatCarro'];
	} elseif ($CodCategoria==4) {
		$Modelo = $row['TipoAuto'];
		$NomeModelo = $row['NomeTipoAuto'];
	} elseif ($CodCategoria==5) {
		$Modelo = $row['TipoMotriz'];
		$NomeModelo = $row['NomeTipoMotriz'];
	}
	$Regional = $row['Regional'];
	$Numero = $row['Numero'];
	$FerroviaOrigem = $row['Ferrovia2'];
	$FerroviaAtual = $row['Ferrovia1'];
	$UltimoLocal = $row['Local'] . " (" . $row['Sigla'] . ")";
	$UltimaData = mostraData($row['UltimaData']);
	$Estado = $row['Estado'];
	$Detalhes = $row['Detalhes'];
}
//Pega a regional
if(($Regional!="")&&($Regional!=0)){
	$consulta = "SELECT * FROM tblRegional WHERE CodLetraRegional = " . $Regional . ";";
	$executa = mysql_query($consulta);
	while ($linha = mysql_fetch_array($executa)) {
		$NomeRegional = $linha['LetraRegional'] . " - "  . $linha['Regional'];
	}
} else {
	$NomeRegional = "-";
}
?><table width="100%" align="center"><tr height="100%"><td align="center" valign="center" height="100%">
<form id="form1" name="form1" method="post" action="#"><div align="center">
  <table width="500" border="1" cellspacing="0" cellpadding="0">
  <tr>
      <td height="23" colspan="2" class="headertabela"><div align="center" class="header">Exibir Material Rodante</div></td>
      </tr>
      <tr>
    <td width="149" class="headertabela"><div align="right">C&oacute;digo:</div></td>
      <td width="345" bgcolor="#FFFFFF"><? echo $CodRodante; ?></td>
    </tr>
  	<tr>
    <td width="149" class="headertabela"><div align="right">Categoria:</div></td>
      <td width="345" bgcolor="#FFFFFF"><? echo $Nome; ?></td>
    </tr>
    <tr>
      <td width="149" class="headertabela"><div align="right">Modelo:</div></td>
      <td width="345" bgcolor="#FFFFFF"><? echo $Modelo; ?></td>
    </tr>
    <? if ($CodCategoria==1) { ?>
    <tr>
      <td width="149" class="headertabela"><div align="right">Fabricante:</div></td>
      <td width="345" bgcolor="#FFFFFF"><? echo $Fabricante; ?></td>
    </tr>
    <tr>
      <td width="149" class="headertabela"><div align="right">Tra&ccedil;&atilde;o:</div></td>
      <td width="345" bgcolor="#FFFFFF"><? echo $Tracao; ?></td>
    </tr>
	<? } elseif ($CodCategoria==2) { ?>
    <tr>
      <td width="149" class="headertabela"><div align="right">Tipo de Vag&atilde;o:</div></td>
      <td width="345" bgcolor="#FFFFFF"><? echo $TipoVag . " - " . $TipoVagDesc; ?></td>
    </tr>
    <tr>
      <td width="149" class="headertabela"><div align="right">Peso Bruto M&aacute;x:</div></td>
      <td width="345" bgcolor="#FFFFFF"><? echo $PesoVag . " - " . $PesoVagDesc . " tons."; ?></td>
    </tr>
    <tr>
      <td width="149" class="headertabela"><div align="right">Bitola (SIGO):</div></td>
      <td width="345" bgcolor="#FFFFFF"><? echo $Bitola; ?></td>
    </tr>
	<? } elseif ($CodCategoria==3) { ?>
    <tr>
      <td width="149" class="headertabela"><div align="right">Tipo de Carro:</div></td>
      <td width="345" bgcolor="#FFFFFF"><? echo $TipoCarro . " - " . $TipoCarroDesc; ?></td>
    </tr>
    <tr>
      <td width="149" class="headertabela"><div align="right">Material:</div></td>
      <td width="345" bgcolor="#FFFFFF"><? echo $MatCarro . " - " . $MatCarroDesc; ?></td>
    </tr>
	<? } elseif ($CodCategoria==4) { ?>
    <tr>
      <td width="149" class="headertabela"><div align="right">Descri&ccedil;&atilde;o:</div></td>
      <td width="345" bgcolor="#FFFFFF"><? echo $NomeModelo; ?></td>
    </tr>
	<? } elseif ($CodCategoria==5) { ?>
    <tr>
      <td width="149" class="headertabela"><div align="right">Descri&ccedil;&atilde;o:</div></td>
      <td width="345" bgcolor="#FFFFFF"><? echo $NomeModelo; ?></td>
    </tr>
	<? } ?>
    <tr>
      <td class="headertabela"><div align="right">N&uacute;mero:</div></td>
      <td bgcolor="#FFFFFF"><? echo $Numero . "-" . CalculaDV($Numero); ?></td>
    </tr>
    <tr>
      <td class="headertabela"><div align="right">Regional:</div></td>
      <td bgcolor="#FFFFFF"><? echo $NomeRegional; ?></td>
    </tr>
    <tr>
      <td class="headertabela"><div align="right">Ferrovia de Origem:</div></td>
      <td bgcolor="#FFFFFF"><? echo $FerroviaOrigem; ?></td>
    </tr>
    <tr>
      <td class="headertabela"><div align="right">Ferrovia Atual:</div></td>
      <td bgcolor="#FFFFFF"><? echo $FerroviaAtual; ?></td>
    </tr>
    <tr>
      <td height="23" class="headertabela"><div align="right">&Uacute;ltimo Local:</div></td>
      <td bgcolor="#FFFFFF"><? echo $UltimoLocal; ?></td>
    </tr>
    <tr>
      <td height="23" class="headertabela"><div align="right">&Uacute;ltima Data:</div></td>
      <td bgcolor="#FFFFFF"><? echo $UltimaData; ?></td>
    </tr>
    <tr>
      <td height="23" class="headertabela"><div align="right">Estado:</div></td>
      <td bgcolor="#FFFFFF"><? echo $Estado; ?></td>
    </tr>
    <tr>
      <td height="23" class="headertabela"><div align="right">Detalhes:</div></td>
      <td bgcolor="#FFFFFF"><? echo $Detalhes; ?></td>
    </tr>
    <tr>
      <td height="23" colspan="2" class="headertabela"><div align="center">
        <input type="button" name="button" id="button" value="Voltar" onclick="javascript:history.back();" />
      </div></td>
      </tr>
  </table>
  </div>
</form></td></tr></table>
</body>
</html>
