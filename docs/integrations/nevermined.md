# Integrating Nevermined with Olas

This guide explains how to integrate Nevermined's subscription and payment services with Olas autonomous agents and services. Nevermined provides monetization capabilities, subscription management, and usage accounting for AI agents in the Olas ecosystem.

## What is Nevermined?

Nevermined is a data ecosystem that enables subscription-based services within the Olas network. It provides:

- Monetization capabilities for AI agents
- Usage monitoring and accounting
- Subscription management (time-based or request-based)
- Payment processing (both fiat and crypto)

## Integration Options

There are multiple ways to integrate Nevermined with Olas:

### 1. Basic Integration (No Code Modification)

For simple monetization without advanced features:

1. **Register your Olas agent in the Nevermined App**
2. **Define pricing and access models**

This approach is suitable if you only need:

- Basic monetization
- Simple usage accounting
- Time or credit-based access control

### 2. Advanced Integration (Using Payment Libraries)

For more sophisticated features, integrate the Nevermined Payment Libraries into your Olas agent:

- Purchase access to other agents
- Query other agents using the Nevermined Query Protocol
- Implement dynamic credit charging based on request complexity

## Step-by-Step Integration Guide

### Prerequisites

- An existing Olas agent or service
- Python >= 3.10 (for Python implementations)
- Node.js >= 16 (for TypeScript/JavaScript implementations)
- A Nevermined account
- (Optional) A Stripe account for fiat payments

### Basic Integration (No Code Changes)

1. **Register your Olas agent with Nevermined**

   Visit the [Nevermined App](https://app.nevermined.io/) and:
   
   - Create an account
   - Select "Register AI Agent"
   - Provide your agent's HTTP endpoint
   - Generate and securely store a JWT authentication token
   - Assign a unique identifier to your service

2. **Create a Payment Plan**

   In the Nevermined App:
   
   - Choose between Time-Based or Credit-Based access
   - Set pricing (free or paid)
   - Define credit requirements per request (for request-based plans)
   - Configure payment options (fiat, crypto, or both)

3. **Configure Mech to Use Nevermined**

   Update your Mech configuration to enable Nevermined subscription:
   
   ```json
   {
     "mech": {
       "payment_model": "nevermined",
       "nevermined_plan_id": "YOUR_NEVERMINED_PLAN_DID"
     }
   }
   ```

### Advanced Integration (With Payment Libraries)

#### 1. Install the Nevermined Payment Libraries

For Python:
```bash
pip install nevermined-payments
```

For TypeScript/JavaScript:
```bash
npm install @nevermined-io/payments
```

#### 2. Initialize the Payments Client

**Python:**
```python
from nevermined_payments import Payments, Environment

payment = Payments(
    app_id="your_olas_agent", 
    nvm_api_key="YOUR_NEVERMINED_API_KEY", 
    version="1.0.0", 
    environment=Environment.get_environment("development")  # or "production"
)
```

**TypeScript:**
```typescript
import { Payments, getPaymentsInstance, Environment } from '@nevermined-io/payments'

const payments = getPaymentsInstance(
  "YOUR_NEVERMINED_API_KEY",
  "development"  // or "production"
)
```

#### 3. Implement the Agent Callback Function

Create a callback function that processes tasks when they're received from users:

**Python:**
```python
async def process_task(data):
    # Get the step information
    step = payment.query.get_step(data["step_id"])
    
    # Check if the step is pending
    if step.step_status != "pending":
        return
    
    # Log the start of processing
    await payment.query.log_task(
        TaskLog(task_id=step.task_id, message="Processing request...", level="info")
    )
    
    # Process the request with your Olas agent logic
    result = your_olas_agent_logic(step.input_query)
    
    # Update the step with the result
    payment.query.update_step(
        did=data["did"],
        task_id=data["task_id"],
        step_id=data["step_id"],
        step={
            "step_id": data["step_id"],
            "task_id": data["task_id"],
            "step_status": "completed",
            "output": result,
            "is_last": True,
        },
    )
    
    # Optional: Charge dynamically based on complexity
    # cost = calculate_cost_based_on_complexity(step.input_query)
    # Include "cost": cost in the step update above
```

#### 4. Subscribe to the Query Protocol

Set up your agent to listen for incoming tasks:

**Python:**
```python
async def main():
    # Initialize your agent
    agent = YourOlasAgent(payment)
    
    # Subscribe to the query protocol with your callback
    subscription_task = asyncio.get_event_loop().create_task(
        payment.query.subscribe(agent.process_task, join_account_room=True)
    )
    
    try:
        await subscription_task
    except asyncio.CancelledError:
        print("Subscription task was cancelled")

if __name__ == "__main__":
    asyncio.run(main())
```

**TypeScript:**
```typescript
async function main() {  
  const payments = getPaymentsInstance(NVM_API_KEY, NVM_ENVIRONMENT)
  console.log(`Connected to Nevermined Network: ${NVM_ENVIRONMENT}`)  

  // Subscribe to receive tasks
  await payments.query.subscribe(processSteps, {
    join_account_room: true
  })
}

main().catch(console.error)
```

## Advanced Features

### Multi-Step Processing

You can implement multi-step processing for complex agent workflows:

```python
async def process_task(data):
    step = payment.query.get_step(data["step_id"])
    
    if step.name == "init":
        # Create additional steps for a multi-step workflow
        transcript_step_id = generate_step_id()
        payment.query.create_steps(
            did=step.did,
            task_id=step.task_id,
            steps={
                "steps": [
                    {
                        "task_id": step.task_id,
                        "step_id": transcript_step_id,
                        "input_query": step.input_query,
                        "name": "process_data",
                        "predecessor": step.step_id,
                        "is_last": False,
                        "order": 2,
                    },
                    {
                        "task_id": step.task_id,
                        "step_id": generate_step_id(),
                        "predecessor": transcript_step_id,
                        "input_query": "",
                        "name": "generate_output",
                        "is_waiting": True,
                        "is_last": True,
                        "order": 3,
                    },
                ]
            },
        )
        # Complete the init step
        payment.query.update_step(...)
    
    elif step.name == "process_data":
        # Process the first real step
        # ...
        
    elif step.name == "generate_output":
        # Process the final step
        # ...
```

### Agent-to-Agent Integration

You can have your agent call other agents in the Nevermined ecosystem:

```python
# Check if we have enough credits to call another agent
balance_result = await payments.get_plan_balance(OTHER_AGENT_PLAN_DID)

if balance_result.balance < required_credits:
    # Order more credits if needed
    await payments.order_plan(OTHER_AGENT_PLAN_DID)

# Get access configuration for the other agent
access_config = await payments.query.get_service_access_config(OTHER_AGENT_DID)

# Create a task for the other agent
task_result = await payments.query.create_task(
    OTHER_AGENT_DID,
    {
        "query": input_data,
        "name": "external_processing",
        "additional_params": [],
        "artifacts": []
    },
    access_config,
    handle_task_updates
)
```

## Dynamic Credit Charging

For request-based plans, you can dynamically charge credits based on request complexity:

```python
# Calculate cost based on complexity
def calculate_cost(input_query):
    # Your logic to determine cost based on complexity
    tokens = len(input_query.split())
    if tokens < 100:
        return 1  # Low complexity
    elif tokens < 500:
        return 3  # Medium complexity
    else:
        return 5  # High complexity

# In your update_step call
payment.query.update_step(
    did=data["did"],
    task_id=data["task_id"],
    step_id=data["step_id"],
    step={
        "step_id": data["step_id"],
        "task_id": data["task_id"],
        "step_status": "completed",
        "output": result,
        "is_last": True,
        "cost": calculate_cost(step.input_query)  # Dynamic cost
    },
)
```

## Embedding Payment Plans

To enable users to purchase plans directly from your website or application:

1. Get your Payment Plan widget code from the Nevermined App
2. Add it to your website
3. Users will be redirected to Nevermined for checkout and then back to your site

## Best Practices

1. **Secure API Keys**: Never expose your Nevermined API keys in client-side code
2. **Error Handling**: Implement robust error handling for network and payment issues
3. **Logging**: Use the logging functions to provide visibility into task progress
4. **Cost Transparency**: Make pricing clear to users before they subscribe
5. **Test in Development**: Use the development environment for testing before going live

## Troubleshooting

- **Task Status Not Updating**: Ensure you're properly calling `update_step` with the correct parameters
- **Subscription Issues**: Verify your Nevermined API key is valid and has the correct permissions
- **Credit Redemption Failures**: Check if the user has sufficient credits for the request
- **Connection Problems**: Ensure your agent has stable network connectivity to Nevermined servers

By following this guide, you'll be able to integrate Nevermined with your Olas agent, offering subscription-based access to your services and unlocking new monetization opportunities.
