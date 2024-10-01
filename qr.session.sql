CREATE TABLE qrs (
    id VARCHAR(50) NOT NULL PRIMARY KEY UNIQUE
);

-- @block
SELECT * FROM qrs;

-- @block
INSERT INTO qrs (id)
VALUES
    ("aAbBB");

-- @block
SELECT * FROM qrs WHERE BINARY id = "aAbBB";
