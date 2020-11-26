DROP Table Films_Roles;
DROP Table Actors_Roles;
DROP Table Films;
DROP Table Actors;

CREATE TABLE Films (
    FilmID int,
    FilmName varchar(255) NOT NULL UNIQUE,
    BoxOffice int DEFAULT 0,
    Year varchar(4) NOT NULL,
    PRIMARY KEY (FilmID)
);

CREATE TABLE Actors (
    ActorID int,
    ActorName varchar(255) NOT NULL UNIQUE,
    PRIMARY KEY (ActorID)
);

CREATE TABLE Films_Roles (
    RoleID int,
    FilmID int,
    RoleName varchar(255) NOT NULL UNIQUE,
    PRIMARY KEY(RoleID),
    FOREIGN KEY (FilmID) REFERENCES Films(FilmID)
);

CREATE TABLE Actors_Roles (
    ActorID int,
    RoleID int,
    FOREIGN KEY (ActorID) REFERENCES Actors(ActorID)
    FOREIGN KEY (RoleID) REFERENCES Films_Roles(FilmRoleIDID)
)