# Flask React App - using React CDN (Version 1.0) with FASTAPI
To understand the basics of React I have simply placed CDN links on the HTML page and routing it through a Flask Route and using Blueprints and Flask-Assets to compile assets and serve it on the frontend

## Setting up FAST API in Flask
Integrating FASTAPI to handle REST API development with out of the box documentation of the APIs on the backend with Flask's expansive and extensible tooling to handle the WSGI aspects of the app.
1. Install dependencies using the pipenv command
```
pipenv install fastapi uvicorn python-multipart jinja2
```

2. Import uvicorn in ``wsgi.py`` and use as below
```
if __name__ == "__main__":
    uvicorn.run(app)
```

3. Import FastAPI modules in ``__init__.py``
> Initialize FastAPI app and mount it the flaskapp to FastAPI using the ``mount() and WSGIMiddleware()`` methods within the Flaskapp app_context function
```
app = FastAPI()
flaskapp = Flask(__name__,instance_relative_config=False)

with flaskapp.app_context():
    app.mount("/vf", WSGIMiddleware(flaskapp))
```

4. Modularized build with FastAPI Routers 
> Akin to Flask Blueprint, FastAPI has Routers which you can use to modularize your build of the app. Under the routers folder you can create [several modules](https://fastapi.tiangolo.com/tutorial/bigger-applications/) to the FastAPI app.
```
app.include_router(engine.router)
```
5. Run the uvicorn command 
> You can access the Flask routes form ``/vf/flask_route`` endpoint and ``/FastAPI_endpoint`` for FastAPI routes
``` 
 uvicorn wsgi:app
```
6. Connect FastAPI to its own SQL Database
> Connect to MySQL database using SQLAlchemy ```create_engine()``` and ```connect()``` methods
```
# Connector for FastAPI to MySQL
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

conn_db = engine.connect()
```
> To carry out queries from the MySQL database you can use the ```execute()``` method which we can get the test_user details from the User table for data that is posted to database in Flask
```
conn_db.execute("SELECT * FROM user;").fetchall()
```
```
{
    "data key": [
                    {
                        "id": 3,
                        "username": "test",
                        "email": "test@email",
                        "created": "2022-08-04T22:22:24",
                        "bio": "This is a test user",
                        "admin": 0
                    }
            ]
}
```
> For data handling in FastAPI routers can used to query and post data to MySQL database using FastAPI models, schema and routes 
```
# Data posted to MySQL from FastAPI
@router.post("/post_items/", response_model=schemas.Item)
def create_item(
    item: schemas.ItemCreate, db: Session = Depends(db_router.get_db)
    ):
    return db_router.create_item(db=db, item=item)

# Get Data from MySQL from FastAPI
@router.get("/get_items", response_model=list[schemas.Item])
def read_item(
    skip: int = 0, limit: int = 100, db: Session = Depends(db_router.get_db)
    ):
    items = db_router.get_items(db, skip=skip, limit=limit)
    return items
```
Reads:
1. [FastAPI vs Flask](https://www.netguru.com/blog/python-flask-versus-fastapi#:~:text=When%20you're%20building%20APIs,tooling%20built%20around%20that%20framework.)
2. [Side by Side implementation of FastAPI and Flask](https://testdriven.io/blog/moving-from-flask-to-fastapi/#additional-features)
3. [FastAPI with Flask](https://www.youtube.com/watch?v=KKT6VpTfk_0)
4. [FastAPI with Relational Databases](https://www.youtube.com/watch?v=4Zy90rd0bkU)