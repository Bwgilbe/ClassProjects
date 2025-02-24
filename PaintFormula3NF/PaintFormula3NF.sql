-- 5a
SELECT c.ColorName,
       GROUP_CONCAT(ct.ColorantName ORDER BY ct.ColorantName DESC SEPARATOR ',') AS Colorants
FROM Color c
NATURAL JOIN Formula f
NATURAL JOIN Colorant ct
GROUP BY c.ColorName
ORDER BY c.ColorName ASC;

-- 5b
SELECT ct.ColorantName,
       COUNT(*) AS Colorant_Count
FROM Formula f
NATURAL JOIN Colorant ct
GROUP BY ct.ColorantName
ORDER BY ct.ColorantName ASC;

-- 5c
SELECT ColorantName
FROM Colorant
WHERE ColorantName LIKE '%Oxide%'
ORDER BY ColorantName ASC;

-- 5d
SELECT DISTINCT 
    c.ColorName
FROM Color c
WHERE EXISTS (
    SELECT 1
    FROM Formula f
    NATURAL JOIN Colorant ct
    WHERE c.ColorCode = f.ColorCode
      AND ct.ColorantName = 'Magenta'
)
AND NOT EXISTS (
    SELECT 1
    FROM Formula f
    NATURAL JOIN Colorant ct
    WHERE c.ColorCode = f.ColorCode
      AND ct.ColorantName = 'Magenta'
      AND f.Oz <> 0
)
ORDER BY c.ColorName ASC;
-- 5e
SELECT ct.ColorantName,
       SUM(f.Oz + f.Shot/48.0 + f.HalfShot/96.0) AS Total_Ounces
FROM Formula f
NATURAL JOIN Colorant ct
GROUP BY ct.ColorantName
ORDER BY ct.ColorantName ASC;

-- 5f
SELECT ct.ColorantName,
       GROUP_CONCAT(c.ColorName ORDER BY c.ColorName ASC SEPARATOR ',') AS Paints
FROM Formula f
NATURAL JOIN Colorant ct
NATURAL JOIN Color c
GROUP BY ct.ColorantName
ORDER BY ct.ColorantName ASC;
