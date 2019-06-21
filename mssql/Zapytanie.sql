SELECT 
	d.id as 'ID',  
	d.firstName as 'Imię',
	d.lastName as 'Nazwisko',
	d.birthDate  'Data urodzenia', 
	sum(m.budget) as 'Suma budżetów filmów',
	avg(m.rating) as 'Średnia ocena filmów'
FROM Director d INNER JOIN Movie m
ON (m.Director = d.id)
GROUP BY d.id, d.firstName, d.lastName, d.birthDate
HAVING sum(m.budget) > 100000
ORDER BY 'Suma budżetów filmów'