<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />
<title>Listar Prefixos</title>
<link href="estilo.css" rel="stylesheet" type="text/css" />
</head>
<body><?
//Includes
include "includeslocalhost.php"; //Conecta ao banco de dados

//Faz a consulta
$sql = "SELECT tblPrefixos.*, tblLocais.Sigla AS SiglaLocal1, tblLocais.Nome As NomeLocal1, tblLocais2.Sigla AS SiglaLocal2, tblLocais2.Nome As NomeLocal2,  tblFerrovias.Nome AS Ferrovia FROM tblPrefixos INNER JOIN tblLocais ON tblLocais.CodLocal = tblPrefixos.Origem INNER JOIN tblLocais tblLocais2 ON tblLocais2.CodLocal = tblPrefixos.Destino INNER JOIN tblFerrovias ON tblPrefixos.CodFerrovia = tblFerrovias.CodFerrovia ORDER BY tblPrefixos.CodFerrovia, tblPrefixos.Prefixo;";
$res = mysql_query($sql);
?><table width="100%" align="center"><tr height="100%"><td align="center" valign="center" height="100%">
<form id="form1" name="form1" method="post" action="#"><div align="center">
  <table width="750" border="1" cellspacing="0" cellpadding="0">
    <tr>
      <td colspan="8" class="headertabela"><div align="center">Listar Prefixos</div></td>
    </tr>
    <tr>
      <td width="5%"  class="headertabela"><div align="center">Cód</div></td>
      <td width="16%" bgcolor="#FFFFFF" class="headertabela"><div align="center">Ferrovia</div></td>
      <td width="16%" bgcolor="#FFFFFF" class="headertabela"><div align="center">Prefixo</div></td>
      <td width="35%" bgcolor="#FFFFFF" class="headertabela"><div align="center">Origem</div></td>
      <td width="35%" bgcolor="#FFFFFF" class="headertabela"><div align="center">Destino</div></td>
      <td width="20%" bgcolor="#FFFFFF" class="headertabela"><div align="center">Detalhes</div></td>
      <td width="4%" bgcolor="#FFFFFF" class="headertabela"><div align="center">E</div></td>
      <td width="4%" bgcolor="#FFFFFF" class="headertabela"><div align="center">X</div></td>
    </tr>
    <?
    //Exibe as linhas encontradas na consulta
    while ($row = mysql_fetch_array($res)) {
		//Exibe as Linhas
		if(strlen($row['Detalhes'])>10){
			$Detalhes = substr($row['Detalhes'],0,10) . "...";
		} else {
			$Detalhes = $row['Detalhes'];
		}
 ?>
    <tr>
      <td><div align="center"><? echo $row['CodPrefixo'];?></div></td>
      <td><div align="center"><? echo $row['Ferrovia'];?></div></td>
      <td><div align="center"><a href="exibirprefixo.php?Cod=<? echo $row['CodPrefixo'];?>" title="Mais detalhes de <? echo $row['Prefixo'];?>"><? echo $row['Prefixo'];?></a></div></td>
      <td><div align="center"><? echo $row['SiglaLocal1']." - ".$row['NomeLocal1'];?></div></td>
      <td><div align="center"><? echo $row['SiglaLocal2']." - ".$row['NomeLocal2'];?></div></td>
      <td><div align="center"><? echo $Detalhes;?></div></td>
      <td><div align="center"><a href="editarlink.php?Cod=<? echo $row['CodLink'];?>"><img alt="Editar" src="images/edit.png" border="0" width="16" height="16" /></a></div></td>
      <td><div align="center"><a href="excluirlink.php?Cod=<? echo $row['CodLink'];?>"><img alt="Excluir" src="images/delete.png" border="0" width="16" height="16" /></a></div></td>
    </tr>
    <?
  }
  
 ?>
    <tr>
      <td height="23" colspan="8" class="headertabela"><div align="center">
          <input type="submit" name="submit" id="submit" value="Atualizar" />
      </div></td>
    </tr>
  </table>
</div>
</form></td></tr></table>
</body>
</html>
