# tblFerroviaVagaoTipo
#
# DESC:			Tabela de armazenamento dos tipos dos vagões das ferrovias
# TODO:			-
# NOTES:		-
#
DROP TABLE IF EXISTS tblFerroviaVagaoTipo;
CREATE TABLE tblFerroviaVagaoTipo (
	CodFerroviaVagaoTipo		INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
	LetraVagaoTipo				VARCHAR(1)		NULL									COMMENT 'Letra do tipo de vagão',
	NomeVagaoTipo				VARCHAR(255)	NULL									COMMENT 'Nome do tipo de vagão',
	Ativo 						BOOLEAN			NOT NULL	DEFAULT TRUE 				COMMENT 'Se o registro está ativo'
) Engine = MyISAM 	DEFAULT CHARSET = utf8mb4	COMMENT = 'Tabela de armazenamento dos tipos dos vagões das ferrovias';

INSERT INTO tblFerroviaVagaoTipo (CodFerroviaVagaoTipo, LetraVagaoTipo, NomeVagaoTipo, Ativo) VALUES
	(1, 'A', 'Gaiola', 1),
	(2, 'C', 'Caboose', 1),
	(3, 'F', 'Fechado', 1),
	(4, 'G', 'Gôndola', 1),
	(5, 'H', 'Hopper', 1),
	(6, 'I', 'Isotérmico', 1),
	(7, 'P', 'Plataforma', 1),
	(8, 'Q', 'Qualquer (outros)', 1),
	(9, 'T', 'Tanque', 1);
