DROP TABLE IF EXISTS people;
CREATE TABLE people (
   personid int(11) NOT NULL AUTO_INCREMENT,
   surname varchar(128),
   givenname varchar(128),
   sex char(1),
   age int(11),
   PRIMARY KEY (personid)
);

DROP TABLE IF EXISTS people_addresses;
CREATE TABLE people_addresses (
   personid int(11) NOT NULL,
   addressid int(11) NOT NULL,
   isPrimary tinyint(1),
   PRIMARY KEY (personid, addressid),
   FOREIGN KEY (personid) REFERENCES people(personid) ON DELETE CASCADE,
   FOREIGN KEY (addressid) REFERENCES addresses(addressid) ON DELETE CASCADE
);

DROP TABLE IF EXISTS addresses;
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

DROP TABLE IF EXISTS education;
CREATE TABLE education (
   personid int(11) NOT NULL,
   institution varchar(256),
   addressid int(11),
   PRIMARY KEY (personid),
   FOREIGN KEY (personid) REFERENCES people(personid) ON DELETE CASCADE,
   FOREIGN KEY (addressid) REFERENCES addresses(addressid) ON DELETE CASCADE
);
