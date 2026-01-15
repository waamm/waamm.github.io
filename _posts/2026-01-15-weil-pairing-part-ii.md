---
title: "The Weil Pairing, Part II: Line Bundles on Complex Tori"
author: waamm
date: 2026-01-15
categories: [Pure Mathematics, Elliptic Curves]
tags: [elliptic-curves, weil-pairing]
math: true
---

> "My mathematics work is proceeding beyond my wildest hopes, and I am even a bit worried --- if it's only in prison that I work so well, will I have to arrange to spend two or three months locked up every year?"
> 
> — André Weil, letter to his wife Eveline from Rouen Prison, 7 April 1940 (around the time he discovered the Weil pairing and proved the Riemann hypothesis for curves over finite fields) **[Wei92, p. 146]**[^Cartan]

[^Cartan]: According to the same autobiography, Cartan wrote to Weil during his imprisonment that "We're not all lucky enough to sit and work undisturbed like you".

In the [previous post](/posts/weil-pairing-part-i/) we remarked that in order to understand the nature of the Weil pairing, we should probably be using line bundles instead of functions. From this perspective, it is only a small step to pass from elliptic curves to [abelian varieties](https://en.wikipedia.org/wiki/Abelian_variety) and to consider line bundles on those instead. This additional generality hopefully helps clarify which features of the construction are essential and which are merely incidental.

But properly constructing the Weil pairing in such generality requires PhD-level algebraic geometry, which I would like to avoid. Instead, we will try keep the main *statements* at roughly the same level of generality, whilst specialising the field to $K = \mathbb{C}$.[^fields] As we saw in the previous post, this simplification allows us to bring in powerful analytic tools --- there, it was the Weierstrass σ-function; here, it will be the Appell–Humbert theorem. I have not seen this approach written out elsewhere,[^Edixhoven] and I hope it may serve as a light introduction even for readers who already have the requisite mathematical background.

[^fields]: Proofs for more general fields are beyond the scope of these posts; but if the reader has the required background, they appear in standard references on abelian varieties like **[Mum74]** and **[Bha17]**, and some of them reappear on Akhil Mathew's [blog](https://amathew.wordpress.com/tag/line-bundles/).

[^Edixhoven]:
    For example, **[Edi02]** is a bit terse in developing the required geometric background (it was written for a very different audience) and when it finally develops the pairing it simply says
    
    > et est muni d’une action

    Most of this post is dedicated to explaining this action in more detail.



## Line bundles

As mentioned in the previous post, the definition of the Weil pairing as usually presented very much indicates a strong connection with line bundles, despite not using that language at all. This is presumably for simplicity --- line bundles don't help with concrete computations and require more abstraction --- but at the very least I believe they do help explain why the Weil pairing exists and what kind of properties one would expect it to have.

Line bundles are generalised by [vector bundles](https://en.wikipedia.org/wiki/Vector_bundle) and those are further generalised by [fibre bundles](https://en.wikipedia.org/wiki/Fiber_bundle); these concepts are pervasive both throughout geometry, providing powerful invariants, and throughout modern [physics](https://ncatlab.org/nlab/show/fiber+bundles+in+physics). Line bundles are also responsible for the group law on elliptic curves.

> **Definition (fibres).**  
> Given a continous map $$\pi: E\rightarrow B$$ of topological spaces, the *fibre* of $$\pi$$ over an element $$b$$ in $$B$$ is the subspace $$\pi^{-1}(b)$$ of $$E$$ that maps to $$b$$.
{: .box .definition }

Intuitively, a fibre bundle is a continuous surjective map $$\pi : E \rightarrow B$$ of topological spaces, where each fibre is homeomorphic to the same space $$F$$, and furthermore in small regions of $$E$$ this map looks like the standard projection $$\mathrm{proj}_1: B \times F \rightarrow B$$ onto the first component. More formally:[^tao]

> **Definition (fibre bundles).**  
> A fibre bundle consists of a 4-tuple $$(E, B, \pi , F)$$, where $$E, B, F$$ are topological spaces (called the *total space*, *base space* and *fibre* respectively) and $$\pi: E\rightarrow B$$ is a continuous surjection
> satisfying *local triviality*, meaning that any point in $$B$$ has an open neighbourhood $$U$$ and homeomorphism $$\varphi: \pi^{-1}(U) \rightarrow U \times F$$
> such that the following diagram commutes:
> 
> ![img-description](assets/img/weil-pairing-part-ii/Fibre_bundle_local_trivial_light.svg){: .light }
> ![img-description](assets/img/weil-pairing-part-ii/Fibre_bundle_local_trivial_dark.svg){: .dark }
> _<span class="light">Local triviality of a fibre bundle over a neighbourhood $$U$$.</span><span class="dark">Local triviality of a fibre bundle over a neighbourhood $$U$$.</span>_
> 
> We will sometimes simply say that $$\pi: E\rightarrow B$$ is a fibre bundle, omitting $$F$$ from notation, or that it is an *$$F$$-bundle*. The fibre above a point $$b$$ is sometimes denoted $$F_b$$. When $$F$$ is a vector space and we can choose these *local trivializations* $$\varphi$$ such that the restriction of $$\varphi$$ to all fibres $$ \pi^{-1}(b) \simeq F$$ is a linear isomorphism, this is called a vector bundle. When the vector space $$F$$ is furthermore a line, i.e. is one-dimensional, it's called a *line bundle*.
{: .box .definition }

The linear isomorphism requirement for vector bundles actually comes for free:

> **Remark (fibre bundles with vector space fibres).**  
> If the fibres of a fibre bundle can be identified (topologically) with a vector space, then one can choose the local trivialisations to be linear isomorphisms, i.e. the fibre bundle is fact a vector bundle [Ste60].
{: .box .remark }

$$S^1$$-bundles are the natural geometric setting for [electromagnetism](https://en.wikipedia.org/wiki/Circle_bundle#Relationship_to_electrodynamics). Given any base space $$B$$ and fibre $$F$$, we can construct at least one fibre bundle:

> **Example (trivial bundle).**  
> Given any pair of topological spaces $$B$$ and $$F$$, the *trivial bundle* $$\mathrm{proj}_1: B \times F \rightarrow B$$ is a fibre bundle.
{: .box .example }

So if $$B = \mathbb{R}$$ and $$F = I \mathrel{\vcenter{:}}= [-1,1] \subset \mathbb{R}$$, the bundle morphism $$\pi: E = \mathbb{R} \times I \rightarrow \mathbb{R}$$ looks like flattening an infinitely long strip into an infinitely long line. 

> **Example (covering space as fibre bundle).**  
> A [covering space](https://en.wikipedia.org/wiki/Covering_space) is a fibre bundle with discrete fibre.
{: .box .example }

### The Möbius bundle

Now let's have a look at a more instructive example. Consider the lattice $\mathbb{Z}$ inside of $$\mathbb{R}$$; as we already mentioned in the previous post, its quotient $$\mathbb{R} /\mathbb{Z}$$ can be identified with the circle $S^1$.

> **Example (Two bundles over the circle $$S^1$$).**  
> Over $$B = S^1$$ with $$F = I \mathrel{\vcenter{:}}= [-1,1]$$, the trivial bundle geometrically looks like a ring (or cylinder). On the other hand, the Möbius strip can also be interpreted as a fibre bundle (called the *Möbius bundle*) with the same base space and fibre:
> ![img-description](assets/img/weil-pairing-part-ii/g9008_light.svg){: .light }
> ![img-description](assets/img/weil-pairing-part-ii/g9008_dark.svg){: .dark }
> _<span class="light">The Möbius strip as a fibre bundle, showing a fibre $$F_y$$ over a point $$y \in S^1$$ and a local trivalisation $$\phi_\alpha$$ over an open subset $$U_\alpha$$.</span><span class="dark">The Möbius strip as a fibre bundle, showing a fibre $$F_y$$ over a point $$y \in S^1$$ and a local trivalisation $$\phi_\alpha$$ over an open subset $$U_\alpha$$.</span>
> ([source](https://www.emanuelmalek.com/Teaching/Modave/LectureNotesFinal.pdf))_
{: .box .example }

This example perhaps helps to explain the old name
“twisted product” for fibre bundles. We can construct both of these bundles through the universal covering map

$$
\mathbb{R}\twoheadrightarrow\mathbb{R}/ \mathbb{Z}
$$

as follows: 

> **Example (Two bundles over the circle $$S^1$$, again).**  
> By definition, the identification $$\mathbb{R} /\mathbb{Z} \simeq S^1$$ is the result of quotienting the following equivalence relation on $\mathbb{R}$:
>
>$$ 
>x \sim x'\quad \textrm{ for }x,x' \in \mathbb{R},\qquad\textrm{if and only if}\qquad x = x'+n\textrm{ for some }n \in \mathbb{Z}.
>$$
> 
> Extending this to
>
>$$ 
>(x,y) \sim (x',y')\quad \textrm{ for }x,x' \in \mathbb{R}\textrm{ and }y,y' \in I,\qquad\textrm{if and only if}\qquad (x,y) = (x'+n,y')\textrm{ for some }n \in \mathbb{Z},
>$$
> 
> the quotient of the trivial bundle $$\mathbb{R} \times F$$ (an infinitely long strip) under this relation is naturally identified with the trivial bundle $$S^1 \times F$$ (a ring). The Möbius bundle is similarly obtained, by instead setting
>
>$$ 
>(x,y) \sim (x',y')\quad \textrm{ for }x,x' \in \mathbb{R}\textrm{ and }y,y' \in I,\qquad\textrm{if and only if}\qquad (x,y) = (x'+n,(-1)^n y')\textrm{ for some }n \in \mathbb{Z}.
>$$
> 
> ![img-description](assets/img/weil-pairing-part-ii/g70115_light.svg){: .light }
> ![img-description](assets/img/weil-pairing-part-ii/g70115_dark.svg){: .dark }
> _<span class="light">Quotienting a trivial bundle on $\mathbb{R}$ to obtain the Möbius bundle on $S^1$.</span><span class="dark">Quotienting a trivial bundle on $\mathbb{R}$ to obtain the Möbius bundle on $S^1$.</span>
> ([source](https://link.springer.com/book/10.1007/978-1-4419-9982-5))_
{: .box .example }

The pair of maps $$(q,\varepsilon)$$ in the last image is an example of


> **Definition (bundle morphism).**  
> Given any pair of fibre bundles $$\pi: E\rightarrow B$$ and $$\pi: E'\rightarrow B'$$, a *bundle morphism* is a pair of continuous maps $$(\varphi, f)$$ such that the following diagram commutes:
> 
> ![img-description](assets/img/weil-pairing-part-ii/bundle_morphism_light.svg){: .light }
> ![img-description](assets/img/weil-pairing-part-ii/bundle_morphism_dark.svg){: .dark }
> _<span class="light">A morphism between two fibre bundles.</span><span class="dark">A morphism between two fibre bundles.</span>_
{: .box .definition }

We will then say that a fibre bundle is *trivial* if it is isomorphic to a trivial bundle.

### Tangent bundles

Although we use it in this post only as an interesting vector bundle to demonstrate sections and illustrate pullbacks, one of the most important examples of a vector bundle is:

> **Proposition (tangent bundle).**  
> The set $$TM$$ of all tangent spaces to all points of a manifold $$M$$ can naturally be given the structure of a vector bundle $$\pi: TM \rightarrow M$$, called the *[tangent bundle](https://en.wikipedia.org/wiki/Tangent_bundle)*.
{: .box .proposition }

In general this vector bundle is not trivial; for even-dimensional spheres $M = S^{2n}$ this follows from the [hairy ball theorem](https://en.wikipedia.org/wiki/Hairy_ball_theorem). But for $M = \mathbb{R}^n$ and $M = S^1$ it is:

> **Proposition (tangent bundle to a Lie group is trivial).**  
> The tangent bundle to a Lie group is trivial.
{: .box .proposition }

### Sections

An analogy I like is that you can only understand a physical system by taking measurements --- if a topological space is the phase space of such a system, measurements correspond to *functions* on that space. Line bundles can be thought of as yielding "generalised functions", as follows:

> **Definition (bundle section).**  
> Given a fibre bundle $$\pi: E\rightarrow B$$, a *(global) section* is a continuous right inverse of $\pi$.
{: .box .definition }

A vector bundle always has a section:

> **Example (zero section).**  
> Given a vector bundle, the map which sends an element in the base space to the zero element in its fibre is a section, called the *zero section*.
{: .box .example }

Since constant maps are continuous, so does a trivial bundle:

> **Example.**  
> For a trivial bundle $$\pi: B \times F \rightarrow B$$, a section is the same as a continuous map $$B \rightarrow F$$.
{: .box .example }

So for the trivial line bundle on a manifold $$M$$, a section is the same as a function on $$M$$.

Fibre bundles do not admit global sections in general, see e.g. the $$\mathbb{Z}/2\mathbb{Z}$$ bundle [here](https://commons.wikimedia.org/wiki/File:Z2_principal_bundle_over_circle.png): if a section were to map a base element to some element in a fibre, then by continuity the rest of the image of the section is fixed to its neighbouring elements, but if you walk around the circle you end up at the other element.

> **Definition (bundle section).**  
> Given a fibre bundle $$\pi: E\rightarrow B$$, a *local section* is a section of the restriction $\pi: \pi^{-1}(U) \rightarrow U$ of the fibre bundle to an open subset $U$ of $$B$$. The set of sections over an open subset $U$ will be denoted by $\Gamma(E, U)$.
{: .box .definition }

As we've already seen, these always exist over a local trivialisation.

> **Example (vector fields as sections).**  
> On a manifold $$M$$, a vector field is the same as a section of the tangent bundle $$TM$$.
{: .box .example }

> **Example (Möbius bundle section).**  
> On the trivial bundle $$\mathbb{R} \times I \rightarrow \mathbb{R}$$, the constant section descends to the trivial bundles on $$S^1$$, but not to the Möbius bundle. Conversely, trigonometric functions like
> 
> $$
> x\mapsto \sin(\pi x),\qquad \textrm{and}\qquad x\mapsto \cos(\pi x) 
> $$
> 
> do descend to sections of the Möbius bundle, but not of the trivial bundle.
{: .box .example }

### Pullback bundles

As in the previous post, we're going to use the universal covering map 

$$
\mathbb{C}\twoheadrightarrow\mathbb{C}/\Lambda
$$

to understand the torus. This time, we will use it to understand line bundles on the torus. The first step is:

> **Proposition (pullbacks of fibre bundles are fibre bundles).**  
> Let $$f: B'\rightarrow B$$ be a continuous map and let $$\pi: E\rightarrow B$$ be a fibre bundle. Then the [categorical pullback](https://en.wikipedia.org/wiki/Pullback_(category_theory))
>
> $$
> \pi': E \underset{B}{\times} B' \longrightarrow B'
> $$
> 
> is a fibre bundle.
{: .box .proposition }

> **Definition (pullback bundle).**  
> This is called the *pullback bundle*, and one typically writes $$f^* (E) \mathrel{\vcenter{:}}=E \times_B B'$$.
{: .box .definition }

> *Proof:* 
> More concretely, the pullback bundle can be described as the subspace
>
> $$
> f^* (E) = \{(e,b') \in E\times B' : \pi(e) = f(b')  \} \subseteq E \times B'.
> $$
> 
> To obtain a local trivialisation around a point in $$B'$$, map it to a point in $$B$$, find a local trivialisation $$U$$ there and pull it back to an open set $$U' \mathrel{\vcenter{:}}= f^{-1}(U)$$ in $$B'$$. Restriction yields a natural morphism $$\pi'^{-1}(U') \rightarrow \pi^{-1}(U)$$, and pulling back the trivialisation $$U \times F \simeq \pi^{-1}(U)$$ yields one for $$\pi'^{-1}(U')$$.
{: .box .proof }

The universal property of the categorical pullback implies that sections of $$\pi: E\rightarrow B$$ pull back to sections of $$f^* (E) \rightarrow B'$$.

> **Example.**  
> The pullback of a trivial bundle is trivial.
{: .box .proposition }

> **Example.**  
> The pullback to $\mathbb{R}$ of the Möbius bundle looks like an infinite corkscrew.
{: .box .proposition }

The only nice picture I could find of a pullback bundle was this one:

> **Example (Two bundles over the circle $$S^1$$).**  
> Let $$\mathcal{M}$$ be a two-dimensional manifold and let $$\gamma: \mathcal{N} \rightarrow \mathcal{M}$$ be a path, mapping a point $$P$$ in $$\mathcal{N}$$ to a point $$Q$$ in $$\mathcal{M}$$. Then we can pullback the tangent bundle $$T \mathcal{M}$$ to a fibre bundle $$\gamma^* T \mathcal{M}$$ over $$\mathcal{N}$$ with two-dimensional fibres. A vector field on $$\mathcal{M}$$, with vector $$\mathbf{v}$$ at $$Q$$, pulls back to a section of the pullback $$\gamma^* T \mathcal{M}$$.
> ![img-description](assets/img/weil-pairing-part-ii/g3470_light.svg){: .light }
> ![img-description](assets/img/weil-pairing-part-ii/g3470_dark.svg){: .dark }
> _<span class="light">The Möbius strip as a fibre bundle, showing a fibre $$F_y$$ over a point $$y \in S^1$$ and a local trivalisation $$\phi_\alpha$$ over an open subset $$U_\alpha$$.</span><span class="dark">The Möbius strip as a fibre bundle, showing a fibre $$F_y$$ over a point $$y \in S^1$$ and a local trivalisation $$\phi_\alpha$$ over an open subset $$U_\alpha$$.</span>
> ([source](https://www.inm.uni-stuttgart.de/institut/mitarbeiter/eugster/papers/Eugster2014a.pdf))_
{: .box .example }


## Systems of Multipliers



Abelian varieties are the $n$-dimensional analogues of elliptic curves, and as a rule of thumb every reasonable statement about elliptic curves should have a generalization that applies to all abelian varieties. In the previous post our first step was to realise a complex elliptic curve as the quotient of a 1-dimensional complex vector space by a lattice, resulting in a complex torus. 

> **Theorem.**  
> Let $$A(\mathbb{C})$$ be an $n$-dimensional abelian variety over the complex numbers, and let $V$ denote the tangent space at the identity; this is an $n$-dimensional complex vector space. Then there exists a lattice $\Lambda \subset V$ such that the exponential map yields an isomorphism
> 
> $$
> A(\mathbb{C}) \simeq \mathbb{C} / \Lambda
> $$
> 
> as compact [complex Lie groups](https://en.wikipedia.org/wiki/Complex_Lie_group). This isomorphism extends to an equivalence of categories.
{: .box .theorem }

We will refer to such an $n$-dimensional torus as a *hypertorus*.

Now let $T = V/\Lambda$ be a hypertorus with projection map

$$\mathrm{proj}: V\twoheadrightarrow V/\Lambda = T,$$

and let $$\pi: L\rightarrow T$$ be a line bundle over this hypertorus. 
From the explicit construction of the pullback bundle $$\mathrm{proj}^* (L) = V \times_T L$$ it follows that the natural action of $$\Lambda$$ on $$V$$ lifts to the pullback bundle simply by setting

$$
\lambda \cdot (z,l) := (\lambda \cdot z,l),\qquad \textrm{for all }\lambda \in \Lambda \textrm{ and } (z,l) \in V \underset{T}{\times} L,
$$

and furthermore $$L$$ is the quotient of the pullback bundle by this action.

Now using that any bundle on $$V$$ is trivial, we may identify $$\mathrm{proj}^* (L)$$ with $$V \times \mathbb{C}$$, and the action of an element $$\lambda \in \Lambda$$ on a fibre $$\mathbb{C}$$ must be linear. Thus we have


\begin{equation}
\lambda \cdot (z,l) = \bigl( \lambda \cdot z, j_\lambda (z) l \bigr)
\label{eq:group-action}
\end{equation}

for some invertible holomorphic function $j_\lambda (z)$ on $$V$$. Since this is a group action, these functions satisfy a cocycle relation:

$$
j_{\lambda + \mu} (z) = j_\lambda(z + \mu) j_\mu (z)\qquad \textrm{for all }\lambda,\mu\in \Lambda.
$$

> **Definition (system of multipliers).**  
Let $\Lambda \subset V$ be a lattice. Then a family of invertible holomorphic functions $\\\{ j_\lambda (z) \\\}_{\lambda \in \Lambda}$ on $V$ satisfying this condition is called a *system of multipliers* on $V$.
{: .box .definition }

> **Proposition (global sections are theta functions).**  
> Conversely, given a system of multipliers on $V$, the quotient of the trivial bundle $$V\times \mathbb{C} \rightarrow V$$ by the relation in Equation \eqref{eq:group-action} yields a line bundle on $$T = V/\Lambda$$ with this system of multipliers.
{: .box .proposition }

This is a version of [descent](https://en.wikipedia.org/wiki/Descent_along_torsors).

> **Definition (theta functions).**  
> Given a system of multipliers $\\\{ j_\lambda (z) \\\}_{\lambda \in \Lambda}$, a *theta function* is a holomorphic function $\theta: V \rightarrow \mathbb{C}$ satisfying
>
> $$
> \theta(z + \lambda) = j_\lambda (z) \theta(z)\qquad \textrm{for all }\lambda \in \Lambda.
> $$
{: .box .definition }


> **Proposition (theta functions).**  
> Let $$L$$ be a line bundle on $$T$$. Then its space of global sections $$\Gamma(T, L)$$ is canonically identified with the space of theta functions for the corresponding system of multipliers.
{: .box .proposition }

The notions of direct sums, duals and tensor products for vector spaces extend naturally to vector bundles over a fixed space $X$, with the latter two operations restricting to line bundles. When line bundles are described via systems of multipliers, these operations correspond respectively to inversion and multiplication. Consequently, the [tensor product bundle](https://en.wikipedia.org/wiki/Tensor_product_bundle) construction endows the set of isomorphism classes of line bundles with a natural group structure.

[^tao]: Terence Tao [believes](https://mathoverflow.net/a/449586) the usual formalisations of these operations are unnatural, and that they are obvious from a different point of view.

> **Definition (Picard group).**  
> This group is called the *Picard group*, and we will denote it by $\mathrm{Pic}(X)$.
{: .box .definition }

The existence of inverses in this group explains why line bundles are often referred to as “invertible bundles.”


Many systems of multipliers correspond to isomorphic line bundles; their equivalence can be captured as follows:

> **Corollary.**  
> Two systems of multipliers $$\\\{ j_\lambda (z) \\\}_{\lambda \in \Lambda}$$ and $$\\\{ j_\lambda '(z) \\\}_{\lambda \in \Lambda}$$ define isomorphic line bundles if and only if there exists a nonvanishing holomorphic function $h$ on $V$ such that $$j_\lambda(z) h(z) = j_\lambda ' (z) h(z + \lambda)$$.
{: .box .proposition }

> *Proof sketch:* Denote the corresponding line bundles on $V$ by $L$ and $L'$. Then $L \simeq L'$ if and only if $L \otimes (L')^{-1}$ is trivial, if and only if $L \otimes (L')^{-1}$ has a nonvanishing global section. By the previous defintion such a section is precisely a theta functions for the system of multipliers $$j_\lambda(z) j_\lambda ' (z)^{-1}$$.
{: .box .proof }

This can be formalised in terms of [group cohomology](https://en.wikipedia.org/wiki/Group_cohomology) as follows:

> **Corollary.**  
> Let $T = V/\Lambda$ be a hypertorus. The map 
>
> $$
> \\\{\textrm{systems of multipliers} \\\} \longrightarrow \mathrm{Pic}(T)
> $$
> 
> induces an isomorphism of groups $\mathrm{H}^1 \bigl(\Lambda, \Gamma(V, \mathcal{O}_V^\times) \bigr) \simeq \mathrm{Pic}(T)$.
{: .box .corollary }

This description is not very concrete; in the previous post we similarly remarked that constructing functions corresponding to divisors is done inductively over general fields, but can be done very explicitly in the analytic setting by using Weierstrass σ-functions, which we showed arise quite naturally. A similar attitude works here, as we'll see in the next sections.

## Line Bundles from Divisors

We now relate this to the usual construction of line bundles on an elliptic curve out of a divisor.

> **Notation.**  
> Given a divisor $D = \sum_{P \in X} n_P [P]$ on a smooth curve $X$, we denote its restriction to an open subset $$U \subseteq X$$ by $$D|_U \mathrel{\vcenter{:}}= \sum_{P \in U} n_P [P]$$.
{: .box .notation }

> **Proposition (line bundle $\mathcal{L}(D)$).**  
> Let $$D$$ be a divisor on a complex torus $T$. Then there exists a natural system of multipliers on $T$ such that the sections of the corresponding line bundle $\mathcal{L}(D)$ are given by
>
> $$
> \Gamma\bigl( \mathcal{L}(D),U \bigr) \simeq \\\{ \textrm{meromorphic function }f\textrm{ on }U: \mathrm{div}(f) + D|_U \geq 0 \\\}.
> $$
{: .box .proposition }

> *Proof:* For each point $P_i$ in the support of $D$, first choose lifts $\tilde{P}_i$ in $\mathbb{C}$, and then pick a meromorphic function $f$ on $\mathbb{C}$ with divisor 
>
> $$\mathrm{div}(f) = \sum_i n_i \sum_{\lambda \in \Lambda} [\tilde{P}_i + \lambda].$$
>
> For example, the previous post showed that
> 
> $$
> f(z)\mathrel{\vcenter{:}}= \prod_{i}\sigma(z-\tilde{P}_{i};\Lambda)^{n_{i}}
> $$
>
> would work. Since this divisor does not change after translation by $\Lambda$, the quotient $f(z + \lambda) / f(z)$ is a nonvanishing holomorphic function and thus setting 
>
> $$
> j_{\lambda}(z) \mathrel{\vcenter{:}}= \frac{f(z + \lambda)}{f(z)}
> $$
>
> yields a system of multipliers. For any holomorphic section $\theta(z)$ of the corresponding bundle, we have $\theta(z+\lambda) = j_\lambda(z)\theta(z)$ which implies that $\theta(z) / f(z)$ is a $\Lambda$-periodic function with divisor $\geq -D$. 
{: .box .proof }

This bundle does not depend on the choice of $f$: if $\tilde{f}$ is another holomorphic function with that divisor, $\tilde{f}(z) / f(z)$ induces an isomorphism between the bundles. We can now derive the notion of linear equivalence of divisors:

> **Proposition.**  
> $\mathcal{L}(D)$ and $\mathcal{L}(D')$ are isomorphic if and only if the divisors $D$ and $D'$ are linearly equivalent.
{: .box .proposition }

> *Proof:* By using the group structure it suffices to show $\mathcal{L}(D)$ is trivial if and only if $D$ is a principal divisor. For the forward direction, the image of $1$ from the trivial bundle yields inside $\mathcal{O}(D)$ yields a function $f$ with $\mathrm{div}(f) + D \geq 0$, but equality is forced because $1$ is nowhere vanishing, so $D = \mathrm{div}(f^{-1})$. 
{: .box .proof }

> **Definition (ramification index).**  
> Let $\phi: X \rightarrow Y$ be a morphism of smooth curves, let $P$ be a point in $X$ and denote its image by $Q = \phi(P)$. Choose a local coordinate $u$ at $Q\in Y$. Then the  *ramification index* $e_P(\phi)$ of the morphism $\phi$ at a point $P$ is the order of the pullback $\phi^*(u)$ at $P$.
{: .box .definition }

In particular:

$$
\begin{equation}
\operatorname{ord}_P (f \circ \phi) = \operatorname{ord}_{\phi(P)} (f) \cdot e_P(\phi)
\label{eq:ramification}
\end{equation}
$$

> **Definition (pullback divisor).**  
> Let $\phi: X\rightarrow X'$ be a morphism of smooth curves and let $$D = \sum_{P' \in X'} n_{P'} [P']$$ be a divisor on $X'$. Then we can pull it back to a divisor on $X$ by defining 
>
> $$
> \phi^*(D) = \sum_{P' \in X'} n_{P'} \sum_{P \in \phi^{-1}(P')} e_P(\phi) [P].
> $$
{: .box .definition }

From \eqref{eq:ramification} it follows that a principal divisor pulls back to a principal divisor, i.e. $\phi ^* \mathrm{div}(f) = \mathrm{div}(f \circ \phi)$, but the converse does not hold: 

> **Notation.**  
> For any abelian variety, we denote the multiplication-by-$n$ map by $[n]$.
{: .box .notation }

> **Proposition.**  
> Let $T$ be a complex torus and let $Q$ be an $n$-torsion point for some $n > 1$. Then $D_Q \mathrel{\vcenter{:}}= [O] - [Q]$ is not principal, but the divisor $[n]^* D_Q$ is principal.
{: .box .proposition }

> *Proof:* The divisor $D_Q$ is not principal since $ O \neq \sum (D_Q) = Q$. Now pick a point $Q'$ such that $n Q' = Q$, then
> 
> $$
> [n]^* D_Q = [n]^* [O] - [n]^* [Q] = \sum_{T\in E[n]} [T] - [Q' + T].
> $$
>
> Recall that the cardinality of $E[n]$ is $n^2$. The two identities
>
> $$
> \deg([n]^* D_Q) = \bigl| E[n] \bigr| \, ( 1 - 1) = 0\qquad \textrm{and}\qquad \sum \bigl( [n]^* D_Q \bigr) = - \sum_{T\in E[n]} Q' = - n^2 Q' = - n Q = - O = O
> $$
>
> then imply the second claim.
{: .box .proof }

> **Proposition.**  
> Let $\phi: T\rightarrow T'$ be a morphism of complex tori and let $$D$$ be a divisor on $T'$. Then
>
> $$
> \mathcal{L}\bigl( \phi^*(D) \bigr) \simeq \phi^* \mathcal{L}(D).
> $$
{: .box .proposition }

> *Proof:* We may lift $\phi$ to the universal covers $\tilde{\phi}: V\rightarrow V'$ of $T$ and $T'$. Then the pullback of $L$ with system of multipliers $\\\{ j_{\lambda'} (z) = f(z+\lambda') / f(z) \\\}_{\lambda' \in \Lambda'}$ is a bundle with system of multipliers
>
> $$
j_\lambda (z)= \frac{f(\tilde{\phi}(z)+\tilde{\phi}(\lambda))}{f(\tilde{\phi}(z))}, 
> $$
> 
> so the bundle corresponding to the divisir of $\phi ^* (f)$, and that's $\mathrm{div}(\phi ^* f) = \phi ^* \mathrm{div}(f) = \phi ^* D$.
{: .box .proof }

{% comment %}

... ook nog uitleggen: alles heeft rational meromorphic section, dus is van de vorm L(D) ??

{% endcomment %}

We are now in a position to show that the additional term in the quasi-periodicity formula for the Weierstrass σ-function defines a system of multipliers, thereby completing the promised proof that these functions are sections of a line bundle. However, we first derive a more concrete description of systems of multipliers, which will make this conclusion even more transparent.

> **Notation (translations).**  
> Given an element $t$ in $T$, we denote the corresponding *translation* by
>
> $$
> \tau_t: T\longrightarrow T, \qquad \tilde{t} \longmapsto \tilde{t} + t
> $$
{: .box .notation }

On a group variety, these translations are the inherent symmetries, making it natural to study the behavior of a line bundle under them.

> **Lemma.**  
> Let $t$ be an element of a complex hypertorus $T = V / \Lambda$ and pick a lift $\tilde{t} \in T$. For any line bundle $L$ on $T$ with system of multipliers $$\\\{j_\lambda(z) \\\}_\lambda$$, the translate $\tau_t^* L$ has system of multipliers $$\\\{ j_\lambda(z + \tilde{t}) \\\}_\lambda$$.
{: .box .lemma }

> *Proof:* Denote by $L'$ the $$\Lambda$$-equivariant line bundle $$V \times \mathbb{C}$$ on $$V$$ with system of multipliers $$\\\{ j_\lambda(z + \tilde{t}) \\\}_\lambda$$, and similarly consider $\tau_t^* L$ as a $$\Lambda$$-equivariant line bundle on $V$. Then the map
>
> $$
> L' \longrightarrow \tau_t^* L,\qquad (z,l) \longmapsto (z + \tilde{t}, l)
> $$
>
> defines a $$\Lambda$$-equivariant bundle isomorphism.
{: .box .proof }

## The Appell–Humbert theorem

In the previous post, we explicitly constructed all elliptic functions on a complex torus using Liouville’s theorem, whose proof requires only basic complex analysis.

Holomorphic line bundles on a complex hypertorus admit an equally simple classification, but establishing it requires substantially more technical machinery. The goal of this section is to sketch some of the key ingredients involved and arrive at the statement we need, while omitting most of the proof. Thus the only result needed from this section is the Appell–Humbert description; everything else may be regarded as optional background.

A first indication that new tools are needed is that, unlike functions, holomorphic line bundles carry nontrivial topological data in addition to their holomorphic structure. This topological information is encoded by its first [Chern class](https://en.wikipedia.org/wiki/Chern_class). For an arbitrary projective variety $X$, this associates to an algebraic line bundle $L$ an element $c_1(L)$ in the first [Chow group](https://en.wikipedia.org/wiki/Chow_group) $\mathrm{CH}^1(X)$. If the variety is smooth over $\mathbb{C}$, [Poincaré duality](https://en.wikipedia.org/wiki/Poincaré_duality) then yields an element in the second cohomology group $\mathrm{H}^2(X; \mathbb{Z})$.

> **Proposition.**  
> Let $T = V / \Lambda$ be a complex hypertorus. Then $\mathrm{H}^2(T; \mathbb{C})$ is isomorphic to the space of skew-symmetric $\mathbb{R}$-bilinear forms on $V$. Furthermore, $\mathrm{H}^2(T; \mathbb{Z})$ may be identified with the subset of forms $E$ which are *integer*-valued on $\Lambda$, meaning $E( \lambda, \mu) \in \mathbb{Z}$ for all $\lambda,\mu \in \Lambda$.[^integer-forms]
{: .box .proposition }

[^integer-forms]:
    Since $V = \Lambda \otimes_\mathbb{Z} \mathbb{R}$, this is equivalent to the space of integer-valued skew-symmetric forms on $\Lambda$: given such an $E$, we extend it to $V$ by setting
    
    $$
    E(\sum_i r_i \lambda_i, \sum_j s_j \lambda_j)= \sum_{i,j} r_i s_j E(\lambda_i, \lambda_j)\qquad \textrm{for all }r_i,s_j \in \mathbb{R}\textrm{ and }\lambda_i, \lambda_j\in \Lambda.
    $$

The [Hodge decomposition](https://en.wikipedia.org/wiki/Hodge_theory#Hodge_theory_for_complex_projective_varieties) decomposes

$$
\mathrm{H}^2(T; \mathbb{C})\simeq \mathrm{H}^{2, 0}(T; \mathbb{C}) \oplus \mathrm{H}^{1, 1}(T; \mathbb{C}) \oplus \mathrm{H}^{0, 2}(T; \mathbb{C})
$$

into three [Dolbeault cohomology](https://en.wikipedia.org/wiki/Dolbeault_cohomology) groups: 
- $\mathrm{H}^{2, 0}(T; \mathbb{C})$ consists of $\mathbb{C}$-bilinear forms,
- $\mathrm{H}^{1, 1}(T; \mathbb{C})$ consists of alternating forms $E$ satisfying 

$$
\begin{equation}
E(ix,iy) = E(x,y),
\label{skew}
\end{equation}$$

- $\mathrm{H}^{0, 2}(T; \mathbb{C})$ consists of $\mathbb{C}$-biantilinear forms.


 A version of the Lefschetz theorem implies that the image of $c_1(\cdot )$ lands inside of $\mathrm{H}^{1, 1}(T; \mathbb{C})$. Those forms can also be described as [Hermitian forms](https://en.wikipedia.org/wiki/Sesquilinear_form#Hermitian_form):

> **Proposition.**  
> Let $V$ be a finite-dimensional complex vector space. There is a bijection between Hermitian forms on $V$ and alternating forms on $V$ satisfying $\eqref{skew}$. This restricts to a bijection between forms taking integral values on a lattice $\Lambda \subset V$.
{: .box .proposition }

> *Proof sketch:* Given a Hermitian form $H$, set $E$ to be its imaginary part, meaning $E(x,y) \mathrel{\vcenter{:}}= \Im \bigl(H(x,y) \bigr)$. In the other direction, given a form $E$ satisfying $\eqref{skew}$ one finds that $H(x,y) \mathrel{\vcenter{:}}= E(x, iy) + i E(x,y)$ is Hermitian.
{: .box .proof }

Thus, to a complex line bundle one can associate a Hermitian form on $V$. We need one more ingredient:

> **Definition (semi-character).**  
> Let $H$ be a Hermitian form on a complex vector space $V$ taking integral values on a lattice $\Lambda \subset V$, and denote its imaginary part by $E = \Im(H)$. A *semi-character* for $H$ (or $E$) is a map $\chi: \Lambda \rightarrow \mathrm{U}(1)$ such that[^semi-character] 
>
> $$ 
> \chi(\lambda + \mu) = \chi(\lambda) \chi(\mu) e^{ \pi i E(\lambda,\mu) }\qquad \textrm{for all }\lambda,\mu \in \Lambda.
> $$
{: .box .definition }

[^semi-character]: In cohomological terminology, a semi-character is a function $\chi: \Lambda \rightarrow \mathrm{U}(1)$ whose coboundary equals the 2-cocycle $(\lambda, \mu) \mapsto e^{\pi i E(\lambda, \mu)}$.

When $H$ is trivial, this reduces to the ordinary definition of a character.

> **Definition (Appell–Humbert datum).**  
> Such a pair $(H,\chi)$ is called an *Appell–Humbert datum*.
{: .box .definition }

Such data allows one to construct line bundles as follows:

> **Proposition.**  
> Let $H$ be a Hermitian form on $V$ with semi-character $\chi$. Then
>
> $$ 
> j_\lambda (z) = \chi(\lambda) e^{ \pi (H(\lambda,z) + H(\lambda,\lambda)/2   )}
> $$
>
> defines a system of multipliers.[^holomorphic]
 Furthermore, the first Chern class of the corresponding line bundle is $E$.
{: .box .proposition }

[^holomorphic]: Here we are using that $H(\lambda,z)$ is linear in $z$ to obtain a holomorphic function; $H(z,\lambda)$ would yield an anti-holomorphic function instead.

> *Proof:* We only show the first part. Expanding $H(\lambda,\mu) = E(\lambda, i\mu) + i E(\lambda,\mu)$ yields
>
> $$
> H(\lambda,\mu)=E(\lambda,i\mu)+iE(\lambda,\mu)=H(\lambda,\mu)/2+H(\mu,\lambda)/2+iE(\lambda,\mu),
> $$
> 
> from which it follows that
> 
> \begin{align}
> \frac{j_{\lambda+\mu}(z)}{j_{\lambda}(z+\mu)j_{\mu}(z)} & =\frac{\chi(\lambda+\mu)e^{\pi(H(\lambda+\mu,z)+H(\lambda+\mu,\lambda+\mu)/2)}}{\chi(\lambda)e^{\pi(H(\lambda,z+\mu)+H(\lambda,\lambda)/2)}\chi(\mu)e^{\pi(H(\mu,z)+H(\mu,\mu)/2)}} \nonumber \\\\\
>  & =\frac{e^{\pi iE(\lambda,\mu)}e^{\pi(H(\lambda+\mu,\lambda+\mu)/2)}}{e^{\pi(H(\lambda,\mu)+H(\lambda,\lambda)/2)}e^{\pi(H(\mu,\mu)/2)}} \nonumber \\\\\
>  & =\frac{e^{\pi iE(\lambda,\mu)}e^{\pi(H(\lambda,\mu)/2+H(\mu,\lambda)/2)}}{e^{\pi H(\lambda,\mu)}}=1. \nonumber 
> \end{align}
{: .box .proof }

> **Notation.**  
> We will denote this line bundle by $L(H,\chi)$.
{: .box .notation }

We can now explicitly describe the set of isomorphism classes of holomorphic line bundles as follows:

> **Theorem (Appell–Humbert [App91, Hum93]).**  
> Let $T$ be a complex hypertorus. The map
> 
> $$ \\\{ \textrm{Appell–Humbert data for }T \\\} \longrightarrow \mathrm{Pic}(T),\qquad (H,\chi) \longmapsto L(H,\chi)$$
>
> is a bijection.
{: .box .theorem }


The induced group structure on the set of Appell–Humbert data (coming from the tensor product on line bundles) is 

$$
(H,\chi) \cdot (H',\chi') = (H+H',\chi \chi').
$$

> **Lemma.**  
> Let $t$ be an element of a complex hypertorus $T = V / \Lambda$ and pick a lift $\tilde{t} \in T$. Then for any holomorphic line bundle $L(H,\chi)$ we have
>
> $$
> \tau_t L(H, \chi) \simeq L(H, \chi'),\qquad \textrm{ where } \chi'(\lambda) \mathrel{\vcenter{:}}= \chi(\lambda) e^{2 \pi i E(\lambda, \tilde{t})}.
> $$
{: .box .lemma }

> *Proof:* By a previous lemma, the system of multipliers of $\tau_t L(H, \chi)$ is $\\\{ j_\lambda(z + \tilde{t}) \\\}_\lambda$; expanding yields
> 
> $$
> j_\lambda(z + \tilde{t}) = j_\lambda(z) e^{\pi H(\lambda, \tilde{t})}.
> $$
>
> The claim then follows by multiplying the right-hand-side by $h(z + \lambda) / h(z)$ for the nonvanishing holomorphic function $h(z) = e^{- \pi H(\tilde{t}, z)}$, yielding an isomorphic line bundle (as we showed earlier) with the required system of multipliers.
{: .box .proof }

## Polarisations

We will now use the Appell–Humbert theorem to prove statements about holomorphic line bundles; the same statements work over arbitrary fields, but the proofs are much more technical. 

{% comment %}

> **Definition (homological equivalence).**  
> A pair of holomorphic line bundles on a hypertorus is said to be *homologically equivalent* if they have the same Chern class.
{: .box .notation }

As we've seen, this is equivalent to saying that their Hermitian forms agree.

{% endcomment %}


> **Theorem.**  
> Let $L$ be a line bundle on an abelian variety $A$. Then the map
>
> $$
> \mathrm{Pol}_L : A \longrightarrow \mathrm{Pic} (A),\qquad a\longmapsto \tau_a^* L \otimes L^{-1}
> $$
>
> is a homomorphism.
{: .box .theorem }

> **Definition.**  
> This is called the *polarisation homomorphism* associated to $L$; when such a line bundle is fixed, one says that $A$ is polarised.
{: .box .definition }

Intuitively, this map measures how a fixed line bundle $L$ changes under translation. In full generality this statement follows from the "theorem of the square", but the proof is simpler if we assume that $A$ is a hypertorus and invoke the Appell–Humbert theorem:

> *Proof:* Let $t$ be an element of a complex hypertorus $T = V / \Lambda$ and pick a lift $\tilde{t} \in T$. Let $L = L(H, \chi)$, then by the previous lemma we find $\mathrm{Pol}_L(t) \simeq L(H, \chi \chi') \otimes L(-H, \chi^{-1}) \simeq L(0, \chi')$ where 
>
> $$
> \chi'(\lambda) = e^{2 \pi i E(\lambda, \tilde{t})}.
> $$
{: .box .proof }

> **Notation.**  
> Let $A$ be an abelian variety. Then the the set of translation-invariant line bundles will be denoted by $\mathrm{Pic}^\circ (A)$; equivalently, this is the kernel in $\mathrm{Pic}(A)$ of the map $L\mapsto \mathrm{Pol}_L(\cdot)$.
{: .box .notation }

The previous lemma implies that for a hypertorus, this corresponds to line bundles with trivial Hermitian form. The "theorem of the square" also implies:

> **Proposition.**  
> Let $(A,L)$ be a polarised abelian variety. Then the image of the homomorphism $\mathrm{Pol}_L(\cdot)$ lands in $\mathrm{Pic}^\circ (A) \subset \mathrm{Pic} (A)$.
{: .box .proposition }

> *Proof:* In the setting of complex hypertori, the previous proof demonstrated that the image is of the form $L(0, \chi)$.
{: .box .proof }

> **Notation.**  
> Let $(A, L)$ be a polarised abelian variety. Then for any point $a$ in $L$ we write $L_a \mathrel{\vcenter{:}}= \mathrm{Pol}_L(a)$ for the corresponding line bundle on $A$.
{: .box .notation }

> **Proposition.**  
> Consider the polarised elliptic curve $\bigl( E, \mathcal{L}([O]) \bigr)$. Then $L_P = \mathcal{L}([O] - [P])$.
{: .box .proposition }

Note that the polarisation map here differs from much of the established elliptic curve literature by a sign (which is not an issue for abelian groups), where instead $P$ would be mapped to $\mathcal{L}([P] - [O])$.

> *Proof:* We have
>
> $$
> \mathcal{L}_{P}=\mathrm{Pol}_{\mathcal{L}([O])}(P)\simeq \mathcal{L}\bigl([O-P]\bigr)\otimes\mathcal{L}([O])^{-1}\simeq\mathcal{L}\bigl([-P]\bigr)\otimes\mathcal{L}([-O])\simeq\mathcal{L}([O]-[P]).
> $$
{: .box .proof }

> **Proposition.**  
> Let $L$ be a line bundle on an abelian variety. If it lies in $\mathrm{Pic}^\circ (A)$, then
>
> $$
> [n]^* L \simeq L^{\otimes n}\qquad\textrm{for all }n\in \mathbb{Z}.
> $$
{: .box .proposition }

For arbitrary fields, this statement follows from the "theorem of the cube".

> *Proof:* Let $\chi$ be the semi-character such that $L \simeq L(0,\chi)$, then $\chi$ is a character. This implies that $\chi \circ n = \chi^n$, and hence
>
> $$
> [n]^* L \simeq L(0, \chi \circ n) = L(0, \chi^n) \simeq L^{\otimes n}\qquad\textrm{for all }n\in \mathbb{Z}.
> $$
{: .box .proof }

> **Corollary.**  
> Let $(A,L)$ be a polarised abelian variety and let $a$ be an element in the $n$-torsion subgroup of $A$. Then $[n]^* L_a$ is trivial.
{: .box .corollary }

> *Proof:* Since $\mathrm{Pol}_L(\cdot)$ is a homomorphism, $L_a^{\otimes n}$ is trivial. As $L_a$ lies in $\mathrm{Pic}^\circ (A)$, the claim now follows from the previous proposition.
{: .box .proof }

## The Weil Pairing for Abelian Varieties

In full generality, the Weil pairing can be phrased as follows:

> **Theorem (Weil pairing).** 
> Let $\phi: A \rightarrow A'$ be a morphism of abelian varieties over a field $K$, thus inducing a pullback map $$\phi^*$$ on their line bundles. Then there exists a natural pairing
>
> $$\mathrm{ker}(\phi) \times \mathrm{ker}(\phi^{*}) \longrightarrow K.$$
> 
{: .box .theorem }

> *Proof:* Let $a \in \mathrm{ker}(\phi)$ and $$\hat{b} \in \mathrm{ker}(\phi^{*})$$. Then by definition there exists an isomorphism $$\xi:\mathcal{O}_{A}\overset{\simeq}{\rightarrow}\phi^{*}(\hat{b})$$. Since $\phi(a)=0$ and $\phi$ is a homomorphism, we have $\phi\circ\tau_{a}=\phi$ and hence $$\tau_{a}^{*}\phi^{*}\hat{b} = \phi^{*}\hat{b}$$. Thus $\tau_{a}^{*}$ induces an automorphism of $$\mathcal{O}_{A}$$, but automorphisms of $$\mathcal{O}_{A}$$ are elements of $$\mathcal{O}_{A}^{\times}$$, and global sections of those are constant. In other words, the composition
>
> $$
> \mathcal{O}_{A}\overset{\xi}{\longrightarrow}\phi^{*}(\hat{b})\overset{\tau_{a}^{*}}{\longrightarrow}\phi^{*}(\hat{b})\overset{\xi^{-1}}{\longrightarrow}\mathcal{O}_{A}.
> $$
>
> yields an element in the base field. Since a different choice of $\xi$ would correspond to multiplying $\xi$ by a constant (by the same reasoning), this element is independent of the choice of $\xi$.
{: .box .proof }

Combining this with the previous corollary yields:

> **Corollary.** 
> Let $(A, L)$ be a polarised abelian variety and let $\phi$ be the endomorphism $[n] : A\rightarrow A$ of multiplication-by-$n$ for some integer $n$. Then there is a natural pairing between points $a,b$ in $A[n]$ obtained by pairing the element $a$ with the line bundle $L_b$.
{: .box .corollary }

When $\phi$ is an [isogeny](https://en.wikipedia.org/wiki/Isogeny) (which is the case for $\phi =[n] $ when $n$ is nonzero), the pairing is perfect; this is an instance of [Cartier duality](https://en.wikipedia.org/wiki/Cartier_duality), and the pairing is sometimes also known as the Cartier pairing (e.g. **[Oda69]**).

Finally, we specialise to the setting of complex elliptic curves:

> **Proposition.**
> For a polarised complex torus $\bigl( T, \mathcal{L}([O]) \bigr)$ with the morphism $\phi = [n]$ given by multiplication-by-$n$, this reduces to the ordinary Weil pairing on elliptic curves.
{: .box .proposition }

More precisely, we will recover the Weil pairing definition of **[Wa08]** and **[Sil09]**:

> *Proof:* Let's apply the last Corollary to a pair of $n$-torsion points $P,Q$ in $T$. We've seen that $L_Q \simeq \mathcal{L}(D_Q)$, where $D_Q = [O] - [Q]$. Then
>
> $$
> [n]^* L_Q \simeq [n]^* \mathcal{L}(D_Q) \simeq \mathcal{L}([n]^* D_Q).
> $$
> 
> We've also seen that $[n]^* D_Q$ is principal, so there exists a function $g$ (which we can explicitly construct using Weierstrass σ-functions) with $\mathrm{div}(g)$ = $[n]^* D_Q$; this is a trivialising section, so $\xi$ sends 1 to (a constant of) $g$. Then $\tau_P^*$ sends the section $g$ to $g(z + P)$ and $\xi^{-1}$ divides by $g(z)$ again (cancelling the extra constant). Since $P$ lies in $E[n]$ and $E[n]$ is a group (and hence invariant under translation), we have
>
> $$\sum_{T\in E[n]} \tau_P^* [R + T] = \sum_{T\in E[n]} [R + (T + P)] = \sum_{T\in E[n]} [R + T]$$
>
> for any point $R$ (including $O$). This implies that the functions $g(z + P)$ and $g(z)$ have the same divisor:
> 
> $$
> \mathrm{div}(\tau_P^*g) = \tau_P^* \mathrm{div}(g) = \tau_P^* [n]^* D_Q = \sum_{T\in E[n]} \tau_P^* [T] - \tau_P^* [Q' + T] = \sum_{T\in E[n]} [T] - [Q' + T] = [n]^* D_Q = \mathrm{div}(g)
> $$
>
> so their fraction is constant; this fraction $g(z + P) / g(z)$ is the Weil pairing.
{: .box .proof }

## References

**[App91]**  P. Appell (1891), "Sur les functiones périodiques de deux variables", Journal de Mathématiques Pures et Appliquées, Série IV, 7: 157–219

**[Bha17]** Bhargav Bhatt (2017, December). Abelian varieties (lecture notes). Retrieved from https://www.math.ias.edu/~bhatt/teaching/mat731f17/lectures.pdf

**[Hum93]**  M. G. Humbert (1893), "Théorie générale des surfaces hyperelliptiques", Journal de Mathématiques Pures et Appliquées, Série IV, 9: 29–170, 361–475

**[Edi02]** Bas Edixhoven (2002, February 28). Le couplage de Weil: de la géométrie à l’arithmétique (Seminar talk). Retrieved from https://websites.math.leidenuniv.nl/edixhoven/talks/2002/2002_02_11.pdf

**[Mum74]** David Mumford. Abelian varieties. Vol. 5. Oxford: Oxford University Press, 1974.

**[Oda69]** Tadao Oda. "The first de Rham cohomology group and Dieudonné modules." Annales scientifiques de l'École Normale Supérieure. Vol. 2. No. 1. 1969.

**[Sil09]** Joseph H. Silverman. The Arithmetic of Elliptic Curves. Vol. 106. New York: Springer, 2009.

**[Was08]** Lawrence C. Washington. Elliptic curves: number theory and cryptography. Chapman and Hall/CRC, 2008.

**[Wei92]** Weil, André. The apprenticeship of a mathematician. Springer Science & Business Media, 1992.