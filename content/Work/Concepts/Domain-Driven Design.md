---
class: note
tags:
source: https://lukasniessen.medium.com/domain-driven-design-ddd-is-a-particular-way-to-structure-your-app-efd4e6865935
related:
author:
date: 2026-03-11
updated: 2026-03-11 20:02:24
aliases:
---
## DDD: Domain-Driven Design

![[Pasted image 20260311200409.png]]
- _The core idea is to put the business domain at the center. We don’t want to structure our app in “technology layers” like database, business, user interface but rather around “business layers”._

**Where is DDD Used?**

- used at code level
- for naming classes, structuring packages, slicing etc
- also used at system design. very commonly in microservices architectures.

The idea is simple. In microservices we want every service to be totally independent. So the question arises, how to we split our app? What boundaries do we want? One way to answer this is DDD: every bounded context becomes a microservice. By doing this we get that every service has a dedicated business purpose and is _“business-wise cohesive”_. And every aggregate belongs to exactly one service. This gives us a very nice and focused way of splitting our app. And time has shown that this approach works very well, it’s the most popular approach for splitting a monolith into microservices.

**KEY CONCEPT:**

_→ eg. event storming - building a banking app_

- **Domain Events**
    - things that can happen in our system, facts that business people care about
    - written in past tense because they already happened
    - _money sent, money received, account opened, payment failed, balance updated_
- **Commands**
    - what commands cause these events?
    - are decisions made by users
    - _send money → money sent, open account → account opened, process payment → payment failed (sometimes)_
- **Aggregates** ⭐
    - a cohesive bundle of related events and commands
    - identify things that “belong together”
    - a collection of related objects managed as a single unit with its own lifecycle
    - do this with all the events and commands
    - _Account_
        - _send money_
        - _receive money_
        - _have its balance updated_
        - _be opened or closed_
    - _transaction agg, payment method agg, regulatory report agg_
- **Bounded Contexts** ⭐
    - a boundary in our big business picture
    - everything in that context is somewhat related, in terms of business
    - ‼️ a bounded context is made up of aggregates as you see, it can be just one or it can be multiple aggregates
        - ❗an aggregate should never be split across different contexts, should be in exactly one context, fully contained
    - _Account Management Context:_
        - _Account aggregate_
        - _Customer aggregate_
    - _Payment Processing Context:_
        - _Transaction aggregate_
        - _Payment Method aggregate_
    - _Compliance Context:_
        - _Audit Log aggregate_
        - _Regulatory Report aggregate_
- **Ubiquitous Language** ⭐
    - we use one language that both teams understand (dev people and business people)
    - bad (generic)
        ```cpp
        class Arrangement {
            String type; // Could be loan, deposit, whatever
            BigDecimal amount;
        }
        ```
    - good (domain language)
        ```cpp
        class SavingsAccount {
            AccountNumber accountNumber;
            Money balance;
            
            void withdraw(Money amount) {
                if (balance.isLessThan(amount)) {
                    throw new InsufficientFundsException();
                }
                // ... rest of withdrawal logic
            }
        }
        ```
    