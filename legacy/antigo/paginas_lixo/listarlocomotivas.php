<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />
<title>Listar Locomotivas</title>
<link href="estilo.css" rel="stylesheet" type="text/css" />
</head>
<body><?
//Includes
include "includeslocalhost.php"; //Conecta ao banco de dados

//Faz a consulta
$sql = "SELECT tblRodante.*, tblModelos.Modelo, tblFerrovias.Nome AS Ferrovia1, tblFerrovias2.Nome AS Ferrovia2, tblLocais.Nome AS Local, tblEstadoRodante.Estado FROM (((((tblRodante INNER JOIN tblModelos ON tblRodante.CodModelo = tblModelos.CodModelo) INNER JOIN tblFerrovias ON tblRodante.FerroviaAtual = tblFerrovias.CodFerrovia) INNER JOIN tblFerrovias tblFerrovias2 ON tblRodante.FerroviaOrigem = tblFerrovias2.CodFerrovia) INNER JOIN tblLocais ON tblRodante.UltimoLocal = tblLocais.CodLocal) INNER JOIN tblEstadoRodante ON tblRodante.Estado = tblEstadoRodante.CodEstado) WHERE tblRodante.Categoria = 4 ORDER BY tblModelos.Modelo;";
$res = mysql_query($sql);
?><table width="100%" align="center"><tr height="100%"><td align="center" valign="center" height="100%">
<form id="form1" name="form1" method="post" action="#"><div align="center">
  <table width="750" border="1" cellspacing="0" cellpadding="0">
  <tr>
    <td colspan="11" class="headertabela"><div align="center">Listar Autos de Linha</div></td>
      </tr>
    <tr>
      <td width="5%"  class="headertabela"><div align="center">Cód</div></td>
      <td width="8%" bgcolor="#FFFFFF" class="headertabela"><div align="center">Modelo</div></td>
      <td width="8%" bgcolor="#FFFFFF" class="headertabela"><div align="center">N&uacute;mero</div></td>
      <td width="10%" bgcolor="#FFFFFF" class="headertabela"><div align="center">Ferr. Atual</div></td>
      <td width="10%" bgcolor="#FFFFFF" class="headertabela"><div align="center">Ferr. Origem</div></td>
      <td width="15%" bgcolor="#FFFFFF" class="headertabela"><div align="center">&Uacute;ltimo Local</div></td>
      <td width="10%" bgcolor="#FFFFFF" class="headertabela"><div align="center">&Uacute;ltima Data</div></td>
      <td width="14%" bgcolor="#FFFFFF" class="headertabela"><div align="center">Estado</div></td>
      <td width="10%" bgcolor="#FFFFFF" class="headertabela"><div align="center">Detalhes</div></td>
      <td width="5%" bgcolor="#FFFFFF" class="headertabela"><div align="center">E</div></td>
      <td width="5%" bgcolor="#FFFFFF" class="headertabela"><div align="center">X</div></td>
    </tr>
    <?
    //Exibe as linhas encontradas na consulta
    while ($row = mysql_fetch_array($res)) {
		//Prepara os dados
		$Modelo = "";
		
		
		//Exibe as Linhas
 ?> 
  <tr>
      <td><div align="center"><? echo $row['CodReg'];?></div></td>
      <td><div align="center"><? echo $row['Modelo'];?></div></td>
      <td><div align="center"><? echo $row['Numero'];?></div></td> 
     <td><div align="center"><? echo $row['Ferrovia1'];?></div></td> 
     <td><div align="center"><? echo $row['Ferrovia2'];?></div></td>
     <td><div align="center"><? echo $row['Local'];?></div></td>
     <td><div align="center"><? echo mostraData($row['UltimaData']);?></div></td>
     <td><div align="center"><? echo $row['Estado'];?></div></td>
     <td><div align="center"><? echo $row['Detalhes'];?></div></td>
     <td><div align="center"><a href="editarrodante.php?Cod=<? echo $row['CodReg'];?>"><img alt="Editar" src="images/edit.png" border="0" width="16" height="16" /></a></div></td>
     <td><div align="center"><a href="excluirrodante.php?Cod=<? echo $row['CodReg'];?>"><img alt="Excluir" src="images/delete.png" border="0" width="16" height="16" /></a></div></td>
  </tr>

 <?
  }
  
 ?>
    <tr>
      <td height="23" colspan="11" class="headertabela"><div align="center">
        <input type="submit" name="submit" id="submit" value="Atualizar" />
      </div></td>
      </tr>
  </table>
  </div>
</form></td></tr></table>
</body>
</html>
