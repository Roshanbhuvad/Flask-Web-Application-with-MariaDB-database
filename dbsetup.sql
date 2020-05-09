DROP DATABASE IF EXISTS `class`;
CREATE DATABASE
IF NOT EXISTS `class`;
USE `class`;
CREATE TABLE `student`
(
`roll_no` int
(20) NOT NULL AUTO_INCREMENT,
`first_name` varchar
(255) UNIQUE NOT NULL,
`last_name` varchar
(255) UNIQUE NOT NULL,
`email` varchar
(255) NOT NULL,
PRIMARY KEY
(`roll_no`)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;



/*INSERT INTO `student` (`
roll_no
`,`first_name
` ,`last_name`, `email` ) VALUES
(1, 1, 'roshan', 'bhuvad', 'roshanbhuvad15@gmail.com');*/


ALTER TABLE `student`
ADD PRIMARY KEY
(`id`);

ALTER TABLE `student`
MODIFY `id` int
(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;