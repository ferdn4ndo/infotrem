# tblFerroviaTremUnidadeTipo
#
# DESC:			Tabela de armazenamento dos tipos de trem-unidade das ferrovias
# TODO:			-
# NOTES:		-
#
DROP TABLE IF EXISTS tblFerroviaTremUnidadeTipo;
CREATE TABLE tblFerroviaTremUnidadeTipo (
	CodFerroviaTremUniTipo		INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
	SiglaTremUniTipo			VARCHAR(5)		NULL									COMMENT 'Sigla do tipo de trem-unidade',
	NomeTremUniTipo				VARCHAR(255)	NULL									COMMENT 'Nome do tipo de trem-unidade',
	Ativo 						BOOLEAN			NOT NULL	DEFAULT TRUE 				COMMENT 'Se o registro está ativo'
) Engine = MyISAM 	DEFAULT CHARSET = utf8mb4	COMMENT = 'Tabela de armazenamento dos tipos de trem-unidade das ferrovias';

INSERT INTO tblFerroviaTremUnidadeTipo (CodFerroviaTremUniTipo, SiglaTremUniTipo, NomeTremUniTipo, Ativo) VALUES
	(1, 'CE', 'Carro motor TUE - cabine', 1),
	(2, 'CH', 'Carro motor TUDH - cabine', 1),
	(3, 'IE', 'Carro reboque TUE - cabine', 1),
	(4, 'IH', 'Carro reboque TUDH - cabine', 1),
	(5, 'MD', 'Automotriz Diesel-Elétrica', 1),
	(6, 'ME', 'Automotriz Elétrica', 1),
	(7, 'MH', 'Automotriz Diesel-Hidráulica', 1),
	(8, 'NE', 'Carro reboque TUE', 1),
	(9, 'NH', 'Carro reboque TUDH', 1),
	(10, 'OE', 'Carro motor TUE', 1),
	(11, 'OH', 'Carro motor TUDH', 1);