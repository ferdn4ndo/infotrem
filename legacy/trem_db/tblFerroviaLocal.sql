# tblFerroviaLocal
#
# DESC:			Tabela de armazenamento dos pátios/estações/locais do módulo de ferrovias
# TODO:			-
# NOTES:		-
#
DROP TABLE IF EXISTS tblFerroviaLocal;
CREATE TABLE tblFerroviaLocal (
	CodFerroviaLocal			INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
	CodFerroviaLocalTipo		INT(8)			NULL									COMMENT 'Código do tipo de local',
	SiglaSigoLocal				VARCHAR(3)		NULL									COMMENT 'Sigla do local no SIGO (ex: LUS)',
	CodLocalPais				INT(8) 			NULL 									COMMENT 'Código do país que pertence o local',
	CodLocalEstado				INT(8) 			NULL 									COMMENT 'Código do estado que pertence o local',
	CodLocalCidade				INT(8)			NULL 									COMMENT 'Código da cidade que pertence o local',
	LatitudeLocal 				DECIMAL(10, 8)	NOT NULL	DEFAULT 0					COMMENT 'Latitude do local',
	LongitudeLocal				DECIMAL(11, 8)	NOT NULL	DEFAULT 0					COMMENT 'Longitude do local',
	CodUsuInserido				INT(8)			NULL 									COMMENT 'Código do usuário que inseriu o registro',
	DataInserido				TIMESTAMP 		NOT NULL 	DEFAULT CURRENT_TIMESTAMP 	COMMENT 'Data de cadastro do registro',
	DataRemovido 				TIMESTAMP 		NULL 	 								COMMENT 'Data que o registro foi removido',
	CodUsuRemovido 				INT(8)			NULL 									COMMENT 'Código do usuário que removeu o registro',
	Ativo 						BOOLEAN			NOT NULL	DEFAULT TRUE 				COMMENT 'Se o registro está ativo'
) Engine = MyISAM 	DEFAULT CHARSET = utf8mb4	COMMENT = 'Tabela de armazenamento dos contatos das entidades cadastradas no sistema';
