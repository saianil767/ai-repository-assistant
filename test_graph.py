from backend.graph import graph

result = graph.invoke(
    {
        "question": "What does this repository do?"
    }
)

print(result)