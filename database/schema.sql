/* CREATE DATABASE redacted_bot; */

/* Create Tables */
DROP TABLE IF EXISTS users CASCADE;
CREATE TABLE users (
    discord_id BIGINT NOT NULL,
    PRIMARY KEY (discord_id)
);

/* Temporary = true (purge end of day) */
DROP TABLE IF EXISTS user_characters CASCADE;
CREATE TABLE user_characters (
    discord_id BIGINT NOT NULL,
    character_name VARCHAR(50) NOT NULL,
    main BOOLEAN NOT NULL,
    temporary BOOLEAN NOT NULL,
    PRIMARY KEY (discord_id, character_name),
    FOREIGN KEY (discord_id) REFERENCES users (discord_id) ON UPDATE CASCADE
);