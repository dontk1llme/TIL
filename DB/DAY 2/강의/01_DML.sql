-- users table 생성
CREATE TABLE users (
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    country TEXT NOT NULL,
    phone TEXT NOT NULL,
    balance INTEGER NOT NULL
);

-- Grouping Data
-- 전체 유저의 평균 balance
SELECT avg(balance) FROM users;
-- 모든 유저의 지역 조회
SELECT DISTINCT country FROM users;
-- 전라북도 평균
SELECT country, avg(balance) FROM users WHERE country="전라북도";
-- 지역별 평균 balance + 정렬
SELECT country, avg(balance) FROM users GROUP BY country ORDER BY avg(balance) DESC;
-- 지역별로 몇 명 사는지
SELECT country, COUNT(*) FROM users GROUP BY country;
-- 성씨 몇 명씩 있는지 + as 임시 칼럼명 + 정렬
SELECT last_name, COUNT(*) AS number_of_name_ FROM users GROUP BY last_name ORDER BY COUNT(*) DESC;
-- 

-- -----------------------------------------------------------

--  Changing Data
CREATE TABLE classmates (
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    address TEXT NOT NULL
);

-- insert
INSERT INTO classmates (name, age, address)
VALUES ('홍길동', 23, '서울');

INSERT INTO classmates
VALUES
    ('김철수',30,'경기'),
    ('이영미',31,'강원'),
    ('박진성',26,'전라'),
    ('최지수',12,'충청'),
    ('정요한',28,'경상');

-- update
UPDATE classmates
SET name='김철수한무두루미',
    address = '제주도'
WHERE rowid=2;

-- delete
DELETE FROM classmates WHERE rowid=5;
DELETE FROM classmates WHERE name LIKE '%영%';
DELETE FROM classmates;
