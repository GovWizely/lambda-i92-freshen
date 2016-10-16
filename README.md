# Lambda I-92 Freshener

This project provides an AWS Lambda that freshens i92 data source when new CSV available in i92 S3 bucket

## Prerequisites

Follow instructions from [python-lambda](https://github.com/nficano/python-lambda) to ensure your basic development environment is ready,
including:

* Python
* Pip
* Virtualenv
* Virtualenvwrapper
* AWS credentials

Then make sure you have your [Trade.gov API Admin Key](https://api.trade.gov) handy. Your need to be authorized as an admin in order to freshen the data.

## Getting Started

	git clone git@github.com:GovWizely/lambda-i92-freshen.git
	cd lambda-i92-freshen
	mkvirtualenv -r requirements.txt lambda-i92-freshen

## Configuration

* Edit `service.py` and change the `API_KEY` to use your key
* Define AWS credentials in either `config.yaml` or in the [default] section of ~/.aws/credentials.
* Edit `config.yaml` if you want to specify a different AWS region, role, and so on.
* Make sure you do not commit the API key or AWS credentials to version control

## Invocation

	lambda invoke -v

{"success":"i92_entries:v1 API freshened"}
 
## Deploy

	lambda deploy
