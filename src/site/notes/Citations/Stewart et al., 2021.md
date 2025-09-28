---
{"dg-publish":true,"permalink":"/citations/stewart-et-al-2021/","created":"2024-03-10T17:06:44.000+00:00","updated":"2025-09-28T23:48:59.282+01:00"}
---

#citation #meat 

- [[Change in demand for animal products worldwide#The UK\|Change in UK demand for meat]]
- [[Citations/Vonderschmidt et al., 2023\|Vonderschmidt et al., 2023]]
- Note that [[Citations/Smith, Scheebeek, Balmford and Garnett, 2021\|Smith, Scheebeek, Balmford and Garnett, 2021]]

Stewart, C., Piernas, C., Cook, B., & Jebb, S. A. (2021). Trends in UK meat consumption: analysis of data from years 1–11 (2008–09 to 2018–19) of the National Diet and Nutrition Survey rolling programme. _The Lancet Planetary Health_, _5_(10), e699-e708.

[Trends in UK meat consumption: analysis of data from years 1–11 (2008–09 to 2018–19) of the National Diet and Nutrition Survey rolling programme - The Lancet Planetary Health](https://www.thelancet.com/journals/lanplh/article/PIIS2542-5196(21)00228-X/fulltext)

- Using 4 day food diary data from the National Diet and Nutrition Survey (NDNS) 2018/19
- By a team at the Nuffield Department of Primary Care Health Sciences (University of Oxford) 
## Results
Between 2008/09 and 2018/19:
- <mark style="background: #FFF3A3A6;">Average daily meat consumption in the UK decreased</mark> by approximately 17.4g per person (from 103.7g to <mark style="background: #FFF3A3A6;">86.3g</mark>)
This can be broken down into: 
- A reduction of 13.7g of <mark style="background: #BBFABBA6;">red meat</mark> (from 37.4g to <mark style="background: #BBFABBA6;">23.7g</mark>) 
- A reduction of 7.0g of <mark style="background: #ABF7F7A6;">processed meat</mark> (from 33.8g to <mark style="background: #ABF7F7A6;">26.8g</mark>)
- An increase of 3.2g of <mark style="background: #FFF3A3A6;">white meat</mark> (from 32.5g to <mark style="background: #FFF3A3A6;">35.7g</mark>). 

```math
(37.4-23.7)/37.4
(35.7-32.5)/32.5
```

The two middle birth-year groups (people born in 1960–79 and 1980–99) and White individuals were the highest meat consumers. Meat intake increased over time among people born after 1999, was unchanged among Asian and Asian British populations, and decreased in all other population subgroups. We found no difference in intake with gender or household income.
# Own calculations from this data
## What percentage of meat eaten by Brits is processed?
This means that as of 2019 <mark style="background: #FFF3A3A6;">processed meat makes up 31.1%</mark> of British non-fish meat consumption
```math 
26.8/(26.8+23.7+35.7) %
```

## What percentage of white and red meat do brits eat is processed?
We might naively estimate that because 60% of non-processed meat Brits eat is white meat, that 60% of processed meat is also likely white meat. In reality more processed meat is likely to be red meat: burgers, sausages, ham and mince compared to chicken nuggets. So <mark style="background: #FFF3A3A6;">let's assume its around 50%</mark>

```math
35.7/(23.7+35.7) % # percentage of non processed meat that is white meat
```

```math
(26.8*0.5)+23.7 # amount of red meat (processed and unprocessed)
(26.8*0.5)+35.7 # amount of white meat (processed and unprocessed)
(26.8*0.5)/((26.8*0.5)+23.7) % # Percentage of all red meat that is processed
(26.8*0.5)/((26.8*0.5)+35.7) % # Percentage of all white meat that is processed
```

