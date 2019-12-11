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
    EXECUTE format('CREATE TABLE IF NOT EXISTS '|| tblName1 ||' ( '|| ID ||' SERIAL PRIMARY KEY, '|| ShortName ||' varchar(30), '|| Age ||' integer, '|| SchoolID ||' integer);');
    EXECUTE format('CREATE TABLE IF NOT EXISTS '|| tblName2 ||' ( '|| ID ||' SERIAL PRIMARY KEY, '|| SchoolID ||' integer, '|| SchoolName ||' varchar(30), '|| NumbOfPupils ||' integer, '|| Place ||' varchar(30));');
    EXECUTE format('CREATE TABLE IF NOT EXISTS '|| tblName3 ||' ( '|| ID ||' SERIAL PRIMARY KEY, '|| MeetingName ||' varchar(128), '|| MeetingDate ||' date, '|| Place ||' varchar(64));');
    EXECUTE format('CREATE TABLE IF NOT EXISTS '|| tblName4 ||' ( '|| ID ||' SERIAL PRIMARY KEY, '|| VisiterID ||' integer, '|| MeetingID ||' integer);');
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
        INSERT INTO Visit (VisiterID, MeetingID) VALUES (1, 2);
        INSERT INTO Visit (VisiterID, MeetingID) VALUES (2, 3);
        INSERT INTO Visit (VisiterID, MeetingID) VALUES (3, 1);
        INSERT INTO Visit (VisiterID, MeetingID) VALUES (4, 2);
        INSERT INTO Visit (VisiterID, MeetingID) VALUES (5, 3);
        INSERT INTO Visit (VisiterID, MeetingID) VALUES (6, 1);
        INSERT INTO Visit (VisiterID, MeetingID) VALUES (7, 2);
        INSERT INTO Visit (VisiterID, MeetingID) VALUES (8, 3);
        RAISE NOTICE 'Table (%) filled', tblName4;
    END IF;
END;
$$;


--call fillAllTables()
CREATE OR REPLACE PROCEDURE fillAllTables()
LANGUAGE plpgsql
AS $$
BEGIN
    CALL fillTable('School');
    CALL fillTable('Child');
    CALL fillTable('Meeting');
    CALL fillTable('Visit');

END;
$$;


-- return id by name meeting name and by name school

CREATE OR REPLACE FUNCTION getIdMeetingName(ikey text)
  returns integer
  AS
$func$
DECLARE 
  ret_id integer;
BEGIN
    SELECT Meeting.ID INTO ret_id FROM Meeting WHERE Meeting.Meetingname = ikey; 
    return ret_id; --< return this variable
END
$func$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION getIdSchoolName(ikey text)
  returns integer
  AS
$func$
DECLARE 
  ret_id integer;
BEGIN
    SELECT School.SchoolID INTO ret_id FROM School WHERE School.SchoolName = ikey; 
    return ret_id; --< return this variable
END
$func$ LANGUAGE plpgsql;

-- insertIntoBase(ID, 'ShortName', Age, SchoolID);
CREATE OR REPLACE PROCEDURE insertIntoBase(IN ShortName_ varchar(30), IN Age_ integer, IN SchoolName_ varchar(30), IN MeetingName_ varchar(128))
LANGUAGE plpgsql
AS $$
DECLARE
    SchoolID_   integer;
    MeetingID_  integer;
    ID_      integer;
BEGIN
    SchoolID_ = getIdMeetingName(MeetingName_);
    MeetingID_ = getIdSchoolName(SchoolName_);
    -- RAISE NOTICE '';
    INSERT INTO Child(ShortName, Age, SchoolId) VALUES (ShortName_, Age_, SchoolID_);
    ID_ := currval('child_id_seq');
    INSERT INTO Visit(VisiterID, MeetingID) VALUES (ID_, MeetingID_);
END;
$$;

-- select clearTables('{tablename_1, tablename_2, ... , tablename_n}');
CREATE OR REPLACE FUNCTION clearTables(tablenames text[]) RETURNS int AS
$func$
DECLARE
    tablename text;
BEGIN
    FOREACH tablename IN ARRAY tablenames LOOP
        EXECUTE FORMAT('DELETE FROM %s', tablename);
        EXECUTE FORMAT('ALTER SEQUENCE %s_id_seq restart with 1', tablename);
    END LOOP;
    RETURN 1;
END
$func$ LANGUAGE plpgsql;

--select dropTables('{tablename_1, tablename_2, ... , tablename_n}')
CREATE OR REPLACE FUNCTION dropTables(tablenames text[]) RETURNS int AS
$func$
DECLARE
    tablename text;
BEGIN
    FOREACH tablename IN ARRAY tablenames LOOP
        EXECUTE FORMAT('DROP TABLE %s', tablename);
    END LOOP;
    RETURN 1;
END
$func$ LANGUAGE plpgsql;

--call findRebel(name)
CREATE OR REPLACE PROCEDURE findRebel(INOUT name VARCHAR(1000))
LANGUAGE plpgsql
AS $$
declare temp VARCHAR(100);
BEGIN
  select ID INTO temp FROM Child WHERE  ShortName Like  name;
	name=temp;
END;
$$;

--call getRebelDataByID(rebel_data)
CREATE OR REPLACE PROCEDURE getRebelDataByID(INOUT rebel_data VARCHAR(200))
LANGUAGE plpgsql
AS $$
declare temp_id int;
declare name VARCHAR(100);
declare rebel_age int;
declare temp_shool VARCHAR(100);
declare shoolplace VARCHAR(100);
declare last_meeting_name VARCHAR(100);

BEGIN
  temp_id=CAST (rebel_data AS INTEGER);
  select ShortName INTO name FROM Child WHERE  Child.ID = temp_id;
  select age INTO rebel_age FROM Child WHERE  Child.ID = temp_id;
  select SchoolName INTO temp_shool FROM Child,School WHERE  Child.ID = temp_id AND Child.SchoolID=School.SchoolID;
  select place INTO shoolplace FROM Child,School WHERE  Child.ID = temp_id AND Child.SchoolID=School.SchoolID;
  select meetingname INTO last_meeting_name FROM Meeting,Visit WHERE  Visit.VisiterID = temp_id AND Visit.MeetingID = Meeting.ID  ORDER BY Meeting.MeetingDate desc limit 1;
	rebel_data=name || ' | ' || rebel_age || ' | ' || temp_shool || ' | ' || shoolplace || ' | ' || last_meeting_name;
END;
$$;

--call dropAllTables()
CREATE OR REPLACE PROCEDURE dropAllTables()
LANGUAGE plpgsql
AS $$
BEGIN
    PERFORM dropTables('{Visit, Child, Meeting, School}');
END;
$$;

--select deleteFromBaseById(ID)
CREATE OR REPLACE PROCEDURE deleteFromBaseById(IN ID_ integer)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM Child WHERE Child.id = ID_;
    DELETE FROM Visit WHERE Visit.VisiterID = ID_; 
END;
$$;
