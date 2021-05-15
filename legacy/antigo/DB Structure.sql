DB Structure

# tblCategorias
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblCategorias (
CodCategoria 		INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
NomeCategoria 		VARCHAR(255)	NOT NULL								COMMENT 'Nome da categoria',
DetalhesCategoria	BLOB			NULL									COMMENT 'Detalhes da categoria',
CategoriaLocal 		BOOLEAN			NOT NULL	DEFAULT FALSE				COMMENT 'Se é categoria de local',
CategoriaFoto 		BOOLEAN			NOT NULL	DEFAULT FALSE				COMMENT 'Se é categoria de foto',
CategoriaVideo		BOOLEAN			NOT NULL	DEFAULT FALSE				COMMENT 'Se é categoria de vídeo',
CategoriaRodante	BOOLEAN			NOT NULL	DEFAULT FALSE				COMMENT 'Se é categoria de material rodante',
CategoriaDocumento	BOOLEAN			NOT NULL	DEFAULT FALSE				COMMENT 'Se é categoria de documento',
CategoriaPlanta		BOOLEAN			NOT NULL	DEFAULT FALSE				COMMENT 'Se é categoria de planta',
CategoriaLink 		BOOLEAN			NOT NULL	DEFAULT FALSE				COMMENT 'Se é categoria de link',
CategoriaPergunta	BOOLEAN			NOT NULL	DEFAULT FALSE				COMMENT 'Se é categoria de pergunta',
CodUsuarioCriado	INT(8)			NOT NULL								COMMENT 'Código do usuário criador',
DataInserido		TIMESTAMP		NOT NULL	DEFAULT CURRENT_TIMESTAMP	COMMENT 'Data da inserção no sistema',
CodUsuarioMod		INT(8)			NULL									COMMENT 'Cód. do último usuário que modificou',
DataModificacao		TIMESTAMP		NULL									COMMENT 'Data da última modificação',
MotivoModificacao	VARCHAR(255)	NULL									COMMENT 'Motivo da última modificação'
) Engine = MyISAM COMMENT = 'Tabela com as categorias gerais do sistema';

# tblBitola
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblBitola (
CodBitola			INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
NomeBitola 			VARCHAR(255)	NOT NULL								COMMENT 'Nome da bitola',
DetalhesBitola		BLOB			NULL									COMMENT 'Detalhes da bitola',
CodUsuarioCriado	INT(8)			NOT NULL								COMMENT 'Código do usuário criador',
DataInserido		TIMESTAMP		NOT NULL	DEFAULT CURRENT_TIMESTAMP	COMMENT 'Data da inserção no sistema',
CodUsuarioMod		INT(8)			NULL									COMMENT 'Cód. do último usuário que modificou',
DataModificacao		TIMESTAMP		NULL									COMMENT 'Data da última modificação',
MotivoModificacao	VARCHAR(255)	NULL									COMMENT 'Motivo da última modificação'
) Engine = MyISAM COMMENT = 'Tabela com as bitolas possíveis';

# tblFerrovias
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblFerrovias (
CodFerrovia			INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
NomeFerrovia		VARCHAR(255)	NOT NULL								COMMENT 'Nome da ferrovia',
CodBitola			INT(8)			NOT NULL								COMMENT 'Código da bitola da ferrovia',
DetalhesFerrovia	BLOB			NULL									COMMENT 'Detalhes da Ferrovia',
CodUsuarioCriado	INT(8)			NOT NULL								COMMENT 'Código do usuário criador',
DataInserido		TIMESTAMP		NOT NULL	DEFAULT CURRENT_TIMESTAMP	COMMENT 'Data da inserção no sistema',
CodUsuarioMod		INT(8)			NULL									COMMENT 'Cód. do último usuário que modificou',
DataModificacao		TIMESTAMP		NULL									COMMENT 'Data da última modificação',
MotivoModificacao	VARCHAR(255)	NULL									COMMENT 'Motivo da última modificação'
) Engine = MyISAM COMMENT = 'Tabela com as ferrovias';

# tblEstado
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblEstado (
CodEstado 			INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
NomeEstado 			VARCHAR(255)	NOT NULL								COMMENT 'Nome do estado',
DetalhesEstado		BLOB			NULL									COMMENT 'Detalhes do estado',
EstadoRodante 		BOOLEAN			NOT NULL	DEFAULT FALSE				COMMENT 'Se é estado de material rodante',
EstadoLocal 		BOOLEAN			NOT NULL	DEFAULT FALSE				COMMENT 'Se é estado de um local',
CodUsuarioCriado	INT(8)			NOT NULL								COMMENT 'Código do usuário criador',
DataInserido		TIMESTAMP		NOT NULL	DEFAULT CURRENT_TIMESTAMP	COMMENT 'Data da inserção no sistema',
CodUsuarioMod		INT(8)			NULL									COMMENT 'Cód. do último usuário que modificou',
DataModificacao		TIMESTAMP		NULL									COMMENT 'Data da última modificação',
MotivoModificacao	VARCHAR(255)	NULL									COMMENT 'Motivo da última modificação'
) Engine = MyISAM COMMENT = 'Tabela com os estados (ativo, baixado, demolido, etc)';


# tblLocal
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblLocal (
CodLocal			INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
SiglaLocal			VARCHAR(3)		NOT NULL	DEFAULT '---'				COMMENT 'Sigla de 3 letras do local (ex: LUS)'	
CodCategoria 		INT(8)			NOT NULL								COMMENT 'Código da categoria do local',
NomeLocal 			VARCHAR(255)	NOT NULL								COMMENT 'Nome do local',
CodBitola			INT(8)			NOT NULL								COMMENT 'Código da bitola do local',
LatitudeLocal		VARCHAR(255)	NOT NULL								COMMENT 'Latitude do local',
LongituteLocal		VARCHAR(255)	NOT NULL								COMMENT 'Longitude do local',
CodEstado 			INT(8)			NOT NULL								COMMENT 'Código do estado do local',
DetalhesLocal		BLOB			NULL									COMMENT 'Detalhes do local',
CodUsuarioCriado	INT(8)			NOT NULL								COMMENT 'Código do usuário criador',
DataInserido		TIMESTAMP		NOT NULL	DEFAULT CURRENT_TIMESTAMP	COMMENT 'Data da inserção no sistema',
CodUsuarioMod		INT(8)			NULL									COMMENT 'Cód. do último usuário que modificou',
DataModificacao		TIMESTAMP		NULL									COMMENT 'Data da última modificação',
MotivoModificacao	VARCHAR(255)	NULL									COMMENT 'Motivo da última modificação'
) Engine = MyISAM COMMENT = 'Tabela com os locais (pátios, estações, etc)';


# tblFerroviaLocal
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblFerroviaLocal (
CodFerroviaLocal	INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
CodLocal 			INT(8)			NOT NULL							 	COMMENT 'Código do local',
CodFerrovia 		INT(8)			NOT NULL								COMMENT 'Código da ferrovia',
AnoInicio			INT(4)			NOT NULL	DEFAULT '0000'				COMMENT 'Ano de início da ferrovia no local',
AnoFinal			INT(4)			NOT NULL	DEFAULT '9999'				COMMENT 'Ano de término da ferrovia no local',
DetalhesFerLocal	BLOB			NULL									COMMENT 'Detalhes da ferrovia no local',
CodUsuarioCriado	INT(8)			NOT NULL								COMMENT 'Código do usuário criador',
DataInserido		TIMESTAMP		NOT NULL	DEFAULT CURRENT_TIMESTAMP	COMMENT 'Data da inserção no sistema',
CodUsuarioMod		INT(8)			NULL									COMMENT 'Cód. do último usuário que modificou',
DataModificacao		TIMESTAMP		NULL									COMMENT 'Data da última modificação',
MotivoModificacao	VARCHAR(255)	NULL									COMMENT 'Motivo da última modificação'
) Engine = MyISAM COMMENT = 'Tabela com as ferrovias que já operaram em determinado local';

# tblModelo
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblModelo (
CodModelo			INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
CodCategoria		INT(8)			NOT NULL								COMMENT 'Código da categoria do mat. rodante',
CodTracaoLoco		INT(8)			NOT NULL	DEFAULT '0'					COMMENT 'Código do tipo de tração da loco',
CodTipoVag 			INT(8)			NOT NULL	DEFAULT '0'					COMMENT 'Código do tipo de vagão',
CodPesoVag 			INT(8)			NOT NULL	DEFAULT '0'					COMMENT 'Código do peso do vagão',
CodTipoCarro		INT(8)			NOT NULL	DEFAULT '0'					COMMENT 'Código do tipo de carro',
CodMatCarro			INT(8)			NOT NULL	DEFAULT '0'					COMMENT 'Código do material do carro',
CodTipoAuto			INT(8)			NOT NULL	DEFAULT '0'					COMMENT 'Código do tipo de auto de linha',
CodTipoMotriz		INT(8)			NOT NULL	DEFAULT '0'					COMMENT 'Código do tipo de automotriz',
DetalhesModelo		BLOB			NULL									COMMENT 'Detalhes do modelo',
CodUsuarioCriado	INT(8)			NOT NULL								COMMENT 'Código do usuário criador',
DataInserido		TIMESTAMP		NOT NULL	DEFAULT CURRENT_TIMESTAMP	COMMENT 'Data da inserção no sistema',
CodUsuarioMod		INT(8)			NULL									COMMENT 'Cód. do último usuário que modificou',
DataModificacao		TIMESTAMP		NULL									COMMENT 'Data da última modificação',
MotivoModificacao	VARCHAR(255)	NULL									COMMENT 'Motivo da última modificação'
) Engine = MyISAM COMMENT = 'Tabela com os modelos de material rodante';


# tblFabricante
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblFabricante (
CodFabricante		INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
NomeFabricante		VARCHAR(255)	NOT NULL								COMMENT 'Nome do fabricante',
DescFabricante		BLOB			NULL									COMMENT 'Detalhes do fabricante',
SiteFabricante		VARCHAR(255)	NULL									COMMENT 'Site do fabricante',
CodUsuarioCriado	INT(8)			NOT NULL								COMMENT 'Código do usuário criador',
DataInserido		TIMESTAMP		NOT NULL	DEFAULT CURRENT_TIMESTAMP	COMMENT 'Data da inserção no sistema',
CodUsuarioMod		INT(8)			NULL									COMMENT 'Cód. do último usuário que modificou',
DataModificacao		TIMESTAMP		NULL									COMMENT 'Data da última modificação',
MotivoModificacao	VARCHAR(255)	NULL									COMMENT 'Motivo da última modificação'
) Engine = MyISAM COMMENT = 'Tabela com os fabricantes';


# tblTracaoLoco
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblTracaoLoco (
CodTracaoLoco		INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
NomeTracaoLoco		VARCHAR(255)	NOT NULL								COMMENT 'Nome do tipo de tração',
DetalhesTracaoLoco	BLOB			NULL									COMMENT 'Detalhes do tipo de tração',
CodUsuarioCriado	INT(8)			NOT NULL								COMMENT 'Código do usuário criador',
DataInserido		TIMESTAMP		NOT NULL	DEFAULT CURRENT_TIMESTAMP	COMMENT 'Data da inserção no sistema',
CodUsuarioMod		INT(8)			NULL									COMMENT 'Cód. do último usuário que modificou',
DataModificacao		TIMESTAMP		NULL									COMMENT 'Data da última modificação',
MotivoModificacao	VARCHAR(255)	NULL									COMMENT 'Motivo da última modificação'
) Engine = MyISAM COMMENT = 'Tabela com os tipos de tração possíveis para locomotivas';


# tblTipoVag
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblTipoVag (
CodTipoVag 			INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
SiglaTipoVag		VARCHAR(2)		NOT NULL								COMMENT 'Sigla do tipo de vagão (ex: FH)',
NomeTipoVag			VARCHAR(255)	NOT NULL								COMMENT 'Nome do tipo de vagão',
DetalhesTipoVag		BLOB			NULL									COMMENT 'Detalhes da tipo de vagão',
CodUsuarioCriado	INT(8)			NOT NULL								COMMENT 'Código do usuário criador',
DataInserido		TIMESTAMP		NOT NULL	DEFAULT CURRENT_TIMESTAMP	COMMENT 'Data da inserção no sistema',
CodUsuarioMod		INT(8)			NULL									COMMENT 'Cód. do último usuário que modificou',
DataModificacao		TIMESTAMP		NULL									COMMENT 'Data da última modificação',
MotivoModificacao	VARCHAR(255)	NULL									COMMENT 'Motivo da última modificação'
) Engine = MyISAM COMMENT = 'Tabela com os tipos de vagão e suas descrições';


# tblPesoVag
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblPesoVag (
CodPesoVag			INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
LetraPesoVag		VARCHAR(1)		NOT NULL								COMMENT 'Letra do peso do vagão (ex: E)',
PesoVag 			INT(3)			NOT NULL								COMMENT 'Peso em toneladas (ex: 100)'
DetalhesPesoVag		BLOB			NULL									COMMENT 'Detalhes da XXXX',
CodUsuarioCriado	INT(8)			NOT NULL								COMMENT 'Código do usuário criador',
DataInserido		TIMESTAMP		NOT NULL	DEFAULT CURRENT_TIMESTAMP	COMMENT 'Data da inserção no sistema',
CodUsuarioMod		INT(8)			NULL									COMMENT 'Cód. do último usuário que modificou',
DataModificacao		TIMESTAMP		NULL									COMMENT 'Data da última modificação',
MotivoModificacao	VARCHAR(255)	NULL									COMMENT 'Motivo da última modificação'
) Engine = MyISAM COMMENT = 'Tabela com os pesos dos vagões e suas descrições';


# tblTipoCarro
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblTipoCarro (
CodTipoCarro 		INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
LetraTipoCarro 		VARCHAR(1)		NOT NULL								COMMENT 'Letra do tipo de carro, ex: P',
NomeTipoCarro		VARCHAR(255)	NOT NULL								COMMENT 'Nome do tipo de carro, ex: 1ª Classe',
DetalhesTipoCarro	BLOB			NULL									COMMENT 'Detalhes do tipo de carro',
CodUsuarioCriado	INT(8)			NOT NULL								COMMENT 'Código do usuário criador',
DataInserido		TIMESTAMP		NOT NULL	DEFAULT CURRENT_TIMESTAMP	COMMENT 'Data da inserção no sistema',
CodUsuarioMod		INT(8)			NULL									COMMENT 'Cód. do último usuário que modificou',
DataModificacao		TIMESTAMP		NULL									COMMENT 'Data da última modificação',
MotivoModificacao	VARCHAR(255)	NULL									COMMENT 'Motivo da última modificação'
) Engine = MyISAM COMMENT = 'Tabela com os tipos de carro e suas descrições';


# tblMatCarro
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblMatCarro (
CodMatCarro 		INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
LetraMatCarro 		VARCHAR(1)		NOT NULL								COMMENT 'Letra do material do carro (ex: C)'
NomeMatCarro		VARCHAR(255)	NOT NULL								COMMENT 'Nome do mat. do carro (ex: carbono)',
DetalhesMatCarro	BLOB			NULL									COMMENT 'Detalhes do material do carro',
CodUsuarioCriado	INT(8)			NOT NULL								COMMENT 'Código do usuário criador',
DataInserido		TIMESTAMP		NOT NULL	DEFAULT CURRENT_TIMESTAMP	COMMENT 'Data da inserção no sistema',
CodUsuarioMod		INT(8)			NULL									COMMENT 'Cód. do último usuário que modificou',
DataModificacao		TIMESTAMP		NULL									COMMENT 'Data da última modificação',
MotivoModificacao	VARCHAR(255)	NULL									COMMENT 'Motivo da última modificação'
) Engine = MyISAM COMMENT = 'Tabela com os materiais de fabricação dos carros';


# tblTipoAuto
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblTipoAuto (
CodTipoAuto			INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
SiglaTipoAuto		VARCHAR(10)		NOT NULL								COMMENT 'Sigla do tipo de auto (ex: SLP)'
NomeTipoAuto		VARCHAR(255)	NOT NULL								COMMENT 'Nome do tipo de auto (ex: Socadora..)',
DetalhesTipoAuto	BLOB			NULL									COMMENT 'Detalhes do tipo de auto',
CodUsuarioCriado	INT(8)			NOT NULL								COMMENT 'Código do usuário criador',
DataInserido		TIMESTAMP		NOT NULL	DEFAULT CURRENT_TIMESTAMP	COMMENT 'Data da inserção no sistema',
CodUsuarioMod		INT(8)			NULL									COMMENT 'Cód. do último usuário que modificou',
DataModificacao		TIMESTAMP		NULL									COMMENT 'Data da última modificação',
MotivoModificacao	VARCHAR(255)	NULL									COMMENT 'Motivo da última modificação'
) Engine = MyISAM COMMENT = 'Tabela com os tipos de auto de linha';


# tblTipoMotriz
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblTipoMotriz (
CodTipoMotriz		INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
SiglaTipoMotriz		VARCHAR(10)		NOT NULL								COMMENT 'Sigla do tipo de automotriz (ex: MH)',
NomeTipoMotriz		VARCHAR(255)	NOT NULL								COMMENT 'Nome do tipo de automotriz',
DetalhesTipoMotriz	BLOB			NULL									COMMENT 'Detalhes do tipo de automotriz',
CodUsuarioCriado	INT(8)			NOT NULL								COMMENT 'Código do usuário criador',
DataInserido		TIMESTAMP		NOT NULL	DEFAULT CURRENT_TIMESTAMP	COMMENT 'Data da inserção no sistema',
CodUsuarioMod		INT(8)			NULL									COMMENT 'Cód. do último usuário que modificou',
DataModificacao		TIMESTAMP		NULL									COMMENT 'Data da última modificação',
MotivoModificacao	VARCHAR(255)	NULL									COMMENT 'Motivo da última modificação'
) Engine = MyISAM COMMENT = 'Tabela com os tipos de automotriz';


# tblFerroviaRodante
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblFerroviaRodante (
CodFerroviaRodante	INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',	
CodRodante			INT(8)			NOT NULL	 							COMMENT 'Código do material rodante',
CodFerrovia 		INT(8)			NOT NULL								COMMENT 'Código da ferrovia',
AnoInicio			INT(4)			NOT NULL	DEFAULT '0000'				COMMENT 'Ano de início da ferrovia no rodante',
AnoFinal			INT(4)			NOT NULL	DEFAULT '9999'				COMMENT 'Ano de término da ferrovia no rodante',
DetalhesFerRodante	BLOB			NULL									COMMENT 'Detalhes da ferrovia no rodante',
CodUsuarioCriado	INT(8)			NOT NULL								COMMENT 'Código do usuário criador',
DataInserido		TIMESTAMP		NOT NULL	DEFAULT CURRENT_TIMESTAMP	COMMENT 'Data da inserção no sistema',
CodUsuarioMod		INT(8)			NULL									COMMENT 'Cód. do último usuário que modificou',
DataModificacao		TIMESTAMP		NULL									COMMENT 'Data da última modificação',
MotivoModificacao	VARCHAR(255)	NULL									COMMENT 'Motivo da última modificação'
) Engine = MyISAM COMMENT = 'Tabela com as ferrovias do material rodante';


# tblLocalRodante
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblLocalRodante (
CodLocalRodante		INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
CodRodante			INT(8)			NOT NULL							 	COMMENT 'Código do material rodante',
CodLocal 			INT(8)			NOT NULL								COMMENT 'Código do local',
DataLocal 			TIMESTAMP 		NOT NULL	DEFAULT '0'					COMMENT 'Data que o rodante foi visto no local',
DetalhesLocRodante	BLOB			NULL									COMMENT 'Detalhes do local do rodante',
CodUsuarioCriado	INT(8)			NOT NULL								COMMENT 'Código do usuário criador',
DataInserido		TIMESTAMP		NOT NULL	DEFAULT CURRENT_TIMESTAMP	COMMENT 'Data da inserção no sistema',
CodUsuarioMod		INT(8)			NULL									COMMENT 'Cód. do último usuário que modificou',
DataModificacao		TIMESTAMP		NULL									COMMENT 'Data da última modificação',
MotivoModificacao	VARCHAR(255)	NULL									COMMENT 'Motivo da última modificação'
) Engine = MyISAM COMMENT = 'Tabela com os locais que os mat. rodante foram vistos';


# tblRodante
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblRodante (
CodRodante			INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
CodCategoria 		INT(8)			NOT NULL								COMMENT 'Código da categoria do rodante',
TemDV				BOOLEAN			NOT NULL	DEFAULT FALSE				COMMENT 'Se tem dígito verificador',
Numero				VARCHAR(6)		NOT NULL								COMMENT 'Número do mat. rodante',
Digito				VARCHAR(1)		NOT NULL	DEFAULT 'X'					COMMENT 'Número do dígito verificador',
CodModelo 			INT(8)			NOT NULL								COMMENT 'Código do modelo do mat. rodante',
CodEstado 			INT(8)			NOT NULL								COMMENT 'Código do estado do mat. rodante',
SabeFabricante		BOOLEAN			NOT NULL	DEFAULT FALSE				COMMENT 'Se o fabricante é conhecido',
CodFabricante		INT(8)			NOT NULL	DEFAULT '0'					COMMENT 'Código do fabricante do mat. rodante',
SabeDataFab			BOOLEAN			NOT NULL	DEFAULT FALSE				COMMENT 'Se a data de fabricação é conhecida',
DataFabricacao		TIMESTAMP 		NOT NULL	DEFAULT '0'					COMMENT 'Data de fabricação do mat. rodante',
TemRegional			BOOLEAN			NOT NULL	DEFAULT FALSE				COMMENT 'Se tem regional',
CodRegional			INT(8)			NOT NULL	DEFAULT '0'					COMMENT 'Código da regional',
DetalhesRodante		BLOB			NULL									COMMENT 'Detalhes do mat. rodante',
CodUsuarioCriado	INT(8)			NOT NULL								COMMENT 'Código do usuário criador',
DataInserido		TIMESTAMP		NOT NULL	DEFAULT CURRENT_TIMESTAMP	COMMENT 'Data da inserção no sistema',
CodUsuarioMod		INT(8)			NULL									COMMENT 'Cód. do último usuário que modificou',
DataModificacao		TIMESTAMP		NULL									COMMENT 'Data da última modificação',
MotivoModificacao	VARCHAR(255)	NULL									COMMENT 'Motivo da última modificação'
) Engine = MyISAM COMMENT = 'Tabela com os materaiais rodantes';


# tblRegional
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblRegional (
CodRegional			INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
LetraRegional		VARCHAR(1)		NOT NULL								COMMENT 'Letra da regional (ex: Z)',
NomeRegional		VARCHAR(255)	NOT NULL								COMMENT 'Nome da regional (ex: ex-Fepasa)',
DetalhesRegional	BLOB			NULL									COMMENT 'Detalhes da regional',
CodUsuarioCriado	INT(8)			NOT NULL								COMMENT 'Código do usuário criador',
DataInserido		TIMESTAMP		NOT NULL	DEFAULT CURRENT_TIMESTAMP	COMMENT 'Data da inserção no sistema',
CodUsuarioMod		INT(8)			NULL									COMMENT 'Cód. do último usuário que modificou',
DataModificacao		TIMESTAMP		NULL									COMMENT 'Data da última modificação',
MotivoModificacao	VARCHAR(255)	NULL									COMMENT 'Motivo da última modificação'
) Engine = MyISAM COMMENT = 'Tabela com as regionais';


# tblLink
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblLink (
CodLink 			INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
CodCategoria 		INT(8)			NOT NULL								COMMENT 'Código da categoria do site',
SiteLink			VARCHAR(255)	NOT NULL								COMMENT 'URL do site',
NomeLink			VARCHAR(255)	NOT NULL								COMMENT 'Nome do site',
DetalhesLink		BLOB			NULL									COMMENT 'Detalhes do site',
CodUsuarioCriado	INT(8)			NOT NULL								COMMENT 'Código do usuário criador',
DataInserido		TIMESTAMP		NOT NULL	DEFAULT CURRENT_TIMESTAMP	COMMENT 'Data da inserção no sistema',
CodUsuarioMod		INT(8)			NULL									COMMENT 'Cód. do último usuário que modificou',
DataModificacao		TIMESTAMP		NULL									COMMENT 'Data da última modificação',
MotivoModificacao	VARCHAR(255)	NULL									COMMENT 'Motivo da última modificação'
) Engine = MyISAM COMMENT = 'Tabela com os links';


# tblRelacao
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblRelacao (
CodRelacao			INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
CodCategoria1		INT(8)			NOT NULL								COMMENT 'Código da categoria do primeiro item',
CodItem1			INT(8)			NOT NULL								COMMENT 'Código do primeiro item',
CodCategoria2		INT(8)			NOT NULL								COMMENT 'Código da categoria do segundo item',
CodItem2			INT(8)			NOT NULL								COMMENT 'Código do segundo item',
DescRelacao			BLOB			NULL									COMMENT 'Detalhes da relação',
CodUsuarioCriado	INT(8)			NOT NULL								COMMENT 'Código do usuário criador',
DataInserido		TIMESTAMP		NOT NULL	DEFAULT CURRENT_TIMESTAMP	COMMENT 'Data da inserção no sistema',
CodUsuarioMod		INT(8)			NULL									COMMENT 'Cód. do último usuário que modificou',
DataModificacao		TIMESTAMP		NULL									COMMENT 'Data da última modificação',
MotivoModificacao	VARCHAR(255)	NULL									COMMENT 'Motivo da última modificação'
) Engine = MyISAM COMMENT = 'Tabela com as relações';


# tblDocumento
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblDocumento (
CodDocumento		INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
CodCategoria		INT(8)			NOT NULL								COMMENT 'Categoria do documento',
NomeDocumento		VARCHAR(255)	NOT NULL								COMMENT 'Nome do documento',
KeywordsDocumento	VARCHAR(255)	NULL									COMMENT 'Palavras chave do documento (sep ,)',
CaminhoDocumento	VARCHAR(255)	NOT NULL								COMMENT 'Caminho do documento',
DetalhesDocumento	BLOB			NULL									COMMENT 'Detalhes do documento',
CodUsuarioCriado	INT(8)			NOT NULL								COMMENT 'Código do usuário criador',
DataInserido		TIMESTAMP		NOT NULL	DEFAULT CURRENT_TIMESTAMP	COMMENT 'Data da inserção no sistema',
CodUsuarioMod		INT(8)			NULL									COMMENT 'Cód. do último usuário que modificou',
DataModificacao		TIMESTAMP		NULL									COMMENT 'Data da última modificação',
MotivoModificacao	VARCHAR(255)	NULL									COMMENT 'Motivo da última modificação'
) Engine = MyISAM COMMENT = 'Tabela com os documentos';


# tblPlanta
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblPlanta (
CodPlanta			INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
CodCategoria 		INT(8)			NOT NULL								COMMENT 'Categoria da planta',
NomePlanta			VARCHAR(255)	NOT NULL								COMMENT 'Nome da planta',
KeywordsPlanta		VARCHAR(255)	NULL									COMMENT 'Palavras chave da planta (sep ,)',
CaminhoPlanta		VARCHAR(255)	NOT NULL								COMMENT 'Caminho da planta',
DetalhesPlanta		BLOB			NULL									COMMENT 'Detalhes da planta',
CodUsuarioCriado	INT(8)			NOT NULL								COMMENT 'Código do usuário criador',
DataInserido		TIMESTAMP		NOT NULL	DEFAULT CURRENT_TIMESTAMP	COMMENT 'Data da inserção no sistema',
CodUsuarioMod		INT(8)			NULL									COMMENT 'Cód. do último usuário que modificou',
DataModificacao		TIMESTAMP		NULL									COMMENT 'Data da última modificação',
MotivoModificacao	VARCHAR(255)	NULL									COMMENT 'Motivo da última modificação'
) Engine = MyISAM COMMENT = 'Tabela com as plantas';


# tblFoto
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblFoto (
CodFoto				INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
CodCategoria 		INT(8)			NOT NULL								COMMENT 'Código da categoria da foto',
TituloFoto			VARCHAR(255)	NOT NULL								COMMENT 'Título da foto',
KeywordsFoto		VARCHAR(255)	NOT NULL								COMMENT 'Palavras chave da foto',
FotoPropria			BOOLEAN			NOT NULL	DEFAULT FALSE				COMMENT 'Se é autoria própria',
AutorFoto			VARCHAR(255)	NULL									COMMENT 'Nome do autor (se for terceiro)',
SabeDataFoto		BOOLEAN			NOT NULL	DEFAULT FALSE				COMMENT 'Se a data da foto é conhecida',
DataFoto			TIMESTAMP 		NOT NULL								COMMENT 'Data da foto',
DetalhesFoto		BLOB			NULL									COMMENT 'Detalhes da foto',
CaminhoFoto			VARCHAR(255)	NOT NULL								COMMENT 'Caminho da foto',
CodUsuarioCriado	INT(8)			NOT NULL								COMMENT 'Código do usuário criador',
DataInserido		TIMESTAMP		NOT NULL	DEFAULT CURRENT_TIMESTAMP	COMMENT 'Data da inserção no sistema',
CodUsuarioMod		INT(8)			NULL									COMMENT 'Cód. do último usuário que modificou',
DataModificacao		TIMESTAMP		NULL									COMMENT 'Data da última modificação',
MotivoModificacao	VARCHAR(255)	NULL									COMMENT 'Motivo da última modificação'
) Engine = MyISAM COMMENT = 'Tabela com as fotos';


# tblVideo
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblVideo (
CodVideo			INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
CodCategoria 		INT(8)			NOT NULL								COMMENT 'Código da categoria do vídeo',
TituloVideo			VARCHAR(255)	NOT NULL								COMMENT 'Título do vídeo',
KeywordsVideo		VARCHAR(255)	NOT NULL								COMMENT 'Palavras chave do vídeo',
VideoProprio		BOOLEAN			NOT NULL	DEFAULT FALSE				COMMENT 'Se é autoria própria',
AutorVideo			VARCHAR(255)	NULL									COMMENT 'Nome do autor (se for terceiro)',
SabeDataVideo		BOOLEAN			NOT NULL	DEFAULT FALSE				COMMENT 'Se a data da foto é conhecida',
DataVideo			TIMESTAMP 		NOT NULL								COMMENT 'Data da filmagem',
DetalhesVideo		BLOB			NULL									COMMENT 'Detalhes do vídeo',
CaminhoVideo		VARCHAR(255)	NOT NULL								COMMENT 'Caminho do video',
CodUsuarioCriado	INT(8)			NOT NULL								COMMENT 'Código do usuário criador',
DataInserido		TIMESTAMP		NOT NULL	DEFAULT CURRENT_TIMESTAMP	COMMENT 'Data da inserção no sistema',
CodUsuarioMod		INT(8)			NULL									COMMENT 'Cód. do último usuário que modificou',
DataModificacao		TIMESTAMP		NULL									COMMENT 'Data da última modificação',
MotivoModificacao	VARCHAR(255)	NULL									COMMENT 'Motivo da última modificação'
) Engine = MyISAM COMMENT = 'Tabela com os vídeos';


# tblFeed
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblFeed (
CodEvento			INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
CodCategoria 		INT(8)			NOT NULL								COMMENT 'Código da categoria do item',
CodItem 			INT(8)			NOT NULL								COMMENT 'Código do item',
NovoOuModificado	BOOLEAN			NOT NULL	DEFAULT FALSE				COMMENT 'Se é novo ou foi uma edição',
DataEvento			TIMESTAMP		NOT NULL	DEFAULT CURRENT_TIMESTAMP	COMMENT 'Data da publicação',
CodUsuario 			INT(8)			NOT NULL	DEFAULT '0'					COMMENT 'Código do usuário autor',
) Engine = MyISAM COMMENT = 'Tabela com as publicações do feed';


# tblCurtidas
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblCurtidas (
CodCurtida 			INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
CodCategoria 		INT(8)			NOT NULL								COMMENT 'Código da categoria do item curtido',
CodItem 			INT(8)			NOT NULL								COMMENT 'Código do item curtido',
DataCurtida			TIMESTAMP		NOT NULL	DEFAULT CURRENT_TIMESTAMP	COMMENT 'Data da curtida',
CodUsuarioCurtida	INT(8)			NOT NULL								COMMENT 'Código do usuário que curtiu',
) Engine = MyISAM COMMENT = 'Tabela com as curtidas';


# tblComentarios
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblComentarios (
CodComentario		INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código do comentário',
CodCategoria 		INT(8)			NOT NULL								COMMENT 'Código da categoria do item comentado',
CodItem 			INT(8)			NOT NULL								COMMENT 'Código do item comentado',
TextoComentario		BLOB			NULL									COMMENT 'Texto do comentário',
DataComentario		TIMESTAMP		NOT NULL	DEFAULT CURRENT_TIMESTAMP	COMMENT 'Data do comentário',
CodUsuarioComent	INT(8)			NOT NULL								COMMENT 'Código do usuário que comentou',
) Engine = MyISAM COMMENT = 'Tabela com os comentários';


# tblUsuario
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblUsuario (
CodUsuario 			INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
NomeUsuario			VARCHAR(255)	NOT NULL								COMMENT 'a',
SenhaUsuario		VARCHAR(255)	NOT NULL								COMMENT 'a',
EmailUsuario		VARCHAR(255)	NOT NULL								COMMENT 'a',
ExibeEmail			BOOLEAN			NOT NULL	DEFAULT FALSE				COMMENT 'Se é XXXXXXX',
CelularUsuario		VARCHAR(255)	NOT NULL								COMMENT 'a',
ExibeCelular		BOOLEAN			NOT NULL	DEFAULT FALSE				COMMENT 'Se é XXXXXXX',
TelefoneUsuario		VARCHAR(255)	NOT NULL								COMMENT 'a',
ExibeTelefone		BOOLEAN			NOT NULL	DEFAULT FALSE				COMMENT 'Se é XXXXXXX',
CidadeUsuario		VARCHAR(255)	NOT NULL								COMMENT 'a',
EstadoUsuario		VARCHAR(2)
ExibeLocal			BOOLEAN			NOT NULL	DEFAULT FALSE				COMMENT 'Se é XXXXXXX',
FacebookUsuario		VARCHAR(255)	NOT NULL								COMMENT 'a',
ExibeFacebook		BOOLEAN			NOT NULL	DEFAULT FALSE				COMMENT 'Se é XXXXXXX',
SkypeUsuario		VARCHAR(255)	NOT NULL								COMMENT 'a',
ExibeSkype			BOOLEAN			NOT NULL	DEFAULT FALSE				COMMENT 'Se é XXXXXXX',
NivelUsuario		| INT(1)
CodAvatar			INT(8)			NOT NULL								COMMENT 'Aaaaaaa',


# tblFotoAvatar
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tbl(
CodAvatar			INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
CaminhoAvatar		VARCHAR(255)	NOT NULL								COMMENT 'a',
CodUsuario 			INT(8)			NOT NULL								COMMENT 'Aaaaaaa',
DataEnvio 			TIMESTAMP		NOT NULL	DEFAULT CURRENT_TIMESTAMP	COMMENT 'Aaaaaaa',


# tblLog
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tbl(
CodUsuario 			INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
IP 					VARCHAR(20)
Pagina				VARCHAR(255)	NOT NULL								COMMENT 'a',
Erro				BOOLEAN			NOT NULL	DEFAULT FALSE				COMMENT 'Se é XXXXXXX',
Mensagem 			VARCHAR(255)	NOT NULL								COMMENT 'a',


# tblPerguntas
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tbl(
CodPergunta
CodCategoria
TituloPergunta
DescricaoPergunta	BLOB			NULL									COMMENT 'Detalhes da XXXX',
CodUsuarioCriado	INT(8)			NOT NULL								COMMENT 'Código do usuário criador',
DataInserido		TIMESTAMP		NOT NULL	DEFAULT CURRENT_TIMESTAMP	COMMENT 'Data da inserção no sistema',
CodUsuarioMod		INT(8)			NULL									COMMENT 'Cód. do último usuário que modificou',
DataModificacao		TIMESTAMP		NULL									COMMENT 'Data da última modificação',
MotivoModificacao	VARCHAR(255)	NULL									COMMENT 'Motivo da última modificação'
) Engine = MyISAM COMMENT = 'Tabela com as bitolas possíveis';


# tblRespostas
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tbl(
CodResposta			INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
CodPergunta			INT(8)			NOT NULL								COMMENT 'Aaaaaaa',
TextoResposta		BLOB			NULL									COMMENT 'Detalhes da XXXX',
CodUsuarioCriado	INT(8)			NOT NULL								COMMENT 'Código do usuário criador',
DataInserido		TIMESTAMP		NOT NULL	DEFAULT CURRENT_TIMESTAMP	COMMENT 'Data da inserção no sistema',
CodUsuarioMod		INT(8)			NULL									COMMENT 'Cód. do último usuário que modificou',
DataModificacao		TIMESTAMP		NULL									COMMENT 'Data da última modificação',
MotivoModificacao	VARCHAR(255)	NULL									COMMENT 'Motivo da última modificação'
) Engine = MyISAM COMMENT = 'Tabela com as bitolas possíveis';


# tblPrefixos
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tbl(
CodPrefixo
NomePrefixo
CodFerrovia
DetalhesPrefixo
CodUsuarioCriado	INT(8)			NOT NULL								COMMENT 'Código do usuário criador',
DataInserido		TIMESTAMP		NOT NULL	DEFAULT CURRENT_TIMESTAMP	COMMENT 'Data da inserção no sistema',
CodUsuarioMod		INT(8)			NULL									COMMENT 'Cód. do último usuário que modificou',
DataModificacao		TIMESTAMP		NULL									COMMENT 'Data da última modificação',
MotivoModificacao	VARCHAR(255)	NULL									COMMENT 'Motivo da última modificação'
) Engine = MyISAM COMMENT = 'Tabela com as bitolas possíveis';
