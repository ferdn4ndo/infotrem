<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
<title>Inserir Documento</title>
<link href="estilo.css" rel="stylesheet" type="text/css" />
</head>
<body>
<?
//Includes
include "includeslocalhost.php"; //Conecta ao banco de dados

//Pega variaveis vinda do formulário via POST
foreach( $_POST as $campo => $vlr){
   $$campo = AntiInjection($vlr);
}

//Tamanho máximo do arquivo (em bytes)
$tamanhoMaximo = 20000000;
//Extensões aceitas
$extensoes = array(".gif", ".jpg", ".jpeg", ".bmp", ".png", ".pdf", ".txt", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".pps", ".gif", ".bmp", ".jpeg", ".jpg", ".png", ".cdr", ".dwg", ".zip", ".rar", ".eml", ".htm", ".html", ".exe");
//Caminho para onde o arquivo será enviado
$caminho = "uploads/documentos/";
//Substituir arquivo já existente (true = sim; false = nao)
$substituir = true;
//Contador de erros
$erros = 0;
 
//Informações do arquivo enviado
$nomeArquivo = $_FILES["arquivo"]["name"];
$tamanhoArquivo = $_FILES["arquivo"]["size"];
$nomeTemporario = $_FILES["arquivo"]["tmp_name"];

//Converte o nome para minúsculo
//$arquivo_minusculo = strtolower($nomeArquivo);

//Tira os espaços
$arquivo_tratado_espaco = str_replace(" ","",$arquivo_minusculo);
	
//Tira os demais caracteres inválidos
$caracteres = array("ç","Ç","~","^","]","[","{","}",";",":","´",",",">","<","/","|","@","$","%","ã","Ã","â","Â","á","Á","à","À","é","É","è","È","ê","Ê","í","Í","î","Î","ó","Ó","ò","Ò","ô","Ô","ú","Ú","ù","Ù","û","Û","ü","Ü","+","=","*","&","(",")","!","#","?","`"," ","©");
$arquivo_tratado = str_replace($caracteres,"_",$arquivo_tratado_espaco);

// Verifica se o nome do arquivo foi modificado
if ($nomeArquivo != $arquivo_tratado) {
	$nomeModificado = true;
} else {
	$nomeModificado = false;
}
	
// Pega a extensão do arquivo
$tipoarquivo = RetornaTipoArquivo($nomeArquivo);
	
// Verifica se o arquivo foi colocado no campo
if (!empty($nomeArquivo)) {
 
	$erro = "";
 
	// Verifica se o tamanho do arquivo é maior que o permitido
	if ($tamanhoArquivo > $tamanhoMaximo) {
		$erro = "O arquivo " . $nomeArquivo . " não deve ultrapassar " . $tamanhoMaximo. " bytes";
		$erros = $erros + 1;
	}
	 
	// Verifica se a extensão está entre as aceitas
	elseif (!in_array(strrchr(strtolower($nomeArquivo), "."), $extensoes)) {
		$erro = "A extensão do arquivo <b>" . $nomeArquivo . "</b> não é válida";
		$erros = $erros + 1;
	} 
	
	// Verifica se o arquivo existe e se é para substituir
	elseif (file_exists($caminho . $arquivo_tratado) and !$substituir) {
		$erro = "O arquivo <b>" . $arquivo_tratado . "</b> já existe";
		$erros = $erros + 1;
	}
 
	// Se não houver erro
	if ($erro=="") {

		// Move o arquivo para o caminho definido
		move_uploaded_file($nomeTemporario, ($caminho . $arquivo_tratado));
		
	}
}
?>
<form id="form1" name="form1" method="post" action="inserirdocumento3.php"><div align="center">
  <table width="100%" border="0" cellspacing="1" cellpadding="1" align="center"><tr><td align="center"><table width="66%" border="1" cellspacing="0" cellpadding="0">
  <tr>
      <td colspan="2" nowrap="nowrap" class="headertabela"><div align="center" class="header">Cadastrar Documento - BD</div>
        <div align="left"></div></td>
      </tr>
  <tr>
      <td width="184" nowrap="nowrap" class="headertabela"><div align="right">Documento:</div></td>
      <td width="300" bgcolor="#FFFFFF"><div align="center"><a href='<? echo $caminho . $arquivo_tratado; ?>' target="_blank"><? echo $caminho . $arquivo_tratado; ?></a></div></td>
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
<p align="center">&nbsp;</p>
</body>
</html>
