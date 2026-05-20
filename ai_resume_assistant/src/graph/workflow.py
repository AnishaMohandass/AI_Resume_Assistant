# This file controls which agent should run based on the user query using LangGraph

# LangGraph orchestrates multi-agent workflows by routing user queries 
# through specialized nodes using conditional graph-based execution

# orchestration - it is the automated coordination & management of complex computer systems, applications, & services

# User Query
#   ↓
# Which Agent Should Handle It?
#   ↓
# Execute Agent
#   ↓
# Return Output

from langgraph.graph import StateGraph, END
# StateGraph → creates the workflow graph
# END → tells LangGraph where execution should stop

from src.agents.skill_agent import skill_agent
from src.agents.ats_agent import ats_agent
from src.agents.improve_agent import improve_agent

# State → shared memory/data passed between nodes
# Eg.) {"query": "Give ATS score"}


# This is the main function that creates the complete LangGraph workflow
# retriever → retrieves resume chunks from VectorDB
# llm → language model
def build_graph(retriever, llm):

    # Creates a workflow graph
    # dict means the graph state will be stored as Python dictionary
    graph = StateGraph(dict)


    # -------------------------------
    # Nodes
    # -------------------------------

    # Creates a node/function for skill analysis
    def skills_node(state):

        # The node calls the Skill agent
        # It sends: user query, retriever, LLM
        output = skill_agent(
            state["query"],
            retriever,
            llm
        )

        # This updates the graph state
        # **state → Keep old data
        # Returns updated state
        return {
            **state,
            "output": output
        }

    # Creates ATS analysis node
    def ats_node(state):

        # The node calls the ATS agent
        # It sends: user query, retriever, LLM
        output = ats_agent(
            state["query"],
            retriever,
            llm
        )

        # Returns updated state
        return {
            **state,
            "output": output
        }

    # Creates resume improvement node
    def improve_node(state):

        # The node calls the Improve agent
        # It sends: user query, retriever, LLM
        output = improve_agent(
            state["query"],
            retriever,
            llm
        )

        # Returns updated state
        return {
            **state,
            "output": output
        }

    # -------------------------------
    # Add Nodes
    # -------------------------------

    # Registers nodes into the graph
    graph.add_node("skills", skills_node)
    graph.add_node("ats", ats_node)
    graph.add_node("improve", improve_node)

    # -------------------------------
    # Router
    # -------------------------------

    # Creates decision-making function
    # This decides which agent should run
    def router(state):

        # Converts query to lowercase
        query = state["query"].lower() 

        # If query contains skills, go to skills node
        if "skill" in query:
            return "skills"

        # If query contains improve, go to improve node
        elif "improve" in query:
            return "improve"

        # else go to ats node
        else:
            return "ats"

    # -------------------------------
    # Conditional Entry
    # -------------------------------

    # Sets router as the starting point of graph
    # If router returns "skills", skills node is executed
    # If router returns "ats", ats node is executed
    # If router returns "improve", improve node is executed
    graph.set_conditional_entry_point(
        router,
        {
            "skills": "skills",
            "ats": "ats",
            "improve": "improve"
        }
    )

    # -------------------------------
    # END GRAPH
    # -------------------------------

    # After node execution, stop graph execution
    # Without this, infinite recursion can happen
    graph.add_edge("skills", END)
    graph.add_edge("ats", END)
    graph.add_edge("improve", END)

    # -------------------------------
    # Compile
    # -------------------------------

    # Converts graph definition into executable workflow
    app = graph.compile()

    # Returns executable LangGraph app
    return app