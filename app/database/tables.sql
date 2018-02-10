create table veterans(
	username varchar(80) not null,
	name varchar(80),
	skills varchar(200),
	years_served int,
	rank varchar(200),
	branch varchar(200),
	bio varchar(120),
	image varchar(80),
	primary key(username)
);

create table organization(
	ID int,
	orgName varchar(80),
	location varchar(80),
	imagestring varchar(80),
	URL varchar(80),
	industry varchar(80),
	profit bit,
	primary key(ID)
);

create table post(
	date_time datetime,
	image varchar(80),
	test varchar(120),
	poster_ID int,
	primary key(date_time,poster_ID),
	foreign key(poster_ID) references organization(ID)
);

create table partOf(
	username varchar(80),
	orgID int,
	position varchar(80),
	primary key(username,orgID,position),
	foreign key(username) references veterans(username),
	foreign key(orgID) references organization(ID)
);
