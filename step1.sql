-- 新建一个数据库university
CREATE SCHEMA `university` DEFAULT CHARACTER SET utf8 ;

-- 使用该数据库
use university;

-- 分别建立department，student，exam三个表格，注意各个key的属性

-- 主键为dept_name
CREATE TABLE `university`.`department` (
  `dept_name` VARCHAR(45) NOT NULL,
  `building` VARCHAR(45) NULL,
  `budget` INT UNSIGNED NULL,
  PRIMARY KEY (`dept_name`));

-- 主键为ID,外码为dept_name
CREATE TABLE `university`.`student` (
  `ID` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `sex` CHAR(1) NULL,
  `age` INT UNSIGNED NULL,
  `emotion_state` VARCHAR(45) NULL,
  `dept_name` VARCHAR(45) NULL,
  PRIMARY KEY (`ID`),
  INDEX `fk_student_1_idx` (`dept_name` ASC),
  CONSTRAINT `fk_student_1`
    FOREIGN KEY (`dept_name`)
    REFERENCES `university`.`department` (`dept_name`)
  ON DELETE SET NULL
  ON UPDATE CASCADE);
  
  -- 主键为student_ID和exam_name,外码为student_ID
  CREATE TABLE `university`.`exam` (
  `student_ID` INT UNSIGNED NOT NULL,
  `exam_name` VARCHAR(45) NOT NULL,
  `grade` INT UNSIGNED NULL,
  PRIMARY KEY (`student_ID`, `exam_name`),
  CONSTRAINT `fk_exam_1`
    FOREIGN KEY (`student_ID`)
    REFERENCES `university`.`student` (`ID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE);

select * from department;
select * from student;
select * from exam;