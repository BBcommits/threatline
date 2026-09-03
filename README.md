# threatline

A retrieval-grounded threat modeller for LLM applications.

## What it does

Describe an LLM application — its system prompt, the tools it can call, the
data it touches — and threatline returns a structured threat model: which
OWASP Top 10 for LLM Applications (2026) risks apply, which MITRE ATLAS
techniques map to them, and concrete attack strings to test it against.
Every finding cites the source passage it came from.

## Status

In development. Started September 2026.

## Why this exists

Most LLM security guidance is a taxonomy you read. This turns it into
something you can run against a specific application.