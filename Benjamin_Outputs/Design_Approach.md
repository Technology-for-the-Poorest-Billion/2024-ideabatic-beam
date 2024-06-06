# Communicating Design Decisions

Part of this project's useful output is a thorough documentation and justification of all design decisions made, quantified and visualised where possible. 

This is useful in the immediate term, as a means of presenting and justifying design decisions to the project partner, and also in the future, as subsequent work on this design problem will be streamlined by the clarity of this discussion, illustrating possibilities that have already been explored and eliminated. 

<br />

The [formalised problem definition](https://github.com/Technology-for-the-Poorest-Billion/2024-ideabatic-beam/blob/main/Benjamin_Outputs/Our_Design_Problem_and_Context.md) naturally gives rise to five key dimensions:
- Cost effectiveness
- Robustness: Environmental resistance and mechanical robustness
- Insulation
- Veracity of temperature prediction
- User friendliness, primarily concerned with modularity

A candidate's performance can be visualised using a radar plot.

<img width="450" alt="Screenshot 2024-05-27 at 10 17 01" src="https://github.com/Technology-for-the-Poorest-Billion/2024-ideabatic-beam/assets/98609386/c045e667-ff44-4336-966f-8e713be696de">

****Figure X: Example of a radar plot****

The scores assigned will be 

- somethinng here about the non-linear characteristic curves of threshold dimensions

The scores will then be combined to give a Key Performance Indicator (KPI), which quantifies the overall performance potential of a design. 

Given that a failure to be fit for purpose in any of the five dimensions would render a design unsuitable, the KPI is calculated as the product of the five scores.

$\{KPI}$ = Score 1 $\times$ Score 2 $\times$ Score 3 $\times$ Score 4 $\times$ Score 5

This product-rating method is also useful for eliminating design candidates: evidence that a candidate is unsuitable on any of the five dimensions immediately sets its KPI to zero and eliminates it from the design process. 

As such, each candidate is checked first against its most problematic dimension in a 'feasability test', so that it can be quickly eliminated if unfeasible. 

The radar plot conveniently visualises three important things:
- Area shows which design candidates to proceed with
- Relative strengths and weaknesses of each design candidate
- Areas for maximum improvement on each design candidate


*This document* shows the candidate designs which resulted from brainstorming, feasability assessments and dimension scoring which resulted in the prototyped design being taken forward.

<br />

# Scoring Candidates on Each Dimension

## Scoring Criteria

Based on personal judgement and continual discussion with the project partner, the following subjective (yet defensible) criteria were used for scoring on the five dimensions: **defend these further!**

### Cost effectiveness
- Any design which is unfeasible within the £15 budget is scored zero
- The remaining four designs are inseparable on cost (neglecting cost of wiring), so are all scored 5 

### Robustness: Environmental resistance and mechanical robustness
The primary risks for environmental and mechanical degradation are water ingress and damage to external wiring.
- Any design which might be susceptible to water ingress is scored 5
- Any design which requires external wiring is scored 8 (can be mitigated by further printing wiring)
- Any design with both of the above is scored 4
- Any design with neither is scored 10

### Insulation
- Any design which does not compromise insulation is scored 10
- Any design which multiplies the 24º cool lifetime by a factor k is scored k<sup>3</sup> x 10

### Veracity of temperature prediction
- Any design with the temperature sensor outside the insulation is scored 9 (an extra layer between sensor and vaccines increases error in algorithm, as there is uncertainty associated with the exact thermal resistance of each layer)
- Any design with the temperature sensor susceptible to mild inorganic heating (eg due to contact with the electronics) by less than 1ºC is scored 7
- Any design with both of the above is scored 6
- Other designs are scored 10

### User friendliness, primarily concerned with modularity
- Any design which has both mechanical and electrical modularity is scored 10
- Any design which is mechanically but not electrically modular is scored 6




