-- Total Sales
SELECT SUM(Sales) AS Total_Sales
FROM sales;

-- Sales by Category
SELECT Category, SUM(Sales) AS Category_Sales
FROM sales
GROUP BY Category;

-- Profit by Region
SELECT Region, SUM(Profit) AS Region_Profit
FROM sales
GROUP BY Region;

-- Top 5 Products
SELECT `Product Name`, SUM(Sales) AS Total_Sales
FROM sales
GROUP BY `Product Name`
ORDER BY Total_Sales DESC
LIMIT 5;

-- Sales by Segment
SELECT Segment, SUM(Sales) AS Segment_Sales
FROM sales
GROUP BY Segment;
