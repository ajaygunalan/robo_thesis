---
tags: ml basics
---

[Video](https://www.youtube.com/watch?v=XepXtl9YKwc&ab_channel=StatQuestwithJoshStarmer)

## Negative Log-Likelihood in Maximum-Likelihood Learning

> [!abstract] In maximum-likelihood learning we pick the parameters θ that make the training set look **least surprising** under our model. Because log-probabilities turn products into sums and "minus" turns maximization into minimization, this goal becomes the average **negative log-likelihood (NLL)** objective:
> 
> $$\mathcal{L}(θ)= -\frac1n\sum_{i=1}^{n}\log p_{θ}\bigl(x^{(i)}\bigr)$$

## Where the equation comes from

> [!info]
> 
> - **Independent data ⇒ product of probabilities**  
>     For i.i.d. data the joint likelihood is $\prod_{i=1}^{n} p_{θ}(x^{(i)})$ 
>     
> - **Logs make life easy**  
>     Taking a log converts the product into a sum:  
>     $\log\prod_{i} p_{θ}(x^{(i)}) = \sum_{i} \log p_{θ}(x^{(i)})$  
>     Sums are numerically stable and differentiable; gradients turn into simple averages 
>     
> - **From maximization to minimization**  
>     Optimizers are usually written as minimizers. Adding a minus sign turns "maximize log-likelihood" into "minimize negative log-likelihood." Dividing by n makes the scale independent of dataset size.
>     

## Intuition in plain words

> [!tip]
> 
> - **Log-likelihood ≈ "surprise."**  
>     Each $-\log p_{θ}(x^{(i)})$ tells us how surprising sample $x^{(i)}$ is under the model: high probability ⇒ small surprise; low probability ⇒ large surprise. We adjust θ to shrink average surprise 
>     
> - **Equivalent view: match distributions.**  
>     The average NLL is (up to an additive constant) the KL divergence $D_{KL}(\hat p_{data}\parallel p_{θ})$. Minimizing NLL therefore **pushes the model toward the empirical data distribution**
>     

## Mental checklist for reading the formula

|Symbol|Meaning|Quick cue|
|---|---|---|
|$p_{θ}(x^{(i)})$|Model probability of sample $x^{(i)}$|"How likely does θ say this point is?"|
|$\log$|Converts products to sums|"Works better for gradients"|
|− sign|Turns maximize into minimize|"Standard loss convention"|
|$1/n$|Average per sample|"Dataset-size independent"|


