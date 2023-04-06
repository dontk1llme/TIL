CREATE TABLE zoo (
  name TEXT NOT NULL,
  eat TEXT NOT NULL,
  weight INT NOT NULL,
  height INT,
  age INT
);

-- 1) 
INSERT INTO zoo VALUES 
(5, 180, 210, 'gorilla', 'omnivore');
-- 순서가 잘못되어서 TEXT, INT등의 format 형식에 맞지 않음
----------------------------------------------------------------------------------
-- 2)
INSERT INTO zoo (rowid, name, eat, weight, age) VALUES
(10,'dolphin', 'carnivore', 210, 3),
(10, 'alligator', 'carnivore', 250, 50);
-- 순서가 잘못되어서 TEXT, INT등의 format 형식에 맞지 않음
----------------------------------------------------------------------------------
-- 3)
INSERT INTO zoo (name, eat, age) VALUES
('dolphin', 'carnivore', 3);
-- weight가 not null인데 데이터를 안 줬음
----------------------------------------------------------------------------------
-- https://stackoverflow.com/questions/46749844/why-are-my-strings-accepted-into-int-values-in-sql-db
-- sqlite3는 관대한 아이라서 포맷이 틀렸어도 에러는 나지 않음. 
-- 정수로 캐스팅 가능하면 해서 넣어주고, 아니면 그냥 몰라 하고 넣어버림