from typing import TypedDict

from langgraph.graph import StateGraph
from langgraph.graph import END

from backend.agents.router_agent import route_question


class GraphState(TypedDict):

    question: str

    route: str

    answer: str


def router_node(state):

    route = route_question(
        state["question"]
    )

    return {
        "route": route
    }


workflow = StateGraph(GraphState)

workflow.add_node(
    "router",
    router_node
)

workflow.set_entry_point(
    "router"
)

workflow.add_edge(
    "router",
    END
)

graph = workflow.compile()