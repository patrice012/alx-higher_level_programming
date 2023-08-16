-- Lists all cities of CA in the database hbtn_0d_usa.
-- Results are ordered by ascending cities.id.
SELECT `cities.id`, `cities.name`
	FROM `cities`, `states`
	WHERE `cities.state_id` = `states.id`
  		AND `states.name` = 'California'
	ORDER BY `cities.id` ASC;

