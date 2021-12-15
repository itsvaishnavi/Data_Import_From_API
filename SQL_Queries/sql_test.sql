-- How many total messages are being sent every day?
SELECT CAST(createdAt AS DATE) as 'Date', COUNT(id) as NumOfMessagesSent
FROM message_table
GROUP BY CAST(createdAt AS DATE)

-- Are there any users that did not receive any message?
SELECT u.id as UserIdNotReceivedAnyMessage FROM users u where u.id NOT in 
(SELECT distinct m.receiver_id FROM message_table m)

-- How many active subscriptions do we have today?
SELECT CAST( GETDATE() AS Date )AS 'Current Date',COUNT(*) As 'Active Subscriptions' FROM SUBSCRIPTIONS
WHERE CAST( GETDATE() AS Date ) >= CAST(startDate as Date) 
AND CAST( GETDATE() AS Date ) <= CAST(endDate as Date)
AND subscription_status = 'Active'

-- How much is the average price ticket (sum amount subscriptions / count subscriptions) breakdown by year/month (format YYYY-MM)?
SELECT CAST(YEAR(endDate) AS VARCHAR(4)) + '-' + CAST(MONTH(endDate) AS VARCHAR(2)) AS 'YYYY-MM', 
CAST(SUM(amount) AS float)/CAST(COUNT(*) AS float) AS 'AVG PRICE TICKET' FROM SUBSCRIPTIONS
GROUP BY CAST(YEAR(endDate) AS VARCHAR(4)) + '-' + CAST(MONTH(endDate) AS VARCHAR(2))