-- script to get total fans by origin country
-- descending order
select origin, sum(fans) nb_fans from metal_bands
group by origin
order by 2 DESC;
