-- Script to create evoting tables:
--    candidate ('President', 'Governor','Senetor', 'MP')
--    voter
--    vote

CREATE TABLE IF NOT EXISTS evoting.voter (
  id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  first_name VARCHAR(100) NOT NULL,
  middle_name VARCHAR(100),
  last_name VARCHAR(100) NOT NULL,
  id_number VARCHAR(100) NOT NULL UNIQUE,
  gender VARCHAR(10) NOT NULL,
  county VARCHAR(100) NOT NULL,
  country VARCHAR(100) NOT NULL,
  constituency VARCHAR(100) NOT NULL,
  ward VARCHAR(100) NOT NULL,
  poling_station VARCHAR(100) NOT NULL,
  create_on datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS evoting.candidate (
  id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  candidate_id VARCHAR(200) NOT NULL,
  electoral_position VARCHAR(200) NOT NULL,
  political_party VARCHAR(256) NOT NULL,
  cleared_on datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (candidate_id) REFERENCES evoting.voter(id_number)
);

CREATE TABLE IF NOT EXISTS evoting.vote (
  id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  vote_id VARCHAR(200) NOT NULL,
  president VARCHAR(100),
  governor VARCHAR(100),
  senetor VARCHAR(100),
  member_of_parliament VARCHAR(100),
  voted_on datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (vote_id) REFERENCES evoting.voter(id_number)
);
