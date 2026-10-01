---
{"dg-publish":true,"permalink":"/we-don-t-actually-know-where-british-agriculture-can-go/","tags":["UK_Agriculture","Land_Use","Food_Security","Agricultural_Land_Classification","Grazing","Policy"],"created":"2026-06-24T17:02:32.000+01:00","updated":"2026-10-01T06:57:10.654+01:00","dg-note-properties":{"Note Type":"Own Work","tags":["UK_Agriculture","Land_Use","Food_Security","Agricultural_Land_Classification","Grazing","Policy"],"AI suggested tags":["Environment/Land","Bryant_Research/Project/CAWF_Food_Sec","Farming"]}}
---


# We Don't Actually Know Where British Agriculture Can Go

In debates about UK land use, people regularly claim that large amounts of British land is "only suitable for grazing." This claim rests on the Agricultural Land Classification (ALC) system, which is the only official framework for grading the quality of agricultural land in England and Wales. The problem is that the ALC system is riddled with limitations so severe that we honestly don't have a solid evidence base for making confident claims about what most British land can and cannot do. This note is a deep-dive into what those limitations are.

## What Is the ALC?

The ALC was devised and introduced by the Ministry of Agriculture, Fisheries and Food (MAFF, now DEFRA) in 1966. It classifies agricultural land in England and Wales into five grades based on the extent to which the land's physical and chemical characteristics impose long-term limitations on agricultural use. The criteria include climate (temperature, rainfall, aspect, exposure, frost risk), site factors (gradient, micro-relief, flood risk), and soil properties (depth, structure, texture, chemicals, stoniness). The full revised guidelines (1988) describe the methodology in detail.

Crucially, the ALC grades land based on its inherent physical properties, not on what it has been used for recently. A common misconception in advocacy circles is that land classified as "only fit for grazing" was classified that way because it was grazed for the last five years. That is incorrect. Grade 5 land is Grade 5 because the soil, climate, and topography are genuinely severe, not because of recent land use.

The grades, briefly:

- **Grade 1:** Excellent quality. No or very minor limitations. Can grow a very wide range of crops including demanding ones like top fruit, soft fruit, salad crops, and winter-harvested vegetables. Yields are high and consistent.
- **Grade 2:** Very good quality. Minor limitations affecting crop yield, cultivations, or harvesting. Wide crop range, but with some reduced flexibility for the most demanding crops.
- **Grade 3a:** Good quality. Moderate limitations, but still capable of consistently producing moderate-to-high yields of a moderate range of crops, or high yields of a narrower range. Grades 1, 2, and 3a together are classified as "Best and Most Versatile" (BMV) land and are given special protection in planning policy under the National Planning Policy Framework.
- **Grade 3b:** Moderate quality. Land capable of producing moderate yields of a narrow range of crops, or moderate yields of grass. Not classified as BMV.
- **Grade 4:** Poor quality. Severe limitations which significantly restrict the range of crops and/or level of yields. Mainly suited to grass, with occasional arable crops (e.g., cereals and forage crops) whose yields are variable. In moist climates, grass yields may be moderate to high but there may be difficulties in utilisation. This grade also includes very droughty arable land.
- **Grade 5:** Very poor quality. Very severe limitations which restrict use to permanent pasture or rough grazing, except for occasional pioneer forage crops. This is predominantly upland moorland, not "degraded" lowland. The word "degraded" would be misleading here: this is land that has always been physically limited by altitude, exposure, thin soils, steep slopes, and/or high rainfall.

Grade 3 (combined, without the 3a/3b subdivision) constitutes roughly half of all agricultural land in England and Wales.

## The Problems

### 1. The maps most people rely on are from the late 1960s and 1970s

After the ALC system was introduced in 1966, the whole of England and Wales was mapped from reconnaissance field surveys between 1967 and 1974. These "Provisional" maps were published at a scale of one inch to one mile and later reissued at 1:250,000 scale. They were explicitly described as "provisional" because the amount of fieldwork varied considerably across the country, and the grading was based mainly on reconnaissance-level ground observations supplemented by existing information. The intention was to refine, resurvey, and produce a final version.

That refinement never happened. The maps retained the "provisional" title and remained the only national-coverage ALC dataset for England. They are the default layer on DEFRA's MAGIC interactive map. These provisional maps are not sufficiently accurate for use in assessment of individual fields or development sites, and Natural England's own metadata says they should not be used other than as general guidance.

### 2. The climate data underpinning the system is even older

The ALC system relies on climate data collected between 1941 and 1980. CPRE's 2025 analysis flags that more up-to-date measurements of temperature and rainfall would likely show a dramatic reduction in the amount of high-grade agricultural land available. In other words, we may be overestimating the quality of our farmland because the climate has changed since the data was collected. See also [[The effects of climate change on UK agriculture\|The effects of climate change on UK agriculture]] for broader context on how climate shifts are altering UK agricultural viability.

Another CPRE study modelled the predicted change in ALC grade over time under UKCP18 climate projections and found that the proportion of BMV land (Grades 1-3a) could fall to a predicted 15.7% by 2050 under high emissions scenarios, driven by increasing drought risk in areas that currently have some of the best land.

Peatland soils are a particular concern. More than 40% of England's crops are grown on lowland peatland, where ALC assessments are more than 50 years old. Since then, these soils have significantly degraded due to drainage and intensive farming, often leaving less fertile mineral soils behind. [[Animal agro and soil health\|Animal agro and soil health]] covers the broader picture of how farming practices interact with soil degradation.

### 3. The provisional maps don't distinguish between Grade 3a and Grade 3b

This is arguably the single biggest practical problem with the system. The provisional maps predate the subdivision of Grade 3 into 3a and 3b, which was only introduced in 1976 and refined further in the 1988 guidelines. Since Grade 3 is roughly half of all agricultural land, this means we genuinely do not know at a national level whether that half is "good" (3a, BMV, can grow a decent range of crops) or "mediocre" (3b, mostly suited to grass and limited arable).

CPRE's Building on Our Food Security (2022) report found that the post-1988 detailed survey dataset covers only about 8% of rural England, and as a result they were only able to identify 3% of Grade 3 land as 3a or 3b.

### 4. Detailed surveys exist, but only for a patchwork of planning-related sites

After the 1988 revised guidelines were published, MAFF carried out detailed site-specific surveys between 1989 and 1999. These are far higher quality: typically at 1:10,000 scale, involving soil auger borings, pit inspections, and proper climate data integration. They do distinguish between 3a and 3b.

The catch: these surveys were only done for land that was under consideration for development proposals. They are not a systematic re-mapping of England. There is no comprehensive programme to survey all areas in detail. What exists is a patchwork of individual site assessments, mostly around the edges of towns. Natural England made these available as open data from around 2016, and described the dataset as "the most detailed and up-to-date ALC dataset." The post-1988 survey polygons can be viewed on Natural England's Open Data Geoportal.

### 5. There is no published breakdown of how much land falls in each grade

This one is particularly frustrating. Despite the ALC being the official framework for decades, I have been unable to find a published summary table showing "X hectares are Grade 1, Y hectares are Grade 2," etc. at the national level. The raw GIS shapefiles are available as open data from data.gov.uk and could be used to calculate this, but the fact that nobody seems to have published a convenient national breakdown is telling.

We know some approximate facts (Grade 3 is "about half," BMV was estimated at about 41% of farmland in 2012), but precise figures for Grade 4 and 5 separately are not readily available. The [[Farming Evidence Pack (DEFRA)\|Farming Evidence Pack (DEFRA)]] contains some government-level data on land use but does not resolve this gap.

### 6. Scotland uses a completely different system

The ALC only covers England and Wales. Scotland uses the Land Capability for Agriculture (LCA) system, developed by the James Hutton Institute (formerly Macaulay Institute). This is a seven-class system where Class 1 is the best and Class 7 is of very limited agricultural value. Classes 1-3.1 are considered "prime" agricultural land (roughly equivalent to BMV in the English system).

The Scottish LCA assessment was carried out in 1981 using data collected between 1978 and 1981, with the 1:250,000 national map published in 1983. More detailed 1:50,000 scale maps covering most of Scotland's cultivated agricultural land were published between 1984 and 1986. There are no plans to update the existing LCA maps, though a digital research platform has been developed to model LCA under different climate change projections.

This means that anyone making claims about "UK grazing land" is talking about two different classification systems that are not directly comparable, both relying on data from the late 1970s to early 1980s at best. [[UK farmland use\|UK farmland use]] has additional data on how land classifications break down across the UK, including the Less Favoured Area (LFA) designations that classify 80-90% of land in Wales and Scotland.

### 7. Land that is used for grazing is not the same as land that can only be used for grazing

This conflation is common and it matters. About 50% of agricultural land in England is grassland and 43% is crops. Much of that grassland is on perfectly good land, potentially Grade 3a or even Grade 2, that is used for grazing by choice (because livestock farming is the established system, or because the farmer prefers it, or because the economics currently favour it). It does not mean that land cannot grow crops.

[[UK agricultural subsidies\|UK agricultural subsidies]] is important context here: subsidy structures, including Less Favoured Area Support Schemes, actively incentivise keeping land in grazing use regardless of its actual productive potential. Some land is grazed because it is subsidised to be grazed, not because nothing else can grow there.

Only Grade 5 land is formally defined as restricted to permanent pasture or rough grazing. Grade 4 land can support some arable crops, just badly and inconsistently. The claim that "most UK grazing land can only be used for grazing" is much stronger than the evidence supports, particularly given how coarse and outdated the underlying classification data is.

[[Is pastoralism the solution to the problems food security and animal agriculture\|Is pastoralism the solution to the problems food security and animal agriculture]] makes a complementary point: even the land that genuinely is marginal barely supports animals either, with harsh conditions and low productivity making the case for grazing weaker than it first appears. [[Land use change, rewilding, grazing and rainforests\|Land use change, rewilding, grazing and rainforests]] goes further, arguing that land assumed to be locked into grazing could support rewilding or Celtic rainforest restoration instead.

For the broader picture of how animal agriculture's land footprint compares to its caloric output, see [[Animal agriculture takes up lots of land but provide few calories\|Animal agriculture takes up lots of land but provide few calories]]. [[Grass fed beef is not better for the environment\|Grass fed beef is not better for the environment]] examines similar land use efficiency claims in the context of pasture-based systems.

## What Would Fix This?

1. A comprehensive resurvey of England and Wales using the post-1988 methodology, with modern climate data and the 3a/3b distinction. This would be expensive but would give us an actual evidence base.
2. Updated climate parameters in the ALC guidelines. The system currently uses 1941-1980 climate data. CPRE and others have been calling for this.
3. A published national breakdown by grade calculated from the existing GIS data, even if just from the provisional maps. This is a trivial GIS task that would at least give everyone a common starting point.
4. Harmonisation or at least a clear mapping between the England/Wales ALC and the Scottish LCA, so that UK-wide claims can be made with appropriate caveats.

## What Could British Land Actually Do?

The question of what would happen if land currently used for grazing were repurposed is explored across several vault notes. [[Convert animal feed cropland to growing vegetables for UK nutrition security\|Convert animal feed cropland to growing vegetables for UK nutrition security]] presents evidence that the UK can grow alternative crops like fava beans, pulses, and legumes on land currently used for livestock feed. [[UK crops and animal feed\|UK crops and animal feed]] documents existing UK pulse and legume production and the underutilized potential for protein crops. [[Boosting UK food security with Alternative Proteins\|Boosting UK food security with Alternative Proteins]] examines the broader alternative protein landscape and its land use implications.

[[Food security in the UK\|Food security in the UK]] provides self-sufficiency data and land productivity analysis, while [[There is no food security case for more factory farming cattle\|There is no food security case for more factory farming cattle]] and [[Livestock on leftovers will not save us, we have to reduce meat\|Livestock on leftovers will not save us, we have to reduce meat]] both question assumptions about the necessity of current land use patterns.

[[Is factory farming necessary for UK food security Q Sustain event talk\|Is factory farming necessary for UK food security Q Sustain event talk]] covers related ground from a public-facing presentation angle.

## Summary

The honest answer to "how much UK land is only fit for grazing?" is: we don't know with any precision. The classification system is sound in principle but its implementation is 50+ years out of date, relies on climate data from as far back as the 1940s, doesn't distinguish between the two halves of its largest grade category, has only been properly surveyed for about 8% of rural England, and doesn't even cover Scotland (which uses a different system entirely).

Grade 5 land almost certainly cannot support crops. Grade 4 land is ambiguous. And a significant portion of land currently used for grazing may well be capable of growing crops but has simply never been assessed at the necessary level of detail.

Sources last checked: April 2026. ALC data is maintained by Natural England. Scottish LCA data is maintained by the James Hutton Institute.


# AI suggested related articles

- [[Citations/Feeding Britain from the Ground Up (Sustainable Food Trust)\|Citations/Feeding Britain from the Ground Up (Sustainable Food Trust)]] (0.77)
- [[Citations/Broomfield et al., 2025\|Citations/Broomfield et al., 2025]] (0.76)
- [[Citations/Land of opportunity - a new land use framework to restore nature and level up Britain (Green Alliance)\|Citations/Land of opportunity - a new land use framework to restore nature and level up Britain (Green Alliance)]] (0.75)
