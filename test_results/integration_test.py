
import sys
import os
from pathlib import Path

# Add project root to path to ensure imports work
sys.path.append(str(Path(__file__).parent.parent))

from src.competition import CompetitionManager
from src.competition.testing.enhanced_engine import EnhancedEngine

# Create an EnhancedEngine instance
engine = EnhancedEngine(seed=42)

# Create a CompetitionManager with the EnhancedEngine
competition = CompetitionManager(data_dir="integration_test_data", engine=engine)

# Test setup_player
player_id = competition.setup_player(name="Integration Test Player")
print(f"Player registered: {player_id}")

# Toggle practice mode
competition.toggle_practice_mode(is_practice=True)
print("Practice mode enabled")

# Set scenario
competition.set_scenario("standard")
print("Scenario set to: standard")

# Set up simulation
competition.setup_simulation()
print("Simulation set up successfully")

# Define a simple intervention strategy
def test_strategy(engine):
    engine.set_lockdown_level(0.5)
    engine.allocate_resources('healthcare', 300)
    engine.allocate_resources('economic', 300)
    engine.allocate_resources('research', 200)
    engine.restrict_travel(True)
    
    def monitor_and_respond(step, state):
        infection_rate = state.population.infected / state.population.total
        if infection_rate > 0.1:
            engine.set_lockdown_level(0.7)
            engine.allocate_resources('healthcare', 50)
        else:
            engine.set_lockdown_level(0.3)
            engine.allocate_resources('economic', 50)
    
    engine.register_step_callback(monitor_and_respond)

# Run simulation
results = competition.run_simulation(steps=100, interventions=[test_strategy])
print("Simulation completed successfully")

# Display the results
competition.display_score(results)

print("\nIntegration Test Passed: EnhancedEngine works with CompetitionManager")
