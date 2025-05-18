from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
import uvicorn
from schema import schema  # Adjust based on your actual module structure
from datetime import datetime
app = FastAPI()

# Mount the GraphQL app
graphql_app = GraphQLRouter(schema, path="/graphql")

# Add it under the correct path
app.add_route("/graphql", graphql_app)

@app.get("/")
def root():
    return {"message": "Hello from FastAPI"}