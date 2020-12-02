-- script lists all bands with Glam rock as their main style, ranked by their longevity
-- descending order
select band_name, IFNULL(split,2020)-formed lifespan from metal_bands where style like '%Glam rock%'
order by 2 DESC;

