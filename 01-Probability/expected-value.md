# Expected Value

## One-Sentence Summary

Expected Value is the probability-weighted average outcome we expect to observe over the long run.

---

## What Is It?

Expected Value is one of the most important concepts in probability and statistics.

It answers the question:

> On average, what should I expect if I repeat this process many times?

Notice that Expected Value is not necessarily what happens next.

Instead, it represents the long-run average outcome.

---

## Why Should I Care?

Expected Value appears everywhere:

- Casinos
- Insurance
- Investing
- Machine Learning
- Artificial Intelligence
- Product Decisions
- A/B Testing

Whenever we make decisions under uncertainty, Expected Value helps us quantify what outcomes are worth on average.

---

## The Big Idea

Imagine playing a game repeatedly.

Sometimes you win.

Sometimes you lose.

Instead of asking:

> What will happen next?

Expected Value asks:

> What happens on average if I play this game thousands of times?

It transforms uncertainty into a meaningful average.

---

## Intuition

Suppose a game works like this:

If you roll a die:

```text
Roll a 6
Win $60

Anything else
Win $0
```

Question:

> What is this game worth on average?

At first glance:

```text
Potential Prize = $60
```

But you only win occasionally.

Expected Value accounts for both:

- Outcome Size
- Outcome Probability

---

## Everyday Analogy

Imagine ordering from a mystery snack box.

Possible outcomes:

| Item | Probability |
|--------|------------|
| Small Snack | 50% |
| Medium Snack | 30% |
| Large Snack | 20% |

Expected Value tells you:

> What size snack can I reasonably expect on average?

It's the average future you should plan for.

---

## Rock & Metal Corner

Imagine a festival ticket lottery.

Possible outcomes:

| Outcome | Probability |
|----------|-------------|
| Back Row | 50% |
| Mid Section | 40% |
| Front Row | 10% |

Expected Value describes the average seat quality you would expect if you entered many lottery drawings.

It helps transform chance into expectation.

---

## How Expected Value Works

The core idea is simple:

Multiply each outcome by its probability.

Then add everything together.

That total becomes the expected value.

---

## Formula

Expected Value is often written as:

```text
E(X)
```

The formula is:

```text
Expected Value =
Σ (Outcome × Probability)
```

Read it as:

```text
Add up all
Outcome × Probability
pairs.
```

Focus on the intuition more than the notation.

---

## Dice Example

Suppose we roll a fair die.

Possible outcomes:

| Outcome | Probability |
|-----------|-------------|
| 1 | 1/6 |
| 2 | 1/6 |
| 3 | 1/6 |
| 4 | 1/6 |
| 5 | 1/6 |
| 6 | 1/6 |

Expected Value:

```text
(1 × 1/6)
+
(2 × 1/6)
+
(3 × 1/6)
+
(4 × 1/6)
+
(5 × 1/6)
+
(6 × 1/6)
```

Result:

```text
3.5
```

---

## The Strange Result

A die never shows:

```text
3.5
```

So how can the expected value be:

```text
3.5?
```

Because Expected Value is not predicting the next outcome.

It predicts the long-run average outcome.

After many rolls:

```text
Average ≈ 3.5
```

---

## Lottery Example

Suppose:

| Outcome | Probability |
|----------|------------|
| $100 | 10% |
| $0 | 90% |

Expected Value:

```text
100 × 0.10
+
0 × 0.90
=
10
```

Expected Value:

```text
$10
```

The lottery ticket has an average value of $10.

---

## The StatQuest Takeaway

Expected Value combines:

- Probability
- Outcomes

into a single meaningful number.

It answers:

> What should I expect on average if this process repeats many times?

It is one of the most useful concepts in all of probability.

---

## Why Expected Value Matters

Expected Value is the foundation of rational decision making under uncertainty.

Instead of focusing on:

```text
Best Case
```

or

```text
Worst Case
```

Expected Value focuses on:

```text
Average Case
```

weighted by probability.

---

## Machine Learning Connection

Expected Value appears throughout machine learning.

### Loss Functions

Training often involves minimizing expected loss.

---

### Risk Minimization

Many ML algorithms seek to minimize expected error.

---

### Reinforcement Learning

Agents choose actions that maximize expected future reward.

This idea is fundamentally based on Expected Value.

---

### Model Evaluation

Expected performance over future data is often more important than performance on a single dataset.

---

## AI / LLM / RAG Connection

### Agentic AI

Agents frequently evaluate actions based on expected outcomes.

---

### Reinforcement Learning

Expected cumulative reward drives decision making.

---

### RAG Systems

Retrieval systems try to maximize expected answer quality.

---

### LLM Decision Making

Many AI systems choose actions that optimize expected utility rather than guaranteeing perfect outcomes.

---

## Expected Value vs Reality

A common mistake:

Expected Value tells us:

```text
Average Outcome
```

It does NOT tell us:

```text
What happens next.
```

Reality can still fluctuate.

Expected Value describes long-run behavior.

---

## Common Misconceptions

### Expected Value Predicts The Future

False.

It predicts the average future over many repetitions.

---

### Expected Value Must Be A Possible Outcome

False.

The expected value of a die is:

```text
3.5
```

even though 3.5 can never occur.

---

### High Expected Value Guarantees Profit

False.

Expected Value is a long-run average.

Short-term results can differ dramatically.

---

### Expected Value Removes Uncertainty

False.

It summarizes uncertainty.

It does not eliminate uncertainty.

---

## Pulkit's Mental Model

Expected Value is the average future we expect to experience.

### Reminder

Expected Value transforms uncertainty into a probability-weighted average.

It tells us what outcomes are worth on average.

---

## Interview Questions

### What is Expected Value?

The probability-weighted average outcome of a random process.

---

### Why is Expected Value important?

It helps quantify long-run average outcomes and supports decision making under uncertainty.

---

### Can Expected Value be a value that never actually occurs?

Yes.

The expected value of a die is 3.5 even though no roll ever produces 3.5.

---

### How is Expected Value calculated?

Multiply each outcome by its probability and add the results.

---

### Where is Expected Value used in machine learning?

Loss functions, reinforcement learning, risk minimization, and model evaluation.

---

## Related Topics

- Probability
- Conditional Probability
- Bayes' Theorem
- Probability Distributions
- Reinforcement Learning
- Decision Theory
- Utility Functions

---

## References

- StatQuest: Expected Value, Clearly Explained!!!
- Statistics Fundamentals Playlist (StatQuest)
