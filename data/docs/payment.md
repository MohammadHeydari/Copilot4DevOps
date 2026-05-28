# Payment Service Overview

The Payment Service handles all transaction processing for the platform.

## Architecture
- Uses bank API for transaction validation
- Depends on Redis cache for idempotency
- Communicates with Fraud Detection Service

## Common Incidents

### Payment Timeout
- Symptom: Transactions stuck in pending state
- Root Cause: Bank API latency or downtime
- Detection: Increased response time > 5s
- Fix: Retry with exponential backoff + fallback provider

### Duplicate Payment
- Symptom: User charged twice
- Root Cause: Missing idempotency key
- Fix: Enable request hashing and Redis lock

### High Failure Rate
- Symptom: 5xx errors spike
- Root Cause: Upstream bank API instability
- Fix: Circuit breaker activation + fallback routing