<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />
<title>Consultar Mat. Rodante</title>
<link href="estilo.css" rel="stylesheet" type="text/css" />
</head>
<body><?
//Includes
include "includeslocalhost.php"; 
?><table width="100%" align="center"><tr height="100%"><td align="center" valign="center" height="100%">
<form id="form1" name="form1" method="post" action="#"><div align="center">
  <table width="740" border="1" cellspacing="0" cellpadding="0">
  <tr>
    <td colspan="4" class="headertabela"><div align="center">Consultar Local:</div></td>
      </tr>
    <tr>
      <td width="29%"  class="headertabela">
        
Categoria:<br /> 
<select name="cmbCategoria" id="cmbCategoria">
        <option selected='selected' disabled="disabled">SELECIONE</option>
        <?
			$sql = "SELECT CodCategoria, Categoria FROM tblCategoriaLocal ORDER BY CodCategoria;";
			$res = @mysql_query($sql);
			
			//Exibe as linhas encontradas na consulta
			while ($row = mysql_fetch_array($res)) {
				echo "<option value=" . $row['CodCategoria'];
				echo ">" . $row['CodCategoria'] . " - " . $row['Categoria'] . "</option>";
			 }
	 ?>
        </select></td>
      <td width="24%"  class="headertabela">
        
Sigla:<br />
<input type="text" name="txtSigla" id="txtSigla" maxlength="3" size="10" /></td>
      <td width="23%"  class="headertabela">
      
Nome:<br />
<input type="text" name="txtNome" id="txtNome" maxlength="100" size="15" />
</td>
      <td width="24%"  class="headertabela">
      
Bitola:<br />
<select name="cmbBitola" id="cmbBitola">
  <option selected='selected' disabled="disabled">SELECIONE</option>
  <?
			$sql = "SELECT CodBitola, Bitola FROM tblBitolas ORDER BY Bitola;";
			$res = @mysql_query($sql);
			
			//Exibe as linhas encontradas na consulta
			while ($row = mysql_fetch_array($res)) {
				echo "<option value=" . $row['CodBitola'];
				echo ">" . $row['Bitola'] . "</option>";
			 }
	 	?>
</select>
      </td>
    </tr>
      <tr>
      <td width="29%"  class="headertabela">
 C&oacute;digo:<br />
<input type="text" name="txtCodigo" id="txtCodigo" maxlength="5" size="10" />
      </td>
      <td width="24%"  class="headertabela">
      
Latitude:<br />
<input type="text" name="txtLatitude" id="txtLatitude" maxlength="10" size="10" />
      </td>
      <td width="23%"  class="headertabela">
 Longitude:
  <br />
  <input type="text" name="txtLongitude" id="txtLongitude" maxlength="10" size="10" />
      </td>
      <td width="24%"  class="headertabela">
      
Estado:<br />
<select name="cmbEstado" id="cmbEstado">
  <option selected='selected' disabled="disabled">SELECIONE</option>
  <?
			$sql = "SELECT CodEstado, Estado FROM tblEstadoLocal ORDER BY Estado;";
			$res = @mysql_query($sql);
			
			//Exibe as linhas encontradas na consulta
			while ($row = mysql_fetch_array($res)) {
				echo "<option value=" . $row['CodEstado'];
				echo ">" . $row['Estado'] . "</option>";
			 }
	 	?>
</select>
      </td>
      </tr><!--
      <tr>
      <td colspan="2"  class="headertabela">
      <input type="checkbox" name="chkFerroviaAtual" id="chkFerroviaAtual" />
Ferrovia Atual:
<select name="cmbFerroviaAtual" id="cmbFerroviaAtual">
  <option selected='selected' disabled="disabled">SELECIONE</option>
  <? /*
			$sql = "SELECT CodFerrovia, Nome FROM tblFerrovias ORDER BY Nome;";
			$res = @mysql_query($sql);
			
			//Exibe as linhas encontradas na consulta
			while ($row = mysql_fetch_array($res)) {
				echo "<option value=" . $row['CodFerrovia'];
				echo ">" . $row['Nome'] . "</option>";
			 }
	*/ ?>
</select>
            </td>
      <td colspan="2"  class="headertabela">
      <input type="checkbox" name="chkFerroviaOrigem" id="chkFerroviaOrigem" />
Ferrovia de Origem:
<select name="cmbFerroviaOrigem" id="cmbFerroviaOrigem">
  <option selected='selected' disabled="disabled">SELECIONE</option>
  <? /*
			$sql = "SELECT CodFerrovia, Nome FROM tblFerrovias ORDER BY Nome;";
			$res = @mysql_query($sql);
			
			//Exibe as linhas encontradas na consulta
			while ($row = mysql_fetch_array($res)) {
				echo "<option value=" . $row['CodFerrovia'];
				echo ">" . $row['Nome'] . "</option>";
			 }
	*/ ?>
</select>
      </td>
      </tr> -->
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
	
	$where = $where . " 1=1 ";
	
	
	//Verifica a categoria
	//if(isset($_POST['chkCategoria'])) {
		if((isset($_POST['cmbCategoria'])) && (!empty($_POST['cmbCategoria']))) {
			$Categoria = $_POST['cmbCategoria'];
			$where = $where . " AND tblLocais.Categoria = " . $Categoria;
		//} else {
		//	$msg = $msg . "O campo 'Categoria' n&atilde;o foi preenchido! <br />";
		//	$erros = $erros + 1;
		}
	//}
	
	//Verifica a sigla
	//if(isset($_POST['chkSigla'])) {
		if((isset($_POST['txtSigla'])) && (!empty($_POST['txtSigla']))) {
			$Sigla = strtoupper($_POST['txtSigla']);
			$where = $where . " AND tblLocais.Sigla = '" . $Sigla . "'";
		//} else {
		//	$msg = $msg . "O campo 'Sigla' n&atilde;o foi preenchido! <br />";
		//	$erros = $erros + 1;
		}
	//}
	
	//Verifica o nome
	//if(isset($_POST['chkNome'])) {
		if((isset($_POST['txtNome'])) && (!empty($_POST['txtNome']))) {
			$NomeSemTratar = strtoupper($_POST['txtNome']);
			$caracteresA = array("ã","Ã","â","Â","á","Á","à","À");
			$NomeTratadoA = str_replace($caracteresA,"A",$NomeSemTratar);
			$caracteresE = array("é","É","è","È","ê","Ê");
			$NomeTratadoE = str_replace($caracteresE,"E",$NomeTratadoA);
			$caracteresI = array("í","Í","î","Î");
			$NomeTratadoI = str_replace($caracteresI,"I",$NomeTratadoE);
			$caracteresO = array("ó","Ó","ò","Ò","ô","Ô");
			$NomeTratadoO = str_replace($caracteresO,"O",$NomeTratadoI);
			$caracteresU = array("ú","Ú","ù","Ù","û","Û","ü","Ü");
			$NomeTratadoU = str_replace($caracteresU,"U",$NomeTratadoO);
			$Nome = $NomeTratadoU;
			$where = $where . " AND tblLocais.Nome LIKE '%" . $Nome . "%'";
		//} else {
		//	$msg = $msg . "O campo 'Nome' n&atilde;o foi preenchido! <br />";
		//	$erros = $erros + 1;
		}
	//}
	
	//Verifica a bitola
	//if(isset($_POST['chkBitola'])) {
		if((isset($_POST['cmbBitola'])) && (!empty($_POST['cmbBitola']))) {
			$Bitola = $_POST['cmbBitola'];
			$where = $where . " AND tblLocais.Bitola = " . $Bitola;
		//} else {
		//	$msg = $msg . "O campo 'Bitola' n&atilde;o foi preenchido! <br />";
		//	$erros = $erros + 1;
		}
	//}
	
	//Verifica o codigo
	//if(isset($_POST['chkCodigo'])) { 
		if((isset($_POST['txtCodigo'])) && (!empty($_POST['txtCodigo']))) {
			if(is_numeric($_POST['txtCodigo'])) {
				$Codigo = $_POST['txtCodigo'];
				$where = $where . " AND tblLocais.CodLocal = " . $Codigo;
			} else {
				$msg = $msg . "O campo 'C&oacute;digo' deve ser num&eacute;rico! <br />";
				$erros = $erros + 1;
			}
		//} else {
		//	$msg = $msg . "O campo 'C&oacute;digo' n&atilde;o foi preenchido! <br />";
		//	$erros = $erros + 1;
		} 
	//}
	
	//Verifica a latitude
	//if(isset($_POST['chkLatitude'])) {
		if((isset($_POST['txtLatitude'])) && (!empty($_POST['txtLatitude']))) {
			if(is_numeric($_POST['txtLatitude'])) {
				$Latitude = $_POST['txtLatitude'];
				$where = $where . " AND tblLocais.Latitude = '" . $Latitude . "'";
			} else {
				$msg = $msg . "O campo 'Latitude' deve ser num&eacute;rico! <br />";
				$erros = $erros + 1;
			}
		//} else {
		//	$msg = $msg . "O campo 'Latitude' n&atilde;o foi preenchido! <br />";
		//	$erros = $erros + 1;
		}
	//}
	
	//Verifica a longitude
	//if(isset($_POST['chkLongitude'])) {
		if((isset($_POST['txtLongitude'])) && (!empty($_POST['txtLongitude']))) {
			if(is_numeric($_POST['txtLongitude'])) {
				$Longitude = $_POST['txtLongitude'];
				$where = $where . " AND tblLocais.Longitude = '" . $Longitude . "'";
			} else {
				$msg = $msg . "O campo 'Longitude' deve ser num&eacute;rico! <br />";
				$erros = $erros + 1;
			}
		//} else {
		//	$msg = $msg . "O campo 'Longitude' n&atilde;o foi preenchido! <br />";
		//	$erros = $erros + 1;
		}
	//}
	
	//Verifica o estado
	//if(isset($_POST['chkEstado'])) {
		if((isset($_POST['cmbEstado'])) && (!empty($_POST['cmbEstado']))) {
			$Estado = $_POST['cmbEstado'];
			$where = $where . " AND tblLocais.Estado = " . $Estado;
		//} else {
		//	$msg = $msg . "'Estado' n&atilde;o foi selecionado! <br />";
		//	$erros = $erros + 1;
		}
	//}
	
	//Verifica a ferrovia de origem
	//if(isset($_POST['chkFerroviaOrigem'])) {
		if((isset($_POST['cmbFerroviaOrigem'])) && (!empty($_POST['cmbFerroviaOrigem']))) {
			$FerroviaOrigem = $_POST['cmbFerroviaOrigem'];
			$where = $where . " AND tblLocais.FerroviaOrigem = " . $FerroviaOrigem;
		//} else {
		//	$msg = $msg . "'Ferrovia de Origem' n&atilde;o foi selecionado! <br />";
		//	$erros = $erros + 1;
		}
	//}
	
	//Verifica a ferrovia atual
	//if(isset($_POST['chkFerroviaAtual'])) {
		if((isset($_POST['cmbFerroviaAtual'])) && (!empty($_POST['cmbFerroviaAtual']))) {
			$FerroviaAtual = $_POST['cmbFerroviaAtual'];
			$where = $where . " AND tblLocais.FerroviaAtual = " . $FerroviaAtual;
		//} else {
		//	$msg = $msg . "'Ferrovia Atual' n&atilde;o foi selecionado! <br />";
		//	$erros = $erros + 1;
		}
	//}
	
	
	//Verifica os erros
	if ($erros==0) {
		$sql = "SELECT tblLocais.*, tblCategoriaLocal.Categoria AS NomeCategoria, tblBitolas.Bitola AS NomeBitola, tblEstadoLocal.Estado AS NomeEstado FROM tblLocais INNER JOIN tblCategoriaLocal ON tblLocais.Categoria = tblCategoriaLocal.CodCategoria  INNER JOIN tblBitolas ON tblLocais.Bitola = tblBitolas.CodBitola INNER JOIN tblEstadoLocal ON tblLocais.Estado = tblEstadoLocal.CodEstado WHERE ". $where ." ORDER BY tblLocais.Sigla;";
		$res = mysql_query($sql);
		$contar = mysql_num_rows($res);
		//echo $sql;
				?><div align="center">
		<table width="740" border="1" cellspacing="0" cellpadding="0">
  <tr>
    <td colspan="13" class="headertabela"><div align="center">Listar Consulta - <? echo $contar; ?> resultado(s) </div></td>
      </tr>
    <tr>
      <td width="5%"  class="headertabela"><div align="center">Cód</div></td>
      <td width="6%" bgcolor="#FFFFFF" class="headertabela"><div align="center">Sigla</div></td>
      <td width="22%" bgcolor="#FFFFFF" class="headertabela"><div align="center">Nome</div></td>
      <td width="6%" bgcolor="#FFFFFF" class="headertabela"><div align="center">Categoria</div></td>
      <td width="7%" bgcolor="#FFFFFF" class="headertabela"><div align="center">Bitola</div></td>
      <!-- <td width="10%" bgcolor="#FFFFFF" class="headertabela"><div align="center">Ferr. Atual</div></td>
      <td width="10%" bgcolor="#FFFFFF" class="headertabela"><div align="center">Ferr. Origem</div></td> -->
      <td width="10%" bgcolor="#FFFFFF" class="headertabela"><div align="center">Latitude</div></td>
      <td width="10%" bgcolor="#FFFFFF" class="headertabela"><div align="center">Longitude</div></td>
      <td width="14%" bgcolor="#FFFFFF" class="headertabela"><div align="center">Estado</div></td><td width="8%" bgcolor="#FFFFFF" class="headertabela"><div align="center">Detalhes</div></td>
<td width="2%" bgcolor="#FFFFFF" class="headertabela"><div align="center">E</div></td>
<td width="2%" bgcolor="#FFFFFF" class="headertabela"><div align="center">X</div></td>      
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
		
		if(strlen($row['Latitude'])>12){
			$Latitude = substr($row['Latitude'],0,12);
		} else {
			$Latitude = $row['Latitude'];
		}
		
		if(strlen($row['Longitude'])>12){
			$Longitude = substr($row['Longitude'],0,12);
		} else {
			$Longitude = $row['Longitude'];
		}
 ?> 
  <tr>
      <td><div align="center"><? echo $row['CodLocal'];?></div></td>
      <td><div align="center"><? echo $row['Sigla'];?></div></td>
      <td><div align="center"><a href="exibirlocal.php?Cod=<? echo $row['CodLocal'];?>"><? echo $row['Nome'];?></a></div></td> 
      <td><div align="center"><? echo $row['NomeCategoria'];?></div></td> 
      <td><div align="center"><? echo $row['NomeBitola'];?></div></td> 
     <!-- <td><div align="center"><? //echo $row['Ferrovia1'];?></div></td> 
     <td><div align="center"><? //echo $row['Ferrovia2'];?></div></td> -->
     <td><div align="center"><? echo $Latitude;?></div></td>
     <td><div align="center"><? echo $Longitude;?></div></td>
     <td><div align="center"><? echo $row['NomeEstado'];?></div></td>
     <td><div align="center"><? echo $Detalhes;?></div></td>
     <td><div align="center"><a href="editarlocal.php?Cod=<? echo $row['CodLocal'];?>"><img alt="Editar" src="images/edit.png" border="0" width="16" height="16" /></a></div></td>
     <td><div align="center"><a href="excluirlocal.php?Cod=<? echo $row['CodLocal'];?>"><img alt="Excluir" src="images/delete.png" border="0" width="16" height="16" /></a></div></td>
  </tr>
  <?  } ?>
	<tr>
      <td height="23" colspan="11" class="headertabela"><div align="center">
        <input type="button" name="button" id="button" value="Voltar" onclick="javascript:history.back();" />
      </div></td>
      </tr>
  </table>
  </div>
</form></td></tr></table></div>
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

