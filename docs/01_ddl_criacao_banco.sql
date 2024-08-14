CREATE TABLE Usuarios (
    usuario_id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    login VARCHAR(100) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL
);

CREATE TABLE Projetos (
    projeto_id INT PRIMARY KEY AUTO_INCREMENT,
    nome_projeto VARCHAR(255) NOT NULL,
    descricao TEXT,
    data_inicio DATE NOT NULL,
    data_termino DATE,
    usuario_responsavel_id INT,
    FOREIGN KEY (usuario_responsavel_id) REFERENCES Usuarios(usuario_id)
);

CREATE TABLE Sprints (
    sprint_id INT PRIMARY KEY AUTO_INCREMENT,
    projeto_id INT,
    nome_sprint VARCHAR(255) NOT NULL,
    descricao TEXT,
    data_inicio DATE NOT NULL,
    data_termino DATE,
    status VARCHAR(50),
    responsavel_id INT,
    FOREIGN KEY (projeto_id) REFERENCES Projetos(projeto_id),
    FOREIGN KEY (responsavel_id) REFERENCES Usuarios(usuario_id)
);

