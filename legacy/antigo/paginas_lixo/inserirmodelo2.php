<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
<?
//Includes
include "includeslocalhost.php"; //Conecta ao banco de dados

//Pega variaveis vinda do formulário via POST
foreach( $_POST as $campo => $vlr){
   $$campo = AntiInjection($vlr);
}
$erro = 0;

if(empty($cmbCategoria)){
	$msg = $msg . "Categoria inv&aacute;lida! <br>";
	$erro = $erro + 1;
}
if($cmbCategoria==1){
	if(empty($txtModelo)){
		$msg = $msg . "Modelo inv&aacute;lido! <br>";
		$erro = $erro + 1;
	}
	if(empty($cmbFabricante)){
		$msg = $msg . "Fabricante inv&aacute;lido! <br>";
		$erro = $erro + 1;
	}
} elseif ($cmbCategoria==2){
	if(empty($cmbTipoVag)){
		$msg = $msg . "Tipo inv&aacute;lido! <br>";
		$erro = $erro + 1;
	}
	if(empty($cmbPesoVag)){
		$msg = $msg . "Peso inv&aacute;lido! <br>";
		$erro = $erro + 1;
	}
}
if($erro == 0){
	
	//Fixa as variáveis nulas
	if ($cmbFabricante=="") { $cmbFabricante = 0; }
	if ($cmbTipoVag=="") { $cmbTipoVag = 0; }
	if ($cmbPesoVag=="") { $cmbPesoVag = 0; }
	
	//Consulta para verificar itens idênticos
	
	$sqlverifica = "SELECT * FROM tblModelos WHERE Modelo = '" . $txtModelo . "' AND Categoria = " . $cmbCategoria . " AND Fabricante = " . $cmbFabricante . " AND CodTipoVag = " . $cmbTipoVag . " AND CodPesoVag = " . $cmbPesoVag . ";";
	
	//echo $sqlverifica;
	
	if(mysqlcontar($id,$sqlverifica) > 0) { //Se já houver um registro igual
		echo "<title>ERRO</title></head><body>";
		echo "<strong>J&aacute; existe um modelo id&ecirc;ntico cadastrado no sistema!</strong>";
		exit;
	} else {
		$sql = "INSERT INTO tblModelos (Categoria, Modelo, CodPesoVag, CodTipoVag, Fabricante, Detalhes) VALUES(" . $cmbCategoria . ",'" . $txtModelo . "'," . $cmbPesoVag . "," . $cmbTipoVag . "," . $cmbFabricante . ",'" . $txtDetalhes ."');";
		
		//echo $sql;
		
		$ask = mysqlexecuta($id,$sql);
		If ($ask!=0){
			redirecionar("index.php");
			echo "<title>Inserir Modelo</title>";
			echo "<META HTTP-EQUIV=Refresh CONTENT=\"10; URL=index.php\">";
			echo "</head>";
			echo "<body>";
			echo "<strong>Cadastro concluído com sucesso!</strong>";
			echo "<p>Redirecionando...<br>Caso não redirecione automaticamente, <a href='index.php'> Clique Aqui!</a>";
		}
		else {
			echo "<title>ERRO</title></head><body>";
			echo "<br><strong>Erro ao interpretar dados!</strong>";
			exit;
		}
	}
} else {
	echo $msg;
}
?>
</body>
</html>
