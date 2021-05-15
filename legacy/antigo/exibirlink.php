<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />
<title>Exibir Link</title>
<link href="estilo.css" rel="stylesheet" type="text/css" />
</head>
<body><?
//Includes
include "includeslocalhost.php"; //Conecta ao banco de dados

//Pega os dados da URL
$CodLink = AntiInjection($_GET["Cod"]);

//Pega a categoria
$sql = "SELECT tblLinks.*, tblCategoriaLink.Categoria AS NomeCategoria FROM tblLinks INNER JOIN tblCategoriaLink ON tblLinks.Categoria = tblCategoriaLink.CodCategoria WHERE tblLinks.CodLink = " . $CodLink . ";";

//Executa o comando
$res = mysql_query($sql);
while ($row = mysql_fetch_array($res)) {
	//Prepara os dados
	$Nome = $row['Nome'];
	$Link = $row['Link'];
	$Categoria = $row['NomeCategoria'];
	$Detalhes = $row['Detalhes'];
}

?><table width="100%" align="center"><tr height="100%"><td align="center" valign="center" height="100%">
<form id="form1" name="form1" method="post" action="#"><div align="center">
  <table width="500" border="1" cellspacing="0" cellpadding="0">
  <tr>
      <td height="23" colspan="2" class="headertabela"><div align="center" class="header">Exibir Link</div></td>
      </tr>
      <tr>
    <td width="149" class="headertabela"><div align="right">C&oacute;digo:</div></td>
      <td width="345" bgcolor="#FFFFFF"><? echo $CodLink; ?></td>
    </tr>
  	<tr>
    <td width="149" class="headertabela"><div align="right">Nome:</div></td>
      <td width="345" bgcolor="#FFFFFF"><? echo $Nome; ?></td>
    </tr>
    <tr>
      <td width="149" class="headertabela"><div align="right">Categoria:</div></td>
      <td width="345" bgcolor="#FFFFFF"><? echo $Categoria; ?></td>
    </tr>
    <tr>
      <td width="149" class="headertabela"><div align="right">Link:</div></td>
      <td width="345" bgcolor="#FFFFFF"><a href="<? echo $Link; ?>" target="_blank" title="Link para <? echo $Nome; ?>"><? echo $Link; ?></a></td>
    </tr>
    <tr>
      <td width="149" class="headertabela"><div align="right">Detalhes:</div></td>
      <td width="345" bgcolor="#FFFFFF"><? echo $Detalhes; ?></td>
    </tr>
    <tr>
      <td height="23" colspan="2" class="headertabela"><div align="center">
        <input type="button" name="button" id="button" value="Voltar" onclick="javascript:history.back();" />
      </div></td>
      </tr>
  </table>
  </div>
</form></td></tr></table>
</body>
</html>
