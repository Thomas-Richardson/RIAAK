---
{"dg-publish":true,"permalink":"/farming-jobs-lost-to-to-industrialisation/","tags":["Economics/jobs","farmers","factory_farming","Bryant/Project/cawf_hidden_harms"],"created":"2025-10-23T17:42:42.235+01:00","updated":"2025-11-06T16:12:38.811+00:00"}
---

- [[CAWF 2 farming MOC.canvas|CAWF 2 farming MOC]]
- [[Are rural communities dependent on animal agriculture for jobs\|Are rural communities dependent on animal agriculture for jobs]]?

Estimating the UK jobs lost / not created due to industrialisation is difficult for 2 reasons:
1. There is no public data on the number of people employed in livestock farming that we know of.
2. It is difficult to isolate the effect of industrialisation just by looking at changes in agricultural jobs in the UK alone. The number of agricultural jobs in the UK overtime is affected by a large number of factors that may be unrelated to industrialisation.

We overcome these issues 2 ways:
1. We estimate the effect of meat production on all agricultural jobs, not just jobs in the livestock sector. The data is directly available. 
2. We use data from a variety of developed countries to isolate the effect of "livestock industrialisation". By examining a number of developed countries who have industrialised their livestock sectors and extracting the common trend, we get an estimate of the average effect of livestock sector industrialisation and agricultural jobs.
  
We combined 2 datasets
1. A dataset of agricultural employment for various countries around the world compiled by [Our World In Data](https://ourworldindata.org/agri-employment-sources) from various sources.
2. A dataset of total countrywide meat production, using FAO data [compiled by Our World in Data](https://ourworldindata.org/meat-production). We summed the tonnage of meat produced for beef, pork and poultry only

For both datasets, we selected all countries in Europe, for the years between 1991-2019. This was the full range of the data available, however data from 1961-1991 was also available for Finland, France, The Netherlands, Spain, Sweden, the UK and the US, which we also included.

The model we used to estimate the effect of livestock sector industrialisation on agricultural jobs was a fixed effects linear regression. This model predicted total agricultural jobs from total meat production, with fixed effects of year and country.

The fixed effects design means that the model is not vulnerable to abnormal years (such as 2008) or abnormal countries (meat production in the US is the highest in the data by a wide margin). The model thus isolates the potential effect of total meat production on agricultural jobs.

### Assumptions
We assume that countries in the data have seen at least some industrialisation of their livestock sectors over time. If this is true, the common patterns between countries across years reflects the effect of industrialisation on a given country.

By using meat production as a proxy of meat sector industrialisation, we are assuming that meat production *only* affects agricultural jobs by reducing the number of livestock farming jobs. Increasing meat production may also come from a number of unrelated factors: improvement in livestock genetics, economic growth, and decreasing meat imports to name a few. However, none of these would be expected to reduce the number of jobs in the agricultural sector, so are unlikely to confound our analysis.

On the other hand, meat production may also increase if the number of farms increases, which should increase the number of agricultural jobs. Additionally, industrialised animals are more likely to be fed crops than non-industrial farm animals, so we should expect that the industrialisation of the UK livestock sector will have increased the number of agricultural jobs in crops. Both of these factors Increase the number of agricultural jobs, so they cannot account for our finding that increased meat production reduces agricultural jobs. In fact, this will mean that we somewhat underestimate the number of livestock jobs that have been destroyed/not created due to livestock industrialisation. 

To calculate job losses due to industrialisation for the UK specifically, we apply the coefficient from our multi-country regression model to UK data. This means that we are assuming that the UK has average levels of industrialisation compared to other countries in the dataset. In fact, it is likely the UK has seen more livestock industrialisation than the average European country. As a result this means our estimates of job losses will be further underestimated.

Fixed effect model cannot definitively prove that something causes something else. However they can provide estimates of causal effects provided some assumptions are met. For us to conclude that increasing meat production causes a decrease in agricultural employment, we must make two assumptions

- That increased meat production in a country does not decrease agricultural jobs through any other mechanism other than automation. If it does, our estimates of job losses will be overestimated.
- That there is no unmeasured third variable that increases production and decreases agricultural jobs as a whole. While we are unable to identify any such variables, we cannot be sure they do not exist.

### Model robustness check
We refit the model many more times, each time excluding a different country or year to test whether results were strongly impacted by the inclusion of certain countries or years. In all cases the results were largely similar, and in all cases meat production had a significant negative effect on agricultural employment.

We also repeated the entire analysis redefining meat production as only pork and poultry (i.e. excluding beef), as beef has seen far less industrialisation as pork and poultry. Consistent with our hypothesis, the effect of meat production in these models showed an even strong negative effect on agricultural jobs.

## Misc
Farm business income is basically net profit
## Number of people employed in agriculture:
https://www.gov.uk/government/collections/agricultural-workforce

![Pasted image 20240617161713.png](/img/user/Pasted%20image%2020240617161713.png)
from [here](https://defra-farming-stats.github.io/auk-dashboard/#workforce)



- If we can get longitudinal data on production by value and production my volume we can estimate prices.
	- https://defra-farming-stats.github.io/auk-dashboard/#production-by-value