"""
Competition System Demo Script

This script demonstrates the basic usage of the competition system.
"""
import os
import sys
from pathlib import Path

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent.parent))

from src.competition import CompetitionManager
from src.mirage.engines.base import EngineV1


def main():
    """Run a demonstration of the competition system."""
    print("=== XPECTO Epidemic 2.0 Competition Demo ===\n")
    
    # Create the epidemic engine
    try:
        engine = EngineV1()
        print("Epidemic engine initialized!")
    except Exception as e:
        print(f"Failed to initialize engine: {e}")
        print("Using placeholder engine for demo purposes.")
        engine = None
    
    # Create competition manager
    competition = CompetitionManager(data_dir="data", engine=engine)
    print("Competition manager initialized!\n")
    
    # Register a demo player
    player_name = input("Enter your name (default: Demo Player): ") or "Demo Player"
    player_id = competition.setup_player(name=player_name)
    print(f"Player registered with ID: {player_id}\n")
    
    # List available scenarios
    print("Available scenarios:")
    scenarios = competition.list_available_scenarios()
    
    # Select a scenario
    print("\nSetting up standard scenario...")
    competition.set_scenario("standard")
    competition.display_scenario_details()
    competition.setup_simulation()
    
    # Define example interventions
    print("\nDefining example interventions...")
    
    def example_intervention(engine):
        """Example intervention function."""
        print("Applying example intervention")
    
    # Run in practice mode
    print("\nRunning simulation in practice mode...")
    competition.toggle_practice_mode(is_practice=True)
    
    # Run the simulation
    try:
        results = competition.run_simulation(steps=50, interventions=[example_intervention])
        print("Simulation completed successfully!")
        
        # Display score
        print("\nScore breakdown:")
        competition.display_score(results)
        
        # Display attempts
        print("\nPlayer attempts:")
        competition.display_player_attempts()
    except Exception as e:
        print(f"Error during simulation: {e}")
    
    # Submit strategy document
    print("\nSubmitting strategy document...")
    strategy_doc = "This is an example strategy focusing on early interventions."
    competition.submit_strategy_document(strategy_doc=strategy_doc)
    
    # Display leaderboard
    print("\nCurrent leaderboard:")
    competition.display_leaderboard()
    
    print("\n=== Demo completed successfully! ===")
    print("You can now use this competition system in your own applications.")


if __name__ == "__main__":
    main()