# GOSH-FHIRworks-2020-APDV

This is a Aging Population Data Visualisation tool. This script visualises data from the aging population (ages 65+) within the GOSH FHIR database. The tool retrieves the data from the database, cleans and filters the data and graphs observation data against age. 

Observation data can be any of the following:
- Heart rate
- Respiratory rate
- Body Mass Index
- Tobacco smoking status NHIS
- Pain severity - 0-10 verbal numeric rating [Score] - Reported
- Systolic Blood Pressure
- Body Height
- Erythrocytes [#/volume] in Blood by Automated count
- Hemoglobin [Mass/volume] in Blood
- MCH [Entitic mass] by Automated count
- Diastolic Blood Pressure
- Blood Pressure

# API
A public GET API to generate graph (image binary data returned) based on observation request.
Query via http://fhir.compositegrid.com:8080/graph
Parameter: observation 

**NOTE: A FHIR caching server (from Greenfrogs) is currently hosted on my private server, which will run out of credit in 41 days (7 May 2020).**

# Website Demo
Click here for a demo: https://gosh-fhir.azurewebsites.net/
Request may take about 5-10 minutes.
