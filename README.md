# OPAL Research

An [OPAL](http://opal.openhealthcare.org.uk) plugin for running research studies.

Features fine grained access control (Clinical Lead, Researcher, Research Nurse, Lab technician roles 
out of the box), with blinding, audit trail, query interface and
data export to CSV for subsequent data analysis.

Custom data collection per study as well as the ability to 'import' patient / episode details from
existing in/outpatient teams.

Supports many concurrent, single or multi-site studies.


## Installation

Add to your implementation's INSTALLED_APPLICATIONS.

Run

    $ python manage.py migrate

Create the column schemas for your roles.

Add the settings so that you point at these :

LIST_SCHEMA_RESEARCH_PRACTITIONER
LIST_SCHEMA_SCIENTIST

You will need to create any models specific to your study (For data collection) in your instance.
