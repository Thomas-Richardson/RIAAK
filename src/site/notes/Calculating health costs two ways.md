---
{"dg-publish":true,"permalink":"/calculating-health-costs-two-ways/","created":"2026-02-24T13:51:22.361+00:00","updated":"2026-02-24T14:57:15.695+00:00"}
---

In order to calculate the health costs of animal products and plant products, you broadly have two methods. Both of these involve calculating the DALYs involved and then attaching some monetisation factor to each DALY. 

1. Look at how much a country is actually spending on a particular disease or to address a certain risk (e.g. [[Citations/The cost of red and processed meat (Zero Carbon Analytics)\|The cost of red and processed meat (Zero Carbon Analytics)]]). This basically assumes that the cost, the amount spent on treating a disease, symptom, or whatever, is directly proportional to the percentage of a country's total DALY burden it represents. If cancer is 10% of the DALYs in the country, we infer that they spend 10% of their health care budget on it. 
	- Flawed because some diseases have highly visible suffering or easily treatable suffering, we might devote more resources or less 
	- but it seems to be roughly correct, and has the property that it is extremely easy to calculate for lots of countries at once without having to track down individualised measures of how much they spend on each disease, which may not even be available.
2. Using the Value of a Life Year (VOLY)
	- [[Citations/External Costs of Animal Sourced Food in the EU ( Impact Institute, 2023)\|External Costs of Animal Sourced Food in the EU ( Impact Institute, 2023)]] Use an approach where they take the value of a statistical life from the OECD and divide it by some number of years (They appear to calculate the average number of healthy years left for a European by using the median age and subtracting from median age at death). The average European has 35 years left to live, so they should be willing to pay 1/35th of this value for each year of life. This is kind of ok but is distorted because it gives you the value of a year regardless of health, so it cannot be equated to DALYs, which have been adjusted for health.  they're also using willingness to pay to not die estimates to compute willingness to pay to avoid a year of disability, which are not the same thing.
	- 
- Using QALYs: DALY burden is years of healthy life lost. QALY cost is the cost people would be willing to pay for a year of life, where un

# VSL
The value of a statistical life is a measure of how much money a life is worth.

The way they do it is they do a load of willingness to pay studies to find out how much people would be willing to pay to reduce their mortality risk. For example someone might be willing to pay £10k to reduce their chance of dying by 1/1000th. 

Then they scale this up to a number that would be equivalent to preventing certain death. So for our example above, this means £10,000 multiplied by 1,000.

 The issue with this number is that it is often treated as the value of one life but it is very much the value of one life at the population level. Because the question of how much money the average person would be willing to pay to avoid themselves dying is not really a question that can be answerable in a satisfactory way. Because it's mostly just dependent on how much money people have. it's also probably an underestimate because a person is probably willing to pay a lot more to avoid death than a hundred people would pay to avoid a 1% risk of death. The math doesn't really work down to the individual level.
 
 The number is only valid for calculations that involve reducing mortality risk by a small amount over a large population. It cannot be used to derive the value of things that have a high chance of killing people. Even if someone is ethically okay with using this number to put a value on a single person's life, it simply would not be statistically valid either 