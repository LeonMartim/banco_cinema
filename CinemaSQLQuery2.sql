CREATE DATABASE cinema;

-- Tabela ator
CREATE TABLE ator (
    cod_ator INT IDENTITY(1,1) NOT NULL  PRIMARY KEY,  -- chave primaria
    nome_artistico VARCHAR(100) NOT NULL,    -- nome pelo qual o ator e conhecido
    nome_real VARCHAR(100) NOT NULL,         -- nome de nascimento
    nacionalidade VARCHAR(50) NOT NULL,      -- ex: Brasil, EUA
    sexo CHAR(1) NOT NULL CHECK (sexo IN ('M','F','O')), -- restricao: so M, F ou O (outro)
    idade INT CHECK (idade >= 0),            -- idade nao pode ser negativa
    indicacao_oscar INT DEFAULT 0 CHECK (indicacao_oscar >= 0), -- padrao 0
    ganhou_oscar INT DEFAULT 0 CHECK (ganhou_oscar >= 0)        -- padrao 0
);

-- Tabela Filme
CREATE TABLE Filme (
    cod_filme INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
    nome_filme VARCHAR(100) NOT NULL,
    data_lancamento DATE NOT NULL,
    orcamento DECIMAL(15,2) NULL,
    tempo INT NULL
);

-- Tabela Personagem
CREATE TABLE Personagem (
    cod_personagem INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
    cod_filme INT,
    cod_ator INT,
    nome_personagem VARCHAR(100),
    cache DECIMAL(15,2),
    FOREIGN KEY (cod_filme) REFERENCES Filme(cod_filme),
    FOREIGN KEY (cod_ator) REFERENCES Ator(cod_ator)
);

-- Tabela Filme (chave cod_ator automatico)
INSERT INTO Ator (nome_artistico, nome_real, nacionalidade, sexo, idade, indicacao_oscar, ganhou_oscar)
VALUES 
('Tom H.', 'Tom Hanks', 'Americana', 'M', 67, 6, 0),
('Matt D.', 'Matt Damon', 'Americana', 'M', 54, 5, 1),
('Nicole K.', 'Nicole Kidman', 'Australiana', 'F', 56, 4, 1),
('Jim C.', 'Jim Carrey', 'Canadense', 'M', 63, 3, 0),
('George C.', 'George Clooney', 'Americana', 'M', 63, 7, 1),
('Maria C.', 'Maria da Costa', 'Brasileira', 'F', 38, 1, 0),
('Jorge L.', 'Jorge Leon', 'Brasileiro', 'M', 32, 4, 1);

-- Tabela Filme (chave cod_filme automatica)
INSERT INTO Filme (nome_filme, data_lancamento, orcamento, tempo)
VALUES
('Forrest Gump', '1994-07-06', 55000000.00, 142),
('Interestelar', '2014-11-07', 165000000.00, 169),
('O Discurso do Rei', '2010-12-25', 15000000.00, 118),
('Debi & Loide', '1994-12-16', 17000000.00, 107),
('Gravidade', '2013-10-04', 100000000.00, 91),
('Filme Futuro', '2026-01-01', 80000000.00, 110),
('Amor e Guerra', '1998-05-15', 45000000.00, 135),
('Espirito Livre', '2010-08-16', 35000000.00, 110);


select * from Ator;
select * from Filme;
select * from Personagem;

-- Tabela personagens()
INSERT INTO Personagem (cod_filme, cod_ator, nome_personagem, cache)
VALUES
(1, 1, 'Forrest Gump', 1200000.00),
(2, 2, 'Dr. Mann', 800000.00),
(2, 1, 'Murph', 850000.00),
(3, 3, 'Rainha Elizabeth', 500000.00),
(4, 4, 'Lloyd', 650000.00),
(5, 5, 'Matt Kowalski', 950000.00),
(5, 3, 'Ryan Stone', 850000.00),
(6, 6, 'Joana Costa', 300000.00),
(7, 1, 'Soldado John', 400000.00),
(7, 2, 'Capit�o Miller', 350000.00),
(8, 7, 'Serafim', 250000.00);
