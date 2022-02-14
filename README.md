![Python tests](https://github.com/raditya3/stock_screener/actions/workflows/python-app.yml/badge.svg?event=push)

# Stock screener
For stocks listed in Nifty 500 index.

This is a hobby project based on [lseffer/stock_screener](https://github.com/lseffer/stock_screener)

__Loosely based on:__

Piotroski F-Score - https://en.wikipedia.org/wiki/Piotroski_F-Score

Magic Formula -	https://en.wikipedia.org/wiki/Magic_formula_investing

NCAV - Net Current Asset Value - https://www.oldschoolvalue.com/blog/investing-strategy/backtest-graham-nnwc-ncav-screen/

## Architecture

This stock screener consists of 3 services

* Postgres database
* Worker service scheduling and executing jobs that fetch the data about the stocks and stores that in the database
* Web server for serving a front end with a login portal

  * Flask app served by gunicorn
  * Configured for nginx

## Usage:
* Install Docker and Docker-compose
* run the `make run` target
* Go to `localhost:5000` and login with credentials found in `dev-vars.env`
  * For a production setup use the `make run_prod` target with your own secret `prod-vars.env`

## TO DO:
* Add more screening methods
* Add more tests
* Possibly refactor the ETL job scripts
* Add a job for sending same data to Google Sheets (like in previous version)
