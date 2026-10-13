# Project 106 — Prometheus + Grafana Monitoring

## Goal
Monitor Kubernetes health and metrics using Prometheus and Grafana.

## Tools
- Kubernetes (Kind)
- Prometheus
- Grafana
- Helm

## Verification
- Grafana UI opened locally at http://localhost:3000
- Prometheus query: up
- Existing monitoring release reused to avoid duplicate resource usage

## Key learning
Prometheus collects and stores time-series metrics. Grafana visualizes those metrics through dashboards and panels.
