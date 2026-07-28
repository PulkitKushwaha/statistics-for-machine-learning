# Hypothesis Testing and The Null Hypothesis

## One-Sentence Summary

Hypothesis testing is a method for deciding whether the evidence in our data is strong enough to challenge the default explanation.

---

## What Is It?

Suppose you observe something interesting.

Maybe:

- A new medicine appears effective.
- A marketing campaign seems successful.
- A machine learning model appears better.
- A new retrieval strategy improves RAG performance.

The key question becomes:

> Is this difference real, or could it have happened by chance?

Hypothesis testing helps answer that question.

It provides a structured framework for evaluating evidence.

---

## Why Should I Care?

Without hypothesis testing, we could easily fool ourselves.

Imagine flipping a coin 10 times and getting:

```text
8 Heads
2 Tails
```

You might think:

> This coin seems unfair.

But is it really?

Or did randomness simply produce an unusual result?

Hypothesis testing helps distinguish:

- Genuine effects
- Random variation

---

## The Big Idea

Statistics begins with a skeptical position.

Instead of immediately believing a claim, we start by assuming:

> Nothing special is happening.

This assumption is called the Null Hypothesis.

Then we ask:

> Is the observed evidence so unusual that we should reject this explanation?

This process is called Hypothesis Testing.

---

# The Null Hypothesis

## What Is It?

The Null Hypothesis is the default explanation.

It typically states:

> There is no effect.

or

> There is no difference.

or

> Nothing unusual is happening.

We represent it as:

```text
H₀
```

(pronounced "H naught")

---

## Examples

### Coin Example

Null Hypothesis:

```text
The coin is fair.
```

---

### Medicine Example

Null Hypothesis:

```text
The medicine has no effect.
```

---

### A/B Testing Example

Null Hypothesis:

```text
The new design performs the same as the old design.
```

---

### Machine Learning Example

Null Hypothesis:

```text
Model A and Model B perform equally well.
```

---

## Intuition

The null hypothesis is the story we assume is true until strong evidence suggests otherwise.

Think of it as the default explanation.

---

## Courtroom Analogy

This is one of the most useful analogies in all of statistics.

Imagine a courtroom.

The defendant starts as:

```text
Innocent
```

not because we know they are innocent,

but because innocence is the default assumption.

Evidence must be provided before we change our belief.

Hypothesis testing works the same way.

The null hypothesis starts as our default assumption.

Evidence must be strong before we reject it.

---

## Rock & Metal Corner

Suppose a band claims:

> "Our new album is significantly better than our previous one."

As a statistician, you start with:

```text
Null Hypothesis:
There is no real difference.
```

Then you collect ratings and analyze the evidence.

The burden of proof belongs to the claim.

Not to the default assumption.

---

# Hypothesis Testing Process

## Step 1

Create a Null Hypothesis.

Example:

```text
The coin is fair.
```

---

## Step 2

Collect Data.

Example:

```text
10 flips
8 heads
2 tails
```

---

## Step 3

Ask:

> How surprising is this result if the null hypothesis is true?

---

## Step 4

If the result is extremely surprising:

Reject the null hypothesis.

Otherwise:

Keep the null hypothesis.

---

# Important Principle

Notice what statisticians do NOT say.

They do NOT say:

```text
The null hypothesis is true.
```

Instead they say:

```text
We do not have enough evidence to reject it.
```

This distinction is extremely important.

---

## Worked Example

Imagine a manufacturing process.

The target weight is:

```text
100 grams
```

Null Hypothesis:

```text
The process is operating normally.
```

You collect product samples.

Suppose the average weight appears unusually different.

You then ask:

> If the process were actually operating normally, how likely would these observations be?

If the results seem highly unusual,

you may reject the null hypothesis.

---

## The StatQuest Takeaway

Hypothesis testing is not about proving things true.

It is about evaluating evidence.

The null hypothesis acts as the default explanation.

We keep it until the data becomes too difficult to explain under that assumption.

---

## Why Statistics Uses This Approach

Because randomness constantly creates unusual results.

Without hypothesis testing:

- We would overreact to noise.
- We would see patterns that do not exist.
- We would make poor decisions.

Hypothesis testing forces us to demand evidence.

---

## Machine Learning Connection

Hypothesis testing appears throughout machine learning.

### Model Comparison

Suppose:

```text
Model A Accuracy = 91%
Model B Accuracy = 92%
```

Is that 1% improvement meaningful?

Or random?

Hypothesis testing helps answer this.

---

### Feature Evaluation

Does a new feature genuinely improve performance?

Or is the improvement noise?

---

### Experimentation

Many ML experiments rely on hypothesis testing frameworks.

---

## AI / LLM / RAG Connection

### Prompt Testing

Suppose Prompt B seems better than Prompt A.

Is the improvement real?

Or random variation?

Hypothesis testing helps evaluate this.

---

### RAG Evaluation

A retrieval strategy may appear better.

Statistical testing helps determine whether the improvement is meaningful.

---

### LLM Benchmarking

Model comparisons often rely on statistical significance testing.

Without it, small fluctuations may be misleading.

---

## Common Misconceptions

### Rejecting The Null Hypothesis Proves The Alternative

False.

It only means the evidence is inconsistent with the null hypothesis.

---

### Failing To Reject Means The Null Is True

False.

It means the evidence is not strong enough.

---

### Hypothesis Testing Eliminates Uncertainty

False.

It helps manage uncertainty.

It does not eliminate it.

---

### Unusual Results Mean Something Important Happened

Not always.

Randomness can produce surprising outcomes.

---

## Pulkit's Mental Model

Hypothesis testing is a courtroom trial for ideas.

The null hypothesis is innocent until strong evidence proves otherwise.

---

## Interview Questions

### What is the null hypothesis?

A default explanation that assumes no effect or no difference exists.

---

### What is hypothesis testing?

A process for evaluating whether observed evidence is strong enough to challenge the null hypothesis.

---

### What does rejecting the null hypothesis mean?

The observed evidence is difficult to explain if the null hypothesis were true.

---

### What does failing to reject the null hypothesis mean?

The evidence is not strong enough to reject it.

---

### Why is hypothesis testing important?

It helps distinguish genuine patterns from random variation.

---

## Related Topics

- Population and Estimated Parameters
- Probability Distributions
- Normal Distribution
- Alternative Hypotheses
- p-values
- Statistical Power
- Confidence Intervals

---

## References

- StatQuest: Hypothesis Testing and The Null Hypothesis, Clearly Explained!!!
- Statistics Fundamentals Playlist (StatQuest)
