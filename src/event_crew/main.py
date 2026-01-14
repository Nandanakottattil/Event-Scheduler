#!/usr/bin/env python
import sys
import warnings
from datetime import datetime

from event_crew.crew import EventManagementCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the Event Management crew.
    """
    inputs = {
        "festival_name": "Annual Tech Fest 2026",
        "events": [
            {
                "event_name": "Hackathon",
                "duration": "8 hours",
                "priority": "High",
                "required_volunteers": 10,
                "preferred_time": "Day 1 Morning"
            },
            {
                "event_name": "Paper Presentation",
                "duration": "3 hours",
                "priority": "Medium",
                "required_volunteers": 5,
                "preferred_time": "Day 1 Afternoon"
            }
        ],
        "venues": [
            {
                "venue_name": "Main Auditorium",
                "capacity": 500,
                "availability": ["Day 1", "Day 2"]
            },
            {
                "venue_name": "Seminar Hall A",
                "capacity": 150,
                "availability": ["Day 1"]
            }
        ],
        "volunteers": [
            {
                "name": "Volunteer A",
                "skills": ["Coordination", "Technical Support"],
                "availability": ["Day 1"]
            },
            {
                "name": "Volunteer B",
                "skills": ["Registration"],
                "availability": ["Day 1", "Day 2"]
            }
        ]
    }

    try:
        EventManagementCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "festival_type": "College Technical Festival",
        "current_year": str(datetime.now().year)
    }

    try:
        EventManagementCrew().crew().train(
            n_iterations=int(sys.argv[1]),
            filename=sys.argv[2],
            inputs=inputs
        )
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        EventManagementCrew().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and return the results.
    """
    inputs = {
        "festival_type": "College Technical Festival",
        "current_year": str(datetime.now().year)
    }

    try:
        EventManagementCrew().crew().test(
            n_iterations=int(sys.argv[1]),
            eval_llm=sys.argv[2],
            inputs=inputs
        )
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
