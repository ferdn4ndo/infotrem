<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />
<title>Inserir V&iacute;deo Externo</title>
<link href="estilo.css" rel="stylesheet" type="text/css" />
</head>
<body><?
//Includes
include "includeslocalhost.php"; //Conecta ao banco de dados

if(isset($_POST['txtLink'])) {
	//Pega variaveis vinda do formulário via POST
	foreach( $_POST as $campo => $vlr){
	   $$campo = AntiInjection($vlr);
	}
	$erro = 0;
	
	if(empty($txtNome)){
		$msg = $msg . "Nome inv&aacute;lido! <br>";
		$erro = $erro + 1;
	}
	if(empty($cmbCategoria)){
		$msg = $msg . "Categoria inv&aacute;lida! <br>";
		$erro = $erro + 1;
	}
	if(empty($txtLink)){
		$msg = $msg . "Link inv&aacute;lido! <br>";
		$erro = $erro + 1;
	}
	
	//Checa se não foram encontrados erros
	if($erro == 0){
	
		//Consulta para verificar itens idênticos
		$sqlverifica = "SELECT * FROM tblVideos WHERE Link = '" . $txtLink . "';";
		
		//Se já houver um registro igual			
		if(mysql_num_rows(mysql_query($sqlverifica)) > 0) {
			$msg = $msg . "J&aacute; existe um registro id&ecirc;ntico no sistema! <br>";
			$erro = $erro + 1;
		} else {
			$sql = "INSERT INTO tblVideos (Categoria, Nome, Descricao, Keywords, CaminhoVideo, Externo) VALUES(" . $cmbCategoria . ",'" . $txtNome . "','" . $txtDescricao . "','" . $txtKeywords .  "','" . $txtLink . "',1);";		
			//echo "<br>" . $sql . "<br>";
			$ask = mysql_query($sql);
			if ($ask==0){
				$msg = $msg . "Erro ao executar comando SQL! <br>";
				$erro = $erro + 1;
			}
		}
	}
	if($erro == 0){
		echo "<p><center>";
		echo "<strong>Cadastro concluído com sucesso!</strong>";
		echo "<p><a href='index.php'> Clique Aqui para retornar &agrave; p&aacute;gina inicial!</a></p></center>";
	} else {
		echo "<p><center><b>ERRO(s):</b><br>";
		echo $msg;
		echo "</center></p>";
	}
}
?><p><table width="100%" height="100%" align="center"><tr height="100%"><td align="center" valign="center" height="100%">
<form id="form1" name="form1" method="post" action="#"><div align="center">
  <table width="66%" border="1" cellspacing="0" cellpadding="0">
  <tr>
      <td colspan="2" nowrap="nowrap" class="headertabela"><div align="center" class="header">Cadastrar V&iacute;deo Externo</div>
        <div align="left"></div></td>
      </tr>
  <tr>
      <td width="184" nowrap="nowrap" class="headertabela"><div align="right">Nome:</div></td>
      <td width="300" bgcolor="#FFFFFF"><span class="style3">
        <input name="txtNome" type="text" id="txtNome" size="50" maxlength="255" />
      </span></td>
    </tr>
    <tr>
      <td width="184" nowrap="nowrap" class="headertabela"><div align="right">Categoria:</div></td>
      <td width="300" bgcolor="#FFFFFF"><div align="left">
        <select name="cmbCategoria" id="cmbCategoria" onchange="mudancaSelecao(this)">
          <option selected="selected" disabled="disabled">SELECIONE</option><?
          $sql = "SELECT * FROM tblCategoriaVideo ORDER BY Categoria;";
			$res = @mysql_query($sql);
			
			//Exibe as linhas encontradas na consulta
			while ($row = mysql_fetch_array($res)) {
				echo "<option value=" . $row['CodCategoria'];
				echo ">" . $row['Categoria'] . "</option>";
			 }
          ?>
        </select>
      </div></td>
    </tr>
    <tr>
      <td width="184" nowrap="nowrap" class="headertabela"><div align="right">Keywords:</div></td>
      <td width="300" bgcolor="#FFFFFF"><div align="left"><span class="style3">
        <input name="txtKeywords" type="text" id="txtKeywords" size="50" maxlength="255" />
      </span></div></td>
    </tr>
    <tr>
      <td width="184" nowrap="nowrap" class="headertabela"><div align="right">Link:</div></td>

      <td width="300" bgcolor="#FFFFFF"><div align="left"><span class="style3">
        <input name="txtLink" type="text" id="txtLink" size="50" maxlength="255" />
      </span></div></td>
    </tr>
    <tr>
      <td width="184" nowrap="nowrap" class="headertabela"><div align="right">Detalhes:</div></td>
      <td width="300" bgcolor="#FFFFFF"><div align="left">
        <textarea name="txtDescricao" cols="47" rows="5" id="txtDescricao"></textarea>
</div></td>
    </tr>

    
    <tr>
      <td height="23" colspan="4" class="headertabela"><div align="center">
        <input type="submit" name="submit" id="submit" value="Enviar" onclick="createURL()" />
      </div></td>
    </tr>
  </table>
  </div>
</form></td></tr></table>
</body>
</html>
