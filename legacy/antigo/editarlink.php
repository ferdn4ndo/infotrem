<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />
<title>Editar Link</title>
<?
//Includes
include "includeslocalhost.php"; //Conecta ao banco de dados

//Pega os dados da URL
$CodLink = $_GET["Cod"];

//Verifica se os dados foram pegos
if ($CodLink == "") {
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
	if(empty($txtNome)){
		$msg = $msg . "Nome inv&aacute;lido! <br>";
		$erro = $erro + 1;
	}
	if(empty($txtLink)){
		$msg = $msg . "Link inv&aacute;lido! <br>";
		$erro = $erro + 1;
	}
	
	if($erro == 0){
		$sql = "UPDATE tblLinks SET Categoria = " . $cmbCategoria . ", Nome = '" . $txtNome . "', Link = '" . $txtLink . "', Detalhes = '" . $txtDetalhes . "' WHERE CodLink = ". $CodLink .";";
		//echo $sql;
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
$sql = "SELECT * FROM tblLinks WHERE CodLink = " . $CodLink . ";";
$res = mysql_query($sql);
while ($row = mysql_fetch_array($res)) {
	$CodCategoria = $row['Categoria'];
	$Nome = $row['Nome'];
	$Link = $row['Link'];
	$Detalhes = $row['Detalhes'];
}
echo $Exibe;
?><table width="100%" align="center"><tr height="100%"><td align="center" valign="center" height="100%">
<form id="form1" name="form1" method="post" action="editarlink.php?Cod=<? echo $CodLink; ?>"><div align="center">
  <table width="500" border="1" cellspacing="0" cellpadding="0">
  <tr>
      <td height="23" colspan="2" class="headertabela"><div align="center" class="header">Editar Link</div></td>
      </tr>
  	<tr>
    <tr>
      <td width="184" nowrap="nowrap" class="headertabela"><div align="right">Nome:</div></td>
      <td width="300" bgcolor="#FFFFFF"><div align="left"><span class="style3">
        <input name="txtNome" type="text" id="txtNome" size="50" maxlength="255" value="<? echo $Nome; ?>" />
      </span></div></td>
  </tr>
    <td width="119" class="headertabela"><div align="right">Categoria:</div></td>
      <td width="196" bgcolor="#FFFFFF"><select name="cmbCategoria" id="cmbCategoria" onchange="mudancaSelecao(this)">
        <option<? if ($Categoria == "") { echo " selected='selected' "; } ?>disabled="disabled">SELECIONE</option>
        <?
			$sql = "SELECT CodCategoria, Categoria FROM tblCategoriaLink ORDER BY CodCategoria;";
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
      <td width="184" nowrap="nowrap" class="headertabela"><div align="right">Link:</div></td>
      <td width="300" bgcolor="#FFFFFF"><div align="left"><span class="style3">
        <input name="txtLink" type="text" id="txtLink" size="50" maxlength="255" value="<? echo $Link; ?>" />
      </span></div></td>
    </tr>
    <tr>
      <td width="184" nowrap="nowrap" class="headertabela"><div align="right">Detalhes:</div></td>
      <td width="300" bgcolor="#FFFFFF"><div align="left">
        <textarea name="txtDetalhes" cols="47" rows="5" id="txtDetalhes" value="<? echo $Detalhes; ?>"></textarea>
      </div></td>
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
