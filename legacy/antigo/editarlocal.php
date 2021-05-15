<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />
<title>Editar Local</title>
<?
//Includes
include "includeslocalhost.php"; //Conecta ao banco de dados

//Pega os dados da URL
$CodLocal = $_GET["Cod"];

//Verifica se os dados foram pegos
if ($CodLocal == "") {
	$Exibe = "<br><center><strong>Erro ao recuperar dados da URL!</strong></center><br>";
}

//Verifica se é para executar
if(isset($_POST['cmbCategoria'])) {
	//Pega variaveis vinda do formulário via POST
	foreach( $_POST as $campo => $vlr){
	   $$campo = AntiInjection($vlr);
	}
	$erro = 0;
	
	if(empty($cmbCategoria)){
		$msg = $msg . "Categoria inv&aacute;lida! <br>";
		$erro = $erro + 1;
	}
	if(empty($txtSigla)){
		$msg = $msg . "Sigla inv&aacute;lida! <br>";
		$erro = $erro + 1;
	}
	if(empty($txtNome)){
		$msg = $msg . "Nome inv&aacute;lido! <br>";
		$erro = $erro + 1;
	}
	if(empty($cmbBitola)){
		$msg = $msg . "Bitola inv&aacute;lida! <br>";
		$erro = $erro + 1;
	}
	if(empty($cmbFerroviaAtual)){
		$msg = $msg . "Ferrovia Atual inv&aacute;lida! <br>";
		$erro = $erro + 1;
	}
	if(empty($cmbFerroviaOrigem)){
		$msg = $msg . "Ferrovia de Origem inv&aacute;lida! <br>";
		$erro = $erro + 1;
	}
	if(empty($cmbEstado)){
		$msg = $msg . "Estado inv&aacute;lido! <br>";
		$erro = $erro + 1;
	}
	
	if($erro == 0){
		$sql = "UPDATE tblLocais SET Sigla = '". $txtSigla ."', FerroviaAtual = ". $cmbFerroviaAtual .", FerroviaOrigem = ". $cmbFerroviaOrigem .", Categoria = ". $cmbCategoria .", Bitola = ". $cmbBitola .", Nome = '" . $txtNome . "', Detalhes = '". $txtDetalhes ."', Estado = ". $cmbEstado . ", Latitude = '". $txtLatitude ."', Longitude = '". $txtLongitude ."' WHERE CodLocal = ". $CodLocal .";";
		echo $sql;
		$ask = mysql_query($sql);
		if ($ask!=0){
			$Exibe = $Mensagem['sucesso'];
		}
		else {
			$Exibe = $Mensagem['erro'];
		}
	} else {
		$Exibe = $Mensagem['erromsg1'] . $msg . $Mensagem['erromsg2'];
	}
}
?>
<link href="estilo.css" rel="stylesheet" type="text/css" />
</head>
<body><?
//Executa o comando
$sql = "SELECT * FROM tblLocais WHERE CodLocal = " . $CodLocal . ";";
$res = mysql_query($sql);
while ($row = mysql_fetch_array($res)) {
	$CodCategoria = $row['Categoria'];
	$Sigla = $row['Sigla'];
	$FerroviaAtual = $row['FerroviaAtual'];
	$FerroviaOrigem = $row['FerroviaOrigem'];
	$Bitola = $row['Bitola'];
	$Estado = $row['Estado'];
	$Nome = $row['Nome'];
	$Latitude = $row['Latitude'];
	$Longitude = $row['Longitude'];
	$Detalhes = $row['Detalhes'];
}
echo $Exibe;
?><table width="100%" align="center"><tr height="100%"><td align="center" valign="center" height="100%">
<form id="form1" name="form1" method="post" action="editarlocal.php?Cod=<? echo $CodLocal; ?>"><div align="center">
  <table width="500" border="1" cellspacing="0" cellpadding="0">
  <tr>
      <td height="23" colspan="2" class="headertabela"><div align="center" class="header">Editar Local</div></td>
      </tr>
  	<tr>
    <td width="119" class="headertabela"><div align="right">Categoria:</div></td>
      <td width="196" bgcolor="#FFFFFF"><select name="cmbCategoria" id="cmbCategoria" onchange="mudancaSelecao(this)">
        <option<? if ($Categoria == "") { echo " selected='selected' "; } ?>disabled="disabled">SELECIONE</option>
        <?
			$sql = "SELECT CodCategoria, Categoria FROM tblCategoriaLocal ORDER BY CodCategoria;";
			$res = @mysql_query($sql);
			
			//Exibe as linhas encontradas na consulta
			while ($row = mysql_fetch_array($res)) {
				echo "<option value=" . $row['CodCategoria'];
				if ($CodCategoria == $row['CodCategoria']) { echo " selected='selected'"; }
				echo ">" . $row['CodCategoria'] . " - " . $row['Categoria'] . "</option>";
			 }
	 ?>
        </select></td>
    </tr>
    <tr>
    
      <td width="119"  class="headertabela"><div align="right">Sigla:</div></td>
      <td width="196" bgcolor="#FFFFFF"><span class="style2">
        <input name="txtSigla" type="text" id="txtSigla" size="5" maxlength="3" value="<? echo $Sigla; ?>"/>
      </span></td>
    </tr>
    <tr>
    
      <td width="119"  class="headertabela"><div align="right">Nome:</div></td>
      <td width="196" bgcolor="#FFFFFF"><span class="style2">
        <input name="txtNome" type="text" id="txtNome" size="30" maxlength="255" value="<? echo $Nome; ?>"/>
      </span></td>
    </tr>
    <tr>
      <td class="headertabela"><div align="right">
        Bitola:
      </div></td>
      <td bgcolor="#FFFFFF"><span class="style2">
        <select name="cmbBitola" id="cmbBitola">
        	<option selected="selected" disabled="disabled">SELECIONE</option>
          <?
			$sql = "SELECT CodBitola, Bitola FROM tblBitolas ORDER BY Bitola;";
			$res = @mysql_query($sql);
			
			//Exibe as linhas encontradas na consulta
			while ($row = mysql_fetch_array($res)) {
				echo "<option value=" . $row['CodBitola'];
				if ($Bitola == $row['CodBitola']) { echo " selected='selected'"; }
				echo ">" . $row['Bitola'] . "</option>";
			 }
	 	?>
        </select>
      </span></td>
    </tr>
    <tr>
      <td class="headertabela"><div align="right">Ferrovia Atual:</div></td>
      <td bgcolor="#FFFFFF"><select name="cmbFerroviaAtual" id="cmbFerroviaAtual">
      	<option selected="selected" disabled="disabled">SELECIONE</option>
        <?
			$sql = "SELECT CodFerrovia, Nome FROM tblFerrovias ORDER BY Nome;";
			$res = @mysql_query($sql);
			
			//Exibe as linhas encontradas na consulta
			while ($row = mysql_fetch_array($res)) {
				echo "<option value=" . $row['CodFerrovia'];
				if ($FerroviaAtual == $row['CodFerrovia']) { echo " selected='selected'"; }
				echo ">" . $row['Nome'] . "</option>";
			 }
	 ?>
      </select></td>
    </tr>
    <tr>
      <td class="headertabela"><div align="right">Ferrovia de Origem:</div></td>
      <td bgcolor="#FFFFFF"><select name="cmbFerroviaOrigem" id="cmbFerroviaOrigem">
      <option selected="selected" disabled="disabled">SELECIONE</option>
        <?
			$sql = "SELECT CodFerrovia, Nome FROM tblFerrovias ORDER BY Nome;";
			$res = @mysql_query($sql);
			
			//Exibe as linhas encontradas na consulta
			while ($row = mysql_fetch_array($res)) {
				echo "<option value=" . $row['CodFerrovia'];
				if ($FerroviaOrigem == $row['CodFerrovia']) { echo " selected='selected'"; }
				echo ">" . $row['Nome'] . "</option>";
			 }
	 ?>
      </select></td>
    </tr>
    <tr>
      <td height="23" class="headertabela"><div align="right">Estado:</div></td>
      <td bgcolor="#FFFFFF"><select name="cmbEstado" id="cmbEstado">
        <option selected="selected" disabled="disabled">SELECIONE</option>
        <?
			$sql = "SELECT CodEstado, Estado FROM tblEstadoLocal ORDER BY Estado;";
			$res = @mysql_query($sql);
			
			//Exibe as linhas encontradas na consulta
			while ($row = mysql_fetch_array($res)) {
				echo "<option value=" . $row['CodEstado'];
				if ($Estado == $row['CodEstado']) { echo " selected='selected'"; }
				echo ">" . $row['Estado'] . "</option>";
			 }
	 	?>
            </select></td>
    </tr>
    <tr>
      <td width="119"  class="headertabela"><div align="right">Latitude:</div></td>
      <td width="196" bgcolor="#FFFFFF"><span class="style2">
        <input name="txtLatitude" type="text" id="txtLatitude" size="30" maxlength="255" value="<? echo $Latitude; ?>"/>
      </span></td>
    </tr>
    <tr>
      <td width="119"  class="headertabela"><div align="right">Longitude:</div></td>
      <td width="196" bgcolor="#FFFFFF"><span class="style2">
        <input name="txtLongitude" type="text" id="txtLongitude" size="30" maxlength="255" value="<? echo $Longitude; ?>"/>
      </span></td>
    </tr>
    <tr>
      <td height="23" class="headertabela"><div align="right">Detalhes:</div></td>
      <td bgcolor="#FFFFFF"><textarea name="txtDetalhes" cols="44" rows="5" id="txtDetalhes" value="<? echo $Detalhes; ?>"></textarea></td>
    </tr>
    <tr>
      <td height="23" colspan="2" class="headertabela"><div align="center">
        <input type="submit" name="submit" id="submit" value="Enviar" />
      </div></td>
      </tr>
  </table>
  </div>
</form></td></tr></table>
</body>
</html>
