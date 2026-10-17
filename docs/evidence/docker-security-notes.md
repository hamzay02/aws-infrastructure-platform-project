# Docker Image Security Review

## Image scanned

* Image: `aws-infrastructure-platform:1.4`
* Tool: Docker Scout
* Packages indexed: 134

## Scan results

* Critical vulnerabilities: 0
* High vulnerabilities: 1
* Medium vulnerabilities: 6
* Low vulnerabilities: 27
* Total reported vulnerabilities: 34

## Findings and follow-up

Docker Scout identified vulnerabilities in the image's software components. The high-severity finding reported for zlib had no fixed version listed in the scan output. Additional findings included pip and operating-system packages.

These results require review; the absence of critical findings does not mean the image is vulnerability-free. Findings should be reassessed as updated base images and package fixes become available.

## Container hardening

* Used a multi-stage Docker build.
* Configured the application to run as a non-root user.
* Tested the API's home, health, and version endpoints locally.

## Evidence

The full scan output is saved in `docker-scout-1.4.txt`.

## Scope

This review was performed locally. The application has not yet been deployed to AWS.
