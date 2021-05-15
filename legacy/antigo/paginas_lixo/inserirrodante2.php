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
if(empty($cmbModelo)){
	$msg = $msg . "Modelo inv&aacute;lido! <br>";
	$erro = $erro + 1;
}
if(empty($txtNumero)){
	$msg = $msg ."N&uacute;mero inv&aacute;lido! <br>";
	$erro = $erro + 1;
}
if(empty($cmbFerroviaAtual)){
	$msg = $msg . "Ferrovia atual inv&aacute;lida! <br>";
	$erro = $erro + 1;
}
if(empty($cmbFerroviaOrigem)){
	$msg = $msg . "Ferrovia de origem inv&aacute;lida! <br>";
	$erro = $erro + 1;
}
if(!empty($txtUltimaData)){
	if(ValidaData($txtUltimaData) == false){
		$msg = $msg . "Ultima data inv&aacute;lida! <br>";
		$erro = $erro + 1;
	}
}
if(empty($cmbEstado)){
	$msg = $msg . "Estado inv&aacute;lido! <br>";
	$erro = $erro + 1;
}


if($erro == 0){
	
	//Consulta para verificar itens idênticos
	
	$sqlverifica = "SELECT * FROM tblRodante WHERE Categoria = " . $cmbCategoria . " AND CodModelo = " . $cmbModelo . " AND Numero = " . $txtNumero . " AND FerroviaAtual = " . $cmbFerroviaAtual .  " AND FerroviaOrigem = " . $cmbFerroviaOrigem . ";";
	
	//echo $sqlverifica;
	
	if(mysqlcontar($id,$sqlverifica) > 0) { //Se já houver um registro igual
		echo "<title>ERRO</title></head><body>";
		echo "<strong>J&aacute; existe um registro id&ecirc;ntico no sistema!</strong>";
		exit;
	} else {
		$sql = "INSERT INTO tblRodante (Categoria, CodModelo, Numero, FerroviaAtual, FerroviaOrigem, UltimoLocal, UltimaData, Estado, Detalhes) VALUES(" . $cmbCategoria . "," . $cmbModelo . "," . $txtNumero . "," . $cmbFerroviaAtual .  "," . $cmbFerroviaOrigem . "," . $cmbUltimoLocal . ",'" . gravaData($txtUltimaData) . "'," . $cmbEstado . ",'" . $txtDetalhes . "');";
		
		//echo $sql;
		
		$ask = mysqlexecuta($id,$sql);
		if ($ask!=0){
			redirecionar("index.php");
			echo "<title>Inserir Material Rodante</title>";
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
