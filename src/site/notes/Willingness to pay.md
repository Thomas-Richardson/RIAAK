---
{"dg-publish":true,"permalink":"/willingness-to-pay/","tags":["#economics","#statistics","#research_methods"],"created":"2025-10-23T17:42:44.151+01:00","updated":"2025-10-23T18:06:08.696+01:00"}
---

#economics  #statistics #research_methods 

- Willingness to pay is the highest value a consumer will pay for a product
- Generally its best to compute willingness to pay relative to your main competitor, but you may often have too many to benchmark or none at all
- [marginal willingness to pay (MWTP)](https://conjointly.com/guides/how-to-interpret-marginal-willingness-to-pay/): the amount customers are willing to pay for a particular feature of your product relative to a specified baseline (i.e. how much your customers are willing to pay for an upgrade from feature A to feature B, in addition to the price they are already paying).
- Note willingness to pay changes over time and varies from person to person.
## How is it measured?
- <mark style="background: #FFF3A3A6;">Gabor-Granger</mark>: elasticity modelling. good for when you have a reasonable range of prices and want the revenue maximising one.
- <mark style="background: #FFF3A3A6;">Van Westendorp</mark>: Identifies each respondents' **"too cheap"**,**"cheap"**,**"expensive"**, and **"too expensive"** price levels to determine **acceptable price range**. Goood when you don't have a good idea on the range of prices to consider
- <mark style="background: #FFF3A3A6;">Conjoint Analysis</mark>: for marginal WTP
- <mark style="background: #FFF3A3A6;">Revealed preference modelling</mark> (name mine): rarer, but uses previouus data to extrapolate to what they would pay for an product they've never seen

## Gabor-Granger
Read more here: https://conjointly.com/products/gabor-granger/

Basically Price elasticity modelling:

![Pasted image 20240621113213.png|600](/img/user/Pasted%20image%2020240621113213.png)

You can ask them multiple "would you buy this for $XX?". I'd probably add in random product attributes or descriptions. Or just ask each participant once or twice. 

[Some articles](https://conjointly.com/blog/gabor-granger-or-van-westendorp/#van-westendorps-price-sensitivity-meter) advocate asking multiple times the same person then getting a highest WTP, the plotting that. I am sceptical of this.

I'd get a few yes/no questions answers, then fit a logstic regression to get the curve, then multiply out each price point with the probability to optimize the price.
### Van Westendorp’s Price Sensitivity Meter
[Van Westendorp’s Price Sensitivity Meter](https://conjointly.com/products/van-westendorp/) is used to build a **range of acceptable prices** for a given item with the following questions:
- At what price would you consider {product} to be so expensive that you would not consider buying it? This gives you <mark style="background: #FFF3A3A6;">Too expensive</mark>
- At what price would you begin to think {product} is getting **expensive**, but you still might consider buying it? This gives you <mark style="background: #FFF3A3A6;">Expensive</mark>
- At what price would you begin to think the product is **so cheap** that you would feel the quality couldn't be very good and not consider it?  This gives you <mark style="background: #FFF3A3A6;">Too cheap</mark>
- At what price would you think the product is a **bargain** – a great buy for the money? This gives you <mark style="background: #FFF3A3A6;">Cheap</mark>

Note: show all 4 questions on the same page to get participants to consider them all together.

Then you can plot them all:

![Pasted image 20240624132413.png|600](/img/user/Pasted%20image%2020240624132413.png)

- The lower bound for this product is where too cheap and expensive intersect. 
	- At prices below this, more consumers think its too cheap than think its expensive
- The upper bound is where too expensive and cheap intersect. 
	- Price higher than this, more consumers think its too expensive than think its cheap
- The optimal price might be the intersection of too expensive and too cheap

You can find the price for which the most people

## Conjoint analysis

![Pasted image 20240624132836.png|600](/img/user/Pasted%20image%2020240624132836.png)

- Price points should range from ~60% to 140% of the realistic price.
- Include up to 7 attributes
- Conjointly argues that 10-14 questions is sufficient
![Pasted image 20240701180753.png|600](/img/user/Pasted%20image%2020240701180753.png)

Preference scores are used to [build simulators](https://conjointly.com/guides/conjoint-preference-share-simulator/) that forecast market shares for a set of different products offered to the market.
## Revealed preference modelling
- This is called many things in the literature but basically its building a model of what consumers paid predicted by the features of a product, then you can use that model to predict what they'd pay for a hypohetical ew product by inputting its hypothetical features.
- I wonder if you can use quantile methods to get a range of willingness to pay?