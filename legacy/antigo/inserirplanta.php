<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />
<title>Inserir Foto</title>
<link href="estilo.css" rel="stylesheet" type="text/css" />
<script type="text/javascript">
  function mudancaSelecao(elemento){
    var selecionada = elemento.options[elemento.options.selectedIndex];
	document.location=('inserirplanta.php?Categoria=' + selecionada.value + "&CaminhoPlanta=" + document.getElementById("txtPath").value);	
  }
</script>
</head><body><?
//Includes
include "includeslocalhost.php"; 

//Pega a categoria
$id = $_GET["Categoria"];

//Checagem da operação à ser executada
$Op = 1;
if (isset($_FILES['arquivo']) || isset($_GET['CaminhoPlanta'])) {
	$Op = 2;
	
}
if (isset($_POST['txtPath'])) {
	$Op = 3;
}

if (isset($_GET['CaminhoPlanta'])) {
	$Path = $_GET['CaminhoPlanta'];
}

//Faz a operação de Upload
if ($Op == 2) {
	//Zera as variáveis
	$erros = 0;
	$msg = "";
	
	//Strings necessárias
	$tamanhoMaximo = 10 * 1024 * 1024; //10MB
	$extensoes = array(".gif", ".jpg", ".jpeg", ".bmp", ".png", ".cdr", ".dwg", ".pdf");
	$caminho = "uploads/plantas/";
	$substituir = true;
	
	//Informações do arquivo enviado
	$nomeArquivo = $_FILES["arquivo"]["name"];
	$tamanhoArquivo = $_FILES["arquivo"]["size"];
	$nomeTemporario = $_FILES["arquivo"]["tmp_name"];
	
	//Substitui os separadores para o sistema de nomenclatura que utilizo
	$arquivo_tratado_sep = str_replace(" - ","_",$nomeArquivo);
	
	//Tira os espaços
	$arquivo_tratado_espaco = str_replace(" ","",$arquivo_tratado_sep);
		
	//Tira os demais caracteres inválidos
	$caracteres = array("ç","Ç","~","^","]","[","{","}",";",":","´",",",">","<","/","|","@","$","%","ã","Ã","â","Â","á","Á","à","À","é","É","è","È","ê","Ê","í","Í","î","Î","ó","Ó","ò","Ò","ô","Ô","ú","Ú","ù","Ù","û","Û","ü","Ü","+","=","*","&","(",")","!","#","?","`"," ","©");
	$arquivo_tratado = str_replace($caracteres,"_",$arquivo_tratado_espaco);
	
	// Pega a extensão do arquivo
	$tipoarquivo = RetornaTipoArquivo($nomeArquivo);
	
	//Faz as verificações
	if (!empty($nomeArquivo)) {
		//Verifica se o tamanho do arquivo é maior que o permitido
		if ($tamanhoArquivo > $tamanhoMaximo) {
			$msg = $msg . "O arquivo " . $nomeArquivo . " não deve ultrapassar " . $tamanhoMaximo. " bytes! <br>";
			$erro = $erro + 1;
		} 
		//Verifica se a extensão está entre as aceitas
		if (!in_array(strrchr(strtolower($nomeArquivo), "."), $extensoes)) {
			$msg = $msg . "A extensão do arquivo <b>" . $nomeArquivo . "</b> não é válida! <br>";
			$erro = $erro + 1;
		} 
		//Verifica se o arquivo existe e se é para substituir
		if (file_exists($caminho . $arquivo_tratado) and !$substituir) {
			$msg = $msg . "O arquivo <b>" . $arquivo_tratado . "</b> já existe! <br>";
			$erro = $erro + 1;
		}
		
		// Se não houver erro
		if ($erros==0) {
			// Move o arquivo para o caminho definido
			move_uploaded_file($nomeTemporario, ($caminho . $arquivo_tratado));
		}
		
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
	
	//Faz as verificações
	if(empty($cmbCategoria)){
		$msg = $msg . "Categoria inv&aacute;lida! <br>";
		$erro = $erro + 1;
	}
	if(empty($cmbModelo)){
		$msg = $msg . "Modelo inv&aacute;lido! <br>";
		$erro = $erro + 1;
	}
	if(empty($txtNumeroInicial)){
		$msg = $msg ."N&uacute;mero Inicial inv&aacute;lido! <br>";
		$erro = $erro + 1;
	} elseif (!is_numeric($txtNumeroInicial)){
		$msg = $msg ."N&uacute;mero Inicial n&atilde;o &eacute; num&eacute;rico! <br>";
		$erro = $erro + 1;
	}
	if(empty($txtNumeroFinal)){
		$msg = $msg ."N&uacute;mero Final inv&aacute;lido! <br>";
		$erro = $erro + 1;
	} elseif (!is_numeric($txtNumeroFinal)){
		$msg = $msg ."N&uacute;mero Final n&atilde;o &eacute; num&eacute;rico! <br>";
		$erro = $erro + 1;
	}
	if((!empty($txtNumeroInicial)) && (!empty($txtNumeroFinal))) {
		if($txtNumeroFinal < $txtNumeroInicial){
			$msg = $msg ."N&uacute;mero Final deve ser maior ou igual ao N&uacute;mero Inicial! <br>";
			$erro = $erro + 1;
		}
	}
	if(empty($txtPath)){
		$msg = $msg . "Caminho da planta inv&aacute;lido! <br>";
		$erro = $erro + 1;
	}

	if($erro == 0){
		//Consulta para verificar itens idênticos
		$sqlverifica = "SELECT * FROM tblPlantas WHERE CaminhoPlanta = '" . $txtPath . "';";
		
		if(mysql_num_rows(mysql_query($sqlverifica)) > 0) { //Se já houver um registro igual
			$msg = $msg . $Mensagem['erroduplicado'];
			$erro = $erro + 1;
		} else {
			$sql = "INSERT INTO tblPlantas (Categoria, CodModelo, NumCatInicial, NumCatFinal, Detalhes, CaminhoPlanta) VALUES(" . $cmbCategoria . "," . $cmbModelo . "," . $txtNumeroInicial . "," . $txtNumeroFinal . ",'" . $txtDetalhes . "','" . $txtPath . "');";
			
			$ask = mysql_query($sql);
			if ($ask==0){
				$msg = $msg . $Mensagem['erro'];
				$erro = $erro + 1;
			}
		}
	}
}
?><? if($Op == 1) { ?>
<form id="form1" name="form1" method="post" action="#" enctype="multipart/form-data"><div align="center">
  <table width="100%" height="480" align="center"><tr height="100%"><td align="center" valign="center" height="100%"><table width="47%" border="1" cellspacing="0" cellpadding="0">
  <tr>
      <td colspan="2" class="headertabela"><div align="center" class="header">Cadastrar Planta
      </div></td>
      </tr>
    <tr>
      <td width="263" height="27" nowrap="nowrap" class="headertabela"><div align="right">Selecione a planta:</div></td>
      <td width="273" bgcolor="#FFFFFF"><div align="left">
        <input type="file" name="arquivo" id="arquivo" />
      </div></td>
    </tr>

    <tr>
      <td colspan="4" class="headertabela"><div align="center">*Tamanho m&aacute;ximo por arquivo: <strong>10mb</strong></div></td>
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
  <table width="100%" border="0" cellspacing="1" cellpadding="1" align="center"><tr><td align="center"><table width="66%" border="1" cellspacing="0" cellpadding="0">
  <tr>
      <td colspan="2" nowrap="nowrap" class="headertabela"><div align="center" class="header">Cadastrar Planta - BD</div>
        <div align="left"></div></td>
      </tr>
  <tr>
      <td width="184" nowrap="nowrap" class="headertabela"><div align="right">Planta:</div></td>
      <td width="300" bgcolor="#FFFFFF"><div align="center"><img src="<?
	//Verifica o tipo de arquivo
	$tipo = strrchr(strtolower($nomeArquivo), ".");
	if ($tipo==".cdr") {
		echo "images/cdr128.png";
		$largura = 128;
		$altura = 128;
	} elseif ($tipo==".dwg") {
		echo "images/dwg128.png";
		$largura = 128;
		$altura = 128;
	} elseif ($tipo==".pdf") {
		echo "images/pdf128.png";
		$largura = 128;
		$altura = 128;
	} else {
		if ($Path != "") {
			echo $Path;
			$tamanhos = getimagesize($Path);
		} else {
			echo $caminho . $arquivo_tratado;
			$tamanhos = getimagesize($caminho . $arquivo_tratado);
		}
		//Calcula altura e largura
		$largura = intval(($tamanhos[1] * 96)/225);
		$altura = intval(($tamanhos[0] * 70)/300);
	}

?>" width="<? echo $largura; ?>" height="<? echo $altura; ?>"/></div></td>
    </tr>
    <tr>
      <td width="184" nowrap="nowrap" class="headertabela"><div align="right">Categoria:</div></td>
      <td width="300" bgcolor="#FFFFFF"><div align="left">
        <select name="cmbCategoria" id="cmbCategoria" onchange="mudancaSelecao(this)">
        <option<? if ($id == "") { echo " selected='selected' "; } ?>disabled="disabled">SELECIONE</option>
        <?
			$sql = "SELECT CodCategoria, Categoria FROM tblCategoriaRodante ORDER BY CodCategoria;";
			$res = @mysql_query($sql);
			
			//Exibe as linhas encontradas na consulta
			while ($row = mysql_fetch_array($res)) {
				echo "<option value=" . $row['CodCategoria'];
				if ($id == $row['CodCategoria']) { echo " selected='selected'"; }
				echo ">" . $row['CodCategoria'] . " - " . $row['Categoria'] . "</option>";
			 }
	 ?>
        </select>
      </div></td>
    </tr>
    <tr>
      <td width="184" nowrap="nowrap" class="headertabela"><div align="right">Modelo:</div></td>
      <td width="300" bgcolor="#FFFFFF"><div align="left">
        <select name="cmbModelo" id="cmbModelo">
       <?
	   if ($id != 0) {
	   		if ($id == "1") {
				//$sql = "SELECT tblModelos.CodModelo, tblModelos.Modelo, tblFabricantes.NomeFabricante FROM (tblModelos INNER JOIN tblFabricantes ON tblModelos.Fabricante = tblFabricantes.CodFabricante) WHERE tblModelos.Categoria = 1 ORDER BY tblModelos.Modelo;";
				$sql = "SELECT tblModelos.CodModelo, tblModLoco.ModeloLoco FROM (tblModelos INNER JOIN tblModLoco ON tblModelos.CodModLoco = tblModLoco.CodModLoco) WHERE tblModelos.Categoria = 1 ORDER BY tblModLoco.ModeloLoco;";
				echo $sql;
				$res = @mysql_query($sql);
				
				//Exibe as linhas encontradas na consulta
				while ($row = mysql_fetch_array($res)) {
					echo "<option value=" . $row['CodModelo'];
					//echo ">" . $row['Modelo']; . " (" .  $row['NomeFabricante'] . ")</option>";
					echo ">" . $row['ModeloLoco'] . "</option>";
			 	}
			} elseif ($id == "2") {
				$sql = "SELECT tblModelos.CodModelo, tblTipoVags.TipoVag, tblPesoVags.LetraPesoVag FROM ((tblModelos INNER JOIN tblTipoVags ON tblModelos.CodTipoVag = tblTipoVags.CodTipoVag) INNER JOIN tblPesoVags ON tblModelos.CodPesoVag = tblPesoVags.CodPesoVag) WHERE tblModelos.Categoria = 2 ORDER BY tblTipoVags.TipoVag;";
				echo $sql;
				$res = @mysql_query($sql);
				
				//Exibe as linhas encontradas na consulta
				while ($row = mysql_fetch_array($res)) {
					echo "<option value=" . $row['CodModelo'];
					echo ">" . $row['TipoVag'] . $row['LetraPesoVag'] . "</option>";
			 	}
			} elseif ($id == "3") {
				$sql = "SELECT tblModelos.CodModelo, tblTipoCarro.LetraTipoCarro, tblMatCarro.LetraMatCarro FROM ((tblModelos INNER JOIN tblTipoCarro ON tblModelos.CodTipoCarro = tblTipoCarro.CodTipoCarro) INNER JOIN tblMatCarro ON tblModelos.CodMatCarro = tblMatCarro.CodMatCarro) WHERE tblModelos.Categoria = 3 ORDER BY tblTipoCarro.LetraTipoCarro;";
				echo $sql;
				$res = @mysql_query($sql);
				
				//Exibe as linhas encontradas na consulta
				while ($row = mysql_fetch_array($res)) {
					echo "<option value=" . $row['CodModelo'];
					echo ">" . $row['LetraTipoCarro'] . $row['LetraMatCarro'] . "</option>";
			 	}
			} elseif ($id == "4") {
				//$sql = "SELECT CodModelo, Modelo FROM tblModelos WHERE Categoria = 4 ORDER BY Modelo;";
				$sql = "SELECT tblModelos.CodModelo, tblTipoAuto.TipoAuto FROM (tblModelos INNER JOIN tblTipoAuto ON tblModelos.CodTipoAuto = tblTipoAuto.CodTipoAuto) WHERE tblModelos.Categoria = 4 ORDER BY tblTipoAuto.TipoAuto;";

				echo $sql;
				$res = @mysql_query($sql);
				
				//Exibe as linhas encontradas na consulta
				while ($row = mysql_fetch_array($res)) {
					echo "<option value=" . $row['CodModelo'];
					echo ">" . $row['TipoAuto'] . "</option>";
			 	}
			} elseif ($id == "5") {
					//$sql = "SELECT CodModelo, Modelo FROM tblModelos WHERE Categoria = 4 ORDER BY Modelo;";
					$sql = "SELECT tblModelos.CodModelo, tblTipoMotrizes.TipoMotriz FROM (tblModelos INNER JOIN tblTipoMotrizes ON tblModelos.CodTipoMotriz = tblTipoMotrizes.CodTipoMotriz) WHERE tblModelos.Categoria = 5 ORDER BY tblTipoMotrizes.TipoMotriz;";

					echo $sql;
					$res = @mysql_query($sql);

					//Exibe as linhas encontradas na consulta
					while ($row = mysql_fetch_array($res)) {
							echo "<option value=" . $row['CodModelo'];
							echo ">" . $row['TipoMotriz'] . "</option>";
					}
			}			
		}
	 ?>
     </select>
      </div></td>
    </tr>
    <tr>
      <td width="184" nowrap="nowrap" class="headertabela"><div align="right">Numero Inicial:</div></td>
      <td width="300" bgcolor="#FFFFFF"><div align="left"><span class="style3">
        <input name="txtNumeroInicial" type="text" id="txtNumeroInicial" size="10" maxlength="6" />
      </span></div></td>
    </tr>
    <tr>
      <td width="184" nowrap="nowrap" class="headertabela"><div align="right">Numero Final:</div></td>
      <td width="300" bgcolor="#FFFFFF"><div align="left"><span class="style3">
        <input name="txtNumeroFinal" type="text" id="txtNumeroFinal" size="10" maxlength="6" />
      </span></div></td>
    </tr>
    <tr>
      <td width="184" nowrap="nowrap" class="headertabela"><div align="right">Detalhes:</div></td>
      <td width="300" bgcolor="#FFFFFF"><div align="left">
        <textarea name="txtDetalhes" cols="47" rows="5" id="txtDetalhes"></textarea>
        <span class="style2">
        <input type="hidden" name="txtPath" id="txtPath" value="<? 
	echo $Path;
?>" />
        </span></div></td>
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
		echo $Mensagem['erromsg1'];
		echo $msg;
		echo $Mensagem['erromsg2'];
	}
} elseif ($Op == 3) { 
	if ($erro == 0) {
    	echo $Mensagem['sucesso'];
	} else {
		echo $Mensagem['erromsg1'];
		echo $msg;
		echo $Mensagem['erromsg2'];
	}
} ?>
</body>
</html>
