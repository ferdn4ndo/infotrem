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
if(empty($txtSigla)){
	$msg = $msg . "Sigla inv&aacute;lida! <br>";
	$erro = $erro + 1;
}
if(empty($txtMunicipio)){
	$msg = $msg . "Municipio inv&aacute;lido! <br>";
	$erro = $erro + 1;
}
if(empty($cmbUF)){
	$msg = $msg . "UF inv&aacute;lido! <br>";
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
	
	$sqlverifica = "SELECT * FROM tblLocais WHERE Sigla = '" . $txtSigla . "' AND Categoria = " . $cmbCategoria . " AND Municipio = '" . $txtMunicipio . "' AND UF = '" . $cmbUF .  "' AND FerroviaAtual = " . $cmbFerroviaAtual . " AND FerroviaOrigem = " . $cmbFerroviaOrigem . " AND Estado = " . $cmbEstado . ";";
	
	//echo $sqlverifica;
	
	if(mysqlcontar($id,$sqlverifica) > 0) { //Se já houver um registro igual
		echo "<title>ERRO</title></head><body>";
		echo "<strong>J&aacute; existe um local id&ecirc;ntico cadastrado no sistema!</strong>";
		exit;
	} else {
		$sql = "INSERT INTO tblLocais (Categoria, Sigla, Municipio, UF, FerroviaAtual, FerroviaOrigem, Estado) VALUES(" . $cmbCategoria . ",'" . $txtSigla . "','" . $txtMunicipio . "','" . $cmbUF .  "'," . $cmbFerroviaAtual . "," . $cmbFerroviaOrigem . "," . $cmbEstado . ");";
		
		//echo $sql;
		
		$ask = mysqlexecuta($id,$sql);
		if ($ask!=0){
			echo "<title>Inserir Local</title>";
			echo "<META HTTP-EQUIV=Refresh CONTENT=\"10; URL=index.php\">";
			echo "</head>";
			echo "<body>";
			echo "<strong>Cadastro concluído com sucesso!</strong>";
			echo "<p>Redirecionando...<br>Caso não redirecione automaticamente, <a href='index.php'> Clique Aqui!</a>";
		}
		else {
			echo "<title>ERRO</title></head><body>";
			echo "<br><strong>Erro ao interpretar dados!</strong><br>";
			exit;
		}
	}
} else {
	echo $msg;
}
?>
</body>
</html>
