# Cloud Catalog
This is a Django App written for the Hybrid Cloud Team to catalog AMIS. Functionality and development is ongoing. It currently contains one app, called ami_info. This shows current AMIs and provides a link to click in to get details.


We are live:
http://13.56.161.184/

To run the server:
```
$ cd cloud/catalog/ami_info
$ python manage.py runserver 8000
```

To use webpage, direct to:

 `http://127.0.0.1:8000/ami_info/`



### Mike S roadmap:
Short term:
* ~~Details page for each AMI~~ 8/16/17
* ~~Allow creation of AMI manually by hand(think blog style)~~ 8/16/17
* ~~Add end of life column information~~ 8/16/17
* ~~Implement update model, many to one with AMI model~~ 8/23/17
* ~~Fix Operating System nav bar drop down to sort~~ 8/17/17
* ~~Implement search bar~~ 8/17/17
* ~~Make sure no two ami id are same of query will fail~~ 8/24/17
* ~~Figure out how to only link to Bootstrap once, not every file(static directory?)~~ 8/24/17 (Can move to static files...not worth doing presently with 2 pages)
* ~~Implement end of life data, test to make sure it is in future(WRITE TESTS!!!)~~ 8/24/17
* ~~If EOL within certain time frame, tag AMI (Color coding with bootstrap alert)~~ 8/16/17
* ~~ ignore~~ 8/18/17
* ~~Real README~~ 8/18/17
* ~~Rewrite the view so that it uses context the 'best practice' way~~ 8/18/17
* ~~Move POST to create new AMI to new funct~~ 8/23/17
* ~~Move application to be hosted on AWS(Nginx, gunicorn)~~ 8/22/17


Long(er) term:
* ~~Auto populate when an AMI is built from Jenkins pipeline~~ 8/23/17
* ~~Figure out versioning strategy...maybe we only show 5 base AMIs and make them be updated? By this I mean when the Jenkins pipeline sends our Django app a POST, we make it specify the OS and then only maintain a log for those 5?~~ 8/23/17
* Implement versioning strategy
* ~~Implement change log for AMI versions~~ 8/23/17
* Decide what information is useful to have about AMI
* By utilizing tagging, possibly let user sort by their Application
* Use default Django templating?
* Off of sqlite, onto RDS
* Implement views testing and testing for Ami, Update models
* Add auth token for POST
