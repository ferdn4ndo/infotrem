<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
<title>Inserir Foto</title>
<script type="text/javascript">
  // Função personalizada que é chamada sempre que
  // houver uma mudança de item no elemento select
  // Note que a função recebe, como argumento, o elemento
  // select no qual o evento onchange foi disparado 
  function mudancaSelecao(elemento){
    // vamos obter a opção selecionada
    var selecionada = elemento.options[elemento.options.selectedIndex];

    // vamos exibir o texto da opção selecionada
    //window.alert("Texto da opção: " + selecionada.text);

    // vamos exibir o valor da opção selecionada
    //window.alert("Valor da opção: " + selecionada.value);
	
	document.location=('inserirfoto2.php?Categoria=' + selecionada.value + "&CaminhoFoto='" + document.getElementById("txtPath").value + "'");
	
  }
</script>
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

$path2 = $_GET["CaminhoFoto"];
$id = $_GET["Categoria"];
$caracteres = array("'","\"","\\");
$path = str_replace($caracteres,"",$path2);

// Tamanho máximo do arquivo (em bytes)
$tamanhoMaximo = 10000000;
// Extensões aceitas
$extensoes = array(".gif", ".jpg", ".jpeg", ".bmp", ".png");
// Caminho para onde o arquivo será enviado
$caminho = "uploads/fotos/";
// Substituir arquivo já existente (true = sim; false = nao)
$substituir = true;
// Contador de erros
$erros = 0;
 

 
	// Informações do arquivo enviado
	$nomeArquivo = $_FILES["arquivo"]["name"];
	$tamanhoArquivo = $_FILES["arquivo"]["size"];
	$nomeTemporario = $_FILES["arquivo"]["tmp_name"];
	
	
	$arquivo_minusculo = strtolower($nomeArquivo);
	$caracteres = array("ç","~","^","]","[","{","}",";",":","´",",",">","<","-","/","|","@","$","%","ã","â","á","à","é","è","ó","ò","+","=","*","&","(",")","!","#","?","`","ã"," ","©");
	$arquivo_tratado = str_replace($caracteres,"_",$arquivo_minusculo);
	
	// Verifica se o nome do arquivo foi modificado
	if ($nomeArquivo != $arquivo_tratado) {
		$nomeModificado = true;
	} else {
		$nomeModificado = false;
	}
	
	// Pega a extensão do arquivo
	switch (strrchr($nomeArquivo, ".")) {
		case ".pdf":
			$tipoarquivo = 0;
			break;
		case ".txt":
			$tipoarquivo = 1;
			break;
		case ".doc":
			$tipoarquivo = 2;
			break;
		case ".docx":
			$tipoarquivo = 2;
			break;
			
	} 
	echo $tipoarquivo;
	
	// Verifica se o arquivo foi colocado no campo
	if (!empty($nomeArquivo)) {
 
		$erro = false;
 
		// Verifica se o tamanho do arquivo é maior que o permitido
		if ($tamanhoArquivo > $tamanhoMaximo) {
			$erro = "O arquivo " . $nomeArquivo . " não deve ultrapassar " . $tamanhoMaximo. " bytes";
			$erros = $erros + 1;
		} 
		// Verifica se a extensão está entre as aceitas
		elseif (!in_array(strrchr($nomeArquivo, "."), $extensoes)) {
			$erro = "A extensão do arquivo <b>" . $nomeArquivo . "</b> não é válida";
			$erros = $erros + 1;
		} 
		// Verifica se o arquivo existe e se é para substituir
		elseif (file_exists($caminho . $arquivo_tratado) and !$substituir) {
			$erro = "O arquivo <b>" . $arquivo_tratado . "</b> já existe";
			$erros = $erros + 1;
		}
 
		// Se não houver erro
		/*
		if (!$erro) {
		
			// Prepara as variáveis para a instrução SQL
			$index = $i + 1;
			$x = "nome" . $index;
			$nome = $_GET[$x];
			$completo = $caminho . $arquivo_tratado;
			$data = date("Y-m-d");
			
			// Prepara a instrução SQL
			$sql = "INSERT INTO tblArquivos (TipoArquivo, CodEvento, NomeArquivo, CaminhoArquivo, DataEnvio) VALUES(" . $tipoarquivo . "," . $codEvento . ",'" . $nome . "','" . $completo .  "','" . $data . "');";
			
			// Executa a instrução SQL
			$ask = mysqlexecuta($id,$sql);
			If ($ask=0){
				$erros = $erros + 1;
				echo "Erro ao interpretar instrução SQL!";
			}
			
			// Caso a instrução SQL também ocorra sem problemas
			if ($erros == 0) { */
		
				// Move o arquivo para o caminho definido
				move_uploaded_file($nomeTemporario, ($caminho . $arquivo_tratado));
				/*
				// Mensagem de sucesso
				echo "O arquivo <b>".$nomeArquivo."</b> foi enviado com sucesso. <br />";
				
				// Mensagem caso o nome do arquivo tenha sido modificado
				if ($nomeModificado) {
					echo "Para melhor adequação ao sistema web, <b>" . $nomeArquivo . "</b> foi renomeado para <b>" . $arquivo_tratado . "</b><br />";
				}
							
				// Mensagem informando o endereço do arquivo
				echo "Seu endereço agora é: <b><a href='" . $caminho . $arquivo_tratado . "'>" . $caminho . $arquivo_tratado . "</a></b><br /><br />";
			*/
			//}
			
		//} 
		// Se houver erro
		//else {
			// Mensagem de erro
			//echo $erro . "<br />";
		//}
	}

if ($erros == 0) {
/*
	// Mensagem de redirecionamento
	echo "Redirecionando para página principal... <br>Caso não redirecione automaticamente, <a href='index.php'> Clique Aqui!</a>";
	echo '<script type="text/javascript">';
	echo 'var t=setTimeout("redir()",5000);';
	echo 'function redir()';
	echo '{';
	echo "document.location=('index.php');";
	echo '}';
	echo '</script>';
	*/
}


?>
<form id="form1" name="form1" method="post" action="inserirfoto3.php" enctype="multipart/form-data"><div align="center">
  <table width="100%" border="0" cellspacing="1" cellpadding="1" align="center"><tr><td align="center"><table width="66%" border="1" cellspacing="0" cellpadding="0">
  <tr>
      <td colspan="2" nowrap="nowrap" class="headertabela"><div align="center" class="header">Cadastrar Foto - BD</div>
        <div align="left"></div></td>
      </tr>
  <tr>
      <td width="184" nowrap="nowrap" class="headertabela"><div align="right">Foto:</div></td>
      <td width="300" bgcolor="#FFFFFF"><div align="center"><img src="<? 
if ($path != "") {
	echo $path;
	$tamanhos = getimagesize($path);
} else {
	echo $caminho . $arquivo_tratado;
	$tamanhos = getimagesize($caminho . $arquivo_tratado);
}
//Calcula altura e largura
$largura = intval(($tamanhos[1] * 96)/225);
$altura = intval(($tamanhos[0] * 70)/300);

?>" width="<? echo $largura; ?>" height="<? echo $altura; ?>"/></div></td>
    </tr>
    <tr>
      <td width="184" nowrap="nowrap" class="headertabela"><div align="right">Categoria:</div></td>
      <td width="300" bgcolor="#FFFFFF"><div align="left">
        <select name="cmbCategoria" id="cmbCategoria" onchange="mudancaSelecao(this)">
          <option selected="selected"<? if ($id == "") { echo " selected='selected' "; } ?>disabled="disabled">SELECIONE</option>
          <option value="1"<? if ($id == "1") { echo " selected='selected' "; } ?>>1 - Locomotivas</option>
          <option value="2"<? if ($id == "2") { echo " selected='selected' "; } ?>>2 - Vag&otilde;es</option>
          <option value="3"<? if ($id == "3") { echo " selected='selected' "; } ?>>3 - Carros de Passageiro</option>
          <option value="4"<? if ($id == "4") { echo " selected='selected' "; } ?>>4 - Autos de linha</option>
          <option value="5"<? if ($id == "5") { echo " selected='selected' "; } ?>>5 - Outros</option>
        </select>
      </div></td>
    </tr>
    <tr>
      <td width="184" nowrap="nowrap" class="headertabela"><div align="right">Modelo:</div></td>
      <td width="300" bgcolor="#FFFFFF"><div align="left">
        <select name="cmbModelo" id="cmbModelo">
          <?
	   if ($id != "") {
			$sql = "SELECT CodModelo, Modelo FROM tblModelos WHERE Categoria = " . $id . " ORDER BY Modelo;";
			$res = @mysql_query($sql);
			
			//Exibe as linhas encontradas na consulta
			while ($row = mysql_fetch_array($res)) {
				echo "<option value=" . $row['CodModelo'];
				echo ">" . $row['Modelo'] . "</option>";
			 }
		}
	 ?>
        </select>
      </div></td>
    </tr>
    <tr>
      <td width="184" nowrap="nowrap" class="headertabela"><div align="right">Numero:</div></td>
      <td width="300" bgcolor="#FFFFFF"><div align="left"><span class="style3">
        <input name="txtNumero" type="text" id="txtNumero" size="10" maxlength="6" />
      </span></div></td>
    </tr>
    <tr>
      <td width="184" nowrap="nowrap" class="headertabela"><div align="right">Ferrovia:
        
      </div></td>
      <td width="300" bgcolor="#FFFFFF"><select name="cmbFerrovia" id="cmbFerrovi">
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
      <td width="184" nowrap="nowrap" class="headertabela"><div align="right">Local:</div></td>
      <td width="300" bgcolor="#FFFFFF"><div align="left">
        <select name="cmbLocal" id="cmbLocal">
          <option>-</option>
          <?
			$sql = "SELECT CodLocal, Sigla, Municipio, UF FROM tblLocais ORDER BY Sigla;";
			$res = @mysql_query($sql);
			
			//Exibe as linhas encontradas na consulta
			while ($row = mysql_fetch_array($res)) {
				echo "<option value=" . $row['CodLocal'];
				echo ">" . $row['Sigla'] . " - " . $row['Municipio'] . " (" . $row['UF'] . ")</option>";
			 }
	 ?>
        </select>
      </div></td>
    </tr>
    <tr>
      <td width="184" nowrap="nowrap" class="headertabela"><div align="right">Data:</div></td>
      <td width="300" bgcolor="#FFFFFF"><div align="left"><span class="style3">
        <input name="txtData" type="text" id="txtData" size="10" maxlength="10" />
      </span></div></td>
    </tr><tr>
      <td width="184" nowrap="nowrap" class="headertabela"><div align="right">Autor:</div></td>
      <td width="300" bgcolor="#FFFFFF"><div align="left"><span class="style3">
        <input name="txtAutor" type="text" id="txtAutor" size="50" maxlength="30" />
      </span></div></td>
    </tr>
    <tr>
      <td width="184" nowrap="nowrap" class="headertabela"><div align="right">Detalhes:</div></td>
      <td width="300" bgcolor="#FFFFFF"><div align="left">
        <textarea name="txtDetalhes" cols="47" rows="5" id="txtDetalhes"></textarea>
        <span class="style2">
        <input type="hidden" name="txtPath" id="txtPath" value="<? 
	if ($path != "") {
	echo $path;
} else {
	echo $caminho . $arquivo_tratado;
}
?>" />
        </span></div></td>
    </tr>

    
    <tr>
      <td height="23" colspan="4" class="headertabela"><div align="center">
        <input type="submit" name="submit" id="submit" value="Enviar" onclick="createURL()" />
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
