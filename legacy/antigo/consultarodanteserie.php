<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />
<title>Consultar Mat. Rodante</title>
<link href="estilo.css" rel="stylesheet" type="text/css" />
</head>
<body><?
//Pega a URL
$Categoria = (isset($_GET["Categoria"])) ? $_GET["Categoria"] : 1;

//Pega os dados da consulta anterior, caso existirem
$Categoria = $_POST['cmbCategoria']; 
$NumeroInicial = $_POST['txtNumeroInicial'];
$NumeroFinal = $_POST['txtNumeroFinal'];

//Includes
include "includeslocalhost.php"; 
?><table width="100%" align="center"><tr height="100%"><td align="center" valign="center" height="100%">
<form id="form1" name="form1" method="post" action="#"><div align="center">
  <table width="750" border="1" cellspacing="0" cellpadding="0">
  <tr>
    <td colspan="4" class="headertabela"><div align="center">Consultar Material Rodante Por S&eacute;rie:</div></td>
      </tr>
    <tr>
      <td  class="headertabela">
        
Categoria:<br /> 
<select name="cmbCategoria" id="cmbCategoria">
        <option selected='selected' disabled="disabled">SELECIONE</option>
        <?
			$sql = "SELECT CodCategoria, Categoria FROM tblCategoriaRodante ORDER BY CodCategoria;";
			$res = @mysql_query($sql);
			
			//Exibe as linhas encontradas na consulta
			while ($row = mysql_fetch_array($res)) {
				echo "<option value=" . $row['CodCategoria'];
				if ($Categoria == $row['CodCategoria']) { echo " selected='selected'"; } 
				echo ">" . $row['CodCategoria'] . " - " . $row['Categoria'] . "</option>";
			 }
	 ?>
        </select></td>
      <td  class="headertabela">
 N&uacute;mero Inicial:<br />
<input type="text" name="txtNumeroInicial" id="txtNumeroInicial" value="<? echo $NumeroInicial; ?>" maxlength="6" size="10" /></td>
		<td  class="headertabela">
 N&uacute;mero Final:<br />
<input type="text" name="txtNumeroFinal" id="txtNumeroFinal" value="<? echo $NumeroFinal; ?>" maxlength="6" size="10" /></td>
      </tr>
    <tr>
      <td height="23" colspan="4" class="headertabela"><div align="center">
      <input type="hidden" name="txtEnviar" id="txtEnviar" value="1" />
        <input type="submit" name="submit" id="submit" value="Consultar" />
      </div></td>
      </tr>
  </table>
  </div>
</form></td></tr></table>
<?
//Verifica se é para executar a consulta
if (isset($_POST['txtEnviar'])) {
	//Define as variáveis
	$erros = 0;
	$msg = "";
	$where = "";
	
	//Verifica a categoria
	if((isset($_POST['cmbCategoria'])) && (!empty($_POST['cmbCategoria']))) {
		$Categoria = $_POST['cmbCategoria']; 
		$where = $where . " tblRodante.Categoria = " . $Categoria;
	} else {
		$msg = $msg . "'Categoria' n&atilde;o foi selecionado! <br />";
		$erros = $erros + 1;
	}
	
	//Verifica o número inicial
	if((isset($_POST['txtNumeroInicial'])) && (!empty($_POST['txtNumeroInicial']))) {
		if(is_numeric($_POST['txtNumeroInicial'])) {
			$NumeroInicial = $_POST['txtNumeroInicial'];
			$where = $where . " AND tblRodante.Numero >= " . $NumeroInicial;
		} else {
			$msg = $msg . "O campo 'N&uacute;mero Inicial' deve ser num&eacute;rico! <br />";
			$erros = $erros + 1;
		}
	} else {
		$msg = $msg . "O campo 'N&uacute;mero Inicial' n&atilde;o foi preenchido! <br />";
		$erros = $erros + 1;
	}
	
	//Verifica o número final
	if((isset($_POST['txtNumeroFinal'])) && (!empty($_POST['txtNumeroFinal']))) {
		if(is_numeric($_POST['txtNumeroFinal'])) {
			$NumeroFinal = $_POST['txtNumeroFinal'];
			$where = $where . " AND tblRodante.Numero <= " . $NumeroFinal;
		} else {
			$msg = $msg . "O campo 'N&uacute;mero Final' deve ser num&eacute;rico! <br />";
			$erros = $erros + 1;
		}
	} else {
		$msg = $msg . "O campo 'N&uacute;mero Final' n&atilde;o foi preenchido! <br />";
		$erros = $erros + 1;
	}
	
	//Verifica o intervalo
	if((!empty($NumeroFinal)) && (!empty($NumeroInicial))) {
		if($NumeroFinal < $NumeroInicial) {
			$msg = $msg . "O campo 'N&uacute;mero Final' deve ser maior ou igual ao campo 'N&uacute;mero Inicial'! <br />";
			$erros = $erros + 1;
		}
	}
	
//Verifica os erros
	if ($erros==0) {
			//////////////////////////////////////////////////////////////////////////////////
			//Prepara a string e o SQL
			if ($Categoria == 1) { //Locomotivas
				$Nome = "Locomotivas";
				$sql = "SELECT tblRodante.*, tblModelos.CodModLoco, tblModLoco.ModeloLoco, tblFabricantes.NomeFabricante, tblTracao.Tracao, tblFerrovias.Nome AS Ferrovia1, tblFerrovias2.Nome AS Ferrovia2, tblLocais.Nome AS Local, tblLocais.Sigla, tblEstadoRodante.Estado FROM ((((((((tblRodante INNER JOIN tblModelos ON tblRodante.CodModelo = tblModelos.CodModelo) INNER JOIN tblModLoco ON tblModelos.CodModLoco = tblModLoco.CodModLoco) INNER JOIN tblFabricantes ON tblModLoco.FabricanteLoco = tblFabricantes.CodFabricante) INNER JOIN tblTracao ON tblModLoco.TracaoLoco = tblTracao.CodTracao) INNER JOIN tblFerrovias ON tblRodante.FerroviaAtual = tblFerrovias.CodFerrovia) INNER JOIN tblFerrovias tblFerrovias2 ON tblRodante.FerroviaOrigem = tblFerrovias2.CodFerrovia) INNER JOIN tblLocais ON tblRodante.UltimoLocal = tblLocais.CodLocal) INNER JOIN tblEstadoRodante ON tblRodante.Estado = tblEstadoRodante.CodEstado) WHERE ". $where ." ORDER BY tblModLoco.ModeloLoco, tblRodante.Numero;";
			} elseif ($Categoria == 2) { //Vagões
				$Nome = "Vag&otilde;es";
				$sql = "SELECT tblRodante.*, tblModelos.CodTipoVag, tblModelos.CodPesoVag, tblFerrovias.Nome AS Ferrovia1, tblFerrovias2.Nome AS Ferrovia2, tblLocais.Nome AS Local, tblLocais.Sigla, tblEstadoRodante.Estado, tblTipoVags.TipoVag, tblPesoVags.LetraPesoVag FROM (((((((tblRodante INNER JOIN tblModelos ON tblRodante.CodModelo = tblModelos.CodModelo) INNER JOIN tblFerrovias ON tblRodante.FerroviaAtual = tblFerrovias.CodFerrovia) INNER JOIN tblFerrovias tblFerrovias2 ON tblRodante.FerroviaOrigem = tblFerrovias2.CodFerrovia) INNER JOIN tblLocais ON tblRodante.UltimoLocal = tblLocais.CodLocal) INNER JOIN tblEstadoRodante ON tblRodante.Estado = tblEstadoRodante.CodEstado) INNER JOIN tblTipoVags ON tblModelos.CodTipoVag = tblTipoVags.CodTipoVag) INNER JOIN tblPesoVags ON tblModelos.CodPesoVag = tblPesoVags.CodPesoVag) WHERE ". $where ." ORDER BY tblTipoVags.TipoVag, tblPesoVags.LetraPesoVag, tblRodante.Numero;";
			} elseif ($Categoria == 3) { //Carros
				$Nome = "Carros";
				$sql = "SELECT tblRodante.*, tblModelos.CodTipoCarro, tblModelos.CodMatCarro, tblFerrovias.Nome AS Ferrovia1, tblFerrovias2.Nome AS Ferrovia2, tblLocais.Nome AS Local, tblLocais.Sigla, tblEstadoRodante.Estado, tblTipoCarro.LetraTipoCarro, tblMatCarro.LetraMatCarro FROM (((((((tblRodante INNER JOIN tblModelos ON tblRodante.CodModelo = tblModelos.CodModelo) INNER JOIN tblFerrovias ON tblRodante.FerroviaAtual = tblFerrovias.CodFerrovia) INNER JOIN tblFerrovias tblFerrovias2 ON tblRodante.FerroviaOrigem = tblFerrovias2.CodFerrovia) INNER JOIN tblLocais ON tblRodante.UltimoLocal = tblLocais.CodLocal) INNER JOIN tblEstadoRodante ON tblRodante.Estado = tblEstadoRodante.CodEstado) INNER JOIN tblTipoCarro ON tblModelos.CodTipoCarro = tblTipoCarro.CodTipoCarro) INNER JOIN tblMatCarro ON tblModelos.CodMatCarro = tblMatCarro.CodMatCarro) WHERE ". $where ." ORDER BY tblTipoCarro.LetraTipoCarro, tblMatCarro.LetraMatCarro, tblRodante.Numero;";
			} elseif ($Categoria == 4) { //Autos de Linha
				$Nome = "Autos de Linha";
				$sql = "SELECT tblRodante.*, tblModelos.CodTipoAuto, tblTipoAuto.TipoAuto, tblFerrovias.Nome AS Ferrovia1, tblFerrovias2.Nome AS Ferrovia2, tblLocais.Sigla, tblLocais.Nome AS Local, tblEstadoRodante.Estado FROM ((((((tblRodante INNER JOIN tblModelos ON tblRodante.CodModelo = tblModelos.CodModelo) INNER JOIN tblTipoAuto ON tblModelos.CodTipoAuto = tblTipoAuto.CodTipoAuto) INNER JOIN tblFerrovias ON tblRodante.FerroviaAtual = tblFerrovias.CodFerrovia) INNER JOIN tblFerrovias tblFerrovias2 ON tblRodante.FerroviaOrigem = tblFerrovias2.CodFerrovia) INNER JOIN tblLocais ON tblRodante.UltimoLocal = tblLocais.CodLocal) INNER JOIN tblEstadoRodante ON tblRodante.Estado = tblEstadoRodante.CodEstado) WHERE ". $where ." ORDER BY tblTipoAuto.TipoAuto, tblRodante.Numero;";
			} elseif ($Categoria == 5) { //Automotriz / Trem-unidade
                                $Nome = "Automotrizes / Trem-unidade";
                                $sql = "SELECT tblRodante.*, tblModelos.CodTipoMotriz, tblTipoMotrizes.TipoMotriz, tblFerrovias.Nome AS Ferrovia1, tblFerrovias2.Nome AS Ferrovia2, tblLocais.Sigla, tblLocais.Nome AS Local, tblEstadoRodante.Estado FROM ((((((tblRodante INNER JOIN tblModelos ON tblRodante.CodModelo = tblModelos.CodModelo) INNER JOIN tblTipoMotrizes ON tblModelos.CodTipoMotriz = tblTipoMotrizes.CodTipoMotriz) INNER JOIN tblFerrovias ON tblRodante.FerroviaAtual = tblFerrovias.CodFerrovia) INNER JOIN tblFerrovias tblFerrovias2 ON tblRodante.FerroviaOrigem = tblFerrovias2.CodFerrovia) INNER JOIN tblLocais ON tblRodante.UltimoLocal = tblLocais.CodLocal) INNER JOIN tblEstadoRodante ON tblRodante.Estado = tblEstadoRodante.CodEstado) WHERE ". $where ." ORDER BY tblTipoAuto.TipoAuto, tblRodante.Numero;";
                        }
				
			$res = mysql_query($sql);
			/*
			while ($row = mysql_fetch_array($res)) {
				//Prepara os dados
				//$CodCategoria = $row['Categoria'];
				if ($Categoria==1) {
					$Modelo = $row['Modelo'];
					$Fabricante = $row['NomeFabricante'];
					$Tracao = $row['Tracao'];
				} elseif ($Categoria==2) {
					$Modelo = $row['TipoVag'] . $row['LetraPesoVag'];
				} elseif ($Categoria==3) {
					$Modelo = $row['LetraTipoCarro'] . $row['LetraMatCarro'];
				} elseif ($Categoria==4) {
					$Modelo = $row['Modelo'];
				}
				$Numero = $row['Numero'];
				$FerroviaOrigem = $row['Ferrovia2'];
				$FerroviaAtual = $row['Ferrovia1'];
				$UltimoLocal = $row['Local'] . " (" . $row['Sigla'] . ")";
				$UltimaData = mostraData($row['UltimaData']);
				$Estado = $row['Estado'];
				$Detalhes = $row['Detalhes'];
			*/	
				//echo $sql;
	echo "<div id='consulta' align='center'>";
			if ($Categoria==1) { ?>
				<table width="750" border="1" cellspacing="0" cellpadding="0">
  <tr>
    <td colspan="13" class="headertabela"><div align="center">Listar Consulta</div></td>
      </tr>
    <tr>
      <td width="5%"  class="headertabela"><div align="center">Cod</div></td>
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
      <td><div align="center"><a href="exibirrodante.php?Cod=<? echo $row['CodReg'];?>"><? echo $row['Numero'] . "-" . CalculaDV($row['Numero']);?></a></div></td> 
     <td><div align="center"><? echo $row['Ferrovia1'];?></div></td> 
     <td><div align="center"><? echo $row['Ferrovia2'];?></div></td>
     <td><div align="center"><? echo $row['Local'] . " (" . $row['Sigla'] . ")";?></div></td>
     <td><div align="center"><? echo mostraData($row['UltimaData']);?></div></td>
     <td><div align="center"><? echo $row['Estado'];?></div></td>
     <td><div align="center"><? echo $Detalhes;?></div></td>
     <td><div align="center"><a href="editarrodante.php?Cod=<? echo $row['CodReg'];?>&Categoria=<? echo $Categoria;?>"><img alt="Editar" src="images/edit.png" border="0" width="16" height="16" /></a></div></td>
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
    <td colspan="11" class="headertabela"><div align="center">Listar Consulta</div></td>
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
		if ($Categoria == 1) { //Locos
			$Modelo = $row['ModeloLoco'];
		} elseif ($Categoria == 2) { //Vags
			$Modelo = $row['TipoVag'] . $row['LetraPesoVag'];
		} elseif ($Categoria == 3) { //Carros
			$Modelo = $row['LetraTipoCarro'] . $row['LetraMatCarro'];
		} elseif ($Categoria == 4) { //Autos
			$Modelo = $row['TipoAuto'];
		} elseif ($Catgoria == 5) { //Automotrizes/trem-unidade
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
     <td><div align="center"><a href="editarrodante.php?Cod=<? echo $row['CodReg'];?>&Categoria=<? echo $Categoria;?>"><img alt="Editar" src="images/edit.png" border="0" width="16" height="16" /></a></div></td>
     <td><div align="center"><a href="excluirrodante.php?Cod=<? echo $row['CodReg'];?>"><img alt="Excluir" src="images/delete.png" border="0" width="16" height="16" /></a></div></td>
  </tr>
  <? } ?>
	<tr>
      <td height="23" colspan="11" class="headertabela"><div align="center">
        <input type="button" name="button" id="button" value="Voltar" onclick="javascript:history.back();" />
      </div></td>
      </tr>
  </table>
    <?

	}
	echo "</div>";
?>
  </div>
</form></td></tr></table>
<?				
	} else {
		echo $Mensagem['erromsg1']; 
		echo $msg; 
		echo $Mensagem['erromsg2'];
	}
}
?>
</body>
</html>

