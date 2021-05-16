# tblFerroviaRodanteFaixaNumerica
#
# DESC:			Tabela de armazenamento das faixas numéricas das ferrovias
# TODO:			-
# NOTES:		-
#
DROP TABLE IF EXISTS tblFerroviaRodanteFaixaNumerica;
CREATE TABLE tblFerroviaRodanteFaixaNumerica (
	CodFerroviaRodanteFaixaNum	INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
	CodFerroviaRodanteTipo		INT(8)			NULL									COMMENT 'Código do tipo de material rodante',
	CodFerroviaTracao			INT(8)			NULL									COMMENT 'Código do tipo de tração (se locomotiva)',
	CodFerroviaBitola			INT(8)			NULL									COMMENT 'Código da bitola',
	CodFerroviaEmpresa			INT(8)			NULL									COMMENT 'Código da empresa que detém a faixa',
	CodFerroviaFabricante		INT(8)			NULL									COMMENT 'Código do fabricante',
	NumeroInicio				INT(6)			NOT NULL								COMMENT 'Número inicial da faixa',
	NumeroFinal					INT(6)			NOT NULL								COMMENT 'Número final da faixa',
	Ativo 						BOOLEAN			NOT NULL	DEFAULT TRUE 				COMMENT 'Se o registro está ativo'
) Engine = MyISAM 	DEFAULT CHARSET = utf8mb4	COMMENT = 'Tabela de armazenamento das faixas numéricas das ferrovias';

INSERT INTO tblFerroviaRodanteFaixaNumerica (CodFerroviaRodanteFaixaNum, CodFerroviaRodanteTipo, CodFerroviaTracao, CodFerroviaBitola, CodFerroviaEmpresa, CodFerroviaFabricante, NumeroInicio, NumeroFinal, Ativo) VALUES
	(1,  2, NULL, NULL, 10, NULL, 000000, 099999, 1),
	(2,  2, NULL, NULL,  6, NULL, 100000, 299999, 1),
	(3,  2, NULL, NULL,  1, NULL, 300000, 599999, 1),
	(4,  2, NULL, NULL,  2, NULL, 600000, 799999, 1),
	(5,  2, NULL, NULL,  7, NULL, 800000, 839999, 1),
	(6,  1,    1,    5,  2, NULL, 900001, 900100, 1),
	(7,  1,    1,    1,  2, NULL, 900101, 900400, 1),
	(8,  1,    1,    2,  2, NULL, 900401, 900500, 1),
	(10, 1,    2,    1,  2, NULL, 900501, 900750, 1),
	(11, 1,    2,    2,  2, NULL, 900751, 901000, 1),
	(12, 1,    2,    1,  2, NULL, 901001, 901500, 1),
	(13, 1,    2,    2,  2, NULL, 901501, 902000, 1),
	(14, 1,    2,    1,  2,    1, 902001, 903000, 1),
	(15, 1,    2,    2,  2,    1, 903001, 904000, 1),
	(16, 1,    2,    1,  2,    2, 904001, 905000, 1),
	(17, 1,    2,    2,  2,    2, 905001, 906000, 1),
	(18, 1,    2,    1,  2,    3, 906001, 907000, 1),
	(19, 1,    2,    2,  2,    3, 907001, 908000, 1),
	(20, 1,    3,    1,  2, NULL, 908001, 909000, 1),
	(21, 1,    3,    2,  2, NULL, 909001, 909999, 1),
	(22, 1, NULL, NULL,  6, NULL, 910000, 911999, 1),
	(23, 1, NULL, NULL,  1, NULL, 912000, 917999, 1),
	(24, 1, NULL, NULL,  7, NULL, 918000, 918099, 1),
	(25, 1, NULL, NULL, 10, NULL, 918100, 919999, 1),
	(26, 3, NULL, NULL,  2, NULL, 920000, 929999, 1),
	(27, 3, NULL, NULL,  6, NULL, 930000, 930999, 1),
	(28, 3, NULL, NULL,  7, NULL, 931000, 931999, 1),
	(29, 3, NULL, NULL,  1, NULL, 933000, 937999, 1),
	(30, 5, NULL,    2,  2, NULL, 946000, 946699, 1),
	(31, 5, NULL,    1,  2, NULL, 947000, 947699, 1),
	(32, 4, NULL, NULL,  2, NULL, 950000, 979999, 1);