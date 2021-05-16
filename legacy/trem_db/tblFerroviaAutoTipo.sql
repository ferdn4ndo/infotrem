# tblFerroviaAutoTipo
#
# DESC:			Tabela de armazenamento dos tipos de auto de linha das ferrovias
# TODO:			-
# NOTES:		-
#
DROP TABLE IF EXISTS tblFerroviaAutoTipo;
CREATE TABLE tblFerroviaAutoTipo (
	CodFerroviaAutoTipo			INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
	SiglaAutoTipo				VARCHAR(5)		NULL									COMMENT 'Sigla do tipo de auto de linha',
	NomeAutoTipo				VARCHAR(255)	NULL									COMMENT 'Nome do tipo de auto de linha',
	Ativo 						BOOLEAN			NOT NULL	DEFAULT TRUE 				COMMENT 'Se o registro está ativo'
) Engine = MyISAM 	DEFAULT CHARSET = utf8mb4	COMMENT = 'Tabela de armazenamento dos tipos de auto de linha das ferrovias';

INSERT INTO tblFerroviaAutoTipo (CodFerroviaAutoTipo, SiglaAutoTipo, NomeAutoTipo, Ativo) VALUES
	(1, 'AAP', 'Alinhadora Automática Plasser', 1),
	(2, 'ALI', 'Auto de Linha de inspeção', 1),
	(3, 'ALS', 'Auto de Linha de Serviço até 10 pass. + 2 reboques', 1),
	(4, 'ALU', 'Auto de Linha de Serviço utilitário', 1),
	(5, 'ATL', 'Auto de Linha', 1),
	(6, 'CCP', 'Carro controle padrão', 1),
	(7, 'CLS', 'Caminhão de Linha', 1),
	(8, 'CPP', 'Compactadora de Lastro Plasser', 1),
	(9, 'DLP', 'Desguarnecedora de Lastro Plasser', 1),
	(10, 'GBK', 'Guindaste Burro Krane', 1),
	(11, 'GOR', 'Guindaste Orton', 1),
	(12, 'GVP', 'Guindaste de Via Permanente', 1),
	(13, 'MNP', 'Socadora Mínima 2 Plasser', 1),
	(14, 'RLK', 'Reguladora de Lastro Kershaw', 1),
	(15, 'RLP', 'Reguladora de Lastro Plasser', 1),
	(16, 'RTM', 'Reperfiladora de Trilho Plasser', 1),
	(17, 'SAP', 'Socadora Niveladora Alinhadora Plasser', 1),
	(18, 'SAT', 'Socadora Niveladora Alinhadora Tamper', 1),
	(19, 'SCP', 'Socadora Niveladora de AMV Plasser', 1),
	(20, 'SNP', 'Socadora Niveladora Plasser', 1),
	(21, 'SOP', 'Soldadora de Trilho Plasser', 1),
	(22, 'STK', 'Guindaste Takraf', 1),
	(23, 'TBL', 'Trem de Barra Longa', 1),
	(24, 'TMS', 'Trole Motor', 1);
