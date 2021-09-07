# Spashzone
Industry Dive's onboarding tool for new software engineers

## Requirements
* Python 3
* Pipenv or other python virtual environment package

## Install
Using [pipenv](https://pipenv.pypa.io/en/latest/):

Install an environment using python 3

`pipenv install`
or
`pipenv install --python your-path-to-python3`

SSH into your environment
`pipenv shell`

If you do not want to use pipenv, you can install requirements for your environment found in the `requirements.txt` file.

## Usage
NOTE: This repository uses a custom manager based on [Django Sites Framework](https://docs.djangoproject.com/en/3.2/ref/contrib/sites/), which allows us to seperate content both in the CMS and on the front end by the site that is currently running. You will need to select a dive site to run (these are in `settings/` and named like `<domain>_settings.py`). 

For example, to run the app as Retail Dive, do:

`python manage.py runserver --settings=settings.retail_settings`

Navigate in your browser to the wavepool homepage at `http://127.0.0.1:8000/` and notice that the navigation bar says "Retail Dive".

Navigate to the Admin CMS (at `http://127.0.0.1:8000/admin/`) and log in using the username `divecandidate` and password `divecandidatetest`.

Notice that the Header bar says "Retail Dive Admin".

Click on the "News Posts" link under the "NEWS" section and look at the titles of the news posts listed. Now, stop the server and restart it, this time as Supply Chain Dive (`python manage.py runserver --settings=settings.supplychain_settings`).

Notice that the header is now "Supply Chain Dive Admin" and there are different news posts listed.

This will be important to keep in mind as you go through the onboarding prompts.

## Explore
Splashzone comes out of the box with a few "Dive Sites" already set up for you. With splashzone running using one of the site settings (Retail Dive is recommended as it has the most content), you can see that there is a front page, news post detail pages, and an archive page.

Each of these pages has a right sidebar that contains an ad and a signup box. There is also a signup box near the footer of each page. These don't actually do anything.

The instructions page is where you will find the onboarding prompts and instructions for how to complete them.


## Onboarding Prompts
With splashzone running locally, navigate to the instructions page (`http://127.0.0.1:8000/instructions/`)


Each prompt includes
- Objectives, which outline what you should get out of going through the exercise
- Description, usually in the form of a [user story](atlassian.com/agile/project-management/user-stories)
- [Acceptance criteria](https://www.productplan.com/glossary/acceptance-criteria/), which provides additional context not included in the user story
- Scenarios, usually in [Gherkin](https://docs.behat.org/en/v2.5/guides/1.gherkin.html#gherkin-syntax) format, which describe, in detail, the expected behavior of a feature you will build (see also: [Behaviour Driven Development ](https://www.agilealliance.org/glossary/bdd/))
