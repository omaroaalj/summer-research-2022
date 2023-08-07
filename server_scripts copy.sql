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
SELECT * FROM Country;
SELECT * FROM Category;
SELECT * FROM CountryOnCategory;