DROP TABLE IF EXISTS people_education;
DROP TABLE IF EXISTS education;
DROP TABLE IF EXISTS people_addresses;
DROP TABLE IF EXISTS addresses;
DROP TABLE IF EXISTS people;

CREATE TABLE people (
   personid int(11) NOT NULL AUTO_INCREMENT,
   surname varchar(128),
   givenName varchar(128),
   femaleParent int(11),
   maleParent int(11),
   sex tinyint(1),
   age int(11),
   PRIMARY KEY (personid),
   FOREIGN KEY (femaleParent) REFERENCES people(personid) ON DELETE CASCADE,
   FOREIGN KEY (maleParent) REFERENCES people(personid) ON DELETE CASCADE
);

CREATE TABLE addresses (
   addressid int(11) NOT NULL AUTO_INCREMENT,
   line1 varchar(128),
   line2 varchar(128),
   city varchar(128),
   state varchar(128),
   country varchar(128),
   zip int(11),
   PRIMARY KEY (addressid)
) ENGINE=INNODB;

CREATE TABLE people_addresses (
   personid int(11) NOT NULL,
   addressid int(11) NOT NULL,
   isPrimary tinyint(1),
   PRIMARY KEY (personid, addressid),
   FOREIGN KEY (personid) REFERENCES people(personid) ON DELETE CASCADE,
   FOREIGN KEY (addressid) REFERENCES addresses(addressid) ON DELETE CASCADE
);

CREATE TABLE education (
   educationid int(11) NOT NULL AUTO_INCREMENT,
   institution varchar(256),
   addressid int(11),
   level varchar(128),
   PRIMARY KEY (educationid),
   FOREIGN KEY (addressid) REFERENCES addresses(addressid) ON DELETE CASCADE
);

CREATE TABLE people_education (
   personid int(11) NOT NULL,
   educationid int(11) NOT NULL,
   PRIMARY KEY (personid, educationid),
   FOREIGN KEY (personid) REFERENCES people(personid) ON DELETE CASCADE,
   FOREIGN KEY (educationid) REFERENCES education(educationid) ON DELETE CASCADE
);
