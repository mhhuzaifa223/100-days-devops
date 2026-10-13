# Project 90: Software Supply Chain Security

## Objective
Generate a Software Bill of Materials (SBOM) for a container image and scan its components for known vulnerabilities.

## Tools
- Trivy
- Docker image: nginx:1.28
- CycloneDX SBOM format

## Implementation
1. Generated a CycloneDX SBOM from the nginx:1.28 container image.
2. Saved the component inventory as sbom.json.
3. Scanned the SBOM with Trivy's vulnerability scanner.

## Results
Trivy reported 801 vulnerability records for the Debian 13.4 components represented in the SBOM.

This count is a scan result, not a count of confirmed exploitable vulnerabilities. Severity, package status, fixed versions, and applicability should be reviewed before deciding on remediation.

## Key Learnings
- An SBOM inventories software components and dependencies.
- Vulnerability scanning helps identify components associated with known CVEs.
- SBOMs support supply-chain transparency and incident response.
- A vulnerability count alone does not establish exploitability or risk.

## Scope
This was a local image and SBOM scan. No cloud resources or Kubernetes cluster were used.
