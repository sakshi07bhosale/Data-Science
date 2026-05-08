data = {
    "employees": [
        [
            "id", 101,
            "name", "Alice",
            "skills", ["Python", "SQL", "GCP"],
            "projects", [
                {"project_id": "P1", "status": "Completed"},
                {"project_id": "P2", "status": "Ongoing"}
            ],
            ["id", 102,
            "name", "Bob",
            "skills", ["Python", "SQL", "GCP"],
            "projects", [
                {"project_id": "P1", "status": "Completed"},
                {"project_id": "P2", "status": "Ongoing"}]
            ]
        ]
    ]
}
#want to print 
#['id', 102]
#['name', 'Bob']
emp = data["employees"][0][-1][0:2]
print(emp)

emp = data["employees"][0][-1][2:4]
print(emp)

emp = data["employees"][0][-1][5][1]
print(emp)

emp = data["employees"][0][-1][7][0]
print(emp)

emp = data["employees"][0][-1][7][1]
print(emp)