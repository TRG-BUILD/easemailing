PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE surveys (
	id INTEGER NOT NULL, 
	name VARCHAR(255), 
	PRIMARY KEY (id)
);
INSERT INTO surveys VALUES(1293732,'EASE - del 1b');
CREATE TABLE labels (
	id INTEGER NOT NULL, 
	organization INTEGER, 
	survey_id INTEGER, 
	field_name VARCHAR NOT NULL, 
	field_value INTEGER NOT NULL, 
	field_text VARCHAR(255) NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (field_name, field_value), 
	FOREIGN KEY(survey_id) REFERENCES surveys (id)
);
INSERT INTO labels VALUES(1,260660,1293732,'statinternal_1',0,'Ikke valgt');
INSERT INTO labels VALUES(2,260660,1293732,'statinternal_1',1,'Valgt');
INSERT INTO labels VALUES(3,260660,1293732,'statinternal_2',0,'Ikke valgt');
INSERT INTO labels VALUES(4,260660,1293732,'statinternal_2',1,'Valgt');
INSERT INTO labels VALUES(5,260660,1293732,'statinternal_3',0,'Ikke valgt');
INSERT INTO labels VALUES(6,260660,1293732,'statinternal_3',1,'Valgt');
INSERT INTO labels VALUES(7,260660,1293732,'statinternal_4',0,'Ikke valgt');
INSERT INTO labels VALUES(8,260660,1293732,'statinternal_4',1,'Valgt');
INSERT INTO labels VALUES(9,260660,1293732,'statinternal_5',0,'Ikke valgt');
INSERT INTO labels VALUES(10,260660,1293732,'statinternal_5',1,'Valgt');
INSERT INTO labels VALUES(11,260660,1293732,'statinternal_6',0,'Ikke valgt');
INSERT INTO labels VALUES(12,260660,1293732,'statinternal_6',1,'Valgt');
INSERT INTO labels VALUES(13,260660,1293732,'statinternal_7',0,'Ikke valgt');
INSERT INTO labels VALUES(14,260660,1293732,'statinternal_7',1,'Valgt');
INSERT INTO labels VALUES(15,260660,1293732,'statinternal_8',0,'Ikke valgt');
INSERT INTO labels VALUES(16,260660,1293732,'statinternal_8',1,'Valgt');
INSERT INTO labels VALUES(17,260660,1293732,'statinternal_9',0,'Ikke valgt');
INSERT INTO labels VALUES(18,260660,1293732,'statinternal_9',1,'Valgt');
INSERT INTO labels VALUES(19,260660,1293732,'statinternal_10',0,'Ikke valgt');
INSERT INTO labels VALUES(20,260660,1293732,'statinternal_10',1,'Valgt');
INSERT INTO labels VALUES(21,260660,1293732,'statinternal_11',0,'Ikke valgt');
INSERT INTO labels VALUES(22,260660,1293732,'statinternal_11',1,'Valgt');
INSERT INTO labels VALUES(23,260660,1293732,'statinternal_12',0,'Ikke valgt');
INSERT INTO labels VALUES(24,260660,1293732,'statinternal_12',1,'Valgt');
INSERT INTO labels VALUES(25,260660,1293732,'statinternal_13',0,'Ikke valgt');
INSERT INTO labels VALUES(26,260660,1293732,'statinternal_13',1,'Valgt');
INSERT INTO labels VALUES(27,260660,1293732,'statinternal_14',0,'Ikke valgt');
INSERT INTO labels VALUES(28,260660,1293732,'statinternal_14',1,'Valgt');
INSERT INTO labels VALUES(29,260660,1293732,'statinternal_15',0,'Ikke valgt');
INSERT INTO labels VALUES(30,260660,1293732,'statinternal_15',1,'Valgt');
INSERT INTO labels VALUES(31,260660,1293732,'statinternal_16',0,'Ikke valgt');
INSERT INTO labels VALUES(32,260660,1293732,'statinternal_16',1,'Valgt');
INSERT INTO labels VALUES(33,260660,1293732,'statinternal_17',0,'Ikke valgt');
INSERT INTO labels VALUES(34,260660,1293732,'statinternal_17',1,'Valgt');
INSERT INTO labels VALUES(35,260660,1293732,'statinternal_18',0,'Ikke valgt');
INSERT INTO labels VALUES(36,260660,1293732,'statinternal_18',1,'Valgt');
INSERT INTO labels VALUES(37,260660,1293732,'statinternal_19',0,'Ikke valgt');
INSERT INTO labels VALUES(38,260660,1293732,'statinternal_19',1,'Valgt');
INSERT INTO labels VALUES(39,260660,1293732,'statinternal_20',0,'Ikke valgt');
INSERT INTO labels VALUES(40,260660,1293732,'statinternal_20',1,'Valgt');
INSERT INTO labels VALUES(41,260660,1293732,'digitaldistributionstatus',1,'Succes');
INSERT INTO labels VALUES(42,260660,1293732,'digitaldistributionstatus',2,'Fejlet');
INSERT INTO labels VALUES(43,260660,1293732,'digitaldistributionstatus',3,'-');
INSERT INTO labels VALUES(44,260660,1293732,'digitaldistributionstatus',4,'I kø');
INSERT INTO labels VALUES(45,260660,1293732,'digitaldistributionstatus',6,'Frafaldet');
INSERT INTO labels VALUES(46,260660,1293732,'digitaldistributionstatus',5,'Fritaget');
INSERT INTO labels VALUES(47,260660,1293732,'risikovurdering',1,'I høj grad');
INSERT INTO labels VALUES(48,260660,1293732,'risikovurdering',2,'I nogen grad');
INSERT INTO labels VALUES(49,260660,1293732,'risikovurdering',3,'I mindre grad');
INSERT INTO labels VALUES(50,260660,1293732,'risikovurdering',4,'I ringe grad');
INSERT INTO labels VALUES(51,260660,1293732,'risikovurdering',5,'Slet ikke');
INSERT INTO labels VALUES(52,260660,1293732,'anbefalinger',1,'I høj grad');
INSERT INTO labels VALUES(53,260660,1293732,'anbefalinger',2,'I nogen grad');
INSERT INTO labels VALUES(54,260660,1293732,'anbefalinger',3,'I mindre grad');
INSERT INTO labels VALUES(55,260660,1293732,'anbefalinger',4,'I ringe grad');
INSERT INTO labels VALUES(56,260660,1293732,'anbefalinger',5,'Slet ikke');
INSERT INTO labels VALUES(57,260660,1293732,'hast_revurdering',1,'I høj grad');
INSERT INTO labels VALUES(58,260660,1293732,'hast_revurdering',2,'I nogen grad');
INSERT INTO labels VALUES(59,260660,1293732,'hast_revurdering',3,'I mindre grad');
INSERT INTO labels VALUES(60,260660,1293732,'hast_revurdering',4,'I ringe grad');
INSERT INTO labels VALUES(61,260660,1293732,'hast_revurdering',5,'Slet ikke');
INSERT INTO labels VALUES(62,260660,1293732,'nyviden',1,'I høj grad');
INSERT INTO labels VALUES(63,260660,1293732,'nyviden',2,'I nogen grad');
INSERT INTO labels VALUES(64,260660,1293732,'nyviden',3,'I mindre grad');
INSERT INTO labels VALUES(65,260660,1293732,'nyviden',4,'I ringe grad');
INSERT INTO labels VALUES(66,260660,1293732,'nyviden',5,'Slet ikke');
INSERT INTO labels VALUES(67,260660,1293732,'opmaerksomhedsniveau',1,'I høj grad');
INSERT INTO labels VALUES(68,260660,1293732,'opmaerksomhedsniveau',2,'I nogen grad');
INSERT INTO labels VALUES(69,260660,1293732,'opmaerksomhedsniveau',3,'I mindre grad');
INSERT INTO labels VALUES(70,260660,1293732,'opmaerksomhedsniveau',4,'I ringe grad');
INSERT INTO labels VALUES(71,260660,1293732,'opmaerksomhedsniveau',5,'Slet ikke');
INSERT INTO labels VALUES(72,260660,1293732,'overhold_fremover',1,'I høj grad');
INSERT INTO labels VALUES(73,260660,1293732,'overhold_fremover',2,'I nogen grad');
INSERT INTO labels VALUES(74,260660,1293732,'overhold_fremover',3,'I mindre grad');
INSERT INTO labels VALUES(75,260660,1293732,'overhold_fremover',4,'I ringe grad');
INSERT INTO labels VALUES(76,260660,1293732,'overhold_fremover',5,'Slet ikke');
INSERT INTO labels VALUES(77,260660,1293732,'andrebilister',1,'I høj grad');
INSERT INTO labels VALUES(78,260660,1293732,'andrebilister',2,'I nogen grad');
INSERT INTO labels VALUES(79,260660,1293732,'andrebilister',3,'I mindre grad');
INSERT INTO labels VALUES(80,260660,1293732,'andrebilister',4,'I ringe grad');
INSERT INTO labels VALUES(81,260660,1293732,'andrebilister',5,'Slet ikke');
INSERT INTO labels VALUES(82,260660,1293732,'situation1',1,'Når jeg bliver overhalet');
INSERT INTO labels VALUES(83,260660,1293732,'situation1',2,'For at følge trafikkens flow');
INSERT INTO labels VALUES(84,260660,1293732,'situation1',3,'Når en bagvedkørende trafikant presser mig');
INSERT INTO labels VALUES(85,260660,1293732,'situation1',4,'Når jeg har siddet fast bag nogen, der kører langsomt');
INSERT INTO labels VALUES(86,260660,1293732,'situation1',5,'Når der kun er lidt eller ingen anden trafik');
INSERT INTO labels VALUES(87,260660,1293732,'situation1',6,'Når jeg kører på en vej, hvor jeg mener, at hastighedsgrænsen skulle være højere');
INSERT INTO labels VALUES(88,260660,1293732,'situation1',7,'Når jeg skal køre langt');
INSERT INTO labels VALUES(89,260660,1293732,'situation1',8,'Når jeg er er stresset ');
INSERT INTO labels VALUES(90,260660,1293732,'situation1',15,'Når passagerer opfordrer mig til det (direkte eller indirekte)');
INSERT INTO labels VALUES(91,260660,1293732,'situation1',10,'Når jeg er sent på den');
INSERT INTO labels VALUES(92,260660,1293732,'situation1',11,'Når jeg kører på strækninger, jeg kender godt');
INSERT INTO labels VALUES(93,260660,1293732,'situation1',12,'Når der er lille risiko for at blive opdaget af politiet');
INSERT INTO labels VALUES(94,260660,1293732,'situation1',13,'Når bilen gerne vil køre hurtigere');
INSERT INTO labels VALUES(95,260660,1293732,'strategi1',1,'Hvor ubehageligt det vil være, hvis nogen kom til skade eller mistede livet pga. min fart');
INSERT INTO labels VALUES(96,260660,1293732,'strategi1',2,'At hastighedsovertrædelser øger brændstofforbruget. Det skader miljøet og er dyrt');
INSERT INTO labels VALUES(97,260660,1293732,'strategi1',3,'At der er mennesker i mit liv, der ønsker at jeg overholder hastighedsgrænsen');
INSERT INTO labels VALUES(98,260660,1293732,'strategi1',17,'At hastighedsovertrædelser generelt ikke accepteres i samfundet');
INSERT INTO labels VALUES(99,260660,1293732,'strategi1',18,'Hvor pinligt det vil være at få en fartbøde');
INSERT INTO labels VALUES(100,260660,1293732,'strategi1',10,'At det har konsekvenser at blive taget af politiet for at køre for stærkt');
INSERT INTO labels VALUES(101,260660,1293732,'strategi1',11,'At det ikke er foreneligt med min opfattelse af mig selv som en god og hensynsfuld bilist');
INSERT INTO labels VALUES(102,260660,1293732,'strategi1',19,'At bruge fartpilot eller fartbegrænser til at styre min hastighed');
INSERT INTO labels VALUES(103,260660,1293732,'strategi1',20,'At det er bedre at komme for sent end at køre for stærkt');
INSERT INTO labels VALUES(104,260660,1293732,'strategi1',13,'At jeg ikke sparer ret meget tid ved at køre for stærkt');
INSERT INTO labels VALUES(105,260660,1293732,'strategi1',14,'At jeg skal forsøge at undgå at sætte mig selv i en lignende situation igen');
INSERT INTO labels VALUES(106,260660,1293732,'strategi1',15,'At selv om det er let og dejligt at køre for stærkt, så er det en farlig vane');
INSERT INTO labels VALUES(107,260660,1293732,'strategi1',21,'At høj fart gør det sværere at reagere i tide, hvis andre laver fejl');
INSERT INTO labels VALUES(108,260660,1293732,'situation2',1,'Når jeg bliver overhalet');
INSERT INTO labels VALUES(109,260660,1293732,'situation2',2,'For at følge trafikkens flow');
INSERT INTO labels VALUES(110,260660,1293732,'situation2',3,'Når en bagvedkørende trafikant presser mig');
INSERT INTO labels VALUES(111,260660,1293732,'situation2',4,'Når jeg har siddet fast bag nogen, der kører langsomt');
INSERT INTO labels VALUES(112,260660,1293732,'situation2',5,'Når der kun er lidt eller ingen anden trafik');
INSERT INTO labels VALUES(113,260660,1293732,'situation2',6,'Når jeg kører på en vej, hvor jeg mener, at hastighedsgrænsen skulle være højere');
INSERT INTO labels VALUES(114,260660,1293732,'situation2',7,'Når jeg skal køre langt');
INSERT INTO labels VALUES(115,260660,1293732,'situation2',8,'Når jeg er er stresset ');
INSERT INTO labels VALUES(116,260660,1293732,'situation2',15,'Når passagerer opfordrer mig til det (direkte eller indirekte)');
INSERT INTO labels VALUES(117,260660,1293732,'situation2',10,'Når jeg er sent på den');
INSERT INTO labels VALUES(118,260660,1293732,'situation2',11,'Når jeg kører på strækninger, jeg kender godt');
INSERT INTO labels VALUES(119,260660,1293732,'situation2',12,'Når der er lille risiko for at blive opdaget af politiet');
INSERT INTO labels VALUES(120,260660,1293732,'situation2',13,'Når bilen gerne vil køre hurtigere');
INSERT INTO labels VALUES(121,260660,1293732,'strategi2',1,'Hvor ubehageligt det vil være, hvis nogen kom til skade eller mistede livet pga. min fart');
INSERT INTO labels VALUES(122,260660,1293732,'strategi2',2,'At hastighedsovertrædelser øger brændstofforbruget. Det skader miljøet og er dyrt');
INSERT INTO labels VALUES(123,260660,1293732,'strategi2',3,'At der er mennesker i mit liv, der ønsker at jeg overholder hastighedsgrænsen');
INSERT INTO labels VALUES(124,260660,1293732,'strategi2',17,'At hastighedsovertrædelser generelt ikke accepteres i samfundet');
INSERT INTO labels VALUES(125,260660,1293732,'strategi2',18,'Hvor pinligt det vil være at få en fartbøde');
INSERT INTO labels VALUES(126,260660,1293732,'strategi2',10,'At det har konsekvenser at blive taget af politiet for at køre for stærkt');
INSERT INTO labels VALUES(127,260660,1293732,'strategi2',11,'At det ikke er foreneligt med min opfattelse af mig selv som en god og hensynsfuld bilist');
INSERT INTO labels VALUES(128,260660,1293732,'strategi2',19,'At bruge fartpilot eller fartbegrænser til at styre min hastighed');
INSERT INTO labels VALUES(129,260660,1293732,'strategi2',20,'At det er bedre at komme for sent end at køre for stærkt');
INSERT INTO labels VALUES(130,260660,1293732,'strategi2',13,'At jeg ikke sparer ret meget tid ved at køre for stærkt');
INSERT INTO labels VALUES(131,260660,1293732,'strategi2',14,'At jeg skal forsøge at undgå at sætte mig selv i en lignende situation igen');
INSERT INTO labels VALUES(132,260660,1293732,'strategi2',15,'At selv om det er let og dejligt at køre for stærkt, så er det en farlig vane');
INSERT INTO labels VALUES(133,260660,1293732,'strategi2',21,'At høj fart gør det sværere at reagere i tide, hvis andre laver fejl');
INSERT INTO labels VALUES(134,260660,1293732,'situation3',1,'Når jeg bliver overhalet');
INSERT INTO labels VALUES(135,260660,1293732,'situation3',2,'For at følge trafikkens flow');
INSERT INTO labels VALUES(136,260660,1293732,'situation3',3,'Når en bagvedkørende trafikant presser mig');
INSERT INTO labels VALUES(137,260660,1293732,'situation3',4,'Når jeg har siddet fast bag nogen, der kører langsomt');
INSERT INTO labels VALUES(138,260660,1293732,'situation3',5,'Når der kun er lidt eller ingen anden trafik');
INSERT INTO labels VALUES(139,260660,1293732,'situation3',6,'Når jeg kører på en vej, hvor jeg mener, at hastighedsgrænsen skulle være højere');
INSERT INTO labels VALUES(140,260660,1293732,'situation3',7,'Når jeg skal køre langt');
INSERT INTO labels VALUES(141,260660,1293732,'situation3',8,'Når jeg er er stresset ');
INSERT INTO labels VALUES(142,260660,1293732,'situation3',15,'Når passagerer opfordrer mig til det (direkte eller indirekte)');
INSERT INTO labels VALUES(143,260660,1293732,'situation3',10,'Når jeg er sent på den');
INSERT INTO labels VALUES(144,260660,1293732,'situation3',11,'Når jeg kører på strækninger, jeg kender godt');
INSERT INTO labels VALUES(145,260660,1293732,'situation3',12,'Når der er lille risiko for at blive opdaget af politiet');
INSERT INTO labels VALUES(146,260660,1293732,'situation3',13,'Når bilen gerne vil køre hurtigere');
INSERT INTO labels VALUES(147,260660,1293732,'strategi3',1,'Hvor ubehageligt det vil være, hvis nogen kom til skade eller mistede livet pga. min fart');
INSERT INTO labels VALUES(148,260660,1293732,'strategi3',2,'At hastighedsovertrædelser øger brændstofforbruget. Det skader miljøet og er dyrt');
INSERT INTO labels VALUES(149,260660,1293732,'strategi3',3,'At der er mennesker i mit liv, der ønsker at jeg overholder hastighedsgrænsen');
INSERT INTO labels VALUES(150,260660,1293732,'strategi3',17,'At hastighedsovertrædelser generelt ikke accepteres i samfundet');
INSERT INTO labels VALUES(151,260660,1293732,'strategi3',18,'Hvor pinligt det vil være at få en fartbøde');
INSERT INTO labels VALUES(152,260660,1293732,'strategi3',10,'At det har konsekvenser at blive taget af politiet for at køre for stærkt');
INSERT INTO labels VALUES(153,260660,1293732,'strategi3',11,'At det ikke er foreneligt med min opfattelse af mig selv som en god og hensynsfuld bilist');
INSERT INTO labels VALUES(154,260660,1293732,'strategi3',19,'At bruge fartpilot eller fartbegrænser til at styre min hastighed');
INSERT INTO labels VALUES(155,260660,1293732,'strategi3',20,'At det er bedre at komme for sent end at køre for stærkt');
INSERT INTO labels VALUES(156,260660,1293732,'strategi3',13,'At jeg ikke sparer ret meget tid ved at køre for stærkt');
INSERT INTO labels VALUES(157,260660,1293732,'strategi3',14,'At jeg skal forsøge at undgå at sætte mig selv i en lignende situation igen');
INSERT INTO labels VALUES(158,260660,1293732,'strategi3',15,'At selv om det er let og dejligt at køre for stærkt, så er det en farlig vane');
INSERT INTO labels VALUES(159,260660,1293732,'strategi3',21,'At høj fart gør det sværere at reagere i tide, hvis andre laver fejl');
INSERT INTO labels VALUES(160,260660,1293732,'strategimail',1,'Ja tak');
INSERT INTO labels VALUES(161,260660,1293732,'strategimail',2,'Nej tak');
INSERT INTO labels VALUES(162,260660,1293732,'strategireminder',1,'Ja tak');
INSERT INTO labels VALUES(163,260660,1293732,'strategireminder',2,'Nej tak');
INSERT INTO labels VALUES(164,260660,1293732,'statcompletion_1',0,'Ikke valgt');
INSERT INTO labels VALUES(165,260660,1293732,'statcompletion_1',1,'Valgt');
INSERT INTO labels VALUES(166,260660,1293732,'statcompletion_2',0,'Ikke valgt');
INSERT INTO labels VALUES(167,260660,1293732,'statcompletion_2',1,'Valgt');
INSERT INTO labels VALUES(168,260660,1293732,'statcompletion_3',0,'Ikke valgt');
INSERT INTO labels VALUES(169,260660,1293732,'statcompletion_3',1,'Valgt');
INSERT INTO labels VALUES(170,260660,1293732,'statcreation_1',0,'Ikke valgt');
INSERT INTO labels VALUES(171,260660,1293732,'statcreation_1',1,'Valgt');
INSERT INTO labels VALUES(172,260660,1293732,'statcreation_2',0,'Ikke valgt');
INSERT INTO labels VALUES(173,260660,1293732,'statcreation_2',1,'Valgt');
INSERT INTO labels VALUES(174,260660,1293732,'statcreation_3',0,'Ikke valgt');
INSERT INTO labels VALUES(175,260660,1293732,'statcreation_3',1,'Valgt');
INSERT INTO labels VALUES(176,260660,1293732,'statcreation_4',0,'Ikke valgt');
INSERT INTO labels VALUES(177,260660,1293732,'statcreation_4',1,'Valgt');
INSERT INTO labels VALUES(178,260660,1293732,'statcreation_5',0,'Ikke valgt');
INSERT INTO labels VALUES(179,260660,1293732,'statcreation_5',1,'Valgt');
INSERT INTO labels VALUES(180,260660,1293732,'statcreation_6',0,'Ikke valgt');
INSERT INTO labels VALUES(181,260660,1293732,'statcreation_6',1,'Valgt');
INSERT INTO labels VALUES(182,260660,1293732,'statcreation_7',0,'Ikke valgt');
INSERT INTO labels VALUES(183,260660,1293732,'statcreation_7',1,'Valgt');
INSERT INTO labels VALUES(184,260660,1293732,'statdistribution_1',0,'Ikke valgt');
INSERT INTO labels VALUES(185,260660,1293732,'statdistribution_1',1,'Valgt');
INSERT INTO labels VALUES(186,260660,1293732,'statdistribution_2',0,'Ikke valgt');
INSERT INTO labels VALUES(187,260660,1293732,'statdistribution_2',1,'Valgt');
INSERT INTO labels VALUES(188,260660,1293732,'statdistribution_3',0,'Ikke valgt');
INSERT INTO labels VALUES(189,260660,1293732,'statdistribution_3',1,'Valgt');
INSERT INTO labels VALUES(190,260660,1293732,'statdistribution_4',0,'Ikke valgt');
INSERT INTO labels VALUES(191,260660,1293732,'statdistribution_4',1,'Valgt');
INSERT INTO labels VALUES(192,260660,1293732,'statdistribution_5',0,'Ikke valgt');
INSERT INTO labels VALUES(193,260660,1293732,'statdistribution_5',1,'Valgt');
INSERT INTO labels VALUES(194,260660,1293732,'statsource_1',0,'Ikke valgt');
INSERT INTO labels VALUES(195,260660,1293732,'statsource_1',1,'Valgt');
INSERT INTO labels VALUES(196,260660,1293732,'statsource_2',0,'Ikke valgt');
INSERT INTO labels VALUES(197,260660,1293732,'statsource_2',1,'Valgt');
INSERT INTO labels VALUES(198,260660,1293732,'statsource_3',0,'Ikke valgt');
INSERT INTO labels VALUES(199,260660,1293732,'statsource_3',1,'Valgt');
INSERT INTO labels VALUES(200,260660,1293732,'statsource_4',0,'Ikke valgt');
INSERT INTO labels VALUES(201,260660,1293732,'statsource_4',1,'Valgt');
INSERT INTO labels VALUES(202,260660,1293732,'statsource_5',0,'Ikke valgt');
INSERT INTO labels VALUES(203,260660,1293732,'statsource_5',1,'Valgt');
INSERT INTO labels VALUES(204,260660,1293732,'statsource_6',0,'Ikke valgt');
INSERT INTO labels VALUES(205,260660,1293732,'statsource_6',1,'Valgt');
INSERT INTO labels VALUES(206,260660,1293732,'statcollect_1',0,'Ikke valgt');
INSERT INTO labels VALUES(207,260660,1293732,'statcollect_1',1,'Valgt');
INSERT INTO labels VALUES(208,260660,1293732,'statcollect_2',0,'Ikke valgt');
INSERT INTO labels VALUES(209,260660,1293732,'statcollect_2',1,'Valgt');
INSERT INTO labels VALUES(210,260660,1293732,'statcollect_3',0,'Ikke valgt');
INSERT INTO labels VALUES(211,260660,1293732,'statcollect_3',1,'Valgt');
INSERT INTO labels VALUES(212,260660,1293732,'statcollect_4',0,'Ikke valgt');
INSERT INTO labels VALUES(213,260660,1293732,'statcollect_4',1,'Valgt');
INSERT INTO labels VALUES(214,260660,1293732,'statoverall_1',0,'Ikke valgt');
INSERT INTO labels VALUES(215,260660,1293732,'statoverall_1',1,'Valgt');
INSERT INTO labels VALUES(216,260660,1293732,'statoverall_2',0,'Ikke valgt');
INSERT INTO labels VALUES(217,260660,1293732,'statoverall_2',1,'Valgt');
INSERT INTO labels VALUES(218,260660,1293732,'statoverall_3',0,'Ikke valgt');
INSERT INTO labels VALUES(219,260660,1293732,'statoverall_3',1,'Valgt');
INSERT INTO labels VALUES(220,260660,1293732,'statoverall_4',0,'Ikke valgt');
INSERT INTO labels VALUES(221,260660,1293732,'statoverall_4',1,'Valgt');
INSERT INTO labels VALUES(222,260660,1293732,'statoverall_5',0,'Ikke valgt');
INSERT INTO labels VALUES(223,260660,1293732,'statoverall_5',1,'Valgt');
CREATE TABLE answers3 (
	answer_id INTEGER NOT NULL, 
	survey_id INTEGER, 
	respondentid INTEGER, 
	organization INTEGER, 
	statinternal_1 INTEGER, 
	statinternal_2 INTEGER, 
	statinternal_3 INTEGER, 
	statinternal_4 INTEGER, 
	statinternal_5 INTEGER, 
	statinternal_6 INTEGER, 
	statinternal_7 INTEGER, 
	statinternal_8 INTEGER, 
	statinternal_9 INTEGER, 
	statinternal_10 INTEGER, 
	statinternal_11 INTEGER, 
	statinternal_12 INTEGER, 
	statinternal_13 INTEGER, 
	statinternal_14 INTEGER, 
	statinternal_15 INTEGER, 
	statinternal_16 INTEGER, 
	statinternal_17 INTEGER, 
	statinternal_18 INTEGER, 
	statinternal_19 INTEGER, 
	statinternal_20 INTEGER, 
	created DATETIME, 
	modified DATETIME, 
	closetime DATETIME, 
	starttime DATETIME, 
	difftime FLOAT, 
	responsecollectsessions INTEGER, 
	numberofreturnedmail INTEGER, 
	importgroup INTEGER, 
	distributionschedule VARCHAR, 
	email VARCHAR, 
	digitaldistributionstatus VARCHAR, 
	digitaldistributionerrormessage VARCHAR, 
	risikovurdering INTEGER, 
	anbefalinger INTEGER, 
	hast_revurdering INTEGER, 
	nyviden INTEGER, 
	opmaerksomhedsniveau INTEGER, 
	overhold_fremover INTEGER, 
	andrebilister INTEGER, 
	uddyb_evaluering INTEGER, 
	situation1 INTEGER, 
	strategi1 INTEGER, 
	situation2 INTEGER, 
	strategi2 INTEGER, 
	situation3 INTEGER, 
	strategi3 INTEGER, 
	strategi_tekstfelt TEXT, 
	strategimail INTEGER, 
	strategireminder INTEGER, 
	email_strategi VARCHAR(255), 
	slutkommentar_1b TEXT, 
	id VARCHAR(50), 
	gr VARCHAR(1), 
	s INTEGER, 
	statcompletion_1 INTEGER, 
	statcompletion_2 INTEGER, 
	statcompletion_3 INTEGER, 
	statcreation_1 INTEGER, 
	statcreation_2 INTEGER, 
	statcreation_3 INTEGER, 
	statcreation_4 INTEGER, 
	statcreation_5 INTEGER, 
	statcreation_6 INTEGER, 
	statcreation_7 INTEGER, 
	statdistribution_1 INTEGER, 
	statdistribution_2 INTEGER, 
	statdistribution_3 INTEGER, 
	statdistribution_4 INTEGER, 
	statdistribution_5 INTEGER, 
	statsource_1 INTEGER, 
	statsource_2 INTEGER, 
	statsource_3 INTEGER, 
	statsource_4 INTEGER, 
	statsource_5 INTEGER, 
	statsource_6 INTEGER, 
	statcollect_1 INTEGER, 
	statcollect_2 INTEGER, 
	statcollect_3 INTEGER, 
	statcollect_4 INTEGER, 
	statoverall_1 INTEGER, 
	statoverall_2 INTEGER, 
	statoverall_3 INTEGER, 
	statoverall_4 INTEGER, 
	statoverall_5 INTEGER, 
	strategi_mail_send_first DATETIME, 
	strategi_mail_send_first_failed DATETIME, 
	strategi_mail_send_second DATETIME, 
	strategi_mail_send_second_failed DATETIME, 
	PRIMARY KEY (answer_id), 
	FOREIGN KEY(survey_id) REFERENCES surveys (id)
);
INSERT INTO answers3 VALUES(0,1293732,822906637,260660,0,0,0,1,0,1,1,0,0,0,1,0,1,0,0,0,0,0,0,0,'2021-08-20 10:27:52','2021-09-17 11:27:08','2021-08-20 10:30:25','2021-08-20 10:28:58','87,296',1,0,NULL,NULL,NULL,'3',NULL,2,3,4,1,3,4,1,NULL,15,3,3,1,7,11,NULL,2,NULL,NULL,NULL,'TEST','r',70,1,1,0,0,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,NULL,NULL,NULL,NULL);
INSERT INTO answers3 VALUES(1,1293732,824124765,260660,0,0,0,1,0,1,1,0,0,0,1,0,1,0,0,0,0,0,0,0,'2021-08-26 08:37:54','2021-09-17 11:27:08','2021-08-26 08:41:34','2021-08-26 08:38:22','191,453',1,0,NULL,NULL,NULL,'3',NULL,1,1,1,3,2,2,1,NULL,4,13,5,19,2,2,NULL,2,NULL,NULL,NULL,'C7MUP58YLR1G','g',185,1,1,0,0,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,NULL,NULL,NULL,NULL);
INSERT INTO answers3 VALUES(2,1293732,824082899,260660,0,0,0,1,0,1,1,0,0,0,1,0,1,0,0,0,0,0,0,0,'2021-08-25 17:32:08','2021-09-17 11:27:08','2021-08-25 17:36:29','2021-08-25 17:32:36','232,463',1,0,NULL,NULL,NULL,'1',NULL,1,3,1,4,3,3,2,NULL,10,13,8,11,3,11,NULL,1,NULL,'msam@build.aau.dk',NULL,'LYQV6C2ZLQ3D','g',165,1,1,0,0,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,NULL,NULL,NULL,NULL);
INSERT INTO answers3 VALUES(3,1293732,827280790,260660,0,0,0,1,0,1,1,0,0,0,1,0,0,1,0,0,0,0,0,0,'2021-09-10 14:56:56','2021-09-17 11:27:08','2021-09-10 14:58:00','2021-09-10 14:57:03','56,586',1,0,NULL,NULL,NULL,'1',NULL,2,3,3,3,3,3,3,NULL,11,17,3,20,5,19,NULL,1,1,'msam@build.aau.dk',NULL,NULL,NULL,NULL,1,1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,1,0,NULL,NULL,NULL,NULL);
INSERT INTO answers3 VALUES(4,1293732,827288913,260660,0,0,0,1,0,1,1,0,0,0,1,0,0,1,0,0,0,0,0,0,'2021-09-10 16:14:32','2021-09-17 11:27:08','2021-09-10 16:15:03','2021-09-10 16:14:36','27,22',1,0,NULL,NULL,NULL,'1',NULL,2,4,3,3,2,3,3,NULL,1,2,5,21,4,17,NULL,1,2,'msam@build.aau.dk',NULL,NULL,NULL,NULL,1,1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,1,0,NULL,NULL,NULL,NULL);
INSERT INTO answers3 VALUES(5,1293732,825480658,260660,0,0,0,1,0,1,1,0,0,0,1,0,0,1,0,0,0,0,0,0,'2021-09-02 19:45:57','2021-09-17 11:27:08','2021-09-02 19:46:34','2021-09-02 19:46:02','31,57',1,0,NULL,NULL,NULL,'1',NULL,3,2,4,2,3,2,3,NULL,8,2,10,2,7,2,NULL,1,2,'msam@build.aau.dk',NULL,NULL,NULL,NULL,1,1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,1,0,NULL,NULL,NULL,NULL);
INSERT INTO answers3 VALUES(6,1293732,827288742,260660,0,0,0,1,0,1,1,0,0,0,1,0,0,1,0,0,0,0,0,0,'2021-09-10 16:11:38','2021-09-17 11:27:08','2021-09-10 16:12:12','2021-09-10 16:11:42','29,323',1,0,NULL,NULL,NULL,'1',NULL,2,4,2,3,4,2,3,NULL,5,14,2,18,13,3,NULL,1,1,'msam@build.aau.dk',NULL,NULL,NULL,NULL,1,1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,1,0,NULL,NULL,NULL,NULL);
INSERT INTO answers3 VALUES(7,1293732,828094766,260660,0,0,0,1,0,1,1,0,0,0,1,0,1,0,0,0,0,0,0,0,'2021-09-15 08:51:50','2021-09-17 11:27:08','2021-09-15 09:23:42','2021-09-15 09:11:09','752,69',1,0,NULL,NULL,NULL,'3',NULL,3,2,2,2,1,2,2,NULL,11,20,6,11,15,20,NULL,2,2,NULL,NULL,'TEST','y',NULL,1,1,0,0,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,NULL,NULL,NULL,NULL);
INSERT INTO answers3 VALUES(8,1293732,827280888,260660,0,0,0,1,0,1,1,0,0,0,1,0,0,1,0,0,0,0,0,0,'2021-09-10 14:59:19','2021-09-17 11:27:08','2021-09-10 15:00:15','2021-09-10 14:59:36','39,234',1,0,NULL,NULL,NULL,'1',NULL,3,2,4,3,3,2,3,NULL,12,15,13,20,7,21,NULL,1,1,'msam@build.aau.dk',NULL,NULL,NULL,NULL,1,1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,1,0,NULL,NULL,NULL,NULL);
INSERT INTO answers3 VALUES(9,1293732,827284595,260660,0,0,0,1,0,1,1,0,0,0,1,0,0,1,0,0,0,0,0,0,'2021-09-10 15:34:04','2021-09-17 11:27:08','2021-09-10 15:34:42','2021-09-10 15:34:11','31,313',1,0,NULL,NULL,NULL,'1',NULL,2,3,2,3,4,3,3,NULL,8,2,2,2,3,13,NULL,1,1,'msam@build.aau.dk',NULL,NULL,NULL,NULL,1,1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,1,0,NULL,NULL,NULL,NULL);
INSERT INTO answers3 VALUES(10,1293732,827288819,260660,0,0,0,1,0,1,1,0,0,0,1,0,0,1,0,0,0,0,0,0,'2021-09-10 16:13:49','2021-09-17 11:27:08','2021-09-10 16:14:28','2021-09-10 16:13:55','32,646',1,0,NULL,NULL,NULL,'1',NULL,2,4,3,2,3,3,3,NULL,3,17,11,15,2,18,NULL,1,2,'msam@build.aau.dk',NULL,NULL,NULL,NULL,1,1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,1,0,NULL,NULL,NULL,NULL);
CREATE VIEW strategi_mailings
as
SELECT
    respondentid,
    julianday(datetime('now'))-julianday(closetime) as days_since_done,
    email_strategi,
    strategi_mail_send_first,
    strategi_mail_send_second,
    l1.field_text as situation1_text,
    l2.field_text as situation2_text,
    l3.field_text as situation3_text,
    ls1.field_text as strategi1_text,
    ls2.field_text as strategi2_text,
    ls3.field_text as strategi3_text
from
    answers3 a
    LEFT JOIN labels l1 on (a.situation1 = l1.field_value and l1.field_name = 'situation1')
    LEFT JOIN labels l2 on (a.situation2 = l2.field_value and l2.field_name = 'situation2')
    LEFT JOIN labels l3 on (a.situation3 = l3.field_value and l3.field_name = 'situation3')
    LEFT JOIN labels ls1 on (a.strategi1 = ls1.field_value and ls1.field_name = 'strategi1')
    LEFT JOIN labels ls2 on (a.strategi2 = ls2.field_value and ls2.field_name = 'strategi2')
    LEFT JOIN labels ls3 on (a.strategi3 = ls3.field_value and ls3.field_name = 'strategi3')
where
    strategimail = 1 AND
    strategireminder = 1 AND
    (strategi_mail_send_first is null OR strategi_mail_send_second is null);
COMMIT;
