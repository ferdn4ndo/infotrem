# tblFerroviaLocalTipo
#
# DESC:			Tabela de armazenamento dos tipos de locais do módulo de ferrovias
# TODO:			-
# NOTES:		-
#
DROP TABLE IF EXISTS tblFerroviaLocalTipo;
CREATE TABLE tblFerroviaLocalTipo (
	CodFerroviaLocalTipo		INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
	NomeLocalTipo				VARCHAR(255)	NOT NULL								COMMENT 'Nome do tipo de local',
	SiglaLocalTipo				VARCHAR(3)		NULL									COMMENT 'Sigla do tipo de local',
	Ativo 						BOOLEAN			NOT NULL	DEFAULT TRUE 				COMMENT 'Se o registro está ativo'
) Engine = MyISAM 	DEFAULT CHARSET = utf8mb4	COMMENT = 'Tabela de armazenamento dos tipos de locais do módulo de ferrovias';

INSERT INTO `tblFerroviaLocalTipo` (`CodFerroviaLocalTipo`, `NomeLocalTipo`, `SiglaLocalTipo`, `Ativo`) VALUES
	(1, 'Estação', 'E', 1),
	(2, 'Posto de Parada', 'P', 1),
	(3, 'Terminal', 'T', 1);