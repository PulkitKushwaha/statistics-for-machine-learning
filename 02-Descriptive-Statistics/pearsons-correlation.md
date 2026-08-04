# Pearson's Correlation

## One-Sentence Summary

Pearson's Correlation measures how strongly two variables move together and in which direction they move.

---

## What Is It?

In the previous topic, we learned about Covariance.

Covariance tells us:

> Do two variables move together?

However, covariance has a problem:

The magnitude depends on the units being used.

This makes interpretation difficult.

Pearson's Correlation solves this problem by standardizing covariance.

It transforms covariance into a value between:

```text
-1 and +1
```

making it much easier to understand.

---

## Why Should I Care?

Many real-world questions involve relationships between variables.

Examples:

- Do study hours relate to exam scores?
- Do advertising costs relate to sales?
- Does sleep affect productivity?
- Do retrieval scores relate to answer quality?

Pearson's Correlation helps quantify those relationships.

---

## The Big Idea

Pearson's Correlation answers two questions:

### Direction

Do variables move:

- Together?
- Opposite each other?

---

### Strength

How strongly do they move together?

---

Covariance only gives direction.

Correlation gives:

- Direction
- Strength

---

## Intuition

Imagine two dancers.

Covariance tells us:

```text
Are they moving together?
```

Pearson's Correlation asks:

```text
How synchronized are they?
```

Perfect synchronization:

```text
+1
```

Perfect opposite movement:

```text
-1
```

No relationship:

```text
0
```

---

## Understanding Correlation Values

### Correlation = +1

Perfect Positive Correlation

As one variable increases:

The other always increases.

Example:

```text
Temperature in Celsius
Temperature in Fahrenheit
```

Perfect relationship.

---

### Correlation = 0

No Linear Relationship

One variable provides no useful information about the other.

---

### Correlation = -1

Perfect Negative Correlation

As one variable increases:

The other always decreases.

Example:

```text
Distance remaining in a race
Distance already completed
```

---

## Rock & Metal Corner

Imagine measuring:

### Variable A

Guitar distortion level

### Variable B

Headbanging intensity

As distortion increases:

Headbanging increases.

Strong positive correlation.

---

Now imagine:

### Variable A

Concert ticket price

### Variable B

Fan attendance

As prices rise:

Attendance may fall.

Negative correlation.

---

## A Simple Example

| Hours Studied | Exam Score |
|---------------|------------|
| 1 | 50 |
| 2 | 60 |
| 3 | 70 |
| 4 | 80 |
| 5 | 90 |

Study time increases.

Scores increase.

Correlation is very close to:

```text
+1
```

---

Now suppose:

| Study Time | Exam Score |
|------------|------------|
| 1 | 80 |
| 2 | 50 |
| 3 | 75 |
| 4 | 60 |
| 5 | 72 |

No obvious pattern.

Correlation is near:

```text
0
```

---

## Why Correlation Is Better Than Covariance

Suppose:

One dataset is measured in:

```text
Meters
```

Another in:

```text
Kilometers
```

Covariance changes.

Correlation remains the same.

This makes correlation easier to compare across datasets.

---

## The Formula (Conceptually)

Pearson's Correlation is:

```text
Standardized Covariance
```

The exact formula is:

Correlation = Covariance / (Standard Deviation of X × Standard Deviation of Y)

You do not need to memorize the formula.

The important idea is:

> Correlation removes the effect of units.

---

## Correlation Does NOT Mean Causation

This is the most famous warning in statistics.

Suppose:

Ice cream sales increase.

Drowning incidents also increase.

Strong positive correlation.

Does ice cream cause drowning?

Of course not.

Both increase because:

```text
Summer temperatures increase.
```

A third variable creates the relationship.

---

## The StatQuest Takeaway

Correlation measures:

- Direction
- Strength

of a linear relationship between two variables.

However:

```text
Correlation ≠ Causation
```

This is one of the most important lessons in all of statistics.

---

## Visual Interpretation

Imagine a scatter plot.

### Correlation ≈ +1

Points form a clear upward line.

---

### Correlation ≈ 0

Points look random.

---

### Correlation ≈ -1

Points form a clear downward line.

---

The closer the points hug a straight line:

The stronger the correlation.

---

## Correlation Does Not Equal Causation

This is one of the most important lessons in all of statistics.

Just because two variables move together does not mean one causes the other.

Correlation tells us:

> Two things are associated.

Causation tells us:

> One thing directly influences the other.

These are very different claims.

---

### The Classic Ice Cream Example

Suppose we observe:

```text
Ice Cream Sales ↑
Drowning Incidents ↑
```

Strong positive correlation exists.

Question:

```text
Does ice cream cause drowning?
```

Of course not.

The real explanation is:

```text
Summer Temperature ↑
        ↓
More Ice Cream
        ↓
More Swimming
        ↓
More Drownings
```

Temperature is the hidden factor driving both variables.

---

### Hidden Variables (Confounding Variables)

A third variable can create a correlation between two other variables.

Example:

```text
Number of Firefighters ↑
Fire Damage ↑
```

Strong positive correlation.

Does hiring firefighters cause damage?

No.

The real cause is:

```text
Large Fire
    ↓
More Firefighters
    ↓
More Damage
```

The fire itself is responsible for both observations.

---

### Reverse Causation

Sometimes the direction of influence is reversed.

Suppose we observe:

```text
Study Time ↑
Exam Scores ↑
```

One explanation:

```text
More Studying
      ↓
Higher Scores
```

Another possibility:

```text
Students Who Enjoy A Subject
         ↓
Study More
         ↓
Score Higher
```

The true causal chain may not be obvious.

---

### Three Possibilities Whenever Correlation Exists

Whenever you observe a correlation, ask:

#### Possibility 1

```text
X causes Y
```

Example:

```text
Studying
    ↓
Exam Scores
```

---

#### Possibility 2

```text
Y causes X
```

Example:

```text
Interest In Subject
        ↓
More Studying
```

---

#### Possibility 3

```text
A Third Variable Causes Both
```

Example:

```text
Motivation
    ↓
More Studying
    ↓
Higher Scores
```

---

### Why This Matters In Machine Learning

Imagine we discover:

```text
Users who buy guitars
also buy audio interfaces.
```

Strong correlation.

Can we conclude:

```text
Buying a guitar causes
someone to buy an audio interface?
```

Not necessarily.

A hidden variable may exist:

```text
Musician
```

which increases the likelihood of buying both.

---

### Why This Matters In AI Systems

Suppose we discover:

```text
Longer Answers
        ↑
User Satisfaction
```

Strong correlation.

Can we conclude:

```text
Longer answers cause satisfaction?
```

Not necessarily.

A more likely explanation could be:

```text
Higher Quality Answers
         ↓
Longer Answers
         ↓
Higher Satisfaction
```

The real driver may be answer quality rather than answer length.

---

### The Mental Model

Imagine two dancers moving together.

Correlation tells us:

```text
The dancers are synchronized.
```

Correlation does NOT tell us:

```text
Who is leading the dance.
```

Maybe:

- Dancer A leads Dancer B
- Dancer B leads Dancer A
- A third dancer leads both

Correlation alone cannot tell the difference.

---

## Pulkit's Mental Model

Correlation tells us that two dancers are moving together.

Causation tells us who is leading the dance.

### Never Forget This

Just because two things move together does not mean one causes the other.

## Machine Learning Connection

Correlation appears everywhere in machine learning.

### Feature Selection

Highly predictive features often show strong correlation with a target variable.

---

### Multicollinearity

Two highly correlated features may create problems in some models.

---

### Exploratory Data Analysis

Correlation matrices are frequently used when understanding datasets.

---

### Linear Regression

Strong correlations often indicate useful predictive relationships.

---

## AI / LLM / RAG Connection

### RAG Evaluation

Do retrieval scores correlate with answer quality?

Correlation helps answer this.

---

### LLM Evaluation

Do confidence scores correlate with correctness?

Correlation helps investigate.

---

### User Analytics

Do longer sessions correlate with higher satisfaction?

---

### Benchmark Analysis

Correlation can reveal relationships between evaluation metrics.

---

## Common Misconceptions

### Correlation Means Causation

False.

This is one of the most common mistakes in statistics.

---

### Correlation Detects Any Relationship

False.

Pearson's Correlation measures linear relationships.

Nonlinear relationships can be missed.

---

### Zero Correlation Means No Relationship Exists

False.

A nonlinear relationship may still be present.

---

### High Correlation Guarantees Good Predictions

False.

Correlation is useful but not sufficient by itself.

---

## Pulkit's Mental Model

Covariance tells us whether two dancers move together.

Correlation tells us how synchronized the dancers are.

---

## Interview Questions

### What is Pearson's Correlation?

A measure of the direction and strength of a linear relationship between two variables.

---

### What range can correlation take?

From:

```text
-1 to +1
```

---

### What does a correlation of +1 mean?

Perfect positive relationship.

---

### What does a correlation of -1 mean?

Perfect negative relationship.

---

### Does correlation imply causation?

No.

Correlation does not prove causation.

---

## Related Topics

- Covariance
- Variance
- Standard Deviation
- Linear Regression
- Feature Selection
- Correlation Matrices
- Principal Component Analysis (PCA)

---

## References

- StatQuest: Pearson's Correlation, Clearly Explained!!!
- Statistics Fundamentals Playlist (StatQuest)
