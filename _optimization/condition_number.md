---
tags: optimization
---

$$\frac{\lambda_{\text{largest}}}{\lambda_{\text{smallest}}}$$



The condition number $\kappa_2(A) = \sigma_{\max}/\sigma_{\min}$ quantifies how many digits you lose when solving $Ax = b$: in double precision, you retain approximately $16 - \log_{10}\kappa_2(A)$ reliable digits since relative error scales as $\kappa_2(A) \cdot u$ where $u \approx 10^{-16}$. For symmetric matrices, $\kappa_2(A) = |\lambda_{\max}|/|\lambda_{\min}|$ (or $\lambda_{\max}/\lambda_{\min}$ when positive definite), revealing the physical meaning—this eigenvalue ratio measures how unevenly the matrix stretches space, with large ratios indicating the matrix barely distinguishes vectors along small-eigenvalue directions, making the inverse hypersensitive there. Well-conditioned matrices like the identity have $\kappa = 1$ and preserve all 16 digits, while $\kappa = 10^8$ costs 8 digits of accuracy even with stable algorithms, and as $\lambda_{\min} \to 0$ the condition number explodes, causing catastrophic accuracy loss that no algorithm can overcome.