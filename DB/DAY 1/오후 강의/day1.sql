-- 1. 테이블 생성

CREATE TABLE users(
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    country TEXT NOT NULL,
    phone TEXT NOT NULL,
    balance INTEGER NOT NULL
);


-- 2. users.csv 파일 users 테이블에 가져오기
-- bash에다가
-- sqlite3 daily1-4.sqlite3
-- sqlite> .mode csv
-- sqlite> .import users.csv users


ALTER TABLE users ADD COLUMN test TEXT;
ALTER TABLE users DROP COLUMN test;
-- DROP 안 되면 세팅 덜한 거 . . .
-- 확장 프로그램 문제 -> 그냥 터미널에서 하세요...


-- 3. users 테이블에서 이름, 나이, 계좌 잔고를 나이가 어린순으로, 만약 같은 나이라면 계좌 잔고가 많은 순으로 정렬해서 조회
SELECT first_name, age, balance FROM users
ORDER BY age, balance DESC;
-- age 오름차 정렬 후 balance 내림차 정렬


-- 강의 ///////////////////////////////////

SELECT * FROM users;
SELECT rowid, first_name FROM users; 
SELECT first_name, age FROM users ORDER BY age;
SELECT first_name, age FROM users ORDER BY age DESC;

SELECT country FROM users;
SELECT DISTINCT country FROM users FROM users ORDER BY country;
SELECT DISTINCT first_name, country FROM users ORDER BY country OREDER BY country;

SELECT first_name, age, balance FROM users WHERE age>=30 ORDER BY balance DESC;
SELECT first_name, age, balance FROM users WHERE age>=30 AND balance>500000 ORDER BY balance DESC;

SELECT first_name, last_name FROM users WHERE first_name LIKE '%호%';
SELECT first_name, last_name FROM users WHERE first_name LIKE '%준';
SELECT first_name, age FROM users WHERE age LIKE '2_';
SELECT first_name, phone FROM users WHERE phone LIKE '%-51__-%';

SELECT first_name, country FROM users WHERE country IN ('경기도', '강원도');
SELECT first_name, country FROM users WHERE country NOT IN ('경기도', '강원도');

SELECT first_name, age FROM users WHERE age BETWEEN 20 AND 30;
SELECT first_name, age FROM users WHERE age NOT BETWEEN 20 AND 30;

SELECT first_name, age FROM users ORDER BY age LIMIT 5;
SELECT first_name, balance FROM users ORDER BY balance DESC LIMIT 10;

SELECT rowid, first_name FROM users LIMIT 10 OFFSET 10;