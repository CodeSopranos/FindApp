CREATE DATABASE NN;
CREATE DATABASE SPb;
CREATE DATABASE Msc;

-- connectBase(name)
-- из процедуры нельзя коннектиться к дб,
-- предлагаю звать через PyQT

-- создание таблиц, пока бе Visited
CREATE PROCEDURE createTables()
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
    EXECUTE format('CREATE TABLE %I (%I SERIAL PRIMARY KEY, %I varchar(30), %I integer
                    );', tblName1, ID, ShortName, SchoolID);
    EXECUTE format('CREATE TABLE %I (%I SERIAL PRIMARY KEY, %I integer, %I varchar(30), %I integer, %I varchar(30)
                    );', tblName2, ID, SchoolID, SchoolName, NumbOfPupils, Place);

    EXECUTE format('CREATE TABLE %I (%I SERIAL PRIMARY KEY, %I varchar(30), %I date, %I varchar(30)
                    );', tblName3, ID, MeetingName, MeetingDate, Place);

    -- EXECUTE format('CREATE TABLE %I (%I SERIAL PRIMARY KEY, %I integer, %I integer 
    --                 );', tblName4, ID, VisiterID, MeetingID);

    RAISE NOTICE 'Table names (%, %, %)', tblName1, tblName2, tblName3;
END;
$$ LANGUAGE plpgsql;

-- Заполнение таблиц по имени [Child, School, Meeting] (Meeting пока нет)
CREATE PROCEDURE fillTable(IN tblName name)
AS $$

    DECLARE tblName1 VARCHAR     := 'Child';
    DECLARE tblName2 VARCHAR     := 'School';
    DECLARE tblName3 VARCHAR     := 'Meeting';

    DECLARE ID VARCHAR           := 'ID';
    DECLARE Age VARCHAR          := 'Age';
    DECLARE ShortName VARCHAR    := 'ShortName';
    DECLARE Phone VARCHAR        := 'Phone';
    DECLARE SchoolID VARCHAR     := 'SchoolID';
    DECLARE SchoolName VARCHAR   := 'SchoolName';
    DECLARE NumbOfPupils VARCHAR := 'NumbOfPupils';
    DECLARE Place VARCHAR        := 'Place';
    DECLARE MeetingName VARCHAR  := 'MeetingName';

BEGIN

    IF tblName = tblName1
    THEN
        INSERT INTO public."Child" ("ShortName", "SchoolID") VALUES ('Ivan Golunov', 3);
        INSERT INTO public."Child" ("ShortName", "SchoolID") VALUES ('Alexey Navalny', 3);
        INSERT INTO public."Child" ("ShortName", "SchoolID") VALUES ('Dmitriy Medvedev', 3);
        INSERT INTO public."Child" ("ShortName", "SchoolID") VALUES ('Michael Saakoshvili', 5);
        INSERT INTO public."Child" ("ShortName", "SchoolID") VALUES ('Vladimir Putin', 5);
        INSERT INTO public."Child" ("ShortName", "SchoolID") VALUES ('Vlad Ivanov', 88);
        INSERT INTO public."Child" ("ShortName", "SchoolID") VALUES ('Pasha Tekhnik', 288);
        INSERT INTO public."Child" ("ShortName", "SchoolID") VALUES ('Oxxxymiron', 288);
 
        RAISE NOTICE 'Table (%) filled', tblName1;
    END IF;
    
    IF tblName = tblName2
    -- SchoolID, SchoolName, NumbOfPupils, Place
    THEN
        INSERT INTO public."School" ("SchoolID", "SchoolName", "NumbOfPupils", "Place") VALUES (3, 'School of Oppositioners', 567, 'Rodionova, p.184');
        INSERT INTO public."School" ("SchoolID", "SchoolName", "NumbOfPupils", "Place") VALUES (5, 'Academy of US Government', 890, 'Lvovskaya, 1b');
        INSERT INTO public."School" ("SchoolID", "SchoolName", "NumbOfPupils", "Place") VALUES (88, 'Autozavod Harlem Shakers', 1000, 'metro Park of Culture');
        INSERT INTO public."School" ("SchoolID", "SchoolName", "NumbOfPupils", "Place") VALUES (288, 'Flying potatoes college', 228, 'Kremlin');

        RAISE NOTICE 'Table (%) filled', tblName2;
    END IF;

END;
$$ LANGUAGE plpgsql;

CREATE PROCEDURE dropTables()
AS $$
    DECLARE tblName1 VARCHAR     := 'Child';
    DECLARE tblName2 VARCHAR     := 'School';
    DECLARE tblName3 VARCHAR     := 'Meeting';
    DECLARE tblName4 VARCHAR     := 'Visit';
BEGIN 
    DROP TABLE public."Child", public."School", public."Meeting";
    RAISE NOTICE 'Table deleted (%, %, %)', tblName1, tblName2, tblName3;
END;
$$ LANGUAGE plpgsql;

-- DROP PROCEDURE createTable;
