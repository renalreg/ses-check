# SES Check

Web utility to check NHS Secure Email Standard reccommendations

## How it works

A nightly GitHub Actions workflow runs a Python script which downloads the [list of DCB1596 accredited organisations](https://digital.nhs.uk/services/nhsmail/the-secure-email-standard), and converts it into a JSON file.

A small static HTML file is served by GitHub Pages, which parses this JSON file and uses it to determine the current NHS reccommendation for sending emails between any two email addresses.

## Caution

This utility currently relies on my best understanding of the NHS Digital Secure Email Standard, and may not be accurate.

The tool will be updated as our understanding of the standard develops.
