use university;

-- 3-1把peoples表中school不是GDUFS的人全部找出来？（包括school为NULL的人）写出MySQL语句。
select * from peoples where school != 'GDUFS' or school is null;

-- 3-2.查找计算机系每次考试学生的平均成绩(最终显示学生姓名, 考试名称, 平均分)。
-- 不是很理解题目意思，所以做成两次操作，一是显示计算机系的学生姓名及对应的考试名称；二是显示计算机系的学生每次考试的考试名称及对应的平均成绩。
-- select name,exam_name from student,exam where student.dept_name = 'computer' and student.ID = exam.student_ID;
select exam_name,avg(grade) from student,exam where student.dept_name = 'computer' and student.ID = exam.student_ID group by exam_name ;

-- 3-3.查找女学霸（考试平均分达到80分或80分以上的女生的姓名, 分数）。
select name,avg(grade) from exam,student where student.ID = student_ID and student.sex = 'f' group by student_ID having avg(grade)>=80;

-- 3-4.找出人数最少的院系以及其年度预算。
-- 找不到解决count最少的函数，用了笨方法，不能解决有两个人数最少的院系的问题？？
select dept_name,budget from department where dept_name = (select dept_name from student group by dept_name order by count(dept_name)limit 0,1);

-- 3-5.计算机系改名了，改成计算机科学系（comp. sci.），写出mysql语句。
update department set dept_name = 'comp.sci.' where dept_name = 'computer';

-- 3-6.修改每个系的年度预算，给该系的每个学生发2000元奖金。（修改每个系的年度预算为 原预算+该系人数*2000）。
-- 这道题不会做，下面这条语句实现不了。不过思想应该没问题。
update department set budget = budget + 2000 * count(dept_name) in(
	      select count(dept_name),dept_name from student as T1 group by dept_name) where T1.dept_name = department.dept_name ;

-- 3-7.向department表中插入一条数据, dept_name属性的值为avg_budget, building为空, 年度预算为所有院系的年度预算平均值.
insert into department 
                      select "avg_budget",NULL,avg(budget) from department; 

-- 3-8. 删除计算机系中考试成绩平均分低于70的学生.
-- 下面的语句无法执行，需要解决（不能在一个表select完后更新同一个表的数据）的问题。
delete from student where student.ID in (select ID from exam,student where student.ID = student_ID and student.dept_name = 'comp.sci.' group by student_ID having avg(grade)<70);

-- 3-9.找出所有正在谈恋爱,但是学习成绩不佳(考试平均分低于75)的学生,强制将其情感状态改为单身.
-- 这道题同上道题的问题一样。
select name from student where student.emotion_state = 'loving' and student.ID in(select student_ID from exam group by student_ID having avg(grade)<75);
update student set emotion_state = 'single' where name in (select name from student where student.emotion_state = 'loving' and student.ID in(select student_ID from exam group by student_ID having avg(grade)<75))
