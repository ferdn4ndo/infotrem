# tblFerroviaTracaoClassificacao
#
# DESC:			Tabela de armazenamento da classificação dos rodeiros das locomotivas
# TODO:			-
# NOTES:		-
#
DROP TABLE IF EXISTS tblFerroviaTracaoClassificacao;
CREATE TABLE tblFerroviaTracaoClassificacao (
	CodTracaoClassificacao		INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
	NomeTracaoClassificacao		VARCHAR(255)	NOT NULL								COMMENT 'Nome da classificacao',
	Ativo 						BOOLEAN			NOT NULL	DEFAULT TRUE 				COMMENT 'Se o registro está ativo'
) Engine = MyISAM 	DEFAULT CHARSET = utf8mb4	COMMENT = 'Tabela de armazenamento da classificação dos rodeiros das locomotivas';

INSERT INTO tblFerroviaTracaoClassificacao (CodTracaoClassificacao, NomeTracaoClassificacao, Ativo) VALUES
	(1, 'B-B', 1),
	(2, 'C-C', 1),
	(3, 'A1A-A1A', 1),
	(4, '2-D+D-2', 1),
	(5, '2-C+C-2', 1),
	(6, '1-C+C-1', 1);