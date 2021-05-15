<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>InfoTrem</title>
<link href="estilo.css" rel="stylesheet" type="text/css" />
<script src="SpryAssets/SpryMenuBar.js" type="text/javascript"></script>
<link href="SpryAssets/SpryMenuBarVertical.css" rel="stylesheet" type="text/css" />
</head><?

//Pega o endereço
$url = $_GET["pagina"];

if ($url == "") {
	$url = "centro.php";
}
?><body bgcolor="#bbbbbb">
<div id="body" align="center">
<table width="900" height="100%" border="1" cellspacing="0" cellpadding="0">
  <tr height="100">
    <th colspan="2" bgcolor="bbbbbb" scope="col"><div align="left"><img src="images/logo900.jpg" width="900" height="100" /></div></th>
  </tr>
  <tr height="21">
    <th height="21" colspan="2" background="images/topbar_fundo.jpg" scope="row">&nbsp;</th>
  </tr>
  <tr height="500">
    <td width="130" valign="top" bgcolor="#EEE"><ul id="MenuBar1" class="MenuBarVertical">
      <li><a class="MenuBarItemSubmenu" href="#">Cadastrar</a>
          <ul>
          	<li><a href="#" class="MenuBarItemSubmenu">Itens</a>
              <ul>
              	<li><a href="inserirdocumento.php" target="centro">Documento</a></li>
                <li><a href="inserirfabricante.php" target="centro">Fabricante</a></li>
                <li><a href="inserirferrovia.php" target="centro">Ferrovia</a></li>
                <li><a href="inserirfoto.php" target="centro">Foto Local</a></li>
                <li><a href="inserirfotoexterna.php" target="centro">Foto Externa</a></li>
                <li><a href="inserirlink.php" target="centro">Link</a></li>
                <li><a href="inserirlocal.php" target="centro">Local</a></li>
                <li><a href="inserirrodante.php" target="centro">Material Rodante</a></li>
                <li><a href="inserirmodelo.php" target="centro">Modelo</a></li>
                <li><a href="inserirplanta.php" target="centro">Planta</a></li>
                <li><a href="inserirprefixo.php" target="centro">Prefixo</a></li>
                <li><a href="inserirvideo.php" target="centro">V&iacute;deo Local</a></li>
                <li><a href="inserirvideoexterno.php" target="centro">V&iacute;deo Online</a></li>
                <li><a href="inserirvideodownload.php" target="centro">V&iacute;deo Online (Download)</a></li>
              </ul>
            </li>
            <li><a href="#" class="MenuBarItemSubmenu">Categorias</a>
              <ul>
                <li><a href="inserircategoriadocumento.php" target="centro">Categoria de Documento</a></li>
                <li><a href="inserircategorialink.php" target="centro">Categoria de Link</a></li>
                <li><a href="inserircategorialocal.php" target="centro">Categoria de Local</a></li>
                <li><a href="inserircategoriarodante.php" target="centro">Categoria de Mat. Rodante</a></li>
                <li><a href="inserircategoriaplanta.php" target="centro">Categoria de Planta</a></li>
              </ul>
            </li>
            <li><a href="#" class="MenuBarItemSubmenu">Estados</a>
              <ul>
                <li><a href="inserirestadolocal.php" target="centro">Estado de Local</a></li>
                <li><a href="inserirestadorodante.php" target="centro">Estado de Mat. Rodante</a></li>
              </ul>
            </li>
            <li><a href="#" class="MenuBarItemSubmenu">Tipos</a>
              <ul>
                <li><a href="inserirtipoauto.php" target="centro">Tipo de Auto de Linha</a></li>
                <li><a href="inserirtipocarro.php" target="centro">Tipo de Carro</a></li>
                <li><a href="inserirtipotracao.php" target="centro">Tipo de Tra&ccedil;&atilde;o</a></li>
                <li><a href="inserirtipovag.php" target="centro">Tipo de Vag&atilde;o</a></li>
              </ul>
            </li>
           	<li><a href="#" class="MenuBarItemSubmenu">Outros</a>
              <ul>
                <li><a href="inserirbitola.php" target="centro">Bitola</a></li>
              	<li><a href="inserirmaterialcarro.php" target="centro">Material de Carro</a></li>
                <li><a href="inserirpesovag.php" target="centro">Peso de Vag&atilde;o</a></li>
              </ul>
            </li>
          </ul>
      </li>
      <li><a href="#" class="MenuBarItemSubmenu">Consultas</a>
        <ul>
          <li><a href="#" class="MenuBarItemSubmenu">Material Rodante</a>
              <ul>
                <li><a href="consultarrodante.php" target="centro">&Uacute;nico</a></li>
                <li><a href="consultarodanteserie.php" target="centro">Por S&eacute;rie</a></li>
              </ul>
          </li>
          <li><a href="consultarlocal.php" target="centro">Local</a></li>
        </ul>
      </li>
      <li><a class="MenuBarItemSubmenu" href="#">Listar</a>
      	<ul>
          <li><a href="#" class="MenuBarItemSubmenu">Material Rodante</a>
              <ul>
              	<li><a href="listarrodante.php?Categoria=5" target="centro">Automotrizes / TU's</a></li>
                <li><a href="listarrodante.php?Categoria=4" target="centro">Autos de Linha</a></li>
                <li><a href="listarrodante.php?Categoria=3" target="centro">Carros</a></li>
                <li><a href="listarrodante.php?Categoria=1" target="centro">Locomotivas</a></li>
                <li><a href="listarrodante.php?Categoria=2" target="centro">Vagões</a></li>
              </ul>
          </li>
          <li><a href="#" class="MenuBarItemSubmenu">Outros</a>
              <ul>
                <li><a href="listarlinks.php" target="centro">Links</a></li>
                <li><a href="listarprefixos.php" target="centro">Prefixos</a></li>
              </ul>
          </li>
        </ul>
      </li>
      <li><a class="MenuBarItemSubmenu" href="#">Ferramentas</a>
          <ul>
            <li><a href="digito.php" target="centro">C&aacute;lculo do D.V.</a></li>
          </ul>
      </li>
    </ul>
    </th>
    <td valign="center" width="770" background="images/frame_fundo.jpg" style="background-position:center; background-repeat:no-repeat;"><iframe id="centro" height="500" align="middle" width="100%" name="centro" frameborder="0" src="<? echo $url; ?>"></iframe></td>
  </tr>
  <tr height="21">
    <th colspan="2" align="center" background="images/footer_fundo.jpg" scope="row">&nbsp;</th>
  </tr>
</table></div>
<script type="text/javascript">
<!--
var MenuBar1 = new Spry.Widget.MenuBar("MenuBar1", {imgRight:"SpryAssets/SpryMenuBarRightHover.gif"});
//-->
</script>
</body>
</html>
