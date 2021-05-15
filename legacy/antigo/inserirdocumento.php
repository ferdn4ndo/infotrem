<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />
<title>Inserir Documento</title>
<link href="estilo.css" rel="stylesheet" type="text/css" />
</head><?
//Includes
include "includeslocalhost.php"; 

//Checagem da opera��o � ser executada
$Op = 1;
if (isset($_FILES['arquivo'])) {
	$Op = 2;
	
}
if (isset($_POST['txtNome'])) {
	$Op = 3;
}

//Faz a opera��o de Upload
if ($Op == 2) {
	//Zera as vari�veis
	$erros = 0;
	$msg = "";
	
	//Strings necess�rias
	$tamanhoMaximo = 200000000;
	$extensoes = array(".gif", ".jpg", ".jpeg", ".bmp", ".png", ".pdf", ".txt", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".pps", ".gif", ".bmp", ".jpeg", ".jpg", ".png", ".cdr", ".dwg", ".zip", ".rar", ".eml", ".htm", ".html", ".exe", ".kmz");
	$caminho = "uploads/documentos/";
	$substituir = true;
	
	//Informa��es do arquivo enviado
	$nomeArquivo = $_FILES["arquivo"]["name"];
	$tamanhoArquivo = $_FILES["arquivo"]["size"];
	$nomeTemporario = $_FILES["arquivo"]["tmp_name"];
	
	//Tira os espa�os
	$arquivo_tratado_espaco = str_replace(" ","",$nomeArquivo);
		
	//Tira os demais caracteres inv�lidos
	$caracteres = array("�","�","~","^","]","[","{","}",";",":","�",",",">","<","/","|","@","$","%","�","�","�","�","�","�","�","�","�","�","�","�","�","�","�","�","�","�","�","�","�","�","�","�","�","�","�","�","�","�","�","�","+","=","*","&","(",")","!","#","?","`"," ","�");
	$arquivo_tratado = str_replace($caracteres,"_",$arquivo_tratado_espaco);
	
	// Pega a extens�o do arquivo
	$tipoarquivo = RetornaTipoArquivo($nomeArquivo);
	
	//Faz as verifica��es
	if (!empty($nomeArquivo)) {
		//Verifica se o tamanho do arquivo � maior que o permitido
		if ($tamanhoArquivo > $tamanhoMaximo) {
			$msg = $msg . "O arquivo " . $nomeArquivo . " n�o deve ultrapassar " . $tamanhoMaximo. " bytes! <br>";
			$erros = $erros + 1;
		} 
		//Verifica se a extens�o est� entre as aceitas
		if (!in_array(strrchr(strtolower($nomeArquivo), "."), $extensoes)) {
			$msg = $msg . "A extens�o do arquivo <b>" . $nomeArquivo . "</b> n�o � v�lida! <br>";
			$erros = $erros + 1;
		} 
		//Verifica se o arquivo existe e se � para substituir
		if (file_exists($caminho . $arquivo_tratado) and !$substituir) {
			$msg = $msg . "O arquivo <b>" . $arquivo_tratado . "</b> j� existe! <br>";
			$erros = $erros + 1;
		}
		
		// Se n�o houver erro
		if ($erros==0) {
			// Move o arquivo para o caminho definido
			move_uploaded_file($nomeTemporario, ($caminho . $arquivo_tratado));
		}
		
		//Define a string
		$Path = $caminho . $arquivo_tratado;
	}	
}

//Faz a opera��o de Cadastro
if ($Op == 3) {
	//Pega os valores do POST
	foreach( $_POST as $campo => $vlr){
	   $$campo = AntiInjection($vlr);
	}
	
	//Zera as vari�veis
	$erros = 0;
	$msg = "";
	
	//Consulta para verificar itens id�nticos
	$sqlverifica = "SELECT * FROM tblDocumentos WHERE Caminho = '" . $txtCaminho . "';";		
	if(mysql_num_rows(mysql_query($sqlverifica)) > 0) {
		$msg = $msg . "J&aacute; existe um registro id&ecirc;ntico no sistema! <br>";
		$erros = $erros + 1;
	} else {
		//Faz o cadastro
		$sql = "INSERT INTO tblDocumentos (Categoria, Nome, Keywords, Caminho, Detalhes) VALUES(" . $cmbCategoria . ",'" . $txtNome . "','" . $txtKeywords . "','" . $txtCaminho .  "','" . $txtDetalhes . "');";		
		//echo "<br>" . $sql . "<br>";
		$ask = mysql_query($sql);
		if ($ask==0){
			$msg = $msg . "Erro ao executar comando SQL! <br>";
			$erros = $erros + 1;
		}
	}
}
?><body>
<? if($Op == 1) { ?>
<form id="form1" name="form1" method="post" action="#" enctype="multipart/form-data"><div align="center">
  <table width="100%" align="center"><tr height="100%"><td align="center" valign="center" height="100%"><table width="47%" border="1" cellspacing="0" cellpadding="0">
  <tr>
      <td colspan="2" class="headertabela"><div align="center" class="header">Cadastrar Documento
      </div></td>
      </tr>
    <tr>
      <td width="263" height="27" nowrap="nowrap" class="headertabela"><div align="right">Selecione o documento:</div></td>
      <td width="273" bgcolor="#FFFFFF"><div align="left">
        <input type="file" name="arquivo" id="arquivo" />
      </div></td>
    </tr>

    <tr>
      <td colspan="4" class="headertabela"><div align="center">*Tamanho m&aacute;ximo por arquivo: <strong>20mb</strong></div></td>
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
<form id="form2" name="form2" method="post" action="#"><div align="center">
  <table width="100%" border="0" cellspacing="1" cellpadding="1" align="center"><tr><td align="center"><table width="66%" border="1" cellspacing="0" cellpadding="0">
  <tr>
      <td colspan="2" nowrap="nowrap" class="headertabela"><div align="center" class="header">Cadastrar Documento - BD</div>
        <div align="left"></div></td>
      </tr>
  <tr>
      <td width="184" nowrap="nowrap" class="headertabela"><div align="right">Documento:</div></td>
      <td width="300" bgcolor="#FFFFFF"><span class="style3"><? echo $Path; ?>
        <input name="txtCaminho" type="hidden" id="txtCaminho" size="50" maxlength="255" value="<? echo $Path; ?>" />
      </span></td>
    </tr>
    <tr>
      <td width="184" nowrap="nowrap" class="headertabela"><div align="right">Categoria:</div></td>
      <td width="300" bgcolor="#FFFFFF"><div align="left">
        <select name="cmbCategoria" id="cmbCategoria">
          <option disabled="disabled" selected="selected">SELECIONE</option>
          <?
			$sql = "SELECT CodCategoria, Categoria FROM tblCategoriaDocumento ORDER BY Categoria;";
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
      <td width="184" nowrap="nowrap" class="headertabela"><div align="right">Nome:</div></td>
      <td width="300" bgcolor="#FFFFFF"><div align="left"><span class="style3">
        <input name="txtNome" type="text" id="txtNome" size="50" maxlength="255" />
      </span></div></td>
    </tr><tr>
      <td width="184" nowrap="nowrap" class="headertabela"><div align="right">Keywords:</div></td>
      <td width="300" bgcolor="#FFFFFF"><div align="left"><span class="style3">
        <input name="txtKeywords" type="text" id="txtKeywords" size="50" maxlength="255" />
      </span></div></td>
    </tr>
    <tr>
      <td width="184" nowrap="nowrap" class="headertabela"><div align="right">Detalhes:</div></td>
      <td width="300" bgcolor="#FFFFFF"><div align="left">
        <textarea name="txtDetalhes" cols="47" rows="5" id="txtDetalhes"></textarea>
        <input type="hidden" name="txtPath" id="txtPath" value="<? echo $caminho . $arquivo_tratado; ?>" /></div></td>
    </tr>

    
    <tr>
      <td height="23" colspan="4" class="headertabela"><div align="center">
        <input type="submit" name="submit" id="submit" value="Enviar" />
      </div></td>
    </tr>
  </table></td>
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
