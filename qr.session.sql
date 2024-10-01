CREATE TABLE qrs (
    id VARCHAR(50) NOT NULL PRIMARY KEY UNIQUE
);

-- @block
SELECT * FROM qrs;

-- @block
INSERT INTO qrs (id)
VALUES
    (1)
