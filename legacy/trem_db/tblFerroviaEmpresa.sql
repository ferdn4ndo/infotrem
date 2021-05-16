# tblFerroviaEmpresa
#
# DESC:			Tabela de armazenamento das empresas administradoras de ferrovias
# TODO:			-
# NOTES:		-
#
DROP TABLE IF EXISTS tblFerroviaEmpresa;
CREATE TABLE tblFerroviaEmpresa (
	CodFerroviaEmpresa			INT(8)			NOT NULL	AUTO_INCREMENT PRIMARY KEY 	COMMENT 'Código de indexação',
	NomeFerroviaEmpresa			VARCHAR(255)	NOT NULL								COMMENT 'Nome da empresa',
	SiglaFerroviaEmpresa		VARCHAR(255)	NOT NULL								COMMENT 'Sigla da empresa',
	Ativo 						BOOLEAN			NOT NULL	DEFAULT TRUE 				COMMENT 'Se o registro está ativo'
) Engine = MyISAM 	DEFAULT CHARSET = utf8mb4	COMMENT = 'Tabela de armazenamento das empresas administradoras de ferrovias';
INSERT INTO `tblFerroviaEmpresa` (`CodFerroviaEmpresa`, `NomeFerroviaEmpresa`, `SiglaFerroviaEmpresa`, `Ativo`) VALUES
	(1, 'Ferrovia Paulista SA', 'Fepasa', 1),
	(2, 'Rede Ferroviária Federal SA', 'RFFSA', 1),
	(3, 'América Latina Logística', 'ALL', 1),
	(4, 'Ferrovia Paulista SA', 'Fepasa', 1),
	(5, 'Companhia Brasileira de Trens Urbanos', 'CBTU', 1),
	(6, 'Companhia Vale do Rio Doce (Vale)', 'CVRD', 1),
	(7, 'Empresa Nacional de Ferrocarriles – Bolívia', 'ENFE', 1),
	(8, 'Administracion de los Ferrocarriles del Estado – Uruguai', 'AFE', 1),
	(9, 'Ferrocarriles Argentinos - Argentina', 'FA', 1),
	(10, 'Particulares', 'PARTICULARES', 1);