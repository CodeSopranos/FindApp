CREATE DATABASE NN;

-- создание процедуры
CREATE PROCEDURE createTable()
AS $$

    DECLARE tblName1 VARCHAR     := 'Child';
    DECLARE tblName2 VARCHAR     := 'Schools';
    DECLARE tblName3 VARCHAR     := 'Meetings';

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
    EXECUTE format('CREATE TABLE IF NOT EXISTS %I (
                    %I integer,
                    %I char(30), 
                    %I integer
                    );', tblName1, ID, ShortName, SchoolID);
    EXECUTE format('CREATE TABLE IF NOT EXISTS %I (
                    %I integer, 
                    %I integer,
                    %I varchar(30),
                    %I integer,
                    %I varchar(30)
                    );', tblName2, ID, SchoolID, SchoolName, NumbOfPupils, Place);

    EXECUTE format('CREATE TABLE IF NOT EXISTS %I (
                    %I integer, 
                    %I varchar(30),
                    %I varchar(30)
                    );', tblName3, ID, MeetingName, Place);

    RAISE NOTICE 'Table names (%, %, %)', tblName1, tblName2, tblName3;
END;
$$ LANGUAGE plpgsql;

-- call createTable();

DROP PROCEDURE createTable;
