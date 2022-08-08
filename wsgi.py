from FlaskReact import create_app
import uvicorn

# Imports and starts App
app = create_app()

if __name__ == "__main__":
    uvicorn.run(app)
