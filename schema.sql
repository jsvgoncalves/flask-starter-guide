drop table if exists users;
create table users (
  id INTEGER primary key AUTOINCREMENT,
  -- ENCRYPTED
  -- name TEXT NOT NULL,
  name TEXT NOT NULL,
  -- email TEXT NOT NULL,
  email TEXT NOT NULL
);
