
-- Sample data for local testing only (Do NOT submit this)
USE CECSProjecta0yada05;

INSERT INTO Users VALUES
(1, 'Aaditya', 'Yadav', 'aaditya@example.com'),
(2, 'Jane', 'Doe', 'jane@example.com');

INSERT INTO Tasks (taskId, Name, DueDate, UserId)
VALUES
(101, 'Test Task', DATE_ADD(CURDATE(), INTERVAL 3 DAY), 1),
(102, 'Project Work', DATE_ADD(CURDATE(), INTERVAL 5 DAY), 1);
