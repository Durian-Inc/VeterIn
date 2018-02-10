create table veterans(
	username varchar(80) not null,
	name varchar(80) not null,
	skills varchar(200),
	years_served int not null,
	rank varchar(200) not null,
	branch varchar(200) not null,
	bio varchar(120),
	image varchar(80),
	contact varchar(80)
	primary key(username)
);

insert into veterans (username, name, skills, years_served, rank, branch, bio, image, contact, employed) values("25cent9", "Innocent Niyibizi", "Hacking, Computer Programming, Wire Tapping, Photography", 3, "Private","Army", "Hello, my name is Innocent and I was in the Army for three years. I was given tasks that are really under NDA", "inni.gif", "25cent9@gmail.com");

CREATE TABLE organization (
	id int not null,
	name varchar ( 80 ) not null,
	location varchar ( 80 ) not null,
	image varchar ( 80 ) not null,
	url varchar ( 80 ) not null,
	industry varchar ( 80 ) not null,
	profit int check (profit <=1 and profit >=0),
	bio	varchar ( 240 ),
	contact	varchar ( 240 ) not null,
	PRIMARY KEY(id)
);

INSERT INTO organization (id, name, location, image, url, industry, profit, bio, contact) VALUES (1, "Innocent's Vet Store", "123 Sesame Street", "vetstore.jpg", "iniyibzi.com", "Public Sector", 1, "Hello, Innocent's Vet Store is mostly aimed towards helping veterans buy from other veterans. Our motto is 'From Veterans, By Veterans' ", "(123)-buy-vets");

create table post(
	postdate datetime not null,
	image varchar(80),
	posttext varchar(120) not null,
	posterid int not null,
	primary key(postdate, posterid),
	foreign key(posterid) references organization(id)
);

INSERT INTO post (postdate, image, posttext, posterid) VALUES ('2015-05-01', "postone.jpg", "Hey this is a test post!", 1);

create table partof(
	username varchar(80) not null,
	orgid int not null,
	position varchar(80) not null,
	primary key(username,orgID, position),
	foreign key(username) references veterans(username),
	foreign key(orgid) references organization(id)
);

INSERT INTO partof (username, orgid, position) VALUES ("25cent9", 1, "owner");
