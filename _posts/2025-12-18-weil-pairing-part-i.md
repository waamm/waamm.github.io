---
title: "The Weil Pairing, Part I: Function Theory on Complex Tori"
author: waamm
date: 2025-12-18
categories: [Pure Mathematics, Elliptic Curves]
tags: [elliptic-curves, weil-pairing]
math: true
---

> “The Weil pairing, first introduced by André Weil in 1940, plays an important role in the theoretical study of the arithmetic of elliptic curves and Abelian varieties. It has also recently become extremely useful in cryptologic constructions related to those objects.”
>
> — **[Mil04]**

This quote by Victor Miller from his seminal 2004 paper[^miller] foreshadowed the emergence of what is today a fully fledged domain known as [pairing-based cryptography](https://en.wikipedia.org/wiki/Pairing-based_cryptography). Despite its significance—and despite cryptographers’ general inclination to dissect every construct they encounter—pairings are often treated as a black box, largely due to their technical complexity.

[^miller]: The main result of his paper actually dates back to an unpublished manuscript from 1986: [Short programs for functions on curves](https://drops.dagstuhl.de/storage/00lipics/lipics-vol291-fun2024/LIPIcs.FUN.2024.34/LIPIcs.FUN.2024.34.pdf)  

I recently spent some time studying the Weil pairing and decided to record some notes and reflections. In Weil’s original work **[Weil40]**, arising from his proof of [the Riemann hypothesis for curves over finite fields](https://en.wikipedia.org/wiki/Local_zeta_function#Riemann_hypothesis_for_curves_over_finite_fields), in Miller’s paper **[Mil04]**, and in many modern references (e.g., **[Cos, Lan87, Wa08, Sil09, Sut23]**), the pairing is defined roughly as follows:

**Notation ([Weil divisors](https://en.wikipedia.org/wiki/Divisor_(algebraic_geometry))).**  
A *divisor on an elliptic curve $E$* is a formal sum of points
$D=\sum_{P\in E} n_P [P]$ with $n_P \in \mathbb{Z}$, such that $n_P$
is nonzero for only finitely many $P$; this finite set of points
is referred to as its *support*, and its degree is defined as $\deg(D)\mathrel{\vcenter{:}}=\sum_{P \in E} n_{P}$.
 The *divisor $$\mathrm{div}(f) = \sum_{P \in E} \mathrm{ord}_P(f) \, [P]$$
of a rational function $f$ on $E$* records at each point $P$ the
order $$\mathrm{ord}_f(P)$$ of the zero (with a plus sign) or pole
(with a minus sign) of $f$ at $P$, and is zero otherwise. When $\mathrm{div}(f)$ and $D$ have disjoint support, we set 
$f(D)\mathrel{\vcenter{:}}= \prod_{P\in E} f(P)^{n_P}$, and when they are equal one says that $D$ is *principal*. Given a pair of divisors $P,Q$ on $E$, we write $P \sim Q$ if $P - Q$ is principal, and say that $P$ and $Q$ are *linearly equivalent*.
{: .box .notation }

> **Definition ([Weil pairing](https://en.wikipedia.org/wiki/Weil_pairing) [Wei40]).**  
> Let $E$ be an elliptic curve defined over a field $K$
> with identity element $O$, and pick an integer $n>0$ which is coprime
> to the characteristic $\mathrm{char}(K)$ of $K$ if $\mathrm{char}(K)>0$, and consider the
> $n$-torsion subgroup $E(K)[n]$. The Weil pairing is an alternating,
> bilinear, non-degenerate, Galois-invariant, and surjective form
> 
> $$
> \mathrm{Weil}_{n}:E(K)[n]\times E(K)[n]\longrightarrow\mu_{n}\mathrel{\vcenter{:}}=\{x\in K:x^{n}=1\}.
> $$
> 
> It is constructed for a pair of points $P,Q\in E(K)[n]$ as follows:
> pick divisors $D_{P}\sim[P]-[O]$ and $D_{Q}\sim[Q]-[O]$ with disjoint
> support. Then there exist functions $f_{P},f_{Q}$ with $\mathrm{div}(f_{P})=nD_{P}$
> and $\mathrm{div}(f_{Q})=nD_{Q}$, and we set
> 
> $$
> \mathrm{Weil}_{n}(P,Q)\mathrel{\vcenter{:}}=\frac{f_{P}(D_{Q})}{f_{Q}(D_{P})}.
> $$
{: .box .definition }

To me, this definition is far from enlightening. The functions $f_{P}$
and $f_{Q}$ are only defined up to multiplication by constants, so using them for evaluations
seems off.[^functions] Moreover, the choice of divisors
$D_{P}$ and $D_{Q}$ (and the use of linear equivalence more generally)
strongly suggest a deeper conneciton with the geometry of line bundles
on $E$ that is left implicit. Some texts (**[Wa08, Sil09]**) provide a second definition, yet it is no more illuminating. What, then, is the conceptual picture behind these constructions?

[^functions]: It works out here technically because the constants cancel out when evaluating a divisor of degree zero like $[P]-[O]$, but that is besides the point.

## The Complex Torus

I don't have access to Weil's original papers --- and it's generally discouraged to read them anyway because his language of algebraic geometry is too dated --- but I want to start with sketching some of the relevant theory over the complex numbers $\mathbb{C}$, which I believe was his point of entry.[^Wikipedia]

[^Wikipedia]: In fact, on [Wikipedia](https://en.wikipedia.org/wiki/Weil_pairing) it has said since 2009:
    > the corresponding results for elliptic functions *were known*, and can be expressed simply by use of the Weierstrass sigma function.

    Although we will indeed end up using Weierstrass σ-functions to show equivalence with the algebraic definition presented at the start of this post, the resulting formula is rather simple and there is no need to express the pairing in terms of functions, and I'm not sure why one would do that.

> **Definition ([lattices](https://en.wikipedia.org/wiki/Lattice_(group))).**  
> Let $n$ be a positive integer. A subset $\Lambda \subset \mathbb{R}^n$ is called a *(full) lattice* if it is a subgroup of $\mathbb{R}^n$ isomorphic to $\mathbb{Z}^{n}$.
{: .box .definition }

Identifying $\mathbb{C}^n \simeq \mathbb{R}^{2n}$, a lattice in $\mathbb{C}^n$ is a subgroup isomorphic to $\mathbb{Z}^{2n}$.

> **Example.**  
> A lattice $\Lambda \subset \mathbb{C}$ is a subgroup $\Lambda = \mathbb{Z} \omega_1 + \mathbb{Z} \omega_2 $ for a pair of elements $\omega_1,\omega_2 \in \mathbb{C}$ which are linearly independent over $\mathbb{R}$ (i.e., they do not lie on the same line through the origin).
{: .box .example }

An elliptic curve $E(K)$ over a field $K$ is typically defined (when
$\mathrm{char}(K)$ is not in $\\{2,3\\}$) as the set of zeroes of a short
Weierstrass equation $y^{2}=x^{3}+ax+b$ (with nonzero discriminant $4 a^3 + 27 b^2$)
over the plane $K^{2}$, together with a point $O$ at infinity. Focusing
on the complex numbers has the advantage that $E(\mathbb{C})$ can
be studied concretely as a [torus](https://en.wikipedia.org/wiki/Torus) $\mathbb{C}/\Lambda$,[^torus] for some lattice $\Lambda \subset \mathbb{C}$, with $O$ the zero element and
elliptic curve addition corresponding to ordinary addition on $\mathbb{C}$:

> **Theorem (the uniformization theorem for elliptic curves).**  
> Let $$E(\mathbb{C})$$ be an elliptic curve over the complex numbers. Then there exists a lattice $\Lambda \subset \mathbb{C}$ such that
> 
> $$
> E(\mathbb{C}) \simeq \mathbb{C} / \Lambda
> $$
> 
> as complex Lie groups.[^equivalence]
{: .box .theorem }

In this setting, torsion points $E(\mathbb{C})[n]$ and their properties
--- such as the canonical identification $E(\mathbb{C})[n] \simeq (\Lambda/n)/\Lambda \simeq(\mathbb{Z}/n\mathbb{Z})^{2}$
--- are straightforward to visualise:

[^torus]: We won't be using it explicitly in this post, but a lattice quotient $\mathbb{C}/\Lambda$ can be identified topologically with a torus, by manipulating the fundamental domain of $\mathbb{C}/\Lambda$ as follows: 
    
    ![img-description](assets/images/Torus_from_rectangle.gif)
    _After identifying opposite sides of a rectangle, it becomes a torus
    ([source](https://commons.wikimedia.org/wiki/File:Torus_from_rectangle.gif))_

[^equivalence]: This correspondence extends to an [equivalence of categories](https://en.wikipedia.org/wiki/Equivalence_of_categories).

![img-description](assets/images/Lattice_torsion_points_light.svg){: .light }
![img-description](assets/images/Lattice_torsion_points_dark.svg){: .dark }
_An elliptic curve $\mathbb{C}/\Lambda$ with its lattice $\Lambda$
generated by $\omega\_{1} = 1$ and $\omega\_{2} = 1/2 + 2i$, showing its 4-torsion subgroup of size $4^2$
([source](https://en.wikipedia.org/wiki/Complex_multiplication#/media/File:Lattice_torsion_points.svg))_

When searching for the complex-analytic analogue of the Weil pairing --- i.e., an explicit description of the pairing on a complex torus $\mathbb{C}/\Lambda$ --- I found that many texts simply state that the result is a skew-symmetric pairing or the exponential of one **[Gal05, Sil09, KR17]**, without explaining why this holds. The only source I found that sketches a derivation is **[Lan87, Appendix A]**, though the argument there is a bit terse; this post is devoted to giving a more detailed and more self-contained explanation, before extending that in the next blog post with line bundles.

My motivation here is that one of the first things I do when learning a new concept in algebraic
geometry is to explore its geometric interpretation, and I find that
this approach often clarifies many of the results that follow. For
example, I would have struggled to understand the definition and properties
of the [Zariski (co)tangent space](https://en.wikipedia.org/wiki/Zariski_tangent_space#Definition) without having seen in differential geometry the description of the tangent space in terms of differentials.
However, this only works when the definition at hand is close to its
geometric origins.

In this case, it turns out that naively complexifying the definition of the Weil pairing does *not* provide much insight --- and for good reason. In the next post, we’ll see that we should be looking at line bundles instead; evidently this pairing is really a product of 20th century geometry, rather than the 19th century developments in which much of the complex analytic theory of elliptic curves originated. Nevertheless, the resulting complex-analytic approach is quite elegant and will be reused in the next post, and I thought it might be worthwhile to record it for readers who are also curious for a quick derivation of the Weil pairing over $\mathbb{C}/\Lambda$.

Concretely, in the rest of this post we will:

1. Explain why divisors like $nD_{P}$ and $nD_{Q}$ are principal, by using them to explicitly construct certain functions on $\mathbb{C}$ and showing that these functions descend to the sought-after functions $f_{P}$ and $f_{Q}$ on $E(\mathbb{C})$.

3. Demonstrate that over $\mathbb{C}$ the Weil pairing $\mathrm{Weil}_{n}(\cdot,\cdot)$ takes the form

    $$(P,Q)\longmapsto\xi^{\langle P,Q \rangle}$$

    for the primitive $n$-th root of unity
    $\xi=e^{2\pi i/n}$ and a certain[^skew] skew-symmetric pairing $\langle \cdot,\cdot \rangle$
    coming from $\Lambda$.

[^skew]: More precisely, this is $n^2$ times the skew-symmetric pairing coming from the canonical principal polarisation; so in terms of that pairing $\langle \cdot ,\cdot \rangle$, it would be $(P,Q) \mapsto e^{2\pi i n \langle P, Q \rangle }$ instead.

Throughout the rest of this post, it is assumed that the reader is comfortable with the basic theory of complex analysis.

## Principal divisors

The complex analytic analogue of the rational functions $f_{P}$ and
$f_{Q}$ on an elliptic curve are certain [meromorphic functions](https://en.wikipedia.org/wiki/Meromorphic_function#On_Riemann_surfaces) on
a complex torus (this is part of a larger [principle](https://en.wikipedia.org/wiki/Algebraic_geometry_and_analytic_geometry)). 

> **Notation (Field of meromorphic functions).**  
> We will denote the field of meromorphic functions on a compact Riemann surface $S$
> by $K(S)$, and its subset of nonzero elements by $K(S)^\times$.
{: .box .notation }

Rather than studying these functions directly on
the torus $\mathbb{C}/\Lambda$, it is often more convenient (as we
will soon see) to pull them back to $\mathbb{C}$ along the universal
covering map 

$$
\mathbb{C}\twoheadrightarrow\mathbb{C}/\Lambda
$$

where we have access to a wider class of functions. Those meromorphic
functions on $\mathbb{C}$ that descend to the torus are naturally
characterised as follows:

> **Definition ([Elliptic functions](https://en.wikipedia.org/wiki/Elliptic_function)).**  
> A meromorphic function on the complex plane $\mathbb{C}$ is called
> *elliptic* (or *doubly-periodic*) *with respect to
> a lattice* $\Lambda$ if
> 
> $$
> f(z+\lambda)=f(z)\qquad\textrm{for all }\lambda\in\Lambda.
> $$
{: .box .definition }

Meromorphic functions on compact Riemann surfaces (and hence elliptic functions) form a remarkably rigid class:

> **Theorem (Liouville's theorem in terms of divisors).**  
> Meromorphic functions on compact Riemann surfaces are classified, up to scalar multiplication, by their divisors.
{: .box .theorem }

> *Proof:* 
> Let $S$ be a compact Riemann surface. Since $\mathrm{ord}_P(\cdot): K(S)^\times \rightarrow \mathbb{Z}$ is a homomorphism, the same is true for the coproduct of morphisms
> 
> $$
> \mathrm{div}(\cdot): K(S)^\times \longrightarrow \bigoplus_{P\in S} \mathbb{Z},\qquad f\longmapsto \bigl(\mathrm{ord}_P(f)\bigr)_{P\in S}.
> $$
> 
> (To put it more plainly, if $f$ and $g$ have the same divisor, then we want to use that $f/g$ has the trivial divisor.) Thus it suffices to show that a nonzero meromorphic function on a compact Riemann surface without zeroes or poles is constant, which is exactly [Liouville's theorem](https://en.wikipedia.org/wiki/Liouville%27s_theorem_(complex_analysis)#On_compact_Riemann_surfaces).
{: .box .proof }

Divisors are often simpler to handle than meromorphic functions, and this statement is often used to show that two meromorphic functions agree. On an elliptic curve, principal divisors can be described very explicitly:

> **Theorem (Abel's theorem for elliptic curves).**  
> Let $D$ be a divisor on an elliptic curve $E$ with identity $O$. Then $D=\sum_{P\in E}n_{P}[P]$
> is principal if and only if
> 
> $$
> \deg(D)\mathrel{\vcenter{:}}=\sum_{P\in E}n_{P}=0\qquad\textrm{and}\qquad\sum_{P\in E}n_{P}P=O.
> $$
{: .box .theorem }

>  **Example.** Let $D_{P}=[P]-[O]$ for a point $P$ in the $n$-torsion of $E$.
> Then both conditions hold for the divisor $nD_{P}$, so by the theorem there exists
> a meromorphic function $f_{P}$ on $\mathbb{C}/\Lambda$ with $\mathrm{div}(f_{P})=nD_{P}$.
{: .box .example }

{% comment %}

>  **Corollary.**
> Let $D$ be a divisor with degree zero on an elliptic curve. Then $D$ has degree zero if and only if $D \sim tau_R(D)\coloneqq$ for some point $R$ (uh wat als nul?), if and only if it holds for any point $R$.
> Let $Q,R$ be two points in an elliptic curve $E$. In particular, for any two points $Q, R$ in an elliptic curve we have $(Q)-(O)\sim(Q+R)-(R)$.
{: .box .corollary }

{% endcomment %}

Both of the identities in this theorem have analogues for arbitrary compact Riemann surfaces. The generalisation of the first identity is:

> **Proposition (the degree of a principal divisor is zero).**  
> Let $f$ be a nonzero meromorphic function on a compact Riemann surface
> $S$. Then $\deg\bigl(\mathrm{div}(f)\bigr)=0$.
{: .box .proposition }

The second statement extends [differently](https://en.wikipedia.org/wiki/Abel–Jacobi_map#Abel–Jacobi_theorem), since compact Riemann surfaces do not possess a group structure in general.

> **Remark**. The Weierstrass ℘-function has a double pole at the origin, so
> Abel's theorem implies that it should have two zeroes as
> well; it turns out these are quite nontrivial to describe explicitly **[EM81, DI08]**.
{: .box .remark }

The forward direction of the theorem can be proven directly (for $\mathbb{C}/\Lambda$)
as follows. Pull back a meromorphic function on $\mathbb{C}/\Lambda$ corresponding to $D$
along the covering map $\mathbb{C}\twoheadrightarrow\mathbb{C}/\Lambda$
to obtain an elliptic function $f$ on $\mathbb{C}$. Let $\gamma$
denote the loop running over the sides of a fundamental parallelogram
(slightly shifted if a zero or pole lies on one of its sides). Then the residue
theorem implies that the two identities reduce to showing

$$  
\frac{1}{2\pi i}\oint_{\gamma}\frac{f'(z)}{f(z)}\mathrm{d}z=0,\qquad\textrm{and}\qquad\frac{1}{2\pi i}\oint_{\gamma}z\frac{f'(z)}{f(z)}\mathrm{d}z\in\Lambda.
$$

## Weierstrass σ-functions

The converse of the theorem can be proved indirectly using a Riemann–Roch
style induction. However, we'd prefer a more explicit construction of the
meromorphic function corresponding to a given divisor.

A natural first attempt at constructing an elliptic function on $\mathbb{C}$
might be to consider the infinite product 

$$
\prod_{\lambda\in\Lambda}(z-\lambda),
$$

 and then note that it has to "shrink" substantially to have any chance of converging.
Removing a large factor, Eisenstein examined the series

$$
z\prod_{\lambda\in\Lambda^{\times}}\left(1-\frac{z}{\lambda}\right) = z \exp\left(\sum_{\lambda\in\Lambda^{\times}}\log(1-\frac{z}{\lambda})\right),\qquad\textrm{where }\Lambda^{\times}\mathrel{\vcenter{:}}=\Lambda \backslash \{0\},
$$

and showed that it converges [conditionally](https://en.wikipedia.org/wiki/Conditional_convergence), but not [absolutely](https://en.wikipedia.org/wiki/Absolute_convergence) **[Eis47]**.[^absolutely] Expanding the Newton–Mercator series

[^absolutely]: Absolute convergence would mean that $\sum_{\lambda\in\Lambda^{\times}}\log(1-\frac{z}{\lambda})$ converges absolutely. For sufficiently small $a$ we have $\log(1-a)\sim-a$, so then $\sum_{\lambda\in\Lambda^{\times}}\frac{1}{|\lambda|}$ converges, but this is false for any lattice: the number of lattice points $\lambda$ with $|\lambda|\leq R$ grows like $cR^{2}$, hence
    $$
    \sum_{|\lambda|\leq R}\frac{1}{|\lambda|}\sim\int_{1}^{R}\frac{r^{2}}{r}\mathrm{d}r=\frac{R^{2}-1}{2}.
    $$

$$
\log(1-\frac{z}{\lambda})=-\frac{z}{\lambda}-\frac{1}{2}\frac{z^{2}}{\lambda^{2}}-\frac{1}{3}\frac{z^{3}}{\lambda^{3}}-\cdots,
$$

in this product, one sees that eliminating the first two terms is
enough to obtain absolute convergence. This can be achieved by inserting
a suitable exponential factor: 

> **Definition ([Weierstrass σ-function](https://en.wikipedia.org/wiki/Weierstrass_functions#Weierstrass_sigma_function) [Wei93]).**  
> Given a lattice $\Lambda$ in $\mathbb{C}$, the *Weierstrass
> σ-function* is the meromorphic function defined on $\mathbb{C}$ as
> 
> $$
> \sigma(z;\Lambda)=z\prod_{\lambda\in\Lambda^{*}}\left(1-\frac{z}{\lambda}\right)\exp\left(\frac{z}{\lambda}+\frac{1}{2}\left(\frac{z}{\lambda}\right)^{2}\right).
> $$
{: .box .definition }

It has a simple zero at each lattice point, and no poles since it converges absolutely.

> **Example.**  
> Let $$\Lambda= \langle \omega_{1}, \omega_{2} \rangle$$ be the lattice generated by $\omega\_{1} = 1$ and $\omega\_{2} = 1/2 + 2i$. Consider the Weierstrass sigma function $$\sigma(z;\Lambda)$$ on the square region $$[-3.5, 3.5] \times [-3.5, 3.5]$$ in the complex plane. On the horizontal line through the origin there are 7 zeroes at $$-3,-2,-1,0,1,2,3$$, and there are two more rows of zeroes at the horiziontal lines through $\omega\_{2}$ and $- \omega\_{2}$:
> 
> ![img-description](assets/images/Weierstrass_sigma_function.png)
> _[Domain colouring](https://en.wikipedia.org/wiki/Domain_coloring) plot of the Weierstrass σ-function with fundamental periods $\omega\_{1} = 1$ and $\omega\_{2} = 1/2 + 2i$ on the square region $$[-3.5, 3.5] \times [-3.5, 3.5]$$.
> ([source code](/assets/source-code/Weierstrass_sigma_function.py))_
{: .box .example }

Observe that $\sigma(-z;\Lambda)=-\sigma(z;\Lambda)$, which follows
from $-\Lambda^* = \Lambda^*$. This is not an elliptic function (as the image of its plot already shows):[^theta]

[^theta]: Instead it's an example of a [theta function](https://en.wikipedia.org/wiki/Theta_function), as we'll see in the next post.

> **Proposition (Quasi-periodicity of σ-functions).**  
> There exists a linear map[^eta] $\lambda\mapsto\eta_{\lambda}$, meaning
> $\eta_{\lambda+\lambda'}=\eta_{\lambda}+\eta_{\lambda'}$ for all $\lambda,\lambda'\in\Lambda$, such that
>
> $$
> \sigma(z+\lambda)=-e^{\eta_{\lambda}(z+\lambda/2)}\sigma(z)
> $$
>
> for all $\lambda\in\Lambda$.
{: .box .proposition }

[^eta]: This is called the [Weierstrass η-function](https://en.wikipedia.org/wiki/Weierstrass_functions#Weierstrass_eta_function).

This statement has a natural interpretation in terms of line bundles, as we'll see in the next post.

> *Proof sketch:* The logarithmic derivative $\zeta(z)\mathrel{\vcenter{:}}=\sigma'(z)/\sigma(z)$
> of the Weierstrass σ-function is the Weierstrass ζ-function, and the derivative of that is minus
> the Weierstrass ℘-function. Since the Weierstrass ℘-function
> is elliptic, it follows that $\zeta(z+\lambda)-\zeta(z)$ is a constant
> $\eta_{\lambda}$ for fixed $\lambda$. This equation also yields linearity:
> 
> $$
> \eta_{\lambda+\lambda'}=\zeta(z+\lambda+\lambda')-\zeta(z)=\zeta(z+\lambda+\lambda')-\zeta(z+\lambda)+\zeta(z+\lambda)-\zeta(z)=\eta_{\lambda'}+\eta_{\lambda}
> $$
>
> for any $\lambda,\lambda'\in\Lambda$.
{: .box .proof }

Nevertheless, we will use these non-elliptic functions to construct elliptic ones:

> **Theorem (Abel's theorem for complex elliptic curves in terms of σ-functions)**  
> Any elliptic function $f$ on $\mathbb{C}$ with zeroes $a_{i}$ and poles $b_{i}$
> in $\mathbb{C}/\Lambda$ can be written as
> 
> $$
> f(z)=c\prod_{i=1}^{n}\frac{\sigma(z-\tilde{a}_{i})}{\sigma(z-\tilde{b}_{i})},
> $$
> 
> for some constant $c$ and choice of elements $\tilde{a}_i,\tilde{b}_i$
> satisfying:
> 
> * $\tilde{a}_i\equiv a_i\mod{\Lambda}$, and
> 
> * $\tilde{b}_i\equiv b_i\mod{\Lambda}$, and
> 
> * $\sum_{i=1}^n {\tilde a_i} = \sum_{i=1}^n {\tilde b_i}$,
>
> and conversely such functions are elliptic.
{: .box .theorem }

> **Example.**  
> Continuing from the previous example, again consider the lattice $$\Lambda= \langle \omega_{1}, \omega_{2} \rangle$$ with $\omega\_{1} = 1$ and $\omega\_{2} = 1/2 + 2i$. The points 
>
> $$
> \tilde a_1 = \tilde a_2 = \omega_{1} / 2 + \omega_{2}/2,\qquad \tilde b_1 = 0
> $$ 
> 
> satisfy the conditions of the theorem. Therefore, the formula given there should yield an elliptic function with respect to $$\Lambda$$. In other words, the function is expected to be periodic with respect to shifts by the fundamental parallelogram with corners 
> 
> $$
> 0, \qquad \omega_{1}, \qquad \omega_{2}, \qquad \omega_{1} + \omega_{2},
> $$
>
> which are marked by the pole at $\tilde b_1 = 0$. Inside the parallelogram there will be a (double) zero at $\tilde a_1$ and and additional pole at $2 \tilde a_1$.
> 
> ![img-description](assets/images/Elliptic_function.png)
> _[Domain colouring](https://en.wikipedia.org/wiki/Domain_coloring) plot of this elliptic function with $\tilde a_1 = \tilde a_2 = \omega\_{1}/2 + \omega\_{2}/2, \tilde b_1 = 0, c = 1$, for fundamental periods $\omega\_{1} = 1$ and $\omega\_{2} = 1/2 + 2i$, on the square region $$[-3.5, 3.5] \times [-3.5, 3.5]$$.
> ([source code](/assets/source-code/Elliptic_function.py))_
{: .box .example }

Again, we are constructing functions on $E(\mathbb C)$ through the covering map $\mathbb{C}\twoheadrightarrow\mathbb{C}/\Lambda$, which does not exist over arbitrary fields; although this theorem still holds in that generality, it is not possible to explicitly construct a function associated to a divisor this directly.

> *Proof:* By Abel's theorem, the number of zeroes and poles indeed agree, and
> we have $\sum_{i=1}^n a_i \equiv \sum_{i=1}^n b_i$ modulo $\Lambda$.
> Thus the existence of these $\tilde a_i,\tilde b_i$ follows. 
> Now denote the right-hand-side for $c=1$ by $g(z)$; it is elliptic,
> since for any $\omega$ in $\Lambda$ we have
> \begin{align}
> g(z + \omega) &= \prod_{i=1}^n  \frac{\sigma(z+\omega-{\tilde a_i})}{\sigma(z+\omega-{\tilde b_i})} \nonumber \\\\\
> &= \prod_{i=1}^n \frac{-e^{\eta_\omega (z-{\tilde a_i} + \omega / 2)} \sigma(z- {\tilde a_i})}{-e^{\eta_{\omega}(z-{\tilde b_i} + \omega / 2)}\sigma ( z - {\tilde b_i} ) } \nonumber \\\\\
> & =g(z)\prod_{i=1}^n e^{\eta_{\omega}({\tilde b_i}-{\tilde a_i})} \nonumber \\\\\
> & =g(z)e^{\eta_{\omega}\sum_{i=1}^n ({\tilde b_i}-{\tilde a_i})}=g(z). \nonumber
> \end{align}
>
> Since $f(z)$ and $g(z)$ are both elliptic functions and have the
> same divisor, Liouville's theorem implies that they are equal, up to a
> constant.
{: .box .proof }

Now for arbitrary points $P,Q,R$ in $E(\mathbb{C})[n]=(\Lambda/n)/\Lambda$
consider the divisors $D_{P}=(P)-(O)$ and $D_{Q}=(Q+R)-(R)$; we
will assume that $P,Q,R$ are chosen so that their support is disjoint. For any choice of lifts $\tilde{P},\tilde{Q},\tilde{R}$
in $\mathbb{C}$, the functions

$$
f_{P}(z)=\frac{\sigma(z-\tilde{P})^{n}}{\sigma(z)^{n-1}\sigma(z-n\tilde{P})}\qquad\textrm{and}\qquad f_{Q}(z)=\frac{\sigma(z-\tilde{Q}-\tilde{R})^{n}}{\sigma(z-\tilde{R})^{n-1}\sigma(z-\tilde{R}-n\tilde{Q})}
$$

are elliptic on $\mathbb{C}$ by the theorem, and they have divisors $nD_{P}$ and $nD_{Q}$ when considered as functions on
the complex torus. Setting $\mathrm{Weil}_n (P,Q) \mathrel{\vcenter{:}}= f_P (D_Q)/f_Q (D_P )$ as before,
we find

> **Lemma.**  
> The value $$\mathrm{Weil}_n (P,Q) $$ is given by $ e^{\eta_{n {\tilde P}} {\tilde Q} - \eta_{n {\tilde Q}} {\tilde P} } $.
{: .box .lemma }

> *Proof:* In evaluating points on $\mathbb{C} / \Lambda$ via σ-functions we have to choose lifts again; it seems plausible that choosing the same lifts $\tilde{P},\tilde{Q},\tilde{R}$ (and similarly for $O$ and $Q+R$) will lead to the simplest formulas. By definition then,
> 
> $$
> f_{P}(D_{Q})=\frac{\sigma(\tilde{Q}+\tilde{R}-\tilde{P})^{n}\sigma(\tilde{R})^{n-1}\sigma(\tilde{R}-n\tilde{P})}{\sigma(\tilde{Q}+\tilde{R})^{n-1}\sigma(\tilde{Q}+\tilde{R}-n\tilde{P})\sigma(\tilde{R}-\tilde{P})^{n}}
> $$
> 
> and
> 
> $$
> f_{Q}(D_{P})=\frac{\sigma(\tilde{P}-\tilde{Q}-\tilde{R})^{n}\sigma(-\tilde{R})^{n-1}\sigma(-\tilde{R}-n\tilde{Q})}{\sigma(\tilde{P}-\tilde{R})^{n-1}\sigma(\tilde{P}-\tilde{R}-n\tilde{Q})\sigma(-\tilde{Q}-\tilde{R})^{n}},
> $$
> 
> so
> \begin{align}
> \frac{f_P(D_Q)}{f_Q(D_P)} & =(-1)^{3n} (-1)^{n-1} \frac{\sigma({\tilde R}-n{\tilde P})\sigma({\tilde P}-{\tilde R}-n{\tilde Q})\sigma({\tilde Q}+{\tilde R})}{\sigma({\tilde Q}+{\tilde R}-n{\tilde P})\sigma({\tilde P}-{\tilde R})\sigma(-{\tilde R}-n{\tilde Q})} \nonumber \\\\\
>  & =-\frac{\sigma(\tilde{R}-n\tilde{P})}{\sigma(-\tilde{R}-n\tilde{Q})}\frac{\sigma(\tilde{P}-\tilde{R}-n\tilde{Q})}{\sigma(\tilde{P}-\tilde{R})}\frac{\sigma(\tilde{Q}+\tilde{R})}{\sigma(\tilde{Q}+\tilde{R}-n\tilde{P})} \nonumber \\\\\
>  & =-(-1)^{4}\frac{e^{-\eta_{n\tilde{P}}(\tilde{R}+n\tilde{P}/2)}\sigma(\tilde{R})}{e^{-\eta_{n\tilde{Q}}(-\tilde{R}+n\tilde{Q}/2)}\sigma(-\tilde{R})}\frac{e^{-\eta_{n\tilde{Q}}(\tilde{P}-\tilde{R}+n\tilde{Q}/2)}\sigma(\tilde{P}-\tilde{R})}{\sigma(\tilde{P}-\tilde{R})}\frac{\sigma(\tilde{Q}+\tilde{R})}{e^{-\eta_{n\tilde{P}}(\tilde{Q}+\tilde{R}+n\tilde{P}/2)}\sigma(\tilde{Q}+\tilde{R})} \nonumber \\\\\
>  & =e^{-\eta_{n\tilde{P}}(\tilde{R}+n\tilde{P}/2)-\eta_{n\tilde{Q}}(\tilde{P}-\tilde{R}+n\tilde{Q}/2)+\eta_{n\tilde{Q}}(-\tilde{R}+n\tilde{Q}/2)+\eta_{n\tilde{P}}(\tilde{Q}+\tilde{R}+n\tilde{P}/2)} \nonumber \\\\\
>  & =e^{\eta_{n\tilde{P}}\tilde{Q}-\eta_{n\tilde{Q}}\tilde{P}}. \nonumber
> \end{align}
{: .box .proof }

> **Corollary.**  
> Now write $\tilde{P}=a\omega_{1}/n+b\omega_{2}/n$ and $\tilde{Q}=c\omega_{1}/n+d\omega_{2}/n$,
> for some fundamental periods $\omega_{1},\omega_{2}$ with imaginary part
> $\Im(\omega_{2}/\omega_{1})>0$, and $\xi \mathrel{\vcenter{:}}= e^{2\pi i/n}$. Then
> 
> $$
> \mathrm{Weil}_n (P,Q)=- e^{2\pi i(ad-bc)/n} = \xi^{ad - bc}.
> $$
{: .box .corollary }

> *Proof:* After using linearity of $\omega\mapsto\eta_{\omega}$ and expanding 
> 
> \begin{align}
> (\eta_{n\tilde{P}}\tilde{Q}-\eta_{n\tilde{Q}}\tilde{P})n & =(a\eta_{1}+b\eta_{2})(c\omega_{1}+d\omega_{2})-(c\eta_{1}+d\eta_{2})(a\omega_{1}+b\omega_{2}) \nonumber \\\\\
 & =(ad-bc)(\eta_{1}\omega_{2}-\eta_{2}\omega_{1}), \nonumber
> \end{align}
> 
> this follows from [Legendre's relation](https://en.wikipedia.org/wiki/Legendre%27s_relation#Elliptic_functions).
{: .box .proof }

## References

{% comment %}
... Guide to Pairing-Based Cryptography
{% endcomment %}

**[Cos]** Craig Costello, *Pairings for Beginners*.
Available at: <https://static1.squarespace.com/static/5fdbb09f31d71c1227082339/t/5ff394720493bd28278889c6/1609798774687/PairingsForBeginners.pdf>

**[DI08]** W. Duke and Ö. Imamoḡlu. "The zeros of the Weierstrass ℘–function and hypergeometric series." Mathematische Annalen 340.4 (2008): 897-905.

**[Eis47]** G. Eisenstein, . "Beiträge zu Theorie der elliptischen Functionen. VI. Genaue Untersuchungen der unendlichen Doppelproducte, aus welchen die elliptischen Functionen als Quotienten zusammengesetzt sind, und der mit ihnen zusammen." Journal für die reine und angewandte Mathematik 35 (1847): 185-274.

**[EM81]** M. Eichler and D. Zagier. "On the Zeros of the Weierstrass ℘-Function." Mathematische Annalen 258 (1981): 399-408.

**[Gal05]** Steven D. Galbraith. "The Weil pairing on elliptic curves over $\mathbb{C}$." Cryptology ePrint Archive (2005). Available at: <https://eprint.iacr.org/2005/323.pdf>

**[Lan87]** Serge Lang, *Elliptic Functions*, 2nd edition, Springer GTM 112, New York, 1987.

**[Mil86]** Victor S. Miller, “Short programs for functions on curves,” unpublished manuscript, 1986.
Available at: <https://crypto.stanford.edu/miller/miller.pdf>

**[Mil04]**  Victor S. Miller, “The Weil pairing, and its efficient calculation,” 
Journal of Cryptology 17 (2004), 235–261.

**[RS17]** Kenneth A. Ribet and William A. Stein. *Lectures on Modular Forms and Hecke Operators*. Available at:
<https://www.wstein.org/books/ribet-stein/main.pdf>

**[Sil09]** Joseph H. Silverman. The Arithmetic of Elliptic Curves. Vol. 106. New York: Springer, 2009.

**[Sut23]** Andrew Sutherland (2023). 18.783 – Elliptic curves [Lecture notes]. Massachusetts Institute of Technology. Available at: https://math.mit.edu/classes/18.783/2023/

**[Wa08]** Lawrence C. Washington. Elliptic curves: number theory and cryptography. Chapman and Hall/CRC, 2008.

**[Wei40]** André Weil, “Sur les fonctions algébriques à corps de constantes finis,” 
C. R. Acad. Sci. Paris 210 (1940), 592–594.

**[Wei93]** K. Weierstrass. "Formeln und Lehrsätze zum Gebrauche der elliptischen Functionen." Formeln und Lehrsätze zum Gebrauche der elliptischen Functionen. Berlin, Heidelberg: Springer Berlin Heidelberg, 1893. 1-96.