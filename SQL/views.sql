-------------------------------------------------
---------------------views-----------------------

--view for auto comleter
CREATE OR REPLACE VIEW v_childNames AS SELECT ShortName FROM Child;

--view for  QComboBox
CREATE OR REPLACE VIEW v_meetingNames AS SELECT MeetingName FROM Meeting;

--view for  QComboBox
CREATE OR REPLACE VIEW v_schoolNames AS SELECT SchoolName FROM School;

--view for TableLayout
CREATE OR REPLACE VIEW v_full_info AS
  SELECT Child.id,ShortName as Name, age as Age, SchoolName as Shool, School.place as SchoolPlace, MeetingName, MeetingDate
  FROM Child, School, Meeting, Visit
  WHERE Child.SchoolID = School.SchoolID and Visit.VisiterID = Child.id and Visit.MeetingID = Meeting.ID;

--view School
CREATE OR REPLACE VIEW v_school AS SELECT * FROM School;

--view Meeting
CREATE OR REPLACE VIEW v_meeting AS SELECT * FROM Meeting;
