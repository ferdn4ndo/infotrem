<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />
<title>Listar Links</title>
<link href="estilo.css" rel="stylesheet" type="text/css" />
</head>
<body><?
//Includes
include "includeslocalhost.php"; //Conecta ao banco de dados

//Faz a consulta
$sql = "SELECT tblLinks.*, tblCategoriaLink.Categoria AS NomeCategoria FROM tblLinks INNER JOIN tblCategoriaLink ON tblLinks.Categoria = tblCategoriaLink.CodCategoria ORDER BY Nome;";
$res = mysql_query($sql);
?><table width="100%" align="center"><tr height="100%"><td align="center" valign="center" height="100%">
<form id="form1" name="form1" method="post" action="#"><div align="center">
  <table width="750" border="1" cellspacing="0" cellpadding="0">
  <tr>
    <td colspan="7" class="headertabela"><div align="center">Listar Links</div></td>
      </tr>
    <tr>
      <td width="5%"  class="headertabela"><div align="center">Cód</div></td>
      <td width="16%" bgcolor="#FFFFFF" class="headertabela"><div align="center">Nome</div></td>
      <td width="16%" bgcolor="#FFFFFF" class="headertabela"><div align="center">Categoria</div></td>
      <td width="35%" bgcolor="#FFFFFF" class="headertabela"><div align="center">Link</div></td>
      <td width="20%" bgcolor="#FFFFFF" class="headertabela"><div align="center">Detalhes</div></td>
      <td width="4%" bgcolor="#FFFFFF" class="headertabela"><div align="center">E</div></td>
      <td width="4%" bgcolor="#FFFFFF" class="headertabela"><div align="center">X</div></td>
    </tr>
    <?
    //Exibe as linhas encontradas na consulta
    while ($row = mysql_fetch_array($res)) {
		//Prepara os dados
		$Modelo = "";
		
		
		//Exibe as Linhas
		if(strlen($row['Detalhes'])>10){
			$Detalhes = substr($row['Detalhes'],0,10) . "...";
		} else {
			$Detalhes = $row['Detalhes'];
		}
 ?> 
  <tr>
      <td><div align="center"><? echo $row['CodLink'];?></div></td>
      <td><div align="center"><a href="exibirlink.php?Cod=<? echo $row['CodLink'];?>" title="Mais detalhes de <? echo $row['Nome'];?>"><? echo $row['Nome'];?></a></div></td>
      <td><div align="center"><? echo $row['NomeCategoria'];?></div></td> 
     <td><div align="center"><a href="<? echo $row['Link'];?>" target="_blank" title="Link para <? echo $row['Nome'];?>"><? echo $row['Link'];?></a></div></td> 
     <td><div align="center"><? echo $Detalhes;?></div></td>
     <td><div align="center"><a href="editarlink.php?Cod=<? echo $row['CodLink'];?>"><img alt="Editar" src="images/edit.png" border="0" width="16" height="16" /></a></div></td>
     <td><div align="center"><a href="excluirlink.php?Cod=<? echo $row['CodLink'];?>"><img alt="Excluir" src="images/delete.png" border="0" width="16" height="16" /></a></div></td>
  </tr>

 <?
  }
  
 ?>
    <tr>
      <td height="23" colspan="7" class="headertabela"><div align="center">
        <input type="submit" name="submit" id="submit" value="Atualizar" />
      </div></td>
      </tr>
  </table>
  </div>
</form></td></tr></table>
</body>
</html>
