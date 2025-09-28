---
{"dg-publish":true,"permalink":"/the-cost-to-the-nhs-of-diabetes-cvd-cancer-and-obesity/","created":"2024-04-22T13:03:43.000+01:00","updated":"2025-09-29T00:29:57.079+01:00"}
---

#economics #health_nutrition

- [[Bryant Confidential/CAWF NHS report MOC\|CAWF NHS report MOC]]

- These are called "burden of illness" studies

NHS budget for 2023/24 [is £160b](https://www.bma.org.uk/advice-and-support/nhs-delivery-and-workforce/funding/health-funding-data-analysis#:~:text=The%20vast%20majority%20of%20the,Public%20Health%20England%20in).
## CVD
- The Public Health England[^10] estimate CVD-related healthcare costs alone in England amounting to an estimated £7.4 billion per year in 2019, and annual costs to the wider economy being an estimated £15.8 billion.[^11] 
	- As [84% of the UK population](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationestimates/bulletins/annualmidyearpopulationestimates/mid2021) lives in England, if we assume that the per capita CVD costs are equal in other parts of the UK (they probably cost more tbh) then we can scale the £7.4 by 1/0.84:
```math
7400000000/0.84
```

- [[Citations/Barton et al., 2011\|Barton et al., 2011]] argued that a 1% reduction in CVD events across the population would save the NHS £30 million. That was for 50 million people (England and Wales). Scaled to all of GB and assuming healthcare spending is the same in Scotland and Ireland, we multiply that by 67000000/50000000 to get 40.2M for all the UK in 2011, if we inflate that to 2023 that means multiplying by 2.5% over 12 years. We found a 10% meat reduction reduced risk by 1.35% so we scale the saving by 1.35 and this gives us the savings that we could expect from 10% meat reduction. 
{ #fb2fb1}


```math
30000000*(67/50)*(1.025^12)*1.35
```
{ #285139}


Concerningly this number is far lower than the 132M we estimated in our model. That said, Barton was weighing the value of preventing events and we're weighing the value of prevented deaths, so ours are more valuable. But are they nearly 2x as valuable? 
## Cancer
[The Independent Cancer Taskforce Report](http://www.cancerresearchuk.org/sites/default/files/achieving_world-class_cancer_outcomes_-_a_strategy_for_england_2015-2020.pdf) (ICTR) [estimated](https://ukhsa.blog.gov.uk/2016/11/01/understanding-the-costs-and-benefits-of-investing-in-cancer/#:~:text=It%20says%3A%20%E2%80%9CThe%20National%20Audit,indicate%20that%20this%20will%20grow) that cancer services cost the NHS approx £6.7bn per year in 2012/2013 and that this would grow by about 9% a year. Extrapolating this to 

```math
6.7*1.09^11
```
## Obesity
- Overweight and obesity is estimated to have cost the NHS £5.1 billion in 2007/2008[^1]
- It is estimated[^13] that the NHS spent £6.1 billion on overweight and obesity-related ill-health in 2014 to 2015.
- Obese individuals cost the NHS [1.5-2 times as much per year](https://www.theguardian.com/society/2023/may/18/obese-patients-cost-nhs-twice-much-healthy-weight-study) as health weight individuals

## Type 2 Diabetes
- A 2012 study found that Type 2 diabetes was responsible for 9.2% of total health resource expenditure (92% of the 10% that all diabetes cost) £8.8b in direct costs[^2] and £13bn in indirect costs such as mortality, sickness, presenteeism and informal care. They project that by 2035 it would rise to 17% of spending.

## More generally
 [^3] [^4]
## References
[^1]: Scarborough, P., Bhatnagar, P., Wickramasinghe, K. K., Allender, S., Foster, C., & Rayner, M. (2011). The economic burden of ill health due to diet, physical inactivity, smoking, alcohol and obesity in the UK: an update to 2006–07 NHS costs. _Journal of public health_, _33_(4), 527-535 t.ly/Y612B
[^2]: Hex, N., Bartlett, C., Wright, D., Taylor, M., & Varley, D. J. D. M. (2012). Estimating the current and future costs of Type 1 and Type 2 diabetes in the UK, including direct health costs and indirect societal and productivity costs. _Diabetic medicine_, _29_(7), 855-862 https://azkurs.org/pars_docs/refs/4/3027/3027.pdf
[^3]: Briggs, A. D., Scarborough, P., & Wolstenholme, J. (2018). Estimating comparable English healthcare costs for multiple diseases and unrelated future costs for use in health and public health economic modelling. _PLoS One_, _13_(5), e0197257. t.ly/wBRKq
[^4]: Murray, C. J., Richards, M. A., Newton, J. N., Fenton, K. A., Anderson, H. R., Atkinson, C., ... & Davis, A. (2013). UK health performance: findings of the Global Burden of Disease Study 2010. _The lancet_, _381_(9871), 997-1020. t.ly/dbhqt
[^10]: Health Matters: Preventing cardiovascular disease t.ly/jUtLt
[^12]: Barton, P., Andronis, L., Briggs, A., McPherson, K., & Capewell, S. (2011). Effectiveness and cost effectiveness of cardiovascular disease prevention in whole populations: modelling study. _Bmj_, _343_. https://www.bmj.com/content/343/bmj.d4044.short
[^13]: https://www.gov.uk/government/publications/health-matters-obesity-and-the-food-environment/health-matters-obesity-and-the-food-environment--2