"""class EmployeePerformanceExpertSystem:
    def __init__(self, efficiency, punctuality, teamwork, goal_achievement):
        self.efficiency = efficiency
        self.punctuality = punctuality
        self.teamwork = teamwork
        self.goal_achievement = goal_achievement

    def evaluate_performance(self):
        score = (
            (self.efficiency * 0.4) +
            (self.punctuality * 0.2) +
            (self.teamwork * 0.2) +
            (self.goal_achievement * 0.2)
        )

        if score >= 90:
            return "Outstanding"
        elif score >= 75:
            return "Good"
        elif score >= 50:
            return "Average"
        else:
            return "Needs Improvement"

def main():
    print("Enter Employee Ratings (0-100):")
    try:
        efficiency = int(input("Efficiency: "))
        punctuality = int(input("Punctuality: "))
        teamwork = int(input("Teamwork: "))
        goal_achievement = int(input("Goal Achievement: "))

        # Optional: Input validation
        for val in [efficiency, punctuality, teamwork, goal_achievement]:
            if not (0 <= val <= 100):
                print("All ratings must be between 0 and 100.")
                return

        expert_system = EmployeePerformanceExpertSystem(
            efficiency, punctuality, teamwork, goal_achievement
        )
        result = expert_system.evaluate_performance()
        print(f"Employee Performance Evaluation: {result}")
    except ValueError:
        print("Please enter valid integer values for all ratings.")

if __name__ == "__main__":
    main()

Enter Employee Ratings (0-100):
Efficiency: 85
Punctuality: 90
Teamwork: 80
Goal Achievement: 88
Employee Performance Evaluation: Good
"""

class EmployeePerformanceExpertSystem:
    def __init__(self, efficiency, punctuality, teamwork, goal_achievement):
        self.efficiency = efficiency
        self.punctuality = punctuality
        self.teamwork = teamwork
        self.goal_achievement = goal_achievement

    def evaluate_performance(self):
        score = (
            (self.efficiency * 0.4) +
            (self.punctuality * 0.2) +
            (self.teamwork * 0.2) +
            (self.goal_achievement * 0.2)
        )
        if score >= 90:
            return "Outstanding"
        elif score >= 75:
            return "Good"
        elif score >= 50:
            return "Average"
        else:
            return "Needs Improvement"

def main():
    print("Enter Employee Ratings (0-100):")
    efficiency = int(input("Efficiency: "))
    punctuality = int(input("Punctuality: "))
    teamwork = int(input("Teamwork: "))
    goal_achievement = int(input("Goal Achievement: "))

    expert_system = EmployeePerformanceExpertSystem(
        efficiency, punctuality, teamwork, goal_achievement
    )
    result = expert_system.evaluate_performance()
    print(f"Employee Performance Evaluation: {result}")

if __name__ == "__main__":
    main()
