# Project 88: HashiCorp Vault Secrets Integration

## Objective
Learn to store and retrieve application secrets using HashiCorp Vault instead of hardcoding credentials in source code.

## Tools
- Docker
- HashiCorp Vault
- Vault CLI
- KV secrets engine

## Implementation
1. Started Vault in development mode using Docker.
2. Bound the Vault port to localhost only.
3. Checked Vault status and verified it was initialized and unsealed.
4. Stored sample API and database credentials in the KV secrets engine.
5. Retrieved the stored values using the Vault CLI.

## Commands Used
The lab used `vault status`, `vault kv put`, and `vault kv get` inside the running Vault container.

## Key Learnings
- Vault centralizes secrets management.
- Applications can retrieve credentials at runtime instead of embedding them in source code.
- Vault tokens control access to secrets.
- Production deployments require persistent storage, secure authentication, TLS, policies, and proper token handling.

## Important Security Note
This project uses Vault development mode with in-memory storage and a training-only root token. It is for local learning only, not production use. Data is lost when the development server stops.

## Result
Successfully stored and retrieved two training-only secrets from Vault.
