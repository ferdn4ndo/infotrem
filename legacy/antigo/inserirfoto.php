<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />
<title>Inserir Foto</title>
<link href="estilo.css" rel="stylesheet" type="text/css" />
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
	
	document.location=('inserirfoto.php?Categoria=' + selecionada.value + "&CaminhoFoto=" + document.getElementById("txtPath").value);
	
  }
</script>
</head><body><?
//Includes
include "includeslocalhost.php"; 
include "function_nomefoto.php";

//Pega a categoria
$id = $_GET["Categoria"];

//Checagem da operação à ser executada
$Op = 1;
if (isset($_FILES['arquivo']) || isset($_GET['CaminhoFoto'])) {
	$Op = 2;
	
}
if (isset($_POST['txtPath'])) {
	$Op = 3;
}

if (isset($_GET['CaminhoFoto'])) {
	$Path = $_GET['CaminhoFoto'];
}

//Faz a operação de Upload
if ($Op == 2) {
	//Zera as variáveis
	$erros = 0;
	$msg = "";
	
	//Strings necessárias
	$tamanhoMaximo = 10 * 1024 * 1024; //10MB
	$extensoes = array(".gif", ".jpg", ".jpeg", ".bmp", ".png");
	$caminho = "uploads/fotos/";
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
	if(empty($txtNumero)){
		$msg = $msg ."N&uacute;mero inv&aacute;lido! <br>";
		$erro = $erro + 1;
	}
	if(empty($cmbFerrovia)){
		$msg = $msg . "Ferrovia inv&aacute;lida! <br>";
		$erro = $erro + 1;
	}
	if(empty($cmbLocal)){
		$cmbLocal = 3295;
		//$msg = $msg . "Local inv&aacute;lido! <br>";
		//$erro = $erro + 1;
	}
	if(empty($txtPath)){
		$msg = $msg . "Caminho da foto inv&aacute;lido! <br>";
		$erro = $erro + 1;
	}
	if(!empty($txtData)){
		if(ValidaData($txtData) == false){
			$msg = $msg . "Data inv&aacute;lida! <br>";
			$erro = $erro + 1;
		}
	}

	if($erro == 0){
		//Prepara o novo nome da foto
		if ($cmbCategoria==2) {
			$NomeNovo = NomeFoto($cmbCategoria,$cmbModelo,$txtNumero."-".CalculaDV($txtNumero),$cmbFerrovia,$cmbLocal,$txtData,$txtAutor);
		} else {
			$NomeNovo = NomeFoto($cmbCategoria,$cmbModelo,$txtNumero,$cmbFerrovia,$cmbLocal,$txtData,$txtAutor);
		}
		
		//Prepara para renomear
		$CaminhoCompleto = "/var/www/infotrem/uploads/fotos/";
		$CaminhoBD = "uploads/fotos/";
		$Extensao = strrchr(strtolower($txtPath), ".");
		$NomeCompleto = $CaminhoCompleto.$NomeNovo.$Extensao;
		$NomeBD = $CaminhoBD.$NomeNovo.$Extensao;
		//Verifica se o nome podera ser utilizado
		if (file_exists($NomeCompleto)) {
			$NomeTmp1 = $CaminhoCompleto.$NomeNovo."_1".$Extensao;
			$NomeTmp2 = $CaminhoBD.$NomeNovo."_1".$Extensao;
			$i = 1;
			while (file_exists($NomeTmp1)) {
				$i++;
				$NomeTmp1 = $CaminhoCompleto.$NomeNovo."_".$i.$Extensao;
				$NomeTmp2 = $CaminhoBD.$NomeNovo."_".$i.$Extensao;
			}
			$NomeCompleto = $NomeTmp1;
			$NomeBD = $NomeTmp2;
		}
		//Renomeia a foto
		$Renomeia = rename("/var/www/infotrem/" . $txtPath, $NomeCompleto);
		echo "/var/www/infotrem/" . $txtPath . "<br>" . $NomeBD . "<br>" . $NomeCompleto;
		if (!$Renomeia) {
			$msg = $msg . "Erro ao renomar foto! <br>";
		}
	
		//Consulta para verificar itens idênticos
		$sqlverifica = "SELECT * FROM tblFotos WHERE CaminhoFoto = '" . $NomeBD . "';";
		if(mysql_num_rows(mysql_query($sqlverifica)) > 0) { //Se já houver um registro igual
			$msg = $msg . $Mensagem['erroduplicado'];
			$erro = $erro + 1;
		} else {
			//Registra a foto e pega o codigo
			$sql = "INSERT INTO tblFotos (Categoria, Ferrovia, Local, Data, Detalhes, Autor, CaminhoFoto) VALUES(" . $cmbCategoria . "," . $cmbFerrovia . "," . $cmbLocal .  ",'" . gravaData($txtData) . "','" . $txtDetalhes . "','" . $txtAutor . "','" . $NomeBD . "');";
            $ask = mysql_query($sql);
			$CodFoto = mysql_insert_id();
			
			//Checa se ja exite um registro de mat. rodante
			$sqlrod = "SELECT CodReg FROM tblRodante WHERE Numero = " . $txtNumero . ";";
			$askrod = mysql_query($sqlrod);
			$cntrod = mysql_num_rows($askrod);
			if($cntrod > 0) {
				//Se ja existe um registro de mat. rodante, atualiza
				while ($rowrod = mysql_fetch_array($askrod)){
					$CodRodante = $rowrod['CodReg'];
				}
				$sqlupd = "UPDATE tblRodante SET UltimaFoto = " . $CodFoto . " WHERE CodReg = " . $CodRodante . ";";
				$askupd = mysql_query($sqlupd);
			} else {
				//Senao, cria um novo mat. rodante
				$sqlins = "INSERT INTO tblRodante (Categoria, CodModelo, Numero, FerroviaAtual, FerroviaOrigem, UltimaFoto, UltimaData, UltimoLocal, Estado, Detalhes) VALUES (" . $cmbCategoria . "," . $cmbModelo . "," . $txtNumero . ",13,13," . $CodFoto . ",'" . gravaData($txtData) . "'," . $cmbLocal . ",5,'');";
				$askins = mysql_query($sqlins);
				
				//Pega o codigo
				$sqlcod = "SELECT * FROM tblRodante WHERE Numero = " . $txtNumero . ";";
				$askcod = mysql_query($sqlcod);
				$rowcod = mysql_fetch_array($askcod);
				while ($rowcod = mysql_fetch_array($askcod)){
							$CodRodante = $rowcod['CodReg'];
				}
				$CodRodante = mysql_insert_id();
			}
			
			//Atualiza o registro da foto
			$sqlfot = "UPDATE tblFotos SET CodRodante = " . $CodRodante . " WHERE CodFoto = " . $CodFoto . ";";
			$askfot = mysql_query($sqlfot);
			
			//Debugging
			$Debug = 0;
			if ($Debug==1){
				echo "CodFoto = " . $CodFoto . "<br>";
				echo "CodRodante = " . $CodRodante . "<br>";
				echo "ask = " . $ask . "<br>";
				echo "que = " . $que . "<br>";
				echo "askrod = " . $askrod . "<br>";
				echo "askupd = " . $askupd . "<br>";
				echo "askins = " . $askins . "<br>";
				echo "askcod = " . $askcod . "<br>";
				echo "cntrod = " . $cntrod . "<br>";
				echo "sql = " . $sql . "<br>";
				echo "cod = " . $cod . "<br>";
				echo "sqlrod = " . $sqlrod . "<br>";
				echo "sqlupd = " . $sqlupd . "<br>";
				echo "sqlins = " . $sqlins . "<br>";
				echo "sqlcod = " . $sqlcod . "<br>";
				echo "sqlfot = " . $sqlfot . "<br>";
				echo "askfot = " . $askfot . "<br>";	
			}
			
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
      <td colspan="2" class="headertabela"><div align="center" class="header">Cadastrar Foto
      </div></td>
      </tr>
    <tr>
      <td width="263" height="27" nowrap="nowrap" class="headertabela"><div align="right">Selecione a foto:</div></td>
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
      <td colspan="2" nowrap="nowrap" class="headertabela"><div align="center" class="header">Cadastrar Foto - BD</div>
        <div align="left"></div></td>
      </tr>
  <tr>
      <td width="184" nowrap="nowrap" class="headertabela"><div align="right">Foto:</div></td>
      <td width="300" bgcolor="#FFFFFF"><div align="center"><img src="<? 
if ($Path != "") {
	echo $Path;
	$tamanhos = getimagesize($Path);
	$exibe = $Path;
} else {
	echo $caminho . $arquivo_tratado;
	$tamanhos = getimagesize($caminho . $arquivo_tratado);
	$exibe = $caminho . $arquivo_tratado;
}
//Calcula altura e largura
$largura = intval(($tamanhos[1] * 96)/225);
$altura = intval(($tamanhos[0] * 70)/300);

?>" width="<? echo $largura; ?>" height="<? echo $altura; ?>"/><br /><center><? echo $exibe; ?></center></div></td>
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
		$Categoria = $id;
			if ($Categoria == "1") {
                                $sql = "SELECT tblModelos.CodModelo, tblModLoco.ModeloLoco FROM (tblModelos INNER JOIN tblModLoco ON tblModelos.CodModLoco = tblModLoco.CodModLoco) WHERE tblModelos.Categoria = 1 ORDER BY tblModLoco.ModeloLoco;";
                                //echo $sql;
                                $res = @mysql_query($sql);

                                //Exibe as linhas encontradas na consulta
                                while ($row = mysql_fetch_array($res)) {
                                        echo "<option value=" . $row['CodModelo'];
                                        if ($CodModelo == $row['CodModelo']) { echo " selected='selected'"; }
                                        echo ">" . $row['ModeloLoco'] . "</option>";
                                }
                        } elseif ($Categoria == "2") {
                                $sql = "SELECT tblModelos.CodModelo, tblTipoVags.TipoVag, tblPesoVags.LetraPesoVag FROM ((tblModelos INNER JOIN tblTipoVags ON tblModelos.CodTipoVag = tblTipoVags.CodTipoVag) INNER JOIN tblPesoVags ON tblModelos.CodPesoVag = tblPesoVags.CodPesoVag) WHERE tblModelos.Categoria = 2 ORDER BY tblTipoVags.TipoVag;";
                                //echo $sql;
                                $res = @mysql_query($sql);

                                //Exibe as linhas encontradas na consulta
                                while ($row = mysql_fetch_array($res)) {
                                        echo "<option value=" . $row['CodModelo'];
                                        if ($CodModelo == $row['CodModelo']) { echo " selected='selected'"; }
                                        echo ">" . $row['TipoVag'] . $row['LetraPesoVag'] . "</option>";
                                }
			} elseif ($Categoria == "3") {
                                $sql = "SELECT tblModelos.CodModelo, tblTipoCarro.LetraTipoCarro, tblMatCarro.LetraMatCarro FROM ((tblModelos INNER JOIN tblTipoCarro ON tblModelos.CodTipoCarro = tblTipoCarro.CodTipoCarro) INNER JOIN tblMatCarro ON tblModelos.CodMatCarro = tblMatCarro.CodMatCarro) WHERE tblModelos.Categoria = 3 ORDER BY tblTipoCarro.LetraTipoCarro;";
                                //echo $sql;
                                $res = @mysql_query($sql);

                                //Exibe as linhas encontradas na consulta
                                while ($row = mysql_fetch_array($res)) {
                                        echo "<option value=" . $row['CodModelo'];
                                        if ($CodModelo == $row['CodModelo']) { echo " selected='selected'"; }
                                        echo ">" . $row['LetraTipoCarro'] . $row['LetraMatCarro'] . "</option>";
                                }
                        } elseif ($Categoria == "4") {
                                $sql = "SELECT tblModelos.CodModelo, tblTipoAuto.TipoAuto FROM (tblModelos INNER JOIN tblTipoAuto ON tblModelos.CodTipoAuto = tblTipoAuto.CodTipoAuto) WHERE tblModelos.Categoria = 4 ORDER BY tblTipoAuto.TipoAuto;";
                                //echo $sql;
                                $res = @mysql_query($sql);

                                //Exibe as linhas encontradas na consulta
                                while ($row = mysql_fetch_array($res)) {
                                        echo "<option value=" . $row['CodModelo'];
                                        if ($CodModelo == $row['CodModelo']) { echo " selected='selected'"; }
                                        echo ">" . $row['TipoAuto'] . "</option>";
                                }
                        } elseif ($Categoria == "5") {
                                $sql = "SELECT tblModelos.CodModelo, tblTipoMotrizes.TipoMotriz FROM (tblModelos INNER JOIN tblTipoMotrizes ON tblModelos.CodTipoMotriz = tblTipoMotrizes.CodTipoMotriz) WHERE tblModelos.Categoria = 5 ORDER BY tblTipoMotrizes.TipoMotriz;";
                                //echo $sql;
                                $res = @mysql_query($sql);

                                //Exibe as linhas encontradas na consulta
                                while ($row = mysql_fetch_array($res)) {
                                        echo "<option value=" . $row['CodModelo'];
                                        if ($CodModelo == $row['CodModelo']) { echo " selected='selected'"; }
                                        echo ">" . $row['TipoMotriz'] . "</option>";
                                }
                        } elseif ($Categoria == "0") {
				echo "<option value='0' selected='selected'>Outros / Diversos</option>";
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
			$sql = "SELECT CodLocal, Sigla, Nome FROM tblLocais ORDER BY Sigla;";
			$res = @mysql_query($sql);
			
			//Exibe as linhas encontradas na consulta
			while ($row = mysql_fetch_array($res)) {
				echo "<option value=" . $row['CodLocal'];
				echo ">" . $row['Sigla'] . " - " . $row['Nome'] . "</option>";
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
	echo $Path;
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
