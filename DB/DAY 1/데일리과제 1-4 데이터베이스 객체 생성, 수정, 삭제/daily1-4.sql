-- 1. 테이블 생성
-- CREATE TABLE users(
--     name TEXT NOT NULL,
--     phoneNumber TEXT NOT NULL,
--     email TEXT NOT NULL UNIQUE,
--     age INTEGER,
--     gender TEXT,
--     address TEXT NOT NULL DEFAULT='no address'
-- );
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

-- 3. users 테이블에서 이름, 나이, 계좌 잔고를 나이가 어린순으로, 만약 같은 나이라면 계좌 잔고가 많은 순으로 정렬해서 조회
SELECT first_name, age, balance FROM users
ORDER BY age, balance DESC;
-- age 오름차 정렬 후 balance 내림차 정렬

