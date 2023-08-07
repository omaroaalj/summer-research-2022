/*
SET FOREIGN_KEY_CHECKS=0;

DROP TABLE IF EXISTS Country;
DROP TABLE IF EXISTS Category;
DROP TABLE IF EXISTS CountryOnCategory;

CREATE TABLE Country(
	country_id INT NOT NULL AUTO_INCREMENT,
    country_name VARCHAR(100),
    PRIMARY KEY (country_id)
);

CREATE TABLE Category(
	category_id INT NOT NULL AUTO_INCREMENT,
    category_name VARCHAR(100),
    PRIMARY KEY (category_id)
);

CREATE TABLE CountryOnCategory(
	country_id INT NOT NULL,
    category_id INT NOT NULL,
    minutes INT,
    PRIMARY KEY (country_id, category_id)
);

ALTER TABLE CountryOnCategory
ADD FOREIGN KEY (`country_id`)
REFERENCES Country(`country_id`);

ALTER TABLE CountryOnCategory
ADD FOREIGN KEY (`category_id`)
REFERENCES Category(`category_id`);

SET FOREIGN_KEY_CHECKS=1;

SELECT * FROM Country;
SELECT * FROM Category;
SELECT * FROM CountryOnCategory;

SELECT Country.country_name, Category.category_name, CountryOnCategory.minutes FROM CountryOnCategory
INNER JOIN Country ON CountryOnCategory.country_id = Country.country_id
INNER JOIN Category ON CountryOnCategory.category_id = Category.category_id
;

*/
/*
-- GAME DATABASE
SET FOREIGN_KEY_CHECKS=0;

DROP TABLE IF EXISTS Publisher;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Developer;
DROP TABLE IF EXISTS Platform;
DROP TABLE IF EXISTS Title;
DROP TABLE IF EXISTS TitleOnPlatform;
DROP TABLE IF EXISTS HasDeveloper;

-- CREATE tables
CREATE TABLE Title(
	id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255),
    releaseYear YEAR,
    rating ENUM('E','E10+','T','M','RP'),
    genreId INT NOT NULL,
    publisherId INT NOT NULL,
    PRIMARY KEY (id)
    );
    
CREATE TABLE Platform(
	platformId INT NOT NULL AUTO_INCREMENT,
	platformName VARCHAR(255),
	PRIMARY KEY (platformId)
);
    
CREATE TABLE Genre (
	genreId INT NOT NULL AUTO_INCREMENT,
	genreName VARCHAR(255),
	PRIMARY KEY (genreId)
);
    
CREATE TABLE Publisher (
	publisherId INT NOT NULL AUTO_INCREMENT,
	publisherName VARCHAR(255),
	PRIMARY KEY (publisherId)
);
    
CREATE TABLE Developer (
	developerId INT NOT NULL AUTO_INCREMENT,
	developerName VARCHAR(255),
	PRIMARY KEY (developerId)
);
    
CREATE TABLE TitleOnPlatform (
	titleId INT NOT NULL,
	platformId INT NOT NULL,
	salesNA DECIMAL(5,2),
	salesEU DECIMAL(5,2),
	salesJP DECIMAL(5,2),
	salesOther DECIMAL(5,2),
	salesGlobal DECIMAL(5,2),
	criticScore INT,
	criticCount INT,
	userScore DECIMAL(5,1),
	userCount INT,
	PRIMARY KEY (titleId, platformId)
);
    
CREATE TABLE HasDeveloper (
	titleId INT NOT NULL,
	developerId INT NOT NULL,
	PRIMARY KEY (titleId, developerId)
);
/*
-- ADD FOREIGN KEYS
ALTER TABLE Title ADD FOREIGN KEY (`genreId`) REFERENCES Genre(`genreId`);
ALTER TABLE Title ADD FOREIGN KEY (`publisherId`) REFERENCES Publisher(`publisherId`);

ALTER TABLE TitleOnPlatform ADD FOREIGN KEY (`titleId`) REFERENCES Title(`id`);
ALTER TABLE TitleOnPlatform ADD FOREIGN KEY (`platformId`) REFERENCES Platform(`platformId`);

ALTER TABLE HasDeveloper ADD FOREIGN KEY (`titleId`) REFERENCES Title(`id`);
ALTER TABLE HasDeveloper ADD FOREIGN KEY (`developerId`) REFERENCES Developer(`developerId`);

SET FOREIGN_KEY_CHECKS=1;

SELECT * FROM Genre;
-- INSERT INTO Developer (developerId, developerName) VALUES (1, 'Nintendo');
SELECT * FROM Developer;
*/

-- CREATE DATABASE int_flights;

SET FOREIGN_KEY_CHECKS=0;

DROP TABLE IF EXISTS Departure;
DROP TABLE IF EXISTS Airline;
DROP TABLE IF EXISTS Airport;
DROP TABLE IF EXISTS WorldArea;

CREATE TABLE Departure (
	id INT NOT NULL AUTO_INCREMENT,
    flight_year YEAR NOT NULL,
    month TINYINT NOT NULL,
    usg_apt CHAR(3) NOT NULL,
    fg_apt CHAR(3) NOT NULL,
    airline_id INT NOT NULL,
    charter INT NOT NULL,
    scheduled INT NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE Airline (
	id INT NOT NULL,
    carrier VARCHAR(7) NOT NULL,
    name VARCHAR(80) NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE Airport (
	apt CHAR(3) NOT NULL,
    name VARCHAR(52) NOT NULL,
    location VARCHAR(30) NOT NULL,
    market VARCHAR(30) NOT NULL,
    latitude DOUBLE,
    longitude DOUBLE,
    is_closed TINYINT,
    utc_time_var VARCHAR(5),
    wa_location_id INT NOT NULL,
    wa_market_id INT NOT NULL,
    PRIMARY KEY(apt)
);

CREATE TABLE WorldArea (
	id INT NOT NULL,
    name VARCHAR(46) NOT NULL,
    general_area VARCHAR(52) NOT NULL,
    capital VARCHAR(47),
    country_code CHAR(2),
    type ENUM
		("Dependency and Area of Special Sovereignty",
		"Independent State in the World") NOT NULL,
	sovereignty VARCHAR(47),
	start_date DATE NOT NULL,
    thru_date DATE,
    comments TEXT,
    PRIMARY KEY (id)
);

ALTER TABLE Departure ADD FOREIGN KEY (`usg_apt`) REFERENCES Airport(`apt`);
ALTER TABLE Departure ADD FOREIGN KEY (`fg_apt`) REFERENCES Airport(`apt`);
ALTER TABLE Departure ADD FOREIGN KEY (`airline_id`) REFERENCES Airline(`id`);
ALTER TABLE Airport ADD FOREIGN KEY (`wa_location_id`) REFERENCES WorldArea(`id`);
ALTER TABLE Airport ADD FOREIGN KEY (`wa_market_id`) REFERENCES WorldArea(`id`);

SET FOREIGN_KEY_CHECKS=1;

SELECT * FROM Airport;
SELECT * FROM Airline;
SELECT * FROM WorldArea;
SELECT * FROM Departure;
SELECT COUNT(*) FROM DEPARTURE;

SHOW PROCESSLIST;