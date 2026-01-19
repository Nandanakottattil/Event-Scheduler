from event_crew.crew import EventCrew

def run():
    """
    Run the crew with user-provided inputs.
    """
    inputs = {
        "events": [
            {
                "name": "Hackathon",
                "duration": "6 hours",
                "priority": "High",
                "preferred_time": "Morning",
                "required_volunteers": 10
            },
            {
                "name": "Paper Presentation",
                "duration": "2 hours",
                "priority": "Medium",
                "preferred_time": "Afternoon",
                "required_volunteers": 4
            }
        ],

        "venues": [
            {
                "name": "Main Auditorium",
                "capacity": 500,
                "facilities": ["Projector", "Sound"],
                "available_slots": ["Morning", "Afternoon"]
            },
            {
                "name": "Seminar Hall",
                "capacity": 120,
                "facilities": ["Projector"],
                "available_slots": ["Afternoon"]
            }
        ],

        "volunteers": [
            {
                "name": "Anu",
                "skills": ["Logistics"],
                "availability": ["Morning"]
            },
            {
                "name": "Rahul",
                "skills": ["Technical Support"],
                "availability": ["Afternoon"]
            }
        ]
    }

    EventCrew().crew().kickoff(inputs=inputs)