# Conditional Probability

## One-Sentence Summary

Conditional probability measures the probability of an event occurring when we already know that another event has happened.

---

## What Is It?

So far, probability has answered questions like:

> What is the chance of rain tomorrow?

Conditional probability asks a more specific question:

> What is the chance of rain tomorrow if the sky is already dark and cloudy?

Notice the difference.

The second question includes extra information.

That additional information changes the probability.

This is the essence of conditional probability.

---

## Why Should I Care?

Most real-world decisions happen under conditions.

Examples:

- What's the chance a patient has a disease if a test result is positive?
- What's the chance an email is spam if it contains certain words?
- What's the chance a customer will buy if they already clicked an advertisement?
- What's the chance a retrieval result is relevant if its similarity score is high?

Conditional probability helps us update our beliefs using new information.

---

## The Big Idea

Probability answers:

> What is likely?

Conditional probability answers:

> What is likely now that I know something else?

As new evidence arrives, probabilities should change.

---

## Intuition

Imagine a deck of cards.

Question 1:

> What is the probability of drawing a King?

Answer:

```text
4 / 52
```

---

Now suppose someone tells you:

> The card is definitely a Face Card.

Suddenly the probability changes.

There are:

```text
12 Face Cards
```

and

```text
4 Kings
```

So the probability becomes:

```text
4 / 12
```

The additional information changed the probability.

---

## Detective Analogy

Imagine a detective investigating a theft.

Initially:

```text
Suspect A

20% likely
```

A new piece of evidence appears.

The probability changes.

The detective updates their belief.

Conditional probability is the mathematics of updating beliefs using evidence.

This idea becomes extremely important when we study Bayes' Theorem.

---

## Rock & Metal Corner

Imagine attending a metal festival.

Question:

> What is the probability a randomly selected attendee likes progressive metal?

Now suppose you learn:

> The attendee is wearing a Dream Theater shirt.

That new information changes the probability dramatically.

Conditional probability measures how much that evidence should change your belief.

---

## Understanding The Notation

Conditional probability is written as:

```text
P(A | B)
```

This is read as:

```text
Probability of A given B
```

or

```text
Probability of A assuming B has already happened
```

---

Example:

```text
P(Rain | Cloudy)
```

means:

```text
Probability of rain given that it is cloudy.
```

---

## The Formula

Conditional probability is defined as:

```text
P(A | B) = P(A and B) / P(B)
```

Do not focus on memorizing this immediately.

Focus on the intuition first.

The formula is simply adjusting probability based on new information.

---

## Why The Formula Makes Sense

Imagine:

```text
A = Rain

B = Cloudy
```

Instead of considering all possible days,

we only consider:

```text
Cloudy Days
```

The probability space gets smaller.

We "zoom in" on the cases where B is true.

Then we ask:

> Among those cases, how often does A occur?

That is conditional probability.

---

## Worked Example

Suppose a class contains:

| Student Type | Count |
|--------------|--------|
| Plays Guitar | 30 |
| Doesn't Play Guitar | 70 |

Total:

```text
100 students
```

---

Now suppose:

```text
20 students
```

both:

- Play Guitar
- Like Metal Music

And:

```text
30 students
```

play guitar.

Question:

> What is the probability a student likes metal music given that they play guitar?

Calculation:

```text
20 / 30
```

Result:

```text
66.7%
```

---

## Visual Explanation

Think of conditional probability as filtering.

Start with:

```text
All Students
```

Then filter:

```text
Only Guitar Players
```

Now calculate probabilities only within that smaller group.

Conditional probability is probability after filtering.

---

## The StatQuest Takeaway

The key insight is:

> New information changes probabilities.

Conditional probability formalizes that process.

Every time we gain evidence, we should update our beliefs.

---

## Why This Matters

Many important statistical ideas depend on conditional probability.

Examples:

- Bayes' Theorem
- Naive Bayes
- Medical Testing
- Risk Analysis
- Machine Learning Classification

Without conditional probability, these topics would not exist.

---

## Machine Learning Connection

Conditional probability appears throughout machine learning.

### Spam Detection

Question:

```text
What is the probability this email is spam
given that it contains specific words?
```

---

### Recommendation Systems

Question:

```text
What is the probability this user likes a product
given their previous behavior?
```

---

### Classification Models

Many classification models are built around conditional probabilities.

---

## AI / LLM / RAG Connection

### RAG Systems

Question:

```text
What is the probability a document is relevant
given its similarity score?
```

---

### AI Reasoning

Modern AI systems continuously update beliefs using new evidence.

This is fundamentally connected to conditional probability.

---

### LLM Prediction

Given the previous words:

```text
The capital of France is ...
```

The model calculates:

```text
Probability of next tokens
given previous tokens.
```

This is a conditional probability problem.

---

## Common Misconceptions

### Conditional Probability Is The Same As Regular Probability

False.

Additional information changes the probability.

---

### P(A | B) Is The Same As P(B | A)

False.

These values can be completely different.

This misunderstanding is one of the main reasons Bayes' Theorem exists.

---

### New Information Doesn't Matter

False.

Conditional probability exists precisely because information changes probability.

---

### Conditional Probability Proves Things

False.

It updates beliefs.

It does not provide certainty.

---

## Pulkit's Mental Model

Probability asks:

"What is likely to happen?"

Conditional probability asks:

"What is likely to happen now that I know something else?"

---

## Interview Questions

### What is conditional probability?

The probability of an event occurring given that another event has already occurred.

---

### What does P(A | B) mean?

The probability of A given B.

---

### Why does conditional probability matter?

Because new information changes probability.

---

### Is P(A | B) always equal to P(B | A)?

No.

They are often very different.

---

### What major concept is built on conditional probability?

Bayes' Theorem.

---

## Related Topics

- Probability Distributions
- Bayes' Theorem
- Expected Value
- Naive Bayes
- Statistical Inference
- AI Reasoning

---

## References

- StatQuest: Conditional Probabilities, Clearly Explained!!!
- Statistics Fundamentals Playlist (StatQuest)
