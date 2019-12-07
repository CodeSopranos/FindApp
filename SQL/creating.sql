CREATE DATABASE NN;
CREATE DATABASE SPb;
CREATE DATABASE Msc;

-- connectBase(name)
-- из процедуры нельзя коннектиться к дб,
-- предлагаю звать через PyQT

-- создание таблиц, пока бе Visited
CREATE OR REPLACE PROCEDURE createTables()
LANGUAGE plpgsql
AS $$

    DECLARE tblName1 VARCHAR     := 'Child';
    DECLARE tblName2 VARCHAR     := 'School';
    DECLARE tblName3 VARCHAR     := 'Meeting';
    DECLARE tblName4 VARCHAR     := 'Visit';

    DECLARE ID VARCHAR             := 'ID';
    DECLARE Age VARCHAR            := 'Age';
    DECLARE ShortName VARCHAR      := 'ShortName';
    DECLARE Phone VARCHAR          := 'Phone';
    DECLARE SchoolID VARCHAR       := 'SchoolID';
    DECLARE SchoolName VARCHAR     := 'SchoolName';
    DECLARE NumbOfPupils VARCHAR   := 'NumbOfPupils';
    DECLARE Place VARCHAR          := 'Place';
    DECLARE MeetingName VARCHAR    := 'MeetingName';
    DECLARE VisiterID   VARCHAR    := 'VisiterID';
    DECLARE MeetingID   VARCHAR    := 'MeetingID';
    DECLARE MeetingDate   VARCHAR  := 'MeetingDate';

BEGIN
    EXECUTE format('CREATE TEMP TABLE '|| tblName1 ||' ( '|| ID ||' SERIAL PRIMARY KEY, '|| ShortName ||' varchar(30), '|| Age ||' integer, '|| SchoolID ||' integer);');
    EXECUTE format('CREATE TEMP TABLE '|| tblName2 ||' ( '|| ID ||' SERIAL PRIMARY KEY, '|| SchoolID ||' integer, '|| SchoolName ||' varchar(30), '|| NumbOfPupils ||' integer, '|| Place ||' varchar(30));');
    EXECUTE format('CREATE TEMP TABLE '|| tblName3 ||' ( '|| ID ||' SERIAL PRIMARY KEY, '|| MeetingName ||' varchar(128), '|| MeetingDate ||' date, '|| Place ||' varchar(64));');
    EXECUTE format('CREATE TEMP TABLE '|| tblName4 ||' ( '|| ID ||' SERIAL PRIMARY KEY, '|| VisiterID ||' integer, '|| MeetingID ||' integer);');
    RAISE NOTICE '(%, %, %, %) created', tblName1, tblName2, tblName3, tblName4;
END;
$$;

-- Заполнение таблиц по имени [Child, School, Meeting] (Meeting пока нет)
CREATE OR REPLACE PROCEDURE fillTable(IN tblName name)
LANGUAGE plpgsql
AS $$
    DECLARE tblName1 VARCHAR     := 'Child';
    DECLARE tblName2 VARCHAR     := 'School';
    DECLARE tblName3 VARCHAR     := 'Meeting';
    DECLARE tblName4 VARCHAR     := 'Visit';

BEGIN
    -- ShortName, Age, SchoolID
    IF tblName = tblName1 THEN
        INSERT INTO Child (ShortName,Age,SchoolID) VALUES ('Ivan Golunov', 33, 3);
        INSERT INTO Child (ShortName,Age,SchoolID) VALUES ('Alexey Navalny', 42, 3);
        INSERT INTO Child (ShortName,Age,SchoolID) VALUES ('Dmitriy Medvedev', 51, 3);
        INSERT INTO Child (ShortName,Age,SchoolID) VALUES ('Michael Saakoshvili', 60, 5);
        INSERT INTO Child (ShortName,Age,SchoolID) VALUES ('Vladimir Putin', 999, 5);
        INSERT INTO Child (ShortName,Age,SchoolID) VALUES ('Vlad Ivanov', 18, 88);
        INSERT INTO Child (ShortName,Age,SchoolID) VALUES ('Pasha Tekhnik', 15, 288);
        INSERT INTO Child (ShortName,Age,SchoolID) VALUES ('Oxxxymiron', 12, 288);
        RAISE NOTICE 'Table (%) filled', tblName1;
    END IF;

    IF tblName = tblName2 THEN
    -- SchoolID, SchoolName, NumbOfPupils, Place
        INSERT INTO School (SchoolID, SchoolName, NumbOfPupils, Place) VALUES (3,  'School of Oppositioners', 567, 'Rodionova, p.184');
        INSERT INTO School (SchoolID, SchoolName, NumbOfPupils, Place) VALUES (5,  'Academy of US Government', 890, 'Lvovskaya, 1b');
        INSERT INTO School (SchoolID, SchoolName, NumbOfPupils, Place) VALUES (88, 'Autozavod Harlem Shakers', 1000, 'metro Park of Culture');
        INSERT INTO School (SchoolID, SchoolName, NumbOfPupils, Place) VALUES (288,'Flying potatoes college', 228, 'Kremlin');
        RAISE NOTICE 'Table (%) filled', tblName2;
    END IF;

    IF tblName = tblName3 THEN
    -- MeetingName, MeetingDate, Place
        INSERT INTO Meeting (MeetingName, MeetingDate, Place) VALUES ('Cancelation of 4. art of Constitution', 'February-4-1990' ,'Taganka');
        INSERT INTO Meeting (MeetingName, MeetingDate, Place) VALUES ('Freedom for Golunov','August-31-2019', 'Saharova dst.');
        INSERT INTO Meeting (MeetingName, MeetingDate, Place) VALUES ('Bolotnaya','May-6-2012','Bolotnaya square');
        RAISE NOTICE 'Table (%) filled', tblName3;
    END IF;

    IF tblName = tblName4 THEN
    --  VisiterID, MeetingID, MeetingDate, Place
        INSERT INTO Visit (VisiterID, MeetingID) VALUES (9, 2);
        INSERT INTO Visit (VisiterID, MeetingID) VALUES (10, 3);
        INSERT INTO Visit (VisiterID, MeetingID) VALUES (11, 1);
        INSERT INTO Visit (VisiterID, MeetingID) VALUES (12, 2);
        INSERT INTO Visit (VisiterID, MeetingID) VALUES (13, 3);
        INSERT INTO Visit (VisiterID, MeetingID) VALUES (14, 1);
        INSERT INTO Visit (VisiterID, MeetingID) VALUES (15, 2);
        INSERT INTO Visit (VisiterID, MeetingID) VALUES (16, 3);
        RAISE NOTICE 'Table (%) filled', tblName4;
    END IF;
END;
$$;

CREATE OR REPLACE PROCEDURE dropTables()
LANGUAGE plpgsql
AS $$
    DECLARE tblName1 VARCHAR     := 'Child';
    DECLARE tblName2 VARCHAR     := 'School';
    DECLARE tblName3 VARCHAR     := 'Meeting';
    DECLARE tblName4 VARCHAR     := 'Visit';
BEGIN
    DROP TABLE child, school, meeting, visit;
    RAISE NOTICE 'Table deleted (%, %, %, %)', tblName1, tblName2, tblName3, tblName4;
END;
$$;
