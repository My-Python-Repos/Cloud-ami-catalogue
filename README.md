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



### Future Road Map


Long(er) term:
* Implement versioning strategy
* Decide what information is useful to have about AMI
* By utilizing tagging, possibly let user sort by their Application
* Use default Django templating?
* Off of sqlite, onto RDS
* Implement views testing and testing for Ami, Update models
* Add auth token for POST
