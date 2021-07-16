#MySQL
CREATE TABLE Teacher (
    t_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    gender Bit NOT NULL,
    subject VARCHAR(30)

);

CREATE TABLE Pupil(
    p_id = INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    gender Bit NOT NULL,
    class VARCHAR(25)
);


#თუ გვინდა, რომ არსებული ორი table დავაკავშიროთ, ამისთვის
#გვჭირდება მესამე table, რომელიც იქნება დაკავშირებული წინა ორ table-თან აიდებით შემდეგნაირად:

CREATE TABLE TeacherToPupil(
    pupil_id INT NOT NULL FOREIGN KEY REFERENCES Pupil(p_id),
    teacher_id INT NOT NULL FOREIGN KEY REFERENCES Teacher(teacher_id),

);

SELECT * FROM Teacher INNER JOIN TeacherToPupil
ON Teacher.t_id = TeacherToPupil.teacher_id
INNER JOIN Pupil ON Pupil.p_id = TeacherToPupil.pupil_id
WHERE Pupil.first_name = 'Giorgi'
