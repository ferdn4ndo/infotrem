<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />
<title>Inserir Local</title>
<link href="estilo.css" rel="stylesheet" type="text/css" />
<style type="text/css">
<!--
.style1 {font-size: small}
.style2 {font-size: 9px}
-->
</style>
</head>
<body><?
//Includes
include "includeslocalhost.php"; //Conecta ao banco de dados

if (isset($_POST['txtNome'])) {
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
		//Consulta para verificar itens idênticos
		$sqlverifica = "SELECT * FROM tblLocais WHERE Sigla = '" . $txtSigla . "';";
		
		if(mysql_num_rows(mysql_query($sqlverifica)) > 0) { //Se já houver um registro igual
			echo $Mensagem['erroduplicado'];
		} else {
			$sql = "INSERT INTO tblLocais (Categoria, Sigla, Nome, Bitola, FerroviaAtual, FerroviaOrigem, Estado) VALUES(" . $cmbCategoria . ",'" . $txtSigla . "','" . $txtNome . "','" . $cmbBitola .  "'," . $cmbFerroviaAtual . "," . $cmbFerroviaOrigem . "," . $cmbEstado . ");";
			
			$ask = mysql_query($sql);
			if ($ask!=0){
				echo $Mensagem['sucesso'];
			}
			else {
				echo $Mensagem['erro'];
			}
		}
	} else {
		echo $Mensagem['erromsg1'];
		echo $msg;
		echo $Mensagem['erromsg2'];
	}
}
?><table width="100%" align="center"><tr height="100%"><td align="center" valign="center" height="100%">
<form id="form1" name="form1" method="post" action="#"><div align="center">
  <table width="500" border="1" cellspacing="0" cellpadding="0">
  <tr>
    <td colspan="2" class="headertabela"><div align="center">Cadastrar Local</div></td>
      </tr>
  	<tr>
    <td width="119" class="headertabela"><div align="right">Categoria:</div></td>
      <td width="196" bgcolor="#FFFFFF"><select name="cmbCategoria" id="cmbCategoria">
        <option selected="selected" disabled="disabled">SELECIONE</option>
        <?
			$sql = "SELECT CodCategoria, Categoria FROM tblCategoriaLocal ORDER BY Categoria;";
			$res = @mysql_query($sql);
			
			//Exibe as linhas encontradas na consulta
			while ($row = mysql_fetch_array($res)) {
				echo "<option value=" . $row['CodCategoria'];
				echo ">" . $row['Categoria'] . "</option>";
			 }
	 	?>
        </select></td>
    </tr>
    <tr>
    
      <td width="119"  class="headertabela"><div align="right">Sigla:</div></td>
      <td width="196" bgcolor="#FFFFFF"><span class="style2">
        <input name="txtSigla" type="text" id="txtSigla" size="5" maxlength="3" />
      </span></td>
    </tr>
    <tr>
    
      <td width="119"  class="headertabela"><div align="right">Nome:</div></td>
      <td width="196" bgcolor="#FFFFFF"><span class="style2">
        <input name="txtNome" type="text" id="txtNome" size="30" maxlength="255" />
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
				echo ">" . $row['Estado'] . "</option>";
			 }
	 	?>
            </select></td>
    </tr>
    <tr>
      <td height="23" class="headertabela"><div align="right">Detalhes:</div></td>
      <td bgcolor="#FFFFFF"><textarea name="txtDetalhes" cols="44" rows="5" id="txtDetalhes"></textarea></td>
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
