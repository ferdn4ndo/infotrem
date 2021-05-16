# tblFerroviaVagaoManga
#
# DESC:			Tabela de armazenamento das mangas dos vagões das ferrovias
# TODO:			-
# NOTES:		-
#
DROP TABLE IF EXISTS tblFerroviaVagaoManga;
CREATE TABLE tblFerroviaVagaoManga (
	CodFerroviaVagaoManga			INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
	LetraVagaoMangaMetrica			VARCHAR(1)		NULL									COMMENT 'Letra da manga na bitola métrica',
	LetraVagaoMangaLarga			VARCHAR(1)		NULL									COMMENT 'Letra da manga na bitola larga',
	PesoMaximoTon					INT(5)			NULL									COMMENT 'Peso máximo em centenas de quilos da bitola',
	Ativo 						BOOLEAN			NOT NULL	DEFAULT TRUE 				COMMENT 'Se o registro está ativo'
) Engine = MyISAM 	DEFAULT CHARSET = utf8mb4	COMMENT = 'Tabela de armazenamento das mangas dos vagões das ferrovias';

INSERT INTO tblFerroviaVagaoManga (CodFerroviaVagaoManga, LetraVagaoMangaMetrica, LetraVagaoMangaLarga, PesoMaximoTon, Ativo) VALUES
	(1, 'A', NULL, 300, 1),
	(2, 'B', 'P', 470, 1),
	(3, 'C', 'Q', 645, 1),
	(4, 'D', 'R', 800, 1),
	(5, 'E', 'S', 1000, 1),
	(6, 'F', 'T', 1195, 1),
	(7, 'G', 'U', 1430, 1),
	(8, 'H', NULL, 9999, 1);

