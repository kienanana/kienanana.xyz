---
class: note
tags:
source: https://learn.microsoft.com/en-us/azure/architecture/patterns/saga
related:
author:
date: 2026-03-11
updated: 2026-03-11 20:10:17
aliases:
---
## Challenges in Microservice Architectures

- Microservices architectures typically assign a dedicated database to each microservice.
- this complicates cross-service data consistency
- architectures that rely on interprocess communication, or traditional transaction models like two-phase commit protocol, are often better suited for the Saga pattern.

## Solution: SAGA

![[Pasted image 20260311201055.png]]

- manages transactions by breaking them into a sequence of local transactions
- Each local transaction:
    1. Completes its work atomically within a single service.
    2. Updates the service's database.
    3. Initiates the next transaction via an event or message.
- If a local transaction fails, the saga performs a series of _compensating transactions_ to reverse the changes that the preceding local transactions made.

**Key concepts in the Saga pattern**

- **Compensable transactions** can be undone or compensated for by other transactions with the opposite effect. If a step in the saga fails, compensating transactions undo the changes that the compensable transactions made.
- **Pivot transactions** serve as the point of no return in the saga. After a pivot transaction succeeds, compensable transactions are no longer relevant. All subsequent actions must be completed for the system to achieve a consistent final state. A pivot transaction can assume different roles, depending on the flow of the saga:
    - **Irreversible or noncompensable transactions** can't be undone or retried.
    - **The boundary between reversible and committed** means that the pivot transaction can be the last undoable, or compensable, transaction. Or it can be the first retryable operation in the saga.
- **Retryable transactions** follow the pivot transaction. Retryable transactions are idempotent and help ensure that the saga can reach its final state, even if temporary failures occur. They help the saga eventually achieve a consistent state.

**Choreography**

In the choreography approach, services exchange events without a centralized controller. With choreography, each local transaction publishes domain events that trigger local transactions in other services.

![Diagram that shows a saga by using choreography.](https://learn.microsoft.com/en-us/azure/architecture/patterns/_images/choreography-pattern.png)

|Benefits of choreography|Drawbacks of choreography|
|---|---|
|Good for simple workflows that have few services and don't need a coordination logic.|Workflow can be confusing when you add new steps. It's difficult to track which commands each saga participant responds to.|
|No other service is required for coordination.|There's a risk of cyclic dependency between saga participants because they have to consume each other's commands.|
|Doesn't introduce a single point of failure because the responsibilities are distributed across the saga participants.|Integration testing is difficult because all services must run to simulate a transaction.|

**Orchestration**

In orchestration, a centralized controller, or _orchestrator_, handles all the transactions and tells the participants which operation to perform based on events. The orchestrator performs saga requests, stores and interprets the states of each task, and handles failure recovery by using compensating transactions.

![Diagram that shows a saga using orchestration.](https://learn.microsoft.com/en-us/azure/architecture/patterns/_images/orchestrator.png)

| Benefits of orchestration                                             | Drawbacks of orchestration                                                            |
| --------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| Better suited for complex workflows or when you add new services.     | Other design complexity requires an implementation of a coordination logic.           |
| Avoids cyclic dependencies because the orchestrator manages the flow. | Introduces a point of failure because the orchestrator manages the complete workflow. |
| Clear separation of responsibilities simplifies service logic.        |                                                                                       |