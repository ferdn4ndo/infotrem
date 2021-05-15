#############################################################################################################################
#                                                         InfoTrem                                                          #
#                                                Estrutura do Banco de Dados                                                #
#                                                                                                                           #
#                                                      DB_Structure.sql                                                     #
#                                                                                                                           #
#                                                    Fernando Constantino                                                   #
#                                                        16/04/2016                                                         #
#                                                        Versão 2.0                                                         #
#############################################################################################################################

#############################################################################################################################
# BANCO DE DADOS QUE O SCRIPT VAI UTILIZAR
#############################################################################################################################
USE 				cscco923_indev;

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
CategoriaEvento		BOOLEAN			NOT NULL	DEFAULT FALSE				COMMENT 'Se é categoria de evento',
CategoriaFeed		BOOLEAN			NOT NULL	DEFAULT FALSE 				COMMENT 'Se é categoria de feed',
CategoriaAlbum		BOOLEAN			NOT NULL	DEFAULT FALSE 				COMMENT 'Se é categoria de álbum',
CodUsuarioCriado	INT(8)			NOT NULL								COMMENT 'Código do usuário criador',
DataInserido		TIMESTAMP		NOT NULL	DEFAULT CURRENT_TIMESTAMP	COMMENT 'Data da inserção no sistema',
CodUsuarioMod		INT(8)			NULL									COMMENT 'Cód. do último usuário que modificou',
DataModificacao		TIMESTAMP		NULL									COMMENT 'Data da última modificação',
MotivoModificacao	VARCHAR(255)	NULL									COMMENT 'Motivo da última modificação',
NivelParaModificar	INT(2) 			NOT NULL	DEFAULT '99' 				COMMENT 'Nível mínimo de usuário p/ modificar'
) Engine = MyISAM 	DEFAULT CHARSET = latin1	COMMENT = 'Tabela com as categorias gerais do sistema';


# tblBitolas
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblBitolas (
CodBitola			INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
NomeBitola 			VARCHAR(255)	NOT NULL								COMMENT 'Nome da bitola',
DetalhesBitola		BLOB			NULL									COMMENT 'Detalhes da bitola',
CodUsuarioCriado	INT(8)			NOT NULL								COMMENT 'Código do usuário criador',
DataInserido		TIMESTAMP		NOT NULL	DEFAULT CURRENT_TIMESTAMP	COMMENT 'Data da inserção no sistema',
CodUsuarioMod		INT(8)			NULL									COMMENT 'Cód. do último usuário que modificou',
DataModificacao		TIMESTAMP		NULL									COMMENT 'Data da última modificação',
MotivoModificacao	VARCHAR(255)	NULL									COMMENT 'Motivo da última modificação',
NivelParaModificar	INT(2) 			NOT NULL	DEFAULT '99' 				COMMENT 'Nível mínimo de usuário p/ modificar'
) Engine = MyISAM 	DEFAULT CHARSET = latin1	COMMENT = 'Tabela com as bitolas possíveis';


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
MotivoModificacao	VARCHAR(255)	NULL									COMMENT 'Motivo da última modificação',
NivelParaModificar	INT(2) 			NOT NULL	DEFAULT '99' 				COMMENT 'Nível mínimo de usuário p/ modificar'
) Engine = MyISAM 	DEFAULT CHARSET = latin1	COMMENT = 'Tabela com as ferrovias';


# tblEstados
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblEstados (
CodEstado 			INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
NomeEstado 			VARCHAR(255)	NOT NULL								COMMENT 'Nome do estado',
DetalhesEstado		BLOB			NULL									COMMENT 'Detalhes do estado',
EstadoRodante 		BOOLEAN			NOT NULL	DEFAULT FALSE				COMMENT 'Se é estado de material rodante',
EstadoLocal 		BOOLEAN			NOT NULL	DEFAULT FALSE				COMMENT 'Se é estado de um local',
CodUsuarioCriado	INT(8)			NOT NULL								COMMENT 'Código do usuário criador',
DataInserido		TIMESTAMP		NOT NULL	DEFAULT CURRENT_TIMESTAMP	COMMENT 'Data da inserção no sistema',
CodUsuarioMod		INT(8)			NULL									COMMENT 'Cód. do último usuário que modificou',
DataModificacao		TIMESTAMP		NULL									COMMENT 'Data da última modificação',
MotivoModificacao	VARCHAR(255)	NULL									COMMENT 'Motivo da última modificação',
NivelParaModificar	INT(2) 			NOT NULL	DEFAULT '99' 				COMMENT 'Nível mínimo de usuário p/ modificar'
) Engine = MyISAM 	DEFAULT CHARSET = latin1	COMMENT = 'Tabela com os estados (ativo, baixado, demolido, etc)';


# tblLocais
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblLocais (
CodLocal			INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
SiglaLocal			VARCHAR(3)		NOT NULL	DEFAULT '---'				COMMENT 'Sigla de 3 letras do local (ex: LUS)',	
CodCategoria 		INT(8)			NOT NULL								COMMENT 'Código da categoria do local',
NomeLocal 			VARCHAR(255)	NOT NULL								COMMENT 'Nome do local',
CodBitola			INT(8)			NOT NULL								COMMENT 'Código da bitola do local',
LatitudeLocal		DECIMAL(10, 8)	NOT NULL								COMMENT 'Latitude do local',
LongituteLocal		DECIMAL(11, 8)	NOT NULL								COMMENT 'Longitude do local',
CodEstado 			INT(8)			NOT NULL								COMMENT 'Código do estado do local',
DetalhesLocal		BLOB			NULL									COMMENT 'Detalhes do local',
CodUsuarioCriado	INT(8)			NOT NULL								COMMENT 'Código do usuário criador',
DataInserido		TIMESTAMP		NOT NULL	DEFAULT CURRENT_TIMESTAMP	COMMENT 'Data da inserção no sistema',
CodUsuarioMod		INT(8)			NULL									COMMENT 'Cód. do último usuário que modificou',
DataModificacao		TIMESTAMP		NULL									COMMENT 'Data da última modificação',
MotivoModificacao	VARCHAR(255)	NULL									COMMENT 'Motivo da última modificação',
NivelParaModificar	INT(2) 			NOT NULL	DEFAULT '99' 				COMMENT 'Nível mínimo de usuário p/ modificar'
) Engine = MyISAM 	DEFAULT CHARSET = latin1	COMMENT = 'Tabela com os locais (pátios, estações, etc)';


# tblFerroviasLocal
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblFerroviasLocal (
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
MotivoModificacao	VARCHAR(255)	NULL									COMMENT 'Motivo da última modificação',
NivelParaModificar	INT(2) 			NOT NULL	DEFAULT '99' 				COMMENT 'Nível mínimo de usuário p/ modificar'
) Engine = MyISAM 	DEFAULT CHARSET = latin1	COMMENT = 'Tabela com as ferrovias que já operaram em determinado local';

# tblModelos
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblModelos (
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
MotivoModificacao	VARCHAR(255)	NULL									COMMENT 'Motivo da última modificação',
NivelParaModificar	INT(2) 			NOT NULL	DEFAULT '99' 				COMMENT 'Nível mínimo de usuário p/ modificar'
) Engine = MyISAM 	DEFAULT CHARSET = latin1	COMMENT = 'Tabela com os modelos de material rodante';


# tblFabricantes
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblFabricantes (
CodFabricante		INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
NomeFabricante		VARCHAR(255)	NOT NULL								COMMENT 'Nome do fabricante',
DescFabricante		BLOB			NULL									COMMENT 'Detalhes do fabricante',
SiteFabricante		VARCHAR(255)	NULL									COMMENT 'Site do fabricante',
CodUsuarioCriado	INT(8)			NOT NULL								COMMENT 'Código do usuário criador',
DataInserido		TIMESTAMP		NOT NULL	DEFAULT CURRENT_TIMESTAMP	COMMENT 'Data da inserção no sistema',
CodUsuarioMod		INT(8)			NULL									COMMENT 'Cód. do último usuário que modificou',
DataModificacao		TIMESTAMP		NULL									COMMENT 'Data da última modificação',
MotivoModificacao	VARCHAR(255)	NULL									COMMENT 'Motivo da última modificação',
NivelParaModificar	INT(2) 			NOT NULL	DEFAULT '99' 				COMMENT 'Nível mínimo de usuário p/ modificar'
) Engine = MyISAM 	DEFAULT CHARSET = latin1	COMMENT = 'Tabela com os fabricantes';


# tblTracoesLoco
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblTracoesLoco (
CodTracaoLoco		INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
NomeTracaoLoco		VARCHAR(255)	NOT NULL								COMMENT 'Nome do tipo de tração',
DetalhesTracaoLoco	BLOB			NULL									COMMENT 'Detalhes do tipo de tração',
CodUsuarioCriado	INT(8)			NOT NULL								COMMENT 'Código do usuário criador',
DataInserido		TIMESTAMP		NOT NULL	DEFAULT CURRENT_TIMESTAMP	COMMENT 'Data da inserção no sistema',
CodUsuarioMod		INT(8)			NULL									COMMENT 'Cód. do último usuário que modificou',
DataModificacao		TIMESTAMP		NULL									COMMENT 'Data da última modificação',
MotivoModificacao	VARCHAR(255)	NULL									COMMENT 'Motivo da última modificação',
NivelParaModificar	INT(2) 			NOT NULL	DEFAULT '99' 				COMMENT 'Nível mínimo de usuário p/ modificar'
) Engine = MyISAM 	DEFAULT CHARSET = latin1	COMMENT = 'Tabela com os tipos de tração possíveis para locomotivas';


# tblTiposVag
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblTiposVag (
CodTipoVag 			INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
SiglaTipoVag		VARCHAR(2)		NOT NULL								COMMENT 'Sigla do tipo de vagão (ex: FH)',
NomeTipoVag			VARCHAR(255)	NOT NULL								COMMENT 'Nome do tipo de vagão',
DetalhesTipoVag		BLOB			NULL									COMMENT 'Detalhes da tipo de vagão',
CodUsuarioCriado	INT(8)			NOT NULL								COMMENT 'Código do usuário criador',
DataInserido		TIMESTAMP		NOT NULL	DEFAULT CURRENT_TIMESTAMP	COMMENT 'Data da inserção no sistema',
CodUsuarioMod		INT(8)			NULL									COMMENT 'Cód. do último usuário que modificou',
DataModificacao		TIMESTAMP		NULL									COMMENT 'Data da última modificação',
MotivoModificacao	VARCHAR(255)	NULL									COMMENT 'Motivo da última modificação',
NivelParaModificar	INT(2) 			NOT NULL	DEFAULT '99' 				COMMENT 'Nível mínimo de usuário p/ modificar'
) Engine = MyISAM 	DEFAULT CHARSET = latin1	COMMENT = 'Tabela com os tipos de vagão e suas descrições';


# tblPesosVag
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblPesosVag (
CodPesoVag			INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
LetraPesoVag		VARCHAR(1)		NOT NULL								COMMENT 'Letra do peso do vagão (ex: E)',
PesoVag 			INT(3)			NOT NULL								COMMENT 'Peso em toneladas (ex: 100)',
DetalhesPesoVag		BLOB			NULL									COMMENT 'Detalhes da XXXX',
CodUsuarioCriado	INT(8)			NOT NULL								COMMENT 'Código do usuário criador',
DataInserido		TIMESTAMP		NOT NULL	DEFAULT CURRENT_TIMESTAMP	COMMENT 'Data da inserção no sistema',
CodUsuarioMod		INT(8)			NULL									COMMENT 'Cód. do último usuário que modificou',
DataModificacao		TIMESTAMP		NULL									COMMENT 'Data da última modificação',
MotivoModificacao	VARCHAR(255)	NULL									COMMENT 'Motivo da última modificação',
NivelParaModificar	INT(2) 			NOT NULL	DEFAULT '99' 				COMMENT 'Nível mínimo de usuário p/ modificar'
) Engine = MyISAM 	DEFAULT CHARSET = latin1	COMMENT = 'Tabela com os pesos dos vagões e suas descrições';


# tblTiposCarro
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblTiposCarro (
CodTipoCarro 		INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
LetraTipoCarro 		VARCHAR(1)		NOT NULL								COMMENT 'Letra do tipo de carro, ex: P',
NomeTipoCarro		VARCHAR(255)	NOT NULL								COMMENT 'Nome do tipo de carro, ex: 1ª Classe',
DetalhesTipoCarro	BLOB			NULL									COMMENT 'Detalhes do tipo de carro',
CodUsuarioCriado	INT(8)			NOT NULL								COMMENT 'Código do usuário criador',
DataInserido		TIMESTAMP		NOT NULL	DEFAULT CURRENT_TIMESTAMP	COMMENT 'Data da inserção no sistema',
CodUsuarioMod		INT(8)			NULL									COMMENT 'Cód. do último usuário que modificou',
DataModificacao		TIMESTAMP		NULL									COMMENT 'Data da última modificação',
MotivoModificacao	VARCHAR(255)	NULL									COMMENT 'Motivo da última modificação',
NivelParaModificar	INT(2) 			NOT NULL	DEFAULT '99' 				COMMENT 'Nível mínimo de usuário p/ modificar'
) Engine = MyISAM 	DEFAULT CHARSET = latin1	COMMENT = 'Tabela com os tipos de carro e suas descrições';


# tblMatCarro
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblMatCarro (
CodMatCarro 		INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
LetraMatCarro 		VARCHAR(1)		NOT NULL								COMMENT 'Letra do material do carro (ex: C)',
NomeMatCarro		VARCHAR(255)	NOT NULL								COMMENT 'Nome do mat. do carro (ex: carbono)',
DetalhesMatCarro	BLOB			NULL									COMMENT 'Detalhes do material do carro',
CodUsuarioCriado	INT(8)			NOT NULL								COMMENT 'Código do usuário criador',
DataInserido		TIMESTAMP		NOT NULL	DEFAULT CURRENT_TIMESTAMP	COMMENT 'Data da inserção no sistema',
CodUsuarioMod		INT(8)			NULL									COMMENT 'Cód. do último usuário que modificou',
DataModificacao		TIMESTAMP		NULL									COMMENT 'Data da última modificação',
MotivoModificacao	VARCHAR(255)	NULL									COMMENT 'Motivo da última modificação',
NivelParaModificar	INT(2) 			NOT NULL	DEFAULT '99' 				COMMENT 'Nível mínimo de usuário p/ modificar'
) Engine = MyISAM 	DEFAULT CHARSET = latin1	COMMENT = 'Tabela com os materiais de fabricação dos carros';


# tblTipoAuto
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblTiposAuto (
CodTipoAuto			INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
SiglaTipoAuto		VARCHAR(10)		NOT NULL								COMMENT 'Sigla do tipo de auto (ex: SLP)',
NomeTipoAuto		VARCHAR(255)	NOT NULL								COMMENT 'Nome do tipo de auto (ex: Socadora..)',
DetalhesTipoAuto	BLOB			NULL									COMMENT 'Detalhes do tipo de auto',
CodUsuarioCriado	INT(8)			NOT NULL								COMMENT 'Código do usuário criador',
DataInserido		TIMESTAMP		NOT NULL	DEFAULT CURRENT_TIMESTAMP	COMMENT 'Data da inserção no sistema',
CodUsuarioMod		INT(8)			NULL									COMMENT 'Cód. do último usuário que modificou',
DataModificacao		TIMESTAMP		NULL									COMMENT 'Data da última modificação',
MotivoModificacao	VARCHAR(255)	NULL									COMMENT 'Motivo da última modificação',
NivelParaModificar	INT(2) 			NOT NULL	DEFAULT '99' 				COMMENT 'Nível mínimo de usuário p/ modificar'
) Engine = MyISAM 	DEFAULT CHARSET = latin1	COMMENT = 'Tabela com os tipos de auto de linha';


# tblTiposMotriz
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblTiposMotriz (
CodTipoMotriz		INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
SiglaTipoMotriz		VARCHAR(10)		NOT NULL								COMMENT 'Sigla do tipo de automotriz (ex: MH)',
NomeTipoMotriz		VARCHAR(255)	NOT NULL								COMMENT 'Nome do tipo de automotriz',
DetalhesTipoMotriz	BLOB			NULL									COMMENT 'Detalhes do tipo de automotriz',
CodUsuarioCriado	INT(8)			NOT NULL								COMMENT 'Código do usuário criador',
DataInserido		TIMESTAMP		NOT NULL	DEFAULT CURRENT_TIMESTAMP	COMMENT 'Data da inserção no sistema',
CodUsuarioMod		INT(8)			NULL									COMMENT 'Cód. do último usuário que modificou',
DataModificacao		TIMESTAMP		NULL									COMMENT 'Data da última modificação',
MotivoModificacao	VARCHAR(255)	NULL									COMMENT 'Motivo da última modificação',
NivelParaModificar	INT(2) 			NOT NULL	DEFAULT '99' 				COMMENT 'Nível mínimo de usuário p/ modificar'
) Engine = MyISAM 	DEFAULT CHARSET = latin1	COMMENT = 'Tabela com os tipos de automotriz';


# tblFerroviasRodante
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblFerroviasRodante (
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
MotivoModificacao	VARCHAR(255)	NULL									COMMENT 'Motivo da última modificação',
NivelParaModificar	INT(2) 			NOT NULL	DEFAULT '99' 				COMMENT 'Nível mínimo de usuário p/ modificar'
) Engine = MyISAM 	DEFAULT CHARSET = latin1	COMMENT = 'Tabela com as ferrovias do material rodante';


# tblLocaisRodante
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblLocaisRodante (
CodLocalRodante		INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
CodRodante			INT(8)			NOT NULL							 	COMMENT 'Código do material rodante',
CodLocal 			INT(8)			NOT NULL								COMMENT 'Código do local',
DataLocal 			TIMESTAMP 		NOT NULL	DEFAULT 0					COMMENT 'Data que o rodante foi visto no local',
DetalhesLocRodante	BLOB			NULL									COMMENT 'Detalhes do local do rodante',
CodUsuarioCriado	INT(8)			NOT NULL								COMMENT 'Código do usuário criador',
DataInserido		TIMESTAMP		NOT NULL	DEFAULT CURRENT_TIMESTAMP	COMMENT 'Data da inserção no sistema',
CodUsuarioMod		INT(8)			NULL									COMMENT 'Cód. do último usuário que modificou',
DataModificacao		TIMESTAMP		NULL									COMMENT 'Data da última modificação',
MotivoModificacao	VARCHAR(255)	NULL									COMMENT 'Motivo da última modificação',
NivelParaModificar	INT(2) 			NOT NULL	DEFAULT '99' 				COMMENT 'Nível mínimo de usuário p/ modificar'
) Engine = MyISAM 	DEFAULT CHARSET = latin1	COMMENT = 'Tabela com os locais que os mat. rodante foram vistos';


# tblRodantes
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblRodantes (
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
DataFabricacao		TIMESTAMP 		NOT NULL	DEFAULT 0					COMMENT 'Data de fabricação do mat. rodante',
TemRegional			BOOLEAN			NOT NULL	DEFAULT FALSE				COMMENT 'Se tem regional',
CodRegional			INT(8)			NOT NULL	DEFAULT '0'					COMMENT 'Código da regional',
DetalhesRodante		BLOB			NULL									COMMENT 'Detalhes do mat. rodante',
CodUsuarioCriado	INT(8)			NOT NULL								COMMENT 'Código do usuário criador',
DataInserido		TIMESTAMP		NOT NULL	DEFAULT CURRENT_TIMESTAMP	COMMENT 'Data da inserção no sistema',
CodUsuarioMod		INT(8)			NULL									COMMENT 'Cód. do último usuário que modificou',
DataModificacao		TIMESTAMP		NULL									COMMENT 'Data da última modificação',
MotivoModificacao	VARCHAR(255)	NULL									COMMENT 'Motivo da última modificação',
NivelParaModificar	INT(2) 			NOT NULL	DEFAULT '99' 				COMMENT 'Nível mínimo de usuário p/ modificar'
) Engine = MyISAM 	DEFAULT CHARSET = latin1	COMMENT = 'Tabela com os materaiais rodantes';


# tblRegionais
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblRegionais (
CodRegional			INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
LetraRegional		VARCHAR(1)		NOT NULL								COMMENT 'Letra da regional (ex: Z)',
NomeRegional		VARCHAR(255)	NOT NULL								COMMENT 'Nome da regional (ex: ex-Fepasa)',
DetalhesRegional	BLOB			NULL									COMMENT 'Detalhes da regional',
CodUsuarioCriado	INT(8)			NOT NULL								COMMENT 'Código do usuário criador',
DataInserido		TIMESTAMP		NOT NULL	DEFAULT CURRENT_TIMESTAMP	COMMENT 'Data da inserção no sistema',
CodUsuarioMod		INT(8)			NULL									COMMENT 'Cód. do último usuário que modificou',
DataModificacao		TIMESTAMP		NULL									COMMENT 'Data da última modificação',
MotivoModificacao	VARCHAR(255)	NULL									COMMENT 'Motivo da última modificação',
NivelParaModificar	INT(2) 			NOT NULL	DEFAULT '99' 				COMMENT 'Nível mínimo de usuário p/ modificar'
) Engine = MyISAM 	DEFAULT CHARSET = latin1	COMMENT = 'Tabela com as regionais';


# tblLinks
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblLinks (
CodLink 			INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
CodCategoria 		INT(8)			NOT NULL								COMMENT 'Código da categoria do site',
SiteLink			VARCHAR(255)	NOT NULL								COMMENT 'URL do site',
NomeLink			VARCHAR(255)	NOT NULL								COMMENT 'Nome do site',
DetalhesLink		BLOB			NULL									COMMENT 'Detalhes do site',
CodUsuarioCriado	INT(8)			NOT NULL								COMMENT 'Código do usuário criador',
DataInserido		TIMESTAMP		NOT NULL	DEFAULT CURRENT_TIMESTAMP	COMMENT 'Data da inserção no sistema',
CodUsuarioMod		INT(8)			NULL									COMMENT 'Cód. do último usuário que modificou',
DataModificacao		TIMESTAMP		NULL									COMMENT 'Data da última modificação',
MotivoModificacao	VARCHAR(255)	NULL									COMMENT 'Motivo da última modificação',
NivelParaModificar	INT(2) 			NOT NULL	DEFAULT '99' 				COMMENT 'Nível mínimo de usuário p/ modificar'
) Engine = MyISAM 	DEFAULT CHARSET = latin1	COMMENT = 'Tabela com os links';


# tblRelacoes
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblRelacoes (
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
MotivoModificacao	VARCHAR(255)	NULL									COMMENT 'Motivo da última modificação',
NivelParaModificar	INT(2) 			NOT NULL	DEFAULT '99' 				COMMENT 'Nível mínimo de usuário p/ modificar'
) Engine = MyISAM 	DEFAULT CHARSET = latin1	COMMENT = 'Tabela com as relações';


# tblDocumentos
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblDocumentos (
CodDocumento		INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
CodCategoria		INT(8)			NOT NULL								COMMENT 'Categoria do documento',
NomeDocumento		VARCHAR(255)	NOT NULL								COMMENT 'Nome do documento',
KeywordsDocumento	VARCHAR(255)	NULL									COMMENT 'Palavras chave do documento (sep ,)',
DocumentoProprio	BOOLEAN			NOT NULL	DEFAULT FALSE				COMMENT 'Se é autoria própria',
AutorDocumento		VARCHAR(255)	NULL									COMMENT 'Nome do autor (se for terceiro)',
CaminhoDocumento	VARCHAR(255)	NOT NULL								COMMENT 'Caminho do documento',
CaminhoThumb		VARCHAR(255)	NULL									COMMENT 'Caminho da miniatura',
DetalhesDocumento	BLOB			NULL									COMMENT 'Detalhes do documento',
CodUsuarioCriado	INT(8)			NOT NULL								COMMENT 'Código do usuário criador',
DataInserido		TIMESTAMP		NOT NULL	DEFAULT CURRENT_TIMESTAMP	COMMENT 'Data da inserção no sistema',
CodUsuarioMod		INT(8)			NULL									COMMENT 'Cód. do último usuário que modificou',
DataModificacao		TIMESTAMP		NULL									COMMENT 'Data da última modificação',
MotivoModificacao	VARCHAR(255)	NULL									COMMENT 'Motivo da última modificação',
NivelParaModificar	INT(2) 			NOT NULL	DEFAULT '99' 				COMMENT 'Nível mínimo de usuário p/ modificar'
) Engine = MyISAM 	DEFAULT CHARSET = latin1	COMMENT = 'Tabela com os documentos';


# tblPlantas
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblPlantas (
CodPlanta			INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
CodCategoria 		INT(8)			NOT NULL								COMMENT 'Categoria da planta',
NomePlanta			VARCHAR(255)	NOT NULL								COMMENT 'Nome da planta',
KeywordsPlanta		VARCHAR(255)	NULL									COMMENT 'Palavras chave da planta (sep ,)',
PlantaPropria		BOOLEAN			NOT NULL	DEFAULT FALSE				COMMENT 'Se é autoria própria',
AutorPlanta			VARCHAR(255)	NULL									COMMENT 'Nome do autor (se for terceiro)',
CaminhoPlanta		VARCHAR(255)	NOT NULL								COMMENT 'Caminho da planta',
CaminhoThumb		VARCHAR(255)	NULL									COMMENT 'Caminho da miniatura',
DetalhesPlanta		BLOB			NULL									COMMENT 'Detalhes da planta',
CodUsuarioCriado	INT(8)			NOT NULL								COMMENT 'Código do usuário criador',
DataInserido		TIMESTAMP		NOT NULL	DEFAULT CURRENT_TIMESTAMP	COMMENT 'Data da inserção no sistema',
CodUsuarioMod		INT(8)			NULL									COMMENT 'Cód. do último usuário que modificou',
DataModificacao		TIMESTAMP		NULL									COMMENT 'Data da última modificação',
MotivoModificacao	VARCHAR(255)	NULL									COMMENT 'Motivo da última modificação',
NivelParaModificar	INT(2) 			NOT NULL	DEFAULT '99' 				COMMENT 'Nível mínimo de usuário p/ modificar'
) Engine = MyISAM 	DEFAULT CHARSET = latin1	COMMENT = 'Tabela com as plantas';


# tblAlbuns
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblAlbuns (
CodAlbum			INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
CodCategoria 		INT(8)			NOT NULL								COMMENT 'Código da categoria do álbum',
TituloAlbum			VARCHAR(255)	NOT NULL								COMMENT 'Título do álbum',
KeywordsAlbum		VARCHAR(255)	NOT NULL								COMMENT 'Palavras chave do álbum',
DetalhesAlbum		BLOB			NULL 									COMMENT 'Detalhes do álbum',
VisualizacoesAlbum	INT(8)			NOT NULL 	DEFAULT 0					COMMENT 'Visualizações do álbum',
CodFotoCapa			INT(8)			NOT NULL 	DEFAULT '0'					COMMENT 'Código da foto de capa do álbum',
CodUsuarioCriado	INT(8)			NOT NULL								COMMENT 'Código do usuário criador',
DataInserido		TIMESTAMP		NOT NULL	DEFAULT CURRENT_TIMESTAMP	COMMENT 'Data da inserção no sistema',
CodUsuarioMod		INT(8)			NULL									COMMENT 'Cód. do último usuário que modificou',
DataModificacao		TIMESTAMP		NULL									COMMENT 'Data da última modificação',
MotivoModificacao	VARCHAR(255)	NULL									COMMENT 'Motivo da última modificação',
NivelParaModificar	INT(2) 			NOT NULL	DEFAULT '99' 				COMMENT 'Nível mínimo de usuário p/ modificar'
) Engine = MyISAM 	DEFAULT CHARSET = latin1	COMMENT = 'Tabela com os álbuns';


# tblFotosAlbum
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblFotosAlbum (
CodFotoAlbum		INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
CodAlbum 			INT(8)			NOT NULL								COMMENT 'Código da categoria do álbum',
CodFoto 			INT(8)			NOT NULL								COMMENT 'Código da categoria do álbum',
CodUsuarioCriado	INT(8)			NOT NULL								COMMENT 'Código do usuário criador',
DataInserido		TIMESTAMP		NOT NULL	DEFAULT CURRENT_TIMESTAMP	COMMENT 'Data da inserção no sistema'
) Engine = MyISAM 	DEFAULT CHARSET = latin1	COMMENT = 'Tabela com as fotos dos álbuns';

# tblEscalasFerreo
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblEscalasFerreo (
CodEscalaFerreo		INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
NomeEscalaFerreo 	VARCHAR(255)	NOT NULL								COMMENT 'Nome da escala (ex: HO)',
PropocaoEscala 		INT(10) 		NOT NULL 	DEFAULT '1'					COMMENT 'Proporção da escala 1:n (ex: 87)',
DetalhesEscala 		BLOB													COMMENT 'Detalhes da escala',
CodUsuarioCriado	INT(8)			NOT NULL								COMMENT 'Código do usuário criador',
DataInserido		TIMESTAMP		NOT NULL	DEFAULT CURRENT_TIMESTAMP	COMMENT 'Data da inserção no sistema',
CodUsuarioMod		INT(8)			NULL									COMMENT 'Cód. do último usuário que modificou',
DataModificacao		TIMESTAMP		NULL									COMMENT 'Data da última modificação',
MotivoModificacao	VARCHAR(255)	NULL									COMMENT 'Motivo da última modificação',
NivelParaModificar	INT(2) 			NOT NULL	DEFAULT '99' 				COMMENT 'Nível mínimo de usuário p/ modificar'
) Engine = MyISAM 	DEFAULT CHARSET = latin1	COMMENT = 'Tabela com as escalas do ferromodelismo';


# tblFotos
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblFotos (
CodFoto				INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
CodCategoria 		INT(8)			NOT NULL								COMMENT 'Código da categoria da foto',
TituloFoto			VARCHAR(255)	NOT NULL								COMMENT 'Título da foto',
KeywordsFoto		VARCHAR(255)	NOT NULL								COMMENT 'Palavras chave da foto',
FotoPropria			BOOLEAN			NOT NULL	DEFAULT FALSE				COMMENT 'Se é autoria própria',
AutorFoto			VARCHAR(255)	NULL									COMMENT 'Nome do autor (se for terceiro)',
SabeDataFoto		BOOLEAN			NOT NULL	DEFAULT FALSE				COMMENT 'Se a data da foto é conhecida',
DataFoto			TIMESTAMP 		NOT NULL	DEFAULT 0					COMMENT 'Data da foto',
EmEscala			BOOLEAN			NOT NULL	DEFAULT FALSE				COMMENT 'Se é foto de modelo em escala',
CodEscalaFerreo		INT(8)			NOT NULL	DEFAULT '0'					COMMENT 'Código da escala do modelo (0=1:1)',
DetalhesFoto		BLOB			NULL									COMMENT 'Detalhes da foto',
CaminhoFoto			VARCHAR(255)	NOT NULL								COMMENT 'Caminho da foto',
CaminhoThumb		VARCHAR(255)	NULL									COMMENT 'Caminho da miniatura',
VisualizacoesFoto	INT(8)			NOT NULL 	DEFAULT 0					COMMENT 'Visualizações da foto',
CodUsuarioCriado	INT(8)			NOT NULL								COMMENT 'Código do usuário criador',
DataInserido		TIMESTAMP		NOT NULL	DEFAULT CURRENT_TIMESTAMP	COMMENT 'Data da inserção no sistema',
CodUsuarioMod		INT(8)			NULL									COMMENT 'Cód. do último usuário que modificou',
DataModificacao		TIMESTAMP		NULL									COMMENT 'Data da última modificação',
MotivoModificacao	VARCHAR(255)	NULL									COMMENT 'Motivo da última modificação',
NivelParaModificar	INT(2) 			NOT NULL	DEFAULT '99' 				COMMENT 'Nível mínimo de usuário p/ modificar'
) Engine = MyISAM 	DEFAULT CHARSET = latin1	COMMENT = 'Tabela com as fotos';


# tblVideos
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblVideos (
CodVideo			INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
CodCategoria 		INT(8)			NOT NULL								COMMENT 'Código da categoria do vídeo',
TituloVideo			VARCHAR(255)	NOT NULL								COMMENT 'Título do vídeo',
KeywordsVideo		VARCHAR(255)	NOT NULL								COMMENT 'Palavras chave do vídeo',
VideoProprio		BOOLEAN			NOT NULL	DEFAULT FALSE				COMMENT 'Se é autoria própria',
AutorVideo			VARCHAR(255)	NULL									COMMENT 'Nome do autor (se for terceiro)',
SabeDataVideo		BOOLEAN			NOT NULL	DEFAULT FALSE				COMMENT 'Se a data da foto é conhecida',
DataVideo			TIMESTAMP		NOT NULL	DEFAULT 0					COMMENT 'Data da filmagem',
DetalhesVideo		BLOB			NULL									COMMENT 'Detalhes do vídeo',
CaminhoVideo		VARCHAR(255)	NOT NULL								COMMENT 'Caminho do video',
CaminhoThumb		VARCHAR(255)	NULL									COMMENT 'Caminho da miniatura',
VisualizacoesVideo	INT(8)			NOT NULL 	DEFAULT 0					COMMENT 'Visualizações do vídeo',
CodUsuarioCriado	INT(8)			NOT NULL								COMMENT 'Código do usuário criador',
DataInserido		TIMESTAMP		NOT NULL	DEFAULT CURRENT_TIMESTAMP	COMMENT 'Data da inserção no sistema',
CodUsuarioMod		INT(8)			NULL									COMMENT 'Cód. do último usuário que modificou',
DataModificacao		TIMESTAMP		NULL									COMMENT 'Data da última modificação',
MotivoModificacao	VARCHAR(255)	NULL									COMMENT 'Motivo da última modificação',
NivelParaModificar	INT(2) 			NOT NULL	DEFAULT '99' 				COMMENT 'Nível mínimo de usuário p/ modificar'
) Engine = MyISAM 	DEFAULT CHARSET = latin1	COMMENT = 'Tabela com os vídeos';


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
CodUsuario 			INT(8)			NOT NULL	DEFAULT '0'					COMMENT 'Código do usuário autor'
) Engine = MyISAM 	DEFAULT CHARSET = latin1	COMMENT = 'Tabela com as publicações do feed';


# tblCurtidas
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblCurtidas (
CodCurtida 			INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
CodCategoria 		INT(8)			NOT NULL								COMMENT 'Código da categoria do item curtido',
CodItem 			INT(8)			NOT NULL								COMMENT 'Código do item curtido',
DataCurtida			TIMESTAMP		NOT NULL	DEFAULT CURRENT_TIMESTAMP	COMMENT 'Data da curtida',
CodUsuario 			INT(8)			NOT NULL								COMMENT 'Código do usuário que curtiu'
) Engine = MyISAM 	DEFAULT CHARSET = latin1	COMMENT = 'Tabela com as curtidas';


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
CodUsuario 			INT(8)			NOT NULL								COMMENT 'Código do usuário que comentou',
VeioDeEdicao		BOOLEAN			NOT NULL	DEFAULT FALSE				COMMENT 'Se o comentário é uma edição de outro',
CodComentEditado	INT(8)			NOT NULL	DEFAULT '0'					COMMENT 'Código do comentário editado'
) Engine = MyISAM 	DEFAULT CHARSET = latin1	COMMENT = 'Tabela com os comentários';


# tblUsuarios
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblUsuarios (
CodUsuario 			INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
NomeUsuario			VARCHAR(255)	NOT NULL								COMMENT 'Nome completo do usuário',
SenhaUsuario		VARCHAR(255)	NOT NULL								COMMENT 'Senha do usuário',
EmailUsuario		VARCHAR(255)	NOT NULL								COMMENT 'E-mail do usuário',
EmailConfirmado		BOOLEAN			NOT NULL	DEFAULT FALSE				COMMENT 'Se o e-mail já foi verificado',
ExibeEmail			BOOLEAN			NOT NULL	DEFAULT FALSE				COMMENT 'Se é para exibir o e-mail',
DataNascimento		TIMESTAMP 		NOT NULL	DEFAULT 0					COMMENT 'Data de nascimento',
ExibeDataNasc 		BOOLEAN			NOT NULL	DEFAULT FALSE				COMMENT 'Se é para exibir a data de nascimento',
CelularUsuario		VARCHAR(255)	NULL									COMMENT 'Celular do usuário',
ExibeCelular		BOOLEAN			NOT NULL	DEFAULT FALSE				COMMENT 'Se é para exibir o celular',
TelefoneUsuario		VARCHAR(255)	NULL									COMMENT 'Telefone do usuário',
ExibeTelefone		BOOLEAN			NOT NULL	DEFAULT FALSE				COMMENT 'Se é para exibir o telefone',
CodLocalPais		INT(8) 			NOT NULL 								COMMENT 'Código do país que mora o usuário',
CodLocalEstado		INT(8) 			NOT NULL 								COMMENT 'Código do estado que mora o usuário',
CodLocalCidade		INT(8)			NOT NULL 								COMMENT 'Código da cidade que mora o usuário',
BairroUsuario		VARCHAR(255)	NULL									COMMENT 'Bairro em que mora o usuário',
EnderecoUsuario		VARCHAR(255)	NULL									COMMENT 'Endereço em que mora o usuário',
CEPUsuario 	 		INT(8) 			NULL 									COMMENT 'CEP do usuário',
LaitudeUsuario 		DECIMAL(10, 8)	NULL									COMMENT 'Latitude em que mora o usuário',
LongitudeUsuario	DECIMAL(11, 8)	NULL									COMMENT 'Longitude em que mora o usuário',
ExibeLocal			BOOLEAN			NOT NULL	DEFAULT FALSE				COMMENT 'Se é para exibir o local',
FacebookUsuario		VARCHAR(255)	NULL									COMMENT 'Facebook do usário',
ExibeFacebook		BOOLEAN			NOT NULL	DEFAULT FALSE				COMMENT 'Se é para exibir o facebook',
SkypeUsuario		VARCHAR(255)	NULL									COMMENT 'Skype do usuário',
ExibeSkype			BOOLEAN			NOT NULL	DEFAULT FALSE				COMMENT 'Se é para exibir o skype',
NivelUsuario		INT(2)			NOT NULL	DEFAULT '0'					COMMENT 'Nível do usuáro (0-99)',
CodAvatar			INT(8)			NOT NULL	DEFAULT '0'					COMMENT 'Código do avatar do usuário',
DataInserido 		TIMESTAMP 		NOT NULL 	DEFAULT CURRENT_TIMESTAMP	COMMENT 'Data que o usuário se registrou',
EsqueciSenha		BOOLEAN			NOT NULL	DEFAULT FALSE				COMMENT 'Se esqueceu a senha',
MD5AlteraSenha		VARCHAR(255)	NULL									COMMENT 'MD5 de checagem pare atlerar senha',
DataUltimaSenha		TIMESTAMP  		NOT NULL 								COMMENT 'Data da última alteração de senha',
FezTour 			BOOLEAN			NOT NULL	DEFAULT FALSE				COMMENT 'Se é já fez o tour no site'
) Engine = MyISAM 	DEFAULT CHARSET = latin1	COMMENT = 'Tabela com os usuários';


# tblNiveisUsuario
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblNiveisUsuario (
CodNivelUsuario		INT(8)			NOT NULL	PRIMARY KEY 			 	COMMENT 'Código de indexação',
NomeNivelUsuario	VARCHAR(255)	NOT NULL								COMMENT 'Nome completo do usuário',
CaminhoPatente		VARCHAR(255) 	NOT NULL								COMMENT 'Caminho para a imagem da patente'
) Engine = MyISAM 	DEFAULT CHARSET = latin1	COMMENT = 'Tabela com os níveis dos usuários';


# tblFotosAvatar
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblFotosAvatar (
CodAvatar			INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
CaminhoAvatar		VARCHAR(255)	NOT NULL								COMMENT 'Caminho do avatar',
AvatarPublico		BOOLEAN			NOT NULL	DEFAULT FALSE				COMMENT 'Se o avatar é público (para escolha)',
CodUsuario 			INT(8)			NOT NULL								COMMENT 'Código do usuário que enviou o avatar',
DataEnvio 			TIMESTAMP		NOT NULL	DEFAULT CURRENT_TIMESTAMP	COMMENT 'Data/hora do envio do avatar'
) Engine = MyISAM 	DEFAULT CHARSET = latin1	COMMENT = 'Tabela com os avatares';


# tblLogs
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblLogs (
CodLog				INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
CodUsuario 			INT(8)			NOT NULL	DEFAULT '0' 				COMMENT 'Código do usuário que gerou o log',
SessaoUsuario		VARCHAR(255)	NULL									COMMENT 'Sessão de login do usuário',
IP 					VARCHAR(20)		NOT NULL								COMMENT 'IP do usuário',
Pagina				VARCHAR(255)	NOT NULL								COMMENT 'Página que gerou o log',
Erro				BOOLEAN			NOT NULL	DEFAULT FALSE				COMMENT 'Se é um erro ou só um registro',
HoraErro			TIMESTAMP 		NOT NULL 	DEFAULT CURRENT_TIMESTAMP 	COMMENT 'Data/hora do erro',
CodErro 			INT(8) 			NULL 									COMMENT 'Código do erro',
ArquivoErro			VARCHAR(255) 	NULL 									COMMENT 'Página do erro',
LinhaErro			INT(8) 			NULL 									COMMENT 'Linha do erro',
TraceErro			BLOB			NULL									COMMENT 'Trace do erro',
Request				VARCHAR(255)	NULL									COMMENT 'Request do erro',
Referer				VARCHAR(255)	NULL									COMMENT 'Referer do erro',
Agent				VARCHAR(255)	NULL									COMMENT 'Agent do erro',
Host				VARCHAR(255)	NULL									COMMENT 'Host do erro',
Port				INT(8)			NULL									COMMENT 'Port do erro',
Mensagem 			VARCHAR(255)	NOT NULL								COMMENT 'Mensagem do log'
) Engine = MyISAM 	DEFAULT CHARSET = latin1	COMMENT = 'Tabela com os logs';


# tblPerguntas
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblPerguntas (
CodPergunta			INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
CodCategoria 		INT(8)			NOT NULL								COMMENT 'Código do da categoria da pergunta',
TituloPergunta		VARCHAR(255)	NOT NULL								COMMENT 'Título da pergunta',
DescricaoPergunta	BLOB			NULL									COMMENT 'Detalhes da XXXX',
PerguntaEncerrada	BOOLEAN			NOT NULL	DEFAULT FALSE				COMMENT 'Se a perguna já foi encerrada',
CodRespostaCerta	INT(8)			NULL									COMMENT 'Código da resposta escolhida',
CodUsuarioCriado	INT(8)			NOT NULL								COMMENT 'Código do usuário criador',
DataInserido		TIMESTAMP		NOT NULL	DEFAULT CURRENT_TIMESTAMP	COMMENT 'Data da inserção no sistema',
CodUsuarioMod		INT(8)			NULL									COMMENT 'Cód. do último usuário que modificou',
DataModificacao		TIMESTAMP		NULL									COMMENT 'Data da última modificação',
MotivoModificacao	VARCHAR(255)	NULL									COMMENT 'Motivo da última modificação',
NivelParaModificar	INT(2) 			NOT NULL	DEFAULT '99' 				COMMENT 'Nível mínimo de usuário p/ modificar'
) Engine = MyISAM 	DEFAULT CHARSET = latin1	COMMENT = 'Tabela com as perguntas';


# tblRespostas
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblRespostas(
CodResposta			INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
CodPergunta			INT(8)			NOT NULL								COMMENT 'Aaaaaaa',
TextoResposta		BLOB			NULL									COMMENT 'Detalhes da XXXX',
CodUsuarioCriado	INT(8)			NOT NULL								COMMENT 'Código do usuário criador',
DataInserido		TIMESTAMP		NOT NULL	DEFAULT CURRENT_TIMESTAMP	COMMENT 'Data da inserção no sistema',
CodUsuarioMod		INT(8)			NULL									COMMENT 'Cód. do último usuário que modificou',
DataModificacao		TIMESTAMP		NULL									COMMENT 'Data da última modificação',
MotivoModificacao	VARCHAR(255)	NULL									COMMENT 'Motivo da última modificação',
NivelParaModificar	INT(2) 			NOT NULL	DEFAULT '99' 				COMMENT 'Nível mínimo de usuário p/ modificar'
) Engine = MyISAM 	DEFAULT CHARSET = latin1	COMMENT = 'Tabela com as respostas das perguntas';


# tblPrefixos
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblPrefixos (
CodPrefixo			INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
SiglaPrefixo		VARCHAR(5)		NOT NULL								COMMENT 'Sigla do prefixo (ex: Y04)',
CodFerrovia 		INT(8)			NOT NULL	DEFAULT '0'					COMMENT 'Código da ferrovia que pertence',
DetalhesPrefixo		BLOB			NULL									COMMENT 'Detalhes do prefixo',
CodUsuarioCriado	INT(8)			NOT NULL								COMMENT 'Código do usuário criador',
DataInserido		TIMESTAMP		NOT NULL	DEFAULT CURRENT_TIMESTAMP	COMMENT 'Data da inserção no sistema',
CodUsuarioMod		INT(8)			NULL									COMMENT 'Cód. do último usuário que modificou',
DataModificacao		TIMESTAMP		NULL									COMMENT 'Data da última modificação',
MotivoModificacao	VARCHAR(255)	NULL									COMMENT 'Motivo da última modificação',
NivelParaModificar	INT(2) 			NOT NULL	DEFAULT '99' 				COMMENT 'Nível mínimo de usuário p/ modificar'
) Engine = MyISAM 	DEFAULT CHARSET = latin1	COMMENT = 'Tabela com os prefixos';


# tblMedalhas
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblMedalhas (
CodMedalha			INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
NomeMedalha			VARCHAR(255)	NOT NULL								COMMENT 'Sigla do prefixo (ex: Y04)',
PesoMedalha 		INT(1)			NOT NULL	DEFAULT '0'					COMMENT 'Peso da medalha (1~3)',
ImagemMedalha		VARCHAR(255)	NOT NULL								COMMENT 'Caminho da imagem da medalha',
DescricaoMedalha	BLOB			NULL									COMMENT 'Descrição da medalha',
CodUsuarioCriado	INT(8)			NOT NULL								COMMENT 'Código do usuário criador',
DataInserido		TIMESTAMP		NOT NULL	DEFAULT CURRENT_TIMESTAMP	COMMENT 'Data da inserção no sistema',
CodUsuarioMod		INT(8)			NULL									COMMENT 'Cód. do último usuário que modificou',
DataModificacao		TIMESTAMP		NULL									COMMENT 'Data da última modificação',
MotivoModificacao	VARCHAR(255)	NULL									COMMENT 'Motivo da última modificação',
NivelParaModificar	INT(2) 			NOT NULL	DEFAULT '99' 				COMMENT 'Nível mínimo de usuário p/ modificar'
) Engine = MyISAM 	DEFAULT CHARSET = latin1	COMMENT = 'Tabela com as medalhas';


# tblMedalhasUsuario
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblMedalhasUsuario (
CodMedalhaUsuario	INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
CodMedalha 			INT(8)			NOT NULL								COMMENT 'Código da medalha ganha',
CodUsuario 			INT(8)			NOT NULL								COMMENT 'Código do usuário que ganhou',
RecebidoEm 			TIMESTAMP 		NOT NULL	DEFAULT CURRENT_TIMESTAMP	COMMENT 'Data da inserção no sistema'
) Engine = MyISAM 	DEFAULT CHARSET = latin1	COMMENT = 'Tabela com as medalhas dos usuários';


# tblFavoritos
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblFavoritos (
CodFavorito			INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
CodCategoria 		INT(8)			NOT NULL								COMMENT 'Código da cat. do item favoritado',
CodItem 			INT(8)			NOT NULL								COMMENT 'Código do item favoritado',
CodUsuario 			INT(8)			NOT NULL								COMMENT 'Código do usuário que favoritou',
DataFavoritado		TIMESTAMP 		NOT NULL	DEFAULT CURRENT_TIMESTAMP 	COMMENT 'Data/hora que favoritou'
) Engine = MyISAM 	DEFAULT CHARSET = latin1	COMMENT = 'Tabela com os favoritos';


# tblEventos
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblEventos (
CodEvento 			INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
CodCategoria 		INT(8)			NOT NULL								COMMENT 'Código do categoria do evento',
NomeEvento 			VARCHAR(255) 	NOT NULL								COMMENT 'Nome do evento',
DetalhesEvento 		BLOB			NULL									COMMENT 'Detalhes do evento',
CodLocalPais		INT(8) 			NOT NULL 								COMMENT 'Código do país do evento',
CodLocalEstado		INT(8) 			NOT NULL 								COMMENT 'Código do estado do evento',
CodLocalCidade		INT(8)			NOT NULL 								COMMENT 'Código da cidade do evento',
BairroEvento		VARCHAR(255)	NULL									COMMENT 'Bairro do evento',
EnderecoEvento		VARCHAR(255)	NULL									COMMENT 'Endereço do evento',
CEPEvento 	 		INT(8) 			NULL 									COMMENT 'CEP do evento',
LaitudeEvento 		DECIMAL(10, 8)	NULL									COMMENT 'Latitude do evento',
LongitudeEvento 	DECIMAL(11, 8)	NULL									COMMENT 'Longitude do evento',
TipoVisibilidade 	INT(1)			NOT NULL	DEFAULT '0'					COMMENT '0=Público, 1=Privado, 2=Secreto',
LinkEvento 			VARCHAR(255) 	NULL									COMMENT 'Link para página do evento',
DataInicio 			TIMESTAMP 		NOT NULL	DEFAULT 0					COMMENT 'Data do início do evento',
DataFinal			TIMESTAMP 		NOT NULL	DEFAULT 0					COMMENT 'Data do final do evento',
CodUsuarioCriado	INT(8)			NOT NULL								COMMENT 'Código do usuário criador',
DataInserido		TIMESTAMP		NOT NULL	DEFAULT CURRENT_TIMESTAMP	COMMENT 'Data da inserção no sistema',
CodUsuarioMod		INT(8)			NULL									COMMENT 'Cód. do último usuário que modificou',
DataModificacao		TIMESTAMP		NULL									COMMENT 'Data da última modificação',
MotivoModificacao	VARCHAR(255)	NULL									COMMENT 'Motivo da última modificação',
NivelParaModificar	INT(2) 			NOT NULL	DEFAULT '99' 				COMMENT 'Nível mínimo de usuário p/ modificar'
) Engine = MyISAM 	DEFAULT CHARSET = latin1	COMMENT = 'Tabela com os eventos';


# tblConvidadosEvento
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblConvidadosEvento (
CodConvidado		INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
CodEvento 			INT(8)			NOT NULL								COMMENT 'Código do evento do convite',
CodUsuario 			INT(8)			NOT NULL								COMMENT 'Código do usuário convidado',
EstadoConvite		INT(1) 			NOT NULL	DEFAULT '0'					COMMENT '0=Em aberto;1=Aceito;2=Talvez;3=Nao',
DataCriado			TIMESTAMP		NOT NULL	DEFAULT CURRENT_TIMESTAMP	COMMENT 'Data da inserção no sistema',
DataAceito 			TIMESTAMP 		NOT NULL 	DEFAULT 0 					COMMENT 'Data que o convite foi aceito',
CodUsuarioCriado 	INT(8)			NOT NULL								COMMENT 'Código do usuário criador'
) Engine = MyISAM 	DEFAULT CHARSET = latin1	COMMENT = 'Tabela com os convites dos eventos';


# tblVisitas
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblVisitas (
CodVisita			INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
IP		 			INT(8)			NOT NULL								COMMENT 'IP do acesso',
Sessao  			INT(8)			NOT NULL								COMMENT 'Sessão do usuário',
DataInicio			TIMESTAMP 		NOT NULL	DEFAULT CURRENT_TIMESTAMP 	COMMENT 'Data de início da sessão',
DataFim				TIMESTAMP 		NOT NULL 	DEFAULT 0					COMMENT 'Data de final da sessão',
CodUsuario 			INT(8)			NOT NULL	DEFAULT '0'					COMMENT 'Código do usuário do acesso',
Online				BOOLEAN			NOT NULL	DEFAULT TRUE				COMMENT 'Se ainda está online'
) Engine = MyISAM 	DEFAULT CHARSET = latin1	COMMENT = 'Tabela com os diferentes visitantes do site';


# tblAcessos
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblAcessos (
CodAcesso			INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
IP		 			INT(8)			NOT NULL								COMMENT 'IP do acesso',
Sessao  			INT(8)			NOT NULL								COMMENT 'Sessão do usuário',
DataAcesso			TIMESTAMP 		NOT NULL	DEFAULT CURRENT_TIMESTAMP 	COMMENT 'Data do acesso',
Pagina 				VARCHAR(255)	NOT NULL								COMMENT 'Página acessada',
CodUsuario 			INT(8)			NOT NULL	DEFAULT '0'					COMMENT 'Código do usuário que acessou'
) Engine = MyISAM 	DEFAULT CHARSET = latin1	COMMENT = 'Tabela com os acessos às páginas do site';


# tblDenuncia
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE tblDenuncias (
CodDenuncia			INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
CodCategoria 		INT(8)			NOT NULL								COMMENT 'Código da categoria da denuncia',
CodCategoriaItem 	INT(8)			NOT NULL								COMMENT 'Código da categoria do item',
CodItem 			INT(8)			NOT NULL								COMMENT 'Código do item',
CodUsuario 			INT(8)			NOT NULL								COMMENT 'Código do usuário denunciando',
DetalhesDenuncia	BLOB 			NULL									COMMENT 'Detalhes da denúncia',
EstadoDenuncia		INT(1) 			NOT NULL	DEFAULT '0'					COMMENT '0=Em aberto;1=Aceito;2=Recusado',
RespostaDenuncia	BLOB			NULL									COMMENT 'Resposta da denúncia',
DataCriado			TIMESTAMP		NOT NULL	DEFAULT CURRENT_TIMESTAMP	COMMENT 'Data da inserção no sistema',
DataResposta		TIMESTAMP 		NOT NULL 	DEFAULT 0 					COMMENT 'Data que o convite foi respondido'
) Engine = MyISAM 	DEFAULT CHARSET = latin1	COMMENT = 'Tabela com as denúncias';


# tblMensagem
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE IF NOT EXISTS tblMensagens (
CodMensagem			INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
CodRemetente 		INT(8)			NOT NULL								COMMENT 'Código do usuário remetente',
CodDestinatario		INT(8)			NOT NULL								COMMENT 'Código do usuário destinatário',
DataEnvio 			TIMESTAMP 		NOT NULL	DEFAULT CURRENT_TIMESTAMP	COMMENT 'Data que a mensagem foi enviada',
Lido 				BOOLEAN			NOT NULL	DEFAULT TRUE				COMMENT 'Se já foi lida',
DataLido			TIMESTAMP 		NOT NULL 	DEFAULT 0 					COMMENT 'Data que a mensagem foi lida',
TextoMensagem		BLOB			NULL									COMMENT 'Texto da Mensagem',
Excluido 			BOOLEAN			NOT NULL	DEFAULT TRUE				COMMENT 'Se foi excluída'
) Engine = MyISAM 	DEFAULT CHARSET = latin1	COMMENT = 'Tabela com as mensagens';

# tblLocalPais
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE IF NOT EXISTS tblLocalPais(
CodLocalPais 		INT(8)			NOT NULL 	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
NomeLocalPais 		VARCHAR(255) 	NOT NULL 								COMMENT 'Nome do país',
SiglaLocalPais		VARCHAR(3) 		NOT NULL								COMMENT 'Sigla do país (ex: BRA)'
) Engine = MyISAM 	DEFAULT CHARSET = latin1	COMMENT = 'Tabela com os países';

# tblLocalEstado
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE IF NOT EXISTS tblLocalEstado(
CodLocalEstado		INT(8) 			NOT NULL 	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
NomeLocalEstado		VARCHAR(255)	NOT NULL 								COMMENT 'Nome do estado (ex: São Paulo)',
UFLocalEstado 		VARCHAR(2) 		NOT NULL 								COMMENT 'UF do estado (ex: SP)',
CodLocalPais 		INT(8) 			NOT NULL 								COMMENT 'Código do país'
) ENGINE = MyISAM 	DEFAULT CHARSET = latin1	COMMENT = 'Tabela com os estados';

# tblLocalCidade
#############################################################################################################################
# NOME DO CAMPO 	TIPO(TAMANHO) 	(NOT) NULL	DEFAULT / PRIMARY / UNIQUE	COMENTÁRIO
#############################################################################################################################
CREATE TABLE IF NOT EXISTS tblLocalCidade(
CodLocalCidade		INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
NomeLocalCidade		VARCHAR(255) 	NOT NULL 								COMMENT 'Nome da cidade (ex: Palmital)',
CodLocalEstado		INT(8) 			NOT NULL 								COMMENT 'Código do estado'
) ENGINE = MyISAM	DEFAULT CHARSET = latin1	COMMENT = 'Tabela com as cidades';	