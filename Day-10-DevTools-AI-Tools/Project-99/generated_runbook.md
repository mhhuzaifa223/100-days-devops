# Generated DevOps Incident Runbook

Generated (UTC): 2026-10-13T06:35:39.011235+00:00

## Incident Summary
- API health check failed or returned HTTP 503.
- High CPU utilization was reported.

## Investigation Steps
1. Check application logs around the incident timestamp.
2. Verify API health and dependent services.
3. Review recent deployments and configuration changes.
4. Confirm the endpoint and dependency connectivity.
5. Inspect CPU metrics over the incident window.
6. Identify resource-intensive processes or containers.
7. Compare CPU usage with request volume and recent changes.

## Recovery Verification
1. Recheck the API health endpoint.
2. Confirm error rates and resource usage have returned to acceptable levels.
3. Monitor for recurring failures before closing the incident.

## Escalation
Escalate to the service owner if the API remains unavailable, customer impact continues, or the cause cannot be established.

## Safety Notes
- Treat these steps as a starting point, not a confirmed diagnosis.
- Do not restart services or change production resources without authorization.
- CPU usage may be correlated with the outage without being its root cause.
