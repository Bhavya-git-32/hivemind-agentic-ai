from src.agents.coordinator_agent import CoordinatorAgent


def test_coordinator():

    coordinator = CoordinatorAgent()

    result = coordinator.process_query(
        "Claims API Architecture"
    )

    assert "results" in result

    assert result["agents_consulted"] >= 1