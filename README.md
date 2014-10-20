# opal-research

Research study plugin for OPAL


## Installation

Add to your implementation's INSTALLED_APPLICATIONS.

Run

    $ python manage.py migrate

Create the column schemas for your roles.

Add the settings so that you point at these :

LIST_SCHEMA_RESEARCH_PRACTITIONER
LIST_SCHEMA_SCIENTIST

You will need to create any models specific to your study (For data collection) in your instance.
