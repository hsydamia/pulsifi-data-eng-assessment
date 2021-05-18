SELECT p.name, p.gender, a.action_type as last_action, pa.created_at as last_action_time
FROM profile p
LEFT JOIN profile_action pa ON p.profile_id = pa.profile_id
INNER JOIN (
  SELECT profile_id, MAX(created_at) AS max_time
  FROM profile_action
  GROUP BY profile_id
) pat ON pa.profile_id = pat.profile_id AND pa.created_at = max_time
LEFT JOIN action a ON pa.action_id = a.action_id