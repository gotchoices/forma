# Matrix Primer for the Metric

How matrices encode the distance formula, and what the notation
in `kaluza-klein.md` means. Starts from scratch.

---

## 1. What a matrix is

A matrix is a rectangle of numbers. A 2×2 matrix has 2 rows and
2 columns:

    A = | 3  1 |
        | 2  5 |

The entry in row i, column j is written A_ij. So:

    A₁₁ = 3    A₁₂ = 1
    A₂₁ = 2    A₂₂ = 5

A matrix isn't a number — it's a machine that operates on vectors.


## 2. Vectors

A vector is an ordered list of numbers. In 2D:

    v = [3, 4]

This represents a displacement: 3 units in the x direction, 4
units in the y direction. We can write it as a column:

    v = | 3 |
        | 4 |

or as a row:

    vᵀ = [3, 4]

The ᵀ symbol means **transpose** — flip a column into a row (or
vice versa). If v is a column vector, vᵀ is the same numbers
written as a row.


## 3. Matrix-vector multiplication

To multiply a matrix times a column vector, take each row of the
matrix and "dot" it with the vector. The dot product of two lists
is: multiply corresponding entries, then add.

    A · v = | 3  1 | · | 3 | = | 3×3 + 1×4 | = | 13 |
            | 2  5 |   | 4 |   | 2×3 + 5×4 |   | 26 |

Row 1 of A dotted with v: 3×3 + 1×4 = 13.
Row 2 of A dotted with v: 2×3 + 5×4 = 26.

Result: a new column vector [13, 26].

**Rule:** the number of columns of the matrix must match the
number of entries in the vector. A 2×2 matrix times a 2-entry
vector gives a 2-entry vector. A 3×3 matrix times a 3-entry
vector gives a 3-entry vector.

**Does order matter?** Yes. Matrix multiplication is not
commutative — A·B and B·A generally give different results (and
may not even be valid in both orders, since the column-count of
the left thing must match the row-count of the right thing).

For our purposes, the shapes dictate the order:

    column (2×1) × matrix (2×2)  →  invalid (1 ≠ 2)
    matrix (2×2) × column (2×1)  →  column (2×1)  ✓
    row (1×2) × column (2×1)     →  scalar (1×1)   ✓
    column (2×1) × row (1×2)     →  matrix (2×2) — a different operation entirely

So you can't rearrange the multiplication — the shapes lock you
into one valid order for each operation. This means you don't need
to memorize ordering rules; just check that the inner dimensions
match.

**Do we need cross products?** No. Cross products are specific to
3D — they produce a vector perpendicular to two input vectors,
which requires exactly three dimensions to define "perpendicular
to a plane." The metric uses only dot products (generalized
through the triple product in §5). Everything in Kaluza-Klein
theory is expressed through the metric, so dot products and the
triple product are all we need.


## 4. Row-vector times column-vector: the dot product

When you multiply a row vector times a column vector (both with
the same number of entries), you get a single number:

    [3, 4] · | 3 | = 3×3 + 4×4 = 25
              | 4 |

This is the dot product: multiply corresponding entries, add them
up. The result is a scalar (a single number), not a vector.

**Notation:**

    vᵀ · v = [3, 4] · | 3 | = 3² + 4² = 25
                       | 4 |

This is just the sum of squares — the square of the length of the
vector (Pythagorean theorem: 3² + 4² = 5², length = 5).


## 5. The triple product: row × matrix × column

We need a way to compute distance² from a displacement vector.
Consider what we have to work with:

- A vector v = [dx, dy] — the displacement
- A matrix g — the geometry (axis scales and tilts)

We want a single number out (distance²). What are our options?

- **v alone** doesn't give distance — [3, 4] is a vector, not a
  number.
- **vᵀ · v** gives dx² + dy² — Pythagorean distance. But this
  only works if the axes are perpendicular and unit-scale. It
  doesn't know about the geometry.
- **g · v** gives a new vector — still not a number.
- **vᵀ · g · v** gives a single number that depends on both the
  displacement AND the geometry. This is the only combination
  that produces a scalar while using both v and g.

The triple product vᵀ · g · v is not something people stumbled
upon — it is the unique way to combine a matrix and a vector into
a scalar (distance²). When g is the identity matrix, it reduces
to vᵀ · v = Pythagorean distance. When g has other entries, it
computes distance for a different geometry. The matrix g
generalizes Pythagoras to any coordinate system.

Let's evaluate it in two steps.

**Step 1:** matrix times column vector (§3):

    A · v = | 3  1 | · | 3 | = | 13 |
            | 2  5 |   | 4 |   | 26 |

**Step 2:** row vector times the result (§4):

    vᵀ · (A · v) = [3, 4] · | 13 | = 3×13 + 4×26 = 39 + 104 = 143
                              | 26 |

The result is a single number: 143.

Let's also expand this directly, without intermediate steps.
Write v = [v₁, v₂]:

    vᵀ · A · v = [v₁, v₂] · | A₁₁  A₁₂ | · | v₁ |
                              | A₂₁  A₂₂ |   | v₂ |

Expanding fully:

    = A₁₁ v₁ v₁ + A₁₂ v₁ v₂ + A₂₁ v₂ v₁ + A₂₂ v₂ v₂

    = A₁₁ v₁² + (A₁₂ + A₂₁) v₁ v₂ + A₂₂ v₂²

Every term is a product of one matrix entry and two vector
entries. Each combination of indices (i,j) from the matrix
gets multiplied by the corresponding pair (vᵢ, vⱼ) from the
vector.


## 6. Connecting to the distance formula

Now set v = [dx, dy] — an infinitesimal displacement. And set
the matrix to the identity:

    g = | 1  0 |
        | 0  1 |

Compute the triple product:

    [dx, dy] · | 1  0 | · | dx | = 1·dx·dx + 0·dx·dy + 0·dy·dx + 1·dy·dy
               | 0  1 |   | dy |

    = dx² + dy²

That's the Pythagorean theorem. The triple product IS the distance
formula.

Written compactly:

    ds² = [dx, dy] · g · [dx, dy]ᵀ

This is line 62 of `kaluza-klein.md`. It says: "the squared
distance ds² equals the row vector of coordinate displacements,
times the metric matrix g, times the column vector of coordinate
displacements."


## 7. Why the matrix matters

Different matrices give different distance formulas.

**Cartesian (flat, perpendicular axes):**

    g = | 1  0 |       ds² = dx² + dy²
        | 0  1 |

**Polar coordinates:**

    g = | 1   0  |     ds² = dr² + r²dθ²
        | 0   r² |

**Stretched space (y-distances count double):**

    g = | 1  0 |       ds² = dx² + 4 dy²
        | 0  4 |

**Tilted axes (off-diagonal terms):**

    g = | 1    0.5 |   ds² = dx² + dx·dy + dy²
        | 0.5  1   |

The off-diagonal entry 0.5 appears twice (once as A₁₂, once as
A₂₁) and they combine: (0.5 + 0.5) dx·dy = 1.0 dx·dy.

The matrix g encodes everything about the geometry: how long each
axis is, and how the axes relate to each other. Diagonal entries
set axis lengths. Off-diagonal entries set axis tilts. This is
why the metric matrix is the fundamental object — it IS the
geometry, written as numbers.


## 8. Scaling to more dimensions

In 3D:

    v = [dx, dy, dz]

    g = | g₁₁  g₁₂  g₁₃ |
        | g₂₁  g₂₂  g₂₃ |
        | g₃₁  g₃₂  g₃₃ |

    ds² = vᵀ · g · v

The formula is identical — just a bigger matrix and a longer
vector. For flat 3D Cartesian space, g is the 3×3 identity matrix
and you get ds² = dx² + dy² + dz².

In 4D spacetime:

    v = [c dt, dx, dy, dz]

    g = | −1  0  0  0 |
        |  0  1  0  0 |
        |  0  0  1  0 |
        |  0  0  0  1 |

    ds² = −c²dt² + dx² + dy² + dz²

The −1 in the top-left corner is what makes time different from
space. Same matrix machinery, just 4×4.

In Kaluza-Klein (5D): a 5×5 matrix. In our T² model (6D): a 6×6
matrix. The machinery scales without any new concepts.


## 9. Index notation: a shorthand for large matrices

Writing out a 5×5 matrix every time is tedious. Index notation
compresses it. We'll build it up in small steps.

### Step 1: label the coordinates with numbers

Instead of calling the coordinates x and y, call them x¹ and x².
The superscript is a **label**, not a power — x² means "the
second coordinate," not "x squared." (This is confusing at first.
Context always makes it clear: if there's a d in front, like dx²,
it's a coordinate label. If it's standalone, like v², it might be
a power. In practice, index notation always uses the label
meaning.)

In 3D the coordinates are x¹, x², x³. In 5D: x¹, x², x³, x⁴,
x⁵. The displacement vector is [dx¹, dx², ..., dxⁿ].

### Step 2: write the distance formula as a sum

In §5 we expanded the 2D triple product to get four terms:

    ds² = g₁₁ dx¹ dx¹ + g₁₂ dx¹ dx² + g₂₁ dx² dx¹ + g₂₂ dx² dx²

Look at the pattern. Each term has:
- One metric entry g with two subscript labels (row, column)
- Two coordinate displacements dx with one superscript label each
- The subscripts on g always match the superscripts on the dx's

We can write this as a double sum:

    ds² = Σᵢ Σⱼ  g_ij  dxⁱ  dxʲ

This says: let i run over {1, 2} and j run over {1, 2}. For each
combination, multiply g_ij × dxⁱ × dxʲ and add them all up.
That gives 2×2 = 4 terms — exactly the four terms above.

In 5D, i and j each run over {1, 2, 3, 4, 5}, giving 25 terms.
The sum notation handles any number of dimensions without
writing them all out.

### Step 3: the up/down convention

Notice that in each term, the label letters have specific
positions:

    g_ij  dxⁱ  dxʲ
     ↓↓    ↑    ↑
    down  up   up

The metric entries g_ij have subscript (down) indices. The
coordinate displacements dxⁱ, dxʲ have superscript (up) indices.
Why? It's a bookkeeping convention that distinguishes two kinds of
objects:

- **Subscript (down) indices** — on things that "measure" or
  "weight" (like the metric)
- **Superscript (up) indices** — on things that "move" or
  "displace" (like coordinates)

The distinction exists because in curved space, these two kinds
of objects transform differently under coordinate changes. For
now, just treat it as a labeling convention — subscripts go on g,
superscripts go on dx.

### Step 4: the Einstein summation convention

Look at the expression g_ij dxⁱ dxʲ again. Focus on the letter i:

    g_ij dxⁱ dxʲ
     ↓        ↑
     i down   i up

The letter i appears **twice** — once as a subscript (on g) and
once as a superscript (on dx). Same for j:

    g_ij dxⁱ dxʲ
      ↓         ↑
      j down    j up

Einstein's convention: **when the same letter appears once up and
once down in a single term, sum over it.** This means the Σ signs
are redundant — the up/down pattern already tells you to sum.

So instead of writing:

    ds² = Σᵢ Σⱼ g_ij dxⁱ dxʲ

you just write:

    ds² = g_ij dxⁱ dxʲ

and everyone knows you mean "sum over i and j" because i and j
each appear once up and once down. The convention exists purely
to save writing Σ signs, which pile up fast in higher dimensions.

### Step 5: expanding the 2D case

Let's verify. In 2D, i and j each run over {1, 2}. Expanding
g_ij dxⁱ dxʲ means: write out every combination of i and j:

    i=1, j=1:  g₁₁ dx¹ dx¹
    i=1, j=2:  g₁₂ dx¹ dx²
    i=2, j=1:  g₂₁ dx² dx¹
    i=2, j=2:  g₂₂ dx² dx²

Sum them:

    g₁₁ dx¹ dx¹ + g₁₂ dx¹ dx² + g₂₁ dx² dx¹ + g₂₂ dx² dx²

If x¹ = x and x² = y, and g is the identity (g₁₁ = g₂₂ = 1,
g₁₂ = g₂₁ = 0):

    = 1·dx·dx + 0·dx·dy + 0·dy·dx + 1·dy·dy = dx² + dy²

Pythagorean theorem, recovered from index notation.

### Step 6: reading the KK metric

In `kaluza-klein.md`, the 5D metric is written:

    ds² = g_μν dxᵘ dxᵛ + ...

This is the same formula — just with Greek letters μ and ν
instead of i and j. Physics convention: Latin letters (i, j, k)
for spatial indices; Greek letters (μ, ν) for spacetime indices.

Here μ and ν each run over {0, 1, 2, 3} where x⁰ = t, x¹ = x,
x² = y, x³ = z. The expression g_μν dxᵘ dxᵛ means: sum over all
16 combinations of μ and ν. It's the 4×4 triple product — the
spacetime part of the distance formula.

The "..." after it is the extra terms from the fifth dimension,
which `kaluza-klein.md` §7–§8 handles separately.


## 10. Summary: three notations for the same formula

All three of these are identical:

**Explicit:**

    ds² = dx² + dy²

**Matrix (triple product):**

    ds² = [dx, dy] · | 1  0 | · | dx |
                     | 0  1 |   | dy |

**Index notation:**

    ds² = g_ij dxⁱ dxʲ    with g = identity

The matrix form shows the geometry as a grid of numbers. The index
form compresses it for large dimensions. The explicit form is what
you compute with. They're all the same distance formula.

---

*Continue to [`kaluza-klein.md`](kaluza-klein.md) §3 (off-diagonal
terms) to see what happens when the matrix has nonzero entries
off the diagonal.*
