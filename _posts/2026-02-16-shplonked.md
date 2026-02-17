---
title: "Generalising Shplonk"
author: waamm
date: 2026-02-16
categories: [Cryptography, Zero-Knowledge Proofs]
tags: [zero-knowledge-proof]
math: true
---

> "The raison d’être of KZG commitments is the remarkable efficiency of evaluation-proof verification."
>
> — Justin Thaler **[Tha22, p. 233]**

The KZG[^pronunciation] protocol was the first construction of a polynomial commitment scheme and remains one of the most widely deployed today **[KZG10]**. 

> **Definition (informal).**  
> Given a polynomial $f$, a *polynomial commitment scheme* (PCS) allows a prover to commit to $f$ and later produce a succinct proof that $f(x) = y$ at any chosen evaluation point $x$, without revealing $f$.
{: .box .definition }

[^pronunciation]: Usually it's named KZG after the authors Kate (pronounced [kah-tey](https://www.cs.purdue.edu/homes/akate/howtopronounce.html)), Zaverucha and Goldberg of **[KZG10]**, and is sometimes it's simply called after Kate.

The enduring appeal of the KZG scheme lies in two key properties: small constant-size evaluation proofs and fast verification of these proofs. KZG commitments now form a core building block in modern cryptography, including vector commitments, range proofs, [verifiable secret-sharing](https://en.wikipedia.org/wiki/Verifiable_secret_sharing) (e.g. **[AJM+23, MDR23, Chunky]**) and [SNARKs](https://en.wikipedia.org/wiki/Non-interactive_zero-knowledge_proof) (e.g. Plonk **[GWC19]**).

Subsequent work introduced techniques for *batching* multiple KZG evaluation proofs --- across different polynomials or different evaluation points --- into a single proof. The culmination of these batching techniques for the ordinary KZG scheme is $$\mathtt{SHPLONK}$$ **[BDFG20]**.

In this post, following Trisha Datta, we generalise $$\mathtt{SHPLONK}$$ so that:

1. The protocol can be instantiated with variants of KZG, not just the original KZG scheme.
2. The protocol supports selective disclosure: some evaluations may remain hidden, while the verifier learns only specified homomorphic functions of them.

We leave out security proofs for now. <span style="color:red">TODO</span>

## $$\mathtt{SHPLONKeD}$$

Suppose we have polynomials $f_1,\ldots,f_n$, each evaluated on a set of points $S_i$. $$\mathtt{SHPLONK}$$ proves all of these evaluations at once. Here, however, we want more flexibility:

1. Some evaluations should be revealed.
2. Some should remain hidden.
3. The verifier should learn only a specified homomorphic function $\varphi$ of the hidden values.

> **Example (masked sumcheck protocol).**  
> In the multivariate version of $\textsf{DekartProof}$, the prover needs to provide the verifier with certain evaluations (and corresponding opening proofs) at an $m$-dimensional challenge point $\mathbf{x} = (x_1 ,\ldots, x_m)$ so that the verifier can check an equation coming out of a masked version of the sumcheck protocol. For efficiency reasons, the masking polynomial $g$ used in this protocol is not committed to directly. Instead, we use that the multivariate polynomial $g$ decomposes into a sum of univariate polynomials $g(X_1 ,\ldots, X_m) = \sum_{i = 1}^m g_i(X_i)$ and commit separately to each of these univariate polynomials $g_i$. To prevent information leakage, we cannot reveal each of the evaluations $y_i \mathrel{\vcenter{:}}= g_i(x_i)$; rather, we reveal only their sum $\sum_{i = 1}^m y_i$, which is the sought-after evaluation $g(\mathbf{x})$. Thus, this setting corresponds to the homomorphism $\varphi(y_1, \ldots, y_m) \mathrel{\vcenter{:}}= \sum_{i = 1}^m y_i$.
{: .box .example }

### Preliminaries

> **Notation.**  
> Given a finite set of points $S$ in a field, we let $V_{S} (X) \mathrel{\vcenter{:}}= \prod_{s \in S} (X - s)$ denote the corresponding vanishing polynomial.
{: .box .notation }

Now recall that for each polynomial $f_i$ we have fixed a set $S_i$ of evaluation points, but that we want to keep some of the evaluations hidden.

> **Notation.**  
> Decompose each of these sets $S_i$ as
> 
> $$ S_i = S_i^\mathrm{rev} \sqcup S_i^\mathrm{hid}, $$
> 
> corresponding to the evaluations that are to be revealed and that are to be kept hidden, and let $h \mathrel{\vcenter{:}}= \sum_i \lvert S_i^\mathrm{hid} \rvert$ denote the total number of evaluations that need to be kept hidden.
{: .box .notation }

To facilitate computation of KZG opening proofs, it is convenient to encode the evaluations of $f_i$ over $S_i$ into a single polynomial.

> **Notation.**  
> Let $L_{i,s} (X)$ denote the Lagrange basis interpolation polynomial which evaluates to $1$ at $s \in S_i$ and to $0$ at all other points of $S_i$.
>
> Then the interpolation polynomial $g_i$ over $S_i$ is
>
> $$g_i(X) = \sum_{s\in S_i} L_{i,s} (X) f_i(s),$$
>
> which agrees with $f_i$ on all points of $S_i$.
{: .box .notation }

The KZG scheme is an example of [pairing-based cryptography](https://en.wikipedia.org/wiki/Pairing-based_cryptography), so we make use of a pairing-friendly elliptic curve:

> **Notation.**  
> Fix generators $[1]_1$ and $[1]_2$ of the groups $$\mathbb{G}_1$$ and $$\mathbb{G}_2$$. Then for a scalar $s$, define
>
> $$ [s]_1 \mathrel{\vcenter{:}}= s \cdot [1]_1 , \qquad \textrm{and} \qquad [s]_2 \mathrel{\vcenter{:}}= s \cdot [1]_2 .$$
{: .box .notation }

Finally, a multi-scalar multiplication (MSM) of size $k$ in an elliptic curve is an operation of the form

$$ \operatorname{MSM}(G_1,\ldots,G_k;s_1,\ldots,s_k) = \sum_{i=1}^k s_i \cdot G_i,$$

i.e., computing a linear combination of group elements $G_i$ with scalar coefficients $s_i$. MSMs are the dominant cost in many proof systems. Here and throughout, an MSM refers to a multi-scalar multiplication in $\mathbb{G}_1$.


### $$\mathtt{SHPLONK}$$

The claim that $f_i $ agrees with $g_i $ on the set $S_i$ is equivalent to the existence of a polynomial $q_i$ satisfying

$$q_i(X) = \frac{ f_i (X) - g_i (X) }{ V_{S_i} (X) }.$$

Applying a version of the Schwartz–Zippel lemma, it suffices given a challenge $c$ to show that there exists a polynomial $q$ such that 

$$q(X) = \sum_{i = 1}^nc^{i-1}  \frac{ f_i (X) - g_i (X) }{ V_{S_i} (X) },$$

which is equivalent to

$$V_S(X) \cdot q(X) = \sum_{i = 1}^n c^{i-1} V_{S\setminus S_i }(X) \cdot \bigl( f_i (X) - g_i (X) \bigr).$$

After committing to $q$, verifying this identity would need $n$ pairings for the right-hand-side, so $n+1$ pairings in total.

Therefore, it is cheaper for the verifier to test it at a point: the claim is that the prover knows $f_i$ and $q$ such that this identity holds. Thus after committing to $q$, the verifier sends a point $x$, and then the prover proves the identity by committing to 

\begin{align}
\check{q}(X) & = \frac{  \sum_{i=1}^n c^{i-1} V_{S \setminus S_i} (x) \cdot \bigl(f_i (X) - g_i (x) \bigr) - V_S (x)\cdot q(X) } {X - x}\nonumber \\\\\
 & = \frac{ \bigl( \sum_{i=1}^n c^{i-1} V_{S\setminus S_i} (x) \cdot f_i (X) - V_S (x) \cdot q(X) \bigr) - \sum_{i=1}^n c^{i-1} V_{S\setminus S_i } (x) \cdot g_i (x) } {X - x} \nonumber 
\end{align}

Using two pairings, this is done in KZG by verifying the identity

$$ \bigl( [\check{q}(\tau)]_1, [\tau]_2 - [x]_2 \bigr) = \bigl( \sum_{i=1}^n c^{i-1} V_{S\setminus S_i} (x) \cdot [f_i (\tau)]_1 - V_S (x) \cdot [q(\tau)]_1 - \bigl[\sum_{i=1}^n c^{i-1} V_{S\setminus S_i } (x) \cdot g_i (x) \bigr]_1 , [1]_2 \bigr),$$

and similarly in other variants.

### Hiding with a sigma protocol

Ordinarily in $$\mathtt{SHPLONK}$$ the prover would send over each $g_i(X)$ (which is natural as they are part of the statement to be proven), but this equation shows that for the pairing check the verifier only needs to be able to construct the expression

\begin{equation}
\bigl[\sum_{i=1}^n c^{i-1} V_{S\setminus S_i } (x) \cdot g_i (x) \bigr]_1.
\label{eq:eval}
\end{equation}

A natural approach would be for the prover to send commitments $$[y_i]_1$$ for the $h$ evaluations $y_i$ that need to be kept hidden, plus a sigma protocol proving that it knows the hidden $y_i$ which give
1. the commitments $$\{[y_i]_1 \}$$,
2. the element $\eqref{eq:eval}$, and
3. the image of $\varphi$.

This is already quite costly for the verifier: if the cost of evaluating the homomorphism $\varphi$ is dominated by computing an MSM of size $\operatorname{cost}(\varphi)$, then the verifier's cost for verifying this sigma protocol should be dominated by an MSM of size $\operatorname{cost}(\varphi) + 2h$.[^msm] Moreover, the verifier then needs to use another MSM of size $h+1$ MSM to compute

$$
\begin{align}
\bigl[\sum_{i=1}^n c^{i-1} V_{S\setminus S_i } (x) g_i (x) \bigr]_1 & = \bigl[\sum_{i=1}^n c^{i-1} V_{S\setminus S_i } (x) \sum_{s\in S_i} L_{i,s}(x) f(s) \bigr]_1 \nonumber \\
 & = \Bigl( \sum_{i=1}^n c^{i-1} V_{S\setminus S_i } (x) \sum_{s\in S_i^\mathrm{rev}} L_{i,s}(x) f(s) \Bigr) \cdot [1]_1 \nonumber \\
 & \qquad + \sum_{i=1}^n c^{i-1} V_{S\setminus S_i } (x) \sum_{s\in S_i^\mathrm{hid}} L_{i,s}(x) \bigl[ f(s) \bigr]_1 \nonumber
\end{align}
$$

[^msm]: Using the Schwartz–Zippel lemma, normally one would expect to see $3$ MSM terms here for each of the hidden $y_i$. Alin Tomescu suggested that since the base $[1]_1$ (and the additional base $[\xi]_1$ for hiding KZG variants) repeats, the corresponding scalars can be summed and this can be merged into one term.

Trisha Datta's approach is that the prover should only have to compute $\eqref{eq:eval}$. Namely, instead of committing to each secret $$y_i$$ individually, it gathers them into a vector $\mathbf{y} \mathrel{\vcenter{:}}= (y_1 ,\ldots, y_h)$ and commits to them all at once in one commitment $C_\mathbf{y}$, using some homomorphic vector commitment scheme (e.g., a hiding KZG variant). (A commitment is needed at the start of the protocol to prevent a possible grinding attack.) Then once the challenge point $x$ is known, it sends the element $\eqref{eq:eval}$ along with a sigma protocol proving that it knows the secret $\mathbf{y}$ giving $C_\mathbf{y}$ and $\eqref{eq:eval}$ and the image of the homomorphism $\varphi$. A commitment for $h$ elements usually has cost similar to that of computing an MSM of size $h$, so the cost of verifying this sigma protocol should be similar to that of computing an MSM of size $\operatorname{cost}(\varphi) + h$.

The following formal description should work in more generality than just the ordinary KZG scheme. Note we are assuming that the Fiat–Shamir transcript already contains the commitments $C_i$ of the $f_i$ and parameters for the $\mathsf{PCS}$.

### {% raw %} $$\textsf{PCS.BatchOpen}\bigl(\mathsf{prk}_\mathsf{PCS}, \\\{ S_i \\\}_i, \varphi; \\\{ f_i \\\}_{1 \leq i \leq n}, \\\{ \rho_i \\\}_{1 \leq i \leq n} \bigr) \rightarrow \bigl( \\\{ y_{i} \\\}_{i}, \mathrm{im}(\varphi), \pi \bigr)$$ {% endraw %}

> The prover batches multiple opening proofs at various points into one opening proof, and keeps some evaluations secret whilst revealing a relationship determined by the homomorphism $\varphi$.

**Step 1a:** Compute all evaluations $y_i$ and add those that are to be revealed to the Fiat–Shamir transcript, along with $S_i$.

**Step 1b:** Compute the commitment $C_\mathbf{y}$ to the remaining $y_i$ and $\mathrm{im}(\varphi)$ and add them to the Fiat–Shamir transcript.

**Step 1c:** $$c \xleftarrow{\mathcal{FS}} \mathbb{F}$$.

**Step 2a:** Compute $$q \mathrel{\vcenter{:}}= \frac{ \sum_{i = 1}^n c^{i-1} V_{S\setminus S_i }(X) \cdot \bigl( f_i (X) - g_i (X) \bigr)} {V_S (X)}$$.

**Step 2b:** Sample commitment randomness $$\rho_q \xleftarrow{\$} \mathcal{R}_\mathsf{Com}$$.

**Step 2c:** Compute the first proof $$ \pi_1 \leftarrow \textsf{PCS.Commit} ( \mathsf{prk}_\mathsf{PCS}, q; \rho_q )$$.

**Step 2d:** Add $\pi_1$ to the Fiat–Shamir transcript.

**Step 3:** $$x \xleftarrow{\mathcal{FS}} \mathbb{F}$$.

**Step 4a:** $f \leftarrow \sum_{i = 1}^n c^{i-1} V_{S\setminus S_i}(x) f_i - V_S(x) q$.

**Step 4b:** $\rho \leftarrow \sum_{i = 1}^n c^{i-1} V_{S\setminus S_i }(x) \rho_i - V_S(x) \rho_q$.

**Step 4c:** $$\pi_2 \leftarrow \textsf{PCS.Open}\bigl(\mathsf{prk}_\mathsf{PCS}, f, x; \rho)$$.

**Step 5a:** Compute $$C_\mathrm{eval} \mathrel{\vcenter{:}}= \bigl[ \sum_{i = 1}^n c^{i-1} V_{S\setminus S_i }(x) \cdot  g_i (x) \bigr]_1 $$

**Step 5b:** Compute the proof of knowledge $\pi_{\mathsf{PoK}}$.

**Step 6:** $\pi \leftarrow (\pi_1, \pi_2, C_\mathbf{y}, C_\mathrm{eval}, \pi_{\mathsf{PoK}})$.

### {% raw %} $$\textsf{PCS.BatchVerify}\bigl(\mathsf{vk}_\mathsf{PCS}, \\\{ S_i \\\}_i, \varphi, \\\{ C_i \\\}_i, \\\{ y_i \\\}_i,  \pi \bigr) \rightarrow \\\{0,1\\\} $$ {% endraw %}

> The verifier succinctly verifies this batch opening, as if only one verification is taking place, and also verifies the image of $\varphi$.

**Step 1a:** Parse the proof $(\pi_1, \pi_2, C_\mathbf{y}, C_\mathrm{eval}, \pi_{\mathsf{PoK}}) \leftarrow \pi$.

**Step 1b:** Add the $y_i$'s and $S_i$'s to the Fiat–Shamir transcript.

**Step 1c:** $$c \xleftarrow{\mathcal{FS}} \mathbb{F}$$.

**Step 2:** Add $\pi_1$ to the Fiat–Shamir transcript.

**Step 3:** $$x \xleftarrow{\mathcal{FS}} \mathbb{F}$$.

**Step 4a:** Compute $C_f \mathrel{\vcenter{:}}= \sum_i c^{i-1} V_{S\setminus S_i}(x) \, C_i - V_S (x) \, \pi_1 $.

**Step 4b:** $$\\\{0, 1\\\} \leftarrow \textsf{PCS.Verify}\bigl(\mathsf{vk}_\mathsf{PCS}, x, C_f, C_\mathrm{eval}, \pi_2)$$.

**Step 5:** Verify the proof of knowledge $\pi_{\mathsf{PoK}}$.

## Acknowledgements

Many thanks to Alin Tomescu for showing me how to efficiently batch the verification of sigma protocol proofs, and to Trisha Datta for carefully explaining how to batch PCS opening proofs, and for showing how to extend $$\mathtt{SHPLONK}$$ to the setting of the sumcheck protocol in $\textsf{DekartProof}$ and the hiding KZG scheme of **[ZGK+17, KT23]**.

## References

**[AJM+23]** Ittai Abraham, Philipp Jovanovic, Mary Maller, Sarah Meiklejohn, and Gilad Stern. "Bingo: Adaptivity and asynchrony in verifiable secret sharing and distributed key generation." In Annual International Cryptology Conference, pp. 39-70. Cham: Springer Nature Switzerland, 2023.

**[BDFG20]** Dan Boneh, Justin Drake, Ben Fisch, Ariel Gabizon. "Efficient polynomial commitment schemes for multiple points and polynomials." Cryptology ePrint Archive (2020).

**[Chunky]** https://alinush.github.io/chunky

**[GWC19]**  Ariel Gabizon, Zachary J. Williamson, and Oana Ciobotaru. "Plonk: Permutations over lagrange-bases for oecumenical noninteractive arguments of knowledge." Cryptology ePrint Archive (2019).

**[KT23]** Tohru Kohrita and Patrick Towa. "Zeromorph: Zero-Knowledge Multilinear-Evaluation Proofs from Homomorphic Univariate Commitments." Journal of Cryptology 37, no. 4 (2024): 38.

**[KZG10]** Aniket Kate, Gregory M. Zaverucha and Ian Goldberg. Constant-size commitments to polynomials and their applications. In ASIACRYPT, volume 6477 of Lecture Notes in Computer Science, pages 177–194. Springer, 2010.

**[MDR23]** Atsuki Momose, Sourav Das, and Ling Ren. "On the Security of KZG Commitment for VSS." In Proceedings of the 2023 ACM SIGSAC Conference on Computer and Communications Security, pp. 2561-2575. 2023.

**[Tha22]** Justin Thaler. "Proofs, arguments, and zero-knowledge." https://people.cs.georgetown.edu/jthaler/ProofsArgsAndZK.pdf

**[ZGK+17]** Yupeng, Zhang, Daniel Genkin, Jonathan Katz, Dimitrios Papadopoulos, and Charalampos Papamanthou. "A zero-knowledge version of vSQL." Cryptology ePrint Archive (2017).

