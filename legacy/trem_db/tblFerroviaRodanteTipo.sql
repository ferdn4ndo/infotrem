# tblFerroviaModeloTipo
#
# DESC:			Tabela de armazenamento dos tipos de material rodante das ferrovias
# TODO:			-
# NOTES:		-
#
DROP TABLE IF EXISTS tblFerroviaModeloTipo;
CREATE TABLE tblFerroviaModeloTipo (
	CodFerroviaModeloTipo		INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
	SiglaModeloTipo				VARCHAR(5)		NULL									COMMENT 'Sigla do tipo de material rodante',
	NomeModeloTipo				VARCHAR(255)	NULL									COMMENT 'Nome do tipo de material rodante',
	Ativo 						BOOLEAN			NOT NULL	DEFAULT TRUE 				COMMENT 'Se o registro está ativo'
) Engine = MyISAM 	DEFAULT CHARSET = utf8mb4	COMMENT = 'Tabela de armazenamento dos tipos de trem-unidade das ferrovias';

INSERT INTO tblFerroviaModeloTipo (CodFerroviaModeloTipo, SiglaModeloTipo, NomeModeloTipo, Ativo) VALUES
	(1, 'L', 'Locomotiva', 1),
	(2, 'V', 'Vagão', 1),
	(3, 'C', 'Carro', 1),
	(4, 'A', 'Auto de linha', 1),
	(5, 'T', 'Automotriz/Trem-unidade', 1);