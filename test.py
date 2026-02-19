# AutoDeploy – CI/CD Quality Gate (PASS Scenario)

service_name = "Payment-Service"

# -------- Quality Metrics --------
unit_tests_passed = True
test_coverage = 85          # % (above threshold)
critical_bugs = 0           # no blocker bugs
response_time_ms = 320      # within SLA (ms)

print(f"Starting CI pipeline for: {service_name}")

# -------- Quality Gates --------
if not unit_tests_passed:
    raise Exception("Quality Gate Failed: Unit tests failed")

if test_coverage < 70:
    raise Exception("Quality Gate Failed: Test coverage below threshold")

if critical_bugs > 0:
    raise Exception("Quality Gate Failed: Critical production bug detected")

if response_time_ms > 500:
    raise Exception("Quality Gate Failed: Performance SLA violation")

print("Pipeline passed – Ready for deployment")
