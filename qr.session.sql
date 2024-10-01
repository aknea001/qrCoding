CREATE TABLE qrs (
    id VARCHAR(50) NOT NULL PRIMARY KEY UNIQUE
);

-- @block
SELECT * FROM qrs
WHERE expiration IS NOT NULL
ORDER BY expiration ASC;

-- @block
INSERT INTO qrs (id)
VALUES
    ("aAbBB");

-- @block
SELECT * FROM qrs WHERE BINARY id = "aAbBB";

-- @block
SET GLOBAL event_scheduler = ON;

-- @block
ALTER TABLE qrs
ADD COLUMN expiration DATETIME;

-- @block
    CREATE EVENT expire
    ON SCHEDULE EVERY 1 HOUR
    DO
    BEGIN
        DELETE FROM qrs
        WHERE expiration <= CURTIME();
    END

-- @block
INSERT INTO qrs (id, expiration) VALUES ("TEST2", DATE_ADD(NOW(), INTERVAL 0.1 HOUR));

-