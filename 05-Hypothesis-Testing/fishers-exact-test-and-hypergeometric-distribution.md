# Fisher's Exact Test and the Hypergeometric Distribution

## One-Sentence Summary

Fisher's Exact Test helps determine whether two categorical variables are related, while the Hypergeometric Distribution calculates how surprising the observed data would be under the assumption of no relationship.

---

## What Is It?

Suppose you observe two groups and notice a difference.

For example:

- A medicine group and a placebo group
- A new website design and an old design
- A new machine learning model and a baseline model

The question becomes:

> Is the observed difference meaningful?

or

> Could this difference have appeared by chance?

Fisher's Exact Test helps answer this question when working with small datasets.

---

## Why Should I Care?

Many experiments produce data that falls into categories.

Examples:

| User | Clicked? |
|--------|---------|
| User 1 | Yes |
| User 2 | No |
| User 3 | Yes |

Or:

| Patient | Recovered? |
|-----------|------------|
| Patient 1 | Yes |
| Patient 2 | No |

When data can be organized into counts like these, Fisher's Exact Test becomes useful.

---

## The Big Idea

Imagine drawing cards from a deck.

You observe an unusual combination.

The natural question is:

> Was this arrangement random?

Fisher's Exact Test calculates exactly how likely the observed arrangement would be if no real relationship existed.

---

## Intuition

Suppose a clinical trial involves:

| Group | Recovered | Not Recovered |
|---------|-----------|--------------|
| Medicine | 8 | 2 |
| Placebo | 3 | 7 |

The medicine appears better.

But appearances can be misleading.

The question becomes:

> If the medicine were actually useless, how likely would it be to observe a table this extreme?

Fisher's Exact Test answers exactly that question.

---

## Courtroom Analogy

Null Hypothesis:

```text
The medicine has no effect.
```

Observed Evidence:

```text
Medicine Group:
8 recovered

Placebo Group:
3 recovered
```

Now we ask:

> How surprising is this evidence if the medicine truly has no effect?

That surprise is calculated using the Hypergeometric Distribution.

---

## The Hypergeometric Distribution

Before understanding Fisher's Exact Test, we need the Hypergeometric Distribution.

---

### What Is It?

The Hypergeometric Distribution describes the probability of drawing a specific number of successes from a finite population without replacement.

The key phrase is:

```text
Without Replacement
```

Once an item is selected, it cannot be selected again.

---

## Card Deck Example

Imagine a standard deck:

```text
52 cards
```

Suppose:

```text
4 Aces
48 Non-Aces
```

You draw:

```text
5 cards
```

Question:

> What is the probability of getting exactly 2 Aces?

The Hypergeometric Distribution solves this problem.

---

## Intuition

The Hypergeometric Distribution asks:

> How surprising is this specific arrangement?

That idea will eventually become the foundation of Fisher's Exact Test.

---

## Rock & Metal Corner

Imagine:

100 festival attendees

Among them:

```text
20 wear Band A shirts
80 wear other shirts
```

Randomly select:

```text
10 attendees
```

Suppose:

```text
8 wear Band A shirts
```

That feels unusual.

The Hypergeometric Distribution measures exactly how unusual it is.

---

## How Fisher's Exact Test Uses It

Fisher's Exact Test analyzes contingency tables.

Example:

| | Success | Failure |
|---|---|---|
| Group A | 8 | 2 |
| Group B | 3 | 7 |

Using the Hypergeometric Distribution, Fisher calculates:

> How likely is this table if the null hypothesis is true?

The result becomes a p-value.

---

## Why "Exact"?

Many statistical tests use approximations.

Fisher's Exact Test does not.

It computes probabilities directly.

Thus:

```text
Exact Test
```

---

## When Is Fisher's Exact Test Useful?

Particularly useful when:

- Sample sizes are small
- Counts are low
- Approximation methods become unreliable

---

## Worked Example

Suppose:

| Treatment | Improved | Not Improved |
|------------|-----------|--------------|
| New Method | 9 | 1 |
| Old Method | 5 | 5 |

Question:

> Are these groups different?

Null Hypothesis:

```text
The treatment does not matter.
```

Fisher's Exact Test calculates how likely it would be to obtain a table this extreme if the null hypothesis were true.

If the probability is very low:

The null hypothesis becomes difficult to believe.

---

## The StatQuest Takeaway

Fisher's Exact Test asks:

> If there is no relationship between the two variables, how surprising is the table we observed?

The Hypergeometric Distribution provides the mathematical engine that answers that question.

---

## Machine Learning Connection

Although Fisher's Exact Test is traditionally associated with statistics, similar ideas appear in machine learning.

### Feature Selection

Does a feature genuinely relate to a target variable?

---

### A/B Testing

Are differences between experiments meaningful?

---

### Data Analysis

Do category distributions differ significantly across groups?

---

## AI / LLM / RAG Connection

### Prompt Evaluation

Suppose:

Prompt A succeeds more often than Prompt B.

Is the difference meaningful?

Statistical testing helps answer this.

---

### RAG Evaluation

Compare:

- Retrieval Strategy A
- Retrieval Strategy B

Fisher-style reasoning helps determine whether observed improvements are meaningful or random.

---

### User Research

Comparing user outcomes across prompt versions often produces categorical data suitable for contingency-table analysis.

---

## Common Misconceptions

### Fisher's Exact Test Proves Causation

False.

It evaluates association.

Not causation.

---

### A Small p-value Proves The Alternative Hypothesis

False.

It provides evidence against the null hypothesis.

---

### Fisher's Exact Test Is Only For Medicine

False.

It applies to any categorical data.

---

### Hypergeometric Distribution And Fisher's Exact Test Are The Same

False.

The Hypergeometric Distribution powers the calculations.

Fisher's Exact Test uses those calculations.

---

## Pulkit's Mental Model

The Hypergeometric Distribution measures how surprising a particular arrangement is.

Fisher's Exact Test uses that surprise to judge whether the null hypothesis still makes sense.

---

## Interview Questions

### What is Fisher's Exact Test?

A statistical test used to determine whether two categorical variables are associated.

---

### What distribution powers Fisher's Exact Test?

The Hypergeometric Distribution.

---

### Why is it called an exact test?

Because it computes probabilities directly rather than using approximations.

---

### When is Fisher's Exact Test preferred?

When sample sizes are small.

---

### What does Fisher's Exact Test ultimately calculate?

A p-value.

---

## Related Topics

- Hypothesis Testing
- Null Hypothesis
- Alternative Hypothesis
- p-values
- Hypergeometric Distribution
- Statistical Power

---

## References

- StatQuest: Fisher's Exact Test and the Hypergeometric Distribution
- Statistics Fundamentals Playlist (StatQuest)
