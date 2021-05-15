<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Inserir V&iacute;deo</title>
<link href="estilo.css" rel="stylesheet" type="text/css" />
</head>
<?
//Includes
include "includeslocalhost.php"; 

//Checagem da operação à ser executada
$Op = 1;

if (isset($_FILES['arquivo'])) {
	$Op = 2;
	
}
if (isset($_POST['txtNome'])) {
	$Op = 3;
}

//Faz a operação de Upload
if ($Op == 2) {
	//Zera as variáveis
	$erros = 0;
	$msg = "";
	
	//Strings necessárias
	$tamanhoMaximo = 100000000;
	$extensoes = array(".wmv", ".avi", ".flv", ".3gp", ".mpg", ".mpeg");
	$caminho = "uploads/videos/";
	$substituir = true;
	
	//Informações do arquivo enviado
	$nomeArquivo = $_FILES["arquivo"]["name"];
	$tamanhoArquivo = $_FILES["arquivo"]["size"];
	$nomeTemporario = $_FILES["arquivo"]["tmp_name"];
	
	//Trata o nome do arquivo
	$arquivo_minusculo = strtolower($nomeArquivo);
	$caracteres = array("ç","~","^","]","[","{","}",";",":","´",",",">","<","-","/","|","@","$","%","ã","â","á","à","é","è","ó","ò","+","=","*","&","(",")","!","#","?","`","ã"," ","©");
	$arquivo_tratado = str_replace($caracteres,"_",$arquivo_minusculo);
	
	//Faz as verificações
	if (!empty($nomeArquivo)) {
		//Verifica se o tamanho do arquivo é maior que o permitido
		if ($tamanhoArquivo > $tamanhoMaximo) {
			$msg = $msg . "O arquivo " . $nomeArquivo . " não deve ultrapassar " . $tamanhoMaximo. " bytes! <br>";
			$erros = $erros + 1;
		} 
		//Verifica se a extensão está entre as aceitas
		if (!in_array(strrchr($nomeArquivo, "."), $extensoes)) {
			$msg = $msg . "A extensão do arquivo <b>" . $nomeArquivo . "</b> não é válida! <br>";
			$erros = $erros + 1;
		} 
		//Verifica se o arquivo existe e se é para substituir
		if (file_exists($caminho . $arquivo_tratado) and !$substituir) {
			$msg = $msg . "O arquivo <b>" . $arquivo_tratado . "</b> já existe! <br>";
			$erros = $erros + 1;
		}
		// Move o arquivo para o caminho definido
		move_uploaded_file($nomeTemporario, ($caminho . $arquivo_tratado));
		
		//Define a string
		$Path = $caminho . $arquivo_tratado;
	}	
}

//Faz a operação de Cadastro
if ($Op == 3) {
	//Pega os valores do POST
	foreach( $_POST as $campo => $vlr){
	   $$campo = AntiInjection($vlr);
	}
	
	//Zera as variáveis
	$erros = 0;
	$msg = "";
	
	//Consulta para verificar itens idênticos
	$sqlverifica = "SELECT * FROM tblVideos WHERE CaminhoVideo = '" . $txtCaminho . "';";		
	if(mysql_num_rows(mysql_query($sqlverifica)) > 0) {
		$msg = $msg . "J&aacute; existe um registro id&ecirc;ntico no sistema! <br>";
		$erros = $erros + 1;
	} else {
		//Faz o cadastro
		$sql = "INSERT INTO tblVideos (Categoria, Nome, Descricao, Keywords, CaminhoVideo, Externo) VALUES(" . $cmbCategoria . ",'" . $txtNome . "','" . $txtDescricao . "','" . $txtKeywords .  "','" . $txtCaminho . "',0);";		
		//echo "<br>" . $sql . "<br>";
		$ask = mysql_query($sql);
		if ($ask==0){
			$msg = $msg . "Erro ao executar comando SQL! <br>";
			$erros = $erros + 1;
		}
	}
}
?>
<body>
<? if($Op == 1) { ?>
<form id="form2" name="form2" method="post" action="#" enctype="multipart/form-data"><div align="center">
  <table width="100%" height="100%" align="center"><tr height="100%"><td align="center" valign="center" height="100%"><table width="47%" border="1" cellspacing="0" cellpadding="0">
  <tr>
      <td colspan="2" class="headertabela"><div align="center" class="header">Cadastrar V&iacute;deo
      </div></td>
      </tr>
    <tr>
      <td width="263" height="27" nowrap="nowrap" class="headertabela"><div align="right">Selecione o v&iacute;deo:</div></td>
      <td width="273" bgcolor="#FFFFFF"><div align="left">
        <input type="file" name="arquivo" id="arquivo" />
      </div></td>
    </tr>

    <tr>
      <td colspan="4" class="headertabela"><div align="center">*Tamanho m&aacute;ximo por arquivo: <strong>100mb</strong></div></td>
    </tr>
    <tr>
      <td height="23" colspan="4" class="headertabela"><div align="center">
        <input type="submit" name="submit" id="submit" value="Enviar"/>
      </div></td>
    </tr>
  </table></td>
    </tr>
</table>
  </div>
</form>
<? } elseif ($Op == 2) { 
		if ($erros == 0) { ?>
<form id="form1" name="form1" method="post" action="#"><div align="center">
  <table width="66%" border="1" cellspacing="0" cellpadding="0">
  <tr>
      <td colspan="2" nowrap="nowrap" class="headertabela"><div align="center" class="header">Cadastrar V&iacute;deo</div>
        <div align="left"></div></td>
      </tr>
  <tr>
      <td width="184" nowrap="nowrap" class="headertabela"><div align="right">V&iacute;deo:</div></td>
      <td width="300" bgcolor="#FFFFFF"><span class="style3"><? echo $Path; ?>
        <input name="txtCaminho" type="hidden" id="txtCaminho" size="50" maxlength="255" value="<? echo $Path; ?>" />
      </span></td>
    </tr>
    <tr>
      <td width="184" nowrap="nowrap" class="headertabela"><div align="right">Nome:</div></td>
      <td width="300" bgcolor="#FFFFFF"><span class="style3">
        <input name="txtNome" type="text" id="txtNome" size="50" maxlength="255" />
      </span></td>
    </tr>
    <tr>
    <tr>
      <td width="184" nowrap="nowrap" class="headertabela"><div align="right">Categoria:</div></td>
      <td width="300" bgcolor="#FFFFFF"><div align="left">
        <select name="cmbCategoria" id="cmbCategoria">
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
      <td width="184" nowrap="nowrap" class="headertabela"><div align="right">Detalhes:</div></td>
      <td width="300" bgcolor="#FFFFFF"><div align="left">
        <textarea name="txtDescricao" cols="47" rows="5" id="txtDescricao"></textarea>
</div></td>
    </tr>
    <tr>
      <td height="23" colspan="4" class="headertabela"><div align="center">
        <input type="submit" name="submit" id="submit" value="Enviar" />
      </div></td>
    </tr>
  </table>
  </div>
</form>
<? 	} else {
		echo "<p><center>ERRO(s):<br>";
		echo $msg;
		echo "</center></p>";
	}
} elseif ($Op == 3) { 
	if ($erros == 0) { ?>
    	<p><center><strong>Cadastro conclu&iacute;do com sucesso!</strong>
		<p><a href='index.php'> Clique Aqui para retornar &agrave; p&aacute;gina inicial!</a></p></center>
<? 	} else {
		echo "<p><center>ERRO(s):<br>";
		echo $msg;
		echo "</center></p>";
	}
} ?>
</body>
</html>
