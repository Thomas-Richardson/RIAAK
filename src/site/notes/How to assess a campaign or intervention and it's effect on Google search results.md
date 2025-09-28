---
{"dg-publish":true,"permalink":"/how-to-assess-a-campaign-or-intervention-and-it-s-effect-on-google-search-results/","created":"2024-10-18T15:51:54.354+01:00","updated":"2025-09-29T00:15:35.097+01:00"}
---

- [[Do Documentaries work\|Do Documentaries work]]
# Analyzing the Impact of an Animal Welfare Report on Veganism Interest: A Difference-in-Differences Approach

## Understanding Difference-in-Differences (DiD)

DiD is a quasi-experimental design used to estimate causal relationships when randomization is not feasible. It compares the changes in outcomes over time between a treatment group and a control group.

- **Treatment Group:** Vegan-related search terms
- **Control Group:** Non-vegan-related search terms
- **Pre-Treatment Period:** Weeks before the report was released
- **Post-Treatment Period:** Weeks after the report was released

## Your Regression Model Components

### Dependent Variable:
- **Search Term Interest:** The weekly search interest for each term from Google Trends

### Independent Variables:
- **Report Live Indicator (`Post`):**
  - `0` before the report was released
  - `1` after the report was released
- **Vegan-Relevant Term Indicator (`Treatment`):**
  - `1` for vegan-related terms
  - `0` for non-vegan-related terms
- **Interaction Term (`Post × Treatment`):**
  - Captures the DiD effect—the additional change in search interest for vegan terms after the report
- **Month Dummies:** Controls for seasonality by accounting for monthly variations
- **Week Number:** Addresses linear trends over time
- **Year Dummies:** Accounts for any yearly effects not captured by the week number or month dummies

## Regression Equation

Your model can be specified as:

```
SearchInterest(it) = β0 + β1 Post(t) + β2 Treatment(i) + β3 (Post(t) × Treatment(i)) + β4 WeekNumber(t) + ∑(m=1 to 11) γm MonthDummy(mt) + ∑(y=1 to Y) δy YearDummy(yt) + ε(it)
```

- `i`: Search term index
- `t`: Time index (week)
- `β3`: The DiD estimator—the effect of the report on vegan-related terms

## Interpreting the Model

- **β1** captures overall changes over time affecting all terms
- **β2** accounts for inherent differences between vegan and non-vegan terms
- **β3** is the key coefficient, measuring the differential effect of the report on vegan terms
- **Month and Year Dummies** control for seasonality and yearly effects
- **β4** captures linear time trends

## Modeling Complex Changes Over Time

To capture more nuanced trends and ensure the robustness of your results, consider the following enhancements:

### 1. Non-Linear Time Trends

- **Include Higher-Order Time Terms:**
  - Add `WeekNumber(t)^2` or even higher powers to model non-linear trends
- **Spline Regression:**
  - Use piecewise linear splines to allow different trends in different periods

### 2. Differential Trends Between Groups

- **Include Interaction of Time and Treatment:**
  - Add an interaction term `WeekNumber(t) × Treatment(i)` to allow vegan-related terms to have a different time trend than non-vegan terms

### 3. Fixed Effects

- **Term Fixed Effects:**
  - Include term-specific fixed effects to control for unobserved, time-invariant characteristics of each search term
  - Modified model:
    ```
    SearchInterest(it) = β0 + β1 Post(t) + β3 (Post(t) × Treatment(i)) + β4 WeekNumber(t) + α(i) + ∑(m=1 to 11) γm MonthDummy(mt) + ∑(y=1 to Y) δy YearDummy(yt) + ε(it)
    ```
    - `α(i)`: Term fixed effects
- **Time Fixed Effects:**
  - Replace month and year dummies with week fixed effects to control for any common shocks affecting all terms in a particular week

### 4. Testing the Parallel Trends Assumption

- **Pre-Trend Analysis:**
  - Validate that vegan and non-vegan terms followed similar trends before the report
  - Include leads and lags of the treatment variable to test for pre-intervention effects

### 5. Controlling for Other Confounders

- **Incorporate Additional Covariates:**
  - Include variables that capture other factors influencing search interest (e.g., other media events, holidays, policy changes)

### 6. Addressing Autocorrelation and Heteroskedasticity

- **Robust Standard Errors:**
  - Use clustered standard errors at the search term level to account for within-term correlation over time
- **Alternative Estimators:**
  - Consider using generalized least squares (GLS) or Newey-West standard errors if appropriate

## Implementing the Enhanced Model

With these considerations, an enhanced model might look like:

```
SearchInterest(it) = β0 + β1 Post(t) + β2 (WeekNumber(t) × Treatment(i)) + β3 (Post(t) × Treatment(i)) + α(i) + λ(t) + ε(it)
```

- `λ(t)`: Time fixed effects (could be week, month, or year, depending on granularity)

## Additional Considerations

### Selection of Control Terms

- Choose non-vegan-related terms that:
  - Have similar pre-report trends to vegan terms
  - Are unaffected by the report
- Potential control terms could be related to other dietary preferences or general health topics not influenced by animal welfare reports

### Data Visualization

- **Plot Trends Over Time:**
  - Visualize the average search interest for both vegan and control terms before and after the report
- **Check for Structural Breaks:**
  - Identify any abrupt changes not accounted for in the model

### Alternative Methods

If assumptions of DiD are not fully met, consider:

- **Interrupted Time Series Analysis:**
  - Model the change in search interest for vegan terms only, focusing on changes in level and slope at the time of the report
- **Synthetic Control Method:**
  - Create a synthetic control group that better matches the pre-intervention trends of vegan terms

## Conclusion

Your proposed regression model effectively sets the foundation for a DiD analysis. By incorporating interaction terms and controlling for time trends and seasonality, you're positioned to estimate the causal impact of the report. Enhancing the model to account for differential trends and fixed effects will help address complex changes over time and strengthen the validity of your findings.

## Next Steps

1. **Data Preparation:**
   - Ensure your data is structured in a panel format with observations for each term-week combination
2. **Assess the Parallel Trends Assumption:**
   - Conduct pre-intervention trend analysis to validate the DiD approach
3. **Model Estimation:**
   - Estimate the regression model using appropriate statistical software
4. **Robustness Checks:**
   - Test alternative model specifications
   - Perform placebo tests using different intervention dates
5. **Interpretation:**
   - Carefully interpret the coefficients, particularly the interaction term, in the context of your study
6. **Documentation:**
   - Document all modeling choices and justify them based on statistical principles and the context of your research

By thoughtfully designing your regression model and thoroughly testing its assumptions, you'll be able to provide compelling evidence regarding the impact of the animal welfare report on interest in veganism.