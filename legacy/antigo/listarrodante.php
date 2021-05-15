<?
//Includes
include "includeslocalhost.php";

//Pega o tipo de listagem
$tipo = AntiInjection($_GET['Categoria']);

//Prepara a string e o SQL
if ($tipo == 1) { //Locomotivas
	$Nome = "Locomotivas";
	$sql = "SELECT tblRodante.*, tblModelos.CodModLoco, tblModLoco.ModeloLoco, tblFabricantes.NomeFabricante, tblTracao.Tracao, tblFerrovias.Nome AS Ferrovia1, tblFerrovias2.Nome AS Ferrovia2, tblLocais.Nome AS Local, tblLocais.Sigla, tblEstadoRodante.Estado FROM ((((((((tblRodante INNER JOIN tblModelos ON tblRodante.CodModelo = tblModelos.CodModelo) INNER JOIN tblModLoco ON tblModelos.CodModLoco = tblModLoco.CodModLoco) INNER JOIN tblFabricantes ON tblModLoco.FabricanteLoco = tblFabricantes.CodFabricante) INNER JOIN tblTracao ON tblModLoco.TracaoLoco = tblTracao.CodTracao) INNER JOIN tblFerrovias ON tblRodante.FerroviaAtual = tblFerrovias.CodFerrovia) INNER JOIN tblFerrovias tblFerrovias2 ON tblRodante.FerroviaOrigem = tblFerrovias2.CodFerrovia) INNER JOIN tblLocais ON tblRodante.UltimoLocal = tblLocais.CodLocal) INNER JOIN tblEstadoRodante ON tblRodante.Estado = tblEstadoRodante.CodEstado) WHERE tblRodante.Categoria = 1 ORDER BY tblModLoco.ModeloLoco, tblRodante.Numero;";
} elseif ($tipo == 2) { //Vagões
	$Nome = "Vag&otilde;es";
	$sql = "SELECT tblRodante.*, tblModelos.CodTipoVag, tblModelos.CodPesoVag, tblFerrovias.Nome AS Ferrovia1, tblFerrovias2.Nome AS Ferrovia2, tblLocais.Nome AS Local, tblLocais.Sigla, tblEstadoRodante.Estado, tblTipoVags.TipoVag, tblPesoVags.LetraPesoVag FROM (((((((tblRodante INNER JOIN tblModelos ON tblRodante.CodModelo = tblModelos.CodModelo) INNER JOIN tblFerrovias ON tblRodante.FerroviaAtual = tblFerrovias.CodFerrovia) INNER JOIN tblFerrovias tblFerrovias2 ON tblRodante.FerroviaOrigem = tblFerrovias2.CodFerrovia) INNER JOIN tblLocais ON tblRodante.UltimoLocal = tblLocais.CodLocal) INNER JOIN tblEstadoRodante ON tblRodante.Estado = tblEstadoRodante.CodEstado) INNER JOIN tblTipoVags ON tblModelos.CodTipoVag = tblTipoVags.CodTipoVag) INNER JOIN tblPesoVags ON tblModelos.CodPesoVag = tblPesoVags.CodPesoVag) WHERE tblRodante.Categoria = 2 ORDER BY tblTipoVags.TipoVag, tblPesoVags.LetraPesoVag, tblRodante.Numero;";
} elseif ($tipo == 3) { //Carros
	$Nome = "Carros";
	$sql = "SELECT tblRodante.*, tblModelos.CodTipoCarro, tblModelos.CodMatCarro, tblFerrovias.Nome AS Ferrovia1, tblFerrovias2.Nome AS Ferrovia2, tblLocais.Nome AS Local, tblLocais.Sigla, tblEstadoRodante.Estado, tblTipoCarro.LetraTipoCarro, tblMatCarro.LetraMatCarro FROM (((((((tblRodante INNER JOIN tblModelos ON tblRodante.CodModelo = tblModelos.CodModelo) INNER JOIN tblFerrovias ON tblRodante.FerroviaAtual = tblFerrovias.CodFerrovia) INNER JOIN tblFerrovias tblFerrovias2 ON tblRodante.FerroviaOrigem = tblFerrovias2.CodFerrovia) INNER JOIN tblLocais ON tblRodante.UltimoLocal = tblLocais.CodLocal) INNER JOIN tblEstadoRodante ON tblRodante.Estado = tblEstadoRodante.CodEstado) INNER JOIN tblTipoCarro ON tblModelos.CodTipoCarro = tblTipoCarro.CodTipoCarro) INNER JOIN tblMatCarro ON tblModelos.CodMatCarro = tblMatCarro.CodMatCarro) WHERE tblRodante.Categoria = 3 ORDER BY tblTipoCarro.LetraTipoCarro, tblMatCarro.LetraMatCarro, tblRodante.Numero;";
} elseif ($tipo == 4) { //Autos de Linha
	$Nome = "Autos de Linha";
	$sql = "SELECT tblRodante.*, tblModelos.CodTipoAuto, tblTipoAuto.TipoAuto, tblFerrovias.Nome AS Ferrovia1, tblFerrovias2.Nome AS Ferrovia2, tblLocais.Sigla, tblLocais.Nome AS Local, tblEstadoRodante.Estado FROM ((((((tblRodante INNER JOIN tblModelos ON tblRodante.CodModelo = tblModelos.CodModelo) INNER JOIN tblTipoAuto ON tblModelos.CodTipoAuto = tblTipoAuto.CodTipoAuto) INNER JOIN tblFerrovias ON tblRodante.FerroviaAtual = tblFerrovias.CodFerrovia) INNER JOIN tblFerrovias tblFerrovias2 ON tblRodante.FerroviaOrigem = tblFerrovias2.CodFerrovia) INNER JOIN tblLocais ON tblRodante.UltimoLocal = tblLocais.CodLocal) INNER JOIN tblEstadoRodante ON tblRodante.Estado = tblEstadoRodante.CodEstado) WHERE tblRodante.Categoria = 4 ORDER BY tblTipoAuto.TipoAuto, tblRodante.Numero;";
} elseif ($tipo == 5) { //Automotriz / Trem-unidade
	$Nome = "Automotrizes / Trem-unidade";
	$sql = "SELECT tblRodante.*, tblModelos.CodTipoMotriz, tblTipoMotrizes.TipoMotriz, tblFerrovias.Nome AS Ferrovia1, tblFerrovias2.Nome AS Ferrovia2, tblLocais.Sigla, tblLocais.Nome AS Local, tblEstadoRodante.Estado FROM ((((((tblRodante INNER JOIN tblModelos ON tblRodante.CodModelo = tblModelos.CodModelo) INNER JOIN tblTipoMotrizes ON tblModelos.CodTipoMotriz = tblTipoMotrizes.CodTipoMotriz) INNER JOIN tblFerrovias ON tblRodante.FerroviaAtual = tblFerrovias.CodFerrovia) INNER JOIN tblFerrovias tblFerrovias2 ON tblRodante.FerroviaOrigem = tblFerrovias2.CodFerrovia) INNER JOIN tblLocais ON tblRodante.UltimoLocal = tblLocais.CodLocal) INNER JOIN tblEstadoRodante ON tblRodante.Estado = tblEstadoRodante.CodEstado) WHERE tblRodante.Categoria = 5 ORDER BY tblTipoMotrizes.TipoMotriz, tblRodante.Numero;";
}

//Executa o comando
$res = mysql_query($sql);
?><!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />
<title>Listar <? echo $Nome; ?></title>
<link href="estilo.css" rel="stylesheet" type="text/css" />
</head>
<body>
<table width="100%" align="center"><tr height="100%"><td align="center" valign="center" height="100%">
<form id="form1" name="form1" method="post" action="#"><div align="center">
  <? if ($tipo == 1) { ?>
  <table width="750" border="1" cellspacing="0" cellpadding="0">
  <tr>
    <td colspan="13" class="headertabela"><div align="center">Listar <? echo $Nome; ?></div></td>
      </tr>
    <tr>
      <td width="5%"  class="headertabela"><div align="center">Cód</div></td>
      <td width="6%" bgcolor="#FFFFFF" class="headertabela"><div align="center">Fabricante</div></td>
      <td width="6%" bgcolor="#FFFFFF" class="headertabela"><div align="center">Tra&ccedil;&atilde;o</div></td>
      <td width="6%" bgcolor="#FFFFFF" class="headertabela"><div align="center">Modelo</div></td>
      <td width="7%" bgcolor="#FFFFFF" class="headertabela"><div align="center">N&uacute;mero</div></td>
      <td width="10%" bgcolor="#FFFFFF" class="headertabela"><div align="center">Ferr. Atual</div></td>
      <td width="10%" bgcolor="#FFFFFF" class="headertabela"><div align="center">Ferr. Origem</div></td>
      <td width="18%" bgcolor="#FFFFFF" class="headertabela"><div align="center">&Uacute;ltimo Local</div></td>
      <td width="10%" bgcolor="#FFFFFF" class="headertabela"><div align="center">&Uacute;ltima Data</div></td>
      <td width="14%" bgcolor="#FFFFFF" class="headertabela"><div align="center">Estado</div></td>
      <td width="10%" bgcolor="#FFFFFF" class="headertabela"><div align="center">Detalhes</div></td>
      <td width="5%" bgcolor="#FFFFFF" class="headertabela"><div align="center">E</div></td>
      <td width="5%" bgcolor="#FFFFFF" class="headertabela"><div align="center">X</div></td>
    </tr>
    <?
    //Exibe as linhas encontradas na consulta
    while ($row = mysql_fetch_array($res)) {
		//Exibe as Linhas
		if(strlen($row['Detalhes'])>10){
			$Detalhes = substr($row['Detalhes'],0,10) . "...";
		} else {
			$Detalhes = $row['Detalhes'];
		}
 ?> 
  <tr>
      <td><div align="center"><? echo $row['CodReg'];?></div></td>
      <td><div align="center"><? echo $row['NomeFabricante'];?></div></td>
      <td><div align="center"><? echo $row['Tracao'];?></div></td> 
      <td><div align="center"><? echo $row['ModeloLoco'];?></div></td> 
      <td><div align="center"><a href="exibirrodante.php?Cod=<? echo $row['CodReg'];?>"><? echo $row['Numero'];?></a></div></td> 
     <td><div align="center"><? echo $row['Ferrovia1'];?></div></td> 
     <td><div align="center"><? echo $row['Ferrovia2'];?></div></td>
     <td><div align="center"><? echo $row['Local'] . " (" . $row['Sigla'] . ")";?></div></td>
     <td><div align="center"><? echo mostraData($row['UltimaData']);?></div></td>
     <td><div align="center"><? echo $row['Estado'];?></div></td>
     <td><div align="center"><? echo $Detalhes;?></div></td>
     <td><div align="center"><a href="editarrodante.php?Cod=<? echo $row['CodReg'];?>&Categoria=<? echo $tipo;?>"><img alt="Editar" src="images/edit.png" border="0" width="16" height="16" /></a></div></td>
     <td><div align="center"><a href="excluirrodante.php?Cod=<? echo $row['CodReg'];?>"><img alt="Excluir" src="images/delete.png" border="0" width="16" height="16" /></a></div></td>
  </tr>
  <?  } ?>
  <tr>
      <td height="23" colspan="13" class="headertabela"><div align="center">
        <input type="submit" name="submit" id="submit" value="Atualizar" />
      </div></td>
      </tr>
  </table>
  <? } else { ?>
  <table width="750" border="1" cellspacing="0" cellpadding="0">
  <tr>
    <td colspan="11" class="headertabela"><div align="center">Listar <? echo $Nome; ?></div></td>
      </tr>
    <tr>
      <td width="5%"  class="headertabela"><div align="center">Cód</div></td>
      <td width="6%" bgcolor="#FFFFFF" class="headertabela"><div align="center">Modelo</div></td>
      <td width="7%" bgcolor="#FFFFFF" class="headertabela"><div align="center">N&uacute;mero</div></td>
      <td width="10%" bgcolor="#FFFFFF" class="headertabela"><div align="center">Ferr. Atual</div></td>
      <td width="10%" bgcolor="#FFFFFF" class="headertabela"><div align="center">Ferr. Origem</div></td>
      <td width="18%" bgcolor="#FFFFFF" class="headertabela"><div align="center">&Uacute;ltimo Local</div></td>
      <td width="10%" bgcolor="#FFFFFF" class="headertabela"><div align="center">&Uacute;ltima Data</div></td>
      <td width="14%" bgcolor="#FFFFFF" class="headertabela"><div align="center">Estado</div></td>
      <td width="10%" bgcolor="#FFFFFF" class="headertabela"><div align="center">Detalhes</div></td>
      <td width="5%" bgcolor="#FFFFFF" class="headertabela"><div align="center">E</div></td>
      <td width="5%" bgcolor="#FFFFFF" class="headertabela"><div align="center">X</div></td>
    </tr>
    <?
    //Exibe as linhas encontradas na consulta
    while ($row = mysql_fetch_array($res)) {
		//Prepara os dados
		if ($tipo == 2) { //Vagoes
			$Modelo = $row['TipoVag'] . $row['LetraPesoVag'];
		} elseif ($tipo == 3) { //Carros
			$Modelo = $row['LetraTipoCarro'] . $row['LetraMatCarro'];
		} elseif ($tipo == 4) { //Autos
			$Modelo = $row['TipoAuto'];
		} elseif ($tipo == 5) { //Automotriz/Trem-unidade
			$Modelo = $row['TipoMotriz'];
		}
		
		//Exibe as Linhas
		if(strlen($row['Detalhes'])>10){
			$Detalhes = substr($row['Detalhes'],0,10) . "...";
		} else {
			$Detalhes = $row['Detalhes'];
		}
 ?> 
  <tr>
      <td><div align="center"><? echo $row['CodReg'];?></div></td>
      <td><div align="center"><? echo $Modelo;?></div></td>
      <td><div align="center"><a href="exibirrodante.php?Cod=<? echo $row['CodReg'];?>"><? echo $row['Numero'];?></a></div></td> 
     <td><div align="center"><? echo $row['Ferrovia1'];?></div></td> 
     <td><div align="center"><? echo $row['Ferrovia2'];?></div></td>
     <td><div align="center"><? echo $row['Local'] . " (" . $row['Sigla'] . ")";?></div></td>
     <td><div align="center"><? echo mostraData($row['UltimaData']);?></div></td>
     <td><div align="center"><? echo $row['Estado'];?></div></td>
     <td><div align="center"><? echo $Detalhes;?></div></td>
     <td><div align="center"><a href="editarrodante.php?Cod=<? echo $row['CodReg'];?>&Categoria=<? echo $tipo;?>"><img alt="Editar" src="images/edit.png" border="0" width="16" height="16" /></a></div></td>
     <td><div align="center"><a href="excluirrodante.php?Cod=<? echo $row['CodReg'];?>"><img alt="Excluir" src="images/delete.png" border="0" width="16" height="16" /></a></div></td>
  </tr>
  <? } ?>
	<tr>
      <td height="23" colspan="11" class="headertabela"><div align="center">
        <input type="button" name="button" id="button" value="Voltar" onclick="javascript:history.back();" />
      </div></td>
      </tr>
  </table>
 <? }  ?>

    
  </div>
</form></td></tr></table>
</body>
</html>
