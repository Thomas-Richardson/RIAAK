---
{"dg-publish":true,"permalink":"/decreased-property-values-from-living-near-im-ps/","created":"2025-10-23T17:42:47.559+01:00","updated":"2025-10-23T18:06:40.018+01:00"}
---

#cawf_farming 

- [[Transparent farms\|Transparent farms]]
- [[Proximity to CAFOs and house prices\|Proximity to CAFOs and house prices]]

To estimate the effect of proximity to an industrial meat production facilities on house prices, we used multi-level regression modelling to test whether houses closer to IMPs sold for lower values than those further away from IMPs. We used our sample of British households that sold in 2023 (see Appendix B), but restricted our analysis to houses with at least 1 IMP within 10km (67,989 houses) We removed a further 1045 houses with a sale value of over £1M as these extreme outliers skewed the distribution of house prices.

We fit a linear mixed effects model predicting house selling price from the distance to nearest IMP. We also included a binary variable of whether the house was a new build, as well as dummy variables for property type (flat, terrace, semi-detached, detached and other). We included random intercepts for district of the UK, postcode of the house and the identity of the nearest IMP. These random intercepts account for the fact that many houses have the some postcode, many districts of the UK naturally contain higher or lower house prices for reasons unrelated to IMPs, and some IMPs may have particularly strong effects on house prices. We also included a random slope of distance from IMP on the identity of the IMP. This models the possibility that different IMPs have different effects on house prices. This is because some IMPs are significantly larger than others so are likely to have stronger effects.

However, we did not find a significant effect of proximity to IMPs on selling price (p > 0.05). Including an effect of distance to nearest IMP squared (which models the hypothesis that the negative effect fades quickly with distance from a given IMP) also did not yield significant results. Additionally, natural log transforming house price (which represents the hypothesis that each km closer to an IMP decreases house price by a fixed *percentage*) also did not show results.