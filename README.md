# Policy Gated Runtime

Small, explicit runtime state machine for three required gates. Any failed gate blocks the run; deployment is allowed only after all approvals.

Run `python3 main.py`. The code is intentionally deterministic. A production adapter would persist transitions transactionally, bind approvers to identities, and verify signed evidence.
