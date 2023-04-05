CREATE TABLE zoo (
  name TEXT NOT NULL,
  eat TEXT NOT NULL,
  weight INT NOT NULL,
  height INT,
  age INT
);

INSERT INTO zoo VALUES 
('gorilla', 'omnivore', 215, 180, 5),
('tiger', 'carnivore', 220, 115, 3),
('elephant', 'herbivore', 3800, 280, 10),
('dog', 'omnivore', 8, 20, 1),
('panda', 'herbivore', 80, 90, 2),
('pig', 'omnivore', 70, 45, 5);

BEGIN;
  DELETE FROM zoo
  WHERE weight < 100; 
  --  몸무게 100보다 적은 애 삭제
ROLLBACK;
-- commit 이전의 insert, update, delete 취소
BEGIN;
  DELETE FROM zoo
  WHERE eat = 'omnivore';
  --  omnivore 먹는 애 삭제
COMMIT;
--  적용 및 영구 저장

SELECT COUNT(*)
FROM zoo;
-- count(*): 3 출력됨
