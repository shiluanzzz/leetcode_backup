
select a.id
from weather a JOIN weather b
where dateDiff(a.recorddate,b.recorddata) = 1 and a.temperature > b.temperature