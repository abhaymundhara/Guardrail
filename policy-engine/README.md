GuardRail Policy Engine

AI policy enforcement layer that scans LLM outputs in real-time against company rules

Architecture

AI Agent to Policy Engine to Production

Features

Real-time policy checking via REST API
Template policies for common violations
Configurable confidence scoring
Extensible policy framework

Policies

PII Leakage Detection blocks SSNs credit cards emails phone numbers

Profanity Filter blocks outputs with banned words

Unauthorized Refund Protection blocks refund offers exceeding limits

Usage

Start the server by installing requirements and running main

Check a policy using curl POST to localhost:8000/check

Adding New Policies

Create a new policy class extending the base